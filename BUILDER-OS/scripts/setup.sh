#!/usr/bin/env bash
# setup.sh — download-once first-run provisioning. Idempotent: re-runs are no-ops.
# Provisions: pip packages, npx MCP server cache, Playwright browsers.
# Writes .harness/.provisioned on success. Usage: scripts/setup.sh [--check]
set -euo pipefail
cd "$(dirname "$0")/.."
PROV=".harness/.provisioned"
PINNED_MCP="@modelcontextprotocol/server-filesystem @browsermcp/mcp @modelcontextprotocol/server-github"

if [[ "${1:-}" == "--check" ]]; then
  if [[ -f "$PROV" ]]; then echo "[setup] provisioned:"; cat "$PROV"; exit 0; else echo "[setup] NOT provisioned"; exit 1; fi
fi
[[ -f "$PROV" ]] && { echo "[setup] already provisioned ($(cat $PROV)). Skipping (delete $PROV to force)."; exit 0; }

echo "[setup] 1/3 pip packages..."
PIP_OK=1
# PEP 668 marks system Pythons externally-managed; fall back to a user-site
# install when the plain install is refused.
if ! python3 -m pip install -q pytest flake8 ruff 2>&1 | tail -n 1; then
  python3 -m pip install -q --user --break-system-packages pytest flake8 ruff 2>&1 | tail -n 1 || PIP_OK=0
fi
python3 -m pytest --version >/dev/null 2>&1 || PIP_OK=0
[[ $PIP_OK == 1 ]] && echo "[setup] pip OK" || echo "[setup] WARN: pip packages incomplete (pytest present: $(python3 -m pytest --version >/dev/null 2>&1 && echo yes || echo no)). Continuing."

echo "[setup] 2/3 pre-warming npx MCP cache..."
# shellcheck disable=SC2086
NPM_OK=0; NPM_TOTAL=0
# NOTE: MCP servers run on demand over stdio (they block, so no --version probe).
# Pre-warm = pin availability via registry metadata + cache the tarball.
for pkg in $PINNED_MCP; do
  NPM_TOTAL=$((NPM_TOTAL+1))
  if ver=$(npm view "$pkg" version 2>/dev/null) && npm cache add "$pkg@$ver" >/dev/null 2>&1; then
    echo "[setup] cached $pkg@$ver"; NPM_OK=$((NPM_OK+1))
  else
    echo "[setup] WARN: could not cache $pkg"
  fi
done

echo "[setup] 3/3 playwright browsers (if playwright present)..."
PW="skipped"
if python3 -c "import playwright" 2>/dev/null; then
  python3 -m playwright install chromium 2>&1 | tail -n 1 && PW="ok" || { echo "[setup] WARN: browser download failed"; PW="failed"; }
else
  echo "[setup] SKIP: playwright not installed (E2E matrix needs it later)"
fi

{
  echo "date=$(date -u +%FT%TZ)"
  echo "pip=$([ $PIP_OK == 1 ] && echo ok || echo partial)"
  echo "npx_cache=$NPM_OK/$NPM_TOTAL"
  echo "playwright=$PW"
} > "$PROV"
echo "[setup] DONE ($PROV). Re-run anytime; delete $PROV to force."
