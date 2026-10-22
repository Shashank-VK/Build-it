#!/usr/bin/env bash
# gate.sh — Sandbox isolation for high-risk command execution
# Usage: task sandbox -- <command>
# Solo AI Product Engineering System v1.0

set -euo pipefail

COMMAND="$*"
WORKSPACE_DIR="$(pwd)"

mask_credentials() {
  sed -E 's/(password|token|secret|api_key|apikey)=[^ ]*/\1=***MASKED***/gI'
}

if command -v docker &>/dev/null; then
  echo "[sandbox] Using Docker isolation"
  docker run \
    --rm \
    --read-only \
    --cap-drop=ALL \
    --no-new-privileges \
    --network none \
    --workdir /workspace \
    -v "${WORKSPACE_DIR}:/workspace:ro" \
    --security-opt="no-new-privileges:true" \
    alpine:latest \
    sh -c "${COMMAND}" 2>&1 | mask_credentials

elif command -v bwrap &>/dev/null; then
  echo "[sandbox] Using bubblewrap isolation"
  bwrap \
    --ro-bind / / \
    --dev /dev \
    --proc /proc \
    --tmpfs /tmp \
    --unshare-net \
    --die-with-parent \
    sh -c "${COMMAND}" 2>&1 | mask_credentials

else
  echo "[sandbox] WARNING: No sandbox available. Install docker or bwrap for proper isolation."
  sh -c "${COMMAND}" 2>&1 | mask_credentials
fi
