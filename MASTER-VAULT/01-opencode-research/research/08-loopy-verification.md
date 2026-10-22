# Phase 8 — Task 2: Deep-Verify Forward-Future/loopy

**Fetch date:** 2026-08-11
**Source URLs fetched directly:**
- raw.githubusercontent.com/Forward-Future/loopy/main/README.md (200 OK)
- raw.githubusercontent.com/Forward-Future/loopy/main/CONTRIBUTING.md (404 — does not exist)
- raw.githubusercontent.com/Forward-Future/loopy/main/skills/loopy/SKILL.md (200 OK)
**Verdict:** See contradiction flag section.

---

## What loopy actually is (from live README)

loopy is NOT a loop execution engine. It is a **SKILL** — specifically, a guided AI agent
companion for working with the **Loop Library**, a public catalog of published reusable loops.

The repository has two distinct parts:
1. **Loop Library website** — a public catalog at signals.forwardfuture.com/loop-library/
   where agents can browse published loops. No installation needed to use.
2. **Loopy skill** — an installable SKILL.md that gives an agent guided workflow for
   discovering, crafting, running, auditing, and saving loops.

Key line from README:
> "The website is the library; Loopy is a companion way to work with it. Installing Loopy adds
> the guided workflow, but it does not install or host the website."

---

## Exact Install Path/Command

The README lists explicit install commands per platform:
```bash
# For a single agent
npx skills add Forward-Future/loopy --skill loopy --agent codex -g -y
npx skills add Forward-Future/loopy --skill loopy --agent cursor -g -y
npx skills add Forward-Future/loopy --skill loopy --agent claude-code -g -y

# For all three at once
npx skills add Forward-Future/loopy \
  --skill loopy \
  --agent codex \
  --agent cursor \
  --agent claude-code \
  -g -y

# Interactive installer (for "another agent" — including OpenCode)
npx skills add Forward-Future/loopy --skill loopy -g
```

**OpenCode is NOT listed by name in the install table.** The README says:
> "Using another agent? Run the interactive installer and choose from the agents it detects."
This covers OpenCode but it is not a named/first-class target like Codex, Cursor, or Claude Code.
The interactive installer should detect OpenCode if it is running and place the SKILL.md in
~/.config/opencode/skills/ or .agents/skills/ per the Agent Skills open standard.

**Config format:** None. Loopy is a pure SKILL.md — there is NO entry needed in opencode.json.
Skills are auto-discovered from ~/.config/opencode/skills/ or .agents/skills/. No MCP config,
no plugin config, no opencode.json changes required.

---

## State Store Analysis — CRITICAL QUESTION

### Does loopy maintain its own state store?

**Answer: YES, but minimally.**

From the SKILL.md (live fetch):
> "Save / Reuse: On request, save a delivered loop to the project's LOOPS.md, and reuse saved
> project loops when they fit a later request."

loopy writes to **LOOPS.md** when saving a loop. This is the only persistent state it manages.

There is no .loopy/ directory, no .codex/goals/, no separate JSON state schema, no database.
LOOPS.md is a single Markdown file in the project root — similar in spirit to how walkinglabs
uses claude-progress.md (flat Markdown, not a structured JSON schema).

### Does it conflict with walkinglabs'' feature_list.json / claude-progress.md?

**NOT directly.** LOOPS.md and feature_list.json serve completely different purposes:
- feature_list.json: tracks which feature is active, its verification steps, and its evidence
- LOOPS.md: stores reusable loop recipes (prompt patterns with feedback cycles)

These do not overlap in content or authority. LOOPS.md is not a state tracker for what work
is in progress — it is a recipe library. A loop in LOOPS.md might say "find the slowest page,
improve it, measure again" — it does not say "feature chat-002 is in_progress."

**However, there is a subtler issue to flag:**

Loopy''s "Run" path (from SKILL.md):
> "Run: Execute an identified loop within the user''s authorized scope and return an evidence-backed
> run receipt."

