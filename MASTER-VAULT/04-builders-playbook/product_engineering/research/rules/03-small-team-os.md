# §33 — Small-Team Operating System

**Workstream:** rules · **Built:** 2026-10-10 · **Read-only:** research only — a derived system from the evidence, not adoption advice.

A complete but lightweight product-building system for a small team (2–8 people), derived from the evidence in `05-evidence-register.md`. For each component: **build / buy / reuse / automate / omit initially** — with reasoning; then a **minimum-viable** version (what to do on day one) and an **advanced** version (what good looks like at maturity). Hyperscale complexity is deliberately excluded: no service mesh, no platform team, no multi-region active-active, no bespoke ML platforms.

## Design principles (from the evidence)

1. **Outcomes over outputs** — the system exists to move metrics, not to ship artefacts `[E-BUILDTRAP]`.
2. **Fixed appetite, flexible scope** — time is the budget; scope is what you spend `[E-SHAPEUP]`.
3. **Boring by default** — innovation tokens go to differentiation only `[E-BORING][E-GALL]`.
4. **Verification is independent of generation** — whoever (or whatever) made it doesn't get to be the only one who checked it `[E-PERRY][E-PEARCE]`.
5. **Reversibility beats perfection** — every step should be undoable `[E-KNIGHT][E-CROWD]`.
6. **Write it down** — decisions, incidents, and reasoning live with the code `[E-ADR][E-ALLSPAW][E-AMZN]`.

Verdict vocabulary: **REUSE** = adopt an existing practice/tool rather than inventing; **BUY** = pay for a managed service; **BUILD** = make it yourself; **AUTOMATE** = set up automation for it; **OMIT** = deliberately skip for now, with a revisit trigger.

---

### 1. Problem intake

- **Verdict: REUSE (a lightweight intake ritual) + AUTOMATE (capture). OMIT the intake committee.**
- **Reasoning:** Small teams die from too many inputs with no triage, or from a heavyweight process nobody feeds. What works is a single capture point plus a fast, regular triage — the Shape Up "bets, not backlogs" insight: unpitched ideas simply return if they matter `[E-SHAPEUP]`. Buying intake software is overkill before you have intake volume.
- **Minimum-viable:** one shared inbox (a channel, a form, or a doc). Weekly 30-minute triage: each item gets *keep as pitch / needs validation / drop*. Dropped items are deleted, not archived into a backlog swamp.
- **Advanced:** intake tagged by source (customer, support, team, data) and by Cagan's risk type; a quarterly review of dropped items for pattern detection; intake SLAs for customer-reported problems. Still no backlog grooming theatre.

### 2. Research (discovery)

