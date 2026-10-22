# §23 — Practical Quality-Gate System

**Workstream:** quality (research only — read-only) · **Researched:** 2026-10-10
**Scope:** A gate for every lifecycle stage — discovery, spec, design, prototype, implementation, testing, security review, deployment, post-launch — each with required inputs, expected deliverables, validation checks, evidence of completion, critical failure conditions, responsible reviewer, automation opportunities, and exceptions/escalation. Plus the risk-level distinction (necessary vs recommended vs optional) and the evidence principle.
**Claim key:** Verified · Corroborated · Inferred · Proposed · Unknown

---

## 0. Governing principles (read first)

### 0.1 The evidence principle
**A passing build, green tests, a pretty screenshot, or an agent's "done" message must NEVER alone count as proof of readiness.** (Required by the commissioning brief; rationale Corroborated below.)

- A green test suite proves the tests passed — not that the tests are *strong*. Suites can pass vacuously: no assertions, conditional assertions, assertions weakened until they can't fail. This test smell is documented back to van Deursen et al. (2001) and is reproduced by LLM-generated tests (arXiv:2410.10628); the "iterate until green" loop pushes agents toward weakening assertions rather than fixing code (Corroborated — practitioner analysis).
- A screenshot proves pixels rendered — not that the design is right, the flow works, or the text is correct.
- An agent's "done" is a status message, not evidence. Evidence is an artifact a stranger could re-check: a named build, a test report with assertion counts, a signed review, a trace.
- Therefore every gate below names **evidence of completion** as a concrete artifact — not a feeling, not a checkbox.

### 0.2 Gate mechanics
Each gate has exactly three verdicts (Proposed, synthesized from release-checklist practice):
- **GO** — every in-scope item is checked, with evidence, or formally excepted by a named owner.
- **NO-GO** — a critical failure condition is present and not excepted. Work stops or rolls back.
- **NOT ASSESSED** — no blocker found, but something in scope could not be checked. This is *not* a pass; the gate names what is missing and what would make it checkable.

Precedence: **NO-GO > NOT ASSESSED > GO.** An unknown is never a pass.

### 0.3 Risk levels — necessary vs recommended vs optional
Controls are calibrated to product risk, not applied uniformly (Proposed framework; the "calibrate the bar to the product" principle is Corroborated by SRE/release-readiness practice):

| Risk tier | Example products | Control posture |
|---|---|---|
| **Tier 1 — High** | Payments, health, safety-critical, EAA/ADA-covered consumer services, auth/identity | All "necessary" controls below are mandatory; most "recommended" become mandatory; exceptions need executive + legal sign-off. |
| **Tier 2 — Standard** | General SaaS, content products, internal tools with many users | "Necessary" controls mandatory; "recommended" adopted by default, skippable with named owner + rationale. |
| **Tier 3 — Low** | Prototypes, internal tools, throwaway experiments | "Necessary" controls apply in lightweight form; "recommended" optional. |

Each gate table marks every control **N** (necessary at Tier 1; mandatory at Tier 2 unless excepted), **R** (recommended), or **O** (optional enhancement).

### 0.4 Parallel tracks, not phases
QA, security, and operational readiness work starts when implementation starts — not after a build is "done." Testing and environment readiness are background tracks that finish *alongside* development, each with a named owner (Corroborated — delivery-framework practice). The gates below are decision points on those tracks, not the tracks themselves.

---

## 1. Gate 1 — Discovery