When loopy "runs" a loop, it executes work and produces a "run receipt." That receipt is returned
in-session (not written to a file automatically). The SKILL.md says run receipts can be fed to
Debrief, which then recommends improvements — but does not auto-write to feature_list.json or
claude-progress.md.

**This is the gap:** loopy''s run receipts and evidence are NOT automatically captured in
feature_list.json evidence[]. If the agent uses loopy to run a loop as part of a DoD §4
verification step, the evidence will exist in-session but will NOT propagate to feature_list.json
automatically. The agent must be explicitly instructed to record loop run receipts as evidence.

This is NOT a contradiction of the "walkinglabs as sole state source of truth" decision —
it is an integration gap that requires an explicit instruction in AGENTS.md.

---

## Do the SKILL.md paths match the architecture doc's "Find/Craft/Run/Debrief/Save" workflow?

From the architecture doc (07-autonomous-agent-architecture.md): The described paths were
Find, Craft, Run, Debrief, Save.

From live SKILL.md:
> Discover, Find, Audit/Loop Doctor, Adapt, Craft/Guided Design, Run, Debrief, Save/Reuse, Publish,
> Find-then-craft

**Comparison:**
| Architecture Doc Said | SKILL.md Actually Has | Match? |
|---|---|---|
| Find | Find | YES |
| Craft | Craft / Guided Design | YES (same thing) |
| Run | Run | YES |
| Debrief | Debrief | YES |
| Save | Save / Reuse | YES |
| (not mentioned) | Discover | ADDITIONAL |
| (not mentioned) | Audit / Loop Doctor | ADDITIONAL |
| (not mentioned) | Adapt | ADDITIONAL |
| (not mentioned) | Publish | ADDITIONAL |

The architecture doc''s five paths are a correct subset of loopy''s actual nine paths.
Nothing in the doc was wrong — it was simply a subset. No contradiction.

---

## FLAG: Architecture Claim vs. Reality

**Architecture doc claim (from 07-autonomous-agent-architecture.md):**
loopy described as "the bounded loop execution layer."

**What the real docs say:**
loopy is a skill that HELPS an agent work with loop recipes — discover them, design them, and
execute them in bounded passes. It is not an execution engine in its own right. The bounded
execution behavior comes from the loop DESIGN (each loop specifies a stopping condition) and
from the agent following loopy''s Run guidance, not from loopy itself enforcing engine-level bounds.

**Severity:** LOW. The practical behavior is the same — when loopy''s Run path is invoked, the agent
executes a bounded loop and returns a receipt. Calling it "the bounded loop execution layer" is
a reasonable characterization of what it does, just not mechanically precise.

**Recommended language correction for AGENTS.md / architecture doc:**
Change "loopy (bounded loop execution layer)" to "loopy (skill for designing and running bounded
loops, using the Loop Library catalog)."

---

## CONTRIBUTING.md

Does not exist at main branch. 404. No contributing guidelines found.
This suggests a smaller, single-maintainer project — consistent with what the README implies.

---

## Summary

| Check | Result |
|---|---|
| OpenCode install command | npx skills add Forward-Future/loopy --skill loopy -g (interactive; OpenCode not named explicitly) |
| Config format | None — pure SKILL.md, no opencode.json entry needed |
| Own state store? | Yes, minimal: LOOPS.md only (not a conflict with walkinglabs) |
| Conflicts with feature_list.json? | No direct conflict; different purposes |
| Integration gap? | YES — run receipts not auto-propagated to feature_list.json (needs explicit AGENTS.md instruction) |
| Find/Craft/Run/Debrief/Save match? | YES — correct subset of loopy''s actual 9 paths |
| "Bounded loop execution layer" claim | Functionally accurate but mechanically imprecise — loopy is a skill, not an engine |
| CONTRIBUTING.md | Does not exist (404) |
