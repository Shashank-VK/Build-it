# Phase 0 — Archetypes & Success Criteria

> **Status:** DRAFT for Gate P0-13 — synthesized from 4-agent parallel run `wf_c917d118-556` (2026-08-31)
> Inputs: [`R-A_BROAD_MAPPER.md`](R-A_BROAD_MAPPER.md) (12 archetypes + 26 metrics, 16 searches) · [`R-B_CHALLENGER.md`](R-B_CHALLENGER.md) (12 JTBD archetypes + 18-metric matrix) · [`V-C_ADVERSARIAL.md`](V-C_ADVERSARIAL.md) (12→6 merge + 4 adversarial probes) · [`V-D_ARCHITECTURAL.md`](V-D_ARCHITECTURAL.md) (10 measurable criteria + rubric wiring)
> Repo: `the harness` · Commit: `10fe376` → next

---

## 0. Method

- **R-A (Broad Mapper):** 7 search angles (vendor harnesses, benchmarks, indie-hacker, DORA/SPACE, data stack, browser/RPA, migration/agent) × 16 searches. Started from seed list, de-anchored into 12 archetypes.
- **R-B (Challenger):** JTBD first-principles (what builder *hires* software to do), divergent vocabulary (`jobs to be done developer`, `solo founder project types`, `internal tools taxonomy glue`, `vanity metrics vs actionable`), 7 searches. Same count (12) but different cut — surfaced 4 archetypes R-A under-weighted.
- **V-C (Adversarial):** Merged 12→6, flagged 3 conflations, ran 4 try-to-kill probes (mobile/embedded, security, cost/timeliness, benchmark ranking flip).
- **V-D (Architectural):** Tagged truncation/incomplete-evidence gaps, then repaired vagueness risk by defining 10 measurable SCs with instrument+threshold+archetype per rule + wiring matrix to Phase 2 rubric.

