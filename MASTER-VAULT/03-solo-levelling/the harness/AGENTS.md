# AGENT REGISTRY — AI Development Harness

> Every agent deployed in this project is tracked here. Updated on every deploy.
> Last updated: 2026-08-31 22:10 IST

## Completed: `wf_c917d118-556` — Phase 0 (ALL 4 DONE) → `373afb9` (6 canonicals, 10 SCs)

| # | Agent ID | Codename | Role | Status | Searches | Output | Chars |
|---|----------|----------|------|--------|----------|--------|-------|
| 1 | `a77aeece63a72a98a` | **R-A (P0)** | Broad Mapper | **DONE** | 16 | [`phase-0/R-A_BROAD_MAPPER.md`](phase-0/R-A_BROAD_MAPPER.md) | 48,954 |
| 2 | `a26632a58467a86d6` | **R-B (P0)** | Challenger | **DONE** | 7 | [`phase-0/R-B_CHALLENGER.md`](phase-0/R-B_CHALLENGER.md) | 21,247 |
| 3 | `aa34f5f9d862f74ea` | **V-C (P0)** | Adversarial | **DONE** | 7 | [`phase-0/V-C_ADVERSARIAL.md`](phase-0/V-C_ADVERSARIAL.md) | 18,668 |
| 4 | `a80a8a51a79d1877a` | **V-D (P0)** | Architectural | **DONE** | — | [`phase-0/V-D_ARCHITECTURAL.md`](phase-0/V-D_ARCHITECTURAL.md) | 14,683 |

Synthesized → [`phase-0/ARCHETYPES_AND_CRITERIA.md`](phase-0/ARCHETYPES_AND_CRITERIA.md) (22K).

## Completed: `wf_4230df94-293` — Phase 1 Batch 1: Execution & Agency (ALL 4 DONE) → `71a01fc` (11 Caps)

| # | Agent ID | Codename | Role | Status | Searches | Output | Chars |
|---|----------|----------|------|--------|----------|--------|-------|
| 5 | `a55e89141d173598e` | **R-A (P1-B1)** | Broad Mapper | **DONE** | 12 | [`phase-1/batch-1/R-A_BROAD_MAPPER.md`](phase-1/batch-1/R-A_BROAD_MAPPER.md) | 67,342 |
| 6 | `a7e97bdac521c3688` | **R-B (P1-B1)** | Challenger | **DONE** | — | [`phase-1/batch-1/R-B_CHALLENGER.md`](phase-1/batch-1/R-B_CHALLENGER.md) | 34,010 |
| 7 | `a517e52114c13720e` | **V-C (P1-B1)** | Adversarial (P1-06) | **DONE** | — | [`phase-1/batch-1/V-C_ADVERSARIAL.md`](phase-1/batch-1/V-C_ADVERSARIAL.md) | 24,740 |
| 8 | `af85124acc57f52e2` | **V-D (P1-B1)** | Architectural (P1-07) | **DONE** | — | [`phase-1/batch-1/V-D_ARCHITECTURAL.md`](phase-1/batch-1/V-D_ARCHITECTURAL.md) | 22,465 |

Converged → [`phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md`](phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md) (31K) — 61 tool uses, 321K tokens.

## Completed: `wf_4434e6aa-c46` — Phase 1 Batch 2: Context, Memory & Knowledge (ALL 4 DONE) → `45eef68` (10 Caps)

| # | Agent ID | Codename | Role | Status | Searches | Output | Chars |
|---|----------|----------|------|--------|----------|--------|-------|
| 9 | `abf6916052dd74a87` | **R-A (P1-B2)** | Broad Mapper | **DONE** | 17 | [`phase-1/batch-2/R-A_BROAD_MAPPER.md`](phase-1/batch-2/R-A_BROAD_MAPPER.md) | 74,534 |
| 10 | `a61d8b65fc83bf4d9` | **R-B (P1-B2)** | Challenger | **DONE** | 13 | [`phase-1/batch-2/R-B_CHALLENGER.md`](phase-1/batch-2/R-B_CHALLENGER.md) | 43,785 |
| 11 | `ab69c9ad43c52d649` | **V-C (P1-B2)** | Adversarial (P1-14) | **DONE** | — | [`phase-1/batch-2/V-C_ADVERSARIAL.md`](phase-1/batch-2/V-C_ADVERSARIAL.md) | 25,013 |
| 12 | `aa9b5d20f32f1cb4f` | **V-D (P1-B2)** | Architectural (P1-15) | **DONE** | — | [`phase-1/batch-2/V-D_ARCHITECTURAL.md`](phase-1/batch-2/V-D_ARCHITECTURAL.md) | 28,010 |

Converged → [`phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md`](phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md) (37K) — 56 tool uses, 337K tokens.

