---
description: Run the Two-Judge council review on the current decision or artifact
agent: build
---

Run the Two-Judge verification council on the subject below.

**Subject:** $ARGUMENTS

## Steps

1. Load and follow `.harness/skills/two-judge-verification/SKILL.md`. That
   skill defines the panel, the model routing, and the verdict format. This
   command only sets up the subject and enforces the output contract.

2. Identify the subject. If `$ARGUMENTS` is empty, use the artifact currently
   under discussion — typically `projects/<project>/design-note.md`, a PR
   description, or a proposed approach stated in this session.

3. Determine what kind of subject this is:
   - an **open decision** with competing options (e.g. choosing between two
     architectures) — council reviews the decision
   - a **finished artifact** that needs stress-testing (e.g. a completed
     design note or PR) — use the `adversarial-review` skill instead, which
     is the correct tool for breaking a finished thing

4. Convene the panel per the skill:
   - **Judge 1 (Devil's Advocate)** — strongest possible case AGAINST
   - **Judge 2 (Steelman)** — strongest possible case FOR, responding
     specifically to Judge 1's objections
   - **Verdict** — the core tradeoff, which argument was stronger and why, the
     recommended decision with explicit reasoning, and the conditions under
     which the opposite decision would be correct

5. Enforce the output contract. The verdict MUST be specific. Do not produce
   a wishy-washy "both sides have merit" answer. If the evidence genuinely
   does not favor either side, say that explicitly and state what additional
   information would break the tie.

6. Record the outcome. In `projects/<project>/build-log.md`, under
   `## Evidence`, note that a council review ran, which judges participated,
   and the resulting decision. Then update `claude-progress.md`.

7. If the council produced a decision that changes scope, update
   `feature_list.json` accordingly and record the change as a dated change
   event.
