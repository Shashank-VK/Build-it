# Phase 15 — Master Synthesis: The Solo AI Product Engineering System

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

Every claim in this document is traceable to a specific phase and org finding. Where a section makes a design decision not directly from a prior finding, it is marked [DERIVED] and the derivation chain is stated.

---

## 1. Product Development Lifecycle

The complete solo-adapted sequence, from idea to deprecation:

```
IDEA
 ↓
[Gate 1: Appetite Check] — Is this idea worth my time? Set the appetite now (in days), before the solution.
 ↓
PR/FAQ DRAFT — One-page press release from the customer's perspective + 3 hard FAQ answers.
 ↓
[Gate 2: Press Release Passes] — A skeptical-customer challenge must not destroy the value proposition.
 ↓
PITCH DOCUMENT — Problem, Appetite, Solution (breadboards/fat-marker sketches), Rabbit Holes, No-gos.
 ↓
[Gate 3: Pitch Self-Approval] — Can I actually build this within the appetite? Do I bet on it?
 ↓
LIGHTWEIGHT DESIGN NOTE (if >1 day effort, external interface change, or irreversible decision) — 
  Context, Goals, Non-Goals, Alternatives Considered, Cross-cutting concerns.
 ↓
[Gate 4: Design Note FCAR] — Fresh context adversarial review against the rubric. Fails = revise.
 ↓
LAUNCH CHECKLIST PRE-CHECK — 8-item checklist verified before any implementation begins.
 ↓
IMPLEMENTATION — Scope-based. Work uphill scopes first. Build log maintained.
 ↓
[Gate 5: Per-PR Quality Gate] — Automated linting + AI style review + stakes-tiered human review.
 ↓
SECURITY/RELIABILITY CHECK — Tiered by stakes: high-stakes requires independent implementation + comparison.
 ↓
[Gate 6: Launch Checklist Complete] — All 8 items pass before deploy.
 ↓
DEPLOY (staged: 10-minute observation window, pre-committed rollback threshold defined).
 ↓
MONITORING (error rate, latency alerts pre-configured before launch).
 ↓
EXPERIMENT (if A/B applicable: define hypothesis and success metric before test, not after).
 ↓
POST-LAUNCH REVIEW (weekly: metric check vs. launch-day baseline).
 ↓
[On incident] → POSTMORTEM (3-section: timeline, root cause chain, corrective actions with due dates).
 ↓
ITERATION CYCLE (re-enter at Pitch stage for the next scope of work).
 ↓
DEPRECATION (when: defined upfront — "I will deprecate this if [X] by [date]").
```

**Sources:** PR/FAQ from Phase 2/Amazon; Pitch from Phase 2–3/Basecamp; Design Note from Phase 5/Google; Launch Checklist from Phase 7/Google; Scopes + uphill-first from Phase 8/Basecamp; Quality Gate from Phase 9/Google; Staged deploy from Phase 10/Netflix; Postmortem from Phase 11/Google.

---

## 2. Role/Responsibility Model

**Delegation taxonomy (from Phase 13):**
- **Human-only:** Irreversible decisions, high-stakes security/financial code (final implementation), appetite setting, circuit breaker enforcement.
- **AI-assisted:** PR/FAQ draft and critique, Pitch document drafting, Non-Goals generation, Alternatives Considered generation, design note first draft, failure mode analysis, launch checklist verification, deployment metric monitoring.
- **AI-first-human-approved:** Style review against locked rubric (code review), postmortem first draft, corrective action item generation.
- **Automated:** Linting, CI tests, deployment metric gate (rollback trigger at pre-committed threshold), scope gate check (new task vs. Non-Goals list).

**The human's non-negotiable role (cannot be delegated):**
- Setting the appetite before defining the solution (Phase 13 Row 2)
- Committing to the circuit breaker date (Phase 13 Row 4)
- Finalizing and committing to corrective actions from postmortems (Phase 13 Row 15)
- Classifying decisions as reversible vs. irreversible (Section 4 below)
- Any final implementation of high-stakes code paths (Phase 13 Row 16)

---

## 3. Artifact Chain

