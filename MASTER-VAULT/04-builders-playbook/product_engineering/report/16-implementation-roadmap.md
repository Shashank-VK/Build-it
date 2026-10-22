# 16 — Implementation Roadmap

**Status:** report section; read-only synthesis, not adoption advice. **This entire roadmap is Proposed** — a synthesis derived from the lifecycle research, the small-team OS, and the quality-gate system, not a report of any team's practice. Every phase is labelled Proposed accordingly; the *supporting* findings keep their original labels. Grounding: `research/rules/03-small-team-os.md` (the small-team OS), `research/quality/03-quality-gates.md` (the 9 quality gates and gate mechanics), `research/economics/02-bottleneck-analysis.md` (why verification capacity must lead generation capacity), `research/rules/01-engineering-rules.md` + `02-anti-patterns.md` (the rules and failure modes each phase installs protection against), `research/discovery/*` (the discovery gates that precede build), and `research/rules/04-templates/*` (the artefacts each phase produces).

**The governing idea (Proposed):** sequence the system so that *verification capacity is installed before generation capacity is scaled*. The economics research (§13) shows the industry did this backwards — generation got cheap first, and review, testing, and operations absorbed the load. This roadmap's phase transitions are therefore governed by *quality-gate verdicts* (GO / NO-GO / NOT ASSESSED, per §17), not by calendar dates.

---

## How phase transitions work (Proposed)

- **Entry criteria:** what must be true to *begin* a phase. If not true, you are still in the previous phase.
- **Exit gates:** the quality-gate verdicts that must be GO (or formally excepted by a named owner) to *leave* a phase. NO-GO on any critical condition stops the transition; NOT ASSESSED is not a pass.
- **Quality-gate verdicts that govern transitions** are named per phase — these are the decision points, not the tracks themselves (the work runs in parallel; the gates are where you decide).
- **Deliberately deferred:** what you explicitly do *not* do in this phase, with the trigger for revisiting. "Not yet" is a decision, not a neglect — record it.

---

## Phase 0 — Foundations (Proposed)

**Goal:** make it possible to ship one small change to real users safely, and to know when it breaks. Nothing in this phase builds product yet — it builds the floor everything else stands on (R-11, R-12, R-15 are critical controls: no exceptions).

