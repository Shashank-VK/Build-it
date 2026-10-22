# Requirements, Product Specification & Scope (§6)

**Workstream:** spec-arch · **Research date:** 2026-10-10 · **Labels used below:** Verified / Corroborated / Inferred / Proposed / Unknown
**Evidence register:** see `04-evidence-register.md` for per-finding metadata (source, type, confidence, contradictions).

---

## 1. What a specification actually is

A spec turns a *validated opportunity* (someone has a problem worth solving) into a *buildable contract*: objectives, target users and use cases, user journeys, functional and non-functional requirements, business rules, acceptance criteria, dependencies, constraints, success metrics, risks/assumptions, explicit exclusions, and release requirements. **Inferred** from consistent structure across software-requirements practice: every element exists to answer one question from a different downstream consumer — PM (why, priority), designer (what the user experiences), engineer (what to build), tester (how to verify), AI agent (what is true and binding).

Two recurring empirical findings shape this whole file:

- Requirements failures are the largest single defect class in software work; teaching material summarizing decades of requirements-engineering literature puts requirements-origin defects at roughly 40–60% of all defects, and notes they are the most costly to fix because they propagate downstream (source: SE course notes, Bradley University — secondary interpretation, figures predate modern agile practice; treat as directionally established, not precise). **Label: Corroborated** (the direction, not the number).
- Type systems and static analysis mitigate only a fraction of real bugs. Gao et al. found ~15% of public JavaScript bugs preventable by static typing; Bogner & Merkel found TypeScript improved quality/readability without significantly reducing bug proneness; a 2026 arXiv study of the TypeScript ecosystem explains the gap: much of today's fault density lives in configuration, dependency, and testing layers — outside typing's scope. **Label: Verified.** Implication: no amount of type checking compensates for a weak spec. The spec is where defect prevention starts.

---

## 2. Anatomy of a complete spec

| Element | Answers | Owner | What goes wrong when missing |
|---|---|---|---|
| Objectives / problem statement | Why build this at all | PM | Team builds something impressive nobody asked for |
| Target users & use cases | Who, in what situation | PM/design | Generic design that fits nobody's actual workflow |
| User journeys | How they flow through it | Designer | Happy-path-only implementations; broken edge paths |
| Functional requirements (FRs) | What the system shall do | PM+eng | Rework when unstated behaviors collide |
| Non-functional requirements (NFRs) | Performance, security, scale, availability targets | PM+eng | "Works" but unusably slow/insecure; NFRs discovered post-launch under load |
| Business rules | Domain invariants and policy | PM/domain expert | Rules scattered in code, implemented inconsistently |
| Acceptance criteria | How we know it's done | PM/tester | Arguments at sign-off; "done" means different things per person |
| Dependencies | What this needs from others | Eng | Blocked mid-sprint on an API/asset nobody requested |
| Constraints | Time, budget, platform, legal | PM | Designs that can't ship (e.g., assume data we can't legally hold) |
| Success metrics | How we judge it in the wild | PM | No learning; can't tell launch from failure |
| Risks & assumptions | What could break the plan | All | Silent bets that explode (e.g., "the vendor API is stable") |
| Explicit exclusions | What's deliberately out | PM | Scope creep by misread; "I thought X was included" |
| Release requirements | Launch gates: docs, migration, rollback, support | Eng/PM | Launch day scrambles |

**Inferred:** this element list is a synthesis; no single source mandates all 13, but omissions map cleanly onto observed failure modes in community reports (search: "assumed requirements scope creep" patterns).

---

## 3. Writing requirements that survive contact with reality

### 3.1 EARS notation (Easy Approach to Requirements Syntax)

EARS is a constrained natural-language format from requirements engineering (Mavin et al.), adopted as the native notation of Amazon Kiro's spec-driven workflow (announced 2025; **Verified** via Wikipedia/EARS article and Kiro documentation references). Five patterns:

| Pattern | Form | Use |
|---|---|---|
| Ubiquitous | The system shall `<response>` | Always true |
| Event-driven | When `<trigger>`, the system shall `<response>` | Triggered by an event |
| State-driven | While `<state>`, the system shall `<response>` | Holds during a state |
| Optional | Where `<feature>` is enabled, the system shall `<response>` | Feature-flagged behavior |
| Unwanted | If `<trigger>`, then the system shall `<response>` | Error/exception handling |

Good (EARS): *"When a user submits the login form with an invalid email, the system shall display an inline validation error below the email field."*
Bad: *"The system should handle login."* — "should" is not a commitment; "handle" is not observable; no trigger, no response, no test.

### 3.2 Acceptance criteria: anatomy of good vs bad

- **Poor:** "Search results page should load quickly." **Better:** "Search results load within 2 seconds for 95% of requests under 1,000 concurrent users." (source: Bomberbot acceptance-criteria guide, citing VersionOne's State of Agile: 64% of teams cite poorly defined criteria as a challenge — community observations + secondary interpretation.)
- **Poor:** "Use Redis to cache sessions." **Better:** "The user remains logged in after closing and reopening the browser within a 30-minute window." — criteria describe *observable user outcomes*, not implementation. This keeps engineers and agents free to choose the mechanism while holding the behavior fixed. **Corroborated** across multiple guides.
- Gherkin (Given/When/Then) doubles as executable specification with BDD runners (Cucumber, SpecFlow, Behave); user-story level criteria should be scenario-structured so they map 1:1 to tests. (source: groundwork `requirements_research.md`, GitHub — first-hand practitioner notes.)

### 3.3 Non-functional requirements must be quantified

"Weak word" catalogs (QRA Corp requirements-writing guide — secondary interpretation, NASA-style lineage): words like *enhanced, fast, scalable, robust, user-friendly* are ambiguous unless paired with numbers. Strong NFR: "P95 API response time ≤ 300ms at 500 RPS; error budget ≤ 0.1% 5xx per day." Without quantification, NFRs are unenforceable and become the post-launch incident.

---

## 4. DELIVERABLE: Strong spec vs weak spec — concrete examples

Both specs describe the same realistic feature: **a weekly email digest of team activity for a small project-management SaaS ("TeamPulse weekly digest").**

### 4.1 The WEAK spec (what many teams actually write)

> **Feature:** Weekly digest email.
> **Description:** Send users a weekly email summarizing their team's activity. Should be nice-looking and engaging. Include the important stuff — completed tasks, overdue items, upcoming deadlines. Make it fast to generate. Users should be able to unsubscribe. Admins can configure it. We should support multiple languages eventually. Launch by end of quarter.

**What's wrong, element by element:**

1. *"Important stuff"* — no enumerated content. Designer includes a sparkline the engineer never planned; engineer includes raw counts the designer didn't design for. Consequence: mismatched build + design rework (**Corroborated** — recurring complaint in community postmortems).
2. *"Nice-looking and engaging"* — subjective, untestable. Sign-off argument guaranteed.
3. *"Fast to generate"* — NFR without numbers (see §3.3).
4. *"Users should be able to unsubscribe"* — scope ambiguity: footer link? preference page? one-click RFC 8058? Each costs different effort; agent/human implementers pick the cheapest, users complain.
5. *"Admins can configure it"* — configure what? Frequency? recipients? content blocks? An open door to a full settings surface.
6. *"Multiple languages eventually"* — "eventually" is scope creep wearing a coat. Either it's excluded (say so) or it's scoped (which languages, i18n framework).
7. *"Launch by end of quarter"* — date without the scope to match; pressures the team to cut silently rather than explicitly.

**Downstream consequences of the weak spec (traced end-to-end):**

- **Engineering:** implementer guesses content set → QA tests a different content set → production mismatch → hotfix week.
- **Design:** mocks a variant of the digest; engineering implements another; pixel-level churn.
- **AI agents:** an agent given this prompt produces plausible-but-wrong defaults (unsubscribe footer link, hardcoded English, no timezone handling). It fills ambiguity with invention — the "literal-minded but talented pair programmer" problem (Vocal Media SDD guide — secondary interpretation, consistent with agent failure reports).
- **Metrics:** no success metric → team can't tell if the digest drives engagement; no learning.
- **Scope:** "admins can configure" quietly becomes a 3-week settings project inside a 2-week feature.

### 4.2 The STRONG spec (same feature)

> **Feature:** TeamPulse weekly digest email — v1
>
> **Objective.** Re-engage dormant teams: raise weekly active-team rate from 41% → 50% within 8 weeks of launch. (Metric: teams with ≥1 non-owner action in trailing 7 days.)
>
> **Target users.** Team members on paid plans who received ≥1 digest-predecessor notification in the last 30 days. *Excludes:* free-plan users (no digests in v1), users with email bounces in last 90 days.
>
> **User journey.**
> 1. Monday 08:00 in the *team's* configured timezone, user receives "Your week at Acme" email.
> 2. Skims: completed tasks (count + top 3 by priority), overdue items (count, red badge), upcoming deadlines (next 7 days, max 5).
> 3. Clicks any item → deep-links to the item in the app, logged in (magic-link token, 24h expiry).
> 4. Footer: "Unsubscribe from digests" one-click link (RFC 8058 List-Unsubscribe + mailto). No preference center in v1.
>
> **Functional requirements (EARS).**
> - FR-1 (ubiquitous): The system shall generate one digest per team per week.
> - FR-2 (event-driven): When a digest is generated, the system shall include tasks completed in the trailing 7 calendar days.
> - FR-3 (state-driven): While a user has email-bounce status, the system shall skip that user.
> - FR-4 (unwanted): If digest generation fails for a team, then the system shall retry once after 30 minutes and log a `digest_failed` event; it shall not send a partial digest.
> - FR-5: The system shall resolve all timestamps in the team's configured timezone; teams without a configured timezone default to UTC.
>
> **Non-functional requirements.**
> - NFR-1: Digest generation completes within 15 minutes of the scheduled send time for 99% of teams; send pipeline P95 ≤ 5 min per 1,000 emails.
> - NFR-2: Bounce/complaint handling follows SES policies; complaint rate < 0.1%.
> - NFR-3: No PII beyond task titles/assignee names in email body; unsubscribe tokens unguessable (≥128-bit entropy).
>
> **Business rules.** BR-1: archived projects excluded from counts. BR-2: a team with zero activity still receives the digest ("Quiet week" variant) — do not skip, to preserve the re-engagement experiment.
>
> **Acceptance criteria.**
> - AC-1: Given a team with 12 completed, 3 overdue, 4 upcoming tasks, When the digest generates, Then the email contains counts (12/3/4), top-3 completed by priority, and exactly one unsubscribe footer link.
> - AC-2: Given a bounced user, When the digest generates, Then no email is sent and a `digest_skipped_bounce` event is logged.
> - AC-3: Given a generation failure, Then a retry occurs within 30–40 min and no partial email is ever sent (verified by sending pipeline idempotency key).
>
> **Dependencies.** Email provider account with dedicated sending domain (owner: infra); timezone field on Team model (blocked on schema change #482); copy review from marketing by T-2 weeks.
>
> **Constraints.** Must use existing SES account (no new vendor); no mobile-app push in v1; GDPR: one-click unsubscribe honored within 72h.
>
> **Success metrics.** Primary: weekly active-team rate 41%→50% in 8 weeks. Guardrail: unsubscribe rate < 2% per send; complaint rate < 0.1%.
>
> **Risks & assumptions.** Assumption: SES dedicated IP warm enough for volume spike (risk: throttling → verify with infra before build). Risk: magic-link tokens increase support load; mitigation: 24h expiry + "request new link" on expired landing page.
>
> **Explicit exclusions.** No preference center; no per-project digests; no i18n (English only in v1; templates structured for later translation); no free-plan users; no push notifications.
>
> **Release requirements.** Feature flag `digest_v1` (team-scoped rollout 5% → 50% → 100%); runbook for SES throttling; dashboard: sends, bounces, complaints, unsubscribe rate; rollback = flag off (no schema revert needed).

**Why this is strong:** every downstream consumer gets what they need — the designer has exact content blocks and a "quiet week" variant; the engineer has triggers, timezone rules, idempotency (AC-3), and NFR numbers; the tester has executable scenarios; the PM has the metric and guardrails; the AI agent has unambiguous SHALL statements with triggers, states, and error handling, plus exclusions that stop it from building a preference center or i18n. Deferred items (i18n, preference center, free-plan) are *named* as exclusions rather than silently half-built — "deferred is not deleted," with explicit re-entry triggers in the roadmap.

---

## 5. MVP vs deferred vs must-not-omit: deciding scope

**MoSCoW** (Corroborated across multiple practitioner skill references):

- **Must Have:** without it the product doesn't work or the hypothesis can't be tested. Ruthless bar: if >40% of features are "Must," the bar is too low. Legal/regulatory and safety items are automatic Musts.
- **Should Have:** important, painful to lack, but a workaround exists (e.g., in-app chat with driver → phone call works).
- **Could Have:** nice-to-have; build only with zero impact on Musts.
- **Won't Have:** explicitly excluded this cycle — naming them is what prevents scope creep.

**Complementary practices** (Inferred synthesis; each corroborated individually):

- **The cupcake, not a cake layer:** an MVP is a complete small experience, not an incomplete large one. Cut scope vertically (fewer users/flows, fully working) not horizontally (all flows, half-built).
- **Optimize for learning speed:** every feature must either test the hypothesis or be removed. "While we're at it / it would be easy to also / users will expect / competitors have" are scope-creep signals; answer each with "does this change our hypothesis?"
- **Risk-first sequencing:** build the riskiest Must Have first. If it fails, you learn early and cheaply.
- **Manual before automated:** concierge/Wizard-of-Oz MVPs are valid; don't build automation for the first 50 users' worth of a process.
- **One user segment:** MVPs serving multiple segments serve none well.
- **Deferred backlog with triggers:** "Build X when metric Y reaches Z" — reassures stakeholders without committing scope.
- **RICE as a tiebreaker** (Reach × Impact × Confidence ÷ Effort) for comparing many ideas — but not as an absolute rule; it ignores dependencies and its scoring is subjective.

**What "must-not-omit" catches:** safety, security, compliance, data recovery, and the acceptance criteria that define "done." These are the items teams most regret deferring because retrofitting them (encryption, audit trails, GDPR unsubscribe) costs 10–100× building them in.

---

## 6. Keeping requirements consistent across PMs, designers, engineers, testers — and AI agents

### 6.1 The core mechanism: one authoritative source of truth

- **Spec as source of truth, versioned with the code.** Spec-driven development (SDD) treats the spec as the governing artifact: design, implementation, tests, and governance all derive from it; code is an expression of the spec. (Sources: Sudhakar Punniyakotti / AI@Pace Medium piece; `stel1os/ai-sdd-sop` GitHub repo; jaig.bio SDD engagement — first-hand practitioner claims, community observations. **Label: Corroborated** as a described practice; the "81% improvement" style figures in LinkedIn marketing are **Unverified** marketing claims — do not cite.)
- **Numbered, traceable requirements** (FR-001…). Tests trace to FRs; code traces to design; every acceptance criterion maps to a test. The Jama Software piece describes this as the "Traceability Information Model": when an upstream requirement changes, downstream artifacts are marked suspect. **Inferred** as generally applicable even without a requirements-management platform: the principle is "single source + explicit links," not the tool.

### 6.2 Why AI agents make spec quality more important, not less

- Agents are "literal-minded but exceptionally talented pair programmers who need unambiguous instructions" (Vocal Media SDD guide — secondary interpretation). EARS notation exists precisely because constrained natural language is parseable by both humans and LLMs (Wikipedia EARS article, citing the SDD context — **Verified**).
- Practitioner rule from an AGENTS.md example: *"The result of generating code when you don't understand the requirements is code that passes a casual review but fails when it matters. Just say what's confusing and ask."* (jidechao/agentrag-openviking AGENTS.md — first-hand practitioner, GitHub.)
- Over-abstraction in agent-generated code is a distinct failure mode: agents default to interfaces around single implementations and plugin systems for known-fixed sets (agents-playbook anti-overengineering guide — first-hand practitioner, GitHub). A spec that names exclusions and fixes scope is the counterweight. See also "A Case Against Abstraction" (dev.to): over-abstracted code crippled even LLM collaboration — bug diagnosis 8–10× longer, onboarding 3–4 months vs 2–3 weeks. (Single-author community observation — **Corroborated** as a recurring pattern, not the exact multipliers.)

### 6.3 Practical consistency toolkit

1. **One spec document per feature**, committed in the repo (SPEC.md or `specs/`), reviewed before implementation — the SDD "Requirements → Design → Tasks" gate flow with human approval checkpoints (dev.to `ai-sdd` framework; angelsen/claude-kiro output-style — practitioner sources).
2. **Requirement IDs referenced in tests and PRs** — mechanical traceability.
3. **Shared glossary** — the same word (e.g., "team," "active") means the same thing to PM, designer, engineer, tester, agent. Many spec disputes are vocabulary disputes. **Inferred** from ambiguity literature.
4. **Design ↔ spec binding:** designs reference FR IDs; reviews check the design against acceptance criteria, not vibes.
5. **Change control on the spec:** when the spec changes mid-build, the change is explicit (diff + rationale), and downstream artifacts are re-verified — not silently reinterpreted.
6. **Machine-readable layers for agents:** AGENTS.md/SPEC.md pattern (AGENTS.md = how the project works; SPEC.md = what to build, numbered FRs; design docs = how per feature) — see `stel1os/ai-sdd-sop` document stack. **Proposed** as a good convention; **Corroborated** that multiple 2026 projects use variants.

---

## 7. Trade-offs and failure modes of specification itself (negative evidence)

- **Over-specification is its own failure mode.** A NASA-lineage requirements guide (via Slideshare/Scribd) cites DoD experience: over-specification — stating unnecessary or overly stringent requirements — is "the primary cause of cost overruns" in their programs. Example: requiring a high-fidelity star field where a simple visual background sufficed; duplicate 30-year-life requirements across system and segment levels. **Label: Corroborated** (multiple aerospace examples, old but structurally sound). Engineering implication: every requirement needs a "why" and a review gate; "nice to have" requirements get deleted when authors are asked to justify need.
- **Specs decay.** A living spec needs the cycle: people write → review/approve → agents/humans build → tests confirm → feedback updates the spec (LinkedIn SDD guide — marketing-flavored but the cycle is sound; **Inferred** as best practice).
- **Wrong-level precision:** specifying *implementation* in acceptance criteria ("use Redis") instead of *behavior* ("stay logged in 30 min") constrains solutions without adding clarity. Conversely, omitting genuinely needed technical constraints (must use existing SES) causes rework. The line: specify constraints that are real (legal, vendor, platform), outcomes that are behavioral, and leave mechanism open otherwise. **Inferred.**
- **AI-specific risk:** a spec written for humans ("handle login gracefully") reads as complete to a human but is a gap an agent fills by inventing. EARS-style SHALL statements with explicit triggers and error handling close the invention surface. **Inferred** from agent behavior reports; **Corroborated** by Kiro's design choice of EARS as native notation.
