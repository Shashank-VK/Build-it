#!/usr/bin/env bash
# =============================================================================
# entropy_scan.sh — Pre-commit secret scanning & high-entropy heuristic scanner
# =============================================================================
set -euo pipefail

TARGET_DIR="${1:-.}"
SUSPICIOUS_COUNT=0

echo "[SECRET-SCAN] Starting pre-commit secret detection on: ${TARGET_DIR}"

# 1. Tier 1: Gitleaks scan (if available)
if command -v gitleaks >/dev/null 2>&1; then
    echo "[SECRET-SCAN] Running Gitleaks scan..."
    if ! gitleaks protect --staged --verbose --redact 2>/dev/null; then
        echo "[SECRET-SCAN] Warning: Gitleaks flagged potential secrets in staged changes or directory."
        SUSPICIOUS_COUNT=$((SUSPICIOUS_COUNT + 1))
    else
        echo "[SECRET-SCAN] Gitleaks staged scan: CLEAN"
    fi
else
    echo "[SECRET-SCAN] Note: gitleaks binary not found on PATH. Proceeding with heuristic entropy scan."
fi

# 2. Tier 2: Shannon high-entropy regex heuristic scan
echo "[SECRET-SCAN] Running Shannon entropy regex scan for 40+ char base64/hex candidates..."

ENTROPY_MATCHES=$(grep -r \
    --include="*.py" \
    --include="*.ts" \
    --include="*.env" \
    --include="*.env.*" \
    -E "[A-Za-z0-9+/]{40,}" \
    "$TARGET_DIR" 2>/dev/null | grep -v "\.git" || true)

if [[ -n "$ENTROPY_MATCHES" ]]; then
    echo "[SECRET-SCAN] ⚠️ Potential high-entropy secret candidates detected:"
    echo "----------------------------------------------------------------------"
    echo "$ENTROPY_MATCHES"
    echo "----------------------------------------------------------------------"
    echo "[SECRET-SCAN] Please verify the lines above. If these contain real credentials, do NOT commit."
    SUSPICIOUS_COUNT=$((SUSPICIOUS_COUNT + 1))
else
    echo "[SECRET-SCAN] Entropy heuristic scan: CLEAN"
fi

# 3. Exit code determination
if [[ "$SUSPICIOUS_COUNT" -gt 0 ]]; then
    echo "[SECRET-SCAN] ❌ Secret scan failed: suspicious strings found." >&2
    exit 1
fi

echo "[SECRET-SCAN] ✅ All secret scans passed successfully."
exit 0
