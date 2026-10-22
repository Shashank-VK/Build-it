# Phase 2 — Layer 1 (Execution & Agency) Ranking Report: CAP-01..07

> **Document Version:** 1.0.0 | **Workflow:** Phase 2 Ranker  
> **Status:** CONVERGED — Gate P2-02 Candidate | **Date:** 2026-09-01  
> **Grounding:** [`phase-1/MASTER_TAXONOMY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/MASTER_TAXONOMY.md) (Layer 1: CAP-01..07) · [`phase-2/RUBRIC.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/RUBRIC.md) · [`phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md) · [`phase-0/ARCHETYPES_AND_CRITERIA.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-0/ARCHETYPES_AND_CRITERIA.md) (C1–C6, SC-01..10)

---

## 1. Executive Summary & Ranked Taxonomy Table

This ranking systematically evaluates all **7 Canonical Capabilities of Layer 1 (Execution & Agency)** from the Master Taxonomy. Each capability is scored 1–5 across the 7 dimensions defined in [`phase-2/RUBRIC.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/RUBRIC.md):
1. **Frequency** (1 = rarely needed; 5 = every run across all archetypes)
2. **Harm-if-absent** (1 = negligible; 5 = catastrophic failure)
3. **Benefit** (1 = marginal; 5 = ≥+10pp TSR / major safety/cost win)
4. **Complexity cost** (inverse: 1 = config hell/cognitive load; 5 = transparent/negligible)
5. **Maintenance burden** (inverse: 1 = heavy drift/breakage; 5 = auto-maintaining)
6. **Security/risk impact** (1 = introduces real risk/attack surface; 5 = strong risk reduction)
7. **Generality** (1 = single archetype; 5 = all 6 archetypes)

### Master Ranked Table (Sorted by Global Tier & Priority)

| Rank | Canonical ID | Canonical Name | Freq (1-5) | Harm (1-5) | Ben (1-5) | Cplx (1-5) | Maint (1-5) | Sec (1-5) | Gen (1-5) | Global Tier | Per-Archetype Tiers (C1–C6) | Primary SC Wiring |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **1** | **CAP-03** | Dynamic Orchestration & Control Flow | 5 | 5 | 5 | 3 | 4 | 3 | 5 | **S** | C1=S, C2=S, C3=S, C4=S, C5=A, C6=S | SC-02, SC-03, SC-08, SC-10 |
| **2** | **CAP-06** | Isolated Workspace Management | 5 | 5 | 5 | 4 | 4 | 4 | 5 | **S** | C1=S, C2=A, C3=B, C4=A, C5=S, C6=S | SC-06, SC-07, SC-10, SC-08 |
| **3** | **CAP-01** | Delegated Subagent Execution | 4 | 4 | 5 | 3 | 3 | 4 | 5 | **S** | C1=S, C2=S, C3=B, C4=S, C5=A, C6=S | SC-01, SC-04, SC-05, SC-09 |
| **4** | **CAP-04** | Deterministic Workflows & Blueprints | 4 | 4 | 4 | 4 | 4 | 5 | 5 | **S** | C1=A, C2=S, C3=S, C4=B, C5=S, C6=S | SC-06, SC-08, SC-10, SC-05 |
| **5** | **CAP-05** | Background & Async Queued Execution | 4 | 3 | 4 | 3 | 3 | 3 | 4 | **A** | C1=A, C2=S, C3=S, C4=A, C5=A, C6=A | SC-01, SC-03, SC-05 |
| **6** | **CAP-07** | Parallel Execution & Fan-Out | 3 | 2 | 4 | 3 | 3 | 3 | 4 | **A** | C1=A, C2=S, C3=A, C4=S, C5=C, C6=S | SC-01, SC-05, SC-03 |
| **7** | **CAP-02** | Agent Teams & Multi-Agent Coordination | 3 | 2 | 4 | 2 | 2 | 2 | 3 | **B** | C1=A, C2=B, C3=C, C4=S, C5=B, C6=A | SC-02, SC-03, SC-04, SC-05 |

---

## 2. Harm 4–5 Veto Compliance Check

The **Harm 4–5 Veto Rule** mandates that any element with `Harm-if-absent ≥ 4` that mitigates critical failure modes (SC-07 security leaks, SC-03 MTTR step recovery, SC-08 artifact health, or SC-06 determinism) **cannot rank below the median** (must rank $\le 4$ out of 7).

- **CAP-03** (`Harm = 5`): Mitigates cascading failures and unhandled tool exceptions (SC-03, SC-08). **Rank 1 (S-Tier)** $\rightarrow$ **PASS**.
- **CAP-06** (`Harm = 5`): Mitigates unsandboxed writes, branch pollution, and state corruption (SC-07, SC-06, SC-10). **Rank 2 (S-Tier)** $\rightarrow$ **PASS**.
- **CAP-01** (`Harm = 4`): Mitigates context window blowup, attention degradation, and goal drift (SC-09, SC-05). **Rank 3 (S-Tier)** $\rightarrow$ **PASS**.
- **CAP-04** (`Harm = 4`): Mitigates non-deterministic LLM routing drift and pipeline flakiness (SC-06, SC-08, SC-10). **Rank 4 (S-Tier)** $\rightarrow$ **PASS**.

All four high-harm capabilities occupy the top 4 foundational positions.

---

## 3. Detailed Canonical Scorecards & Architectural Rationale

```
================================================================================
SCORECARD 1: CAP-03 Dynamic Orchestration & Control Flow
================================================================================
Element: CAP-03 Dynamic Orchestration & Control Flow
  Frequency: 5 (Every dynamic multi-step agent run requires state tracking, retry loops, and dynamic branching)
  Harm if absent: 5 (Catastrophic: cascading tool failures, infinite retry loops, state loss, unhandled exceptions lead to SC-02 <50% and SC-03 failure)
  Benefit: 5 (Enables resilient end-to-end execution, automatic error recovery, +20pp TSR across all dynamic workflows)
  Complexity: 3 (Requires state machine engine, checkpointing, and dynamic DAG evaluator)
  Maintenance: 4 (Abstracts recovery logic; low per-project maintenance once runtime is established)
  Security: 3 (Controls execution flow; requires strict transition boundaries to prevent unconstrained recursion)
  Generality: 5 (Fundamental across all 6 archetypes)
  → Global tier: S | Per-archetype: C1=S, C2=S, C3=S, C4=S, C5=A, C6=S
  SC wiring: SC-02 (TSR recovery), SC-03 (MTTR-Step auto-recovery <45s), SC-08 (AHG gate retry), SC-10 (IDFR state continuity)
  Evidence: batch-1 E3, LangGraph StateGraph, Agno orchestrator, Windsurf Cascade runtime, Temporal integration
```

### Architectural Rationale & Archetype Profile: CAP-03
- **Problem Solved:** Manages execution state, dynamic graph sequencing, dependency resolution, failure recovery, and non-deterministic decision branching across multi-step agent runs.
- **Why S-Tier:** It is the central nervous system of any autonomous runtime. If absent, any runtime exception or tool error immediately crashes the workflow, violating SC-03 (MTTR-Step) and collapsing SC-02 (TSR).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: S)`: Drives code generation $\rightarrow$ compile error $\rightarrow$ AST replan $\rightarrow$ test fix cycles.
  - `C2 (Data/MLOps: S)`: Dynamically handles schema drift, data validation faults, and DAG sensor triggers.
  - `C3 (Automation/Browser: S)`: Essential for DOM mutation adaptation, selector fallback retries, and CAPTCHA escalation paths.
  - `C4 (Agentic/Knowledge: S)`: Drives the core ReAct loop, query refinement, and iterative hypothesis testing.
  - `C5 (Platform/Infra: A)`: Sequences dependent cloud resources with conditional rollbacks.
  - `C6 (Migration: S)`: Orchestrates multi-phase cutover, dual-write synchronization, and parity discrepancy recovery.

---

```
================================================================================
SCORECARD 2: CAP-06 Isolated Workspace Management
================================================================================
Element: CAP-06 Isolated Workspace Management
  Frequency: 5 (Required across every concurrent task, multi-agent run, or branching code experiment)
  Harm if absent: 5 (Catastrophic: parallel edits clobber uncommitted working tree, branch pollution, race conditions, SC-06 DRR drops <50%)
  Benefit: 5 (Guarantees clean branch isolation, zero workspace collision, effortless dirty-state rollbacks, +15pp TSR in multi-task runs)
  Complexity: 4 (Git worktree primitive is native, fast, and transparent; container overlays add modest setup)
  Maintenance: 4 (Auto-cleaned via lifecycle hooks: worktree remove on completion)
  Security: 4 (Strong filesystem boundary preventing dirty file leaking and uncontrolled workspace pollution)
  Generality: 5 (Universal across all 6 archetypes)
  → Global tier: S | Per-archetype: C1=S, C2=A, C3=B, C4=A, C5=S, C6=S
  SC wiring: SC-06 (DRR determinism ≥90%), SC-07 (SSHC sandbox boundary: 0 writes outside workdir), SC-10 (IDFR drift-free), SC-08 (AHG gate pass)
  Evidence: batch-1 E6 & MEC-01, Claude Code isolation: worktree, Cursor VM/worktree tasks, Copilot task workspaces, gwq, Vibora, AgentsMesh
```

### Architectural Rationale & Archetype Profile: CAP-06
- **Problem Solved:** Provides clean checkout sandboxes (primarily via `git worktree` / `MEC-01` or container overlays) to prevent dirty working directory clobbering, race conditions, and uncommitted drift.
- **Why S-Tier:** A non-negotiable safety and determinism primitive. Without workspace isolation, concurrent agent branches corrupt the developer's working state and invalidate CI test suites (failing SC-07 zero unsandboxed writes and SC-06 determinism).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: S)`: Isolates parallel feature drafts and automated PR generation from live code.
  - `C2 (Data/MLOps: A)`: Provides isolated environments for experimental data transformation scripts.
  - `C3 (Automation/Browser: B)`: Scraper code isolated in checkouts, though browser fleets often rely on browser context sandboxes.
  - `C4 (Agentic/Knowledge: A)`: Bounded scratchpads for generating and checking large document corpuses.
  - `C5 (Platform/Infra: S)`: Non-negotiable for IaC state isolation, preventing accidental production state file locking or mutation.
  - `C6 (Migration: S)`: Mandatory for running side-by-side legacy and modern codebases during strangler migrations.

---

```
================================================================================
SCORECARD 3: CAP-01 Delegated Subagent Execution
================================================================================
Element: CAP-01 Delegated Subagent Execution
  Frequency: 4 (Used in almost all non-trivial tasks across C1, C2, C4, C6; slightly less frequent in one-shot C3/C5 scripts)
  Harm if absent: 4 (Goal drift, context rot, attention dilution in >30k tokens; embedding cosine drops <0.90, leading to severe task failure)
  Benefit: 5 (Subagents keep main agent lean, partition expertise, enable structured task execution, +15pp TSR on multi-step tasks)
  Complexity: 3 (Requires subagent schema definition, parameter passing, and result synthesis)
  Maintenance: 3 (Subagent prompt templates and tool allowlists must be kept in sync as tools evolve)
  Security: 4 (Enables least-privilege scoping: child agents can be given read-only tool allowlists and restricted environments)
  Generality: 5 (Universal pattern applicable across all 6 archetypes)
  → Global tier: S | Per-archetype: C1=S, C2=S, C3=B, C4=S, C5=A, C6=S
  SC wiring: SC-01 (TTFUA rapid draft/scout), SC-04 (HIR scoped autonomy), SC-05 (CPSR anti-context-rot), SC-09 (CSP context survival >30k tokens)
  Evidence: batch-1 E1 & M3, Claude Code subagents (.claude/agents/*.md), Codex custom agents (.codex/agents/*.toml), Copilot agents (.github/agents/*.agent.md), Cursor SDK subagents, Gemini CLI agents
```

### Architectural Rationale & Archetype Profile: CAP-01
- **Problem Solved:** Solves context window saturation, attention degradation ("lost in the middle"), prompt bloat, and tool schema confusion by spawning bounded child agents with dedicated system prompts and tool allowlists.
- **Why S-Tier:** Standard single-context agents degrade severely beyond 30k tokens. Subagent delegation preserves parent context invariants (SC-09), controls total token spend by summarizing outputs (SC-05), and enforces least-privilege tool allowlists (SC-07).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: S)`: Partitions tasks into dedicated frontend, backend, test generation, and review subagents.
  - `C2 (Data/MLOps: S)`: Dispatches subagents for SQL dialect translation, schema validation, and pipeline verification.
  - `C3 (Automation/Browser: B)`: Invoked for specialized DOM analysis or multi-site scraping sub-tasks.
  - `C4 (Agentic/Knowledge: S)`: Foundational pattern for research scouts, fact-checkers, and synthesis subagents.
  - `C5 (Platform/Infra: A)`: Scopes subagents to read-only policy audits vs IaC code authoring.
  - `C6 (Migration: S)`: Decomposes monolithic codebases into isolated file-level migration subagents.

---

```
================================================================================
SCORECARD 4: CAP-04 Deterministic Workflows & Blueprints
================================================================================
Element: CAP-04 Deterministic Workflows & Blueprints
  Frequency: 4 (Standard build, test, lint, deploy, and data pipelines require deterministic blueprints)
  Harm if absent: 4 (High: using non-deterministic LLM loops for standard operations causes flakiness, latency, cost explosion, and drift)
  Benefit: 4 (Zero-drift reproducibility, 10x faster execution on specifiable paths, major token savings)
  Complexity: 4 (Low complexity: straightforward declarative schemas, YAML/JSON DAGs, transparent execution)
  Maintenance: 4 (Highly stable once specified; changes only with pipeline definition)
  Security: 5 (Strong security: strictly deterministic execution paths with no prompt injection surface on fixed edges)
  Generality: 5 (Universally applicable across all 6 archetypes)
  → Global tier: S | Per-archetype: C1=A, C2=S, C3=S, C4=B, C5=S, C6=S
  SC wiring: SC-06 (DRR determinism ≥90%), SC-08 (AHG gate pass rate), SC-10 (IDFR 100% no-op on frozen input), SC-05 (CPSR cost optimization)
  Evidence: batch-1 E4, Windsurf Cascade workflows (.windsurf/workflows/stages/), CrewAI Flows, Temporal workflows, n8n automation, LangGraph StateGraph deterministic subgraphs
