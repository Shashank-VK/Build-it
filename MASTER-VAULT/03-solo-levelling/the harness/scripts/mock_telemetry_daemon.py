#!/usr/bin/env python3
"""
Mock Telemetry Daemon for Autonomous Dev Harness (GAP-TEL-01)
=============================================================
Provides a lightweight local receiver for OpenTelemetry (OTLP) traces and
Langfuse-compatible telemetry events during offline and air-gapped development.

Features:
- OTLP traces receiver on /v1/traces (default port: 4318)
- Langfuse ingestion receiver on /api/public/ingestion (default port: 3000)
- In-memory ring buffer (capped at 1000 items) + JSONL file persistence
- Real-time stdout logging: timestamp | model | tokens_used | cost_usd
- /status (GET) and /reset (POST) operational endpoints
- Zero external dependencies (Python stdlib only)
"""

import argparse
import collections
import datetime
import http.server
import json
import os
from pathlib import Path
import signal
import sys
import threading
import time
from typing import Any, Dict, List, Optional, Tuple


class TelemetryStore:
    """Thread-safe store for in-memory telemetry buffer and metrics aggregation."""

    def __init__(self, output_file: Path, max_buffer_size: int = 1000):
        self.output_file = output_file
        self.max_buffer_size = max_buffer_size
        self.lock = threading.Lock()
        self.start_time = time.time()
        self.buffer = collections.deque(maxlen=max_buffer_size)
        self.total_spans_received: int = 0
        self.total_cost_usd: float = 0.0
        self.unique_models: set = set()

    def record_span(
        self,
        raw_event: Dict[str, Any],
        source: str,
        model: str,
        tokens_used: int,
        cost_usd: float,
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Record an incoming span or event into memory and append to JSONL file."""
        if not timestamp:
            timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

        normalized_record = {
            "timestamp": timestamp,
            "source": source,
            "model": model,
            "tokens_used": tokens_used,
            "cost_usd": cost_usd,
            "raw_payload": raw_event,
        }

        with self.lock:
            self.total_spans_received += 1
            self.total_cost_usd += cost_usd
            if model and model != "unknown":
                self.unique_models.add(model)
            self.buffer.append(normalized_record)

            # Persist to disk
            self._write_jsonl(normalized_record)

        # Log to stdout: timestamp | model | tokens_used | cost_usd
        tokens_str = f"{tokens_used} tokens" if tokens_used else "0 tokens"
        cost_str = f"${cost_usd:.6f}" if cost_usd else "$0.000000"
        print(f"{timestamp} | {model} | {tokens_str} | {cost_str}")
        sys.stdout.flush()

        return normalized_record

    def _write_jsonl(self, record: Dict[str, Any]) -> None:
        """Append record to the target JSONL file safely."""
        try:
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.output_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(record, default=str) + "\n")
        except Exception as e:
            print(f"[ERROR] Failed writing to {self.output_file}: {e}", file=sys.stderr)

    def get_status(self) -> Dict[str, Any]:
        """Return runtime status and metrics summary."""
        with self.lock:
            uptime = round(time.time() - self.start_time, 2)
            return {
                "status": "ok",
                "uptime_seconds": uptime,
                "total_spans_received": self.total_spans_received,
                "total_cost_usd": round(self.total_cost_usd, 6),
                "unique_model_names": sorted(list(self.unique_models)),
                "buffered_spans_count": len(self.buffer),
                "max_buffer_capacity": self.max_buffer_size,
                "output_file": str(self.output_file),
            }

    def reset(self) -> Dict[str, Any]:
        """Clear the in-memory buffer and reset counters."""
        with self.lock:
            self.buffer.clear()
            self.total_spans_received = 0
            self.total_cost_usd = 0.0
            self.unique_models.clear()
            return {
                "status": "ok",
                "message": "In-memory telemetry buffer and metrics reset successfully",
                "total_spans_received": 0,
                "total_cost_usd": 0.0,
                "unique_model_names": [],
            }


def _parse_otlp_attributes(attrs_raw: Any) -> Dict[str, Any]:
    """Parse OTLP key-value attribute array or dict."""
    if isinstance(attrs_raw, dict):
        return attrs_raw
    parsed = {}
    if isinstance(attrs_raw, list):
        for item in attrs_raw:
            if isinstance(item, dict) and "key" in item:
                val = item.get("value")
                if isinstance(val, dict):
                    v = next(iter(val.values())) if val else None
                    parsed[item["key"]] = v
                else:
                    parsed[item["key"]] = val
    return parsed


def _extract_otlp_span_info(span: Dict[str, Any]) -> Tuple[str, int, float, str]:
    """Extract model, tokens, cost, and timestamp from an OTLP span dict."""
    attrs = _parse_otlp_attributes(span.get("attributes", []))

    # Model extraction
    model = (
        attrs.get("gen_ai.request.model")
        or attrs.get("gen_ai.response.model")
        or attrs.get("llm.model")
        or attrs.get("model")
        or attrs.get("model_name")
        or span.get("name")
        or "otlp-span"
    )

    # Tokens extraction
    tokens = 0
    if "gen_ai.usage.total_tokens" in attrs:
        try:
            tokens = int(attrs["gen_ai.usage.total_tokens"])
        except (ValueError, TypeError):
            pass
    elif "gen_ai.usage.prompt_tokens" in attrs or "gen_ai.usage.completion_tokens" in attrs:
        p = attrs.get("gen_ai.usage.prompt_tokens", 0) or 0
        c = attrs.get("gen_ai.usage.completion_tokens", 0) or 0
        try:
            tokens = int(p) + int(c)
        except (ValueError, TypeError):
            pass
    elif "llm.usage.total_tokens" in attrs:
        try:
            tokens = int(attrs["llm.usage.total_tokens"])
        except (ValueError, TypeError):
            pass

    # Cost extraction
    cost = 0.0
    cost_candidates = [
        attrs.get("gen_ai.cost"),
        attrs.get("cost"),
        attrs.get("estimated_cost"),
        span.get("cost"),
    ]
    for c in cost_candidates:
        if c is not None:
            try:
                cost = float(c)
                break
            except (ValueError, TypeError):
                continue

    # Timestamp extraction
    nano_time = span.get("startTimeUnixNano")
    if nano_time:
        try:
            sec = int(nano_time) / 1e9
            ts = datetime.datetime.fromtimestamp(sec, tz=datetime.timezone.utc).isoformat()
        except Exception:
            ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    else:
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

    return str(model), tokens, cost, ts


def _extract_langfuse_event_info(event: Dict[str, Any]) -> Tuple[str, int, float, str]:
    """Extract model, tokens, cost, and timestamp from a Langfuse event dict."""
    body = event.get("body") if isinstance(event.get("body"), dict) else event
    usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}

    # Model extraction
    model = (
        body.get("model")
        or body.get("model_name")
        or event.get("model")
        or body.get("name")
        or "langfuse-event"
    )

    # Tokens extraction
    tokens = 0
    if "total" in usage:
        try:
            tokens = int(usage["total"])
        except (ValueError, TypeError):
            pass
    elif "total_tokens" in usage:
        try:
            tokens = int(usage["total_tokens"])
        except (ValueError, TypeError):
            pass
    elif "input" in usage or "output" in usage:
        inp = usage.get("input", 0) or 0
        out = usage.get("output", 0) or 0
        try:
            tokens = int(inp) + int(out)
        except (ValueError, TypeError):
            pass
    elif "tokens_used" in body:
        try:
            tokens = int(body["tokens_used"])
        except (ValueError, TypeError):
            pass

    # Cost extraction
    cost = 0.0
    cost_candidates = [
        body.get("calculatedTotalCost"),
        body.get("estimated_cost"),
        body.get("totalCost"),
        usage.get("totalCost"),
        body.get("cost"),
        event.get("estimated_cost"),
    ]
    for c in cost_candidates:
        if c is not None:
            try:
                cost = float(c)
                break
            except (ValueError, TypeError):
                continue

    # Timestamp extraction
    ts = (
        event.get("timestamp")
        or body.get("timestamp")
        or datetime.datetime.now(datetime.timezone.utc).isoformat()
    )

    return str(model), tokens, cost, ts


class TelemetryRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler for OTLP traces, Langfuse events, /status, and /reset."""

    store: TelemetryStore

    def log_message(self, format: str, *args: Any) -> None:
        """Suppress default HTTP access logging to keep stdout clean for telemetry lines."""
        pass

    def _send_json_response(self, status_code: int, data: Dict[str, Any]) -> None:
        """Send a standard JSON response with permissive CORS headers."""
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self) -> None:
        """Handle CORS preflight requests."""
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_GET(self) -> None:
        """Handle GET requests for /status and /health."""
        path = self.path.split("?")[0].rstrip("/")
        if path == "/status":
            self._send_json_response(200, self.store.get_status())
        elif path in ("", "/health", "/healthz"):
            self._send_json_response(200, {
                "status": "healthy",
                "service": "mock-telemetry-daemon",
                "endpoints": ["/v1/traces", "/api/public/ingestion", "/status", "/reset"],
            })
        else:
            self._send_json_response(404, {
                "error": "Not Found",
                "path": self.path,
                "valid_endpoints": ["/v1/traces", "/api/public/ingestion", "/status", "/reset"],
            })

    def do_POST(self) -> None:
        """Handle POST requests for /v1/traces, /api/public/ingestion, and /reset."""
        path = self.path.split("?")[0].rstrip("/")
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            payload = json.loads(raw_body.decode("utf-8")) if raw_body else {}
        except json.JSONDecodeError:
            payload = {"raw_text": raw_body.decode("utf-8", errors="replace")}

        # 1. Reset endpoint
        if path in ("/reset", "/api/public/reset"):
            result = self.store.reset()
            self._send_json_response(200, result)
            return

        # 2. OpenTelemetry OTLP traces (/v1/traces)
        if path in ("/v1/traces", "/v1/metrics", "/v1/logs"):
            extracted_spans = []
            if isinstance(payload, dict) and "resourceSpans" in payload:
                for r_span in payload.get("resourceSpans", []):
                    for s_span in r_span.get("scopeSpans", []):
                        for span in s_span.get("spans", []):
                            model, tokens, cost, ts = _extract_otlp_span_info(span)
                            rec = self.store.record_span(
                                raw_event=span,
                                source="otlp",
                                model=model,
                                tokens_used=tokens,
                                cost_usd=cost,
                                timestamp=ts,
                            )
                            extracted_spans.append(rec)
            else:
                # Handle single span or flat dict
                model, tokens, cost, ts = _extract_otlp_span_info(payload if isinstance(payload, dict) else {})
                rec = self.store.record_span(
                    raw_event=payload,
                    source="otlp",
                    model=model,
                    tokens_used=tokens,
                    cost_usd=cost,
                    timestamp=ts,
                )
                extracted_spans.append(rec)

            self._send_json_response(200, {
                "status": "ok",
                "spans_received": len(extracted_spans),
            })
            return

        # 3. Langfuse Ingestion (/api/public/ingestion)
        if path in ("/api/public/ingestion", "/api/public/traces", "/api/public/events"):
            events_batch: List[Dict[str, Any]] = []
            if isinstance(payload, dict) and "batch" in payload and isinstance(payload["batch"], list):
                events_batch = payload["batch"]
            elif isinstance(payload, list):
                events_batch = payload
            elif isinstance(payload, dict):
                events_batch = [payload]

            successes = []
            for item in events_batch:
                model, tokens, cost, ts = _extract_langfuse_event_info(item)
                self.store.record_span(
                    raw_event=item,
                    source="langfuse",
                    model=model,
                    tokens_used=tokens,
                    cost_usd=cost,
                    timestamp=ts,
                )
                event_id = item.get("id") if isinstance(item, dict) else str(time.time())
                successes.append({"id": event_id or "0", "status": 200})

            self._send_json_response(200, {
                "status": "success",
                "successes": successes,
            })
            return

        # Fallback for generic telemetry push
        self._send_json_response(200, {
            "status": "received",
            "path": self.path,
        })


