# VERIFIER D — Architectural Verifier Report | Phase 0 Anchor
**Date: 2026-08-31 | Tasks: P0-09, P0-10 | Inputs: R-A (full), R-B (NOT RECEIVED in bundle)**

**Files reviewed:**
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\R-A Phase 0 Longlists.md` (truncated at archetype 02 detail, 12-archetype overview present, P0-07 25-metric table NOT in payload)
- `R-B Phase 0 Longlists` — **MISSING from orchestrator payload** — verification limited to R-A + inferred completeness gap

## 1. Verification Verdict

| Deliverable | Verdict | Rationale |
|---|---|---|
| **P0-01 Archetype Longlist (12)** | **CONDITIONAL PASS** | R-A correctly de-anchored: 12-way split is not seed-copy. Splits are justified: 03 unfolds ETL/ELT/Streaming/Reverse-ETL, 04 vs 05 separates glue vs stateful RPA, 06 vs 07 isolates MLOps vs Agentic, 08 vs 09 separates discourse vs artifact. Search angles A1-A7 documented with query families. **GAP:** `Research Method` table lists angles but no source URLs/citations rendered in truncated payload; no explicit exclusions/merge rationale log. Archetypes 10-12 conflate internal DX; need stricter boundary vs 02. |
| **P0-07 Metrics Longlist (25)** | **FAIL - INCOMPLETE EVIDENCE** | Payload contains no 25-metric table to audit. Cannot verify measurability, instrument coverage, or archetype variance. R-B absent — cannot cross-check convergence/divergence. Blocks unconstrained sign-off on P0-09 unless P0-09 re-derives with proper measurability. |
| **P0-09 / P0-10 Readiness** | **PROCEED WITH CORRECTED P0-09 BELOW** | Proceeding to define FINAL 10 criteria that repair the vagueness risk ("better DX") and enforce definition+instrument+threshold+archetype per rule. |

**Spawned fix (not blocking):** P0-07 longlist must be re-emitted with 25 rows each containing instrument+unit before Phase 1. Do not average-away variance in Phase 2.

---

## 2. P0-09 — FINAL 10 Harness Success Criteria (MEASURABLE)

All thresholds are SLOs over N=50 consecutive runs on pinned harness version + model unless noted. Tag: `Level` = harness | project | run ; `Type` = Leading (predicts) | Lagging (outcome).

### SC-01: Time-to-First-Usable-Artifact (TTFUA)
- **Definition:** Wall-clock from `harness run` to first preview/deployable artifact that passes smoke (HTTP 200 or `build ok` or DAG `dry-run ok`).
- **Why:** Greenfield/agentic value is 0→1 speed; slow scaffold = abandoned task. DORA-adjacent lead time proxy.
- **How to observe / Instrument:** Harness OTel span `run.start -> artifact.smoke_pass` from JSONL trace; CI preview URL probe. Instrument: `harness trace.jsonl + /health` poller.
- **Threshold/Target:** P50 <90s (01 Greenfield, 10 Tooling), <150s (02 Backend, 04 Glue), <180s (06 MLOps, 07 Agent), N/A strict for 08 Research (first draft <600s). P95 <2x P50.
- **Archetypes:** Critical 01,02,10 ; High 04,07 ; Low 08,09 (narrative tolerance). **Level: run** (agg to project) | **Leading**

### SC-02: End-to-End Task Success Rate (TSR)
- **Definition:** % runs where human-adjudicated acceptance criteria pass + automated benchmark suite passes.
- **Why:** Ultimate lagging outcome; replaces vague "capability".
- **How / Instrument:** Per-archetype gold set (SWE-bench Verified slice, Terminal-Bench, Browser-RPA replay suite, custom 5-task per archetype harness). Harness grader `verdict.json` + human spot-check (n=10).
- **Threshold:** >=75% for 01,02,04,10 ; >=65% for 03,11,12 (infra/data strict) ; >=60% for 05,06,07 (non-determinism higher). Overall harness weighted mean reported WITH per-archetype breakdown — do not average.
- **Archetypes:** ALL — but gold sets differ. **Level: run -> harness** | **Lagging**

### SC-03: Mean Time to Recovery After Step Failure (MTTR-Step)
- **Definition:** Mean seconds to auto-recover (retry, re-plan, alternative tool) after a tool call fails (non-zero exit, 4xx/5xx, selector miss) without human input, capped at task timeout.
- **Why:** Distinguishes brittle scripts from harness-grade resilience; predicts prod incident MTTR.
- **How / Instrument:** Trace parser: `tool.error -> tool.success` or `planner.replan` span difference; failure injected via `fault-inject` flag (kill 10% of tool calls).
- **Threshold:** P50 MTTR <45s when recovery possible; auto-recovery attempted in >=80% of recoverable failures; no infinite retry (max 3 / step).
- **Archetypes:** Critical 05 (selector), 03/11 (idempotent retry), 07 (tool loop) ; Moderate 02,06. **Level: run** | **Leading** (predicts SC-02)

### SC-04: Human Intervention Rate (HIR) — Autonomy
- **Definition:** Interventions / run: explicit human `approve/resume/edit` events required to reach success.
- **Why:** Measures harness autonomy vs babysitting; cost & interrupt budget.
- **How / Instrument:** Count `human.input` events in trace; survey chip `was_blocked`. Instrument: harness event bus.
- **Threshold:** Median 0 for 01,02,04,09,10 ; <=1 for 03,05,06,11,12 ; <=2 for 07,08 (research review gate is expected). Intervention-free success rate >= SC-02 minus 10pp.
- **Archetypes:** Variance preserved: 08 Research *expects* 1 review gate — not penalized. **Level: run** | **Leading**

### SC-05: Cost per Successful Run (CPSR)
- **Definition:** (Tokens * price + container minutes * price + external API $) / successful runs. Report also p50 tokens/success.
- **Why:** Prevents capability at any cost; gates model/harness choice.
- **How / Instrument:** Token counter from provider + `cost-ledger.jsonl` (harness must emit). Instrument: `litellm cost` or harness ledger.
- **Threshold:** Greenfield/Backend/Tooling < $0.80 / success ; Browser RPA < $1.50 (proxy/compute) ; MLOps train excluded (inference sub-task < $0.60) ; Agent system < $1.20. Budget guard must fire <5% overruns.
- **Archetypes:** All; strictest 01,02 (commodity). **Level: run -> project** | **Leading** (predicts sustainability)

### SC-06: Determinism & Reproducibility Rate (DRR)
- **Definition:** % of identical inputs (same prompt+seed+repo snapshot) that yield byte-identical *or* semantically equivalent artifact on re-run (n=3) — graded by diff + test pass, not LLM judge.
- **Why:** Flaky harness = untrustworthy CI.
- **How / Instrument:** 3x replay harness `replay --seed 0,1,2` ; `diff --ignore` + test suite pass; embedding similarity >=0.98 for non-deterministic prose.
- **Threshold:** >=90% for 11,12,03,10 (IaC/data/tooling) ; >=80% for 01,02 ; >=60% for 07,08 (agent/research) with trace determinism (tool order) logged.
- **Archetypes:** Critical 11,03,12 ; relaxed 07,08 with justification. **Level: harness** | **Leading**

### SC-07: Security & Secret-Handling Conformance (SSHC)
- **Definition:** Incident rate: (a) secrets leaked to log/artifact/telemetry, (b) unsandboxed FS/network egress, (c) injection execution (prompt injection payload runs tool). Zero-tolerance.
- **Why:** Harm-if-absent = catastrophic; primary regulator.
- **How / Instrument:** Static scan `gitleaks --no-git` on artifacts+traces, egress audit (`allowlist` violations), injection red-team suite (10 payloads from `indirect-prompt-injection` bench). Instrument: `harness audit` + `gitleaks` + network proxy log.
- **Threshold:** 0 leaks / 100 runs ; 0 unsandboxed writes outside `workdir` ; >=90% injection blocked (tool not executed). Any leak = harness FAIL regardless of other SCs.
- **Archetypes:** ALL ; elevated 02,04,05,11 (secrets, browser creds, IaC policy). **Level: harness + run** | **Lagging** (but leading for trust)

### SC-08: Artifact Health Gate Pass Rate (AHG)
- **Definition:** % runs where artifact passes archetype-specific static gate without human fix: `typecheck + lint + unit tests + (archetype gate: e.g., `terraform validate`, `dbt test`, `playwright --dry`)`.
- **Why:** Replaces "better DX" with checkable quality.
- **How / Instrument:** CI gate `gate.sh` per archetype; harness must run gate before declaring success.
- **Threshold:** >=85% for 01,02,10 ; >=80% for 03,11 (dbt/TF) ; >=70% for 05 (flaky selectors allowed 1 retry). Gate P50 runtime <30s.
- **Archetypes:** All except 08 (use citation gate instead). **Level: run -> project** | **Lagging**

### SC-09: Context & State Persistence Under Compaction (CSP)
- **Definition:** Success retention across context compaction / rolling window: % runs >30k tokens where key intents (project goal, constraints, prior decisions) survive compaction without regression.
- **Why:** Long-horizon archetypes die at 100k tokens without explicit memory.
- **How / Instrument:** Long-task probe (add 40k tokens of synthetic context) + `memory-probe` QA: 5 questions on prior decisions; harness must emit `compaction` event and `memory_snapshot.json`.
- **Threshold:** >=85% QA accuracy post-compaction for 07,08,12 ; >=75% for 03,06,09 ; no silent goal drift (goal embedding cosine >0.90).
- **Archetypes:** Critical 07,08,12 (agent/research/migration) ; Moderate others. **Level: run (long)** | **Leading**

### SC-10: Idempotency & Drift-Free Re-run (IDFR)
- **Definition:** Second `apply/run` with same inputs produces no-op / no drift: `terraform plan` empty, `dbt run` 0 rows changed (when source frozen), ETL checksum stable, migration codemod idempotent.
- **Why:** Infra/Data/Migration harness must be declarative; non-idempotent = prod incidents.
- **How / Instrument:** Double-run harness: `run; run --again` and diff `plan.json`/`manifest.json`/`checksum`. Instrument: `drift-detector.sh`.
- **Threshold:** 100% no-op on second run for 11,03,12 when inputs frozen ; <5% false drift due to timestamps. Chrome/Browser excluded (stateful target).
- **Archetypes:** Critical 11,03,12 ; N/A for 01,08 (expected additive). **Level: project** | **Lagging** (maintenance predictor)

**Variance rule:** Publish SCs as 12-column heatmap (archetypes x SC). Global single number is for rank only; decision uses archetype-weighted view. Do not report SC-02/SC-05/SC-08 as single mean.

---

## 3. P0-10 — Rubric Dimension Wiring to SCs (Phase 2 Traceability)

**Phase 2 ranking process:** Each candidate harness feature/capability is scored 1-5 on 7 rubric dims. The 7-dim vector predicts regression on SCs if the feature were omitted (harm-if-absent) or added (benefit). Trace is deterministic via weight matrix below — not ad-hoc.

### 3.1 Wiring Matrix (weights: 0 none, 1 weak, 2 primary)

| Rubric Dim (1-5) | Primary SCs it predicts (regression if omitted/low) | Secondary | Mechanism |
|---|---|---|---|
| **Frequency** (how often needed) | SC-01 TTFUA (2), SC-04 HIR (2), SC-05 CPSR (2) | SC-02 (1) | High-frequency omissions inflate every-run tax; low-frequency features допуст threshold relaxation |
| **Harm-if-absent** | SC-07 SSHC (2), SC-03 MTTR (2), SC-08 AHG (2), SC-06 DRR (2) | SC-10 (1), SC-09 (1) | Harm 4-5 forces gate: any feature with harm>=4 that mitigates SC-07/SC-03/SC-08 must not be ranked below median; if omitted, those SCs are expected to breach thresholds first |
| **Benefit (if present)** | SC-02 TSR (2), SC-08 AHG (2), SC-01 (1) | SC-05 (1) | Benefit 5 = delta on lagging SC-02/SC-08 measurable in A/B (≥+10pp TSR) |
| **Complexity** (authoring/LLM cost) | SC-05 CPSR (2), SC-06 DRR (1) | SC-03 (1) | Complexity 4-5 predicts SC-05 overrun and SC-06 flake; requires complexity budget and SC-05 guard |
| **Maintenance** (drift/breakage) | SC-10 IDFR (2), SC-09 CSP (2), SC-06 (1) | SC-03 (1) | Maintenance 4-5 maps directly to future SC-10 drift failures and SC-09 compaction rot |
| **Security** | SC-07 SSHC (2) | SC-08 (1) | Security 4-5 is veto class: harm-if-absent already captures, but security dim isolates secret-handling; SC-07 threshold is non-negotiable |
| **Generality** (archetype coverage) | Variance preservation rule (2) | SC-02 (1) | Generality 5 = feature applies ≥8 archetypes (score via SC-02 per-archetype heatmap uniformity). Low generality (1-2) is NOT penalty if archetype-specific — must not be averaged away; route to project-level SC instead of harness-level |

### 3.2 How High "Harm if Absent" (4-5) Maps to Regressing Criteria

Decision rule for Phase 2:

- **Harm 5 (catastrophic if absent):** Expected regression **SC-07 (security leak) OR SC-03/SC-08 block** within 10 runs. Examples: no secret redaction → SC-07 immediate FAIL; no retry/compensation → SC-03 MTTR → cascades to SC-02 <50%; no static gate → SC-08 <40%. Such items are P0 gates regardless of Frequency.
- **Harm 4 (major):** Expected regression **SC-06 (flakiness), SC-09 (long-run amnesia), or SC-10 (drift)**. Examples: no compaction memory → SC-09 QA <50% on 07/08/12; no idempotency guard → SC-10 drift on 11/03. These rank above pure Benefit items.
- **Harm ≤2:** No lagging SC expected to breach; lag is confined to SC-01/SC-05 (speed/cost) — rank by Benefit/Cost tradeoff, not by risk.

**Trace artifact for Phase 2:** For each ranked candidate, emit `wiring.json`:
```json
{"candidate":"selector-resilience proxy","rubric":{"frequency":5,"harm":5,"benefit":4,"complexity":3,"maintenance":3,"security":3,"generality":2},"predicted_regression":["SC-03","SC-02:05","SC-07"],"observed_SC_delta":"+12pp TSR on 05 after A/B"}
```

### 3.3 Leading vs Lagging & Level Tags (for dashboard)

- **Leading (early signal, run/harness):** SC-01, SC-03, SC-04, SC-05, SC-06, SC-09 — use to *predict* SC-02/SC-07/SC-08 before full benchmark. Wire: Frequency/Complexity/Maintenance dims drive these.
- **Lagging (outcome, run/project/harness):** SC-02, SC-07, SC-08, SC-10 — final acceptance; Benefit/Harm dims drive these.
- **Harness-level:** SC-06, SC-07 (global invariant). **Project-level:** SC-10, SC-09 long, SC-08 per archetype. **Run-level:** SC-01 through SC-05, SC-08.

### 3.4 Anti-Averaging Rule (preserve archetype variance)

Phase 2 ranking MUST consume per-archetype SC deltas, not harness mean. Computation: `score = sum(dim * w_dim) ` where `w_dim` is calibrated on archetype-specific SC threshold slack (e.g., Browser RPA SC-03 weight 2x vs Greenfield). Report `p10 archetype` SC, not mean, as bottleneck.

---

## 4. Sources (representative, not exhaustive)

DORA lead-time/MTTR [DORA 2023]; SPACE/DX Core4 [Forsgren et al., Zimmermann]; SWE-bench Verified + Terminal-Bench grading [OpenAI/PRISM]; DEVIN evaluation harness [Cognition]; Playwright/Puppeteer RPA resilience patterns; 6R/7R migration [AWS/Gartner]; Modern Data Stack Bronze-Silver-Gold [Databricks]; Agent harness cost/ determinism benchmarks [Anthropic Claude Code, SWE-bench harness cost ledger].

**Open gaps to close before Phase 1:** Re-emit P0-07 with 25 rows each having unit+instrument+threshold; attach source URLs for A1-A7; provide R-B bundle for cross-verification; publish per-archetype gate scripts (`gate.sh` variants) to make SC-08/SC-10 runnable.
