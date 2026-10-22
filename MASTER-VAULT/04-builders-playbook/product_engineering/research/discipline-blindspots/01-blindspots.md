# Discipline Blind Spots — Blind-Spot Hunter Workstream

**Status:** follow-up phase research, 2026-10-10. **Method:** public-ecosystem sweep (official docs/engineering blogs/repos/papers/talks/postmortems **and** Reddit, X, HN, practitioner blogs, GitHub issues/PRs/discussions, podcasts, teardowns, benchmarks, failure reports), with a deliberate hunt for FAILURE EVIDENCE per candidate. **Label discipline:** every major claim labeled **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown**, inherited from the report's README conventions. Nothing installed, built, configured, ranked, or recommended. **Date accessed for all web sources:** 2026-10-10.

**Scope note:** this workstream tested 8 assigned candidates plus discovered ones, against (a) the 19-section report, (b) §19's 11 confirmed missing topics, and (c) the 8 sibling follow-up disciplines (trust & safety; EU AI Act compliance engineering; payments/billing/entitlements; mobile release engineering; notifications engineering; API-as-product; compliance engineering SOC 2/ISO/FedRAMP/PCI; FinOps). A candidate is CONFIRMED only when the evidence shows teams failing without it **and** the report + siblings have no home for it.

## Ranking

Same F/B/A/E rubric as §19 (Failure weight / lifecycle Breadth / Actionability / Evidence strength).

| # | Discipline | F | B | A | E | Verdict |
|---|---|---|---|---|---|---|
| B1 | Data-contract / data-quality engineering (pipelines) | H | H | H | Corroborated | **CONFIRMED** |
| B2 | Multi-tenancy engineering | H | M | H | Corroborated | **CONFIRMED** |
| B3 | Experimentation-platform engineering | H | M | H | Corroborated | **CONFIRMED** |
| B4 | ML platform / MLOps beyond LLM evals | H | M | M | Mixed (failure Corroborated; discipline Inferred) | **CONFIRMED** |
| B5 | Disaster-recovery engineering — residual gap (RTO/RPO, evacuation, failure-domain separation) | M | M | H | Corroborated | **CONFIRMED (narrow; overlaps §11)** |
| K1 | Email deliverability engineering | — | — | — | — | **KILLED — subsumed by notifications sibling** |
| K2 | InnerSource | — | — | — | — | **KILLED — niche, no failure evidence** |
| K3 | Developer-support / support-ops tooling engineering | — | — | — | — | **KILLED — thin evidence; adjacent to T4/§02/§04** |
| K4 | Data-migration engineering (discovered) | — | — | — | — | **KILLED — already covered (§11 §6)** |

---

## B1 — Data-contract / data-quality engineering (data pipelines) — CONFIRMED

**What it is (plain English).** The discipline of making data pipelines *fail loudly at the source* instead of silently at the dashboard. A **data contract** is an explicit, enforced agreement between a data producer and its consumers about schema, types, constraints, and freshness — checked at ingestion or build time, before bad data propagates. Around contracts sits **data-quality engineering**: tests on every pipeline run (the data equivalent of unit tests), freshness/volume/schema anomaly monitoring ("data observability"), ownership per dataset, and data SLAs with named consumers.

