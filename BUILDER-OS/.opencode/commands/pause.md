---
description: Safely pause the current feature — flush the build log, clear in_progress
agent: build
---

Safely park the work in progress so the next session can resume cleanly.

## Steps

1. Locate the workspace (`BUILDER-OS/` or the nearest ancestor containing
   `feature_list.json`).

2. Identify the active feature — the one with `status: "in_progress"`. If there
   is none, report that and stop.

3. Flush the build log. In `projects/<project>/build-log.md`, append a new
   session block to the `## Session Log` (never overwrite — append):
   - **Scopes worked**: which feature(s) were active
   - **Uphill/Downhill**: for each scope, is it moving uphill or downhill
   - **Decisions made**: each decision and why; flag irreversible ones
   - **Rabbit holes encountered**
   - **Change events**: any requirement shifts or assumption failures, dated
   - **Appetite consumed**: days remaining
   - **Next session plan**: what gets picked up next

4. Record any partial work:
   - If files were changed but not verified, state that explicitly under
     "Change events" and note which files.
   - If a test was written but is failing, record it honestly. Never record a
     passing receipt for a test that does not pass.

5. Update `feature_list.json`:
   - set the active feature's `status` back to `"not_started"` (or `"blocked"`
     if it is genuinely blocked, with the reason in `notes`)
   - leave `evidence[]` exactly as it is — do NOT clear real evidence
   - enforce `single_active_feature`: exactly zero features may be
     `in_progress` after this command

6. Update `claude-progress.md` with a short status line for the paused feature.

7. If the working tree is dirty, do NOT commit automatically. Report
   `git status -s` and ask whether to commit, and what the commit message
   should say.

8. Report a pause summary: feature id, why it is paused, what state it is in,
   and what the next session should pick up.

Do not delete work. Pausing preserves state; it does not discard it.
