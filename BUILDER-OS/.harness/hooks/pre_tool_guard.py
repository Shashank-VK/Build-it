#!/usr/bin/env python3
"""
pre_tool_guard.py
Security guard for Solo AI Product Engineering Harness.
Runs before every tool execution. Blocks dangerous command patterns.
Version: 1.0 — See scripts/test_pre_tool_guard.py for runnable tests.
Solo AI Product Engineering System v1.0
"""

import json
import re
import sys
from pathlib import Path


def _log_warn(msg: str) -> None:
    """Fail-open warning: stderr + telemetry log, never crashes guard."""
    # Deliberate fail-open: a logging failure must NEVER crash the guard, so
    # these handlers stay broad by design. BLE001/S110 are suppressed on
    # purpose — narrowing them could let an unexpected error escape and
    # abort the guard, which is the exact failure mode this guards against.
    try:
        print(f"GUARD WARN: {msg}", file=sys.stderr)
    except Exception:  # noqa: BLE001, S110
        pass
    try:
        log_path = Path(__file__).resolve().parents[1] / "telemetry" / "guard.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(f"GUARD WARN: {msg}\n")
    except Exception:  # noqa: BLE001, S110
        pass


BLOCK_PATTERNS = [
    # Destructive rm on system paths
    (
        r"rm\s+.*(-rf?|--recursive|--force).*\s*(\/etc|\/usr|\/var|\/home|\/root|\/sys|\/proc|~\/)",
        "rm with recursive/force on critical system path"
    ),
    (r"rm\s+.*'[^']*'.*(-rf?|--recursive)", "rm with quoted path and force flag"),
    (r"rm\s+.*--\s+", "rm with -- separator (flag injection attempt)"),

    # Script injection via network fetch
    (r"curl\s+.*\|\s*(sudo\s+)?bash", "curl piped to bash (script injection)"),
    (r"curl\s+.*\|\s*(sudo\s+)?python3?", "curl piped to python (script injection)"),
    (r"wget\s+.*\|\s*(sudo\s+)?bash", "wget piped to bash (script injection)"),
    (r"wget\s+.*\|\s*(sudo\s+)?python3?", "wget piped to python (script injection)"),
    (r"curl\s+.*-fsSL", "curl with -fsSL flags (script injection)"),

    # Privilege / execution helpers
    (r"chmod\s+\+x", "chmod +x (making downloaded payload executable)"),
    (r"base64\s+.*(--decode|-d\b)", "base64 decode (obfuscated payload)"),

    # Env exfiltration
    (r"\b(env|printenv)\b", "env|printenv exfil"),

    # Hardcoded secret patterns
    (r"AKIA[0-9A-Z]{16}", "AWS access key ID detected"),
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style secret key detected"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub personal access token detected"),

    # Git force push to protected branches
    (r"git\s+push\s+.*\+\s*(main|master)", "force push to protected branch"),
    (r"git\s+push\s+.*(--force|-f)\s+.*(main|master)", "force push to protected branch"),

    # AWS STS credential patterns
    (r"ASIA[0-9A-Z]{16}", "AWS STS temporary credential key detected"),

    # Unquoted secrets in command arguments
    (
        r"(password|passwd|secret|token|api_key|apikey)\s*=\s*[A-Za-z0-9+/._-]{20,}",
        "potential unquoted secret in command argument"
    ),
]


def check_command(command: str) -> str | None:
    """Check command against block patterns. Returns block reason or None."""
    for pattern, reason in BLOCK_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return reason
    return None


def main() -> int:
    """
    Read tool invocation from stdin as JSON.
    Exit 0 = allow execution.
    Exit 1 = block execution (caller raises fatal error).
    """
    try:
        raw = sys.stdin.read()
        invocation = json.loads(raw)
        tool_name = invocation.get("tool", "")
        args = invocation.get("args", {})

        command_str = ""
        if tool_name in ("bash", "shell", "run_command", "execute"):
            command_str = str(args.get("command", args.get("cmd", "")))
        elif tool_name == "write_file":
            # content checked by post-hook secret-scan
            return 0

        if command_str:
            block_reason = check_command(command_str)
            if block_reason:
                print(f"GUARD BLOCK: {block_reason}", file=sys.stderr)
                print(f"Blocked command: {command_str[:300]}", file=sys.stderr)
                return 1

        return 0

    except json.JSONDecodeError as e:
        _log_warn(f"JSON parse failed, fail-open: {e}")
        return 0  # Allow on parse errors — don't block on guard failures
    except Exception as e:  # noqa: BLE001 - deliberate fail-open, see _log_warn
        _log_warn(f"unexpected error, fail-open: {e}")
        print(f"GUARD ERROR: {e}", file=sys.stderr)
        return 0  # Fail open on unexpected errors


if __name__ == "__main__":
    sys.exit(main())
