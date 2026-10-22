#!/usr/bin/env bash
# secret-scan.sh — Scan for hardcoded secrets
# Solo AI Product Engineering System v1.0

set -euo pipefail

TARGET="${1:-.}"
FOUND=0

echo "[secret-scan] Scanning: $TARGET"

SECRET_PATTERNS=(
  "api_key\s*=\s*['\"][A-Za-z0-9+/]{20,}['\"]"
  "secret\s*=\s*['\"][A-Za-z0-9+/]{20,}['\"]"
  "password\s*=\s*['\"][^'\"]{8,}['\"]"
  "token\s*=\s*['\"][A-Za-z0-9+/._-]{20,}['\"]"
  "ASIA[0-9A-Z]{16}"
  "sk-[A-Za-z0-9]{20,}"
  "ghp_[A-Za-z0-9]{36}"
)

for pattern in "${SECRET_PATTERNS[@]}"; do
  matches=$(grep -rniE "$pattern" "$TARGET" \
    --exclude-dir=".git" \
    --exclude-dir="node_modules" \
    --exclude="*.env.template" \
    --exclude="secret-scan.sh" \
    --exclude="GOD_PROMPT.md" \
    2>/dev/null || true)
  if [[ -n "$matches" ]]; then
    echo "[secret-scan] FOUND potential secret: $pattern"
    echo "$matches"
    FOUND=1
  fi
done

if [[ $FOUND -eq 1 ]]; then
  echo "[secret-scan] FAILED: Potential secrets detected. Remove before committing."
  exit 1
else
  echo "[secret-scan] PASSED: No secrets detected."
  exit 0
fi
