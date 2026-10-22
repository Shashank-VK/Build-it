#!/usr/bin/env python3
"""Post-tool auto-formatter + AST syntax validator for written Python files.

Usage: post_tool_linter.py <filepath>
Exit 0 when clean (ruff applied if available, compile check passed).
Exit 1 with a fatal message otherwise.
"""
import py_compile
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: post_tool_linter.py <filepath>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    if path.suffix != ".py" or not path.exists():
        return 0
    if shutil.which("ruff"):
        r = subprocess.run(
            ["ruff", "check", "--fix", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if r.returncode != 0:
            print(r.stdout + r.stderr, file=sys.stderr)
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as e:
        print(f"[post-tool-linter] FATAL: syntax error in {path}: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