- **Verdict: REUSE (continuous-discovery habits) + BUILD (the habit itself). OMIT dedicated researchers and research repositories initially.**
- **Reasoning:** Torres's evidence says weekly customer contact beats quarterly research projects `[E-TORRES]`; Cagan's four risks say *what* to research `[E-CAGAN]`. A small team can't afford a research function, but it can afford one conversation a week per builder. Tools: the ones you already have (calls, notes, session recordings).
- **Minimum-viable:** each builder talks to ≥1 user/week; notes in a shared doc; one opportunity-solution tree per active initiative (outcome → opportunities → solutions → experiments).
- **Advanced:** research cadence tracked like any metric; a lightweight insight log searchable by theme; prototype testing with 5 users per iteration (Nielsen's long-standing finding, corroborated industry-wide); win/loss notes on every kill decision feeding R-34.

### 3. Prioritisation

- **Verdict: REUSE (appetite-based betting). OMIT scoring frameworks (RICE/WSJF) initially.**
- **Reasoning:** Scoring frameworks give false precision to guesses and cost more to maintain than they return at small scale. Shape Up's appetite + betting table is the right weight: leadership places a few explicit bets per cycle, everything else waits `[E-SHAPEUP]`. The prioritisation artefact is the *bet list*, not a ranked backlog of 200 items.
- **Minimum-viable:** per cycle, leadership picks 1–3 bets with fixed appetites; each bet has a one-paragraph problem statement and a named outcome metric (R-02). Everything not bet on is explicitly not being done.
- **Advanced:** bets mapped to strategy themes (Perri's vision→strategy→opportunity chain `[E-BUILDTRAP]`); appetite calibrated from historical cycle data; explicit "explore" bets (spikes) separated from "exploit" bets (features).

### 4. Requirements

- **Verdict: REUSE (PR/FAQ + PRD template) + BUILD (the writing). OMIT requirements-management tooling.**
- **Reasoning:** Amazon's evidence says the writing *is* the requirements work — a PR/FAQ surfaces weak thinking before design `[E-AMZN]`; Spolsky's spec item says the same from 2000 `[E-JOEL]`. At small scale the document lives in the repo next to the code; no Jira custom workflows needed.
- **Minimum-viable:** for each bet: a one-page PR/FAQ (template 03 doubles as this for small bets) naming the customer, problem, outcome metric, and non-goals. No separate "requirements phase" — shaping and writing are the phase.
- **Advanced:** full PRD (template 03) for large bets; tenets for tradeoff decisions (Amazon practice); requirements versioned with the code; traceability from requirement → task → test for regulated surfaces only.

### 5. Design & prototyping

- **Verdict: REUSE (fat-marker shaping sketches; design-system borrowing) + BUY (prototyping tooling you already pay for). OMIT a bespoke design system initially; OMIT high-fidelity for everything.**
- **Reasoning:** Shape Up's "fat-marker sketch" — enough fidelity to communicate shape, not so much that engineering loses optionality `[E-SHAPEUP]`. For UI, borrow a component library's design system (shadcn-style, Tailwind UI, etc.) rather than inventing one — boring by default (R-07). High-fidelity only where the visual *is* the risk.
- **Minimum-viable:** breadboards/flows for logic, fat-marker sketches for layout; clickable prototype only when usability risk is high (Cagan `[E-CAGAN]`); prototype acceptance criteria written before building the prototype (template 07).
- **Advanced:** a defined design-system (template 06) once ≥2 surfaces share components; prototype testing ritual with 5 users; motion/interaction specs for the differentiating surfaces; design tokens in code.

### 6. Architecture

- **Verdict: REUSE (boring patterns; ADRs) + BUILD (the decisions). OMIT microservices, OMIT platform engineering.**
- **Reasoning:** Gall's law — start from a working simple system `[E-GALL]`; Team Topologies — cognitive load is the constraint, and a 5-person team has exactly one team's worth `[E-CONWAY]`; McKinley — boring technology `[E-BORING]`. The architecture for a small team is a modular monolith on managed services, with ADRs recording the few decisions that matter `[E-ADR]`.
- **Minimum-viable:** modular monolith; managed Postgres; managed hosting/PaaS; one ADR per significant decision (template 05); failure strategy per integration (R-10) even if it's just "timeout + retry + degrade".
- **Advanced:** extract services only when a module has a different scaling, team-ownership, or failure-isolation need (with the ADR explaining why); async boundaries at the proven pain points; documented data model and consistency choices (Kleppmann `[E-KLEPPMANN]`); architecture fitness functions in CI.

### 7. Repository foundations

- **Verdict: BUILD (once, properly) + AUTOMATE (from day one). Never OMIT.**
- **Reasoning:** R-11 and R-12 are critical controls: version control, branch protection, one-step reproducible builds, build/release/run separation `[E-JOEL][E-12F]`. This is the cheapest high-leverage investment in the whole system — a day of setup prevents entire classes of incident (Knight Capital's manual partial deploy `[E-KNIGHT]`).
- **Minimum-viable:** single repo (monorepo-friendly), main-branch protection, CI that builds + tests on every PR, one-command release artefact, environment-based config (R-15), secrets scanning on commit.
- **Advanced:** trunk-based development with short-lived branches; hermetic/reproducible builds; SBOM per release; deployment previews per PR; repo templates so new services inherit the foundations.

### 8. Coding agents

- **Verdict: REUSE (agent harnesses and skills) + AUTOMATE (guardrails) + BUILD (your agent-instruction docs). OMIT autonomous production agents.**
- **Reasoning:** Anthropic's taxonomy says: workflows (deterministic paths) where the path is known, agents (dynamic) only where it isn't; simplest pattern first; agents need sandbox testing, guardrails, human checkpoints `[E-ANTHROPIC]`. And R-13 says AI output is untrusted until verified `[E-PERRY][E-PEARCE]`. So: agents as supervised contributors inside the same review/test gates as humans — never as unsupervised authors of production change.
- **Minimum-viable:** written agent instructions per repo (template 09: scope caps, verification steps, what the agent must never do); agents work in branches, humans review every diff; SAST/SCA/secrets scans run on agent-produced PRs identically; no agent with production write access.
- **Advanced:** standardised skill/agent-instruction library across repos; sandboxed agent execution; agent action logs; eval harnesses for agent-assisted workflows (did the change pass tests? did review find issues?); staged autonomy — read-only investigation agents first, write access only with human approval gates.

### 9. Testing

- **Verdict: BUILD (the tests) + AUTOMATE (execution and gating) + REUSE (frameworks). OMIT 100%-coverage dogma and dedicated QA headcount initially.**
- **Reasoning:** R-18/R-19: critical paths tested, releases gated, production-shaped inputs `[E-CROWD]`. Coverage percentage is a vanity metric; the gate is "critical paths proven". A small team can't afford a QA department, but it can afford the discipline that Joel Test item #10 modernised into automated testing `[E-JOEL]`.
- **Minimum-viable:** automated tests for critical paths (template 10); CI runs the suite on every PR and blocks merge on red; flaky tests quarantined with an owner, not tolerated; production-shaped fixtures for the risky paths.
- **Advanced:** test pyramid kept honest (fast unit, meaningful integration, few E2E on critical flows); contract tests at service seams; load tests for the scaling risks; chaos/fault-injection for the failure strategies (Nygard's test harness `[E-RELEASEIT]`); mutation testing on the most critical logic.

### 10. Code review

- **Verdict: REUSE (review ritual + checklist) + AUTOMATE (assignment, pre-checks). OMIT review-as-bureaucracy.**
- **Reasoning:** R-20: every production change gets a second pair of eyes; AI-assisted diffs get *more* scrutiny because the author's confidence is inflated `[E-PERRY]`. Small PRs (R-14) make review fast; the checklist (template 11) makes it consistent.
- **Minimum-viable:** branch protection requiring one human review; PR template with risk tier; small diffs by default; author must be able to explain AI-assisted code (Willison's boundary `[E-KARPATHY]`).
- **Advanced:** risk-tiered reviewers (security-sensitive → qualified human); AI pre-review as triage, never as the only reviewer; review SLAs; periodic review-quality retros (are we catching real issues?); stacked diffs for large changes.

### 11. UX & visual QA

- **Verdict: BUILD (the checklist habit) + AUTOMATE (regression screenshots). OMIT a QA department; OMIT pixel-perfection everywhere.**
- **Reasoning:** Missing UX states and broken responsive behaviour are usability-risk failures (Cagan `[E-CAGAN]`), and they're cheap to catch with a checklist (Gawande's mechanism `[E-GAWANDE]`). Visual regression tooling is cheap; human visual QA focuses on the differentiating surfaces.
- **Minimum-viable:** UX-states checklist per flow (template 12/17: loading, empty, error, offline, destructive-confirm); responsive check at 3 viewports on real devices; hallway usability testing (Joel Test #12, modernised `[E-JOEL]`).
- **Advanced:** automated visual regression on key screens; accessibility checks in CI (axe-style) plus periodic manual audit; design-system conformance checks; session-replay sampling for real-world UX validation.

### 12. Security checks

- **Verdict: AUTOMATE (scanners in the pipeline) + REUSE (ASVS as the requirement list) + BUILD (threat models for trust boundaries). OMIT a security team; OMIT the annual-pentest-as-only-plan.**
- **Reasoning:** ASVS L1 is *designed* to be automatable — SAST, SCA, secrets, DAST — so a small team gets the baseline without headcount `[E-ASVS]`; threat modeling at design time is cheap and catches what scanners can't `[E-SHOSTACK]`; AI-generated security code needs independent review `[E-PERRY]`. The pentest comes later as validation, not as the plan.
- **Minimum-viable:** secrets scanning (block on detection), SAST + SCA in CI, ASVS L1 gap register before internet-facing launch (template 13), 10-minute threat model for trust boundaries, patch SLA by severity (R-23).
- **Advanced:** ASVS L2 as the target for sensitive-data surfaces; scheduled DAST; annual pentest; bug-bounty or coordinated-disclosure page (security.txt); dependency reachability analysis to prioritise patching; agent tool-permission audits.

### 13. CI/CD

- **Verdict: BUY or REUSE (managed CI) + AUTOMATE (everything). Never OMIT; never BUILD your own CI server.**
- **Reasoning:** CI is the enforcement arm of R-11 through R-20: build, test, scan, review-gate, artefact. Managed CI (the boring choice, R-07) costs little and removes an entire maintenance surface. DORA elite performance is structurally downstream of CI/CD maturity `[E-DORA]`.
- **Minimum-viable:** managed CI; pipeline = build → test → scan → artefact; required checks before merge; artefact promotion (the tested artefact is the shipped artefact, R-12).
- **Advanced:** DORA metrics piped from the pipeline; deployment previews; progressive-delivery automation (canary analysis, auto-rollback); pipeline-as-code reviewed like code; hermetic builds with SBOM attestation.

### 14. Deployment

- **Verdict: BUY (managed platform/PaaS) + AUTOMATE (progressive rollout, rollback). OMIT self-managed orchestration initially.**
- **Reasoning:** R-25: reversible, progressive releases `[E-KNIGHT][E-CROWD]`; Twelve-Factor disposability and dev/prod parity `[E-12F]`. A PaaS gives you rolling deploys, instant rollback, and environment parity for near-zero ops cost — the boring choice that prevents the exotic-choice incidents.
- **Minimum-viable:** PaaS/managed hosting; one-command deploy from a tagged artefact; instant rollback (rehearsed); database migrations with expand/contract discipline; deploy on demand, no freeze windows (R-27).
- **Advanced:** progressive delivery (canary with automatic promotion/rollback on golden-signal regression); feature flags for risky behaviour changes (R-26) with owner + expiry hygiene (R-16); blue-green for the riskiest cuts; multi-region only when latency/regulation demands it — with the ADR.

### 15. Monitoring (observability + alerting)

- **Verdict: BUY (managed observability) + AUTOMATE (dashboards, alerts, alert-path tests). OMIT building your own stack; OMIT alerting on everything.**
- **Reasoning:** R-28/R-29: four golden signals from day one; alert on symptoms, page only on actionable `[E-SRE]`; GitLab's dead-mailbox lesson — test the alert path `[E-GITLAB]`. Managed observability is boring-tech-compliant (R-07) and a small team cannot maintain a metrics stack *and* a product.
- **Minimum-viable:** golden-signal dashboards per service (template 14 requires them before launch); a handful of symptom-based alerts with runbook links; alert-path test proving a human gets paged; structured logs.
- **Advanced:** SLOs with error budgets governing release risk (R-31); burn-rate alerting; distributed tracing at the seams that hurt; business-metric dashboards next to technical ones; incident metrics (MTTR, time-to-detect) reviewed in postmortems.

### 16. Customer feedback

- **Verdict: REUSE (direct channels) + AUTOMATE (collection). OMIT feedback-management platforms initially.**
- **Reasoning:** Torres: weekly contact beats quarterly studies `[E-TORRES]`; the fastest feedback loop is the founder/support inbox, not a platform. Automation here means *collection* (in-app prompts, support tagging), not analysis — analysis stays human at small scale.
- **Minimum-viable:** one monitored support channel with a response SLA; in-app feedback affordance; support issues tagged and triaged in the weekly intake (component 1); every incident's customer impact recorded in the postmortem.
- **Advanced:** feedback tagged to opportunities in the opportunity-solution tree; NPS/CSAT-style pulse with *comment* analysis, not just scores; churn/retention interviews; public changelog closing the loop ("you asked, we shipped").

### 17. Continuous improvement

- **Verdict: BUILD (the rituals) + REUSE (DORA + postmortem formats). OMIT transformation programmes.**
- **Reasoning:** Improvement at small scale is three rituals: blameless postmortems (learn from incidents `[E-ALLSPAW][E-SRE]`), DORA trend review (find the bottleneck `[E-DORA]`), and kill/fix/keep (prune the product `[E-BUILDTRAP][E-SHAPEUP]`). No consultants, no maturity models — just the cadence.
- **Minimum-viable:** postmortem for every significant incident with action items tracked to done (template 15); monthly 30-minute review: DORA trends + one bottleneck to fix + kill/fix/keep for one feature.
- **Advanced:** error-budget policy mediating feature vs reliability work (R-31); quarterly architecture fitness review (are the ADRs still true?); team health/retrospective feeding the same improvement backlog; the improvement backlog prioritised with the same appetite discipline as product work.

---

## The system at a glance

| # | Component | Verdict | MVP in one line | Revisit trigger for Advanced |
|---|---|---|---|---|
| 1 | Problem intake | Reuse + Automate | One inbox, weekly triage, no backlog swamp | Intake volume > triage capacity |
| 2 | Research | Reuse + Build | 1 user conversation/week/builder | Dedicated researcher affordable |
| 3 | Prioritisation | Reuse | 1–3 appetite-fixed bets per cycle | Strategy needs theme-level mapping |
| 4 | Requirements | Reuse + Build | One-page PR/FAQ per bet | Large bets needing full PRDs |
| 5 | Design & prototyping | Reuse + Buy | Fat-marker sketches; borrowed components | Shared surfaces needing a design system |
| 6 | Architecture | Reuse + Build | Modular monolith + ADRs | Proven scaling/ownership pain |
| 7 | Repo foundations | Build + Automate | Protected main, CI, one-command release | Multi-service repo templates |
| 8 | Coding agents | Reuse + Automate + Build | Supervised agents, human-reviewed diffs | Eval harnesses for agent workflows |
| 9 | Testing | Build + Automate + Reuse | Critical paths tested, CI gates | Contract/chaos/load testing |
| 10 | Code review | Reuse + Automate | One human review, risk-tiered | Review SLAs, AI pre-review triage |
| 11 | UX & visual QA | Build + Automate | UX-states checklist, 3 viewports | Visual regression, a11y in CI |
| 12 | Security checks | Automate + Reuse + Build | Scanners in CI, ASVS L1 gate | ASVS L2, pentest, disclosure page |
| 13 | CI/CD | Buy/Reuse + Automate | Managed CI, test→scan→artefact | Progressive delivery, DORA piping |
| 14 | Deployment | Buy + Automate | PaaS, one-command deploy, rehearsed rollback | Canary automation, flags |
| 15 | Monitoring | Buy + Automate | Golden signals, symptom alerts, tested paging | SLOs, error budgets, tracing |
| 16 | Customer feedback | Reuse + Automate | One support channel + SLA, weekly triage | Feedback→opportunity mapping |
| 17 | Continuous improvement | Build + Reuse | Postmortems, monthly metrics review | Error-budget policy, arch reviews |

**What was deliberately omitted throughout:** service mesh, platform team, multi-region active-active, bespoke ML infra, scoring-framework bureaucracy, requirements-management suites, self-hosted CI, security team before product-market fit, and any process whose maintenance cost exceeds its learning value at 2–8 people. Each omission carries a revisit trigger — simplicity is a stage, not a religion.