**Entry criteria:**
- A named product bet with an outcome metric (rules R-01/R-02; discovery Gates 1–2 need not be fully passed, but the *bet and metric must exist* — you cannot instrument what you haven't named).
- The team exists and has deploy authority to production.

**What gets built:**
1. **Repository foundations** (small-team OS #7): single repo, protected `main`, CI that builds + tests on every PR, one-command release artefact, environment-based config, secrets scanning on commit. [Rules R-11, R-12, R-15 — Verified]
2. **Managed runtime** (small-team OS #14): PaaS or managed hosting; deploy from a tagged artefact; instant rollback *rehearsed*, not just documented. [R-25 — Verified]
3. **Golden signals from day one** (small-team OS #15): latency, traffic, errors, saturation per service, dashboards a stranger could read; structured logs; one symptom-based alert with a tested alert path (prove a human gets paged — the GitLab dead-mailbox lesson [Verified]). [R-28, R-29 — Verified]
4. **Modular monolith skeleton** (§15): bounded contexts with *mechanically enforced* boundaries (import-linter contracts, no cross-module FKs in CI); managed Postgres; ADRs for the handful of load-bearing choices (framework, database, hosting). [Gall's law; spec-arch — Corroborated]
5. **The intake ritual** (small-team OS #1): one shared inbox, weekly 30-minute triage; dropped items deleted, not archived into a backlog swamp.

**Quality-gate verdicts that govern the Phase 0 → 1 transition:**
- **Quality Gate 8 (Deployment)** — GO on a *throwaway* deploy: immutable artefact promoted through stages, tested rollback, smoke tests. The rollback must have been rehearsed on the real path.
- **Quality Gate 9 (Post-launch)** — GO in lightweight form: alerts exist that would catch a bad deploy, on-call is staffed, the alert path is tested end-to-end.

**Deliberately deferred (with revisit triggers):**
- Microservices or service extraction — trigger: proven deploy contention or divergent scaling profile (spec-arch, Corroborated).
- SLOs and error budgets — trigger: enough production history to set honest SLOs (SRE, Verified).
- Feature flags — trigger: the first behaviour change with uncertain outcome (R-26).
- Analytics instrumentation beyond the outcome metric — trigger: the first decision that needs funnel/cohort evidence (gaps T8).
- Agents with write access — trigger: agent workflows that pass their eval harnesses (automation 01, rules R-13).

**Why this order:** Knight Capital's manual partial deploy [Verified] and CrowdStrike's untested content path [Verified] are both Phase-0 failures — the floor missing, not the product. The cheapest day of setup in the whole system prevents entire incident classes.

---

## Phase 1 — First loop (Proposed)

**Goal:** take one small bet all the way from validated problem to real users and measured outcome — proving the *whole* loop works end to end before any scale. The bet is small on purpose: the system is being debugged, not the product.

**Entry criteria:**
- Phase 0 exit gates GO.
- The bet has passed the problem-discovery checklist and decision-criteria gate (§17): named segment, priced pain, kill criterion pre-committed. Discovery Gates 1–2 GO (or conditional-pass with named open items and owners).

**What gets built:**
1. **The discovery → build → measure loop, run once:** PR/FAQ or one-page PRD (R-04/R-02) → fat-marker shaping sketches with borrowed components (R-05, R-07) → agent instructions per repo (R-13, R-21: scope caps, verification steps, never-do list) → small, coherent, reviewable changes (R-14) → critical-path tests with CI gating (R-18) → every change gets a human second pair of eyes (R-20) → deploy behind progressive rollout with a rehearsed rollback (R-25).
2. **Coding agents as supervised contributors** (small-team OS #8): agents work in branches; humans review every diff; SAST/SCA/secrets scans run on agent-produced PRs identically; no agent with production write access. [Anthropic, Verified; R-13 — Verified]
3. **UX-states checklist per flow** (small-team OS #11): loading, empty, error, offline, destructive-confirm — designed, not discovered. Responsive check at 3 viewports on a real device.
4. **ASVS Level 1 gap register** before the first internet-facing traffic (R-22): pass/fail/N-A per requirement, owner, close date. The register is the release artefact. [OWASP ASVS — Verified]
5. **Threat model** for the first trust boundary crossed (auth, payments, PII, agent tool access) (R-09) — the 10-minute version if the boundary is simple. [Shostack — Corroborated]
6. **Post-launch evaluation scheduled *before* launch:** the pre-committed metric, the date, the decider, and the kill/fix/keep decision it feeds (R-02, R-34). [Ries; Perri — Verified/Corroborated]
7. **The blameless postmortem ritual** (R-30): written after the first incident (there will be one), with action items tracked to closure like any work. [Allspaw; SRE — Verified]

**Quality-gate verdicts that govern the Phase 1 → 2 transition** (the full Gate 1–9 sequence, run in lightweight form on the first bet):
- **Gate 4 (Prototype):** GO — the riskiest assumption was actually tested, with a learnings memo and a go/pivot/kill decision.
- **Gate 5 (Implementation):** GO — CI green on the exact artefact; scans clean or triaged; human code review (an agent's approval is not evidence).
- **Gate 7 (Security review):** GO — ASVS L1 register complete; no unresolved high/critical findings on the release path.
- **Gate 8 (Deployment):** GO — staged rollout; tested rollback; artifact promoted, not rebuilt.
- **Gate 9 (Post-launch):** GO — watch report recorded; the pre-committed outcome metric is being measured; post-launch evaluation date set.

**Deliberately deferred:**
- Full PRDs, tech design docs, test plans for every change — trigger: bet size and risk justify the writing (templates scale with appetite).
- Async/event-driven architecture — trigger: measured burst or fan-out pain (spec-arch, Corroborated).
- AI cost metering per feature — trigger: the first AI feature in the request path (R-32).
- Load testing — trigger: launch traffic expectations that could plausibly break the system (template 18).

**Why this order:** the first loop is where the *system's* bugs surface — the gate that nobody knows how to run, the alert path that doesn't page, the rollback that's theoretical. §13's economics says the industry scaled generation before installing verification; Phase 1 is the deliberate reversal: prove verification works on one bet before scaling either.

---

## Phase 2 — Hardening (Proposed)

**Goal:** turn the proven loop into the *default* way of working — industrialise verification, so that when generation volume rises, the system absorbs it instead of destabilising. This is the phase the bottleneck analysis (§13) says most teams skip.

**Entry criteria:**
- Phase 1 exit gates GO on the first bet.
- The team has survived one full loop including one incident with a written postmortem (the improvement ritual is proven, not just documented).

**What gets built:**
1. **Verification industrialisation** — the direct response to §13's binding-constraint finding (Corroborated):
   - Risk-tiered review: security-sensitive changes (auth, money, migrations) require a qualified human reviewer; AI-assisted diffs get *more* scrutiny (R-20) [Perry — Verified]; review SLAs so review doesn't become the queue (LinearB's 4.6× wait is the failure to avoid).
   - Test discipline: test pyramid kept honest (fast unit, meaningful integration, few E2E on critical flows); production-shaped fixtures for risky paths (R-19) [CrowdStrike — Verified]; flaky tests quarantined with owners, never tolerated (R-18).
   - Progressive delivery: canary with automatic promotion/rollback on golden-signal regression; feature flags with owner + expiry hygiene (R-25, R-26, R-16) [Knight Capital; CrowdStrike — Verified].
2. **Threat modelling and security as routine:** 10-minute threat models for new trust boundaries (R-09); ASVS L1 gap register maintained per release; dependency patch SLAs tracked like any SLA with SBOM per release (R-23) [Log4Shell — Corroborated]; secret-scan + SAST + SCA + DAST cadence.
3. **Product-analytics instrumentation engineered** (gaps T8 — Corroborated, practitioner consensus): tracking plan as the authoritative spec; schema validation in CI; typed tracking library; identity resolution designed before the first Track call; consent in the collection layer. The funnel evidence the business will need in Phase 3 is trustworthy only if this exists now.
4. **AI cost metering** (R-32 — Proposed as named rule): token/compute cost per request, attributed per feature and per user cohort, with cost anomaly alerts. Unit economics known before scale, not discovered after. [Demo-vs-product economics — Corroborated]
5. **Backups and restore discipline** (R-24): monitored backup success, tested alert paths, rehearsed restores on a calendar, RPO/RTO written and verified. [GitLab 2017 — Verified]
6. **The improvement cadence** (small-team OS #17): monthly 30-minute review — DORA trends (R-33), one bottleneck to fix, kill/fix/keep for one feature (R-34). DORA's own guidance: team-level, never individual [Verified].

**Quality-gate verdicts that govern the Phase 2 → 3 transition:**
- **Gate 6 (Testing):** GO in full form — frozen release candidate, full interaction inventory exercised, regression suite green, defect log with severities, no unresolved S1/S2.
- **Gate 7 (Security review):** GO — threat models current for all trust boundaries; ASVS L1 maintained; patch SLAs met.
- **Gate 8 (Deployment):** GO — progressive rollout automated or routine; rollback rehearsed quarterly (game-day).
- **Gate 9 (Post-launch):** GO — SLOs defined with error budgets starting to govern release risk (R-31); incident metrics (MTTR, time-to-detect) reviewed in postmortems.

**Deliberately deferred:**
- Error-budget *policy* as a hard gate on shipping — trigger: enough reliability history that the budget math is honest (SRE, Verified).
- Load/chaos testing as routine — trigger: scaling risks identified by measurement (R-17: no optimisation without measurement).
- Agent autonomy expansion (read-only investigation → write with approval gates) — trigger: eval harnesses show agent workflows passing tests and surviving review (automation 01).
- A second database or a message broker — trigger: measured workload divergence or burst/fan-out pain (spec-arch, Corroborated).

**Why this order:** DORA 2025's amplifier finding [Corroborated] — AI amplifies the system it lands in; the seven capabilities that flip AI from harm to help are pre-existing engineering disciplines (small batches, strong tests, fast feedback, version control, platforms). Phase 2 is *building those disciplines deliberately* instead of hoping they emerge. "Speed without stability is accelerated chaos" is the price of skipping it.

---

## Phase 3 — Scale (Proposed)

**Goal:** grow usage, team, and surface area without the system degrading — scaling the *verified* loop, not just the output volume.

**Entry criteria:**
- Phase 2 exit gates GO.
- At least one bet has passed its post-launch evaluation against a pre-committed metric (R-02, R-34) — the loop demonstrably moves outcomes, not just ships artefacts.
- Kill/fix/keep has been run at least once and a feature was actually killed or fixed (the kill mechanism is proven, not theoretical — otherwise this is the build trap with better tooling).

**What gets built:**
1. **Scaling on measured pain only:** service extraction with an ADR explaining the measured trigger (deploy contention, divergent scaling profile, failure-isolation need) [Corroborated]; async/event-driven paths with the full production prerequisites (idempotent consumers, bounded retries + alerting DLQs, outbox publishing, schema registry, queue-lag alerts) [Corroborated]; caching with an invalidation story; specialised stores per genuinely different workload (search, time-series). Each addition is an operational commitment, reviewed as one.
2. **Error-budget governance** (R-31): SLOs mediate feature-vs-reliability work; budget-burn alerts; the freeze policy written down *before* it's needed. [SRE — Verified]
3. **AI spend governance** (R-32): per-feature unit economics reviewed against value produced; design for the expensive tail (caching, smaller models for easy cases); caps and abuse protection. The margin-collapse-on-success failure mode (AP-18) is a Phase-3 killer.
4. **Security maturity:** ASVS L2 as the target for sensitive-data surfaces; annual pentest as *validation*, not the plan; coordinated-disclosure page (security.txt); agent tool-permission audits.
5. **Quality gates in full:** all nine gates running at their calibrated risk tier (§17: Tier 1 mandatory-heavy, Tier 2 default, Tier 3 lightweight); the gate summary table is the operating picture.
6. **Deceptive-UX and regulatory surfaces** (gaps T10): the FTC Consumer Reviews/Testimonials Rule (16 CFR Part 465, effective Oct 2024, ~$53k per violation [Verified]) and adjacent regimes (UK DMCC, California age-appropriate design) operationalised as launch-gating checks — testimonial pipelines with provenance checks, no AI-generated "customers", no dark patterns in growth UX.

**Quality-gate verdicts that govern staying in Phase 3** (continuous, not a one-time exit):
- **All nine gates** at the product's calibrated risk tier, with NOT ASSESSED treated as a blocker and exceptions named, owned, and dated.
- **DORA trend review** (R-33) quarterly: deployment frequency, lead time, change failure rate, recovery time — acting on the bottleneck, never ranking people.
- **Kill/fix/keep** (R-34) on a cadence: every significant feature judged against its pre-committed metric; removal ships with rollout care (R-25).

**Deliberately deferred (even here):**
- Service mesh, platform team, multi-region active-active — trigger: the team size and reliability requirements where the operations cost is justified by measured need, not anticipated need (the hyperscale cargo-culting §15 forbids).
- Bespoke ML infrastructure — trigger: the product's differentiation genuinely requires it (R-07).

**Why this order:** Phase 3 is where §13's deferred bottleneck — maintenance and operations — arrives. GitClear's structural decay [Corroborated]: duplication +81%, refactoring 21%→<4% of commits. The kill/fix/keep ritual and error budgets are the counterweights; without them, Phase 3 is where throughput gains convert into maintenance debt.

---

## Summary: the roadmap at a glance (Proposed)

| Phase | Goal | The one thing it proves | Governing gate verdicts | What must NOT happen yet |
|---|---|---|---|---|
| **0 — Foundations** | One safe deploy to real users | The floor holds: build, deploy, roll back, get paged | Gate 8 (Deployment) GO; Gate 9 (Post-launch) GO lightweight | No product build before the floor exists |
| **1 — First loop** | One bet, end to end, measured | The whole loop works: discovery → build → measure → learn | Gates 4, 5, 7, 8, 9 GO on the first bet | No scaling either generation or verification until the loop is proven |
| **2 — Hardening** | Verification becomes the default | The system absorbs volume without destabilising | Gate 6 full GO; Gates 7, 8, 9 mature | No generation scale-up before verification is industrialised |
| **3 — Scale** | Grow without degrading | Outcomes move at scale; the tail is priced | All 9 gates at calibrated tier, continuously; DORA trends; kill/fix/keep | No hyperscale architecture on anticipated need |

**The phase-transition rule (Proposed):** a phase ends when its governing gate verdicts are GO — never when the calendar says so. NO-GO stops the transition; NOT ASSESSED is not a pass; exceptions require a named owner and a date. The roadmap's deepest claim is a sequencing claim: *verification capacity before generation scale*. Everything else is detail.

---

**Sources:** `research/rules/03-small-team-os.md` · `research/quality/03-quality-gates.md` · `research/economics/02-bottleneck-analysis.md` · `research/rules/01-engineering-rules.md` · `research/rules/02-anti-patterns.md` · `research/discovery/01-problem-discovery.md` · `research/discovery/03-validation.md` · `research/spec-arch/02-architecture-decisions.md` · `research/automation/01-automation-stack.md` · `research/gaps/01-missing-topics.md` (T8, T10) · `research/rules/04-templates/`
