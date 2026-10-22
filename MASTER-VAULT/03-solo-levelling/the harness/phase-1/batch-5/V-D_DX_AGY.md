# ARCHITECTURAL VERIFICATION REPORT (PHASE 1, BATCH 5)
**Domain:** Developer Experience (DX), Observability, Evaluation & Meta-Harness Governance  
**Verifier:** VERIFIER D (Architectural Verifier & Ontology Gatekeeper)  
**Deliverable IDs:** P1-39 & P1-40  
**Scope:** Converged Taxonomical Reconciliation of Researcher A (R-A) & Researcher B (R-B) Submissions

---

## 1. Executive Summary & Canonical Ontological Axioms

Modern autonomous agent harnesses frequently suffer from severe category errors—treating user-interface widgets as foundational capabilities, confusing durable ledger data structures with policy enforcement engines, or conflating telemetry infrastructure with core functional harness requirements. 

This verification report enforces the **Six-Level Canonical Ontology** across all Batch 5 candidates, resolves cross-batch redundancies across Batches 1–4, settles key architectural boundary questions, and presents a converged master schema.

```
       ┌─────────────────────────────────────────────────────────────┐
       │                       6-LEVEL ONTOLOGY                      │
       ├─────────────────────────┬───────────────────────────────────┤
       │ 1. Capability           │ Functional Invariant ("What")     │
       │ 2. Substrate / Runtime  │ Cross-Cutting Host / Execution    │
       │ 3. Mechanism            │ Algorithmic Pattern ("How")       │
       │ 4. Protocol / Standard  │ Wire / Schema Spec (RFC, Contract)│
       │ 5. Resource / Artifact  │ Durable State / Manifest / Ledger │
       │ 6. Tool / Product / CLI │ Executable Binary / UI Artifact   │
       └─────────────────────────┴───────────────────────────────────┘
```

### Core Architectural Resolutions
1. **Observability is a Cross-Cutting Substrate, NOT a Standalone Capability:** Observability is not a single feature that an agent invokes; it is an underlying runtime substrate that provides telemetry sinks, spans, metrics, and trace contexts to every capability across the lifecycle.
2. **Evaluation & Meta-Evaluation are Governance Capabilities:** Offline benchmarking, live regression testing, and synthetic task generation constitute the verification arm of **Autonomous Harness Governance (AHG)**, supported by eval engine runtimes.
3. **Tripartite Reversibility Split (Batch 1 E11 De-duplication):** Rollback cannot be treated monolithically. Reversibility requires three distinct mechanisms: (a) *Filesystem Workspace Snapshots* (Git tree refs), (b) *Context/Memory Window Rollbacks* (trajectory truncation), and (c) *Compensating Tool Inversions* (idempotent rollback hooks).
4. **Cost Ledger vs. Cost Governance (Batch 2 B10 De-duplication):** The *Token/Cost Meter* is an ephemeral Resource/Artifact; *Cost Governance* is an enforcement Capability operating via hard-stop budget mechanisms.
5. **Self-Improvement vs. Auto-Tuning:** *Instinct Mining* extracts few-shot heuristics and rules from episodic memory (Artifact mutation); *Auto-Tuning* optimizes runtime hyperparameters (temperature, top-p, context compression thresholds) via empirical search mechanisms.
6. **Anti-Bloat & Complexity Budgets:** To satisfy SC-01 (TTFUA) and SC-08 (AHG), harnesses must enforce formal *Complexity Budgets* that deprecate, tombstone, and prune stagnant rules, dead tools, and bloated prompt templates.

---

## 2. Cross-Batch De-duplication & Conflation Matrix

To ensure zero architectural overlap with Batches 1 through 4, candidate primitives are cross-referenced and resolved below:

