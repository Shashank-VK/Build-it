---
description: Capture a raw idea into feature_list.json and open the Socratic interview
agent: build
---

Capture the user's idea below into the BUILDER-OS feature scope lock.

**Idea:** $ARGUMENTS

## Steps

1. Locate the active workspace. Prefer `BUILDER-OS/` in the current directory.
   If `feature_list.json` is not found, ask the user for the project path
   before writing anything.

2. Read `feature_list.json`. Report the current state:
   - how many features exist and their statuses
   - which feature is `in_progress` (there must be at most one)
   - the next feature id to use

3. Append ONE new feature for the idea:
   - `id`: `<area>-NNN`, following the existing numbering in the file
   - `priority`: next integer after the current highest
   - `area`: short slug (e.g. `chat`, `billing`, `auth`)
   - `title`: one line, imperative
   - `user_visible_behavior`: what a user can do once this ships
   - `status`: `"not_started"`
   - `verification`: 2-4 concrete, observable steps
   - `evidence`: `[]`
   - `notes`: empty

4. Order features so **uncertain (uphill) work comes first**. If the new
   feature has unknowns, move it earlier in the priority order.

5. Update `claude-progress.md` with one line noting the new feature was added.

6. Report the new feature id and the 3-bullet alignment check. Do NOT start
   implementation — that is a separate step. If critical details are missing
   (stack, data model, auth, target platform), ask ONE batched list of up to
   5-7 questions, then stop and wait for the answer.