```

### Architectural Rationale & Archetype Profile: CAP-04
- **Problem Solved:** Eliminates latency, non-determinism, token waste, and flakiness caused by using LLM reasoning loops for static, specifiable, multi-step operational sequences.
- **Why S-Tier:** Using LLM autonomy for static operations (e.g., compile $\rightarrow$ lint $\rightarrow$ unit test $\rightarrow$ smoke test) is an anti-pattern. Workflows guarantee 100% repeatable execution, eliminate prompt injection vulnerabilities on fixed transition edges, and enforce strict health gates (SC-08, SC-10).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: A)`: Reusable scaffold, build, lint, and preview deployment pipelines.
  - `C2 (Data/MLOps: S)`: Rigid Medallion (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) ETL processing stages and data quality checks.
  - `C3 (Automation/Browser: S)`: Fixed webhook automation, scheduled extraction, and retry policies.
  - `C4 (Agentic/Knowledge: B)`: Fixed citation verification and markdown report assembly stages.
  - `C5 (Platform/Infra: S)`: Strictly enforced `validate → plan → security-audit → apply` infrastructure blueprints.
  - `C6 (Migration: S)`: Multi-stage migration blueprint (AST extract $\rightarrow$ codemod $\rightarrow$ typecheck $\rightarrow$ unit test $\rightarrow$ parity diff).

