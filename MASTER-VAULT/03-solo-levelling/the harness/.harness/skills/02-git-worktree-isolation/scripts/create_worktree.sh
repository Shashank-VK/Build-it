#!/usr/bin/env bash
# =============================================================================
# create_worktree.sh — Create an isolated Git worktree for feature development
# =============================================================================
set -euo pipefail

FEATURE_NAME="${1:-}"
BASE_REF="${2:-HEAD}"

if [[ -z "$FEATURE_NAME" ]]; then
    echo "Error: Missing feature name." >&2
    echo "Usage: $0 <feature-name> [base-ref]" >&2
    echo "Example: $0 user-auth main" >&2
    exit 1
fi

# Ensure we are inside a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "Error: Must be run inside a Git repository." >&2
    exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
TARGET_DIR="${REPO_ROOT}/../wt-${FEATURE_NAME}"
BRANCH_NAME="feat/${FEATURE_NAME}"

echo "[WORKTREE] Target directory: ${TARGET_DIR}"
echo "[WORKTREE] Target branch:    ${BRANCH_NAME}"
echo "[WORKTREE] Base reference:   ${BASE_REF}"

if [[ -d "$TARGET_DIR" ]]; then
    echo "Error: Target directory '${TARGET_DIR}' already exists." >&2
    exit 1
fi

# Create the worktree on the new feature branch
git -C "$REPO_ROOT" worktree add "$TARGET_DIR" -b "$BRANCH_NAME" "$BASE_REF"

echo "[WORKTREE] Successfully created worktree at: ${TARGET_DIR}"

# Change directory into the worktree
cd "$TARGET_DIR"
echo "[WORKTREE] Switched to working tree: $(pwd)"
echo "[WORKTREE] To switch your parent shell, run: cd \"${TARGET_DIR}\""
