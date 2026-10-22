#!/usr/bin/env python3
"""Deterministic Post-Tool Auto-Formatter & AST Syntax Validator (CAP-20, CAP-37).

Executes fast auto-formatters (Ruff / Prettier) and AST syntax diagnostics
immediately after file modification, injecting any syntax errors back to the agent.
"""
import argparse
import os
import subprocess
import sys

def lint_and_format(filepath: str) -> bool:
    if not filepath or not os.path.exists(filepath):
        return True

    ext = os.path.splitext(filepath)[1].lower()
    has_errors = False

    # Python Files
    if ext == ".py":
        # 1. Format
        try:
            subprocess.run(["ruff", "format", filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

        # 2. Syntax AST Verification
        try:
            res = subprocess.run(
                ["ruff", "check", "--select=E9,F63,F7,F82", filepath],
                capture_output=True,
                text=True
            )
            if res.returncode != 0:
                print(f"[AST SYNTAX ERROR IN {filepath}]\n{res.stdout}", file=sys.stderr)
                has_errors = True
        except FileNotFoundError:
            # Fallback to Python compiler AST check
            try:
                import py_compile
                py_compile.compile(filepath, doraise=True)
            except Exception as e:
                print(f"[PYTHON SYNTAX ERROR IN {filepath}]: {e}", file=sys.stderr)
                has_errors = True

    # TypeScript / JavaScript / JSON / Markdown Files
    elif ext in [".ts", ".tsx", ".js", ".jsx", ".json", ".md"]:
        # 1. Format with prettier if available
        try:
            subprocess.run(["npx", "prettier", "--write", filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

        # 2. JSON syntax check
        if ext == ".json":
            try:
                import json
                with open(filepath, "r") as f:
                    json.load(f)
            except Exception as e:
                print(f"[JSON SYNTAX ERROR IN {filepath}]: {e}", file=sys.stderr)
                has_errors = True

    return not has_errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post-tool linter & formatter")
    parser.add_argument("--file", help="Target file modified by tool")
    args, unknown = parser.parse_known_args()

    target_file = args.file if args.file else (unknown[0] if unknown else None)
    if not target_file:
        sys.exit(0)

    success = lint_and_format(target_file)
    sys.exit(0 if success else 1)
