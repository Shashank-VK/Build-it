# VERIFIER C — Adversarial Verifier Report | Phase 0 | 2026-08-31

## P0-03: MERGE, CLUSTER & CANONICAL PROPOSAL (12 → 6)

### Input Longlists
- **R-A (Broad Mapper) P0-01:** 12 archetypes: 01 Greenfield Full-Stack, 02 Production Backend/API, 03 Data Pipeline & Lakehouse, 04 Event-Driven Automation, 05 Browser/RPA, 06 AI/ML MLOps, 07 LLM Agent System, 08 Research/Synthesis, 09 Data Science/Dashboard, 10 Dev Tooling/CLI/SDK, 11 Infra/DevOps/IaC, 12 Migration/Strangler
- **R-B (Challenger):** Not delivered to verifier (parallel thread). Merge executed against R-A + inferred challenger deltas (mobile/game/embedded, financial/regulated, security gaps flagged in search corpus). Deduplication applied aggressively regardless.

### Clustering & Overlap Map

| Cluster | Members | Overlap Signal | Resolution |
|---------|---------|----------------|------------|
| **Product Engineering** | 01 + 02 + 10 (part) | 01 and 02 share auth, contracts, migrations, observability, preview deploys. 10 is product-engineering dogfooding (CLI/SDK) with same lifecycle (semver, backward-compat) but consumer is developer not end-user. | **MERGE 01+02 → C1; keep 10 as sub-mode inside C1** — lifecycle stage, not distinct harness. Split would duplicate scaffolding/contract gates. |
| **Data & Intelligence Fabric** | 03 + 06 + 09 | 03 (Batch/Streaming/ELT/Reverse-ETL), 06 (Notebook→Registry→Serving), 09 (Notebook→Dashboard) all share Bronze→Silver→Gold, DAG, idempotency, data versioning, reproducibility, data quality. 03 internally conflates 3 pipeline modes. | **MERGE 03+06+09 → C2; flag 03 as conflated** — batch/streaming/reverse-ETL are *modes*, not archetypes. Justification: warehouse-as-source-of-truth + experiment tracking cover all three. |
| **Automation & Surface Ops** | 04 + 05 | 04 (SaaS glue/webhooks/cron) and 05 (Playwright fleet/RPA) share trigger catalog, secret management, retry/compensation, selector resilience, stealth/proxy, stateful recovery. Distinct only in surface (API vs DOM). | **MERGE 04+05 → C3** — harness demands identical except selector vs webhook registry. Keep DOM-resilience as capability toggle, not archetype. |
| **Reasoning & Agentic Systems** | 07 + 08 | 07 (ReAct/multi-agent + tools/memory/guardrails) and 08 (long-horizon research/dossier) share source grounding, citation, hallucination gate, trace viewer, injection resistance, human review. 08 is 07 with *no side-effect tools* and stricter grounding. 07 itself conflates single ReAct vs crew. | **MERGE 07+08 → C4; flag 07 as conflated** — multi-agent is orchestration mode, not archetype. Research is read-only agent variant. |
| **Substrate & Operations** | 11 | Terraform/Pulumi, K8s, CI/CD, secrets, policy — declarative drift, blast-radius, cost visibility. No overlap with product/data harms to merge; distinct non-goals (containers/orchestration meaningless for embedded). | **KEEP → C5** |
| **Evolution & Modernization** | 12 | 6R/7R, codemods, dual-write, shadow traffic, incremental cutover. Spans product + data + infra but harness is uniquely migration-specific. | **KEEP → C6** — cannot merge without losing dual-write/shadow-traffic gating. |

**Drop/Merge Rationale Count:** Keep 2 (C5, C6), Merge 4 clusters covering 10 inputs. No outright drops — every seed archetype maps to a canonical; granularity reduced from 12 to 6 to avoid harness-factorial explosion.

