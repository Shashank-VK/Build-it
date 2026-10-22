#!/usr/bin/env bash
# =============================================================================
# AI Development Harness — Real OS Sandbox Invocation Gate (CAP-24 / SC-07)
#
# Provides mechanical blast-radius containment using Linux namespaces (Bubblewrap)
# or container runtimes (Docker/Podman). Enforces read-only root filesystems,
# isolated process trees, credential masking, and optional network air-gapping.
# =============================================================================

set -euo pipefail

# Default configuration
DEFAULT_TIMEOUT=60
WORKSPACE_DIR="${HARNESS_WORKSPACE:-$(pwd)}"
SCRATCH_DIR="${HARNESS_SCRATCH:-$(pwd)/scratch}"
NETWORK_MODE="none" # "none" (air-gapped) or "allow"
READ_ONLY_WORKSPACE=0
CUSTOM_TIMEOUT="$DEFAULT_TIMEOUT"
PASSTHROUGH_ENVS=()
COMMAND_ARGS=()

print_usage() {
    cat << 'USAGE'
Usage: gate.sh [OPTIONS] -- COMMAND [ARGS...]

Options:
  --workspace <DIR>    Directory to bind as writable workspace (default: current directory)
  --scratch <DIR>      Designated scratchpad directory
  --network <MODE>     Network mode: 'none' (air-gapped, default) or 'allow'
  --timeout <SECS>     Command execution timeout in seconds (default: 60)
  --ro                 Mount workspace as strictly read-only
  --env <KEY=VAL>      Pass environment variable into the sandbox
  --help               Display this help message
USAGE
}

# Parse command-line flags
while [[ $# -gt 0 ]]; do
    case "$1" in
        --workspace)
            WORKSPACE_DIR="$2"
            shift 2
            ;;
        --scratch)
            SCRATCH_DIR="$2"
            shift 2
            ;;
        --network)
            NETWORK_MODE="$2"
            shift 2
            ;;
        --timeout)
            CUSTOM_TIMEOUT="$2"
            shift 2
            ;;
        --ro)
            READ_ONLY_WORKSPACE=1
            shift 1
            ;;
        --env)
            PASSTHROUGH_ENVS+=("$2")
            shift 2
            ;;
        --help)
            print_usage
            exit 0
            ;;
        --)
            shift
            COMMAND_ARGS=("$@")
            break
            ;;
        *)
            echo "[SANDBOX-GATE] Error: Unknown option '$1'" >&2
            print_usage >&2
            exit 2
            ;;
    esac
done

if [[ ${#COMMAND_ARGS[@]} -eq 0 ]]; then
    echo "[SANDBOX-GATE] Error: No command specified. Use '-- <command> [args...]'" >&2
    exit 2
fi

# Resolve canonical paths
RESOLVED_WORKSPACE="$(cd "$WORKSPACE_DIR" 2>/dev/null && pwd || echo "$WORKSPACE_DIR")"
mkdir -p "$SCRATCH_DIR" 2>/dev/null || true
RESOLVED_SCRATCH="$(cd "$SCRATCH_DIR" 2>/dev/null && pwd || echo "$SCRATCH_DIR")"

# -----------------------------------------------------------------------------
# Runtime Detection: Priority 1 = Bubblewrap (bwrap), Priority 2 = Docker/Podman
# -----------------------------------------------------------------------------
if command -v bwrap >/dev/null 2>&1; then
    SANDBOX_ENGINE="bwrap"
elif command -v docker >/dev/null 2>&1; then
    SANDBOX_ENGINE="docker"
elif command -v podman >/dev/null 2>&1; then
    SANDBOX_ENGINE="podman"
else
    SANDBOX_ENGINE="unsupported"
fi

if [[ "$SANDBOX_ENGINE" == "unsupported" ]]; then
    echo "[SANDBOX-GATE] CRITICAL SECURITY ALERT: No OS sandbox runtime (bwrap, docker, podman) found on host." >&2
    echo "[SANDBOX-GATE] To satisfy SC-07 Harm 4-5 Veto Shield, unsandboxed execution is blocked." >&2
    exit 126
fi

# -----------------------------------------------------------------------------
# Execution Engine 1: Bubblewrap (bwrap) — Zero-daemon unprivileged namespaces
# -----------------------------------------------------------------------------
if [[ "$SANDBOX_ENGINE" == "bwrap" ]]; then
    BWRAP_FLAGS=(
        # 1. Namespace Isolation
        --unshare-user
        --unshare-ipc
        --unshare-pid
        --unshare-uts
        --die-with-parent
        --new-session

        # 2. Filesystem Hermetic Containment
        --ro-bind / /             # Entire host filesystem is strictly read-only
        --dev /dev                 # Minimal isolated device nodes
        --proc /proc               # Isolated procfs matching PID namespace
        --tmpfs /tmp               # Ephemeral in-memory tmpfs
        --tmpfs /run               # Ephemeral runtime state
        --tmpfs /var/tmp           # Ephemeral var tmp
    )

    # 3. Network Isolation (strict whitelist — fail fast on unknown modes)
    case "$NETWORK_MODE" in
        none)
            BWRAP_FLAGS+=(--unshare-net)
            ;;
        allow)
            : # network enabled — no unshare
            ;;
        *)
            echo "[SANDBOX-GATE] Error: invalid --network mode '$NETWORK_MODE' (must be 'none' or 'allow')" >&2
            exit 2
            ;;
    esac

    # 4. Workspace Read/Write Boundary (mount BEFORE credential masking so
    #    masking is never over-shadowed by a later workspace bind)
    if [[ "$READ_ONLY_WORKSPACE" -eq 1 ]]; then
        BWRAP_FLAGS+=(--ro-bind "$RESOLVED_WORKSPACE" "$RESOLVED_WORKSPACE")
    else
        BWRAP_FLAGS+=(--bind "$RESOLVED_WORKSPACE" "$RESOLVED_WORKSPACE")
    fi

    if [[ -d "$RESOLVED_SCRATCH" && "$RESOLVED_SCRATCH" != "$RESOLVED_WORKSPACE"* ]]; then
        BWRAP_FLAGS+=(--bind "$RESOLVED_SCRATCH" "$RESOLVED_SCRATCH")
    fi

    # 5. Zero-Trust Credential Masking (AFTER workspace bind — never over-shadowed)
    for SENSITIVE_DIR in "/root" "$HOME/.ssh" "$HOME/.aws" "$HOME/.gnupg" "$HOME/.config/gcloud" "$HOME/.azure" "$HOME/.kube"; do
        if [[ -d "$SENSITIVE_DIR" && "$SENSITIVE_DIR" != "$RESOLVED_WORKSPACE"* ]]; then
            BWRAP_FLAGS+=(--tmpfs "$SENSITIVE_DIR")
        fi
    done

    # 6. Environment & Working Directory
    BWRAP_FLAGS+=(
        --chdir "$(pwd)"
        --setenv PATH "$PATH"
        --setenv HOME "$HOME"
        --setenv USER "$USER"
        --setenv HARNESS_SANDBOX "bwrap"
        --setenv HARNESS_SANDBOX_NETWORK "$NETWORK_MODE"
    )

    for ENV_PAIR in "${PASSTHROUGH_ENVS[@]}"; do
        ENV_KEY="${ENV_PAIR%%=*}"
        ENV_VAL="${ENV_PAIR#*=}"
        BWRAP_FLAGS+=(--setenv "$ENV_KEY" "$ENV_VAL")
    done

    # Execute with timeout
    exec timeout --kill-after=5s "${CUSTOM_TIMEOUT}s" bwrap "${BWRAP_FLAGS[@]}" "${COMMAND_ARGS[@]}"