---

```
================================================================================
SCORECARD 5: CAP-05 Background & Async Queued Execution
================================================================================
Element: CAP-05 Background & Async Queued Execution
  Frequency: 4 (Essential for long-running builds, test suites, crawler jobs, and multi-hour migrations)
  Harm if absent: 3 (Without async execution, interactive sessions block, network timeouts abort long tasks; foreground-only passes short tasks)
  Benefit: 4 (Unblocks user terminal/UI, enables parallel fleet execution, prevents dropped sessions on network disconnect)
  Complexity: 3 (Requires job queue substrate, state persistence, worker polling/SSE notifications)
  Maintenance: 3 (Queue health, orphan task cleanup, dead-letter queue management)
  Security: 3 (Requires authenticated task tokens and sandbox isolation for background workers)
  Generality: 4 (High value for C1, C2, C3, C4, C5; slightly lower for interactive spikes)
  → Global tier: A | Per-archetype: C1=A, C2=S, C3=S, C4=A, C5=A, C6=A
  SC wiring: SC-01 (TTFUA unblocks user immediately via task token), SC-03 (MTTR queued retry without session freeze), SC-05 (CPSR spot/batch compute optimization)
  Evidence: batch-1 E5 & M8, Claude Code background agents (Ctrl+B), Cursor Background Agents (VMs, Cloud Agent API), GitHub Copilot coding agent (Actions infra, gh agent-task), Open-Swarm, NeoSigma
```