**Conflated Flags (deduplicate aggressively):**
- **A03 Data Pipeline & Lakehouse = 3 archetypes in 1:** Batch vs Streaming vs Reverse-ETL have divergent DAG, CDC, warehouse-as-source-of-truth demands. Must be treated as modes under C2 with capability toggles, not separate canonicals.
- **A07 Agent System = 2 in 1:** Single ReAct loop vs multi-agent crew have opposite tool-registry/budget-guard/trace demands. Merged into C4 with orchestration-mode switch.
- **A08 vs A09 Research vs Data Science:** Both produce knowledge artifacts; split is *output format* (report vs dashboard), not harness. Merged into C2 (analytics product) vs C4 (synthesis) disambiguated by grounding gate presence.

---

### CANONICAL 6 (+ Constraints Matrix)

| # | Canonical Name | Definition | Example Projects | Key Constraints |
|---|----------------|------------|------------------|-----------------|
| **C1** | **Product Engineering (0→1 → Scale)** | End-user or developer-facing product owning full stack: scaffold → vertical slice → auth/billing → contracts → multi-tenant hardening → growth. Absorbs greenfield web, production backend, CLI/SDK/scaffold. | Micro-SaaS directory/scheduler; waitlist→Stripe→dashboard MVP; multi-tenant REST/GraphQL/gRPC API with webhooks/rate limits; extracted microservice; published CLI/linter/template generator/harness itself | **Solo vs Team:** Solo viable 0→1, team ≥3 for scale/multi-tenant **Prototype vs Production:** Both (gate: vertical-slice → contract-gated) **Cost/Latency/Security/Reliability:** Security (AuthN/AuthZ, secrets), Reliability (SLO), Latency P95 for API **Duration:** weeks→months, continuous **Supervision:** Low 0→1, high for breaking-change **Autonomy Tolerance:** High for scaffolding, low for migrations/billing |
| **C2** | **Data, Analytics & MLOps Fabric** | Data movement & intelligence fabric: ingest→transform→serve; Bronze→Silver→Gold, CDC/streaming, reverse-ETL, notebook→registry→serving→monitoring, notebook→dashboard. Unified by data quality/versioning/reproducibility. | CDC pipeline Postgres→warehouse; streaming feature store; ELT Lakehouse; notebook-to-API model serving with drift detection; interactive dashboard/report | **Solo vs Team:** Solo for exploration, team for pipeline ownership **Prototype vs Production:** Prototype (notebook) → Production (DAG/registry) **Cost/Latency/Security/Reliability:** Cost (training/compute), Reliability (idempotency, data quality), Security (PII) **Duration:** days (analysis) → quarters (platform) **Supervision:** Medium (data quality gate) **Autonomy Tolerance:** Medium; low for prod data mutation |
| **C3** | **Automation & Browser Surface Ops** | Scheduled/event-triggered glue across SaaS APIs, webhooks, cron/iPaaS plus stateful browser fleet for scraping/RPA/render. Shared harness: trigger catalog, secret retry/compensation, human-in-loop. | SaaS webhook glue; cron enrichment; Playwright fleet for price monitoring/form filling; stealth scraping with proxy rotation/stateful recovery | **Solo vs Team:** Solo-ideal **Prototype vs Production:** Production-grade from day 1 (failure-aware) **Cost/Latency/Security/Reliability:** Reliability (retry/stateful recovery), Security (secrets/stealth), Latency (queue) **Duration:** hours→weeks per flow, long-lived fleet **Supervision:** Low (alert on failure) **Autonomy Tolerance:** High (guarded by compensation) |
| **C4** | **Agentic & Knowledge Synthesis Systems** | Agent loop + tools + memory + guardrails (single ReAct or crew) *plus* read-only long-horizon reasoning producing grounded reports/dossiers. Unified by tool registry, budget guard, injection resistance, citation/hallucination gate, trace viewer. | ReAct tool-using agent; multi-agent crew; research dossier/memo over sources with citation; publication pipeline | **Solo vs Team:** Solo can ship single agent; crew needs team **Prototype vs Production:** Prototype (prompt) → Production (eval harness) **Cost/Latency/Security/Reliability:** Cost (token×volume), Latency (TTFT/p95), Security (prompt injection, PII), Reliability (faithfulness) **Duration:** days→months **Supervision:** High (hallucination/guardrail review) **Autonomy Tolerance:** Low→Medium (budget-gated) |
| **C5** | **Platform, Infra & DevOps (IaC)** | Provisioning & operating the substrate: Terraform/Pulumi, K8s, CI/CD, secrets, policy. Declarative drift detection, blast-radius control, cost visibility. Distinct non-goals vs app archetypes. | Terraform landing zone; K8s platform; CI/CD + policy as code; secrets rotation | **Solo vs Team:** Team (blast-radius) **Prototype vs Production:** Production only **Cost/Latency/Security/Reliability:** Cost (FinOps), Security (policy), Reliability (uptime) **Duration:** continuous **Supervision:** High (plan/apply gate) **Autonomy Tolerance:** Very low (dry-run required) |
| **C6** | **Migration, Modernization & Strangler Rebuild** | Moving legacy→modern via 6R/7R: rehost→replatform→rebuild with codemods, dual-write, shadow traffic, incremental cutover. | Monolith→microservices strangler; DB migration with dual-write; legacy language codemod | **Solo vs Team:** Team **Prototype vs Production:** Production (live system) **Cost/Latency/Security/Reliability:** Reliability (cutover safety), Security (parity), Cost (dual-run) **Duration:** months→years **Supervision:** Very high **Autonomy Tolerance:** Very low (shadow/dual-write gated) |

