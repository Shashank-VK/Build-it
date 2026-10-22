#!/usr/bin/env bash
# gate.sh — Sandbox isolation for high-risk command execution
# Usage: task sandbox -- <command>
# Solo AI Product Engineering System v1.0

set -euo pipefail

COMMAND="$*"
WORKSPACE_DIR="$(pwd)"

mask_credentials() {
  sed -E -e 's/(password|token|secret|api_key|apikey)=[^ ]*/\1=***MASKED***/gI' \
         -e 's/sk-[A-Za-z0-9]{20,}/sk-***MASKED***/g' \
         -e 's/ghp_[A-Za-z0-9]{36}/ghp_***MASKED***/g' \
         -e 's/AKIA[0-9A-Z]{16}/AKIA***MASKED***/g' \
         -e 's/ASIA[0-9A-Z]{16}/ASIA***MASKED***/g' \
         -e 's/"(password|token|secret|api_key|apikey)"[[:space:]]*:[[:space:]]*"[^"]*"/"\1": "***MASKED***"/gI'
}

# Ensure writable output dir for read-only workspace mount
mkdir -p "${WORKSPACE_DIR}/output"

if command -v docker &>/dev/null; then
  echo "[sandbox] Using Docker isolation"
  timeout 120 docker run \
    --rm \
    --read-only \
    --cap-drop=ALL \
    --no-new-privileges \
    --network none \
    --memory 512m \
    --cpus 1 \
    --workdir /workspace \
    -v "${WORKSPACE_DIR}:/workspace:ro" \
    -v "${WORKSPACE_DIR}/output:/workspace/output:rw" \
    --security-opt="no-new-privileges:true" \
    python:3.12-slim \
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
  # Fallback path: strict mode refuses host execution; otherwise run host cmd.
  if [[ "${SANDBOX_STRICT:-0}" == "1" ]]; then
    echo "[sandbox] WARNING: No sandbox available and SANDBOX_STRICT=1. Refusing host execution." >&2
    exit 1
  fi
  echo "[sandbox] WARNING: No sandbox available. Install docker or bwrap for proper isolation."
  sh -c "${COMMAND}" 2>&1 | mask_credentials
fi
