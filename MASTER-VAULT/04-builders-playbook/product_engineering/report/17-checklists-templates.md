# 17 — Checklists & Templates

**Status:** report section; read-only synthesis, not adoption advice. **Source:** `research/rules/04-templates/` (18 fill-in-ready templates), `research/discovery/01-problem-discovery.md` (problem-discovery checklist §6, decision-criteria gate §7), `research/discovery/03-validation.md` (validation stage gates §6.2), `research/quality/03-quality-gates.md` (the 9 quality gates). Claim labels preserved (**Verified / Corroborated / Inferred / Proposed / Unknown**). This section is the *index plus the highest-leverage checklists in full* — the remaining templates are described with pointers, not duplicated, so this section stays readable.

**How to use this section:** run the gates in lifecycle order — discovery → spec → design → prototype → implementation → testing → security → deployment → post-launch. Every template ends with acceptance criteria; the filled template is done when the criteria are met, not when the sections are full. *Italic text in a template is a prompt — delete the prompt, keep your answer. `[ ]` checkboxes are literal. "N/A with reason" is always acceptable — but the reason must be written down.*

---

## 1. Problem-discovery checklist (in full)

*Source: `research/discovery/01-problem-discovery.md` §6. Use as a gate review before any solution work begins. Every row must be satisfiable with a pointer to actual evidence.*

| # | Checkpoint | Evidence required | Kill/continue rule |
|---|---|---|---|
| 1 | Segment named | Written description of *who* (role, context, budget authority) | Can't name them → stop, do 5 more interviews |
| 2 | Problem stated in their words | 5–10 story-based interview notes with specific past incidents | Only opinions collected → stop, re-run as story interviews |
| 3 | Priced pain | Workaround described with time/money cost, or budget line identified | No priced pain after 10 interviews → reject |
| 4 | Root cause diagnosed | Each "why" in the chain backed by observed data | Cause is speculation → research more before solutioning |
| 5 | Frequency & trend | Behavioral data or repeated interview reports; direction (growing/stable/shrinking) | Rare and shrinking → defer |
| 6 | "Why now" answered | Named market/tech/regulatory change, or evidence it's newly solvable | No "why now" → flag as high timing risk |
| 7 | Demand vs. assumption separated | At least one commitment signal (time, reputation, data, money) beyond compliments | Only compliments → stop; run a commitment test |
| 8 | Differentiation hypothesis | Written answer to "why would someone switch to us" that isn't cosmetic | Cosmetic only → reject or reframe the problem |
| 9 | Commercial viability sketched | Rough WTP range, reachable channel, cost-to-serve estimate | Math can't work → reject |
| 10 | Kill criterion pre-committed | Written statement of what evidence would kill this problem framing | No kill criterion → do not proceed (bias protection) |
| 11 | Four risks triaged | Value, usability, feasibility, viability each rated high/med/low uncertainty with owner | Value or viability risk unexamined → research more |
| 12 | Decision: proceed / pivot / reject | Dated decision with evidence pointers, signed by the product trio | No decision → discovery theater |

**Discovery theater** — the failure mode where interviews happen but never change a decision [community observations]. Row 12 exists specifically to prevent it: discovery that cannot produce a *no* is not discovery.

---

## 2. Decision-criteria gate (in full)

*Source: `research/discovery/01-problem-discovery.md` §7. Apply after the checklist. Score each criterion; the decision follows the **lowest** score, not the average.*

