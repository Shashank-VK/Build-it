#!/usr/bin/env bash
# verify.sh — Master verification gate
# Solo AI Product Engineering System v1.0

set -euo pipefail

PASS=0
FAIL=0

check() {
  local name="$1"
  local cmd="$2"
  printf "[verify] %-50s" "${name}..."
  if eval "$cmd" > /dev/null 2>&1; then
    echo "PASS"
    ((PASS++))
  else
    echo "FAIL"
    ((FAIL++))
  fi
}

echo "=== Verification Gate ==="
echo ""

check "Secret scan clean"                  "bash scripts/secret-scan.sh"
check "pre_tool_guard.py syntax valid"     "python3 -c 'import ast; ast.parse(open(\".harness/hooks/pre_tool_guard.py\").read())'"
check "scope-check.py syntax valid"        "python3 -c 'import ast; ast.parse(open(\"scripts/scope-check.py\").read())'"
check "os/lifecycle.md exists"             "test -f os/lifecycle.md"
check "os/fcar-rubric.md exists"           "test -f os/fcar-rubric.md"
check "os/gates.md exists"                 "test -f os/gates.md"
check "os/engineering-rules.md exists"     "test -f os/engineering-rules.md"
check "prfaq template exists"              "test -f os/artifacts/prfaq-template.md"
check "pitch template exists"             "test -f os/artifacts/pitch-template.md"
check "design-note template exists"        "test -f os/artifacts/design-note-template.md"
check "launch-checklist template exists"   "test -f os/artifacts/launch-checklist-template.md"
check "postmortem template exists"         "test -f os/artifacts/postmortem-template.md"
check "harness config exists"              "test -f .harness/config/harness.yaml"
check "hooks.json exists"                  "test -f .harness/hooks/hooks.json"
check "FCAR skill exists"                  "test -f .harness/skills/fcar-reviewer/SKILL.md"
check "CLAUDE.md exists"                   "test -f CLAUDE.md"

echo ""
echo "=== Results: ${PASS} passed, ${FAIL} failed ==="

if [[ $FAIL -gt 0 ]]; then
  echo "[verify] GATE FAILED. Resolve all failures before proceeding."
  exit 1
else
  echo "[verify] GATE PASSED. All verification checks clean."
  exit 0
fi