### Architectural Rationale & Archetype Profile: CAP-05
- **Problem Solved:** Decouples execution lifecycle from client connection lifetimes, preventing terminal blocking, network timeouts on long operations (>10 min), and dropped tasks during fleet execution.
- **Why A-Tier:** Vital for operational usability, long-running agent autonomy, and scalable compute dispatch. It ranks in A-Tier rather than S-Tier because interactive foreground execution is technically capable of completing shorter tasks without failing correctness criteria.
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: A)`: Unblocks the developer while long test suites and container builds run asynchronously.
  - `C2 (Data/MLOps: S)`: Indispensable for massive dataset transformations, feature store updates, and model training.
  - `C3 (Automation/Browser: S)`: The baseline operating model for continuous cron jobs, event-driven webhooks, and fleet web scrapers.
  - `C4 (Agentic/Knowledge: A)`: Allows long-horizon research dossiers to compile in the background.
  - `C5 (Platform/Infra: A)`: Manages asynchronous cluster creation and multi-region infrastructure provisioning.
  - `C6 (Migration: A)`: Executes multi-hour codebase transformations and shadow traffic recording.

---

```
================================================================================
SCORECARD 6: CAP-07 Parallel Execution & Fan-Out
================================================================================
Element: CAP-07 Parallel Execution & Fan-Out
  Frequency: 3 (Used when tasks can be decomposed into embarrassingly parallel subproblems; not needed for strictly serial workflows)
  Harm if absent: 2 (Tasks can execute serially; primary penalty is wall-clock latency rather than correctness or safety)
  Benefit: 4 (Massive latency reduction: 5-10x speedup on multi-file migrations, parallel test generation, and bulk audits)
  Complexity: 3 (Requires concurrency knobs, rate limiting, error aggregation, and fan-in merge logic)
  Maintenance: 3 (Concurrency race condition handling, API rate limit adaptation)
  Security: 3 (Risk of hitting API rate limits or overwhelming target services; requires bounded concurrency governors)
  Generality: 4 (Applicable across C1, C2, C4, C6; gated/low-concurrency in C5 due to blast-radius)
  → Global tier: A | Per-archetype: C1=A, C2=S, C3=A, C4=S, C5=C, C6=S
  SC wiring: SC-01 (TTFUA wall-clock acceleration P50 <90s), SC-05 (CPSR concurrency vs token budget Pareto frontier), SC-03 (MTTR partial failure aggregation)
  Evidence: batch-1 E9, OpenAI Codex max_concurrent_threads_per_session=6, Cursor up to 8 parallel Background Agents, LangGraph Send fan-out primitive