| Criterion | Pass | Conditional (research more) | Fail (reject/pivot) |
|---|---|---|---|
| **Problem reality** | ≥5 independent story-based accounts of specific past pain in the named segment | 2–4 accounts, or accounts outside the named segment | <2 accounts after genuine effort, or pain described only hypothetically |
| **Pain priced** | Workaround cost or budget quantified by the customer | Cost implied but not quantified | No cost anyone will name |
| **Root-cause confidence** | Cause confirmed by observation or behavioral data, not just self-report | Plausible cause, single evidence type | Competing causes, no way to distinguish cheaply |
| **Demand signal** | Commitment observed (time, reputation, data, money) | Interest expressed by credible buyers without commitment | Politeness only; "interesting" with no follow-through |
| **Differentiation** | 10× on the thing they care about, or an unserved job | Parity with a credible wedge (distribution, price, focus) | Cosmetic; incumbent copies in a quarter |
| **Commercial viability** | WTP × reachable buyers > cost-to-serve + cost-to-acquire with margin | One variable unproven but testable cheaply | Math fails on verified numbers |
| **Timing** | Named "why now" with evidence | Timing neutral | Headwind: regulation, platform, or market moving against |

**Decision rule (Proposed):** Any single **Fail** → reject the problem framing or pivot to an adjacent one; do not "research more" around a failed criterion unless you can name the specific cheaper test that would change it. Two or more **Conditional** → time-boxed research sprint (≤2 weeks) with pre-committed kill criteria, then re-gate. All **Pass/Conditional** → proceed to ideation with the conditionals recorded as the riskiest assumptions to test first in validation.

---

## 3. Validation stage gates (in full)

*Source: `research/discovery/03-validation.md` §6.2. Apply per experiment and per idea (aggregating experiments). Thresholds below are illustrative defaults — each team must pre-commit its own numbers before running the test; the structure, not the specific values, is the deliverable.*

### 3.1 Per-experiment verdicts