## Active: `wf_0122c038-89e` — Phase 1 Batch 3: Integration & Extensibility (2 RUNNING)

| # | Agent ID | Codename | Role | Status | Searches | Output |
|---|----------|----------|------|--------|----------|--------|
| 13 | `a6254c53f50cb898a` | **R-A (P1-B3)** | Broad Mapper (P1-17,19,21) | **RUNNING** | — | — pending |
| 14 | `a8bba49fe6a476953` | **R-B (P1-B3)** | Challenger (P1-18,20) | **RUNNING** | — | — pending |
| 15 | `pending` | V-C (P1-B3) | Adversarial (P1-22) | **QUEUED** (barrier) | — | — |
| 16 | `pending` | V-D (P1-B3) | Architectural (P1-23) | **QUEUED** (barrier) | — | — |

Dir: `.claude/.../workflows/wf_0122c038-89e/`

## Retired: `wf_19071a3d-703` (KILLED — sequential bug)

| Agent ID | Role | Reason |
|----------|------|--------|
| `ae04cf163e43a6f3b` | R-A attempt | Sequential `await agent()` not `pipeline()` — killed via `TaskStop w8qvg25ko`. |

## Planned Deployments (per `plan.md §8`)

| Phase | Batch | Tasks | Dispatch Shape |
|-------|-------|-------|----------------|
| P1 Batch 4 | Safety/Governance | P1-25..32 | R-A+R-B → V-C+V-D |
| P1 Batch 5 | DX/Observability/Meta | P1-33..43 | R-A+R-B → V-C+V-D |
| P1 cross-batch | Dedupe + level hygiene | P1-41..42 | V-C+V-D barrier |
| P2 | Ranking (5 groups A–E) | P2-04..17 | R-A+R-B per group → V-C+V-D |
| P3 | Tool selection (per element) | P3-03..30 | R-A + R-B + V-C per element |
| P3.5 | Empirical validation | P3.5-02..11 | R-A/R-B + V-C/V-D shadow |
| P4 | Documentation (6 batches) | P4-02..14 | R-A/V-C + R-B/V-D batched |

## WSL Dispatch

- **WSL:** Ubuntu 26.04 LTS, WSL2, `/mnt/c/Users/Shashank Karamudi/Desktop/solo-levelling/the harness` · **opencode:** `1.18.18` · **agy:** `1.1.21`

## Rules

- No solo agent on a two-lens brief — parallel divergence mandatory. No phase without V-C+V-D+senior gate. Every output mirrored to `.md` same turn.

---

## CURRENT STATE (supersedes above stale rows)

> **Updated 2026-09-01.** The phase rows above stopped at Phase 1 Batch 3 mid-flight. Full tally below.

### Phase 1 (research/discovery) — ALL 5 BATCHES COMPLETE via agy
- **B1** Execution (`wf_4230df94-293`, 4 agents) → `71a01fc`
- **B2** Context (`wf_4434e6aa-c46`, 4 agents) → `45eef68`
- **B3** Integration (agy, R-A/R-B/V-C/V-D) → `2de263e`+`025dff2`
- **B4** Safety (agy) → `9cbc74b`
- **B5** DX/Meta (agy) → `892fc75`
- **Synthesis** (D-1 merger + D-2 auditor, agy) → `f23d6c3` (MASTER_TAXONOMY, 48 elements)

### Phase 2 (ranking) — 10-agent fleet (agy)
- 5 group rankers + arbiter + tension verifier → `d488f4f` (21S/12A/4B)

### Phase 3 (tool selection) — 26-agent fleet (agy)
- 8 tool batches T-A..T-H + 2 verifiers + overlap sweep + slice build → `5f55267` (TOOL_SELECTION_INDEX)

### Phase 3.5 (validation) — V1-V4 + materialization
- V1-V4 internal validation + 3 materializer agents → `fe45860` (VALIDATION_REPORT)
- `.harness/` now operational (15+ capabilities)

### Phase 4 (documentation) — 6 doc batches
- D-1..D-6 + interaction map → `a2e5098`

### VALIDATION FLEET — 28 agents (this cycle)
- **26 validators** (V-TX-1..8, V-TO-1..8, V-OB-1..6, V-KB-1..4) + **2 synthesizers** (V-SYN-1/2)
- Outputs: `validation/*.md` (evidence-backed verdicts)
- → `6b24866` (verdicts) + `5b9cefe` (audit + remaining gaps)
- Fix pass → `45e694b` (guard/Cedar/sandbox/YAML/presets hardened)

### Grand total: 4 (P0) + 20 (P1) + 10 (P2) + 26 (P3) + 8 (P3.5) + 6 (P4) + 28 (validation) = **102+ agent deployments**, all mirrored to `.md`.