| Batch 5 Candidate Primitives | Prior Batch Overlap | Conflation Type / Risk | Architectural Resolution & De-duplication Rule |
| :--- | :--- | :--- | :--- |
| **Checkpoints & Rewind** | Batch 1 (`E11: Reversibility`) | **Redundancy & Level Error:** Confusing storage snapshot (Resource) with Reversibility (Capability). | Retain Batch 1 `E11` as the master Capability. In Batch 5, classify *Git Tree-Ref Snapshotting* and *Trajectory Truncation* strictly as **Mechanisms** servicing `E11`. |
| **Cost Tracking / Meter** | Batch 2 (`B10: Budget Governance`) | **Conflation:** Confusing accounting data ledger with governance enforcement. | Retain Batch 2 `B10` as the policy gate. Batch 5 introduces the *Cost Ledger Schema* strictly as a **Resource / Artifact** and *Token Cost Metering* as a **Mechanism**. |
| **Hooks DX & Ergonomics** | Batch 3 (`B3-13: Lifecycle Hooks`) | **Redundancy:** Re-defining hook lifecycles. | Batch 3 defines the hook execution runtime. Batch 5 focuses exclusively on developer interfaces: *Hook Testing Utilities* (Tool) and *Declarative Hook Manifests* (Protocol). |
| **Telemetry & Tracing** | Batch 4 (`Flight Recorder / Provenance`) | **Conflation:** Conflating audit persistence with real-time telemetry emission. | Batch 4 governs immutable audit storage and cryptographic provenance. Batch 5 defines the *Observability Substrate* (OTel span generation, micro-HUD statusline projection, streaming sinks). |
| **Headless CI / Batch Engine** | Batch 1 (`E5: Background Execution`) | **Overlap:** Re-implementing async workers. | `E5` governs generic background execution. Batch 5 standardizes the *Headless Non-Interactive CI Runner* as an operational **Framework/Runtime**. |
| **Eval Harnesses** | Batch 1 (`E9: Fanout / Concurrency`) | **Conflation:** Treating parallel eval execution as a new concurrency primitive. | Concurrency leverages Batch 1 `E9`. Batch 5 defines the *Evaluation Capability* and *Benchmark Test Suite Artifacts*. |

---

## 3. Converged Batch 5 Master Table (30 Canonical Primitives)

*Lifecycles:* `build` (configuration, CI, synthesis), `run` (execution, telemetry, live control), `review` (eval, audit, post-mortem, governance).  
*Tiers:* `foundational` (core harness requirement), `important` (production reliability & DX), `specialized` (high-assurance/scale systems), `situational` (domain-specific optimization).

```
========================================================================================================================
                                      CONVERGED BATCH 5 ARCHITECTURAL MASTER TABLE
========================================================================================================================
```