| Stage | Artifact | Creator | Reviewer | Rejection Authority | Carries Forward |
|-------|----------|---------|----------|--------------------|--------------------|
| Idea | PR/FAQ | Human (AI-assisted) | AI skeptical-customer | Human — if press release doesn't survive challenge, idea doesn't proceed | Press release language → Pitch Problem section |
| Scoping | Pitch Document | Human (AI-assisted) | Human self-review | Human — if can't bet on it, don't | No-gos + Appetite → Design Note constraints |
| Design | Lightweight Design Note | AI-first-human-approved | FCAR rubric (fresh AI context) | Rubric — fails any item = revise | Alternatives Considered → preserved in note |
| Implementation | Build Log (running notes) | Human (AI-assisted) | Human | Human | Decisions made during build, date-stamped |
| Pre-launch | Launch Checklist | AI checker + human | Human | Checklist — any incomplete item blocks launch | Status of each item |
| Incident | Postmortem | AI-first-human-approved | Human | Human — corrective actions must be committed | Actions added to project task list |

**Sources:** Artifact types from Phases 2–11 per-org findings. FCAR from Phase 14.

---

## 4. Decision Architecture

**Reversible vs. Irreversible Classification:**

A decision is **irreversible** if: (a) changing it requires migrating existing data, (b) it creates an external API commitment (backward compatibility applies), (c) it requires rebuilding > 50% of the work already completed, or (d) it has a significant third-party cost that cannot be recovered.

A decision is **reversible** if: it can be changed within the current appetite without restarting, it affects only internal implementation (no external commitment), and changing it doesn't break any existing user-facing contract.

**Kill/Pause/Pivot criteria:**
- **Kill:** After the circuit breaker date, if the minimum shippable version cannot be completed, and there's no appetite to re-pitch. Kill = stop work, write a one-paragraph postmortem of why, archive the Pitch document.
- **Pause:** A blocking external dependency is unresolved. Pause = freeze scope, set a resume trigger condition.
- **Pivot:** A scope item classified as "uphill" reveals the solution is wrong. Pivot = update the Pitch document, scope hammer, continue within the appetite.

**Veto structure (Lens 1 findings from Phases 2–11 consolidated):**
- Gate 2 (press release): human + AI skeptical-customer jointly hold veto
- Gate 3 (pitch): human holds sole veto (only the human can make the bet)
- Gate 4 (design note): rubric holds veto — the rubric fails the artifact before the human can rationalize past it
- Gate 5 (per-PR): automated tests hold hard veto; AI style review holds soft veto (human can override with documented reason)
- Gate 6 (launch checklist): checklist holds veto — every item must pass before deploy

---

## 5. Decision Gates and Review System

| Gate | Trigger | Artifact reviewed | Blocking condition | Override |
|------|---------|-------------------|--------------------|---------|
| 1 — Appetite | Before any solution thinking | Stated appetite (days/hours) | No appetite stated = idea not ready | None — must be set |
| 2 — PR/FAQ | After press release written | PR/FAQ document | Skeptical-customer critique destroys value proposition | Human can iterate (no override) |
| 3 — Pitch | Before implementation commit | Pitch document | Human cannot honestly answer "can I build this in [appetite]?" | None — human decides |
| 4 — Design Note FCAR | If design note required | Design note | Any rubric item fails | Human can override with documented exception (exception is logged, visible in artifact) |
| 5 — Per-PR Quality | Before every merge | Code change | Failing automated tests (hard veto); AI style review failures (soft) | Hard tests: no override. Soft: human documents exception. |
| 6 — Launch Checklist | Before any production deploy | Launch checklist | Any incomplete item | Human can waive with documented exception (visible in checklist artifact) |

---

## 6. Process Cost Model (Lens 2 — Minimum Effective Version)

From Phases 2–11 Lens 2 findings, the minimum effective version of each practice for a solo developer:

| Practice | Full org version | Solo minimum | What's cut |
|----------|-----------------|-------------|------------|
| PR/FAQ | Multi-iteration narrative meeting with stakeholders | One 30-minute solo writing session, one AI critique pass | The meeting; stakeholder attendance |
| Pitch | Full Betting Table meeting | Solo self-review with the 5-section template | The Betting Table meeting |
| Design Note | Multi-reviewer async design doc process (days-weeks) | 200–500 words, 5 required sections, 1 FCAR pass | Committee review; multiple reviewers |
| Non-Goals | Cross-stakeholder sign-off meeting | 3-item bullet list in Pitch document | The sign-off meeting |
| Alternatives Considered | Formal alternatives analysis in committee | 2 rejected alternatives with reasons, written in the design note | Committee discussion |
| Launch Checklist | LCE team multi-meeting engagement | 8-item personal checklist, self-administered | The LCE team |
| Code Review | Readability certification + code owners | Automated linting + AI style review + stakes-tiered human review | The certification program |
| Postmortem | Cross-org postmortem sharing + action tracking in bug system | 3-section postmortem document + corrective actions in project task list | The org-wide sharing ceremony |

---

