# §12 — Testing, Release Readiness & Deployment

**Workstream:** build-ship · **Researched:** 2026-10-10 · **Scope:** test types and test quality, coverage limitations, flaky tests, defect classification, code review as pre-merge evidence, release gates, CI/CD, staged rollouts, migrations, rollback, post-deployment verification; what evidence is required BEFORE merge and BEFORE exposing a release to users. Read-only research only.

**Labels:** **Verified** = primary source · **Corroborated** = multiple independent sources · **Inferred** = reasoned from evidence · **Proposed** = single-sourced practitioner prescription · **Unknown** = not established. Evidence classes noted per finding.

---

## 1. The test-type catalog (what each type is for)

**Plain English:** different tests answer different questions. Unit tests ask "does this function do the right thing?"; integration tests ask "do these parts work together?"; end-to-end tests ask "can a real user complete a real task?"

| Type | Question it answers | Strength | Characteristic weakness |
|---|---|---|---|
| Unit | Does this unit behave correctly in isolation? | Fast, precise fault localization ("the bug is on line 47") | Mocks can drift from reality; structurally coupled to code, brittle under refactoring |
| Integration | Do components work together (service↔DB, service↔broker)? | Catches the seam bugs where most production failures live | Needs real-ish dependencies; slower |
| Contract (consumer-driven) | Does the provider still honor what consumers expect? | Fast, no shared staging env, blocks breaking changes pre-merge | Can't catch runtime/network/data problems |
| E2E | Can a user complete a critical journey? | Only test of the whole assembled system | Slow, expensive, flaky; every feature E2E'd = inverted pyramid |
| Regression | Did we break something that used to work? | Guards the existing contract with users | Can calcify into change-detector tests that block refactoring |
| Visual | Does it still *look* right? | Catches unintended UI changes | Pixel-diff flakiness (anti-aliasing, fonts); dynamic content must be stabilized |
| Accessibility (a11y) | Can people with disabilities use it? | Automated scans (axe-core) have near-zero false positives | Automation catches only ~20–50% of WCAG issues; keyboard flow, focus order, meaningful alt text need humans |
| Performance / load | Does it meet latency/throughput budgets under realistic load? | Finds capacity cliffs before users do | Requires production-like data and traffic shapes to mean anything |
| Security | Are known vulnerability classes exercised? | Shift-left catches issues at PR time | Can't prove absence; needs threat-model grounding |
| Exploratory | What happens when a skilled human pokes at it? | Finds the bugs nobody thought to automate for | Not repeatable; depends on tester skill |

**Google's size-based framing (Verified** from *Software Engineering at Google* Ch. 11): small tests run in a single process/thread, no sleep, no I/O, no blocking calls — the constraints exist to make nondeterminism and slowness structurally hard. Medium tests may span processes; large tests span systems. "We encourage engineers to try to write small tests whenever possible, regardless of the scope of the test."

---

## 2. Test quality: why coverage is a flag, not a goal

**Plain English:** coverage measures which lines *ran* during tests, not whether the tests would *notice* if those lines were wrong. A test that executes code but asserts nothing meaningful still counts toward coverage.

**Concrete example (Corroborated):** a pagination function tested only with "returns something," "returns array," "length > 0," "no error" — 100% line coverage, but mutation testing (below) scores it 63%: changing `i <= offset + limit` to `i < offset + limit` (a real page-size bug) doesn't fail any test.

**Mutation testing — the adequacy check:** deliberately introduce small plausible bugs ("mutants": `>` → `>=`, `+` → `-`, `return x` → `return 0`, `true` → `false`) and measure the percentage the suite kills (fails on). Score = mutants killed ÷ total. A surviving mutant in domain logic is a missing test the team can act on directly (**Corroborated** across practitioner docs; worked example: a real public module with 6 hand-written tests, "looking well-tested," had 9 of 112 mutants survive — coverage had hidden it completely).

