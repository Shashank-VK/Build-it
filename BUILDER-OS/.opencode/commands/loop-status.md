---
description: Report current loop state — active feature, step count, spend, quarantine
agent: build
---

Report the current state of the BUILDER-OS build loop.

## Steps

1. Locate the workspace (`BUILDER-OS/` in the current directory, or the nearest
   ancestor containing `feature_list.json`).

2. Read `feature_list.json` and summarize:
   - **Active feature**: the one with `status: "in_progress"` (there must be at
     most one — flag it loudly if there are zero or more than one)
   - **Counts** by status: `not_started`, `in_progress`, `blocked`, `passing`
   - **Upbill/downhill**: for the active feature, note whether it is still
     moving uphill (unknowns unresolved) or downhill (path is clear)
   - **Evidence**: how many `passing` features carry a non-empty `evidence[]`

3. Read `claude-progress.md` and show the most recent session entry.

4. Read `.harness/telemetry/spend.csv` if it exists and report today's total
   cost and whether it is within the $10/day budget (warn at 80%).

5. Check for unresolved blockers:
   - any feature with `status: "blocked"` — list its `notes`
   - a `quarantine/` directory in the workspace, if present — list its contents

6. Report the loop-rail state: `max_steps=15` per session, and whether the
   current session appears close to that budget.

Output a compact report. Do not modify any files.