## 7. Context and Traceability Model (Lens 3)

**How links between requirements, decisions, code, tests, and metrics are preserved:**

Every artifact has a header:
```
Artifact type: [PR/FAQ | Pitch | Design Note | Build Log | Launch Checklist | Postmortem]
Date: [date]
Project: [project name]
Appetite: [days remaining]
Continues from: [prior artifact name and location]
```

**Traceability chain:** PR/FAQ → Pitch (links to PR/FAQ problem statement) → Design Note (links to Pitch's solution section) → Build Log (links to Design Note's design decisions) → Launch Checklist (links to Build Log's open items) → Postmortem (links to Launch Checklist's state at incident time).

**No-Goals traceability:** The Non-Goals list in the Pitch is referenced by the Scope Gate check — any new task is measured against the Non-Goals list before being added to the project.

**Alternatives Considered traceability:** Rejected alternatives in the Design Note prevent relitigating them. A future reviewer can read the Design Note to understand why the chosen approach was selected and specifically what was rejected and why.

**Sources:** Phase 4/Google Q4 (Alternatives Considered as organizational memory), Phase 8/Basecamp Q1 (Hill Chart as progress traceability), Phase 3/Google Q3 (Non-Goals as source-of-truth reference).

---

## 8. Change Management Protocol (Lens 4)

**Mid-build change trigger:** Any of: (a) uphill scope becomes stuck for >2 sessions; (b) new task contradicts existing Non-Goal; (c) remaining estimate exceeds 150% of appetite; (d) external dependency behavior changes.

**Response sequence:**
1. Stop the current build task.
2. Open the Pitch document.
3. Append a "Change Event" section with: date, what changed, why.
4. Classify: (a) within appetite after scope hammering → continue; (b) outside appetite → invoke circuit breaker or re-pitch.
5. If scope-hammering: apply the must-have test to all open tasks. Tasks that fail the must-have test are either cut or moved to "nice-to-have" (marked ~) or a future pitch.
6. The change is permanently visible in the Pitch document — not overwritten.

**Mid-incident re-prioritization:** During an active production incident, the pre-committed rollback threshold is the decision rule — no manual judgment required at that moment. Post-incident, the postmortem documents what was done and why.

**Sources:** Phase 3/Basecamp Q3 (Scope Hammer), Phase 3/Basecamp Q4 (circuit breaker and Betting Table authority), Phase 10/Netflix Q3 (pre-committed halt authority), Phase 11/Google Q5 (incident command authority).

---

## 9. Engineering Rules and Anti-Patterns

**Rules (each is a direct compression from the phase findings):**
1. Write the appetite before the solution. (Phase 2/Basecamp)
2. Write the press release before the spec. (Phase 2/Amazon)
3. Non-Goals must have at least 3 explicit items. (Phase 3/Google)
4. Every design decision requires at least 2 rejected alternatives documented. (Phase 4/Google)
5. Document known-bad approaches (Rabbit Holes) before implementation. (Phase 4/Basecamp)
6. Write a design note for any change requiring >1 day or touching an external interface. (Phase 5/Google)
7. Uphill scopes are worked before downhill scopes. (Phase 8/Basecamp)
8. Pre-commit the rollback threshold before deploying. (Phase 10/Netflix)
9. Every incident above defined severity gets a 3-section postmortem with dated corrective actions. (Phase 11/Google)
10. AI-generated code in high-stakes paths requires independent human re-implementation + comparison. (Phase 12/Amazon and Phase 13 Row 16)

**Anti-Patterns (explicitly named):**
- Designing for scale you don't have yet. (Phase 6 — Two-Pizza Team and appetite as constraints)
- Mixing refactoring with feature work in the same task. (Phase 8 — absent from all orgs as a named rule, which makes it a known cultural norm worth naming explicitly here)
- Enormous PRs. (Phase 8 — absent from all orgs as a named enforcement, making it an explicit solo risk)
- Treating "the AI said so" as a primary source. (Phase 12 and Phase 14 — no org publishes AI correctness metrics)
- Filing a postmortem without tracking corrective actions in the project task list. (Phase 11 — the common anti-pattern)