| ID | Canonical Primitive Name | Input Source | Correct Architectural Level | Conflation Flag & Target Resolution | Lifecycle | Tier | SC-Wiring | Formal Behavioral Invariant & Harness Contract |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B5-01** | **Observability Substrate** | R-A (Observability) | **Cross-Cutting Substrate** | Flagged as pseudo-capability; re-tagged as runtime infrastructure. | `run` | `foundational` | SC-06, SC-08 | Emits standardized, structured events and OpenTelemetry-compliant trace contexts for every harness step. |
| **B5-02** | **Structured Execution Spans & Traces** | R-A (Traces/Logs) | **Resource / Artifact** | Conflated with Flight Recorder; resolved as active telemetry model. | `run` / `review` | `foundational` | SC-06, SC-08 | Immutable, acyclic graph of execution spans containing parent ID, token counts, tool I/O, and model activations. |
| **B5-03** | **Micro-HUD & Statusline Projection** | R-A / R-B (Statusline) | **Mechanism** | Conflated with Observability; resolved as human-in-the-loop projection. | `run` | `important` | SC-01, SC-08 | Projects synchronous state deltas (current tool, elapsed time, running token burn) to terminal stderr at $\le 100\text{ms}$ latency. |
| **B5-04** | **Adaptive Output Streaming & Formatting** | R-A (Output Styles) | **Mechanism** | Conflated with UI tool; resolved as stream transformation pipeline. | `run` | `important` | SC-01 | Decouples raw model stream tokens from ANSI/JSON/Markdown terminal sinks via configurable stream multiplexers. |
| **B5-05** | **Workspace State Snapshots** | R-A / R-B (Checkpoints) | **Mechanism** | Redundant with Batch 1 E11; re-tagged as FS-level snapshot mechanism. | `run` | `foundational` | SC-06, SC-08 | Captures atomic filesystem diffs (via Git tree OIDs or CoW snapshots) prior to executing mutating tool calls. |
| **B5-06** | **Trajectory Context Rewind** | R-A / R-B (Rewind/Undo) | **Mechanism** | Redundant with Batch 1 E11; re-tagged as context truncation mechanism. | `run` | `foundational` | SC-05, SC-06 | Truncates agent conversation history and memory buffers back to a designated checkpoint index while maintaining causality. |
| **B5-07** | **Compensating Tool Inversion** | R-B (Undo Split) | **Mechanism** | Conflated with generic undo; resolved as tool-level inverse execution. | `run` | `specialized` | SC-06, SC-08 | Executes registered undo handlers (e.g., `git revert`, DB rollback, container reset) for external side effects. |
| **B5-08** | **Cost Ledger & Token Meter** | R-A / R-B (Cost Ledger) | **Resource / Artifact** | Conflated with Batch 2 B10 Budgeting; resolved as ledger artifact. | `run` | `foundational` | SC-05 | Monotonically increasing append-only register tracking input/output/cached tokens, invocation counts, and USD cost. |
| **B5-09** | **Real-Time Budget Hard-Stop Gate** | R-B (Cost Budget) | **Mechanism** | Redundant with B2-B10; retained as runtime circuit-breaker mechanism. | `run` | `foundational` | SC-05 | Intercepts agent loop prior to model dispatch; terminates execution if cumulative cost $\ge \text{MaxBudgetThreshold}$. |
| **B5-10** | **Headless Non-Interactive CI Runner** | R-A (Headless/CI) | **Framework / Runtime** | Conflated with Batch 1 E5; resolved as non-interactive CLI runner. | `build` / `run` | `foundational` | SC-01, SC-06 | Executes harness workflows in deterministic, unbuffered headless environments emitting standard Unix exit codes. |
| **B5-11** | **Harness-as-Code (HaC) Specification** | R-A / R-B (HaC) | **Protocol / Standard** | Conflated with code config; resolved as formal declarative schema. | `build` | `foundational` | SC-01, SC-08 | Declarative YAML/JSON schema specifying agent roles, tool permissions, system prompts, memory limits, and hooks. |
| **B5-12** | **HaC Migration & Schema Evolution Engine**| R-A (Versioning/Migr.) | **Mechanism** | Conflated with Git versioning; resolved as schema transform engine. | `build` | `important` | SC-06, SC-08 | Automatically validates, lints, and upgrades legacy HaC declarations to newer schema versions via AST transforms. |
| **B5-13** | **Multi-Environment Parity Synchronizer** | R-B (HaC Parity) | **Mechanism** | Conflated with env-vars; resolved as cross-host config reconciler. | `build` | `important` | SC-01, SC-06 | Guarantees identical execution semantics across local developer CLI, remote sandboxes, and headless CI environments. |
| **B5-14** | **Crash Resilience & Auto-Recovery Engine**| R-A (Reliability/Recov.)| **Framework / Runtime** | Conflated with generic try/catch; resolved as lifecycle supervisor. | `run` | `foundational` | SC-06 | Catches fatal harness exceptions, persists in-flight state to disk, and attempts idempotent recovery or safe teardown. |
| **B5-15** | **Agent Stall & Loop Watchdog** | R-A (Deadlock/Stall) | **Mechanism** | Conflated with OS timeout; resolved as behavioral cycle detector. | `run` | `foundational` | SC-05, SC-06 | Detects repeated identical tool invocations, semantic cycling, or zero-progress output, terminating stuck executions. |
| **B5-16** | **Evaluation & Benchmark Capability** | R-A (Eval Harnesses) | **Capability** | Conflated with test runner tool; established as core AHG capability. | `review` | `foundational` | SC-06, SC-08 | The harness invariant allowing offline and online empirical scoring of agent accuracy, safety, and task completion. |
| **B5-17** | **Evaluation Execution Engine** | R-A (Eval Harness) | **Framework / Runtime** | Conflated with evaluation capability; resolved as runner framework. | `review` | `foundational` | SC-06 | Parallel orchestration runtime that feeds task instances to agent containers and collects performance metrics. |
| **B5-18** | **Benchmark Task Suite Manifest** | R-A / R-B (Task Suites)| **Resource / Artifact** | Conflated with dataset files; resolved as formal test schema. | `review` | `foundational` | SC-06 | Version-controlled collection of task prompts, initial repo states, gold patch diffs, and verification test scripts. |
| **B5-19** | **Meta-Evaluation Capability** | R-A (Meta-Eval) | **Capability** | Conflated with standard eval; resolved as grader validation capability. | `review` | `specialized` | SC-06, SC-08 | Capability to evaluate the accuracy, variance, calibration, and bias of automated LLM-as-a-judge evaluators. |
| **B5-20** | **Synthetic Adversarial Task Synthesizer**| R-A (Synthetic Bench) | **Mechanism** | Conflated with prompt engineering; resolved as automated generator. | `build` / `review` | `specialized` | SC-06 | Generates mutated edge-case tasks and security injection scenarios to stress-test harness guardrails and tool safety. |
| **B5-21** | **Autonomous Self-Improvement Capability** | R-A / R-B (Self-Improve)| **Capability** | Conflated with auto-tuning mechanism; established as learning capability. | `review` $\to$ `build` | `specialized` | SC-06, SC-08 | The invariant enabling a harness to autonomously refine its prompts, tool definitions, and routing from historical logs. |
| **B5-22** | **Instinct Mining & Pattern Distillation** | R-A / R-B (Instincts) | **Mechanism** | Conflated with RAG; resolved as offline heuristic distillation. | `review` $\to$ `build` | `specialized` | SC-01, SC-06 | Mines successful trajectories for recurring patterns and crystallizes them into compact system rules and few-shot memories. |
| **B5-23** | **Hyperparameter & Prompt Auto-Tuning** | R-B (Auto-Tuning) | **Mechanism** | Conflated with self-improvement; resolved as parameter search. | `build` | `specialized` | SC-05, SC-06 | Optimizes sampling temperatures, prompt compression ratios, and tool selection thresholds via Bayesian or hill-climbing search. |
| **B5-24** | **Instinct & Rule Memory Bank** | R-A (Learned Rules) | **Resource / Artifact** | Conflated with raw prompt; resolved as structured knowledge store. | `build` / `run` | `important` | SC-01, SC-06 | Durable, queryable repository of learned domain rules, workspace quirks, and anti-patterns indexed for context injection. |
| **B5-25** | **Complexity Budget Enforcement** | R-A / R-B (Anti-Bloat) | **Capability** | Conflated with token budgeting; established as harness size governance. | `build` | `foundational` | SC-01, SC-08 | Invariant enforcing strict upper bounds on total prompt tokens, active tools, registered hooks, and rule counts. |
| **B5-26** | **Dead Code & Stale Rule Pruner** | R-B (Anti-Bloat/YAGNI) | **Mechanism** | Conflated with linter; resolved as dynamic utilization garbage collector.| `build` / `review` | `important` | SC-01, SC-08 | Analyzes telemetry to identify rules, skills, and tools that have zero activation over $N$ runs and marks them for pruning. |
| **B5-27** | **Formal Deprecation Protocol** | R-A / R-B (Deprecation)| **Protocol / Standard** | Conflated with code comments; established as contract transition spec. | `build` | `important` | SC-08 | Standardized schema for marking tools, configs, and APIs as `deprecated`, specifying migration paths and sunset deadlines. |
| **B5-28** | **Hard Sunset & Tombstoning Engine** | R-B (Sunset vs Depr.) | **Mechanism** | Conflated with deprecation; resolved as breaking-change enforcement gate.| `run` | `important` | SC-06, SC-08 | Intercepts calls to past-deadline tombstoned capabilities, returning deterministic failure errors rather than model hallucination. |
| **B5-29** | **Ergonomic CLI Shell & Workspace Host** | R-A (Interactive CLI) | **Tool / Product / CLI**| Conflated with harness runtime; isolated as frontend presentation client.| `run` | `foundational` | SC-01 | Interactive terminal user interface exposing keyboard shortcuts, slash commands, diff previews, and confirmation modals. |
| **B5-30** | **Autonomous Harness Governance (AHG) Gate**| R-A (Governance) | **Capability** | Conflated with rule list; established as top-level harness governor. | `review` | `foundational` | SC-08 | Orchestrates self-improvement, complexity budgeting, deprecation enforcement, and eval verification into an integrated feedback loop. |

