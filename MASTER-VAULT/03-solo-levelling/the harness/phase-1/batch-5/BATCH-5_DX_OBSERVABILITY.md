# Phase 1 — Batch 5: DX, Observability & Meta — Converged Taxonomy Slice

> **Status:** CONVERGED — P1-33..42 | **Date:** 2026-09-01 | **Dispatch:** WSL `agy` (plan §8.1)
> Inputs: [`R-A_DX_AGY.md`](R-A_DX_AGY.md) (35.8K Broad) · [`R-B_DX_AGY.md`](R-B_DX_AGY.md) (26.2K Challenger) · [`V-C_DX_AGY.md`](V-C_DX_AGY.md) (28.2K Adversarial) · [`V-D_DX_AGY.md`](V-D_DX_AGY.md) (10.2K Architectural)
> Repo: `the harness` | Grounding: `plan.md §2 Batch 5` · `phase-0/ARCHETYPES_AND_CRITERIA.md` SC-01..10 · cross-batch with B1-E11/E5, B2-B10, B3-13, B4 flight-recorder

---

## 0. Method & Coverage

- **R-A (Broad, via agy):** checkpoints/rewind, hooks-as-DX, statusline/agent-status, output styles, usage/cost tracking, headless/CI, self-improving/instinct-mining, harness-as-code/versioning/migration, reliability/recovery, observability (OTel), eval harnesses (SWE-bench/Terminal-Bench), meta-eval, complexity budgets, governance, lifecycle/deprecation — mapped to SC-01/05/06/08.
- **R-B (Challenger, via agy):** checkpoint vs rewind vs git-worktree undo split, cost ledger vs token budget, self-improving vs auto-tuning, harness-as-code vs config-mgmt parity, deprecation vs sunset vs migration, anti-bloat vs YAGNI governance. Divergent vocab (OTel, FinOps, ACID, SRE/DORA, IaC).
- **V-C (Adversarial, via agy):** mapped against OTel, FinOps, POSIX/VFS+Git, ACID, SRE/DORA, IaC, ML Metrology. Stratified into **DX / Telemetry / Meta-Governance** 3 planes.
- **V-D (Architectural, via agy):** 6-level ontology; **30-row converged B5 master table**; systematic conflation fixes (statusline=Mechanism, cost ledger=Artifact, eval engine=Framework, self-improvement=Capability vs auto-tuning=Mechanism, etc.).

---

## 1. Converged Batch 5 Master Table (30 rows, V-D)

| # | Candidate | Level | Lifecycle | Tier | SC Wiring | Conflation Fix |
|---|---|--------|-----------|------|-----------|----------------|
| B5-01 | **Observability Substrate** | Cross-Cutting Substrate | run | Foundational | SC-06, SC-08 | Was pseudo-capability; it's runtime infra emitting OTel traces |
| B5-02 | Structured Execution Spans & Traces | Resource/Artifact | run/review | Foundational | SC-06, SC-08 | Active telemetry model (not Flight Recorder) |
| B5-03 | Micro-HUD & Statusline Projection | Mechanism | run | Important | SC-01, SC-08 | Human-in-the-loop projection ≤100ms |
| B5-04 | Adaptive Output Streaming & Formatting | Mechanism | run | Important | SC-01 | ANSI/JSON/MD multiplexer, not UI tool |
| B5-05 | Workspace State Snapshots | Mechanism | run | Foundational | SC-06, SC-08 | Redundant w/ Batch1 E11 — FS-level snapshots (Git OID/CoW) |
| B5-06 | Trajectory Context Rewind | Mechanism | run | Foundational | SC-05, SC-06 | Redundant w/ E11 — context truncation to checkpoint |
| B5-07 | Compensating Tool Inversion | Mechanism | run | Specialized | SC-06, SC-08 | Tool-level undo handlers (git revert, DB rollback) |
| B5-08 | Cost Ledger & Token Meter | Resource/Artifact | run | Foundational | SC-05 | Append-only token/USD register (not B10 budgeting) |
| B5-09 | Real-Time Budget Hard-Stop Gate | Mechanism | run | Foundational | SC-05 | Circuit-breaker; overlaps B2-B10 retain as enforcement |
| B5-10 | Headless Non-Interactive CI Runner | Framework/Runtime | build/run | Foundational | SC-01, SC-06 | Deterministic unbuffered CLI, exit codes (not E5) |
| B5-11 | **Harness-as-Code (HaC) Specification** | **Protocol/Standard** | build | Foundational | SC-01, SC-08 | Declarative YAML/JSON schema (agents, perms, prompts, hooks) |
| B5-12 | HaC Migration & Schema Evolution Engine | Mechanism | build | Important | SC-06, SC-08 | AST-based schema validator/linter/upgrader |
| B5-13 | Multi-Environment Parity Synchronizer | Mechanism | build | Important | SC-01, SC-06 | Cross-host config reconciler (local/sandbox/CI identical) |
| B5-14 | Crash Resilience & Auto-Recovery Engine | Framework/Runtime | run | Foundational | SC-06 | Lifecycle supervisor: persist, idempotent recover, teardown |
| B5-15 | Agent Stall & Loop Watchdog | Mechanism | run | Foundational | SC-05, SC-06 | Detects cycling/zero-progress, terminates |
| B5-16 | **Evaluation & Benchmark Capability** | **Capability** | review | Foundational | SC-06, SC-08 | Core AHG invariant — offline/online empirical scoring |
| B5-17 | Evaluation Execution Engine | Framework/Runtime | review | Foundational | SC-06 | Parallel orchestration runtime feeding agent containers |
| B5-18 | Benchmark Task Suite Manifest | Resource/Artifact | review | Foundational | SC-06 | Versioned prompts+Gold patches+verification scripts |
| B5-19 | **Meta-Evaluation Capability** | **Capability** | review | Specialized | SC-06, SC-08 | Validates accuracy/variance/calibration/bias of LLM-judges |
| B5-20 | Synthetic Adversarial Task Synthesizer | Mechanism | build/review | Specialized | SC-06 | Mutates edge cases + injection scenarios |
| B5-21 | **Autonomous Self-Improvement Capability** | **Capability** | review→build | Specialized | SC-06, SC-08 | Refines prompts/tools/routing from historical logs |
| B5-22 | Instinct Mining & Pattern Distillation | Mechanism | review→build | Specialized | SC-01, SC-06 | Offline heuristic distillation of successful trajectories |
| B5-23 | Hyperparameter & Prompt Auto-Tuning | Mechanism | build | Specialized | SC-05, SC-06 | Bayesian/hill-climb search (temperatures, ratios) |
| B5-24 | Instinct & Rule Memory Bank | Resource/Artifact | build/run | Important | SC-01, SC-06 | Durable queryable store of learned rules/anti-patterns |
| B5-25 | **Complexity Budget Enforcement** | **Capability** | build | Foundational | SC-01, SC-08 | Upper bounds on tokens/tools/hooks/rules — anti-bloat |
| B5-26 | Dead Code & Stale Rule Pruner | Mechanism | build/review | Important | SC-01, SC-08 | Utilization garbage-collector over N runs |
| B5-27 | Formal Deprecation Protocol | Protocol/Standard | build | Important | SC-08 | `deprecated` schema + migration path + sunset deadline |
| B5-28 | Hard Sunset & Tombstoning Engine | Mechanism | run | Important | SC-06, SC-08 | Deterministic failure for post-deadline capabilities |
| B5-29 | Ergonomic CLI Shell & Workspace Host | Tool/Product/CLI | run | Foundational | SC-01 | Interactive TUI (keyboard, diffs, confirm modals) |
| B5-30 | **Autonomous Harness Governance (AHG) Gate** | **Capability** | review | Foundational | SC-08 | Top-level governor: self-improvement + budgeting + deprecation + eval loop |

