#!/usr/bin/env bash
# ==============================================================================
# run_validation.sh — Orchestrates an Empirical Harness Validation Run (Phase 3.5)
# ==============================================================================
# Usage:
#   ./scripts/run_validation.sh <archetype> <target-repo-path>
#
# Arguments:
#   $1 (archetype): C1 | C2 | C6
#   $2 (target-repo-path): Path to target git repository to evaluate
# ==============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# --- 1. Argument Validation ---
if [ $# -lt 2 ]; then
  echo "Error: Missing required arguments."
  echo "Usage: $0 <C1|C2|C6> <target-repo-path>"
  exit 1
fi

ARCHETYPE="$1"
TARGET_REPO="$2"

if [[ ! "$ARCHETYPE" =~ ^(C1|C2|C6)$ ]]; then
  echo "Error: Invalid archetype '$ARCHETYPE'. Supported archetypes are: C1, C2, C6"
  exit 1
fi

if [ ! -d "$TARGET_REPO" ]; then
  echo "Error: Target repository directory '$TARGET_REPO' does not exist."
  exit 1
fi

# Resolve absolute path for target repo
TARGET_REPO_ABS="$(cd "$TARGET_REPO" && pwd)"

# --- 2. Create Run Scratch Directory ---
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
RUN_REL_DIR="scratch/validation/${ARCHETYPE}-${TIMESTAMP}"
RUN_DIR="${REPO_ROOT}/${RUN_REL_DIR}"
mkdir -p "$RUN_DIR"

LOG_FILE="${RUN_DIR}/run.log"
LOG_REL_FILE="${RUN_REL_DIR}/run.log"

# --- 3. Copy Workflow YAML ---
WORKFLOW_SRC="${REPO_ROOT}/.harness/workflows/build-verify.yaml"
if [ ! -f "$WORKFLOW_SRC" ]; then
  echo "Error: Base workflow file '$WORKFLOW_SRC' not found."
  exit 1
fi

cp "$WORKFLOW_SRC" "${RUN_DIR}/build-verify.yaml"

echo "================================================================="
echo " Starting Harness Empirical Validation Run: ${ARCHETYPE}-${TIMESTAMP}"
echo " Archetype:   $ARCHETYPE"
echo " Target Repo: $TARGET_REPO_ABS"
echo " Workflow:    ${RUN_DIR}/build-verify.yaml"
echo " Log Target:  $LOG_FILE"
echo "================================================================="

# --- 4. Run Workflow & Capture Logs ---
{
  echo "=== Harness Empirical Validation Run Started at $(date -u) ==="
  echo "Archetype: $ARCHETYPE"
  echo "Target Repository: $TARGET_REPO_ABS"
  echo "Workflow Config: ${RUN_DIR}/build-verify.yaml"
  echo "--- Environment Diagnostics ---"
  echo "Git Branch: $(git -C "$TARGET_REPO_ABS" rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'N/A')"
  echo "Git Commit: $(git -C "$TARGET_REPO_ABS" rev-parse HEAD 2>/dev/null || echo 'N/A')"
  echo "-------------------------------"
  echo ""
  
  # Placeholder for agy CLI runner invocation against target repo
  echo "TODO: invoke agy with workflow against $TARGET_REPO"
  
  echo ""
  echo "=== Harness Empirical Validation Run Completed at $(date -u) ==="
} > "$LOG_FILE" 2>&1

# --- 5. Output Summary & Log Reminder ---
echo ""
echo "Run complete. Log: ${LOG_REL_FILE}"
echo "Fill in phase-3.5/FRICTION_LOG.md with results from this run"