---

## 4. Deep-Dive Architectural Deconstructions

```
                               ┌─────────────────────────────────────────────────────────────┐
                               │               AUTONOMOUS HARNESS GOVERNANCE (AHG)           │
                               │                (Continuous Improvement Loop)                │
                               └──────────────────────────────┬──────────────────────────────┘
                                                              │
                                     ┌────────────────────────┴────────────────────────┐
                                     ▼                                                 ▼
        ┌─────────────────────────────────────────────────────────┐       ┌─────────────────────────────────────────┐
        │                 OBSERVABILITY SUBSTRATE                 │       │           EVALUATION SUBSTRATE          │
        ├─────────────────────────────────────────────────────────┤       ├─────────────────────────────────────────┤
        │ • Structured Spans & Traces (Resource)                  │       │ • Benchmark Task Suites (Resource)      │
        │ • Micro-HUD & Statusline (Mechanism)                    │       │ • Eval Execution Engine (Framework)     │
        │ • Token / Cost Ledger (Resource)                        │       │ • Meta-Eval & Calibration (Capability)  │
        └────────────────────────────┬────────────────────────────┘       └────────────────────┬────────────────────┘
                                     │                                                         │
                                     └────────────────────────┬────────────────────────────────┘
                                                              ▼
                               ┌─────────────────────────────────────────────────────────────┐
                               │           SELF-IMPROVEMENT & COMPLEXITY GOVERNANCE          │
                               ├─────────────────────────────────────────────────────────────┤
                               │ • Instinct Mining & Rule Distillation (Mechanism)           │
                               │ • Complexity Budget & Stale Rule Pruning (Mechanism)        │
                               │ • Deprecation Lifecycle & Sunset Tombstoning (Protocol/Mech)│
                               └─────────────────────────────────────────────────────────────┘
```