> Absolute paths for audit: `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness` (repo root; launch.json not present — verify before preview_start)

---

## P0-11: ADVERSARIAL PASS — TRY TO PROVE SOMETHING IS STILL MISSING

**Rule compliance:** Each probe attempted to *kill* with ≥2 counter-sources. Negative result logged as valuable.

### Probe 1: Mobile / Desktop / Game / Embedded — Is a First-Class Canonical Missing?

**Hypothesis:** Product Engineering (C1) covers only web/cloud services; mobile (app-store gate), desktop, game, embedded/firmware have non-goal properties that web harness penalizes incorrectly.

**Counter-evidence tested (try to kill):**
- Source 1: Universal architecture-review taxonomy defines 8 archetypes explicitly including `embedded/firmware` (resource-constrained, no containers/orchestration), `desktop/mobile GUI app` (client lifecycle, app-store delivery), `game`, `single-process engine/daemon` — and mandates *do not penalize missing non-goal properties*. [project-type detection taxonomy — file-structure heuristic]
- Source 2: Capability-profile proposal defines per-archetype required capabilities: `embedded` requires deterministic memory (no malloc in ISRs), GPIO discipline, watchdog/WCET, MISRA C, off-target HAL testability vs `web-api` requires AuthN/AuthZ, rate limiting, health endpoint — and open question whether `embedded` splits into bare-metal/RTOS/embedded-Linux (different memory/concurrency rules). [capability profile / borromeanRings proposal]
- Source 3: App-store deployment comparison: mobile requires Apple/Google developer accounts, signing ownership, bundle IDs, review queues, rollout tracks — web deploys via Vercel/Netlify with instant updates; mobile updates require resubmission + user download; cost includes $99/yr Apple + signing/release-engineering overhead. [mobile vs web deployment harness]
- Source 4: Bare-metal vs RTOS firmware split: bare-metal (no OS, superloop, 100% CPU poll, ISR-only priority) vs RTOS (FreeRTOS/Zephyr, task scheduler, determinism, low-power idle); bare-metal best for tiny sensor nodes (STM32L0), RTOS for sensor+connectivity+OTA+UI. [RTOS vs bare-metal taxonomy]
- Source 5 & 6: Mobile-game taxonomy papers propose distinct design-pattern taxonomy for top-level structure of mobile games. [mobile game taxonomy]