```

### Architectural Rationale & Archetype Profile: CAP-07
- **Problem Solved:** Eliminates wall-clock latency bottlenecks on embarrassingly parallel, decomposable engineering subproblems.
- **Why A-Tier:** Delivers 5x–10x speedups on large-scale tasks. It ranks in A-Tier because tasks still succeed sequentially in its absence (harm is low), and high fan-out must be carefully governed against API rate limits and token spend (SC-05).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: A)`: Concurrent test suite execution and parallel component scaffolding.
  - `C2 (Data/MLOps: S)`: Parallel shard extraction and concurrent partition transformation.
  - `C3 (Automation/Browser: A)`: Concurrent domain crawling across multi-worker browser pools.
  - `C4 (Agentic/Knowledge: S)`: Concurrent search queries dispatched across multiple search engines and vector stores.
  - `C5 (Platform/Infra: C)`: Explicitly throttled / restricted to low concurrency to prevent resource race conditions and state locks.
  - `C6 (Migration: S)`: Massive speedup when applying codemods across hundreds of disconnected legacy source files.

---

```
================================================================================
SCORECARD 7: CAP-02 Agent Teams & Multi-Agent Coordination
================================================================================
Element: CAP-02 Agent Teams & Multi-Agent Coordination
  Frequency: 3 (High in complex architectural, research, and migration settings; overkill/wasteful for solo/glue/scaffold tasks)
  Harm if absent: 2 (Alternative exists: hub-and-spoke subagents CAP-01 can solve most tasks without peer messaging overhead)
  Benefit: 4 (+10pp TSR on complex collaborative tasks, multi-perspective debate, adversarial code review)
  Complexity: 2 (High coordination overhead, chatty token loops, deadlocks, consensus protocol configuration)
  Maintenance: 2 (Multi-agent conversational graphs drift easily, high prompt coupling between communicating roles)
  Security: 2 (Expanded attack surface: prompt injection can propagate horizontally across peer agents without centralized filtering)
  Generality: 3 (Specialized to collaborative/adversarial use cases; poor fit for deterministic data/infra workflows)
  → Global tier: B | Per-archetype: C1=A, C2=B, C3=C, C4=S, C5=B, C6=A
  SC wiring: SC-02 (TSR +10pp on crew tasks), SC-03 (MTTR peer recovery), SC-04 (HIR consensus reduces escalations), SC-05 (CPSR token loop risk)
  Evidence: batch-1 E2, Claude Agent Teams (messaging), CrewAI Crews & Flows, LangGraph Supervisor+Worker, AutoGen / AG2 Conversational Groups, zeoel 23-agent team
```

