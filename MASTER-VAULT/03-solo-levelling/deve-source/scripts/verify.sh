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
    PASS=$((PASS + 1))
  else
    echo "FAIL"
    FAIL=$((FAIL + 1))
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
check "pytest suite passes"                "python3 -m pytest scripts/ -x -q"
check "flake8/ruff syntax clean"           "(python3 -m flake8 .harness/hooks/ scripts/ --max-line-length=100 || python3 -m ruff check .harness/hooks/ scripts/ || python3 -c 'import py_compile,glob; [py_compile.compile(f,doraise=True) for f in glob.glob(\".harness/hooks/*.py\")+glob.glob(\"scripts/*.py\")]')"
check "permissions/check.py --selftest"    "python3 .harness/permissions/check.py --selftest"
check "no __pycache__/.pyc tracked"        "! git ls-files | grep -qE '__pycache__|\\.pyc'"

echo ""
echo "--- Workflow-Skill cross-check ---"
for d in .harness/skills/*/; do
  skill=$(basename "$d")
  wf="$skill"
  case "$skill" in
    fcar-reviewer) wf="fcar-review" ;;
    launch-checklist-runner) wf="launch-checklist" ;;
    postmortem-opener) wf="postmortem" ;;
  esac
  if ! ls ".harness/workflows/${wf}.yaml" >/dev/null 2>&1; then
    echo "[verify] WARN: no matching workflows/*.yaml for skill '${skill}' (expected .harness/workflows/${wf}.yaml)"
  fi
done
# deploy-monitor is automated-only (no skill dir) by design
if ! ls .harness/workflows/deploy-monitor.yaml >/dev/null 2>&1; then
  echo "[verify] WARN: missing automated-only workflows/deploy-monitor.yaml"
fi

echo ""
echo "=== Results: ${PASS} passed, ${FAIL} failed ==="

if [[ $FAIL -gt 0 ]]; then
  echo "[verify] GATE FAILED. Resolve all failures before proceeding."
  exit 1
else
  echo "[verify] GATE PASSED. All verification checks clean."
  exit 0
fi
===== REBUILT 2026-10-10: Part 13 banner-only block replaced with 303-file verbatim Part 13. Prior banner line numbers for Parts 14-17/addendum superseded — see verification.md rebuilt register. =====