| Verdict | Condition | Next action |
|---|---|---|
| **Validated** | Pre-committed success criterion met, on a representative sample, with the primary metric moving and guardrails intact | Promote the assumption to "holds for now"; attack the next-riskiest assumption |
| **Invalidated** | Pre-committed kill criterion triggered, or success criterion missed by a wide margin with no sampling excuse | Kill the solution framing; return to the opportunity or pivot the problem |
| **Inconclusive** | Result lands between success and kill lines, or a sampling/method flaw is discovered | Run *one* cheaper follow-up test targeting the ambiguity — not a bigger version of the same test. Two consecutive inconclusives = treat as invalidated (the market is telling you it doesn't care enough to give a clear signal) |

### 3.2 Per-idea stage gates

| Gate | Proceed | Revise | Research more | Stop |
|---|---|---|---|---|
| **Problem → Ideation** | Problem gate passed (§2 above): priced pain, named segment, demand signal | Opportunity real but solution space mis-shaped; re-ideate with new constraints | ≥2 conditional criteria; time-boxed ≤2-week sprint with kill criteria | Kill criterion hit: no priced pain, unworkable economics, cosmetic differentiation |
| **Idea → Prototype** | Riskiest assumption identified; cheapest test designed; success/kill criteria pre-committed | Assumption test shows the *mechanism* is wrong but adjacent mechanism plausible | Key dimension is Unknown and testable cheaply (spike, 5 interviews) | Feasibility spike fails with no alternative path; or value test shows nobody cares |
| **Prototype → Build** | Value + usability evidenced (behavioral/commitment, not opinion); feasibility spike passed; viability math works on verified numbers | Usability fails but value holds → redesign, re-test usability only | Viability input (WTP, CAC) still estimated → pricing/pilot test first | Paid-pilot or prepayment test fails; Sean Ellis <25% with no segment story; unit economics fail on measured costs |
| **Build → Scale** | Retention/expansion in cohort; repeatable acquisition motion; economics improve with scale | Works for one segment, not the next → segment deliberately, don't generalize | Scale unknowns (support load, infra cost curve) → instrumented limited rollout | Retention flatlines; acquisition costs rise faster than value; the "growth" is bought, not earned |

### 3.3 The stop discipline

1. **Stop on evidence, not on feelings.** The kill criteria were pre-committed precisely so that sunk cost can't vote. Sunk cost is not a reason to continue; it's the reason the criteria were written down beforehand.
2. **Distinguish "stop the solution" from "stop the problem."** Most stops should be solution-stops: the opportunity survives, the approach doesn't. Only stop the problem when the decision-criteria gate (§2) fails.
3. **Write the postmortem while it's fresh.** What was believed, what was tested, what was learned, what would change the decision. Future ideas will rhyme with this one; the record is the asset.

---

## 4. Quality-gate tables (condensed)

*Source: `research/quality/03-quality-gates.md`. A gate for every lifecycle stage. Each gate has exactly three verdicts (Proposed): **GO** — every in-scope item checked with evidence, or formally excepted by a named owner; **NO-GO** — a critical failure condition present and not excepted; **NOT ASSESSED** — something in scope could not be checked (not a pass; the gate names what is missing). Precedence: **NO-GO > NOT ASSESSED > GO.** An unknown is never a pass.*

### 4.1 The evidence principle (read first)

**A passing build, green tests, a pretty screenshot, or an agent's "done" message must NEVER alone count as proof of readiness** (Corroborated rationale): a green suite proves the tests passed — not that the tests are *strong* (suites can pass vacuously; LLM-generated tests reproduce this test smell, and the "iterate until green" loop pushes agents toward weakening assertions rather than fixing code — Corroborated); a screenshot proves pixels rendered, not that the flow works; an agent's "done" is a status message, not evidence. **Evidence is an artifact a stranger could re-check:** a named build, a test report with assertion counts, a signed review, a trace.

### 4.2 Risk tiers (Proposed framework; calibration principle Corroborated)

| Risk tier | Example products | Control posture |
|---|---|---|
| **Tier 1 — High** | Payments, health, safety-critical, EAA/ADA-covered consumer services, auth/identity | All "necessary" controls mandatory; most "recommended" become mandatory; exceptions need executive + legal sign-off |
| **Tier 2 — Standard** | General SaaS, content products, internal tools with many users | "Necessary" controls mandatory; "recommended" adopted by default, skippable with named owner + rationale |
| **Tier 3 — Low** | Prototypes, internal tools, throwaway experiments | "Necessary" controls apply in lightweight form; "recommended" optional |

### 4.3 The nine gates, condensed

**N** = necessary at Tier 1 (mandatory at Tier 2 unless excepted) · **R** = recommended · **O** = optional enhancement.

| Gate | Inputs → Deliverables | Evidence | Critical failure | Reviewer |
|---|---|---|---|---|
| **1 Discovery** | problem/users/constraints → brief + legal-scope statement | Dated brief, decision log | No user/problem; legal scope unknown (Tier 1) | Product lead (N); legal for Tier 1 (R) |
| **2 Spec** | Brief → stories with **testable acceptance criteria** | Versioned spec, criteria checklist | Untestable criteria; no a11y criteria (Tier 1/2); scope ambiguous enough that two engineers would build different things | Product + Eng leads (N) |
| **3 Design** | Spec → **all states designed**: default, loading, empty, error, destructive-confirm | State coverage, contrast record | Happy-path-only design; no keyboard spec for custom components; contrast failing WCAG AA on primary surfaces | Design lead (N) |
| **4 Prototype** | Riskiest assumption named → prototype + learnings memo + go/pivot/kill decision | Memo with decision and named decider | Prototype "validates" without touching the risk; learnings memo missing | Product lead (N) |
| **5 Implementation** | Spec/design → code + tests on frozen CI | CI run on the **exact commit hash**; scan reports; axe report; **human** code-review approval (an agent's approval is not evidence) | CI red or skipped; new axe violations; secrets in code; unreviewed merge to a release branch | Eng lead / reviewer (N) |
| **6 Testing** | Frozen RC → test report + defect log | Report with build ID; defect log; a11y record; performance numbers | Open S1/S2; scope changed mid-test without re-verification; a11y skipped (Tier 1); flaky tests counted as passes (any test passing only on retry is a defect) | QA lead (N) |
| **7 Security review** | Threat model → signed review record | Reviewer, date, scope, residual risks named | Open high/critical finding; auth/payment/crypto change without a security reviewer; known-vulnerable dependency on the release path | Security lead (N at Tier 1) |
| **8 Deployment** | GO RC → staged deploy + smoke test | Deploy log with artifact checksum; rollback rehearsal record; smoke-test result | No rollback path; untested restore; artifact mismatch (deployed ≠ tested); Tier 1 big-bang without staged exposure | Eng/SRE lead (N); on-call briefed (N) |
| **9 Post-launch** | Live traffic → watch report + retro | Watch report; incident/rollback log (even if empty — "no incidents" is a recorded observation); retro with action items | No monitoring on new failure modes; alerts firing and unactioned; S1 without a blameless postmortem | SRE lead for the window (N); Product for the retro (R) |

**Worked calibration:** a Tier 1 checkout needs legal-scope ID (G1), accessibility acceptance criteria (G2), all-states design (G3), axe-zero-new-violations + human review (G5), full inventory test + keyboard + screen-reader passes + scope freeze (G6), payment/auth security review (G7), tested rollback + staged rollout (G8), alert coverage + launch watch (G9). A Tier 3 internal prototype runs the same gates lightweight: thin brief, testable criteria, error states for the demoed flow, CI green, smoke test, and a note saying what was skipped and why. **The gates are never absent — they scale.**

---

## 5. Product-authenticity & polish checklist (in full)

*Source: `research/rules/04-templates/17-product-authenticity-polish.md`. Use before any user-facing launch or demo that represents the product. "Authentic" = what the user sees is what the product is; "polished" = the details hold up under attention. Check literally — a Gawande-style killer-items list. Blocks AP-03, AP-12/13/15, AP-14, AP-08.*

### 5.1 Visual identity
- [ ] Logo, name, and visual language consistent across every surface (no mixed identities)
- [ ] No default-framework styling visible where the brand should be
- [ ] Favicon, title tags, and social/OG metadata present and correct
- [ ] Visual quality holds at the marketing surface *and* three clicks deep

### 5.2 Functional completeness
- [ ] Every visible control does something real — no dead buttons, dead links, decorative inputs
- [ ] Every advertised capability works on real data
- [ ] No "coming soon" placeholders on primary flows (or they're honest, dated, and rare)
- [ ] Permissions/roles actually enforced, not just hidden in the UI

### 5.3 Responsive
- [ ] Core flows verified at 360px / 768px / 1280px on a real device
- [ ] No horizontal scroll, no overlapping text, no unreachable controls at any width
- [ ] Touch targets and hover-independence verified on mobile

### 5.4 Accessibility
- [ ] Keyboard-only completion of core flows
- [ ] Focus visible; semantic markup; icon-only controls named
- [ ] Contrast AA on body text; reduced-motion respected
- [ ] Form errors associated and announced

### 5.5 Content quality
- [ ] Zero lorem ipsum, TODO, or placeholder copy anywhere user-visible
- [ ] Copy is in the user's language — no developer jargon in user-facing text
- [ ] Empty states are helpful (explain + next action), not blank
- [ ] Dates, numbers, currencies localised

### 5.6 Realistic demos
- [ ] Demo uses production-shaped data, not perfect fixtures
- [ ] Simulated capabilities disclosed wherever the demo is shown
- [ ] The demo path is a real code path — no demo-only branches

### 5.7 UX states
- [ ] Loading, empty, error, offline, permission-denied, rate-limited, destructive-confirm, and success states all designed and verified

### 5.8 Security
- [ ] ASVS L1 gap register complete for the launched surface
- [ ] No secrets in client-visible code, URLs, or error messages
- [ ] Auth and session behaviour sane (logout works, sessions expire, passwords handled per ASVS)

### 5.9 Privacy
- [ ] Data collection disclosed; consent where required
- [ ] Minimum-necessary data actually practised (no speculative harvesting)
- [ ] Data deletion / export path exists where regulation or promise requires
- [ ] Third-party scripts/trackers inventoried and justified

### 5.10 Trust
- [ ] Pricing/fees shown honestly — no drip pricing or hidden costs
- [ ] Claims on the marketing surface are true of the product *today* (AP-14)
- [ ] Contact/support path real and monitored; status page exists if uptime is promised
- [ ] Terms and policies present, readable, and consistent with behaviour

**Acceptance criteria:** every section checked or N/A with a written reason — no silent skips; failures filed as blocking bugs with owners, not noted and shipped; a second person (not the builder) ran this checklist.

---

## 6. Launch-readiness checklist (in full)

*Source: `research/rules/04-templates/18-launch-readiness.md`. The final go/no-go for a public launch — technical correctness AND real user experience. Both halves must pass; a technically perfect launch of a confusing product is still a failed launch. Blocks technically-ready-but-user-hostile launches, AP-14, AP-18, AP-19.*

### Part A — Technical correctness

**A1. Build & deploy**
- [ ] Release artefact is the tested artefact (R-12); release-readiness passed for the launch build
- [ ] Rollback rehearsed; kill switches verified live
- [ ] Migrations rehearsed forward and back on production-shaped data
- [ ] Feature flags: owners, defaults, and expiry dates set (R-16, R-26)

**A2. Reliability & scale**
- [ ] Load tested to _…×_ expected launch traffic; breaking point known
- [ ] Failure strategies verified — timeouts, breakers, degradation actually exercised
- [ ] Backups running, monitored, and restore-tested (R-24); RPO/RTO written and verified
- [ ] On-call rotation staffed, alert path tested end-to-end (R-29)

**A3. Security & privacy**
- [ ] ASVS L1 gap register complete; zero blocking fails
- [ ] Dependency scan clean per patch SLA (R-23); SBOM generated
- [ ] Secrets audit: none in code, logs, client bundles, or AI transcripts (R-15)
- [ ] Privacy checklist passed (authenticity §9 above); data-handling promises match behaviour

**A4. Observability & cost**
- [ ] Golden-signal dashboards live (R-28); launch-specific alerts with runbooks (R-29)
- [ ] AI/model cost metering per feature in place; cost anomaly alerts set (R-32)
- [ ] Analytics events for the primary outcome metric verified end-to-end (R-02)

### Part B — Real user experience

**B1. First-run experience (tested as a stranger, on a clean account)**
- [ ] Signup/onboarding completable with no outside help; value moment reachable in _…_ minutes
- [ ] A confused user can recover: help, search, support contact all real and monitored
- [ ] First-run UX states verified (loading, empty, error)

**B2. Authenticity & polish**
- [ ] Product authenticity & polish checklist passed (§5 above) — all ten sections

**B3. Content & communication**
- [ ] Launch announcement accurate against the *shipped* product — updated if scope changed
- [ ] Pricing page matches actual billing behaviour; no surprises in the first invoice path
- [ ] Support macros/FAQs ready for the top-5 expected questions; support team briefed
- [ ] Status page live if uptime is promised anywhere

**B4. The "day-two" test**
- [ ] A returning user finds their data intact and the product sensibly changed (no silent resets)
- [ ] Notification/email behaviour sane (no spam, unsubscribe works, no secrets in emails)
- [ ] The kill/fix/keep evaluation is scheduled: metric _…_, date _…_, decider _…_

**Decision:** **LAUNCH** — both halves pass · **HOLD** — blocking items listed, each with an owner, re-check date set. *Partial launches (beta, waitlist, geo-limited) are legitimate — they still run this checklist, with N/A reasons for the deferred half.*

**Acceptance criteria:** no section skipped silently; every N/A has a written reason and a revisit date; Part B was verified by someone who did not build the product, on a clean account, on a real device; the post-launch evaluation is scheduled *before* launch, not after.

---

## 7. Demo-authenticity checklist (condensed)

*Source: `research/rules/04-templates/07-prototype-acceptance.md` (prototype acceptance). Its job is to make what's real explicit, so demos never become commitments by accident. Enforces R-04; blocks AP-14 and AP-06.*

- [ ] **Reality inventory complete** — every capability shown marked *Real* (works on real data, real path) or *Simulated* (Wizard-of-Oz / hardcoded / mocked). Rule: anything not marked is assumed simulated.
- [ ] **Simulated capabilities disclosed** wherever the demo is shown — undisclosed fakery in commitment demos is AP-14.
- [ ] **Feasibility verdict recorded** — what was learned, the biggest surprise, what the real build would do differently.
- [ ] **Throwaway-vs-evolve decided explicitly**, with a deletion date for throwaway code (default: throwaway — Brooks: plan to throw one away; carried parts get full verification before they count as product code).
- [ ] **Decision recorded:** proceed to build / iterate the prototype / kill — with reason and lesson even if killed.

---

## 8. The remaining templates: index with pointers

*Full fill-in-ready text lives in `research/rules/04-templates/<file>`. Each is presented here with its purpose, when to use it, and the rules it enforces — the pointers, not the content.*

| # | Template | What it is (one paragraph) | Use when | Enforces |
|---|---|---|---|---|
| 01 | [problem-validation.md](../research/rules/04-templates/01-problem-validation.md) | The written record of the problem-discovery checklist (§1): problem statement in the customer's words, an evidence log (interviews, observations, behavioral data — each with date and source), the priced pain, the four-risk triage, and the pre-committed kill criterion. Half a day to write, one week to evidence. | Before resourcing any bet | R-01, R-03 |
| 02 | [idea-evaluation.md](../research/rules/04-templates/02-idea-evaluation.md) | Comparing candidate solutions to a *validated* problem (template 01 must exist first): each candidate scored against the outcome metric, the riskiest assumption it carries, the cheapest test for that assumption, and the appetite it would consume. Two-hour timebox; prevents solution-love from skipping validation. | Multiple candidate solutions to one problem | R-02, R-03 |
| 03 | [prd.md](../research/rules/04-templates/03-prd.md) | The bet in writing: press release *first* (if it's boring, the thinking isn't done), then problem, outcome metric with target and window, non-goals, appetite, and the kill/fix/keep evaluation date. For small bets (≤2-week appetite) sections 1–3 alone serve as the PR/FAQ. | Defining a significant bet | R-02, R-04, R-05 |
| 04 | [technical-design-document.md](../research/rules/04-templates/04-technical-design-document.md) | The build's technical shape: context, goals and non-goals, interfaces, data model, the failure strategy per integration point (R-10 — timeout, retry, breaker, degrade), rollout and rollback plan. Sized proportionally: one page for small, several for large. | Any bet with architectural surface — new service, data model, integration, or anything irreversible | R-05, R-06, R-10 |
| 05 | [architecture-decision-record.md](../research/rules/04-templates/05-architecture-decision-record.md) | The one-decision record: context, decision, alternatives considered, consequences, status (proposed/accepted/superseded/deprecated) — 20 minutes of writing, stored as `docs/adr/NNNN-title.md` next to the code, superseded records kept so the reasoning history survives. | Any decision that constrains future work | R-06 |
| 06 | [design-system-definition.md](../research/rules/04-templates/06-design-system-definition.md) | Shared UI foundations defined *only when ≥2 surfaces share components*: scope and non-goals, 3–5 principles each with an opposite, tokens, component inventory. Explicitly not for a first product — borrow a component library instead (R-07). | ≥2 surfaces sharing UI, inconsistency becoming a tax | Consistency w/o bureaucracy |
| 08 | [development-task-definition.md](../research/rules/04-templates/08-development-task-definition.md) | A unit of build work for a human *or* a coding agent, sized so one task = one reviewable change (R-14): what will be true when done, context, scope boundaries, verification steps the author must run, and for agents, the autonomy caps. | Defining build tasks | R-05, R-14, R-13 |
| 09 | [agent-instructions.md](../research/rules/04-templates/09-agent-instructions.md) | Standing repo instructions for coding agents (`AGENTS.md`, skill files, harness configs): scope of authority — what the agent may do unsupervised, what needs human approval, what is forbidden (production access, force-push, deleting data, disabling tests). Derived from Anthropic's "Building Effective Agents": simplest pattern first, guardrails and human checkpoints. | Defining coding-agent behaviour per repo | R-13, R-21, R-14 |
| 10 | [test-plan.md](../research/rules/04-templates/10-test-plan.md) | Verification planned before it runs: scope, the critical paths that gate the release (R-18), production-shaped test cases for the risky paths (R-19), the device/browser matrix, and the flaky-test quarantine policy. A paragraph for small changes, the full template for significant bets. | Planning verification for a bet | R-18, R-19 |
| 11 | [code-review.md](../research/rules/04-templates/11-code-review.md) | Two checklists in one: the author's (diff small and single-purpose; verification steps run; AI-assisted portions read, explainable, and tested — Willison's boundary; no secrets, no repurposed flags; risk tier named) and the reviewer's (risk-tiered scrutiny: high-risk = auth/money/migrations get a qualified human; AI diffs get *more* scrutiny). | Every production change | R-14, R-20, R-13 |
| 12 | [ux-visual-qa.md](../research/rules/04-templates/12-ux-visual-qa.md) | The pre-release UX pass, one per flow: UX states per flow (loading, empty, error, offline, destructive-confirm — mandatory), responsive at three viewports on real devices, interaction checks beyond the happy path. The working-level detail behind the authenticity checklist (§5). | Before any user-facing release | R-03 |
| 13 | [security-verification.md](../research/rules/04-templates/13-security-verification.md) | Security verification structured on OWASP ASVS chapters: scope and target level (L1 pre-launch minimum, L2 for sensitive data), the threat model for trust boundaries (R-09), the ASVS gap register (pass/fail/N-A per requirement, owner, close date), dependency/patch SLA status. The gap register is the release artefact. | Before any internet-facing deploy (R-22); trust-boundary changes (R-09) | R-09, R-21, R-22, R-23 |
| 14 | [release-readiness.md](../research/rules/04-templates/14-release-readiness.md) | The per-release go/no-go: release identity (immutable artefact ID, commit, pipeline run), verification (CI green on the artefact, critical-path tests, scans), rollout plan, rollback procedure, feature-flag map, on-call acknowledgement. Nothing ships with unchecked boxes — each needs a check or a named, dated exception. | Every production release | R-25, R-26, R-27, R-18, R-22 |
| 15 | [incident-response.md](../research/rules/04-templates/15-incident-response.md) | Two parts: Part A runs the incident (declare severity by *user impact*, incident commander, the respond loop), Part B is the blameless postmortem — timeline, impact, contributing factors, action items with owners and dates, shared with the wider team. "Human error" is the start of the investigation, never the conclusion. | Any production incident | R-29, R-30 |
| 16 | [post-launch-evaluation.md](../research/rules/04-templates/16-post-launch-evaluation.md) | Judging the bet against its pre-committed metric: the bet as committed (metric, baseline, target — copied, not rewritten), what actually happened, the verdict (keep/fix/kill per R-34), and the dated decision with a named decider. This is where the outcome metric renders its verdict. | After the pre-committed measurement window | R-02, R-34 |

**How the set is used at different bet sizes** (from `00-index.md`): small bets (≤2-week appetite): 01 → 03 (as PR/FAQ) → 08 → 11 → 14 — that's the whole system. Large bets: run the full sequence; 04 and 10 are mandatory, 13 gates internet-facing launch, 18 gates public launch. **Start at 01.** No bet skips problem validation; everything downstream assumes it's done.

---

**Sources:** `research/rules/04-templates/` (00–18) · `research/discovery/01-problem-discovery.md` · `research/discovery/03-validation.md` · `research/quality/03-quality-gates.md` · `research/discovery/04-evidence-register.md`
