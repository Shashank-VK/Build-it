---
description: Diagnose a stuck loop — repeated identical calls, step budget, unresolved blockers
agent: build
---

Diagnose why the build loop is stuck. Read-only diagnosis first; propose fixes,
do not apply them without the user's go-ahead.

## Steps

1. Locate the workspace (`BUILDER-OS/` or the nearest ancestor containing
   `feature_list.json`).

2. Check for an **Infinite Agentic Loop (IAL)** — the most common cause:
   - Review this session's tool calls for two consecutive calls with the same
     tool AND the same arguments.
   - If found, name the duplicated call and what it kept producing.
   - Recommend the `.harness/skills/26-systematic-rca/SKILL.md` 5-Whys route.

3. Check the **step budget**: `max_steps=15` per session. If the session has
   exceeded 15 steps, the loop rail should have fired. Report the count and
   recommend handing control back to the developer.

4. Check for **self-certification**: the agent declared a task complete
   without a deterministic external gate. Verify the claimed completion
   against a real gate:
   ```bash
   bash scripts/verify.sh
   ```
   If it was not run, that is the finding.

5. Check **scope drift**:
   - Is the active feature's `verification` list actually satisfied?
   - Does the build log show changes to files outside the feature's scope?
   - Are there `not_started` features that were partially implemented?

6. Check **unresolved blockers**: features with `status: "blocked"` and any
   `quarantine/` entries. A blocker with no `notes` is itself a defect.

7. Run `bash scripts/verify.sh` and report the raw output. A failing gate is
   the most likely root cause of a stuck loop — report which gate failed.

8. Output a diagnosis: **root cause**, **evidence**, and **recommended next
   action**. If the evidence is inconclusive, say so explicitly and state what
   additional information would break the tie. Do not fabricate a cause.
