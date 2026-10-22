#!/usr/bin/env bash
# spend-log.sh — Log model token spend to .harness/telemetry/spend.csv
# Usage: spend-log.sh <model> <tokens> [cost]
# Appends "date,model,tokens,cost" (creates header if missing).
# Warns at 80% of $10/day (sums today's cost via awk).
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: spend-log.sh <model> <tokens> [cost]" >&2
  exit 1
fi

MODEL="$1"
TOKENS="$2"
COST="${3:-0}"
CSV=".harness/telemetry/spend.csv"

mkdir -p "$(dirname "$CSV")"
if [[ ! -f "$CSV" ]]; then
  echo "date,model,tokens,cost" > "$CSV"
fi

TODAY="$(date +%F)"
echo "${TODAY},${MODEL},${TOKENS},${COST}" >> "$CSV"

TOTAL=$(awk -F, -v today="$TODAY" 'NR>1 && $1==today {sum+=$4} END {print sum+0}' "$CSV")
if awk -v total="$TOTAL" 'BEGIN {exit !(total >= 8.0)}'; then
  echo "[spend-log] WARN: daily spend \$$TOTAL exceeds 80% of \$10 budget" >&2
fi
