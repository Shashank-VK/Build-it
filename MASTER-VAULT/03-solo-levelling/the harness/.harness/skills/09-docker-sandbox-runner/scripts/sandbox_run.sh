#!/usr/bin/env bash
# =============================================================================
# sandbox_run.sh — Sane-default wrapper for .harness/sandbox/gate.sh
# Default: Read-Only workspace, air-gapped network. Pass --rw to enable writes.
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Find repository root (4 levels up from .harness/skills/09-docker-sandbox-runner/scripts)
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
GATE_SCRIPT="${REPO_ROOT}/.harness/sandbox/gate.sh"

if [[ ! -f "$GATE_SCRIPT" ]]; then
    # Fallback to relative path lookup from current working directory
    if [[ -f "./.harness/sandbox/gate.sh" ]]; then
        GATE_SCRIPT="$(pwd)/.harness/sandbox/gate.sh"
    else
        echo "Error: Sandbox gate script not found at '${GATE_SCRIPT}'" >&2
        exit 1
    fi
fi

READ_ONLY=1
NETWORK_MODE="none"
TIMEOUT=""
WORKSPACE=""
SCRATCH=""
ENVS=()
COMMAND_ARGS=()

print_usage() {
    cat << 'USAGE'
Usage: sandbox_run.sh [OPTIONS] [--] COMMAND [ARGS...]

Options:
  --rw                 Enable writable workspace (default is read-only)
  --ro                 Force read-only workspace (default)
  --network <MODE>     Network mode: 'none' (default) or 'allow'
  --timeout <SECS>     Command execution timeout in seconds
  --workspace <DIR>    Directory to bind as workspace
  --scratch <DIR>      Scratchpad directory
  --env <KEY=VAL>      Pass environment variable
  --help               Show this help message
USAGE
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --rw)
            READ_ONLY=0
            shift 1
            ;;
        --ro)
            READ_ONLY=1
            shift 1
            ;;
        --network)
            NETWORK_MODE="$2"
            shift 2
            ;;
        --timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        --workspace)
            WORKSPACE="$2"
            shift 2
            ;;
        --scratch)
            SCRATCH="$2"
            shift 2
            ;;
        --env)
            ENVS+=("$2")
            shift 2
            ;;
        --help|-h)
            print_usage
            exit 0
            ;;
        --)
            shift
            COMMAND_ARGS=("$@")
            break
            ;;
        *)
            COMMAND_ARGS=("$@")
            break
            ;;
    esac
done

if [[ ${#COMMAND_ARGS[@]} -eq 0 ]]; then
    echo "Error: No command specified." >&2
    print_usage >&2
    exit 2
fi

# Build gate.sh options
GATE_OPTS=()
if [[ "$READ_ONLY" -eq 1 ]]; then
    GATE_OPTS+=(--ro)
fi

GATE_OPTS+=(--network "$NETWORK_MODE")

if [[ -n "$TIMEOUT" ]]; then
    GATE_OPTS+=(--timeout "$TIMEOUT")
fi

if [[ -n "$WORKSPACE" ]]; then
    GATE_OPTS+=(--workspace "$WORKSPACE")
fi

if [[ -n "$SCRATCH" ]]; then
    GATE_OPTS+=(--scratch "$SCRATCH")
fi

for E in "${ENVS[@]}"; do
    GATE_OPTS+=(--env "$E")
done

exec bash "$GATE_SCRIPT" "${GATE_OPTS[@]}" -- "${COMMAND_ARGS[@]}"
