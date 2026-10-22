#!/bin/bash
# Master verification gate v2: secret-scan + syntax + pytest + coverage-gate + claim-check
set -euo pipefail
cd "$(dirname "$0")/.."
echo "[verify] secret-scan..."
bash scripts/secret-scan.sh
echo "[verify] python syntax..."
python3 -m py_compile scripts/*.py .harness/hooks/*.py
echo "[verify] pytest..."
python3 -m pytest scripts/ -x -q
echo "[verify] coverage gate..."
python3 scripts/coverage_gate.py
echo "[verify] claim check..."
python3 scripts/claim_check.py
echo "[verify] ALL GATES PASSED."