### 4.1 Substrate vs. Capability: The Observability & Telemetry Decoupling
* **Architectural Flaw in Candidate Submissions:** Treating Observability as a standard capability implies that an agent chooses when to invoke it.
* **Invariant Resolution:** Observability is a **Cross-Cutting Substrate** (`B5-01`). The harness runtime wraps all tool dispatches, LLM completions, context compressions, and hook invocations in OpenTelemetry-compliant trace spans (`B5-02`). 
* **Mechanism Specialization:**
  * *Micro-HUD / Statusline (`B5-03`):* Real-time projection mechanism rendering active tool, token velocity, and elapsed milliseconds to the terminal without mutating standard stdout.
  * *Adaptive Output Streaming (`B5-04`):* Demultiplexing mechanism routing raw text chunks to syntax highlighters, markdown formatters, or structured CI log buffers.

### 4.2 Evaluation, Meta-Evaluation, and Verification Lifecycles
* **Evaluation as a Capability (`B5-16`):** The functional guarantee that the harness can objectively grade agent performance against gold standard diffs or unit test assertions offline.
* **Framework Separation (`B5-17`):** The *Evaluation Engine* is the containerized orchestration runtime (e.g., Docker/gVisor runner executing SWE-bench or HumanEval tasks).
* **Meta-Evaluation (`B5-19`):** A specialized Capability verifying the judge itself. When LLM-as-a-Judge is employed for subjective coding evaluation, Meta-Eval benchmarks judge consistency against human ground truth via Cohen's Kappa ($\kappa \ge 0.85$) and adversarial perturbation testing.

### 4.3 State Reversibility Tripartite Split (Batch 1 E11 Reconciliation)
To eliminate ambiguity with Batch 1's `E11: Reversibility`, rollback is formally split into three orthogonal mechanisms:

```
                               ┌─────────────────────────────────────────────────────────┐
                               │               TRIPARTITE REVERSIBILITY SPLIT            │
                               └────────────────────────────┬────────────────────────────┘
                                                            │
                 ┌──────────────────────────────────────────┼──────────────────────────────────────────┐
                 ▼                                          ▼                                          ▼
  ┌─────────────────────────────┐            ┌─────────────────────────────┐            ┌─────────────────────────────┐
  │      WORKSPACE STORAGE      │            │       AGENT TRAJECTORY      │            │       EXTERNAL STATE        │
  ├─────────────────────────────┤            ├─────────────────────────────┤            ├─────────────────────────────┤
  │ Git Tree Snapshot (B5-05)   │            │ Context Rewind (B5-06)      │            │ Compensating Inversion(B5-07│
  │ Hard reset of modified,     │            │ Truncation of conversation  │            │ Execution of inverse API/   │
  │ created, or deleted files   │            │ messages back to index $k$  │            │ DB compensating calls       │
  └─────────────────────────────┘            └─────────────────────────────┘            └─────────────────────────────┘
```

