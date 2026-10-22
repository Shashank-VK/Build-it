#!/usr/bin/env python3
"""ABAC permission check (policies.cedar + presets.json)."""
import argparse
import json
import sys
from pathlib import Path

CLASS3 = {"git_push_main", "drop_database", "terraform_apply_production", "publish_package"}
READ_ACTIONS = {"read_file", "list_dir", "grep_search", "view_file", "find_by_name", "read_url_content", "search_web"}
WRITE_ACTIONS = {"write_to_file", "replace_file_content", "run_test", "create_branch"}
WRITE_ROLES = {"Coder", "DevOps", "Planner"}
SENSITIVE_PATHS = ["/etc/", "/root/", ".ssh", ".aws", ".gnupg", "gcloud"]
try:
    PRESETS = json.loads((Path(__file__).parent / "presets.json").read_text())
except Exception:
    PRESETS = {}


def check(principal, action, resource, has_approval, token_valid):
    res = str(resource or "")
    for s in SENSITIVE_PATHS:
        if s in res:
            return False, f"deny: sensitive path '{s}'"
    if action in CLASS3:
        if has_approval and token_valid:
            return True, "allow: Class-3 approved"
        return False, "deny: Class-3 needs approval+token"
    if action in READ_ACTIONS:
        return True, "allow: read-only"
    if action in WRITE_ACTIONS and principal in WRITE_ROLES and "workspace" in res:
        return True, "allow: workspace write"
    return False, "deny: default-deny"


def selftest():
    assert check("Anyone", "read_file", "workspace/notes.md", False, False)[0]
    assert check("Coder", "write_to_file", "workspace/app.py", False, False)[0]
    assert not check("Coder", "git_push_main", "workspace/repo", False, False)[0]
    assert check("Coder", "git_push_main", "workspace/repo", True, True)[0]
    assert not check("Coder", "read_file", "/etc/passwd", True, True)[0]
    assert not check("Coder", "read_file", "/home/u/.ssh/id_rsa", False, False)[0]
    print("selftest: 6/6 passed")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    data = json.load(sys.stdin)
    ok, reason = check(data.get("principal", ""), data.get("action", ""), data.get("resource", ""), data.get("has_approval", data.get("has_human_approval", False)), data.get("token_valid", data.get("approval_token_valid", False)))
    print(reason, file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
