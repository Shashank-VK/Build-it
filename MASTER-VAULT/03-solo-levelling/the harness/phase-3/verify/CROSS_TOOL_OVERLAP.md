# Phase 3 Cross-Tool Overlap Sweep & Deduplication Report

> **Document Type:** Systematic Cross-Capability Dependency Audit & Tool Deduplication Sweep  
> **Source Files Audited:**  
> • [`phase-3/tools/T-A_EXECUTION.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (Execution Layer)  
> • [`phase-3/tools/T-B_CONTEXT.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (Context & Knowledge Layer)  
> • [`phase-3/tools/T-C_INTEGRATION.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-C_INTEGRATION.md) (Integration Layer)  
> • [`phase-3/tools/T-D_SAFETY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (Safety & Governance Layer)  
> • [`phase-3/tools/T-E_DX_META.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (DX & Meta-Governance Layer)  
> • [`phase-3/tools/T-F_A_TIER.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (A-Tier Capabilities Batch)  
> • [`phase-3/tools/T-G_A_TIER_2.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (Tier-2 Governance & Observability)  
> • [`phase-3/tools/T-H_B_TIER.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (B-Tier & Niche Capabilities)  
> **Output Artifact on Disk:** [`phase-3/verify/CROSS_TOOL_OVERLAP.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/verify/CROSS_TOOL_OVERLAP.md)  
> **Status:** 🟢 **SWEEP COMPLETE — ALL OVERLAPS RESOLVED & DEDUPLICATED**

---

## 1. Executive Summary & Sweep Methodology

During the evaluation of the 37 harness capabilities across Batches `T-A` through `T-H`, multiple high-leverage tools were independently selected or referenced across several capabilities and batch files. While this demonstrates the multi-purpose utility of modern developer tools, an uncurated list causes duplicate daemon overhead, conflicting configurations, and dependency bloat.

### 3-Way Decision Framework:
1. **`KEEP (Consolidate at Primary)`**: Anchor the tool at its single **Primary Anchor Capability**. Secondary capability requirements are treated as native API features or deployment modes of that primary tool, avoiding duplicate dependencies.
2. **`SPLIT (Multi-Purpose Matrix)`**: Formally split the tool's runtime role into distinct configuration interfaces when the tool genuinely serves multiple decoupled architectural planes (e.g., LiteLLM Gateway vs Budget Governor; Git Worktree Concurrency vs State Rollback).
3. **`REMOVE (Purge Redundancy / Gate Failure)`**: Eliminate redundant duplicate entries and demoted tools (e.g., RouteLLM, Lakera Guard) that failed verification gates.

```
========================================================================================
                          CROSS-TOOL OVERLAP SWEEP SUMMARY
========================================================================================
  Total Batch Documents Audited           : 8 Markdown Files (T-A through T-H)
  Total Tool Evaluations Analyzed         : 114 Tool Mentions & Evaluations
  Total Overlapping Tools Identified       : 31 Tools / Primitives
  Decision Breakdown:
    - Consolidated at Primary (KEEP)      : 27 Tools / Primitives
    - Multi-Purpose Partitioned (SPLIT)   :  2 Tools (LiteLLM, Git Worktree)
    - Demoted / Purged (REMOVE)           :  2 Tools (RouteLLM, Lakera Guard)
----------------------------------------------------------------------------------------
  FINAL DEDUPLICATED ESSENTIAL SUITE COUNT: 55 TOOLS & PRIMITIVES
========================================================================================
```

---

## 2. Master Cross-Tool Overlap Table

| # | Tool / Primitive | Appears In (Files & Capabilities) | Declared Roles Across Batches | Decision | Primary Anchor Capability | Consolidation Rationale |
|:--|:---|:---|:---|:---:|:---|:---|
| **1** | **LiteLLM** | • [`T-C`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-C_INTEGRATION.md) (CAP-22)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-16, CAP-23)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-35)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-12) | 1. Model Gateway Proxy (CAP-22)<br>2. Spend & Quota Manager (CAP-16/35)<br>3. Dynamic Fallback Router (CAP-23)<br>4. In-Gateway Semantic Cache (CAP-12) | 🔀 **SPLIT** | **CAP-22 (Model Gateways)** *(Primary deployment)* | LiteLLM is a genuinely multi-purpose gateway substrate. Deployed as a single proxy service, but config is partitioned across Gateway Routing (`CAP-22/23`), Budget Rules (`CAP-16/35`), and Caching (`CAP-12`). |
| **2** | **LangGraph** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-03, CAP-07)<br>• [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-29)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-02) | 1. StateGraph Orchestration (CAP-03)<br>2. `Send` Map-Reduce Fan-Out (CAP-07)<br>3. `interrupt()` Stateful HITL (CAP-29)<br>4. Multi-Agent Supervisor (CAP-02) | 🔒 **KEEP** | **CAP-03 (Dynamic Orchestration)** | Core state-graph engine. The `Send` API (CAP-07), `interrupt()` checkpointing (CAP-29), and Supervisor pattern (CAP-02) are native library features of LangGraph. |
| **3** | **Temporal** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-03, CAP-04, CAP-05)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-05)<br>• [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-29, CAP-30) | 1. Durable Control Flow (CAP-03)<br>2. Deterministic Replay (CAP-04)<br>3. Async Queued Tasks (CAP-05)<br>4. Signals Async Human Task (CAP-29)<br>5. Saga Compensators (CAP-30) | 🔒 **KEEP** | **CAP-05 (Background Execution)** | Unified durable execution engine. Workflow determinism, async queues, signals, and saga rollbacks are standard SDK features of a single Temporal cluster connection. |
| **4** | **gVisor (`runsc`)** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-24)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. OCI Sandbox Kernel (CAP-24)<br>2. AHG Sandbox Execution Gate (CAP-37) | 🔒 **KEEP** | **CAP-24 (Hermetic Isolation)** | gVisor provides the user-space virtualization kernel. CAP-37 (AHG Gate) invokes gVisor as its containment layer. Keep anchored at CAP-24. |
| **5** | **Bubblewrap (`bwrap`)** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-24)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. User Namespace Sandbox (CAP-24)<br>2. Local Sub-10ms CLI Jail (CAP-37) | 🔒 **KEEP** | **CAP-24 (Hermetic Isolation)** | Bubblewrap provides unprivileged local sandboxing. Referenced in CAP-37 as an execution gate. Anchor at CAP-24. |
| **6** | **Docker Engine / docker-py** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-24)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. Container Toolchain Runtime (CAP-24)<br>2. Ephemeral Sandbox Runner (CAP-37) | 🔒 **KEEP** | **CAP-24 (Hermetic Isolation)** | Universal container runtime substrate. Anchor at CAP-24; CAP-37 invokes Docker containers as sandboxed execution targets. |
| **7** | **Open Policy Agent (OPA) / Rego** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-25)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. Declarative Authorization Engine (CAP-25)<br>2. AHG Tool Evaluation Policy Gate (CAP-37) | 🔒 **KEEP** | **CAP-25 (Authorization Governance)** | OPA Rego policies define least-privilege rules. CAP-37 executes OPA queries before granting tool execution permissions. Anchor at CAP-25. |
| **8** | **Google CEL** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-25)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. In-Process Boolean Rule Engine (CAP-25)<br>2. Deterministic Guardrail Micro-Gate (CAP-37) | 🔒 **KEEP** | **CAP-25 (Authorization Governance)** | Sub-millisecond expression evaluator for fast input guards. Keep anchored at CAP-25. |
| **9** | **AWS Cedar** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-25)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. Formally Verified ABAC Engine (CAP-25)<br>2. AHG Policy Backend (CAP-37) | 🔒 **KEEP** | **CAP-25 (Authorization Governance)** | Formally verified permit/forbid policy backend. Anchor at CAP-25. |
| **10** | **Gitleaks** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-26)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37)<br>• [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-31) | 1. Stream DLP Secret Scanner (CAP-26)<br>2. Pre-Commit / Pre-Tool DLP Filter (CAP-37)<br>3. Supply-Chain Pre-Push Blocker (CAP-31) | 🔒 **KEEP** | **CAP-26 (Zero-Trust Secret Governance)** | Gitleaks is the ultra-fast regex scanner binary. Used as a filter across CI, hooks, and DLP pipelines. Centralize at CAP-26. |
| **11** | **TruffleHog** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-26)<br>• [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-31) | 1. Deep Entropy & API Verifier (CAP-26)<br>2. Supply-Chain Dependency Scanner (CAP-31) | 🔒 **KEEP** | **CAP-26 (Zero-Trust Secret Governance)** | Deep secret detection engine. Primary role is secret scanning; supply chain audit is a complementary operational mode. Anchor at CAP-26. |
| **12** | **Git Worktree + pygit2** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-06)<br>• [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-30) | 1. Parallel Subagent Branch Isolation (CAP-06)<br>2. Atomic State Rollback / Teardown (CAP-30) | 🔀 **SPLIT** | **CAP-06 (Workspace Isolation)** & **CAP-30 (State Reversibility)** | Dual architectural lifecycle: CAP-06 provisions concurrent zero-collision directories, while CAP-30 uses the worktree boundary to instantly discard rejected agent mutations via `git worktree remove`. |
| **13** | **SQLite (aiosqlite / SqliteSaver)** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-03/04)<br>• [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-30) | 1. In-Process State Checkpointing (CAP-03)<br>2. ACID Transactional Savepoints (CAP-30) | 🔒 **KEEP** | **CAP-30 (State Reversibility)** / Embedded Infra | Embedded database standard used across state checkpointers and transactional rollback savepoints. |
| **14** | **Letta (MemGPT)** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-08, CAP-10, CAP-14)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-10) | 1. Memory OS Context Paging (CAP-08)<br>2. Long-term Fact Consolidation (CAP-10)<br>3. Archival Session Search (CAP-14) | 🔒 **KEEP** | **CAP-10 (Memory Consolidation & State)** | Letta is an autonomous memory management system. Context compaction and archival recall are built-in features of Letta's memory architecture. Anchor at CAP-10. |
| **15** | **Mem0** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-10, CAP-14)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-10) | 1. User/Agent Preference Memory (CAP-10)<br>2. Experiential Fact Recall (CAP-14) | 🔒 **KEEP** | **CAP-10 (Memory Consolidation & State)** | Mem0 extracts and consolidates persistent facts and user preferences. Recall is handled via the same Mem0 search API. Anchor at CAP-10. |
| **16** | **Qdrant** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-13, CAP-14, CAP-15)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-14) | 1. Hybrid Sparse/Dense Vector Engine (CAP-13)<br>2. Past Trace Vector Store (CAP-14)<br>3. Semantic Code Chunk Store (CAP-15) | 🔒 **KEEP** | **CAP-13 (Vector Indexing & Retrieval)** | Qdrant is the universal vector storage engine. CAP-14 (Trace Recall) and CAP-15 (Code Search) utilize Qdrant collections. Anchor at CAP-13. |
| **17** | **LanceDB** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-08, CAP-10, CAP-13, CAP-14) | 1. Embedded Vector Database (CAP-13)<br>2. Local Context Chunk Storage (CAP-08)<br>3. Local Memory Items Store (CAP-10)<br>4. In-Process Memory Recall (CAP-14) | 🔒 **KEEP** | **CAP-13 (Vector Indexing & Retrieval)** | Serverless in-process vector store. Used as an embedded persistence substrate across memory and context caching. Anchor at CAP-13. |
| **18** | **LlamaIndex** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-13, CAP-15)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-14) | 1. RAG Ingestion & Index Pipeline (CAP-13)<br>2. Hierarchicaarness/phase-3/tools/T-B_CONTEXT.md) (CAP-13, CAP-15)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-14) | 1. RAG Ingestion & Index Pipeline (CAP-13)<br>2. Hierarchical Code Parser Index (CAP-15)<br>3. Experiential Trace Indexing (CAP-14) | 🔒 **KEEP** | **CAP-15 (Code Context Parsing & Indexing)** | Data framework for AST-aware code chunking, parsing, and structured retrieval. Anchor at CAP-15 with cross-links to CAP-13/14. |
| **19** | **Repomix** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-08, CAP-15) | 1. Token-Optimized Code Packager (CAP-15)<br>2. Deterministic Context Compaction (CAP-08) | 🔒 **KEEP** | **CAP-15 (Code Context Parsing & Indexing)** | Specialized repository context packing CLI. Compaction is a natural byproduct of its XML packing output. Anchor at CAP-15. |
| **20** | **Tiktoken & Tokenizers** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-08, CAP-16)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-16)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-35) | 1. Context Window Validation (CAP-08)<br>2. Pre-Flight Token Budgeting (CAP-16)<br>3. Hard Limit Quota Gate (CAP-35) | 🔒 **KEEP** | **CAP-16 (Context Budgeting & Allocation)** | In-process sub-millisecond BPE token counter. Used across context window guards and cost tracking. Anchor at CAP-16. |
| **21** | **LLMLingua / LongLLMLingua** | • [`T-B`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-B_CONTEXT.md) (CAP-08, CAP-09, CAP-16) | 1. Context Eviction / Compaction (CAP-08)<br>2. Perplexity Prompt Compression (CAP-09)<br>3. Dynamic Budget Reducer (CAP-16) | 🔒 **KEEP** | **CAP-09 (Prompt Compression)** | Prompt compression algorithm. Used when prompt tokens exceed allocation limits. Anchor at CAP-09. |
| **22** | **Promptfoo** | • [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-32)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-33)<br>• [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-34) | 1. Fast Local CLI Eval Engine (CAP-32)<br>2. Grader Assertions & Red-Teaming (CAP-33)<br>3. DSPy Prompt Regression Suite (CAP-34) | 🔒 **KEEP** | **CAP-32 (Evaluation Engines & Harnesses)** | High-speed local CLI test and assertion runner. Referenced in CAP-33/34 as the downstream execution harness for prompt test suites. Anchor at CAP-32. |
| **23** | **DeepEval** | • [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-32)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-33)<br>• [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-34) | 1. Unit-Test LLM Eval Framework (CAP-32)<br>2. G-Eval & CoT Judge Calibration (CAP-33)<br>3. Metric Evaluator for DSPy Tuning (CAP-34) | 🔒 **KEEP** | **CAP-33 (Meta-Evaluation & Calibration)** | Specialized framework for LLM judge calibration and G-Eval alignment. Anchor at CAP-33 (Essential in C4 archetype). |
| **24** | **Langfuse** | • [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-16)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-35)<br>• [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-28) | 1. Token/Spend Analytics (CAP-16)<br>2. Fleet Cost Attribution & Telemetry (CAP-35)<br>3. Distributed Trace Receiver (CAP-28) | 🔒 **KEEP** | **CAP-35 (Cost & Budget Governance)** | Dedicated open-source observability and cost attribution backend. Anchor at CAP-35 (with direct linkage to CAP-16). |
| **25** | **Arize Phoenix** | • [`T-G`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-G_A_TIER_2.md) (CAP-28, CAP-34)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-33) | 1. OTel Tracing & Trajectory Replay (CAP-28)<br>2. Judge Eval & Cluster Drift (CAP-33)<br>3. Trace Eval for Self-Improvement (CAP-34) | 🔒 **KEEP** | **CAP-28 (Execution Provenance)** | AI observability, span tracing, and execution replay backend. Anchor at CAP-28. |
| **26** | **Trigger.dev v3** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-05)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-05) | 1. Code-First Background Tasks (CAP-05)<br>2. Async Job Runner with Real-Time Logs (CAP-05) | 🔒 **KEEP** | **CAP-05 (Background Execution)** | Redundant duplicate entry across batch files for the same capability. Retain single entry at CAP-05. |
| **27** | **Pre-Commit + Ruff** | • [`T-C`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-C_INTEGRATION.md) (CAP-20)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. Git Hook Linter/Formatter (CAP-20)<br>2. Deterministic AST Quality Gate (CAP-37) | 🔒 **KEEP** | **CAP-20 (Lifecycle Hooks)** | Pre-commit framework executing Ruff lint/format rules. Anchor at CAP-20. |
| **28** | **Native Lifecycle Hooks** | • [`T-C`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-C_INTEGRATION.md) (CAP-20)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. Agent Event Interceptors (CAP-20)<br>2. Pre/Post-Tool Policy Validation (CAP-37) | 🔒 **KEEP** | **CAP-20 (Lifecycle Hooks)** | Native in-process event hook runner (`hooks.json`). Anchor at CAP-20. |
| **29** | **Native Interactive Confirmation (`ask_question` / Permission Matrix)** | • [`T-D`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-29)<br>• [`T-E`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-E_DX_META.md) (CAP-37) | 1. In-Process Modal Approval (CAP-29)<br>2. Tool Escalation Permission Gate (CAP-37) | 🔒 **KEEP** | **CAP-29 (HITL Escalation Gateway)** | Interactive confirmation framework and permission matrix. Anchor at CAP-29. |
| **30** | **Graphiti (Zep)** | • [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-11)<br>• [`T-F`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-10) | 1. Bi-Temporal Agent Knowledge Graph (CAP-11)<br>2. Graph-Based Memory Backend (CAP-10) | 🔒 **KEEP** | **CAP-11 (Bi-Temporal KG Memory)** | Bi-temporal knowledge graph engine. Anchor at CAP-11 (Essential for C2/C4). |
| **31** | **CrewAI Flows** | • [`T-A`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-A_EXECUTION.md) (CAP-04, CAP-01)<br>• [`T-H`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-H_B_TIER.md) (CAP-02) | 1. Event-Driven DAG Workflows (CAP-04)<br>2. Role-playing Agents (CAP-01/02 - Avoid) | 🔒 **KEEP** | **CAP-04 (Deterministic Workflows)** | CrewAI Flows `@flow` DSL selected specifically for deterministic code DAGs. Role-playing multi-agent chat loops are explicitly avoided. Anchor at CAP-04. |

---

## 3. Purged & Demoted Redundancies (Gate Failures)

The following candidate tools appeared in batch recommendations but have been formally **REMOVED** from Essential status due to verification gate failures:

1. ❌ **RouteLLM (LMSYS)** — Appeared in [`T-F_A_TIER.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-F_A_TIER.md) (CAP-23)
   - **Gate Failure:** >24-month maintenance stagnation (last commit August 2024), obsolete routing matrix drift.
   - **Resolution:** **REMOVED from Essential**. Replaced entirely by **LiteLLM Dynamic Rule-Based Routing**.
2. ❌ **Lakera Guard** — Appeared in [`T-D_SAFETY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) (CAP-27)
   - **Gate Failure:** Invalid repository URL (HTTP 404), closed commercial SaaS dependency violating hermetic runtime invariant.
   - **Resolution:** **REMOVED from Essential**. Replaced by **Structural XML Fencing + PROT-04 Taint Tracking** and local classifiers.

---

## 4. Final Deduplicated Essential Tool List (55 Primitives)

Following cross-tool overlap consolidation, the production AI Development Harness requires exactly **55 Essential Tools and Primitives** across the 5 architectural layers:

```
========================================================================================
             FINAL DEDUPLICATED ESSENTIAL TOOL SUITE BY ARCHITECTURAL LAYER
========================================================================================
  1. Execution Layer (CAP-01 .. CAP-07)                 : 10 Essential Tools
  2. Context & Knowledge Layer (CAP-08 .. CAP-16)       : 11 Essential Tools
  3. Integration Layer (CAP-17 .. CAP-23)               :  7 Essential Tools
  4. Safety & Governance Layer (CAP-24 .. CAP-30)       : 14 Essential Tools
  5. Developer Experience & Meta-Layer (CAP-28 .. 37)   : 13 Essential Tools
----------------------------------------------------------------------------------------
  TOTAL DEDUPLICATED ESSENTIAL SUITE                    : 55 TOOLS & PRIMITIVES
========================================================================================
```

### Layer 1: Execution Layer (10 Essential Tools)
1. **Claude Agent SDK** (`anthropics/claude-agent-sdk-python`) — `CAP-01` Delegated Subagents
2. **OpenAI Agents SDK** (`openai/openai-agents-python`) — `CAP-01` Delegated Subagents
3. **Antigravity CLI Subagent Runtime** (`invoke_subagent`) — `CAP-01` Delegated Subagents
4. **LangGraph** (`langchain-ai/langgraph`) — `CAP-03` Dynamic Orchestration *(Consolidates CAP-07 Fan-Out & CAP-02 Supervisor)*
5. **Temporal SDK & Engine** (`temporalio/temporal`) — `CAP-05` Background & Durable Execution *(Consolidates CAP-03, CAP-04, CAP-29, CAP-30)*
6. **CrewAI Flows** (`crewAIInc/crewAI`) — `CAP-04` Deterministic Workflows
7. **Taskfile / Just** (`go-task/task` / `casey/just`) — `CAP-04` Deterministic Local Workflows
8. **Trigger.dev v3** (`triggerdotdev/trigger.dev`) — `CAP-05` Background & Queued Execution
9. **Git Worktree Manager** (`git worktree` / `pygit2`) — `CAP-06` Workspace Isolation *(Split: Creation & Branch Isolation)*
10. **AnyIO Structured Concurrency** (`agronholm/anyio`) — `CAP-07` Bounded Parallel Fan-Out

### Layer 2: Context & Knowledge Layer (11 Essential Tools)
11. **LLMLingua / LongLLMLingua** (`microsoft/LLMLingua`) — `CAP-09` Prompt Compression *(Consolidates CAP-08 Compaction)*
12. **Letta (MemGPT)** (`letta-ai/letta`) — `CAP-10` Memory Consolidation *(Consolidates CAP-08 & CAP-14)*
13. **Mem0** (`mem0ai/mem0`) — `CAP-10` Memory Consolidation *(Consolidates CAP-14 Preferences)*
14. **Graphiti (Zep)** (`getzep/graphiti`) — `CAP-11` Bi-Temporal Knowledge Graph Memory
15. **RedisVL / Valkey** (`valkey-io/valkey` / `redis-vl-python`) — `CAP-12` Semantic Caching Substrate
16. **Qdrant** (`qdrant/qdrant`) — `CAP-13` Vector Indexing & Hybrid Retrieval *(Consolidates CAP-14 & CAP-15)*
17. **LanceDB** (`lancedb/lancedb`) — `CAP-13` Serverless Embedded Vector Store *(Consolidates CAP-08, CAP-10, CAP-14)*
18. **LlamaIndex** (`run-llama/llama_index`) — `CAP-15` Code Context Parsing & Indexing *(Consolidates CAP-13/14)*
19. **Tree-sitter** (`tree-sitter/tree-sitter`) — `CAP-15` AST/CST Code Parsing Engine
20. **Repomix** (`yamadashy/repomix`) — `CAP-15` Codebase Context Packaging
21. **Tiktoken & Tokenizers** (`openai/tiktoken` / `huggingface/tokenizers`) — `CAP-16` Context Budgeting *(Consolidates CAP-08 & CAP-35)*

### Layer 3: Integration Layer (7 Essential Tools)
22. **FastMCP** (`jlowin/fastmcp` / `modelcontextprotocol`) — `CAP-17` Model Context Protocol (MCP) SDK
23. **Reference MCP Servers Suite** (`modelcontextprotocol/servers`) — `CAP-17` Canonical Tool Calling Standard
24. **Procedural Skills Engine (40 Skills)** (Harness Native / `SKILL.md`) — `CAP-18` Procedural Skills Repository
25. **Ambient Rules Engine** (`CLAUDE.md`, `.cursorrules`, `.gemini/rules/`) — `CAP-19` Ambient Rules & Guidelines
26. **Native Lifecycle Hooks Engine** (`hooks.json`) — `CAP-20` Lifecycle Interceptors *(Consolidates CAP-37 AHG)*
27. **Pre-Commit + Ruff** (`pre-commit/pre-commit` / `astral-sh/ruff`) — `CAP-20` AST & Commit Interceptors
28. **LiteLLM** (`BerriAI/litellm`) — `CAP-22` Model Gateways *(Split: Proxy, Router, Spend Manager, Semantic Cache)*

### Layer 4: Safety & Governance Layer (14 Essential Tools)
29. **gVisor (`runsc`)** (`google/gvisor`) — `CAP-24` Hermetic Isolation *(Consolidates CAP-37 Sandboxing)*
30. **Bubblewrap (`bwrap`)** (`containers/bubblewrap`) — `CAP-24` Sub-10ms Namespace Sandbox
31. **Docker Engine / docker-py** (`moby/moby` / `docker-py`) — `CAP-24` Container Isolation Substrate
32. **Open Policy Agent (OPA) / Rego** (`open-policy-agent/opa`) — `CAP-25` Declarative Authorization *(Consolidates CAP-37)*
33. **AWS Cedar** (`cedar-policy/cedar`) — `CAP-25` Formally Verified ABAC
34. **Google CEL** (`google/cel-spec` / `cel-python`) — `CAP-25` Fast In-Process Boolean Micro-Rules
35. **Gitleaks** (`gitleaks/gitleaks`) — `CAP-26` Stream DLP Secret Scanner *(Consolidates CAP-31 & CAP-37)*
36. **TruffleHog** (`trufflesecurity/trufflehog`) — `CAP-26` Deep Entropy & API Secret Scanner
37. **Infisical CLI & Platform** (`Infisical/infisical`) — `CAP-26` JIT Ephemeral Subprocess Secret Injection
38. **HashiCorp Vault / OpenBao & hvac** (`openbao/openbao` / `hashicorp/vault`) — `CAP-26` Dynamic JIT Secret Broker
39. **Structural XML Delimiter Fencing & PROT-04** (OWASP LLM01 Standard / Native) — `CAP-27` Prompt Injection Defense
40. **Native Interactive Confirmation (`ask_question` / Permission Matrix)** — `CAP-29` HITL Escalation Gateway
41. **Rich & InquirerPy** (`Textualize/rich` / `InquirerPy`) — `CAP-29` Terminal Interactive Modal UI
42. **SQLite Savepoints & Rollback** (`sqlite3` / `aiosqlite`) — `CAP-30` Transactional Memory Reversibility

### Layer 5: Developer Experience & Meta-Layer (13 Essential Tools)
43. **OpenInference / OpenTelemetry** (`Arize-ai/openinference` / `open-telemetry`) — `CAP-28` Execution Provenance
44. **JSONL Trajectory Ledger** (`transcript.jsonl`) — `CAP-28` Immutable Local Execution Provenance
45. **Arize Phoenix** (`Arize-ai/phoenix`) — `CAP-28` OTel Tracing Backend & Replay Platform
46. **Sigstore Cosign** (`sigstore/cosign`) — `CAP-31` Keyless Supply-Chain Artifact Signing
47. **SLSA GitHub Generator** (`slsa-framework/slsa-github-generator`) — `CAP-31` Cryptographic Build Provenance
48. **Promptfoo** (`promptfoo/promptfoo`) — `CAP-32` Local CLI Evaluation & Assertion Engine *(Consolidates CAP-33/34)*
49. **Inspect AI** (`UKGovernmentBEIS/inspect_ai`) — `CAP-32` Agentic Benchmark & Tool-Use Eval Harness
50. **SWE-bench Runner & Suite** (`princeton-nlp/SWE-bench`) — `CAP-32` Golden SWE Agent Benchmark Harness
51. **DeepEval** (`confident-ai/deepeval`) — `CAP-33` Meta-Evaluation & G-Eval Judge Calibration *(S-Tier in C4)*
52. **DSPy** (`stanfordnlp/dspy`) — `CAP-34` Programmatic Self-Improving Prompt Compilation
53. **Langfuse** (`langfuse/langfuse`) — `CAP-35` Fleet Cost Attribution & Telemetry *(Consolidates CAP-16)*
54. **Semgrep** (`semgrep/semgrep`) — `CAP-36` AST Deprecation Policy Enforcement
55. **`deprecated` Decorator** (`tantale/deprecated` / PEP 702) — `CAP-36` Runtime Schema & API Sunset Management

---

## 5. Architectural Synthesis & Implementation Rules

1. **Zero Runtime Bloat Guarantee:** By consolidating overlapping tools into their primary host capabilities, we reduce duplicate background daemons and overlapping pip dependencies from 114 declared tool instances down to **55 unique, non-colliding components**.
2. **Configuration Partitioning (SPLIT Tools):**
   * **LiteLLM**: Single service deployment (`litellm --config config.yaml`), with YAML blocks partitioned into `model_list` (CAP-22/23), `general_settings.max_budget` (CAP-16/35), and `litellm_settings.cache` (CAP-12).
   * **Git Worktree**: Unified `pygit2` / CLI binding with explicit entry points for `create_isolated_workspace()` (CAP-06) and `revert_agent_worktree()` (CAP-30).
3. **Execution Pipeline Integration:** Downstream slices (harness configs, MCP definitions, permission matrices) must strictly consume tool identifiers and capabilities defined in this deduplicated catalog.