### Architectural Rationale & Archetype Profile: CAP-02
- **Problem Solved:** Enables peer-to-peer collaboration, multi-perspective debate, consensus negotiation, and persistent inter-agent messaging that cannot be modeled as simple hierarchical hub-and-spoke subtasks.
- **Why B-Tier:** Highly effective for specialized collaborative scenarios (e.g., adversarial code review or multi-persona debate in C4), but carries high complexity, token inflation, communication graph fragility, and lateral prompt injection risks. Most standard tasks are solved more reliably and cheaply via hierarchical subagents (`CAP-01`).
- **Per-Archetype Breakdown:**
  - `C1 (Product Eng: A)`: Architectural debate (e.g., architect vs frontend specialist vs database engineer).
  - `C2 (Data/MLOps: B)`: Data pipeline designer paired with an independent data auditor.
  - `C3 (Automation/Browser: C)`: Overkill and inefficient for deterministic browser actions and API glue.
  - `C4 (Agentic/Knowledge: S)`: Foundational for adversarial fact-checking, peer review, and multi-perspective research synthesis.
  - `C5 (Platform/Infra: B)`: Infrastructure author paired with a security compliance reviewer.
  - `C6 (Migration: A)`: Legacy domain specialist debating modern framework architects on migration strategy.

---

## 4. Key Layer 1 Architectural Tensions & Trade-offs

1. **CAP-01 (Hub-and-Spoke Subagents) vs CAP-02 (Peer Teams):**
   - Hub-and-spoke subagents enforce strict context boundaries and deterministic summaries, optimizing for token budget (`SC-05`) and predictable completion.
   - Peer teams provide richer debate and autonomous negotiation, but introduce $O(N^2)$ message complexity and potential conversational deadlocks.
2. **CAP-06 (Workspaces) vs CAP-07 (Fan-Out):**
   - High fan-out concurrency (`CAP-07`) without strict filesystem workspace isolation (`CAP-06`) results in git merge conflicts, dirty uncommitted overwrites, and failing health gates.
   - Pairing `CAP-07` with `git worktree` isolation (`MEC-01`) creates an ultra-fast, zero-collision execution harness.
3. **CAP-03 (Dynamic Orchestration) vs CAP-04 (Deterministic Workflows):**
   - Harness architectures should avoid using dynamic LLM routing (`CAP-03`) for well-defined, static tool sequences.
   - The optimal harness builds deterministic blueprints (`CAP-04`) for structural pipelines and embeds dynamic orchestration (`CAP-03`) strictly at error-recovery and exploratory decision points.

---

## 5. Artifact Reference & Repo State

The complete ranking document and structured scorecards have been saved to the repository at:
[`phase-2/rankings/G1_EXECUTION.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-2/rankings/G1_EXECUTION.md)
stic workflows (`CAP-04`) for known structural graphs and embeds dynamic orchestration (`CAP-03`) only at non-deterministic decision and error recovery nodes.

---

## 4. Verification & Traceability Sign-Off

- **Taxonomy Source:** `phase-1/MASTER_TAXONOMY.md` §1 (CAP-01..07)
- **Batch 1 Inputs:** `phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md`, `V-D_ARCHITECTURAL.md`, `V-C_ADVERSARIAL.md`
- **Archetypes & Metrics:** `phase-0/ARCHETYPES_AND_CRITERIA.md` (C1–C6, SC-01..10)
- **Rubric & Veto Verification:** All 7 dimensions scored; Harm 4–5 veto verified; no average-based flattening applied.