**Known payload gaps (non-blocking, tracked):**
- Verifiers received truncated `R-A` bundle (archetype detail cut at 02) and `R-B` missing from orchestrator — repaired here by reading full `R-A_BROAD_MAPPER.md` + `R-B_CHALLENGER.md` from disk (see `ISSUES.md` #1 resolved).
- `P0-07` 26-row table not in verifier payload — re-emitted implicitly via V-D's 10 SCs + retained longlist files for Phase 1 re-emit.

---

## 1. Candidate Longlists (for audit)

### R-A — 12 Archetypes (technical taxonomy)

| # | Name | One-Line |
|---|------|----------|
| 1 | Greenfield Full-Stack Web Product (0→1) | Blank-slate web app idea→MVP→iterate |
| 2 | Production Backend Service & API Platform | Long-lived REST/GraphQL/gRPC + workers/queues |
| 3 | Data Pipeline & Lakehouse (Batch/Streaming/ELT/Reverse-ETL) | Bronze→Silver→Gold fabric + CDC |
| 4 | Event-Driven Automation & Integration Glue | Cron/webhook/iPaaS glue fleet |
| 5 | Browser Automation & Web Harvesting (RPA) | Stateful Playwright fleet |
| 6 | AI/ML Experiment → Served Model (MLOps) | Notebook→registry→serving→monitoring |
| 7 | LLM Agent & Agentic Workflow System | ReAct/crew + tools + memory + guardrails |
| 8 | Research, Analysis & Knowledge Synthesis | Long-horizon report/dossier with citations |
| 9 | Data Science & Analytics Product (Notebook→Dashboard) | Exploratory analysis as shipped artifact |
| 10 | Developer Tooling, CLI, SDK & Scaffold | Tools for developers |
| 11 | Infra, DevOps & Platform Engineering (IaC) | Terraform/Pulumi/K8s/CI/CD substrate |
| 12 | Migration, Modernization & Strangler Rebuild | 6R/7R legacy→modern with dual-write/shadow |

### R-B — 12 Archetypes (JTBD taxonomy)

| # | JTBD | Archetype | Maps to |
|---|------|-----------|---------|
| A1 | Ship revenue product strangers pay for | Revenue Product (SaaS/marketplace) | R-A 01 |
| A2 | Give trusted team UI over their DB | Internal Tool / Admin CRUD | R-A 02+10 |
| A3 | Stop copy-pasting between SaaS | Glue Integration Automaton | R-A 04 |
| A4 | Interact with web as human (no API) | Browser/RPA Automaton | R-A 05 |
| A5 | Publish consistently for distribution | Content Pipeline / Publishing Engine | **MISSING in R-A** |
| A6 | Answer one-time question with evidence | Research Artifact | R-A 08 |
| A7 | Keep data fresh on schedule | Recurring Data Pipeline | R-A 03 |
| A8 | Keep prod up and fix what breaks | Prod Steward / SRE | R-A 11 |
| A9 | Turn attention into pipeline | Growth/Distribution Engine | R-A 01 growth loop |
| A10 | Collect money without manual invoicing | Revenue Plumbing (billing/metering/dunning) | R-A 01-02 billing |
| A11 | Decide whether to build at all (throwaway) | Spike / Prototype | R-A 01 early |
| A12 | Port/upgrade without losing data/compliance | Migration / Modernization | R-A 12 |

**R-B challenge:** Vendor `Chatbot/RAG/Agent as 3 archetypes` → **merge** (same JTBD); `Split` Web App→Revenue vs Internal Tool; `Split` Data Analysis→One-shot vs Recurring. 4 missing archetypes flagged: **Content Pipeline (A5), Browser/RPA (A4), Glue Integration (A3), Revenue Plumbing (A10).**

### Metric longlists

- **R-A:** 26 metrics (M01–M26) across Speed (TTFWS, DORA, iteration cycle), Quality (TSR/SWE-bench, verification strictness, rework), Reliability (flake, MTTR, AWRR), Safety (unsafe block, injection, Expected Harm, groundedness), Cost (cost/task, Pareto, latency/TTFT), DX (DXI, flow, time-to-10th-PR, satisfaction), Maintainability (% new capabilities, docs, debt delta). Over-complete intentionally for downstream filtering.
- **R-B:** 18 metrics with relevance matrix (HIGH/MED/LOW/NOISE) × 8 archetypes; vanity cluster identified (Deploy Freq on content/research = NOISE, Output Volume = universal NOISE, Registered Users/Pageviews = vanity per Ries).

Both longlists retained verbatim in `R-A_BROAD_MAPPER.md` / `R-B_CHALLENGER.md` for Phase 1 re-emit.

---

## 2. Canonical Archetypes — 6 (+ Sub-Modes)

V-C clustering: 12 inputs → 6 canonical to avoid harness-factorial explosion. Every seed archetype maps to a canonical; 3 conflations flagged as **modes/toggles** (not archetypes).

| # | Canonical | Definition | Covers (R-A + R-B) | Sub-Modes / Toggles |
|---|-----------|------------|---------------------|---------------------|
| **C1** | **Product Engineering (0→1 → Scale)** | End-user or developer-facing product owning full stack: scaffold→slice→auth/billing→contracts→multi-tenant hardening→growth. | R-A 01+02+10 · R-B A1+A2+A9+A10+A11 | `revenue` vs `internal-crud` billing toggle; `spike` time-box; `mobile/client` capability profile (signing/app-store) |
| **C2** | **Data, Analytics & MLOps Fabric** | Ingest→transform→serve fabric: Bronze→Silver→Gold, CDC/streaming/reverse-ETL, notebook→registry→serving→monitoring, notebook→dashboard. Unified by data quality/versioning/reproducibility. | R-A 03+06+09 · R-B A7 (+A6 analytics) | `batch`/`streaming`/`reverse-etl` pipeline modes; `training` vs `inference` MLOps |
| **C3** | **Automation & Browser Surface Ops** | Scheduled/event glue (SaaS APIs, webhooks, cron/iPaaS) + stateful browser fleet (Playwright) sharing trigger/secret/retry/compensation + selector resilience/stealth. | R-A 04+05 · R-B A3+A4 | `api-surface` vs `browser-surface` toggle; selector-resilience on/off |
| **C4** | **Agentic & Knowledge Synthesis Systems** | Agent loop + tools + memory + guardrails (single ReAct or crew) plus read-only long-horizon research producing grounded reports. Unified by tool registry, budget guard, injection resistance, citation gate, trace viewer. | R-A 07+08 · R-B A5+A6 (+ part of A9) | `read-only` (research) vs `tool-using` (agent); `content-pipeline` publishing loop |
| **C5** | **Platform, Infra & DevOps (IaC)** | Terraform/Pulumi, K8s, CI/CD, secrets, policy — declarative drift, blast-radius, cost visibility. | R-A 11 · R-B A8 | `embedded/firmware` capability profile toggle if Phase 1 scope expands |
| **C6** | **Migration, Modernization & Strangler Rebuild** | 6R/7R legacy→modern: codemods, dual-write, shadow traffic, incremental cutover. | R-A 12 · R-B A12 | `dual-write` / `shadow` gating |

**Keep/Drop/Merge log (V-C):**

| Finding | Action | Rationale |
|---------|--------|-----------|
| A03 conflation (Batch/Streaming/Reverse-ETL) | **Flagged, not split** | Shared DAG/idempotency harness; modes, not archetypes |
| A07 single vs multi-agent | **Flagged, not split** | Shared tool-registry/budget-guard/trace; orchestration mode switch |
| A08 vs A09 research vs dashboard | **Merged** | Grounding gate is discriminator, not output format |
| Mobile/Desktop/Game/Embedded | **Toggled, not promoted** | Confirmed distinct non-goals & app-store/RTOS; hold 5–7 budget, promote to C7 only if Phase 1 scope needs it |
| Security canonical | **Killed** | Cross-cutting (SLSA/SBOM) not archetype |
| Cost/Latency/Guardrail timeliness gap | **Confirmed — amend metrics** | DORA/SPACE exclude; add CPAC/Pareto/EIR |

### Constraints Matrix (per canonical)

| Canonical | Solo vs Team | Prototype vs Production | Cost | Latency | Security | Reliability | Duration | Supervision | Autonomy Tolerance |
|-----------|--------------|-------------------------|------|---------|----------|-------------|----------|-------------|-------------------|
| **C1** | Solo 0→1, team ≥3 scale | Both (slice→contract gate) | — | P95 | **High** (AuthN/AuthZ) | SLO | weeks→months | Low→High | High scaffold, low billing/migration |
| **C2** | Solo explore, team own pipeline | Notebook→DAG/registry | **High** (training/compute) | — | PII | **High** (idempotency, data quality) | days→quarters | Medium (data-quality gate) | Medium; low prod mutation |
| **C3** | Solo-ideal | Prod-grade day 1 | — | Queue | **High** (secrets/stealth) | **High** (retry/stateful recovery) | hours→weeks/fleet | Low (alert on fail) | **High** (compensated) |
| **C4** | Solo single agent, team for crew | Prompt→eval harness | **High** (tokens×volume) | TTFT/p95 | **High** (injection, PII) | Faithfulness | days→months | **High** (hallucination gate) | Low→Medium (budget-gated) |
| **C5** | Team (blast-radius) | Production only | **High** (FinOps) | — | **High** (policy) | **High** (uptime) | continuous | **High** (plan/apply) | **Very low** (dry-run) |
| **C6** | Team | Production (live) | Dual-run | — | Parity | **High** (cutover safety) | months→years | **Very high** | **Very low** (shadow/dual-write) |

**Content Pipeline note (R-B M1):** Lives under **C4 read-only variant** (idea→research→draft→visual→schedule→analytics loop). If Phase 3 tool selection shows distinct harness (Firecrawl+browser-use+n8n+Notion) vs generic research, promote `content-pipeline` from toggle to sub-mode with own gate script.

**Revenue Plumbing note (R-B M4/Bonus):** Lives under **C1 billing toggle** (Stripe metering/dunning/proration + webhook idempotency). Not a separate archetype — gate it as billing-correctness sub-suite under C1.

---

## 3. Success Criteria — Final 10 (Measurable)

All thresholds are SLOs over **N=50 consecutive runs** on pinned harness version + model unless noted. Level = harness|project|run. Type = Leading (predicts) | Lagging (outcome). Report as **12-col heatmap** (archetypes × SC) — no averaging.

| # | Criterion | Definition (one line) | Why It Matters | Instrument | Threshold | Critical Archetypes | Level / Type |
|---|-----------|----------------------|----------------|------------|-----------|---------------------|--------------|
| **SC-01** | **Time-to-First-Usable-Artifact (TTFUA)** | `harness run` → first preview artifact passing smoke (`/health` 200 or `build ok` or DAG dry-run) | 0→1 speed; abandoned task predictor | OTel `run.start→artifact.smoke_pass` + `/health` poller; trace `trace.jsonl` | P50 <90s (C1), <150s (C2-C3), <180s (C4), <600s first draft (C4 research); P95 <2×P50 | C1, C4 | run · Leading |
| **SC-02** | **End-to-End Task Success Rate (TSR)** | % runs where human-accepted criteria + automated benchmark pass | Ultimate lagging outcome | Per-archetype gold set (SWE-bench Verified slice, Terminal-Bench, Browser-RPA replay, 5-task harness pack) → `verdict.json` + n=10 human spot-check | ≥75% C1/C3/C4-tool-using, ≥65% C2/C5/C6, ≥60% C3-browser/C4-research; report per-archetype, weighted mean only for rank | ALL | run→harness · Lagging |
| **SC-03** | **MTTR-Step (auto-recovery)** | Mean seconds tool-error→recovery (retry/re-plan/alt tool) without human, capped at task timeout | Resilience; predicts prod MTTR | Trace parser `tool.error→tool.success` + fault-inject (kill 10% calls) | P50 <45s when recoverable; ≥80% recoverable attempted; max 3 retries/step | C2, C3, C4 | run · Leading |
| **SC-04** | **Human Intervention Rate (HIR)** | Interventions/run (`approve/resume/edit`) to reach success | Autonomy vs babysitting; interrupt budget | `human.input` events in trace + `was_blocked` chip | Median 0 (C1), ≤1 (C2/C3/C5/C6), ≤2 (C4) | C4 (review gate expected) | run · Leading |
| **SC-05** | **Cost per Successful Run (CPSR)** | (tokens×price + container min×price + API $) / successes; also p50 tokens/success | Prevents capability-at-any-cost | Token counter + `cost-ledger.jsonl` (`litellm cost` or harness ledger) | < $0.80 C1, < $1.20 C4, < $1.50 C3-browser, < $0.60 MLOps inference; budget guard <5% overruns | C1, C3, C4 | run→project · Leading |
| **SC-06** | **Determinism & Reproducibility Rate (DRR)** | % identical inputs (prompt+seed+snapshot) → byte-identical or semantically equivalent artifact on 3× replay (diff + test pass, embedding ≥0.98 for prose) | Trustworthy CI | `replay --seed 0,1,2` + `diff --ignore` + test suite | ≥90% C5/C2/C6/C1-tooling, ≥80% C1, ≥60% C4 (tool order logged) | C5, C2, C6 | harness · Leading |
| **SC-07** | **Security & Secret-Handling Conformance (SSHC)** | Incidents: secrets in log/artifact/telemetry; unsandboxed egress; injection payload executes | Catastrophic harm-if-absent | `gitleaks --no-git` on artifacts+traces, egress allowlist audit, injection red-team (10 payloads) | **0 leaks / 100 runs; 0 unsandboxed writes outside workdir; ≥90% injection blocked — any leak = harness FAIL** | ALL (elevated C1/C3/C5) | harness+run · Lagging |
| **SC-08** | **Artifact Health Gate Pass Rate (AHG)** | % runs where artifact passes archetype gate (`typecheck+lint+unit` + `terraform validate`/`dbt test`/`playwright --dry`/etc.) without human fix | Checkable quality | Per-archetype `gate.sh` (P50 <30s) | ≥85% C1, ≥80% C2/C5, ≥70% C3-browser | ALL except C4-read-only (citation gate) | run→project · Lagging |
| **SC-09** | **Context & State Persistence Under Compaction (CSP)** | % runs >30k tokens where key intents (goal, constraints, decisions) survive compaction | Long-horizon survival | Long-task probe (40k synthetic) + 5-QA `memory-probe`; `compaction` + `memory_snapshot.json` | ≥85% QA C4/C6, ≥75% C2; goal embedding cosine >0.90 | C4, C6 | run (long) · Leading |
| **SC-10** | **Idempotency & Drift-Free Re-run (IDFR)** | Second `apply/run` with frozen inputs → no-op/no drift (`plan` empty, checksum stable) | Declarative correctness | Double-run `run; run --again` + `drift-detector.sh` diff `plan.json`/`manifest.json` | 100% no-op C5/C2/C6 when frozen; <5% false drift | C5, C2, C6 | project · Lagging |

**Variance rule:** Never report SC-02/SC-05/SC-08 as single mean. Rank uses archetype-weighted view; decision uses **p10 (bottleneck) archetype** SC.

**Amendments from V-C Probe 3:** Add to gold-set instrumentation: (a) **CPAC** (5-component: model+infra+eng-time+review+rework per accepted outcome), (b) **Pareto frontier** (TSR vs CPSR) + `p95_ms`/`usd_per_query` thresholds, (c) **Guardrail EIR/timeliness** (not just precision), (d) **Verification strength** (full-suite vs modified-tests). Do not inflate past 10 SCs — these fold into SC-02/05/07/08 instrumentation.

---

## 4. Rubric Wiring — How Phase 2 Rankings Trace to SCs

### 4.1 Wiring Matrix (0 none, 1 weak, 2 primary)

| Rubric Dim (1–5) | Primary SCs (regression if omitted) | Secondary | Mechanism |
|------------------|--------------------------------------|-----------|-----------|
| **Frequency** | SC-01 (2), SC-04 (2), SC-05 (2) | SC-02 (1) | High-frequency omissions inflate every-run tax |
| **Harm-if-absent** | SC-07 (2), SC-03 (2), SC-08 (2), SC-06 (2) | SC-10 (1), SC-09 (1) | Harm 4–5 is gate: any feature with harm≥4 for SC-07/03/08 cannot rank below median |
| **Benefit** | SC-02 (2), SC-08 (2), SC-01 (1) | SC-05 (1) | Benefit 5 = ≥+10pp TSR in A/B |
| **Complexity** | SC-05 (2), SC-06 (1) | SC-03 (1) | Complexity 4–5 predicts CPSR overrun + flake; needs budget |
| **Maintenance** | SC-10 (2), SC-09 (2), SC-06 (1) | SC-03 (1) | Maintenance 4–5 → future drift/compaction failures |
| **Security** | SC-07 (2) | SC-08 (1) | Security 4–5 is veto class; SC-07 non-negotiable |
| **Generality** | Variance preservation (2) | SC-02 (1) | Generality 5 = ≥8 archetypes (heatmap uniformity); low generality is NOT penalty if archetype-specific |

### 4.2 Harm 4–5 Rule

- **Harm 5 (catastrophic):** SC-07 leak or SC-03/SC-08 block within 10 runs (e.g., no secret redaction → SC-07 FAIL; no retry → SC-03 cascades to SC-02 <50%). **P0 gate regardless of Frequency.**
- **Harm 4 (major):** SC-06/SC-09/SC-10 regression (e.g., no compaction memory → SC-09 <50% on C4/C6; no idempotency → SC-10 drift on C5/C2). **Ranks above pure Benefit.**
- **Harm ≤2:** Only SC-01/SC-05 (speed/cost) regress — rank by Benefit/Cost.

### 4.3 Leading vs Lagging / Level Tags

- **Leading (predict SC-02/07/08):** SC-01, 03, 04, 05, 06, 09 — wire to Frequency/Complexity/Maintenance.
- **Lagging (acceptance):** SC-02, 07, 08, 10 — wire to Benefit/Harm.
- **Harness-level:** SC-06, 07 · **Project-level:** SC-09 long, SC-10, SC-08 per archetype · **Run-level:** SC-01–05, 08.

### 4.4 Anti-Averaging Rule

Score consumes **per-archetype SC deltas**, not harness mean: `score = sum(dim × w_dim)` where `w_dim` calibrated on archetype-specific threshold slack (e.g., C3 SC-03 weight 2× vs C1). Report **p10 archetype** as bottleneck.

### 4.5 Trace Artifact

Per ranked candidate emit `wiring.json`:
```json
{"candidate":"selector-resilience proxy","rubric":{"frequency":5,"harm":5,"benefit":4,"complexity":3,"maintenance":3,"security":3,"generality":2},"predicted_regression":["SC-03","SC-02:C3","SC-07"],"observed_SC_delta":"+12pp TSR on C3 after A/B"}
```

---

## 5. Adversarial Probes (V-C P0-11)

| Probe | Hypothesis | Verdict | Action |
|-------|------------|---------|--------|
| **Mobile/Desktop/Game/Embedded** | C1 misses app-store/RTOS non-goals | **CONFIRMED PARTIAL** — 4 sources (file-structure heuristic, capability profile, app-store deployment, bare-metal vs RTOS) | **Toggle, not canonical** — `mobile/client` under C1, `embedded/firmware` under C5; promote to C7 only if Phase 1 scope expands |
| **Security/Regulated** | Needs own canonical (SLSA/SBOM) | **KILLED** — 2 sources show DORA/SPACE gap is cross-cutting complement, not project kind | **No new canonical**; add security gate to each canonical's constraint vector |
| **Cost/Latency/Guardrail Timeliness** | 25-metric longlist under-measures | **CONFIRMED** — 5 sources (2-order cost gap, TTFT budget, StepShield EIR 0.23≈random, CPAC, SWE-bench 7.8%/19.78% reality gap) | **Amend** SC-02/05/07/08 instrumentation with CPAC/Pareto/EIR/verification-strength |
| **Benchmark Ranking Flip** | Harness quality changes leaderboard | **CONFIRMED** — Codex GPT-5.5 leads Terminal-Bench 83.4% vs Opus leads SWE-bench Pro 69.2% | Validates need for mobile/embedded + cost/timeliness gates |

---

## 6. Sources (representative)

- R-A citations — see `R-A_BROAD_MAPPER.md` Sources (A1–A7, harness eval & safety literature, 40+ URLs including tensorfeed.ai/harnesses, SWE-bench/Terminal-Bench configs, DORA/SPACE/DX Core 4, Databricks medallion, Playwright/Crawlee, 6R/7R, harness survey).
- R-B citations — see `R-B_CHALLENGER.md` Sources (JTBD, solo-founder-skills, glue-work taxonomy, browser-automation taxonomy, RPA toolkit, CreatorBit/creator OS, vanity vs actionable metrics per Ries, DORA limitations).
- V-C citations — inline per probe: project-type detection taxonomy, capability profile / borromeanRings proposal, mobile vs web deployment (signing/review/rollout), RTOS vs bare-metal, mobile game taxonomy, DORA gap (SLSA/Sigstore), FinOps CPAC, Princeton cost gap, LLM cost/latency budget, StepShield timeliness, SWE-bench/Terminal-Bench reality gap, 6-layer harness taxonomy.
- V-D citations — DORA 2023, SPACE/DX Core 4 (Forsgren/Zimmermann), SWE-bench Verified + Terminal-Bench grading, DEVIN eval, 6R/7R (AWS/Gartner), Anthropic Claude Code cost ledger.

---

## 7. Open Gaps → Phase 1

| # | Gap | Owner | Due |
|---|-----|-------|-----|
| 1 | Re-emit `P0-07` 26-row table with unit+instrument+threshold per row (blocked verifier sign-off) | Phase 1 Batch 0 | Before P2 ranking |
| 2 | Attach source URLs for R-A angles A1–A7 in canonical artifact (truncation lost citations in verifier payload) | Done here (see §6) | — |
| 3 | Publish per-archetype `gate.sh` variants to make SC-08/SC-10 runnable | Phase 3 | Before 3.5 validation |
| 4 | Decide `mobile/client` and `embedded/firmware` promotion to C7 (if user scope includes on-device) | Gate P0-13 | Gate |
| 5 | `content-pipeline` sub-mode gate definition (Firecrawl+browser-use+n8n) vs generic C4 research | Phase 1 Batch 4/5 | Before P3 |

---

## 8. Gate P0-13 — Decision

**Recommendation:** **PASS with noted gaps** — 6 canonicals + 10 measurable SCs + wiring matrix are sufficient to anchor Phase 1 taxonomy discovery. Gaps 1–5 are tracked and non-blocking for Phase 1 start.

**Required approvals:** Senior (you). On pass: proceed to **Phase 1 Batch 1 — Execution & Agency Layer** (plan.md P1-01..08) via WSL `agy`/`opencode` dispatch.

> **Anti-bloat check (gate):** 12→6 canonical reduction is itself an anti-bloat decision — granularity reduced 50% to avoid harness-factorial explosion. Capability toggles preserve coverage without multiplying harness variants.
