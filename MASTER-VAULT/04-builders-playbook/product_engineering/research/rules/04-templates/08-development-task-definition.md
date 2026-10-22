# Template 08 — Development Task Definition

**Use when:** defining a unit of build work for a human or a coding agent. Sized so one task = one reviewable change (R-14). **Enforces:** R-05 (scope), R-14 (small changes), R-13 (verification for agents).

## 1. Task

*One sentence: what will be true when this is done?*

> _Fill in._

## 2. Context

*Links: PRD/design doc section, ADR, related tasks. The minimum a competent stranger (or agent) needs to start without asking questions.*

> _Fill in._

## 3. Scope

- **In scope:** _…_
- **Out of scope (no-gos for this task):** _…_
- **Don't touch:** _… (files/systems explicitly off-limits)_

## 4. Acceptance criteria

*Concrete, checkable, written before work starts. "Works correctly" is not a criterion.*

- [ ] _…_
- [ ] _…_
- [ ] Tests: _which tests prove this_ (link template 10 section)
- [ ] Docs updated: _…_ / N/A because _…_

## 5. Verification steps (mandatory for agent-executed tasks)

*How the author (human or agent) proves the work before review: commands run, tests added, manual checks performed, diff self-reviewed. For agents: paste the verification transcript or checklist output.*

- [ ] _…_

## 6. Risks and unknowns

*What's uncertain, what could go wrong, and the fallback if it does.*

> _Fill in._

## Acceptance criteria (for the task definition itself)

- [ ] Completable in ≤1–2 days; if larger, split it
- [ ] Acceptance criteria are checkable by someone other than the author
- [ ] Out-of-scope and don't-touch are explicit
- [ ] Verification steps exist before work begins (not invented after)

## Anti-patterns this blocks

AP-02 (scope creep) · AP-09 (unverified agent output) · AP-11 (automation without verification).