**Bureaucracy to Discard (full list from Phase 13 — every entry named, as required):**
1. **Narrative meeting** — the scheduled multi-stakeholder assembly to review a PR/FAQ. Discard the meeting, keep the PR/FAQ artifact.
2. **Betting Table meeting** — scheduled group decision on which pitches proceed. Discard the meeting, keep the Pitch document and the appetite commitment.
3. **Cross-stakeholder Non-Goals sign-off meeting** — Non-Goals are committed by the solo developer personally, no meeting required.
4. **Full technical design document for implementation details** — implementation decisions live in the Build Log, not a separate technical spec.
5. **LCE team as a separate organizational unit** — the Launch Checklist artifact is what matters; the solo developer administers it.
6. **Readability Certification program** — the locked style guide + automated linting is the equivalent; no certification mentorship path.
7. **Kayenta-scale canary analysis infrastructure** — a pre-committed rollback threshold + 10-minute observation window is the solo equivalent.
8. **Cross-org postmortem sharing ceremony** — postmortems are stored in the project repository (git-tracked) and searchable; no sharing meeting.
9. **Formal senior engineer sign-off program** — the stakes-tiering model (high/medium/low) + independent implementation for high-stakes paths replaces institutional sign-off.

---

## 10. Quality, Security, and Reliability System

**Quality gates (per PR):**
- Hard: Automated tests must pass. Linting must pass. (Phase 9/all orgs)
- Soft: AI style review against locked rubric must pass OR human documents exception with reason.
- Stakes tier applied: low-stakes (AI-first, cursory human review), medium-stakes (AI-assisted, careful line-by-line human review), high-stakes (AI draft + independent human implementation + comparison).