# -----------------------------------------------------------------------------
# Execution Engine 2: Docker / Podman Container Isolation
# -----------------------------------------------------------------------------
elif [[ "$SANDBOX_ENGINE" == "docker" || "$SANDBOX_ENGINE" == "podman" ]]; then
    CONTAINER_RUNTIME="$SANDBOX_ENGINE"
    CONTAINER_IMAGE="${HARNESS_DOCKER_IMAGE:-python:3.11-slim}"

    # Network strict whitelist (fail fast on unknown modes)
    case "$NETWORK_MODE" in
        none|allow) : ;;
        *)
            echo "[SANDBOX-GATE] Error: invalid --network mode '$NETWORK_MODE' (must be 'none' or 'allow')" >&2
            exit 2
            ;;
    esac

    # Workspace mount :ro or :rw per --ro flag (respects read-only request)
    local MOUNT_OPTS="rw"
    [[ "$READ_ONLY_WORKSPACE" -eq 1 ]] && MOUNT_OPTS="ro"

    # Compute a working directory that exists inside the container:
    #   if pwd is under workspace, use workspace-relative pwd; else use workspace root
    local CONTAINER_WORKDIR="$RESOLVED_WORKSPACE"
    if [[ "$(pwd)" == "$RESOLVED_WORKSPACE"* ]]; then
        CONTAINER_WORKDIR="$(pwd)"
    fi

    CONTAINER_FLAGS=(
        run --rm
        -i
        --read-only
        --cap-drop=ALL
        --security-opt=no-new-privileges
        --user "$(id -u):$(id -g)"
        -w "$CONTAINER_WORKDIR"
        --tmpfs /tmp:rw,noexec,nosuid
        -v "$RESOLVED_WORKSPACE:$RESOLVED_WORKSPACE:$MOUNT_OPTS"
        -e "HARNESS_SANDBOX=$CONTAINER_RUNTIME"
        -e "HARNESS_SANDBOX_NETWORK=$NETWORK_MODE"
    )

    if [[ -d "$RESOLVED_SCRATCH" && "$RESOLVED_SCRATCH" != "$RESOLVED_WORKSPACE"* ]]; then
        CONTAINER_FLAGS+=(-v "$RESOLVED_SCRATCH:$RESOLVED_SCRATCH:rw")
    fi

    if [[ "$NETWORK_MODE" == "none" ]]; then
        CONTAINER_FLAGS+=(--network none)
    fi

    for ENV_PAIR in "${PASSTHROUGH_ENVS[@]}"; do
        CONTAINER_FLAGS+=(-e "$ENV_PAIR")
    done

    exec timeout --kill-after=5s "${CUSTOM_TIMEOUT}s" "$CONTAINER_RUNTIME" "${CONTAINER_FLAGS[@]}" "$CONTAINER_IMAGE" "${COMMAND_ARGS[@]}"
fi