| Element | Content |
|---|---|
| **Required inputs** | Problem statement; affected user segments (including users of assistive technology, low-bandwidth, older devices); success metrics; known constraints (legal regimes that apply — EAA? ADA Title II? 508?); prior research or data. |
| **Expected deliverables** | Discovery brief: problem, users, hypotheses, risks, open questions, decision log. Explicit statement of which accessibility/legal regimes apply (N at Tier 1). |
| **Validation checks** | N: Are disabled users represented in the user segments? R: Were at least two independent evidence sources consulted (not just stakeholder opinion)? O: Competitive accessibility benchmark. |
| **Evidence of completion** | Written brief, dated, with named author; decision log entries. |
| **Critical failure conditions** | No identifiable user or problem (solution in search of a problem); applicable legal regime unidentified for a Tier 1 product; discovery skipped entirely for a Tier 1 change. |
| **Responsible reviewer** | Product lead (N); legal/compliance consulted for Tier 1 (R). |
| **Automation opportunities** | Low. Analytics pulls and survey tooling can feed inputs; judgment stays human. |
| **Exceptions / escalation** | Time-boxed spike work may pass with a "thin brief" if the reviewer records what's deferred; Tier 1 legal-scope questions escalate to counsel, never waived by product alone. |

---

## 2. Gate 2 — Spec (requirements)

| Element | Content |
|---|---|
| **Required inputs** | Discovery brief; scope boundaries; non-functional requirements (performance budgets, accessibility target, e.g. "WCAG 2.2 AA"). |
| **Expected deliverables** | Written spec: user stories or job statements with **acceptance criteria per story**; explicit non-functional requirements; out-of-scope list; error/edge-case handling specified (not "TBD"). |
| **Validation checks** | N: Every story has testable acceptance criteria (no "works well," no "fast"). N (Tier 1): accessibility acceptance criteria named (keyboard, SR, contrast, zoom). R: Each criterion maps to a verification method (which test, which reviewer). O: Formal counterexample review ("how could this criterion pass while the feature is broken?"). |
| **Evidence of completion** | Spec document under version control; acceptance criteria checklist; reviewer sign-off comment. |
| **Critical failure conditions** | Acceptance criteria missing or untestable; accessibility criteria absent for a Tier 1/2 consumer product; scope ambiguous enough that two engineers would build different things. |
| **Responsible reviewer** | Product lead + engineering lead (N); accessibility reviewer for Tier 1 (R→N at Tier 1). |
| **Automation opportunities** | Lint specs for weasel words ("user-friendly," "seamless," "robust") — Proposed technique; cheap and surprisingly effective. Traceability tooling linking stories to tests. |
| **Exceptions / escalation** | "Conditional pass": proceed with named open items, each with an owner and a date — the honest middle state between ready and blocked (Corroborated delivery practice). Unowned open items = NO-GO. |

---

## 3. Gate 3 — Design

| Element | Content |
|---|---|
| **Required inputs** | Approved spec; design system / tokens; brand constraints; content inventory for the surfaces in scope. |
| **Expected deliverables** | Designs for all states: default, loading, **empty, error, and destructive-confirmation states** (N — these are the states most often never designed); responsive breakpoints; focus/hover/disabled/error component states; content and microcopy (realistic, not lorem). |
| **Validation checks** | N: Every screen has its empty/error/loading variants designed. N: Focus indicators and keyboard interaction specified for custom components. R: Contrast checked on actual color pairs (not eyeballed). R: Designs reviewed against the APG patterns for dialogs/menus. O: Reduced-motion variant specified. |
| **Evidence of completion** | Design file or annotated exports covering all states; contrast-check record; design-review sign-off. |
| **Critical failure conditions** | Core flows designed only for the happy path; no error/empty states; custom interactive components with no keyboard spec; text contrast failing WCAG AA on primary surfaces. |
| **Responsible reviewer** | Design lead (N); accessibility reviewer for component patterns (R). |
| **Automation opportunities** | Design-token contrast checkers; Figma/Sketch accessibility annotation plugins; screenshot-diff of design iterations. |
| **Exceptions / escalation** | Decorative or Tier 3 surfaces may defer non-critical states with a recorded follow-up ticket; core-flow states are never deferred at Tier 1. |

---

## 4. Gate 4 — Prototype