**Mechanics (how it works).** Contract validation at execution time (e.g., dbt's `contract.enforced: true` fails the build before bad data is written); dbt/Great Expectations/Soda tests asserting uniqueness, non-null, accepted ranges on every run; the five observability pillars (freshness, volume, quality, schema, lineage) monitored per pipeline stage; versioned schemas with backward-compatible evolution and migration windows for breaking changes; severity-tiered contract tests (fail loudly vs warn); lineage so a broken upstream is traceable to affected downstream tables.

**Why compulsory — the failure evidence.** This is the strongest failure record of any candidate tested:
- Monte Carlo's 2026 State of Data Quality survey (via practitioner reporting, Oct 2026): **68% of teams need 4+ hours just to detect a data incident** (up from 62% in 2022); **average resolution 15 hours**; **74% of data issues are found by business stakeholders first** (up from 47% in 2022) — "for 3 out of 4 issues, the monitoring system is a VP in a Slack channel" (**Corroborated** as vendor survey; direction-trusted, magnitude-discounted per report rules).
- dbt's 2026 State of Analytics Engineering (same reporting): 72% of data teams prioritise AI coding while **only 24% prioritise AI-assisted pipeline testing and observability** — teams are accelerating pipeline *authorship* while neglecting pipeline *verification*, the exact asymmetry the report's T2 names for code review.
- The canonical failure mode, repeated across practitioner sources: **silent schema changes** — an upstream renames a field; nothing fails; nulls propagate through three transformations; the CFO asks why revenue reads zero. "One renamed field away from a very bad day" (practitioner consensus, **Corroborated**).
- Second-order failures: LinkedIn 2019 pipeline freeze cited as causing **months of A/B delays** (single secondary, attributed); Peloton 2021 demand forecasts off ~300% (single secondary, attributed — treat as illustrative, not audited).

**How world-class companies do it.** Netflix's Guardian programme cited as running contract-style checks across 1,000+ pipelines daily (single secondary, **Corroborated-single** — not independently audited); Uber Michelangelo cited as making pipeline quality checks mandatory (single secondary). The convergent practitioner playbook: contracts at ingestion, tests in CI on every run, observability on the five pillars, owner per dataset, weekly data-health rituals, 99.9%-style data SLOs (**Corroborated** as practitioner consensus).

**Key practices.** Producer/consumer contracts with enforced schemas; backward-compatible evolution by default, versioned contracts + migration windows for breaking changes; dbt/Great Expectations/Soda tests as build gates; freshness and volume anomaly alerting; lineage catalogues (Amundsen/DataHub class); data SLAs naming owner, freshness target, and consumers; blameless data postmortems.

**Failure modes.** Silent schema drift; dashboard-discovered incidents; taxonomy-less pipelines nobody owns; alert fatigue from un-actionable monitors; the "Snowflake it" fallacy (new warehouse, same ungoverned pipelines); AI-accelerated pipeline authorship without verification (the 72%/24% split above).

**Bottlenecks.** Detection latency (hours before anyone knows); ownership vacuum (data quality is everyone's problem until it is no one's); backfill cost once bad data has fanned out; trust collapse — once stakeholders stop trusting the numbers, every decision re-litigates the data first.

**Lifecycle slot:** build (contracts ship with pipelines) → operate (observability, incident response) → improve (data SLOs, trust repair). **Provisional home:** new section or a data-engineering extension of §15's reference architecture; pairs with §19-T8 (instrumentation) — T8 owns *event* contracts, B1 owns *pipeline* contracts. Explicitly distinct from §11's Pact API-contract coverage (service-to-service, not data-producer-to-consumer).

---

## B2 — Multi-tenancy engineering — CONFIRMED

**What it is (plain English).** The architecture discipline of serving many customers from shared infrastructure *without them ever touching each other* — and without one customer's workload degrading another's. It covers the tenancy-model decision (silo / pool / bridge), tenant isolation (data, compute, cache, queues), noisy-neighbor fairness, per-tenant operations (backup/restore, migration, data export), and tenant-aware security testing.

**Mechanics.** **Silo** (database-per-tenant): strongest isolation, simplest compliance story (HIPAA/PCI/SOC 2), cost rising linearly per customer. **Pool** (shared schema, `tenant_id` on every row): cheapest and fastest to build; one heavy tenant can slow everyone; one missing `WHERE tenant_id` clause leaks data. **Bridge** (the common real answer): pool the small tenants, silo the regulated/enterprise/heavy ones in the same product — and design from day one so moving a tenant across the line is a migration, not a rewrite. Fairness machinery: per-tenant rate limiting at the gateway, Kubernetes resource quotas per tenant namespace, tenant-scoped autoscaling metrics, fair-share queue schedulers (deficit round-robin across tenant virtual queues), automatic graduation of heavy tenants to dedicated infrastructure. Isolation machinery: tenant-context guards injecting tenant scope into every request, row-level security as a second line of defence, per-tenant cache key namespacing, tenant-tagged backup metadata, adversarial leak tests ("tests whose only job is to try to read another tenant's data, run on every release").

**Why compulsory — the failure evidence.**
- **Cloudflare, September 2026 (Corroborated** via company disclosure + secondary reporting): a `skip_block_zeroing` misconfiguration on shared dm-thin storage pools in Containers/Sandboxes let one customer's container recover residual data (filesystem metadata, directory structures, complete SQLite databases, `.env`/credential files) left by other tenants on the same host. Reported via HackerOne Sept 4, fleet fixed by Sept 19; no evidence of malicious exploitation found. A tenant-isolation failure at the storage layer of a hyperscaler — caught by a researcher, not by the platform's own controls.
- **Flowise, August 2025 (Corroborated** via security advisory + practitioner analysis): an authenticated vulnerability where a `$vars` object intended for the current workspace's environment variables reportedly included other tenants' variables — the canonical "logged in normally, sees another customer's data" incident.
- The stakes framing from AWS's SaaS tenant-isolation guidance (via practitioner citation): crossing the tenant boundary "in any form would represent a significant and potentially un-recoverable event for a SaaS business." The same bug class sits at the top of the OWASP API Security Top 10 (2023) as API1: Broken Object Level Authorization (**Verified** via OWASP).
- The "multi-tenant architecture wall" (practitioner consensus, **Corroborated**): "almost every SaaS company hits it" — the report's own AP-05 names multi-tenancy as a "genuinely stable domain pattern," i.e., one of the few abstractions worth designing early, but the report never says what the engineering *is*.

**How world-class companies do it.** AWS SaaS Factory's isolation guidance (silo/pool/bridge selection per tenant); the bridge-model playbook (start pooled for speed, isolate on compliance/load triggers, `tenant_id` from the first commit); CSO-practitioner framing for regulated tenants (FedRAMP/ITAR/CJIS pushing dedicated "cluster-per-tenant" at 2–3× cost); fair-share scheduling and per-tenant quotas as the noisy-neighbor answer rather than over-provisioning.

**Key practices.** Tenancy-model decision recorded per product with graduation triggers (compliance requirement, data-residency clause, repeated noisy-neighbor incidents); tenant_id tagging from day one; per-tenant rate limits, quotas, and metrics; tenant-context guards + RLS defence-in-depth; cross-tenant leak tests in CI; tenant-granular backup/restore and GDPR export; idempotency and rate-limit keys scoped by tenant.

**Failure modes.** Cross-tenant data leaks (the unrecoverable event); noisy-neighbor degradation surfacing first with the largest accounts; per-tenant restore impossible under contractual SLAs in pooled models; load tests passing on average-tenant profiles while production skew kills the shared instance; RLS-only isolation (one DB-engine CVE from full exposure).

**Bottlenecks.** The tenancy decision compounds: retrofit cost grows with every untagged row and unscoped key; enterprise security questionnaires arrive before the isolation story exists; compliance frameworks (FedRAMP/ITAR) can force dedicated infrastructure that the unit economics didn't plan for.

**Lifecycle slot:** architecture/design (the model decision is load-bearing in the first sprints) → build (guards, quotas, leak tests) → operate (per-tenant monitoring, graduation, restore). **Provisional home:** new section or inside §15 reference architecture as the SaaS tenancy layer; security aspects adjacent to §10/R-09. Overlap check: §02 mentions tenant isolation only for AI retrieval indexes; §14 mentions multi-tenancy once as an abstraction exception; R-09 covers threat-modelling trust boundaries generally. None of them is the discipline.

---

## B3 — Experimentation-platform engineering — CONFIRMED

**What it is (plain English).** The engineering discipline of making product experiments *trustworthy at scale* — not "we run A/B tests" but the platform, statistics, and process that stop the organisation from shipping false positives. It has three layers: the **flagging/assignment infrastructure** (consistent bucketing, mutual exclusion, holdouts, geo experiments), the **stats engine** (variance reduction, sequential testing, multiple-comparison correction, diagnostics), and the **operating system** (experiment review, pre-registration of hypotheses and metrics, learnings repositories).

**Mechanics.** Consistent hashing assignment so a user stays in their arm; mutual-exclusion layers so experiments don't collide; CUPED-style variance reduction (pre-experiment covariates as regressors — "used in every experimentation system at Lyft, Uber, Airbnb, Netflix, and Microsoft" per Che Sharma's UDEM talk, secondary summary); sequential testing / always-valid p-values so teams can peek without p-hacking; Bonferroni/Holm correction when testing multiple metrics; holdout groups measuring the cumulative impact of the whole programme; switchback and geo experiments (Netflix's Quasimodo) for marketplace/network-effect cases where user-level randomisation leaks; diagnostics that catch sample-ratio mismatch and other invalid experiments before anyone reads the results.

**Why compulsory — the failure evidence.**
- The **peeking** failure mode (practitioner consensus, **Corroborated**): classic test statistics assume a fixed sample size decided in advance; in practice everyone watches the dashboard, and "many practitioners fall victim to peeking, where an experimental outcome is erroneously called before the proper sample size has been reached" — shipping features on false positives, or killing winners early.
- **Multiple metrics without correction** → false positives "and the overall p-hacking problem" (Sharma talk summary): testing three or four variants against a handful of metrics without Bonferroni/Holm-style correction manufactures wins.
- Netflix's institutional lesson: "our intuition is generally wrong" — even no-brainer ideas (auto-play next episode) required testing; artwork experiments moved viewing **20–30%** for a title (company-reported via secondary, **Corroborated-single**). The corollary the evidence supports: organisations that test on intuition instead of a disciplined platform systematically misattribute.
- The cost of *not* having the platform: LinkedIn 2019's pipeline freeze cited as causing months of A/B delays (single secondary, attributed) — experimentation velocity is gated by data-platform reliability, tying B3 to B1.

**How world-class companies do it.** Netflix (experimentation built into product decisions; geo experiments with re-randomisation and difference-in-differences; Quasimodo automation); the CUPED-at-every-hyperscaler pattern above; Statsig-style sequential/switchback/bandit test types with warehouse-native deployment; Kohavi's *Trustworthy Online Controlled Experiments* as the canon (§11 already cites Kohavi/Microsoft research in its sources — the report knows the *citation* but not the *engineering*).

**Key practices.** Assignment infrastructure with mutual exclusion and holdouts; stats engine with variance reduction + sequential analysis + multiplicity correction; experiment diagnostics (sample-ratio mismatch, pre-period balance); hypothesis/metric pre-registration; a learnings repository so results compound; guardrail metrics that auto-stop harmful experiments.

**Failure modes.** Peeking → false-positive launches; uncorrected multiple comparisons → manufactured wins; overlapping experiments → polluted reads; network-effect leakage → wrong conclusions in marketplaces; no holdout → nobody knows what the programme actually contributed; diagnostics-free dashboards → invalid experiments read as results.

**Bottlenecks.** Statistical expertise doesn't scale with experiment volume — the platform must encode the stats so product teams can't mis-set them; sample-size constraints in low-traffic products (sequential testing helps but doesn't create power); the cultural step from "we A/B test" to "we trust the platform's verdict over intuition."

**Lifecycle slot:** build (flagging infra ships with the product) → improve (the experimentation loop is the improvement engine). **Provisional home:** paired with §19-T8 (instrumentation) — T8 makes behaviour *measurable*, B3 makes decisions *trustworthy*; or inside the §13 feedback-loop coverage, which currently names experimentation without engineering it. Overlap check: §11's source list cites Kohavi; §13 mentions feedback once; neither covers the discipline.

---

## B4 — ML platform / MLOps beyond LLM evals — CONFIRMED

**What it is (plain English).** The report covers LLM/agent evals (§05) thoroughly. Classical ML — models trained on historical data and serving predictions in production (pricing, fraud, recommendations, forecasting) — needs a different platform: **training infrastructure**, **feature stores** (consistent features between training and serving), **model registries** (versioning, lineage, approvals), and **drift monitoring** (detecting when the world has moved out from under the model). The discipline is keeping a *deployed* model honest as reality changes.

**Mechanics.** Feature stores eliminating training/serving skew; model registries with versioned artefacts, lineage, and promotion gates; monitoring split into *data drift* (input distributions moved — detectable with tests like Kolmogorov-Smirnov per column, no model needed) vs *concept drift* (the relationship itself changed); retraining pipelines with backtesting across market regimes; uncertainty margins sized to the model's published error rate; human-in-the-loop gates before high-stakes automated decisions.

**Why compulsory — the failure evidence.**
- **Zillow Offers, 2021 (Corroborated):** models trained on a stable, appreciating housing market kept producing confident valuations after market dynamics shifted (supply-chain renovation costs, price volatility). Result: ~$304M write-down in Q3 2021, ~2,000 jobs cut, the iBuying business shut down; by Q3 2021, 93% of Zillow's Phoenix listings were priced below what it had paid (GeekWire 2021 via 2026 secondary analysis; figures **Corroborated** across outlets). The durable lesson from practitioner analysis: "the deeper issue was the absence of strong monitoring systems capable of detecting drift and responding quickly to changing conditions" — a platform failure, not just a model failure.
- **Epic's sepsis-prediction model (Corroborated** via the LinkedIn practitioner analysis, Sept 2026): a genuine predictor leaked into training, then shipped generically to hundreds of hospitals that "had no access or expertise to catch it before deploying" — a *deployment-governance* failure wearing a modelling error's clothes.
- Counter-evidence preserved: the same analysis argues that in six of seven studied AI failures (MD Anderson, Zillow, Amazon hiring, Ofqual, UK Home Office, DWP), "the decision that killed the project was made before the model existed" — problem framing, label selection, deployment governance. This does not weaken B4; it *scopes* it: the platform discipline covers exactly the deployment/monitoring/governance layer where those failures lived.

**How world-class companies do it.** Uber's Michelangelo (cited in practitioner reporting as making ML quality checks mandatory — single secondary); the feature-store pattern for training/serving consistency; open drift-detection libraries (Evidently-class Kolmogorov-Smirnov per-column checks) as the cheap first line; retraining cadences tied to drift signals rather than calendars.

**Key practices.** Feature store as the single source of truth for features; model registry with lineage and promotion gates; data-drift and concept-drift monitors with alert thresholds; backtesting across regimes before promotion; error-rate-sized safety margins on automated decisions; staged rollout of model versions with shadow scoring.

**Failure modes.** Training/serving skew; silent drift (confident predictions on a moved world); unversioned models nobody can roll back; retraining on polluted feedback loops; automating high-stakes decisions on point estimates with no uncertainty margin.

**Bottlenecks.** Monitoring is the neglected half of every ML budget (the build-vs-operate asymmetry, cf. §19-T9); drift signals are noisy and need baselines; the organisational gap — data scientists own the model, nobody owns the model's *behaviour in production*.

**Lifecycle slot:** build (training infra, feature store) → ship (registry, promotion gates, shadow scoring) → operate (drift monitoring, retraining). **Provisional home:** new section or an ML-platform extension of §05, explicitly scoped as "classical ML serving" to avoid colliding with §05's LLM/agent-eval coverage. Overlap check: zero hits for feature store / model registry / drift anywhere in the report — confirmed by full-text search.

---

## B5 — Disaster-recovery engineering: the residual gap (RTO/RPO, evacuation, failure-domain separation) — CONFIRMED (narrow)

**What it is.** §11 covers recovery *tactics* well (chaos engineering, game days, rollback rehearsal, "backups are not recovery" via Atlassian/GitLab, SLOs/error budgets). What it does not cover is DR as an *engineered programme*: **RTO/RPO as objectives** (how much downtime and data loss the business can survive, per system, translated into architecture), **evacuation drills** (sustained operation without a zone/region, not just a failover demo), **failback** (getting back, the forgotten half), and **failure-domain separation** (a backup in the same building is a copy, not a recovery).

**Why compulsory — the failure evidence.**
- **OVHcloud Strasbourg fire, March 2021 (Corroborated):** SBG2 destroyed, SBG1 damaged; ~3.6M websites dark; customers discovered their paid backups were stored *in the same complex* — "for them the difference between a backup and a copy mattered more than the marketing had suggested." A class action of ~140 companies sought ~€10M; a French court ordered damages in March 2023. The lesson is distinct from §04's "backups are not recovery" (which is about *restore testing*): this is about *failure-domain separation* — geography as an engineering decision, owned by nobody ("the location of a backup was a checkbox nobody owned").
- The **rehearsed-failover illusion** (practitioner analysis, Oct 2026, **Corroborated-single**): a DR demo run once, in a scheduled window, by the three engineers who built it, measures the failover under ideal conditions — "no concurrent production load, no partial outage, no engineer logging in from a hotel room at two in the morning." The four-minute number is not the number that matters.
- The programme mechanics exist as vendor practice: AWS ARC zonal-shift multi-day evacuation drills (48–72h on N-1 AZs, "produce evidence that your multi-AZ architecture delivers genuine, sustained resilience"), Resilience Hub validating architectures against declared RTO/RPO, quarterly failover tests measuring *actual* RTO/RPO against targets (AWS architecture blogs, 2026 — vendor, direction-trusted).

**How world-class companies do it.** RTO/RPO declared per system from business-impact analysis, then validated by drill (not estimated); sustained evacuation drills rather than momentary failover tests; backup-success monitoring with end-to-end-tested alerting (the report's GitLab lesson) extended to *restore* rehearsals and *failback* rehearsals; geographic separation of backups as a named architectural decision with an owner.

**Key practices.** RTO/RPO targets per tier with named owners; quarterly failover tests measuring actuals vs targets; multi-day evacuation drills; failback runbooks tested, not just written; backup/restore/failback as three separate rehearsed capabilities; failure-domain mapping (power, network, building, site, region) for every recovery copy.

**Failure modes.** Backups sharing the primary's failure domain; untested restores (GitLab, covered); untested failback; RTO/RPO as slideware; the rehearsed demo mistaken for capability; silent replication failure discovered during the disaster.

**Bottlenecks.** Drills are expensive and scary, so they get scheduled "next quarter" indefinitely; multi-region roughly triples cost (practitioner estimate); failback is unglamorous and therefore untested; nobody owns the backup's geography.

**Lifecycle slot:** architecture (RTO/RPO targets, failure-domain design) → operate (drills, rehearsals, quarterly tests). **Provisional home:** extension of §11's recovery coverage, not a new top-level section — this is the narrowest CONFIRM, kept because RTO/RPO-as-engineering and evacuation drills have no home anywhere in the report, and the OVH failure mode (failure-domain separation) is distinct from the GitLab/Atlassian restore-testing lesson already covered. The compliance sibling owns DR *plans as audit artefacts*; B5 is the *engineering* of actually recovering.

---

## KILLED candidates

### K1 — Email deliverability engineering — KILLED (subsumed by sibling)

**Reason.** Real practice, real regulatory floor — but it is the *email channel* of notifications engineering, which a sibling workstream already owns. A standalone section here would duplicate that workstream's email-delivery coverage.

**What the evidence shows.** Gmail/Yahoo bulk-sender requirements (Feb 2024; Gmail escalated to active rejection Nov 2025; Microsoft followed May 2025): SPF + DKIM + DMARC (p=none minimum), spam-complaint rate under 0.1–0.3%, one-click unsubscribe honoured within 48h, 5,000/day threshold. Non-compliant bulk mail is now rejected at the gateway (550 5.7.515) rather than filtered to spam — "the old playbook of send, measure, clean up no longer has a measurement phase" (**Corroborated** via practitioner reporting, Sept 2026). Dedicated-IP warmup ramps, reputation monitoring via Google Postmaster Tools, subdomain separation — all genuine mechanics.

**Why killed anyway.** (a) The sibling "notifications engineering" workstream is the natural home: deliverability is channel-delivery engineering, and splitting email-reputation out from notification orchestration/preferences/multi-channel delivery would fragment the topic. (b) Failure evidence skews marketing-ops (campaigns landing in spam), not product-engineering discipline — no postmortem of a *product* failing for lack of a deliverability *engineering* function was found. (c) The report's closest existing touchpoint (GitLab's DMARC-bounced backup alert, §04) is incidental.

**Handoff for the notifications sibling:** the Gmail/Yahoo/Microsoft authentication mandates and the 0.1–0.3% complaint ceiling are load-bearing 2024–2026 facts for any email-channel treatment; evidence rows EV-DEL-01–03 in the register carry the sources.

### K2 — InnerSource — KILLED (niche, no failure evidence)

**Reason.** Genuine practice with real enterprise adoption — but scale-dependent, without failure/postmortem evidence, and conceptually adjacent to topics the report already owns.

**What the evidence shows.** InnerSource (open-source practices applied inside the company: discoverable repos, cross-team pull requests, maintainer review) has documented adoption at Bosch (InnerSource chief expert on record), PayPal (2014-era practices: 90% coverage gates, in-repo docs, GitHub-based discussion), BBC, Mercedes-Benz Tech Innovation, Dutch Tax Administration (UN Open Source Week panel, June 2025), NYT (internal developer platform contributions), Walmart (tooling unification), GitHub (internal language communities), plus academic case-study backing (Riehle et al., SAP platform case studies) (**Corroborated** for adoption; benefits like "40% drop in repeated work" are single-source practitioner claims, unattributed-unverified).

**Why killed anyway.** (a) No failure evidence: the hunt found adoption stories and benefit claims but no postmortem, measured loss, or reversal attributable to *lacking* InnerSource — the compulsory bar is not met. (b) Scale-dependent: every adoption case is a large enterprise with platform/product-unit splits; nothing in the evidence suggests it is load-bearing for the report's core audience. (c) Adjacent to owned topics: §19-T5 (open-source strategy) covers the open-source mechanics; §19-T1 (platform engineering) covers the internal-platform collaboration problem InnerSource addresses. A merge into T1/T5 would be the coordinator's call, not a new discipline.

### K3 — Developer-support / support-ops tooling engineering — KILLED (thin evidence; adjacent)

**Reason.** The internal tooling that makes support fast (admin consoles, audited impersonation, tenant/user/billing ops, role-based internal permissions) is real engineering — but the evidence base is thin and the report already covers the adjacent ground.

**What the evidence shows.** Practitioner/skill sources describe a convergent pattern: an operations surface (tenant ops, user ops, billing ops, support ops, compliance ops), a least-privilege internal role model (support_l1/l2, billing_ops, engineering_oncall, security — not a single `is_super_admin` boolean), an audited mutation pipeline (actor, justification, before/after state, same-transaction audit log), and impersonation as the most-sensitive feature (time-boxed, justified, banner-visible, fully audited) (**Inferred** as discipline — sources are community skill repos of uncertain provenance, not primary engineering writing; treat mechanics as plausible, not verified).

**Why killed anyway.** (a) No failure postmortem found: no case of a company failing, losing material revenue, or suffering a breach *because* it lacked support-ops tooling (the inverse — support tools as attack surface — appears in security literature, but that's §10's territory). (b) Covered adjacently: §02's Domain C playbook (post-resolution sampling, action approvals, audit logging), §04's Cursor "Sam" case (support-ops governance), and §19-T4 (workforce-automation / human-fallback architecture) together own the problem space; the admin console is the *instrument* of T4's escalation boundary, not a separate discipline. Recommended: fold as a practice note under T4 rather than a new section.

### K4 — Data-migration engineering (discovered candidate) — KILLED (already covered)

**Reason.** Tested as a discovery candidate (expand–contract, dual-write, backfills, parity verification — strong practitioner consensus, Stripe's "Online migrations at scale" as canonical writeup, Christoph Bussler's dual-write-divergence counterweight). **Killed on coverage check:** §11 §6 already covers it in depth — expand–migrate–contract with dual-write, resumable rate-limited backfills with reconciliation, shadow-reads with diff logging, flag-gated read switching, and the driving asymmetry ("rolling back code is easy; rolling back data migrations is hard"), all labeled Corroborated. Nothing to add.

---

## Discovery notes — other candidates considered and not pursued

- **Search/relevance engineering:** real discipline, but niche to search-heavy products; no failure-evidence sweep performed — noted as possible future work, not a confirmed blind spot.
- **Observability-cost engineering** (telemetry spend, sampling, cardinality): 2024–2026 practitioner topic, but thin as a *compulsory* discipline; overlaps the FinOps sibling. Noted, not confirmed.
- **Docs-as-product / documentation engineering:** niche; §19-T6 touches developer docs within ecosystem strategy. Not pursued.
- **Feature-flag lifecycle management:** §11 covers flag misuse (Knight Capital, Google Cloud 2025) and flag-graveyard retire triggers. Covered.
- **Data-residency/sovereignty engineering:** folded into B2 as a tenancy-model driver (FedRAMP/ITAR) rather than standalone.

## Honest gaps in this blind-spot hunt

1. **No live-browser verification, no paywalled sources, no non-English sweep.** All sources are public web, fetched as text.
2. **Vendor-interest contamination.** Load-bearing figures from vendors selling the remedy: Monte Carlo's data-quality survey (B1), Statsig's experimentation marketing (B3). Mechanisms are cross-corroborated; vendor figures are direction-trusted, magnitude-discounted per report rules.
3. **Attribution debt.** Netflix Guardian's "1,000+ pipelines daily" and Uber Michelangelo's "mandatory" quality checks (B1), the artwork 20–30% lift (B3), Peloton's ~300% forecast miss (B1) rest on single secondaries — marked as such in the register; verify against primaries before final-report citation.
4. **Zillow attribution.** The "drift did it" framing is **Inferred** from secondary analysis; the counter-argument (failures were pre-model: problem framing, no error-rate margin) is preserved in B4 and EV-ML-04. Both point the same way for engineering: the missing layer was deployment/monitoring/governance, i.e., the platform.
5. **Social sweep limits.** A dedicated per-candidate HN/X sweep was beyond the diminishing-returns stop; Reddit/GitHub surfaced via web search where indexed.
6. **B5 is the narrowest CONFIRM.** If the coordinator prefers, it folds into §11 as "RTO/RPO, evacuation drills, failure-domain separation" — the verdict is deliberately scoped so the merge is trivial.
7. **Email deliverability (K1)** evidence is preserved in the register as a handoff for the notifications sibling rather than dropped.