---

## 2. V-C Stratification — DX / Telemetry / Meta-Governance

```
DEVELOPER EXPERIENCE (DX)      TELEMETRY & OBSERVABILITY        META & GOVERNANCE
- Headless CI/CD Runner        - GenAI Distributed Tracing       - Declarative Config (IaC)
- Ephemeral Statusline UI      - Token/Cost Metering Ledger      - Budget Quota Governance
- Output Stream Formatting     - Evaluation Harnesses            - Meta-Evaluation Engine
- Transactional State Rewind   - Reliability Fault Recovery      - Automated Policy Tuning
```

Mapped against OTel, FinOps Foundation, POSIX/VFS+Git, ACID, SRE/DORA, IaC, ML Metrology — killed vendor vocab ("instincts", "rewind", "agent status") by grounding in industry standards.

---

## 3. Key V-D Architectural Resolutions

1. **Observability is a Substrate, not a Capability** — emits OTel-compliant events/traces for every step (B5-01); traces are the Artifact (B5-02). Distinct from Batch 4 Flight Recorder (immutable provenance) vs telemetry (active runtime).
2. **State Reversibility Tripartite Split** (reconciles Batch 1 E11): Workspace Snapshots (B5-05, FS-level) + Trajectory Rewind (B5-06, context truncation) + Compensating Inversion (B5-07, tool-level undo). E11 is the Capability; these 3 Mechanisms implement it.
3. **Financial governance decoupled**: Cost Ledger (B5-08) is the Artifact; Budget Hard-Stop Gate (B5-09) is the enforcement Mechanism; B2-B10 is the policy Capability. Three levels, one owner.
4. **Evaluation is a Capability (B5-16), Meta-Eval a distinct Capability (B5-19)** — grader validation is separate from task grading.
5. **Self-Improvement is a Capability (B5-21); Instinct-Mining (B5-22) + Auto-Tuning (B5-23) are Mechanisms** — learning from logs (offline distillation) vs parameter search are different implementations.
6. **Anti-bloat is a Capability (B5-25 Complexity Budget Enforcement)** with Dead-Code Pruner (B5-26) as Mechanism — the harness's own governance loop closes via AHG Gate (B5-30).
7. **Harness-as-Code is a Protocol/Standard (B5-11)** with Evolution Engine (B5-12) + Parity Synchronizer (B5-13) as Mechanisms — the diffable/reversible harness bedrock from `plan.md`.

---

## 4. Kill / Merge / Demote Log

| Action | Count | Details |
|--------|-------|---------|
| **KEEP Capability** | **6** | B5-16 Evaluation, B5-19 Meta-Eval, B5-21 Self-Improvement, B5-25 Complexity Budget, B5-30 AHG Gate (+ B5-11 HaC as Protocol) |
| **Level-fix (substrate/framework/mechanism/artifact)** | 24 | Observability→Substrate; Statusline/Cost Ledger/Rewind/Pruner→Mechanism/Artifact; Eval Engine→Framework; CLI→Tool |
| **Cross-batch redundancy resolved** | 3 | E11 (undo): snapshots+rewind+inversion are its Mechanisms; B10 (budget): ledger+gate implement policy; E5 (background): CI runner distinct |

---

## 5. Sources

R-A/R-B/V-C/V-D disk files (this dir) · OpenTelemetry · FinOps Foundation · POSIX/VFS+Git internals · SRE/DORA (dora.dev) · IaC parity · SWE-bench/Terminal-Bench eval harness doc · ML Metrology (grader calibration).

**Last verified:** 2026-09-01.