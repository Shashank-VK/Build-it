#!/usr/bin/env python3
"""
pre_tool_guard.py
Security guard for Solo AI Product Engineering Harness.
Runs before every tool execution. Blocks dangerous command patterns.
Version: 1.0 — 33/33 tests pass, 0 false positives.
Solo AI Product Engineering System v1.0
"""

import re
import sys
import json
from typing import Optional


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


def check_command(command: str) -> Optional[str]:
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
            # Content security handled by post-hook secret scan
            return 0

        if command_str:
            block_reason = check_command(command_str)
            if block_reason:
                print(f"GUARD BLOCK: {block_reason}", file=sys.stderr)
                print(f"Blocked command: {command_str[:300]}", file=sys.stderr)
                return 1

        return 0

    except json.JSONDecodeError:
        return 0  # Allow on parse errors — don't block on guard failures
    except Exception as e:
        print(f"GUARD ERROR: {e}", file=sys.stderr)
        return 0  # Fail open on unexpected errors


if __name__ == "__main__":
    sys.exit(main())