**What coverage can't see (Corroborated):** duplicate tests validating the same scenario, tests with external dependencies that flake, unused mocks giving false isolation, assertions on implementation details, and — newly important — AI-generated tests: assistants can generate many syntactically different tests exercising *identical* behavior, inflating test counts and nudging coverage up without adding validation scenarios. One 2026 replicability study (arXiv 2607.22880) found that for LLM-generated suites, coverage correlates only weakly with bug detection *within* one model, while raw mutation score correlates strongly (r = 0.863) with real-bug detection *across* models; on buggy code, coverage correlations collapse entirely — "an agent that writes the test second writes the test its code passes" (**Corroborated** via the study's reporting in practitioner notes; underlying paper is primary but accessed second-hand — mark **Corroborated**).

**Practitioner guidance (Corroborated):** 80% line coverage is a reasonable target; 100% is vanity producing low-value tests (Goodhart's law: a coverage target degrades into assertion-free tests). Run mutation analysis on changed code in PRs and full analysis nightly; set thresholds with headroom (one project CI-fails below 88% with observed scores 90.5–94.0, deliberately not gated at the best observed score — "a gate set to the best observed score would fail on an unlucky afternoon and teach everyone to ignore it").

**Prevent:** false confidence from green coverage numbers; assertion-free generated tests; lowering a coverage ratchet to unblock a merge without a documented reason ("exactly the silent regression the ratchet exists to prevent").

---

## 3. The testing pyramid and its critics

**Origin (Verified):** Mike Cohn's *Succeeding with Agile* popularized the pyramid: many fast unit tests at the base, fewer integration tests, few E2E tests at the top — a model about *cost and feedback speed*, not a law of nature.

**The criticisms (Corroborated** across a 2025–2026 wave of practitioner essays):
1. The 70/20/10-style ratio is made up; the right mix emerges from the system's actual risk profile — a data pipeline, a REST API, and a React frontend need different shapes.
2. Over-mocked unit tests are "actively misleading — they test your mock, not your system." The pyramid as usually drawn says nothing about mocks drifting.
3. Production's failure modes are emergent and live in interactions: partial failures (one dependency *slow*, not down), message-ordering violations under concurrent consumers, cache-invalidation races, retry storms. None are unit-testable; most aren't caught by conventional sequential integration tests either.
4. The classic pyramid omits contract tests and component tests, which carry the weight in microservice architectures ("thick middle" beats "tall pyramid" for API-first systems).
5. For UI-heavy apps, a smaller number of integration/E2E tests over real user journeys beats a mountain of component unit tests for actual risk reduction.

**What's kept (Inferred consensus):** invest in fast feedback; don't lean on slow tests for everything; fix test *infrastructure* (fast, reliable, isolated environments change the cost structure — if integration tests take 45s each you'll avoid writing them; at 2s you won't); a few deliberate E2E tests on the 3–4 critical user paths that would be immediately catastrophic if broken.

---

## 4. Flaky tests

**Definition (Verified):** a test that can pass and fail without a relevant code change. **Measurement is not standardized** — Google's 1.5% figure counts *test runs*; its ~16% figure counts *tests in inventory* showing some flakiness; GitHub counts commits with an affected build; Bitrise counts teams with any flakiness. These can all be true simultaneously and do not average into an "industry flake rate" (**Corroborated** via a 2026 denominator-first analysis). Before reusing any flake statistic: check the unit, the population, and the observation period.

**Root causes (Corroborated):** the canonical taxonomy (Luo et al., FSE 2014 — old, undisplaced) classified 201 flaky-fix commits across 51 Apache projects: async wait 45%, concurrency 20%, test-order dependency 12% — 77% of fixes in the top three, *all defects in test code*, none fixable by migrating frameworks. A 2025 analysis found 75% of flaky tests cluster with others sharing a root cause (mean cluster size 13.5) — fixing one data-provisioning bug often clears dozens of failures at once.

**Structural prevention (Verified** from Google's practices): hermetic, ephemeral test environments — spawn the system under test *and all its dependencies* in a container, removing network calls to shared staging/prod stacks. Gains: no flaky-dependency failures, reproducibility (the dependency can't release a new version between your run and your repro), and debuggability (you can read the dependency's logs and inspect its database).

**Triage probes (Proposed** practitioner heuristic): (1) does it pass alone? (2) does it survive repetition + concurrency? (3) does it survive a clean database? Passes-alone-but-fails-in-suite = order dependency or shared state; fails-identically-everywhere = real defect or stale locator; fails-only-under-concurrency = data collision. Only after all three are clean is the tooling suspect.

**Scale of the problem:** Google runs ~150M tests/day; even 1.5% flaky runs is an enormous absolute number, which is why Google built automated flake detection (DeFlaker: 95.5% recall, 1.5% false alarms on 1,874 flakes — Bell et al. 2018) and, by 2026, LLM-based failure diagnosis (Auto-Diagnose: 90.14% correct root-cause identification on 71 real failures across 39 teams; 52,635 failing tests processed — **Corroborated** via MarkTechPost reporting of the arXiv paper).

---

## 5. Contract testing (Pact-style, consumer-driven)

**Plain English:** the consumer writes down exactly what it expects from the provider ("when I call /customers/1 I expect this shape"); the provider verifies it honors those expectations in CI; a `can-i-deploy` gate blocks releases with unverified contracts.

**What it's good for (Corroborated):** catching obvious API breakages (field renames, type changes); documenting what consumers actually use (useful for deprecation); enabling independent deployability without a shared staging environment; fast deterministic feedback.

**What it is NOT enough for — the negative evidence (Corroborated** from a first-hand "looked good, broke anyway" practitioner account): version mismatches between test and production; messy real-world data; network failures and timeouts; schema-evolution coordination; resilience and error handling. Pact verifies the *agreement*, not the *behavior under adversity*. The practitioner's evolved stack: contract tests + integration tests + production-traffic shadowing + chaos testing for resilience + contract-compliance monitoring in production ("contract tests told us what should work; monitoring tells us what actually works").

**Design notes (Corroborated):** use flexible type matchers, not hardcoded values; consumer defines, provider verifies, production validates; clean stale contracts from the broker; consumer-driven fits when the provider exists to serve the consumer; producer-driven fits public/multi-consumer APIs.

---

## 6. Visual, accessibility, performance, security, exploratory testing

- **Visual regression (Corroborated** practitioner pitfalls): snapshot before page stabilizes (wait for network idle, fonts, animation completion); handle dynamic content (dates, avatars, random IDs) via clip regions or DOM transforms; set minimum diff thresholds to absorb anti-aliasing noise; approve baseline changes post-merge on main only, never on feature branches; never use visual tests as the *only* layer (they verify pixels, not behavior/a11y/performance).
- **Accessibility (Corroborated):** axe-core (Deque) has near-zero false positives and is the standard engine wired into Playwright/Cypress suites. Automated scans catch roughly 20–50% of WCAG issues (missing alt text, contrast, missing labels, invalid ARIA); they cannot judge whether alt text is *meaningful* (`alt="image"` passes and is useless), whether focus order makes sense, keyboard traps, or whether captions match audio. Guidance: scan settled pages, scan each distinct *state* (modal open, form error state — not just URLs), scope to new/reworked screens first on existing apps (a blanket scan everyone learns to skip is worse than no scan), and keep a recurring manual keyboard + screen-reader pass. Context: 95.9% of the top-1M home pages have at least one detected WCAG 2 failure, averaging 56.1 errors/page (WebAIM-derived via contextqa — **Corroborated**).
- **Performance/load:** budgets and production-like traffic shapes; without them the numbers don't transfer.
- **Security testing:** "shift left" — security reviews, pre-approved libraries, security features in the automated suite (DORA capability). Dependency scanning belongs here (see §11).
- **Exploratory:** finds what nobody automated for; complements but doesn't replace the suite.

---

## 7. Defect classification (making bugs teach)

**Orthogonal Defect Classification — ODC (Verified** from Chillarege et al., IEEE TSE 1992, and the current IBM spec): each defect is classified on mutually exclusive attributes — opener attributes (Activity: where found; Trigger: what surfaced it; Impact: how the customer experiences it) and closer attributes (Target: what was modified; Defect Type: Function/Assignment/Checking/Algorithm/Interface/Timing/Build; Qualifier: Missing/Incorrect/Extraneous; Source; Age). The *distribution* is the signal: e.g., a cluster of "Function/Missing found in Requirements activity" says the requirements review process is broken. It turns defects into in-process measurements of where the process leaks.

**IEEE 1044-2009 (Corroborated** via practitioner research): standardizes a 17-attribute defect schema and 17-attribute failure schema with only *informative, optional* example values — schema-standardization, not category-standardization — a genuinely different design philosophy from ODC.

**Operational use (Inferred/Proposed):** defect leakage by phase (requirements-type defects found in system test = weak upstream review); injection-vs-detection cross-tabs (many boundary triggers caught in function test = weak unit boundary coverage); root-cause distributions trending per release.

---

## 8. Release readiness: evidence BEFORE merge vs BEFORE users

**Before merge (the change gate):** automated checks green (lint, format, typecheck, unit/integration/contract tests, dependency/security scan) *before* human review; small, single-concern change with tests in the same PR; human review covering design → functionality → complexity → tests → naming/style (Google order); review within one business day; no rubber-stamps; breaking changes to shared components called out with a migration path; coverage ratchet honored, not silently lowered.

**Before exposing a release to users (the release gate):** the change is deployed but hidden — feature flags at safe defaults, progressive rollout (internal → 1% → 10/25/50 → 100%) with error/latency/business-metric monitoring at each step; canary or blue-green with automated analysis and rollback triggers; migrations run under expand–migrate–contract with dual-write and shadow-read parity proof; contract `can-i-deploy` gates; post-deployment verification (smoke tests, synthetic probes matching recent failure modes — see OWASP AISVS guidance on probing canaries with malformed inputs rather than promoting on a vacuous green signal).

**Staged rollouts — why they exist (the incident record):**
- **CrowdStrike, July 2024 (Verified):** faulty content update shipped to ~8.5M Windows machines simultaneously → global crashes; the fix commitment was staged, canary-style rollouts for such updates.
- **GPT-4o sycophancy, April 2025 (Corroborated** via OWASP AISVS synthesis): a system-prompt change deployed to 100% of traffic with no staged rollout → harmful behavior for three days before rollback; social media became the alerting system. Lesson: prompt/config changes deserve the same rollout discipline as code, and canary analysis must include *behavioral* metrics (guardrail alert rates), not just latency/errors — functional metrics passed while safety regressed.
- **Argo Rollouts failure modes (community observations, first-hand):** a canary promotion left sticky-session cookies pointing at deleted canary pods — half the users disappeared for an hour; mitigation was cookie hygiene (10-minute TTL during canaries, explicit rewrite on promote/abort), not another deploy. Separately: ArgoCD "Synced/Healthy" with zero errors while the deploy silently hadn't taken effect for 3 days — the tool verifies *manifest state*, not *runtime behavior*; post-deploy verification must check behavior, not dashboard color.

**Rollback:** Google SRE's maxim — "rollback early, rollback often"; every runbook ships with exact undo commands and the conditions that trigger them. Rollback must be rehearsed, not just documented (game days). Note the asymmetry: rolling back *code* is easy; rolling back *data migrations* is hard — which is why expand–migrate–contract keeps every phase independently reversible (**Corroborated**).

**Prevent:** the "silent success" failure — all systems green while users are broken (see the incident table in §13). Post-deploy verification closes this gap.

---

## Key sources consulted (full register in 05-evidence-register.md)

*Software Engineering at Google* Ch. 11 (testing overview), Ch. 9 (code review); DORA research; Mike Cohn (*Succeeding with Agile*); Luo et al. FSE 2014 (flaky taxonomy); Bell et al. 2018 (DeFlaker); Google Auto-Diagnose (arXiv 2604.12108); Chillarege et al. 1992 (ODC) + IBM ODC v5.2 spec; IEEE 1044-2009; mutation-testing practitioners (Stryker, oracle-gate, arXiv 2607.22880); Pact contract-testing practitioners (incl. negative case study); axe-core/Deque docs; WebAIM-derived a11y stats; visual-regression pitfalls (graycode skills); Google SRE Book/Workbook (rollback, monitoring); OWASP AISVS rollback chapter (GPT-4o sycophancy, vLLM CVEs); CrowdStrike July 2024; Argo Rollouts failure stories.

## Honest gaps

- No controlled experiment found isolating the *causal* effect of any single test-type mix on escaped defects; the pyramid critiques are principled practitioner arguments, not trials.
- Flaky-rate figures are definition-dependent; treat every quoted percentage with its denominator.
- The arXiv mutation/LLM-test study (2607.22880) was accessed via practitioner notes, not the paper itself.
- Visual-testing flake rates and a11y automation coverage percentages vary by source (20–50%); the range is reported, not a point estimate.