1. **Workspace State Snapshot (`B5-05`):** Restores dirty filesystem state via lightweight Git tree refs or copy-on-write overlay diffs.
2. **Trajectory Context Rewind (`B5-06`):** Slices in-memory dialogue history to remove failed tool executions and hallucinated branches before retrying.
3. **Compensating Tool Inversion (`B5-07`):** Emits compensating transactions for non-filesystem side effects (e.g., reverting a remote branch push, sending an undo webhook).

### 4.4 Financial Governance: Ledger Artifact vs. Hard-Cap Enforcement
* **Cost Ledger Schema (`B5-08`):** A lightweight, append-only JSON/in-memory data structure tracking exact token breakdowns:
  $$\text{Total Cost} = \sum_{i=1}^{N} \left( T_{\text{prompt}}^{(i)} \cdot C_{\text{in}} + T_{\text{completion}}^{(i)} \cdot C_{\text{out}} + T_{\text{cached}}^{(i)} \cdot C_{\text{cache}} \right)$$
* **Real-Time Budget Hard-Stop (`B5-09`):** A synchronous lifecycle interceptor. If $\text{Total Cost} \ge \text{MaxBudgetThreshold}$, the runtime halts model invocation, saves a checkpoint (`B5-05`), and raises an uncatchable `BudgetExceededException`, protecting against runaway autonomous loops.

### 4.5 Harness-as-Code (HaC), Parity, and Declarative Evolution
* **HaC Specification (`B5-11`):** Fully declarative, version-controlled contract (e.g., `harness.yaml`, `AGY.json`) defining the agent sandbox.
* **Migration Engine (`B5-12`):** Applies automated schema version upgrades (`v1alpha1` $\to$ `v1` $\to$ `v2`) preventing breaking changes across harness releases.
* **Multi-Environment Parity Synchronizer (`B5-13`):** Resolves environment skew by guaranteeing that an agent configuration running in local interactive CLI behaves with bit-for-bit semantic equivalence inside a headless GitHub Actions CI container.

### 4.6 Autonomous Self-Improvement: Instinct Mining vs. Auto-Tuning
* **Instinct Mining (`B5-22`):** Extracts semantic heuristics from successful post-mortem traces. *Example:* If an agent failed 3 times before learning that `npm test` requires `-- --runInBand`, the miner distills: `"Rule: In project repo X, always append --runInBand to npm test"` into the Instinct Memory Bank (`B5-24`).
* **Hyperparameter Auto-Tuning (`B5-23`):** Pure parameter optimization. Runs offline grid or Bayesian searches over temperature, max context window slices, and tool output truncation limits to maximize benchmark pass rates at minimal cost.

### 4.7 Harness Anti-Bloat, Complexity Budgets, and Deprecation Protocols
As autonomous systems evolve, prompt prompts and tool registries grow uncontrollably, degrading agent reasoning (the "context-bloat tax").

```
                                  ┌────────────────────────────────────────────────────────┐
                                  │                COMPLEXITY BUDGET GATE                  │
                                  ├────────────────────────────────────────────────────────┤
                                  │ Total System Prompt Tokens   ≤ 4,000                   │
                                  │ Registered Tools Active      ≤ 20                      │
                                  │ Active Dynamic Instincts     ≤ 30                      │
                                  └───────────────────────────┬────────────────────────────┘
                                                              │ (Breach Trigger)
                                                              ▼
                                  ┌────────────────────────────────────────────────────────┐
                                  │         DEAD CODE & STALE RULE PRUNER (B5-26)          │
                                  ├────────────────────────────────────────────────────────┤
                                  │ Identify zero-activation rules over past 50 runs       │
                                  │ Evict lowest-utility heuristics to cold archive        │
                                  └───────────────────────────┬────────────────────────────┘
                                                              │
                                                              ▼
                                  ┌────────────────────────────────────────────────────────┐
                                  │             FORMAL SUNSET TOMBSTONE (B5-28)            │
                                  ├────────────────────────────────────────────────────────┤
                                  │ Enforce hard error for removed tools / deprecated APIs │
                                  └────────────────────────────────────────────────────────┘
```

* **Complexity Budget Enforcement (`B5-25`):** Imposes hard boundaries:
  $$\sum \text{Prompt Tokens} \le K_{\text{prompt}}, \quad |\text{Active Tools}| \le N_{\text{tools}}, \quad |\text{Active Rules}| \le M_{\text{rules}}$$
