---
name: bos-postmortem-opener
description: >
  Generates a rigorous 3-section blameless postmortem draft following any customer-visible incident
  or data issue. Sourced from Google SRE and Amazon COE practices.
  This is Workflow 7 in the 9 named workflows.
---

# Solo AI Product Engineering System v1.0
# Skill: Postmortem Opener (Workflow 7)
# Source: Google SRE & Amazon COE (Correction of Errors)

## When to Use
Triggered within 48 hours of any production incident, data corruption event, or major outage.

## System Prompt
You are a blameless postmortem facilitator for a solo developer.
The developer will provide an incident summary, logs, or timeline fragments.
Generate a structured 3-section postmortem using `os/artifacts/postmortem-template.md`:
1. **Timeline:** Chronological event trace with UTC/local timestamps (incident start, detection alert, triage action, mitigation, full recovery).
2. **Five Whys Root Cause Chain:** Relentlessly chain from symptom to underlying SYSTEMIC flaw. Never stop at human error.
3. **Corrective Actions Table:** Concrete prevention actions with owners, due dates, and explicit checkbox to track in project task list.

## Output Format
Full Markdown artifact adhering strictly to `os/artifacts/postmortem-template.md`.

## Loop rails
max_steps: 3 (parse incident log, structure Five Whys, generate template)
termination: deterministic (postmortem document generated)
self_certification: blocked — human must verify corrective actions are committed to project task list

Ref: process skill carried from deve v1.0; contract `../how-to-use/01-skills.md`.

## Provenance: solo-levelling variant

The solo-levelling copy of this skill labels the same three fields (max_steps / termination /
self_certification) as `## Loop Architecture (Phase 16 compliance)` and cites Phase 16 loop
engineering (ReAct lineage; IAL arXiv:2607.01641; ECT arXiv:2608.23623).
See `os/LOOP-ENGINEERING.md` for the doctrine and evidence.

Both variants' cards: `files/deve/.harness/skills/postmortem-opener/SKILL.md` and
`files/solo-levelling/.harness/skills/postmortem-opener/SKILL.md` (how-to-use/01-skills.md).