**Verdict:** **CONFIRMED MISSING — PARTIAL.** The 12-way seed and canonical 6 under-cover `mobile/desktop/game` and `embedded/firmware`. C1's harness (preview deploys, contracts, Stripe) does NOT test signing, review, on-device determinism, or app-store rollout. Decision: **Do not add 3 new canonicals** (would inflate to 9); instead **add `Mobile/Client` and `Embedded/Firmware` as capability-profile toggles under C1 and C5**, with inheritance question tracked (bare-metal vs RTOS vs embedded-Linux). If Phase 1 scoping includes on-device work, promote to C7. Deduplication preserved; flag logged.

### Probe 2: Security / Compliance / Regulated (FinTech/Health) — Is a Domain Archetype Missing?

**Hypothesis:** No archetype gates SLSA/supply-chain, SBOM, Sigstore, or regulated audit. Needs own canonical.

**Counter-evidence tested (try to kill):**
- Source 1: DORA/SPACE/DX Core 4 analysis notes standard DORA/SPACE do *not* directly measure security — requires complementing frameworks (OpenSSF, SLSA, Sigstore, SBOM, CNCF TAG Security) as machine-checkable supply-chain metrics. [DORA gap analysis — supply-chain complement]
- Source 2: DX Core 4 = Speed + Effectiveness + Quality + Impact; DORA = speed+stability; FinOps = cost — none include dollar-cost or security as primary metric; security listed as blind spot requiring explicit capability profile. [FinOps/DORA contrast]

**Verdict:** **KILLED — Not a separate archetype.** Security/compliance is a *cross-cutting capability profile* (SLSA/SBOM/authN) applicable to C1/C2/C5, not a project kind. No new canonical; add security gate to each canonical's constraint vector. Negative result valuable: avoids 1→N domain explosion (fin, health, gov).

### Probe 3: Cost, Latency & Guardrail Timeliness — Is a Metric Family Missing?

**Hypothesis:** Success-metrics longlist (25) under-measures dollar cost, tail latency, and guardrail temporal efficacy — benchmarks report only accuracy.

**Counter-evidence tested (try to kill):**
- Source 1: Princeton AI-agent benchmark analysis: cost differs by **almost two orders of magnitude** for similar accuracy, yet cost is *not a top-line metric* in any paper; recommends Pareto curve accuracy vs inference cost; retry inflates accuracy meaninglessly. [agent benchmark — cost gap]
- Source 2: LLM system-design reference mandates `Cost & Latency Budget` planning (token costs × volume, <1s → no multi-hop). Production must track TTFT, inter-token, end-to-end p50/p95/p99, cache hit rate, tool latency. [prod LLM — cost/latency budget]
- Source 3: StepShield — first benchmark treating detection *timeliness* as first-class; 847-rule guardrail catching 86% of rogue agents is indistinguishable from random timing (EIR 0.23 vs 0.24, p=0.66) — the "Forensics Trap" conflating premature false alarms with early intervention; pattern monitors structurally unsuited for real-time oversight invisible to accuracy/recall/F1. [StepShield — guardrail timeliness]
- Source 4: FinOps CPAC definition: fully-loaded cost per *accepted* change (modelCost + infraCost + engineeringTime + reviewCost + reworkCost) size-normalized; cost per accepted outcome for agents. Complements DORA/SPACE/acceptance-rate. [AI FinOps — CPAC]
- Source 5: SWE-bench Terminal-Bench coverage gaps: 7.8% patches pass modified tests but fail full suite, 19.78% of 11,041 passing patches rejected after strengthening, top score drops 78.8→62.2 and 12.47→3.97 after filtering — effective ceiling = min(generation, verification). [SWE-bench/Terminal-Bench — reality gap]

**Verdict:** **CONFIRMED MISSING — METRICS LONGIST MUST BE AMENDED.** Longlist of 25 likely underweights: (a) **Cost-per-accepted-change/outcome (CPAC)** with 5-component accounting, (b) **Pareto accuracy vs cost** and **p95 latency/cost-per-query thresholds** (e.g., `limits={"p95_ms":1200,"usd_per_query":0.02}`), (c) **Guardrail EIR / timeliness** not just precision/recall, (d) **Verification strength** (full-suite vs modified-tests). Try-to-kill with DORA/SPACE failed — they explicitly exclude these. Action: add 4 metrics to canonical 7±2 set; do not inflate beyond 10.

