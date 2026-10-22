# The Builder's Playbook

The distilled, solo-sized operating manual on top of the full research report. Research discovered what works; this playbook tells you what to do with it when you're one person with a clock running.

**Who it's for:** a solo builder who (a) wants to win hackathons, and (b) wants a personal project system that kills abandoned projects. Built for one human, possibly with AI coding tools.

## What's in here

| File | What it is |
|---|---|
| `01-hackathon-win-system.md` | The win system: idea selection, stack rules, 48h battle plan, demo script framework, judging psychology, anti-patterns, team/solo notes |
| `02-project-execution-plan.md` | The personal project OS: 6 phases with gates, weekly ritual, build log, retros, abandonment-syndrome fixes |
| `03-checklists.md` | Solo-sized checklists: pre-hackathon, during-hackathon (3 gates), demo-day, project launch readiness |
| `templates/` | 5 fill-in-ready markdown templates: 48h battle plan, idea evaluator, demo script, build log, project retrospective |
| `research/` | Raw hackathon research (notes + evidence register) — the evidence behind 01 |

## How to use it

- **Hackathon in 2 days?** Read `01`, copy `templates/idea-evaluator.md` + `templates/battle-plan-48h.md` into your repo, run the 3 gates from `03`.
- **Starting a real project?** Read `02`, run the pre-build sit-down (§3 of that file), start the build log the day you start building.
- **Launch day?** Run the launch-readiness checklist in `03`.

The one maxim this whole thing reduces to (from the distillation):

> *"Know what you're being judged on, cut everything that doesn't serve it, verify what the AI wrote, deploy before you're ready, and never show anything you can't defend as real."*

## Assumptions (explicit)

1. **Stack-agnostic.** Nothing here depends on your language, framework, or host. Your experience level is unknown — nothing here assumes you're junior or senior.
2. **Solo.** You are one person. No reviewers, no QA, no designer. Every gate that needs a second human has been replaced with something you can run against yourself in minutes. What can't be replaced is flagged honestly (see `02` §6's caveats — the "second pair of eyes" problem is real and unsolved).
3. **Two modes.** Hackathon mode (24–48h judged demo) and project mode (weeks-long builds with real users). The two are different games; the playbook compresses but doesn't confuse them. See `02` §5 for the mode table.

## Evidence labels (read before trusting anything)

Every hackathon claim carries a label — `research/hackathon-intel-notes.md` has the full sourcing:

- **Verified** — directly documented in a named primary source (organizer guide, judge interview, winner postmortem).
- **Corroborated** — same claim in 2+ independent sources.
- **Inferred** — plausible pattern from limited sources; treat as hypothesis.
- **Proposed** — my synthesis for solo use; not anyone's claim but the report's.
- **Unknown** — insufficient evidence. Listed, not filled in.

Every adaptation of the base report notes its source section (e.g., "adapted from §14 R-05"). Unmarked adaptations are **Proposed**.

## Relationship to the base report

The full evidence lives in the base report: [`../atlas/product_engineering/`](../atlas/product_engineering/) — 21 sections, 5 appendices, 1,453-row evidence register, 675+ deduped sources (2026-10-10). This playbook **references** it and never duplicates it. When you see "§14 R-05" or "§17 §7", that's a pointer into that report.

Specifically:
- Discipline keep/skip/kill lists → adapted from the §14 rules + §11 gates distillation (`01` §5, `03`).
- Quality gates → §11 §5 scaled per §17 §4.2 Tier-3 calibration (`02` §2, `03` mid-hackathon gates).
- Templates → §17's 18 templates shrunk to 5 (`templates/`, each header says what it adapts and what was cut).
- Demo authenticity / reality inventory → §17 §7, §14 AP-14 (`01` §4, `03` demo-day checklist).

## Honest gaps (what this playbook can't tell you)

Carried forward from the research, not papered over:

- **Solo vs team win rates: Unknown.** Solo wins are documented; relative odds aren't.
- **Live demo vs video, systematically: Unknown.** Format-dependent; no head-to-head evidence.
- **48h hour-by-hour winner schedule: partially Inferred.** Sources skew 24h. The 48h battle plan is built from the Corroborated structure (skeleton by ~25% of clock, code freeze in the last ~15%, submit 30 min early) and labeled where hours are Proposed.
- **Measured score weights, most prize amounts, judge watch behavior: Unknown or single-source.** Read the rubric of *your* event instead of assuming.
- **The "second pair of eyes" problem is unsolved.** See `02` §6. AI pre-review is triage, not a reviewer; a cold self-read is the weakest gate in this OS.