| Element | Content |
|---|---|
| **Required inputs** | Designs; the riskiest assumption named in writing (technical, usability, or desirability). |
| **Expected deliverables** | A prototype that exercises *only* the riskiest assumption, plus a written record of what was learned and what was decided. |
| **Validation checks** | N: The prototype actually tests the named risk (not a polished demo of the easy parts). R: Tested with at least one representative user — including an assistive-technology user if the risk touches interaction. O: Instrumented with the metric that would falsify the hypothesis. |
| **Evidence of completion** | Prototype link/build + learnings memo with a go / pivot / kill decision and named decider. |
| **Critical failure conditions** | Prototype "validates" the idea without touching the risk; learnings memo missing (prototype becomes shadow production code); usability risk untested for a Tier 1 consumer flow. |
| **Responsible reviewer** | Product lead (N). |
| **Automation opportunities** | Minimal — prototypes are throwaway by design. Analytics snippet if the risk is behavioral. |
| **Exceptions / escalation** | Low-risk internal tools may skip prototyping with a one-line recorded rationale; Tier 1 novel interactions may not. |

---

## 5. Gate 5 — Implementation

| Element | Content |
|---|---|
| **Required inputs** | Spec (Gate 2 GO), designs incl. all states (Gate 3 GO), engineering environment, CI pipeline. |
| **Expected deliverables** | Working code behind the spec; unit + integration tests; updated docs; no TODO/FIXME in shipped paths without a ticket. |
| **Validation checks** | N: CI green **on the exact artifact** (not "tests passed on a different commit"). N: Static analysis + dependency vulnerability scan clean or triaged. N: axe-core run on changed pages — zero new *violations*. R: Test review for assertion strength (would this test fail if the code were wrong? — the anti-vacuity check). R: Keyboard walk-through of changed flows before merge. O: Mutation testing on critical logic. |
| **Evidence of completion** | CI run linked to the commit hash; scan reports; axe report; code-review approval by a human reviewer (an agent's approval is not evidence — see §0.1). |
| **Critical failure conditions** | CI red or skipped; known S1/S2 defect merged; new axe violations; secrets/credentials in code; unreviewed merge to a release branch. |
| **Responsible reviewer** | Engineering lead / code reviewer (N); security reviewer for auth/crypto/payment code (N at Tier 1). |
| **Automation opportunities** | High: CI pipelines, linters, SAST/dependency scanning, axe-core in CI, preview deployments per PR, automated visual snapshots of changed components. |
| **Exceptions / escalation** | Emergency hotfix lane: may merge with post-hoc review within 24h, named owner, and a follow-up ticket; the lane's use is itself audited. |

---

## 6. Gate 6 — Testing (functional + accessibility + performance)

| Element | Content |
|---|---|
| **Required inputs** | Release candidate build (frozen scope — no commits after testing starts without re-running affected checks); test plan; seeded test data; device/browser matrix. |
| **Expected deliverables** | Executed test report: pass/fail per case **with evidence** (traces, screenshots, logs); defect log with severities; accessibility test record (auto + keyboard + SR tiers); performance measurements vs budget. |
| **Validation checks** | N: Scope freeze recorded (ticket list + tagged commit range); late additions re-trigger affected tests (Corroborated release-checklist practice). N: Full §21 interaction inventory exercised on the candidate (routes, buttons, forms, dialogs, auth, payments in sandbox, error/empty states via fault injection). N: Regression suite green; flaky-test quarantine — any test passing only on retry is a defect, not a pass. R: Cross-browser/device matrix per the supported list. R: Screen-reader task completion on core flows (2 pairings). O: Exploratory testing session, load/soak test. |
| **Evidence of completion** | Test report artifact with build ID; defect log; accessibility record; performance numbers; named test lead sign-off. |
| **Critical failure conditions** | Unresolved S1/S2 defects; scope changed mid-test without re-verification; accessibility tier 2/3 skipped for a Tier 1 product; performance budget breached on a core flow without an approved exception. |
| **Responsible reviewer** | Test/QA lead (N); product lead accepts residual S3/S4s in writing (R). |
| **Automation opportunities** | Very high: e2e suites (Playwright/Cypress), visual regression, link crawlers, axe-core, performance budgets in CI (Lighthouse CI), fault-injection harnesses. But see §0.1: the suite's *strength* is itself reviewed. |
| **Exceptions / escalation** | S3/S4 deferrals need named owner + ticket + product sign-off; S1/S2 deferral at Tier 1 needs executive + (where legal regimes apply) legal sign-off. |

---

## 7. Gate 7 — Security review

| Element | Content |
|---|---|
| **Required inputs** | Threat model (or explicit statement that the change is out of threat-model scope, with rationale); architecture/data-flow diagram for changed surfaces; dependency list. |
| **Expected deliverables** | Review record: threats considered, findings with severity, remediation or risk acceptance per finding. |
| **Validation checks** | N: No unresolved high/critical findings on the release path. N: Secrets handling, authZ checks, input validation on changed endpoints verified (not assumed). R: Third-party/integration failure modes reviewed (what happens when the vendor is down or hostile). O: Penetration test for Tier 1 launches. |
| **Evidence of completion** | Signed review record naming reviewer, date, scope, and residual risks accepted. |
| **Critical failure conditions** | Open high/critical finding; auth/payment/crypto change without security reviewer; known-vulnerable dependency on the release path. |
| **Responsible reviewer** | Security lead (N at Tier 1; R at Tier 2 — Tier 3 may use checklist self-review). |
| **Automation opportunities** | SAST/DAST/dependency scanning in CI; secret scanning on push; license scanning. Automation finds known-bad patterns; the review judges design-level risk. |
| **Exceptions / escalation** | Risk acceptance must be written, time-boxed, and signed by the security lead + product owner; silent acceptance is a NO-GO. |

---

## 8. Gate 8 — Deployment

| Element | Content |
|---|---|
| **Required inputs** | Release candidate with Gates 5–7 GO/NOT-ASSESSED-resolved; rollout plan; rollback plan; migration plan; feature-flag map; on-call roster. |
| **Expected deliverables** | Deployed release to the planned exposure (staged/canary/blue-green for Tier 1 — not big-bang on a critical service); deploy log; post-deploy smoke test result. |
| **Validation checks** | N: Immutable artifact promoted through stages (not rebuilt at deploy). N: **Tested rollback path** — restore meets RPO/RTO, rehearsed not just documented. N: DB migrations backward-compatible and reversible. N: Smoke tests on the live candidate. R: Feature flags for risky changes; deploy annotations on dashboards. O: Automated canary analysis. |
| **Evidence of completion** | Deploy log with artifact checksum; rollback rehearsal record; smoke-test result; monitoring dashboard link showing the release. |
| **Critical failure conditions** | No rollback path; untested restore; migration not reversible; deploy of an artifact different from the tested one; Tier 1 big-bang deploy without staged exposure. |
| **Responsible reviewer** | Engineering lead / SRE (N); on-call acknowledged and briefed (N). |
| **Automation opportunities** | Very high: progressive delivery tooling, automated rollback triggers on SLO breach, migration dry-runs, smoke-test jobs post-deploy. |
| **Exceptions / escalation** | Emergency deploys may compress staging but never skip the rollback check; the exception and its owner are logged. |

---

## 9. Gate 9 — Post-launch

| Element | Content |
|---|---|
| **Required inputs** | Live traffic; monitoring/alerting; support channel; the success metrics from Gate 1. |
| **Expected deliverables** | Launch watch report (error rates, latency, business metrics vs baseline); incident log; accessibility/quality follow-up tickets filed from real usage; retrospective notes. |
| **Validation checks** | N: Alerts that would catch *this release* going wrong exist and fired correctly in staging (alert coverage is tested, not assumed). N: Error budgets/SLOs defined; a bad deploy has a named rollback decider. R: Real-user monitoring segmented by device/assistive-tech where possible. R: Support-ticket triage for accessibility reports within SLA. O: Post-launch accessibility spot-check with a screen-reader user. |
| **Evidence of completion** | Watch report for the launch window; incident/rollback log (even if empty — "no incidents" is a recorded observation, not an assumption); retrospective with action items. |
| **Critical failure conditions** | No monitoring on new failure modes; alert fatigue ignored (alerts firing and unactioned); S1 incident without a blameless postmortem; accessibility complaints routed to /dev/null. |
| **Responsible reviewer** | On-call/SRE lead for the watch window (N); product lead for the retrospective (R). |
| **Automation opportunities** | High: SLO/error-budget tracking, anomaly detection, synthetic monitoring of core flows, automated accessibility rescans on a schedule (regression, not proof). |
| **Exceptions / escalation** | Watch-window length scales with risk (hours for Tier 3, days+ for Tier 1); shortening it needs engineering-lead sign-off. |

---

## 10. The gate summary table

| Gate | Inputs → Deliverables | Evidence | Critical failure | Reviewer | Automation |
|---|---|---|---|---|---|
| 1 Discovery | problem/users/constraints → brief + legal-scope statement | dated brief, decision log | no user/problem; legal scope unknown (T1) | Product lead | Low |
| 2 Spec | brief → stories with testable acceptance criteria | versioned spec, criteria checklist | untestable criteria; no a11y criteria (T1/2) | Product + Eng leads | Spec linting, traceability |
| 3 Design | spec → all states designed (incl. empty/error) | state coverage, contrast record | happy-path-only; no keyboard spec | Design lead | Token contrast checks |
| 4 Prototype | riskiest assumption → learnings + decision | memo with go/pivot/kill | risk untested; memo missing | Product lead | Minimal |
| 5 Implementation | spec/design → code + tests on frozen CI | CI on exact hash, scans, axe, human review | red CI; new axe violations; secrets | Eng lead / reviewer | CI, SAST, axe, previews |
| 6 Testing | frozen RC → test report + defect log | report with build ID, a11y record | open S1/S2; scope drift; a11y skipped (T1) | QA lead | e2e, visual, crawlers, perf |
| 7 Security review | threat model → signed review record | reviewer/date/scope/residual risks | open high/crit; unreviewed auth/payment | Security lead | SAST/DAST/secrets scans |
| 8 Deployment | GO RC → staged deploy + smoke test | deploy log, rollback rehearsal | no rollback; artifact mismatch | Eng/SRE lead | Progressive delivery, auto-rollback |
| 9 Post-launch | live traffic → watch report + retro | watch report, incident log | no monitoring; unactioned alerts | SRE + Product | SLOs, synthetics, rescans |

---

## 11. Necessary vs recommended vs optional — worked example

For a **Tier 1** product (EAA-covered e-commerce checkout), the non-negotiable set includes: legal-scope identification (G1); accessibility acceptance criteria (G2); all-states design incl. error/empty (G3); axe-zero-new-violations + human code review (G5); full §21 inventory test + keyboard + screen-reader passes + scope freeze (G6); security review of payment/auth (G7); tested rollback + staged rollout (G8); alert coverage + launch watch (G9).

For a **Tier 3** internal prototype, the same gates run in lightweight form: a thin brief (G1), testable criteria (G2), happy-path design plus error states for the demoed flow (G3), CI green (G5), smoke test (G6/G8), and a note saying what was skipped and why. The gates are never *absent* — they scale.

**Optional enhancements** (adopt when the team has slack, never as gate requirements): mutation testing, formal counterexample review of acceptance criteria, competitive accessibility benchmarks, pen tests on non-Tier-1 launches, post-launch SR-user spot checks. These improve quality but must not become checkbox theater that delays the necessary controls.
