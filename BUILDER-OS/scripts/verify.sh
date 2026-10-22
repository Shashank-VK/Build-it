#!/usr/bin/env bash
# Master verification gate v3 (Side-effect free): secret-scan + syntax + pytest + coverage-gate + claim-check + evals
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1

GUARD_LOG=".harness/telemetry/guard.log"
GUARD_BAK=""
if [ -f "$GUARD_LOG" ]; then
  GUARD_BAK=$(mktemp)
  cp "$GUARD_LOG" "$GUARD_BAK"
fi
cleanup() {
  if [ -n "$GUARD_BAK" ] && [ -f "$GUARD_BAK" ]; then
    cp "$GUARD_BAK" "$GUARD_LOG"
    rm -f "$GUARD_BAK"
  fi
  rm -rf .pytest_cache .ruff_cache scripts/__pycache__ evals/__pycache__ .harness/hooks/__pycache__
}
trap cleanup EXIT

echo "[verify] secret-scan..."
bash scripts/secret-scan.sh
echo "[verify] python syntax..."
python3 -B -m py_compile scripts/*.py .harness/hooks/*.py
echo "[verify] lint (flake8)..."
if python3 -m flake8 --version >/dev/null 2>&1; then
  python3 -m flake8 .harness/hooks/ scripts/ evals/ --max-line-length=100
elif python3 -m ruff --version >/dev/null 2>&1; then
  python3 -m ruff check --no-cache .harness/hooks/ scripts/ evals/
else
  echo "[verify] ERROR: neither flake8 nor ruff is installed. Install with: pip install flake8" >&2
  exit 1
fi
echo "[verify] lint (ruff)..."
if python3 -m ruff --version >/dev/null 2>&1; then
  python3 -m ruff check --no-cache .harness/hooks/ scripts/ evals/
fi
echo "[verify] pytest..."
python3 -B -m pytest -p no:cacheprovider scripts/ -x -q
echo "[verify] os evals..."
python3 -B -m pytest -p no:cacheprovider evals/ -x -q
echo "[verify] coverage gate..."
python3 -B scripts/coverage_gate.py
echo "[verify] claim check..."
python3 -B scripts/claim_check.py
echo "[verify] ALL GATES PASSED (ZERO SIDE EFFECTS)."