def run_server(
    port: int = 4318,
    langfuse_port: int = 3000,
    output_file: Optional[Path] = None,
) -> None:
    """Run dual-listener HTTP server handling OTLP and Langfuse endpoints."""
    if output_file is None:
        output_file = Path("scratch/mock_telemetry.jsonl")

    store = TelemetryStore(output_file=output_file)

    class CustomHandler(TelemetryRequestHandler):
        pass

    CustomHandler.store = store

    servers: List[http.server.HTTPServer] = []

    # Server 1: Primary OTLP & Status port
    try:
        server_otlp = http.server.ThreadingHTTPServer(("", port), CustomHandler)
        servers.append(server_otlp)
    except Exception as e:
        print(f"[ERROR] Could not bind to port {port}: {e}", file=sys.stderr)
        sys.exit(1)

    # Server 2: Langfuse Ingestion port (if different from primary port)
    if langfuse_port != port:
        try:
            server_langfuse = http.server.ThreadingHTTPServer(("", langfuse_port), CustomHandler)
            servers.append(server_langfuse)
        except Exception as e:
            print(f"[WARNING] Could not bind to Langfuse port {langfuse_port}: {e}", file=sys.stderr)

    # Banner requirement
    print(
        f"Mock Telemetry Daemon running. OTLP: http://localhost:{port}/v1/traces | "
        f"Langfuse: http://localhost:{langfuse_port}/api/public/ingestion | "
        f"Status: http://localhost:{port}/status"
    )
    sys.stdout.flush()

    # Graceful shutdown handler
    shutdown_event = threading.Event()

    def handle_signal(sig, frame):
        shutdown_event.set()
        for s in servers:
            threading.Thread(target=s.shutdown).start()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Launch servers in threads
    threads = []
    for s in servers:
        t = threading.Thread(target=s.serve_forever, daemon=True)
        t.start()
        threads.append(t)

    # Wait for shutdown signal or interrupt
    try:
        while not shutdown_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        for s in servers:
            s.shutdown()
            s.server_close()
        print("\nMock Telemetry Daemon stopped cleanly.")
        sys.stdout.flush()


def main() -> None:
    """CLI entrypoint for the mock telemetry daemon."""
    parser = argparse.ArgumentParser(
        description="Mock Telemetry Daemon for OpenTelemetry and Langfuse trace collection."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=4318,
        help="Port for OpenTelemetry OTLP collector & status (default: 4318)",
    )
    parser.add_argument(
        "--langfuse-port",
        type=int,
        default=3000,
        help="Port for Langfuse ingestion endpoint (default: 3000)",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("scratch/mock_telemetry.jsonl"),
        help="Local file path for writing JSONL telemetry records (default: scratch/mock_telemetry.jsonl)",
    )

    args = parser.parse_args()
    run_server(
        port=args.port,
        langfuse_port=args.langfuse_port,
        output_file=args.output_file,
    )


if __name__ == "__main__":
    main()
