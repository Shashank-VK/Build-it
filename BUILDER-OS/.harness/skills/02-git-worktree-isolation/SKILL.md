---
name: bos-git-worktree-isolation
domain: Execution & Version Control
version: 1.0.0
tier: Essential
cap: CAP-06
triggers:
  - "new feature"
  - "speculative change"
  - "isolate work"
  - "git worktree"
---

# Git Worktree Isolation

## Objective
Provide an isolated, zero-conflict filesystem environment for speculative feature development, high-risk refactoring, and parallel multi-agent tasks by provisioning dedicated Git worktrees linked to independent working trees.

## When to Activate
- Starting development on a new feature or complex sub-system.
- Executing speculative or high-risk changes that may need to be discarded without polluting the primary workspace.
- Running parallel agent workflows or test matrices simultaneously without repository index or file lock contention.
- Debugging an urgent issue or reproducing a bug while preserving in-progress uncommitted work on the current branch.

## Step-by-Step Runbook

### Why Worktrees Outperform In-Place Branch Switching
Switching branches within a single working tree introduces severe operational risks for autonomous agents:
1. **Zero Stash Conflicts**: Switching branches with dirty working trees requires `git stash`, which often creates merge conflicts, lost untracked files, or corrupted intermediate state upon `git stash pop`.
2. **Parallel Agent Execution**: Multiple agents or background processes can work concurrently on distinct physical directories linked to the same Git object database without write-lock collisions on `.git/index`.
3. **Independent Build Artifacts**: Build caches, node_modules, virtualenvs, and test outputs remain isolated per worktree, preventing cross-branch contamination.

---

### Execution Protocol

#### Step 1: Initialize the Isolated Worktree
From the root of your current repository, provision a new worktree in a sibling directory on a new feature branch:

```bash
# General syntax: git worktree add <path> -b <branch-name> [base-commit]
git worktree add ../scratch-my-feature -b feat/my-feature HEAD
```

Alternatively, use the helper script:
```bash
bash .harness/skills/02-git-worktree-isolation/scripts/create_worktree.sh my-feature
```

#### Step 2: Navigate and Establish Environment
Enter the newly provisioned worktree and prepare the development environment:

```bash
cd ../scratch-my-feature

# Verify active branch and status
git branch --show-current
git status

# If applicable, install or link dependencies
# npm install / poetry install / pip install -e .
```

#### Step 3: Implement Changes & Verify Tests
Perform development, execute unit tests, and run validation gates strictly within the isolated worktree directory:

```bash
# Execute tests in isolation
pytest tests/ -v
# or
npm test
```

#### Step 4: Commit Changes and Push Branch
Stage and commit changes using conventional commit messages, then push the feature branch to remote:

```bash
git add .
git commit -m "feat(scope): implement isolated feature changes"
git push -u origin feat/my-feature
```

#### Step 5: Merge via PR / Rebase and Clean Up
Once the feature branch has been reviewed, merged, or verified, return to the main workspace and cleanly dismantle the worktree:

```bash
# Return to the primary repository root
cd -

# List active worktrees to confirm target path
git worktree list

# Safely remove the worktree directory and associated metadata
git worktree remove ../scratch-my-feature

# Prune any stale administrative worktree metadata
git worktree prune

# (Optional) Delete the local feature branch if merged
git branch -d feat/my-feature
```

## Completion Gate
- Dedicated worktree directory is successfully provisioned and linked to `feat/{feature}` without altering the main working directory.
- All test suites pass 100% clean inside the isolated worktree.
- Commits are pushed cleanly to the remote tracking branch.
- `git worktree list` confirms the worktree has been cleanly removed and pruned after completion.

## Common Pitfalls
- **Branch Already Checked Out**: Git prevents checking out a branch that is currently checked out in another active worktree. Ensure you create a new branch or remove the existing worktree first.
- **Manual Deletion with `rm -rf`**: Deleting the worktree folder with `rm -rf` leaves dangling references in `.git/worktrees/`. Always use `git worktree remove <path>` followed by `git worktree prune`.
- **Relative Path Mistakes**: When creating sibling worktrees (e.g. `../wt-feature`), ensure paths are relative to the repository root to avoid creating nested worktrees inside `.git/` or untracked subdirectories.
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