* **Dead Code / Stale Rule Pruner (`B5-26`):** Identifies and evicts rules or tools with zero activation or negative reward correlations over $N=50$ trajectories.
* **Deprecation vs. Sunset (`B5-27` vs. `B5-28`):** 
  * *Deprecation (`B5-27`):* Tool outputs non-fatal warning to log/trace indicating end-of-life and migration path.
  * *Sunset Tombstoning (`B5-28`):* Physical removal from schema. Calls to tombstoned tools return immediate deterministic dispatch faults, preventing hallucinated tool arguments.

---

## 5. Success Criteria (SC) Wiring & Traceability

Every Batch 5 primitive directly drives one or more core harness performance metrics:

```
┌──────────────────────────────┬────────────────────────────────────────────────────────┬──────────────────────┐
│ Success Criterion            │ Primary Driving Primitives                              │ Impact Mechanism     │
├──────────────────────────────┼────────────────────────────────────────────────────────┼──────────────────────┤
│ SC-01: Time-To-First-Useful- │ • Micro-HUD Statusline (B5-03)                          │ Eliminates startup   │
│        Action (TTFUA)        │ • Adaptive Output Stream (B5-04)                       │ latency and provides │
│                              │ • Complexity Budget & Anti-Bloat (B5-25, B5-26)        │ instantaneous visual │
│                              │ • Ergonomic CLI Shell (B5-29)                          │ feedback to operator │
├──────────────────────────────┼────────────────────────────────────────────────────────┼──────────────────────┤
│ SC-05: Cost Bounds & Token   │ • Context Rewind (B5-06)                               │ Halts runaway loops, │
│        Efficiency            │ • Cost Ledger & Token Meter (B5-08)                    │ prunes dead context, │
│                              │ • Real-Time Budget Hard-Stop (B5-09)                   │ and enforces hard    │
│                              │ • Loop / Stall Watchdog (B5-15)                        │ financial ceilings   │
├──────────────────────────────┼────────────────────────────────────────────────────────┼──────────────────────┤
│ SC-06: Defect Reduction      │ • Workspace Snapshots (B5-05)                          │ Prevents regression, │
│        Ratio (DRR)           │ • Crash Recovery Engine (B5-14)                        │ ensures atomic undo, │
│                              │ • Evaluation Engine & Suites (B5-16, B5-17, B5-18)     │ and verifies fixes   │
│                              │ • Meta-Evaluation & Calibration (B5-19)                │ before deployment    │
├──────────────────────────────┼────────────────────────────────────────────────────────┼──────────────────────┤
│ SC-08: Autonomous Harness    │ • Observability Substrate & Spans (B5-01, B5-02)       │ Closes the loop from │
│        Governance (AHG)      │ • HaC Spec & Migration (B5-11, B5-12)                  │ runtime telemetry to │
│                              │ • Instinct Mining & Learning (B5-21, B5-22)            │ self-governing rule  │
│                              │ • Deprecation & Sunset Protocols (B5-27, B5-28, B5-30) │ updates & anti-bloat │
└──────────────────────────────┴────────────────────────────────────────────────────────┴──────────────────────┘
```

---

## 6. Authoritative Standards Reference

1. **Telemetry & Tracing:** [OpenTelemetry Specification v1.34+](https://opentelemetry.io/docs/specs/otel/) (W3C TraceContext, Distributed Spans, Baggage Propagation), OpenLLMetry / OpenInference Semantic Conventions for Generative AI.
2. **Evaluation & Benchmarking Standards:** SWE-bench (OpenAI/Princeton), HumanEval (OpenAI), GAIA (General AI Assistants), AgentBench (Tsinghua).
3. **Configuration & Versioning:** JSON Schema Draft 2020-12, OpenAPI 3.1.0 Specification, Semantic Versioning 2.0.0 (SemVer).
4. **Lifecycle & Deprecation:** IETF RFC 8594 (The Sunset HTTP Header Field), IETF RFC 8288 (Web Linking for Deprecation).
5. **Filesystem State Snapshotting:** Git Internals Manual (Plumbing: `write-tree`, `commit-tree`, `read-tree`), Linux OverlayFS / Copy-on-Write (CoW) specifications.

---
**Verification Conclusion:** Batch 5 is fully reconciled, de-duplicated against Batches 1–4, and consolidated into 30 canonical, strictly typed architectural primitives ready for Phase 2 synthesis.