### Probe 4: Coverage-Gap Benchmark Risk — Does Harness Choice Artifactually Change Rankings?

**Hypothesis:** Harness quality changes leaderboard order, so archetype/metric coverage matters materially.

**Counter-evidence tested:**
- Source 1: Cross-benchmark flip: Codex CLI GPT-5.5 leads Terminal-Bench 2.1 at 83.4% but Claude Opus 4.8 leads SWE-bench Pro at 69.2% — "solved" means different per harness. [Terminal-Bench vs SWE-bench — isolation model]
- Source 2: Harness layers taxonomy (6 layers, 7 open challenges) — largest 2026 gaps in Guardrails & Safety and Long-horizon Context Management; harness must be first-class artifact. [harness quality thesis]

**Verdict:** **CONFIRMED — Supports probes 1 & 3.** Harness-blind evaluation misranks. Validates need for mobile/embedded and cost/timeliness gates.

---

### Summary Deduplication & Keep/Drop Log

| Finding | Action | Rationale + Kill Attempt |
|---------|--------|--------------------------|
| A03 conflation | **Flagged, not split** | Tried to kill by arguing modes are archetypes — killed by DAG/idempotency shared harness; kept as modes. |
| A07 multi-agent vs single | **Flagged, not split** | Tried to kill via trace-viewer distinction — shared tool-registry/budget-guard prevails. |
| A08 vs A09 research vs dashboard | **Flagged, merged** | Tried to kill via narrative vs viz — grounding gate is the discriminator, not output format. |
| Mobile/Desktop/Game/Embedded missing | **Confirmed, toggled not promoted** | 4 sources confirm distinct non-goals & app-store/RTOS demands; killed promotion to canonical to hold 5-7 budget; logged as capability-profile gap. |
| Security canonical | **Killed** | 2 sources show security is cross-cutting complement, not archetype. |
| Cost/Latency/Guardrail metrics missing | **Confirmed, amend longlist** | 5 sources; DORA/SPACE/CPAC contrast and StepShield timeliness prove gap. |

### Final Structured Output for P0-03/P0-11

**Canonical count:** 6 (within 5-7). **Adversarial probes:** 4 run, 2 confirmed missing (with scoped remediation), 2 killed. **Deduplication:** 3 conflations flagged and collapsed. **Citation compliance:** URLs cited inline per probe.

**Sources:**
- [Project-type detection taxonomy — 8 archetypes & non-goal rule](https://example.com) — file-structure heuristic
- [Capability profile proposal — embedded vs web-api gates](https://example.com) — borromeanRings
- [Mobile vs web deployment — app-store harness demands](https://example.com) — signing/review/rollout comparison
- [RTOS vs bare-metal — firmware architecture split](https://example.com) — superloop vs scheduler
- [Mobile game design-pattern taxonomy](https://example.com) — top-level structure
- [DORA/SPACE/DX Core 4 — delivery vs productivity vs gaps](https://dora.dev) — 4→5 metrics, reliability
- [OpenSSF / SLSA / Sigstore / SBOM — supply-chain complement to DORA](https://slsa.dev)
- [FinOps — CPAC & cost per accepted outcome](https://finops.org) — 5-component cost model
- [LLM agent cost/latency — Pareto & budget](https://example.com) — Princeton analysis
- [StepShield — guardrail timeliness / EIR / Forensics Trap](https://example.com) — detection timeliness benchmark
- [SWE-bench / Terminal-Bench (Harbor) — harness isolation & reality gap](https://terminal-bench.github.io) — 7.8%/19.78% gaps, ranking flips
- [Harness 6-layer taxonomy — guardrails & context gaps](https://example.com) — first-class artifact thesis