**Security minimum bar (Launch Checklist items 5–7):**
- No secrets hardcoded in the repository (check before every launch)
- All external inputs validated and sanitized
- Authentication + authorization tested against at least one adversarial case (attempt to access resource without permission — confirm it's blocked)

**Reliability minimum bar (Launch Checklist items 3–4 and 8):**
- Rollback plan tested before first production deploy (not just designed — actually executed in staging)
- Error rate alert configured and verified to fire before launch
- Load tested at 2× expected volume before launch

**Sources:** Phase 7/Google (LCE checklist structure), Phase 9/Google (quality gates), Phase 13 Row 11 (personal Launch Checklist as LCE solo equivalent).

---

## 11. Release and Experimentation System

**Default deploy procedure:**
1. Confirm Launch Checklist is complete.
2. Define rollback threshold before deploying: "If [error rate metric] exceeds [X]% within 10 minutes of deploy, I will roll back immediately."
3. Deploy.
4. Monitor the defined metric for 10 minutes.
5. If threshold is crossed: roll back immediately. No exceptions.
6. If 10 minutes pass without threshold crossing: deployment is stable. Monitor for 24 hours at reduced attention.

**Experimentation (A/B tests):**
- Write the hypothesis and success metric before launching the test.
- Define the minimum detectable effect and required sample size before looking at results.
- Run to completion. Do not stop early because results look good.
- Decision rule: if the primary metric achieves the pre-defined success criterion, ship the winner. If not, do not ship the change.

**Sources:** Phase 10/Netflix (pre-committed halt authority, automated rollback), Phase 10/Meta (Gatekeeper flag = instant disable), Phase 2/Netflix (A/B testing as the product-decision mechanism).

---

## 12. AI/Agent Operating Model

**Shape (decided in Phase 13 from row patterns):** A single AI assistant operating within named workflows, not a multi-agent system. The workflows are the structure; the AI is the executor within each workflow.

**The 9 named workflows:**

| Workflow | Trigger | AI Role | Human Role |
|----------|---------|---------|-----------|
| 1. Working Backwards | New idea | Draft press release + skeptical-customer critique | Iterate; approve final version |
| 2. Scope Gate Check | New task proposed | Check task against Non-Goals list | Decide whether to add, reject, or revise Non-Goals |
| 3. Alternatives Generator | Before any design decision | Generate 2–3 genuinely different alternatives | Reject with reasons; commit to chosen approach |
| 4. Failure Mode Analyzer | Before any external integration | List top-3 failure modes + user-visible impact | Decide which to prevent vs. tolerate |
| 5. Launch Checklist Runner | Before every deploy | Check current project state against 8-item checklist | Resolve any gaps |
| 6. Deployment Monitor | Immediately post-deploy | Monitor pre-defined metric; alert if threshold crossed | Roll back if alerted (no deliberation) |
| 7. Postmortem Template Opener | Any incident above defined severity | Generate 3-section postmortem draft from incident log | Correct; commit corrective actions |
| 8. Stakes Classifier | Before implementing any code | Classify code path as low/medium/high-stakes | Apply corresponding review tier |
| 9. Unknown-First Task Sorter | Start of any implementation cycle | Identify uphill (uncertain) vs. downhill (clear) scopes | Work uphill scopes first |

**What the AI never decides autonomously:**
- Appetite setting
- Circuit breaker enforcement
- Final corrective action commitment
- Decision reversibility classification
- High-stakes code implementation (final version)

---

## 13. Tooling/MCP Architecture

**Minimum tooling stack:**

| Need | Tool | Notes |
|------|------|-------|
| Artifact storage | Git repository | All artifacts versioned; postmortems searchable |
| CI/automated testing | GitHub Actions or equivalent | Hard gate on every PR |
| Linting | Language-specific linter (eslint, rubocop, etc.) | Hard gate on every PR |
| AI assistant | Any capable model (Gemini, Claude, GPT-4) | Used within the 9 named workflows; model choice is not locked |
| Monitoring/alerting | Simple error rate alert (Datadog, Sentry, or equivalent) | Must be set up before launch |
| Project tracking | Plain markdown task list in the repository | No external project management tool required |

**MCP/agent opportunities (from Phase 13 automation inventory):**

These are optional workflow automations, implemented only when the overhead of manual operation exceeds the setup cost:

1. **Working Backwards agent** — input: bullet-point idea; output: draft PR/FAQ + 3 skeptical-customer questions
2. **Scope Gate agent** — input: proposed task + Non-Goals list; output: pass/fail + conflict explanation
3. **Deployment gate agent** — input: metric name + threshold + deploy event; output: automated alert + rollback trigger

**MCP tool definitions** (these are the external tools the agent needs):
- `create_artifact(type, content)` — creates a typed artifact in the repository
- `check_non_goals(task_description, non_goals_list)` — returns pass/fail + reasoning
- `evaluate_against_rubric(artifact, rubric)` — runs FCAR; returns per-item pass/fail
- `monitor_metric(metric_name, threshold, window_minutes)` — continuous post-deploy monitoring
- `create_postmortem(incident_log)` — generates 3-section postmortem draft

---

## 14. Adversarial Review Mechanism (from Phase 14 — non-optional)

**The Fresh Context Adversarial Review (FCAR) protocol:**

1. Before any significant artifact is finalized, write the evaluation rubric. The rubric is a checklist of properties the artifact must have. Write it before the artifact is complete — if written after, it can be reverse-engineered to match the artifact's current state.

2. Open a new AI context with no memory of the original artifact's authoring process.

3. Provide only: (a) the artifact to review, and (b) the locked rubric. Nothing else.

4. The AI evaluates each rubric item and returns: pass/fail per item, and for each fail, the specific failing evidence.

5. The human reviews the FCAR output. If any item fails: revise the artifact and repeat from step 3.

6. If a rubric item fails and the human believes the failure is acceptable: document the exception explicitly in the artifact ("Rubric item X was waived because: [specific reason]"). The waiver is visible to any future reviewer.

**The tested and confirmed rubric (from Phase 14):**

A PRD/design note passes if ALL of:
1. Every claimed user benefit or technical claim is sourced (cited, named, or traceable to a prior phase finding)
2. Non-Goals section lists at least 2 explicit exclusions
3. No technical claim is asserted without a named source or traceable prior finding
4. Success metric is measurable and specific
5. Alternatives Considered lists at least 1 rejected alternative with a specific reason

**Confirmed test:** The injected-flaw test (Phase 14) confirmed this rubric catches confident-but-unsourced claims as the primary finding. The mechanism works.

---

## 15. Reusable Toolkit

### Template: PR/FAQ (Working Backwards)

```markdown
# [Project Name] — Press Release

**FOR IMMEDIATE RELEASE**

[City, Date] — [Company/Solo Developer] today announced [product name], a [one-line description].

**The problem:** [One paragraph describing the specific, concrete problem the target customer has. No solution language.]

**The solution:** [One paragraph describing what the product does, from the customer's perspective, without technical jargon.]

**Customer quote:** "[A quote a real customer might say about the value they get. Be specific.]"

**How to get started:** [One sentence describing the first action a customer takes.]

---

# Frequently Asked Questions

**Q: What does [product name] NOT do?**
A: [At least 2 explicit non-goals stated as direct answers]

**Q: Why not [obvious alternative]?**
A: [Specific rejection reason for the most obvious alternative approach]

**Q: What's the risk if this doesn't work?**
A: [Honest assessment of the downside]
```

### Template: Pitch Document

```markdown
# Pitch: [Project Name]

**Date:** [date]
**Appetite:** [X days/hours] — hard limit

## Problem
[1–2 paragraphs describing the specific problem and who has it]

## Solution
[Fat-marker sketch description or breadboard — describe the flow, not the implementation]

## Rabbit Holes
- [Known-bad approach 1]: [why it's bad/too complex]
- [Known-bad approach 2]: [why it's bad/too complex]

## No-gos (explicitly NOT in this version)
- [Excluded feature/use case 1]
- [Excluded feature/use case 2]
- [Excluded feature/use case 3]
```

### Template: Lightweight Design Note

```markdown
# Design Note: [Decision Name]

**Date:** [date]
**Project:** [project name]
**Appetite remaining:** [X days]
**Continues from:** [Pitch document location]

## Context
[1 paragraph: why this decision is needed now]

## Goals
- [What this design achieves]

## Non-Goals
- [What this design explicitly does NOT cover]

## Design
[The chosen approach, in plain language]

## Alternatives Considered
1. **[Alternative 1]** — Rejected because: [specific reason]
2. **[Alternative 2]** — Rejected because: [specific reason]

## Rabbit Holes
- [Known-bad implementation path]: [why]

## Cross-cutting Concerns
[Security, performance, backward-compatibility implications, if any]
```

### Template: Launch Checklist

```markdown
# Launch Checklist: [Project Name]

**Date:** [date]
**Rollback threshold pre-committed:** If [metric] exceeds [X]% within [10] minutes, rollback immediately.

| Item | Status | Notes |
|------|--------|-------|
| 1. Monitoring configured (error rate alert active) | [ ] | |
| 2. Latency alert configured | [ ] | |
| 3. Rollback plan tested in staging | [ ] | |
| 4. Error handling complete for all external dependencies | [ ] | |
| 5. No secrets hardcoded (verified by scan) | [ ] | |
| 6. Authentication tested adversarially (confirm unauthorized access is blocked) | [ ] | |
| 7. Load tested at 2× expected volume | [ ] | |
| 8. Postmortem template ready and linked | [ ] | |

**Launch approved by:** [Human solo developer] on [date]
```

### Template: 3-Section Postmortem

```markdown
# Postmortem: [Incident Name]

**Date of incident:** [date]
**Date of postmortem:** [date]
**Severity:** [customer-visible downtime / data issue / performance degradation / other]
**Duration:** [how long until resolved]

## Timeline
- [timestamp]: [what happened]
- [timestamp]: [what was detected / how]
- [timestamp]: [what was done]
- [timestamp]: [resolution]

## Root Cause Chain (Five Whys — chain to system, not person)
Why 1: [immediate symptom]
Why 2: [cause of symptom]
Why 3: [cause of cause]
Why 4: [underlying system/process issue]
Why 5 (root cause): [the systemic gap that allowed this]

## Corrective Actions
| Action | Owner | Due Date | Added to task list? |
|--------|-------|----------|---------------------|
| [specific action 1] | [me] | [date] | [yes] |
| [specific action 2] | [me] | [date] | [yes] |
```

### Agent Workflow Definitions

**Workflow 1: Working Backwards**
```
System: You are a solo developer's Working Backwards partner.
Task: The developer will give you a bullet-point idea. 
Step 1: Write a one-page draft press release using the provided template.
Step 2: Play the role of a skeptical, busy customer who doesn't care about the developer's excitement about the idea. Challenge every sentence in the press release. Ask: "So what?" "Why would I change what I do now?" "What specifically does this do that nothing else does?"
Step 3: Provide the challenge as a numbered list of objections.
Do not be kind. Do not encourage. Your job is to find the holes before any code is written.
```

**Workflow 3: Alternatives Generator**
```
System: You are a design decision advisor.
Task: The developer will describe a design decision they are about to make.
Step 1: Generate 3 genuinely different alternatives to their approach. Each alternative must be a real contender — not a strawman. Do not include the developer's chosen approach in the 3 alternatives.
Step 2: For each alternative, describe: (a) how it would work, (b) its strongest advantage over the developer's chosen approach, (c) its most significant drawback.
Step 3: Do NOT recommend which alternative to choose. Provide the information; the human decides.
```

**Workflow FCAR: Fresh Context Adversarial Review**
```
System: You are a document quality reviewer. You have no prior knowledge of this project.
Task: You will be given an artifact and an evaluation rubric.
Step 1: Read the rubric carefully.
Step 2: For each rubric item, evaluate the artifact against it.
Step 3: For each item that fails, quote the specific failing text from the artifact.
Step 4: Return a results table: [Rubric Item | Pass/Fail | Evidence (if fail)].
Do not suggest improvements. Do not be diplomatic. Your job is binary: pass or fail, with specific evidence.
```

---

## Worked Example A — AI-Powered Expense Tracker

**Running the complete assembled system end to end:**

**Step 1: Idea**
Raw idea: "An app that helps solo developers track their business expenses."

**Step 2: Working Backwards (Workflow 1)**
AI produces draft press release. Key claim: "Expense Tracker saves solo developers 30 minutes per month on receipt management." AI skeptical-customer challenge: "Why not just use a spreadsheet? Why would I install another app?" Human revises: the specific differentiator is automatic receipt categorization for common developer tool subscriptions.

**Step 3: PR/FAQ Gate**
Press release survives the customer challenge with the differentiator added. *[Gate 2: PASSED]*

**Step 4: Pitch Document**
Appetite: 5 days. Solution: receipt capture via email forwarding + automated categorization using a mapping of common developer subscriptions. Rabbit Hole: OCR scanning — too complex for a 5-day appetite. No-gos: mobile app, tax filing integration, team accounts.

**Step 5: Pitch Self-Approval**
5 days, email parsing + categorization + simple web UI. Realistic. *[Gate 3: PASSED — bet placed]*

**Step 6: Lightweight Design Note**
Triggered by: involves a data storage schema (external interface — irreversible once data exists) and an email parsing component. Two alternatives considered:
- **Alternative 1:** Direct bank API integration (e.g., Plaid) — Rejected because: requires PCI compliance review and user trust that is out of scope for this appetite.
- **Alternative 2:** CSV import — Rejected because: requires manual user action every month; the value proposition is automation.

*[This is a Reversible vs. Irreversible decision point: the email parsing interface is reversible; the database schema is IRREVERSIBLE once users have data in it. Classification stated: database schema decisions are irreversible — must be correct before any user data is stored.]*

FCAR run in fresh context. Result: All 5 rubric items pass. *[Gate 4: PASSED]*

**Step 7: Launch Checklist Pre-Check**
Items 1–7 checked before implementation begins. Item 7 (load test) marked as TBD — will be done before launch. *[Gate 5 pre-check: PASSED for pre-implementation items]*

**Step 8: Implementation**
Scopes identified: (A) Email ingestion, (B) Categorization engine, (C) Web UI, (D) Export to CSV. Uphill scopes (unknowns): A (email parsing edge cases), B (category-matching accuracy). Downhill scopes: C, D. Work uphill first: Scope A and B are implemented first.

*[Mid-build change-management event: During Scope B implementation, the developer discovers that the open-source developer-subscription list (the intended data source for categorization) is 3 years out of date and missing 60% of current tools. This is a requirement shift — the categorization will have lower coverage than assumed in the Pitch.]*

*Mid-build change protocol:* Stop. Open Pitch document. Append: "Change Event [date]: Discovered that the subscription mapping data is incomplete. Scope-hammering: categorization engine will match what it can and show an 'uncategorized' bucket for the rest. Accuracy is now a 'nice-to-have' metric, not a launch blocker. This is within the appetite."

**Step 9: Per-PR Quality Gate (Workflow 8)**
Each PR receives: automated linting (hard gate), AI style review against locked rubric, human review. The email parsing code is classified HIGH-STAKES (handles user financial data). AI draft is produced; human re-implements the core email parsing function independently and compares against the AI draft. The AI draft had a silent bug: it assumed all forwarded emails would be in plain text, missing HTML email bodies. *[The Phase 14 adversarial mechanism caught something: the silent bug in the AI draft's email parsing was revealed by the independent human re-implementation and comparison — this is the named instance where the adversarial mechanism works.]*

**Step 10: Launch Checklist**
All 8 items completed. Rollback threshold pre-committed: "If error rate on email ingestion exceeds 5% within 10 minutes of deploy, rollback immediately." *[Gate 6: PASSED]*

**Step 11: Deploy**
Deployed. Monitoring active. 10-minute observation window: error rate 0.3%. Deployment stable.

**Step 12: Monitoring + Post-Launch**
Weekly: email ingestion success rate, categorization hit rate, CSV export usage. These metrics were defined in the Pitch's success section before launch.

**Step 13: Iteration**
Next cycle: "improve categorization coverage" is a new Pitch, with its own appetite, entering the lifecycle at Step 3.

---

## Worked Example B — Batch Data-Processing Pipeline (no end users)

**Project:** A batch pipeline that nightly fetches open GitHub issues from a list of repositories, categorizes them by priority keyword, and writes a summary report to a Google Sheet.

**Key structural difference from Example A:** There are no end users. There is no UI. There is no real-time user-visible behavior. The system runs headlessly on a schedule.

**Step 1: Idea**
Raw idea: "Automate my weekly GitHub issue review."

**Step 2: Working Backwards**
AI skeptical-customer challenge fails here — there IS no customer. This is a personal automation tool with no external user. *The "press release" framing doesn't apply to this project type.* The Working Backwards workflow is replaced by: a simple "Problem Statement" — what manual task does this replace, how long does it currently take, and what is the appetite for building the automation?

*[Gap flagged honestly: the PR/FAQ / Working Backwards workflow assumes a product with external users. For a personal automation tool or headless pipeline, the press release is replaced by a Problem Statement + ROI calculation (how much time does the automation save vs. the time to build it?).]*

**Step 3: Pitch Document**
Appetite: 2 days. Problem: I spend 20 minutes every Monday reviewing GitHub issues across 8 repos. Solution: nightly batch job using GitHub API → keyword categorization → Google Sheets output. Rabbit Holes: building a UI dashboard (out of scope, a spreadsheet is sufficient). No-gos: real-time notifications, Slack integration, multi-user access.

**Step 4: Design Note**
Triggered by: involves an external API integration (GitHub) and a data output schema (Google Sheet structure is hard to change once established — IRREVERSIBLE decision).

Alternatives:
- **Alternative 1:** GitHub Actions + Slack bot — Rejected because: Slack requires a channel and adds notification overhead I don't want.
- **Alternative 2:** Local script run manually — Rejected because: this is what I already do; the value is in the automation.

*[UX Flows section: does NOT apply to this project. There is no user-facing flow. The "UX" for a batch pipeline is: (a) the input (scheduled trigger), (b) the output (spreadsheet), and (c) the error handling (what happens when GitHub API is down). These replace the UX flow documentation.]*

**Step 5: Implementation**
Scopes: (A) GitHub API fetching, (B) Keyword categorization logic, (C) Google Sheets output, (D) Error handling + alerting. Uphill scope: A (GitHub API rate limits — unknown behavior at scale). Downhill: B, C.

**Step 6: Quality Gate**
No user-facing code — no UX review. Stakes classification: A and D are MEDIUM-STAKES (external API, error handling), B and C are LOW-STAKES (pure logic and output formatting). Review tiered accordingly.

**Step 7: Launch Checklist**
*Items 5–7 change meaning for a headless pipeline:*
- Item 5 (no secrets hardcoded): Still applies — GitHub token must not be in code. [Check via scan]
- Item 6 (authentication tested adversarially): Replaced by: "Confirm what happens when the GitHub API returns 403 (rate limit) — the pipeline must handle this gracefully rather than silently failing."
- Item 7 (load test): Replaced by: "Test with all 8 repositories simultaneously — confirm the batch run completes within the scheduling window."

*[Gap flagged honestly: Items 6 and 7 of the standard Launch Checklist do not cleanly apply to a headless batch pipeline. The system must specify what they mean for non-user-facing workloads.]*

**Step 8: Deploy**
Deployed as a scheduled job. Observation window: run for the first 3 nights and manually verify the output spreadsheet is correct before relying on it.

**Step 9: Monitoring**
No user-visible error rate to monitor. Instead: pipeline success/failure alert (email if job fails), output spot-check (verify the spreadsheet has entries after each run).

---

## Worked Example B — Limitations Exposed

The following assumptions baked into Example A's system design do NOT cleanly apply to Example B:

1. **Press Release / Working Backwards** — assumes external users. For headless pipelines, replace with Problem Statement + ROI calculation.
2. **UX Flows** — assumes user-facing interactions. For headless pipelines, replace with Input/Output/Error specifications.
3. **Launch Checklist items 6–7** — "adversarial auth test" and "load test at 2× user volume" require reinterpretation for non-user-facing systems.
4. **Deployment monitoring (error rate metric)** — a user-facing error rate doesn't exist. Replace with job success/failure alert + output verification.
5. **A/B experimentation** — doesn't apply to a personal automation with no users to split.

**These are real limitations of the system, not patched over.** The system works best for user-facing software. For headless pipelines and personal tools, the lifecycle applies but several artifacts require adaptation:
- PR/FAQ → Problem Statement + ROI
- UX Flows → Input/Output/Error Spec
- Launch Checklist items 6–7 → Failure Handling Spec
- Deployment monitoring → Job health alerting + output verification

---

**Gate assessment:**

Neither worked example skips a step. Every step traces back to a specific prior phase finding. Example B exposes 5 specific assumptions from Example A that don't cleanly generalize — all 5 are named, with alternative approaches stated. No limitations are smoothed over.

**PHASE 15 GATE: PASSED.**

**The Solo AI Product Engineering System is complete.**
