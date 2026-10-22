# SYNTHESIS D-2 — MASTER TAXONOMY LEVEL-HYGIENE AUDIT
## Phase 1: AI Development Harness Architecture

> **Role:** Synthesis D-2 — Master Taxonomy Level-Hygiene Auditor  
> **Date:** 2026-09-01  
> **Scope:** Full abstraction hygiene audit of **101 candidate elements** across Batches 1 to 5  
> **Artifact on Disk:** [`phase-1/synthesis/MASTER_D2.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/synthesis/MASTER_D2.md)

---

## 1. Abstraction Ontology & Hygiene Criteria

To eliminate category errors, vendor conflation, and taxonomy bloat, every candidate element discovered during Phase 1 is strictly evaluated against a 6-tier ontological hierarchy:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            6-TIER ABSTRACTION HIERARCHY                                      │
├──────────────────────────┬──────────────────────────────────────────────────────────────────┤
│ Level                    │ Definition & Criteria                                            │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 1. Capability (CAP)      │ Fundamental functional requirement (WHAT the harness needs).    │
│                          │ Vendor-agnostic; survives complete rewrite/replacement of tech.  │
│                          │ Target: ~30–40 canonical capabilities across the entire harness. │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 2. Mechanism (MEC)       │ Algorithmic, structural, or behavioral pattern (HOW it works).   │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 3. Protocol / Standard   │ Formal data schema, IPC format, or contract (INTERFACES).        │
│    (STD / PROT)          │ (e.g., JSON-RPC 2.0, POSIX, Git CLI contract, SLSA v1.0).        │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 4. Framework / Runtime   │ Software engine, supervisor library, or execution environment.   │
│    (RUN / FW)            │ (e.g., LangGraph, gVisor, OPA, LiteLLM, Claude Agent SDK).       │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 5. Resource / Artifact   │ Passive data asset, file, config, or prompt template on disk.    │
│    (ART / RES)           │ (e.g., SKILL.md, AGENTS.md, transcript.jsonl, hooks.json).       │
├──────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ 6. Tool / Product / Repo │ External standalone binary, SaaS product, or public repository.  │
│    (TLS / PRD)           │ (e.g., Claude Code, Cursor, HashiCorp Vault, Semgrep, Pinecone). │
└──────────────────────────┴──────────────────────────────────────────────────────────────────┘
```

---

## 2. Cross-Batch Boundary & Deduplication Verifications

The audit inspected all cross-batch touchpoints to enforce single-canonical ownership:

### 2.1 Hooks & Lifecycle Interception (B1-E10 ↔ B3-13 ↔ B4-12)
- **Finding:** Batch 1 discovered `E10 Lifecycle Interception / Hooks`; Batch 3 re-introduced `B3-13 Lifecycle Hooks`; Batch 4 used `PreToolUse` hooks for injection defense.
- **Audited Resolution:** Unified into a single Top-Level Capability: **Lifecycle Interception & Policy Hooks** (owned by Layer 3: Integration & Extensibility / Control Plane).
- **Sub-level Assignment:** `hooks.json` is a Resource ([`B3-15`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L39)); `PreToolUse` policy checks and event dispatchers are Mechanisms ([`B3-14`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L38) / `M6`).

### 2.2 Workspace Isolation vs Hermetic Sandboxing (B1-E6 ↔ B4-01)
- **Finding:** Potential conflation between Git Worktrees ([`B1-E6`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md#L31)) and Execution Sandboxing ([`B4-01`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md#L24)).
- **Audited Resolution:** **Strict Dual-Boundary Separation (2 distinct Capabilities)**:
  1. **Isolated Workspace Management (B1-E6):** Filesystem-level isolation managing parallel checkouts, branches, and directory trees without branch pollution. (Primary Mechanism: Git Worktree `M1` / `S2`).
  2. **Hermetic Isolated Execution (B4-01):** Kernel/syscall-level process containment preventing untrusted code execution from accessing host networks or filesystem roots. (Mechanisms: microVM, gVisor `B4-02/03`).

### 2.3 State Reversibility, Checkpoints & Undo (B1-E11 ↔ B4-20 ↔ B5-05/06/07)
- **Finding:** Reversibility was listed as Capability `E11` in Batch 1, Capability `B4-20` in Batch 4, and fragmented into 3 mechanisms in Batch 5 (`B5-05`, `B5-06`, `B5-07`).
- **Audited Resolution:** Unified into a single Top-Level Capability: **State Reversibility & Side-Effect Compensation** ([`E11 / B4-20`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md#L36)).
- **Sub-level Assignment:** Deconstructed into 4 specific operational Mechanisms:
  - *Filesystem Snapshots* ([`B5-05`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L26))
  - *Context Truncation / Rewind* ([`B5-06`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L27))
  - *Compensating Tool Inversion* ([`B5-07`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L28))
  - *Saga Coordinator* ([`B4-22`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md#L45))

### 2.4 Autonomy Calibration vs HITL Approval Gates (B1-E7/E8 ↔ B4-04/19)
- **Finding:** Autonomy policy and HITL review gates were split across Batch 1 and Batch 4.
- **Audited Resolution:** **Two distinct, orthogonal Capabilities**:
  1. **Autonomy Calibration & Least-Privilege Policy (E7 / B4-04):** The static/dynamic policy determining what an agent is allowed to execute unassisted.
  2. **Human-in-the-Loop (HITL) Interruption & Approval Gates (E8 / B4-19):** The interactive execution primitive that suspends execution, presents structured diffs, and awaits human authorization.

### 2.5 Prompt Injection Defense & Untrusted Fencing (B2-B6 ↔ B4-12)
- **Finding:** Batch 2 defined `B6 Untrusted-Content Fencing` (context assembly); Batch 4 defined `B4-12 Indirect Injection Gateway` (tool I/O).
- **Audited Resolution:** Unified into a single Top-Level Capability: **Instruction-vs-Data Trust Boundary & Injection Defense** ([`B2-B6 / B4-12`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md#L34)). Operates as a dual-boundary system: Delimiter Fencing (`M-B6a`) at context assembly + Dual-LLM/PreToolUse Scanner (`M-B6c` / `B4-13`) at the tool boundary.

### 2.6 Context Budgeting vs Harness Complexity Budgeting (B2-B10 ↔ B5-08/09/25)
- **Finding:** Budgeting spanned prompt token limits (Batch 2), cost meters (Batch 5), and system complexity bounds (Batch 5).
- **Audited Resolution:** **Two distinct Capabilities**:
  1. **Context Window Budget Governance (B2-B10):** Turn-level allocation across prompt components (P0–P10 hierarchy).
  2. **Harness Complexity & Financial Budget Enforcement (B5-25):** System-level quotas on cumulative run cost, tool proliferation, and hook depth.
  - *Artifact:* `Cost Ledger` ([`B5-08`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L29)).
  - *Mechanism:* `Real-Time Hard-Stop Circuit Breaker` ([`B5-09`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L30)).

### 2.7 Audit Provenance vs Observability vs Replay (B4-14/17 ↔ B5-01/02)
- **Finding:** Telemetry, audit trails, and execution replay were conflated across Batches 4 and 5.
- **Audited Resolution:**
  - **Execution Provenance & Immutable Audit (B4-14):** Capability (WAL Flight Recorder `B4-15` is Mechanism; `transcript.jsonl` `B4-16` is Resource).
  - **Deterministic Execution Replayability (B4-17):** Capability (Virtual Clock & Syscall Interception `B4-18` is Mechanism).
  - **Telemetry & Observability Substrate (B5-01):** Infrastructure Substrate / Framework (OTel Spans `B5-02` are Resources).

---

## 3. Complete 101-Candidate Master Level-Audit Table

| # | Candidate Identifier & Name | Batch Label | Audited Level | Hygiene Flag | Cross-Batch Mapping & Deduplication |
|---|-----------------------------|-------------|---------------|--------------|--------------------------------------|
| **Batch 1: Execution & Agency Layer (11 Candidates)** |
| 01 | **E1 Delegated Subagent Execution** | Capability | **Capability** | `CLEAN` | Interfaces with B3-02 (MCP Client), B4-05 (CapBAC) |
| 02 | **E2 Agent Teams / Collaboration** | Capability | **Capability** | `CLEAN` | Uses B8 (Shared Experience Memory), B4-05 (CapBAC) |
| 03 | **E3 Orchestration Layer** | Capability | **Capability** | `CLEAN` | Dynamic DAG engine driving B3-22 tool schemas |
| 04 | **E4 Workflows / Flows (Blueprints)** | Capability / Mech | **Capability** | `CONFLATED -> FIX` | Retagged to *Deterministic Workflow Blueprint Execution* (blueprint files are Resources) |
| 05 | **E5 Background / Async Execution** | Capability | **Capability** | `CLEAN` | Distinct from B5-10 Headless CI Runner mode |
| 06 | **E6 Git Worktree Isolated Workspaces**| Capability | **Capability** | `CONFLATED -> FIX` | Retagged to *Isolated Workspace Management*; Git Worktree is Mechanism M1 / S2 |
| 07 | **E7 Autonomy Calibration** | Capability | **Capability** | `CLEAN` | Merged with B4-04 into unified Autonomy & Authz Capability |
| 08 | **E8 Human-in-the-Loop Controls** | Capability | **Capability** | `CLEAN` | Merged with B4-19 into unified HITL Interruption Capability |
| 09 | **E9 Parallel Execution & Fan-out** | Capability | **Capability** | `CLEAN` | Sub-capability of Orchestration (independent concurrency knob) |
| 10 | **E10 Lifecycle Interception / Hooks** | Capability | **Capability** | `CLEAN` | Duplicate of B3-13; unified as Lifecycle Interception & Hooks |
| 11 | **E11 Reversibility / Compensation** | Capability | **Capability** | `CLEAN` | Duplicate of B4-20; implemented by B5-05/06/07 Mechanisms |
| **Batch 2: Context, Memory & Knowledge Layer (10 Candidates)** |
| 12 | **B1 Working Memory Isolation** | Capability | **Capability** | `CLEAN` | Turn-level context window container; governed by B10 & B5-25 |
| 13 | **B2 Context Compaction (Pinned)** | Capability | **Capability** | `CLEAN` | Anti-exhaustion loop; preserves B6 fencing & B1 pinned tokens |
| 14 | **B3 Memory Consolidation Daemon** | Capability | **Capability** | `CLEAN` | Sleep-pass promotion; consumes B1-E5 async & B1-E10 hooks |
| 15 | **B4 Typed / Bi-Temporal KG Memory** | Capability | **Capability** | `CLEAN` | Specialized relational memory substrate (Cypher is Protocol) |
| 16 | **B5 Semantic Cache** | Capability (Spec) | **Capability (Spec)** | `CONFLATED -> FIX` | Borderline Mechanism; kept as Specialized Capability for response reuse |
| 17 | **B6 Untrusted-Content Fencing** | Capability (Veto) | **Capability** | `CLEAN` | Merged with B4-12 into Instruction Trust Boundary Capability |
| 18 | **B7 External Retrieval (RAG)** | Capability | **Capability** | `CLEAN` | Stateless external data retrieval (Vector DB is Tool) |
| 19 | **B8 Memory Recall (Internal)** | Capability | **Capability** | `CLEAN` | Stateful reconstructive experience recall across sessions |
| 20 | **B9 Knowledge Curation (Build-Time)**| Capability | **Capability** | `CLEAN` | Build-time corpus indexing & distillation; feeds B3-06 |
| 21 | **B10 Context Budget Governance** | Capability | **Capability** | `CLEAN` | Turn-level prompt/tool/context token allocation |
| **Batch 3: Integration & Extensibility Layer (24 Candidates)** |
| 22 | **B3-01 Model Context Protocol (MCP)** | Protocol/Standard | **Protocol/Standard** | `CLEAN` | Cross-referenced in Batch 1 S1 |
| 23 | **B3-02 MCP Client Subsystem** | Framework/Runtime | **Framework/Runtime** | `CLEAN` | Harness middleware executing MCP protocol |
| 24 | **B3-03 MCP Server Runtime** | Framework/Runtime | **Framework/Runtime** | `CLEAN` | External isolated process hosting tools |
| 25 | **B3-04 MCP Registry & Catalogs** | Tool/Product/Repo | **Tool/Product/Repo** | `CLEAN` | Catalog/discovery service (mcp.so, Glama, PulseMCP) |
| 26 | **B3-05 MCP Primitives (Schemas)** | Protocol/Standard | **Protocol/Standard** | `CLEAN` | JSON-RPC data models for tools/resources/prompts |
| 27 | **B3-06 Skills Capability** | Capability | **Capability** | `CLEAN` | Procedural runbook loading & execution |
| 28 | **B3-07 Individual Skill Resource** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | `SKILL.md` + frontmatter file asset |
| 29 | **B3-08 GitHub Skills Repositories** | Impl/Repo | **Tool/Product/Repo** | `CLEAN` | Remote package sources |
| 30 | **B3-09 Progressive Disclosure** | Mechanism | **Mechanism** | `CLEAN` | Two-stage loading mechanism for B3-06 under B10 |
| 31 | **B3-10 Rules Enforcement** | Capability | **Capability** | `CLEAN` | Hierarchical ambient constraint enforcement |
| 32 | **B3-11 Directory & Project Rules** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | `AGENTS.md`, `.cursorrules` file assets |
| 33 | **B3-12 Rule Dedup & Inheritance** | Mechanism | **Mechanism** | `CLEAN` | Tree-traversal resolution mechanism |
| 34 | **B3-13 Lifecycle Hooks** | Capability | **Capability** | `DUPLICATE` | Identical to Batch 1 E10; unified as Lifecycle Interception |
| 35 | **B3-14 Deterministic Policy Gates** | Mechanism | **Mechanism** | `CLEAN` | Pre/PostToolUse policy evaluation mechanism |
| 36 | **B3-15 Hook Configuration Manifest**| Resource/Artifact | **Resource/Artifact** | `CLEAN` | `hooks.json` configuration file |
| 37 | **B3-16 Plugin Packaging** | Capability | **Capability** | `CLEAN` | Multi-component extension bundling & namespacing |
| 38 | **B3-17 Plugin Manifest & Bundle** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | `plugin.json` package archive |
| 39 | **B3-18 Model Gateway & Translation** | Capability | **Capability** | `CLEAN` | Provider-agnostic LLM interfacing & schema translation |
| 40 | **B3-19 Multi-Provider Proxy** | Tool/Framework | **Tool/Product/Repo** | `CONFLATED -> FIX` | LiteLLM/Portkey are Tools/Proxies implementing B3-18 |
| 41 | **B3-20 Dynamic Model Routing** | Capability | **Capability** | `CLEAN` | Cost/quality turn routing capability |
| 42 | **B3-21 Model Router Engines** | Tool/Mechanism | **Tool/Product/Repo** | `CONFLATED -> FIX` | RouteLLM/OpenRouter are Tools/Engines implementing B3-20 |
| 43 | **B3-22 Function Calling Schemas** | Protocol/Standard | **Protocol/Standard** | `CLEAN` | JSON-Schema tool call interface contract |
| 44 | **B3-23 Execution vs Control Plane** | Arch Pattern | **Architectural Pattern**| `CONFLATED -> FIX` | Design Invariant / Boundary, NOT a Capability |
| 45 | **B3-24 Governance Scoping & Cascade**| Mechanism/Pattern | **Mechanism** | `CLEAN` | Priority cascade resolution mechanism |
| **Batch 4: Safety, Governance & Trust Layer (26 Candidates)** |
| 46 | **B4-01 Hermetic Isolated Execution** | Capability | **Capability** | `CLEAN` | OS/process kernel isolation (distinct from E6 workspace) |
| 47 | **B4-02 Container/MicroVM Sandbox** | Mechanism | **Mechanism** | `CLEAN` | Isolation mechanism implementing B4-01 |
| 48 | **B4-03 gVisor / Bubblewrap / Wasm** | Framework/Runtime | **Framework/Runtime** | `CLEAN` | Sandbox execution runtimes |
| 49 | **B4-04 Authorization & Governance** | Capability | **Capability** | `CLEAN` | Merged with Batch 1 E7 into Autonomy & Authz Capability |
| 50 | **B4-05 CapBAC Model** | Mechanism | **Mechanism** | `CLEAN` | Token capability security mechanism |
| 51 | **B4-06 Declarative Policy Engine** | Mechanism | **Mechanism** | `CLEAN` | Policy-as-code mechanism |
| 52 | **B4-07 OPA / Cedar Engine** | Framework/Runtime | **Framework/Runtime** | `CLEAN` | Concrete policy evaluation runtime |
| 53 | **B4-08 Zero-Trust Secret Governance**| Capability | **Capability** | `CLEAN` | Zero plaintext secrets in LLM context/workspace |
| 54 | **B4-09 JIT Credential Brokering** | Mechanism | **Mechanism** | `CLEAN` | Ephemeral secret injection mechanism |
| 55 | **B4-10 HashiCorp Vault / AWS KMS** | Tool/Product/Repo | **Tool/Product/Repo** | `CLEAN` | External KMS/Vault tools |
| 56 | **B4-11 DLP & Stream Masking** | Mechanism | **Mechanism** | `CLEAN` | Real-time secret scrubber mechanism |
| 57 | **B4-12 Indirect Injection Defense** | Capability | **Capability** | `DUPLICATE` | Merged with B2-B6 into Instruction Trust Boundary |
| 58 | **B4-13 Dual-LLM Sanitizer** | Mechanism | **Mechanism** | `CLEAN` | Sanitizer architecture implementing B6/B4-12 |
| 59 | **B4-14 Execution Provenance** | Capability | **Capability** | `CLEAN` | Immutable non-repudiable audit capability |
| 60 | **B4-15 Cryptographic Flight Recorder**| Mechanism | **Mechanism** | `CLEAN` | WAL logging mechanism implementing B4-14 |
| 61 | **B4-16 Transcript `transcript.jsonl`**| Resource/Artifact | **Resource/Artifact** | `CLEAN` | Append-only execution record artifact |
| 62 | **B4-17 Deterministic Replayability** | Capability | **Capability** | `CLEAN` | Deterministic run replay capability |
| 63 | **B4-18 Virtual Clock & Syscall Mock**| Mechanism | **Mechanism** | `CLEAN` | Interception mechanism implementing B4-17 |
| 64 | **B4-19 HITL Escalation Gateway** | Capability | **Capability** | `DUPLICATE` | Sibling to Batch 1 E8; unified into HITL Interruption |
| 65 | **B4-20 State Reversibility** | Capability | **Capability** | `DUPLICATE` | Sibling to Batch 1 E11; unified into State Reversibility |
| 66 | **B4-21 Worktree Rollback Engine** | Mechanism | **Mechanism** | `DUPLICATE MEC` | Overlaps B1-M1 / B5-05; implements Reversibility |
| 67 | **B4-22 Saga Transaction Coordinator**| Mechanism | **Mechanism** | `CLEAN` | Distributed rollback mechanism |
| 68 | **B4-23 Supply-Chain Integrity** | Capability | **Capability** | `CLEAN` | Manifest attestation & provenance verification |
| 69 | **B4-24 Sigstore / Cosign / SLSA** | Protocol & Tool | **Standard & Tool** | `CONFLATED -> FIX` | SLSA is Standard; Sigstore/Cosign are Tools |
| 70 | **B4-25 Signed Skill Manifest** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | Cryptographically signed manifest artifact |
| 71 | **B4-26 Static AST / Secret Scanner** | Mechanism | **Mechanism** | `CLEAN` | Semgrep/TruffleHog static analysis mechanism |
| **Batch 5: DX, Observability & Meta Layer (30 Candidates)** |
| 72 | **B5-01 Observability Substrate** | Substrate | **Substrate / Infra** | `CONFLATED -> FIX` | Cross-cutting OTel telemetry pipeline, NOT a Capability |
| 73 | **B5-02 Structured Spans & Traces** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | OTel trace data artifact |
| 74 | **B5-03 Micro-HUD & Statusline** | Mechanism | **Mechanism** | `CLEAN` | Terminal statusline rendering mechanism |
| 75 | **B5-04 Adaptive Output Streaming** | Mechanism | **Mechanism** | `CLEAN` | Multiplexed streaming mechanism |
| 76 | **B5-05 Workspace State Snapshots** | Mechanism | **Mechanism** | `CLEAN` | FS snapshot mechanism implementing E11/B4-20 |
| 77 | **B5-06 Trajectory Context Rewind** | Mechanism | **Mechanism** | `CLEAN` | Context truncation mechanism implementing E11 |
| 78 | **B5-07 Compensating Tool Inversion** | Mechanism | **Mechanism** | `CLEAN` | Reverse-action undo mechanism implementing E11 |
| 79 | **B5-08 Cost Ledger & Token Meter** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | Append-only token/USD ledger artifact |
| 80 | **B5-09 Real-Time Hard-Stop Gate** | Mechanism | **Mechanism** | `CLEAN` | Circuit-breaker mechanism implementing B5-25 |
| 81 | **B5-10 Headless Non-Interactive CI**| Framework/Runtime | **Runtime Mode** | `CONFLATED -> FIX` | Deployment execution mode, NOT a standalone Capability |
| 82 | **B5-11 Harness-as-Code (HaC) Spec** | Protocol/Standard | **Protocol/Standard** | `CLEAN` | Declarative YAML/JSON schema for harness configuration |
| 83 | **B5-12 HaC Schema Evolution Engine** | Mechanism | **Mechanism** | `CLEAN` | Schema migration & linting mechanism |
| 84 | **B5-13 Multi-Env Parity Synchronizer**| Mechanism | **Mechanism** | `CLEAN` | Cross-host configuration sync mechanism |
| 85 | **B5-14 Crash Resilience Supervisor**| Framework/Runtime | **Framework/Runtime** | `CLEAN` | Supervisor runtime recovering crashed processes |
| 86 | **B5-15 Agent Stall Watchdog** | Mechanism | **Mechanism** | `CLEAN` | Loop & stall detection mechanism |
| 87 | **B5-16 Evaluation & Benchmarking** | Capability | **Capability** | `CLEAN` | Empirical offline/online task evaluation |
| 88 | **B5-17 Evaluation Execution Engine** | Framework/Runtime | **Framework/Runtime** | `CLEAN` | Parallel eval orchestration runtime |
| 89 | **B5-18 Benchmark Task Suite Manifest**| Resource/Artifact | **Resource/Artifact** | `CLEAN` | Test case / Gold dataset manifest artifact |
| 90 | **B5-19 Meta-Evaluation Capability** | Capability | **Capability** | `CLEAN` | Grader/Judge validation & calibration capability |
| 91 | **B5-20 Synthetic Adversarial Synthesizer**| Mechanism | **Mechanism** | `CLEAN` | Adversarial task generation mechanism |
| 92 | **B5-21 Autonomous Self-Improvement**| Capability | **Capability** | `CLEAN` | Prompt/rule distillation from historical runs |
| 93 | **B5-22 Instinct Mining & Distillation**| Mechanism | **Mechanism** | `CLEAN` | Offline heuristic extraction mechanism |
| 94 | **B5-23 Hyperparameter Auto-Tuning** | Mechanism | **Mechanism** | `CLEAN` | Parameter search mechanism |
| 95 | **B5-24 Instinct & Rule Memory Bank** | Resource/Artifact | **Resource/Artifact** | `CLEAN` | Learned rule store artifact |
| 96 | **B5-25 Complexity Budget Enforcement**| Capability | **Capability** | `CLEAN` | System-level quotas on cost/tools/hooks/complexity |
| 97 | **B5-26 Dead Code & Rule Pruner** | Mechanism | **Mechanism** | `CLEAN` | Garbage collection mechanism |
| 98 | **B5-27 Formal Deprecation Protocol** | Protocol/Standard | **Protocol/Standard** | `CLEAN` | Lifecycle schema for capability deprecation |
| 99 | **B5-28 Hard Sunset Tombstoning** | Mechanism | **Mechanism** | `CLEAN` | Execution blocker mechanism |
| 100| **B5-29 Ergonomic CLI Shell Host** | Tool/Product/CLI | **Tool/Product/Repo** | `CONFLATED -> FIX` | TUI Product / User Interface, NOT a Capability |
| 101| **B5-30 Autonomous Harness Governance**| Capability | **Capability** | `CLEAN` | Top-level meta-eval & self-improvement governor gate |

---

## 4. The 36 Canonical Top-Level Capabilities

From the ~101 discovered candidates, exactly **36 genuine Top-Level Capabilities** emerge as the true functional specification for the AI Development Harness:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   36 CANONICAL TOP-LEVEL HARNESS CAPABILITIES                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Layer 1: Execution & Agency (7 Capabilities)                                           │
│  1. Delegated Subagent Execution (E1)                                                  │
│  2. Agent Teams & Multi-Agent Collaboration (E2)                                       │
│  3. Dynamic Orchestration & Control-Flow (E3)                                          │
│  4. Deterministic Workflow Blueprint Execution (E4)                                    │
│  5. Background & Asynchronous Queued Execution (E5)                                    │
│  6. Isolated Workspace Management (E6)                                                 │
│  7. Parallel Execution & Task Fan-Out (E9)                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Layer 2: Context, Memory & Knowledge (9 Capabilities)                                  │
│  8. Working Memory Isolation (B1)                                                      │
│  9. Context Compaction & Pinned Preservation (B2)                                      │
│ 10. Memory Consolidation & Promotion Daemon (B3)                                       │
│ 11. Relational / Bi-Temporal Knowledge Graph Memory (B4)                               │
│ 12. Semantic Response Cache (B5) [Specialized]                                         │
│ 13. Instruction-vs-Data Trust Boundary & Injection Defense (B6 / B4-12)                │
│ 14. External Retrieval (Stateless RAG) (B7)                                            │
│ 15. Memory Recall (Internal Reconstructive Experience) (B8)                            │
│ 16. Knowledge Curation & Build-Time Indexing (B9)                                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Layer 3: Integration & Extensibility (6 Capabilities)                                  │
│ 17. Procedural Skill Loading & Execution (B3-06)                                       │
│ 18. Hierarchical Rules Enforcement (B3-10)                                             │
│ 19. Lifecycle Interception & Policy Hooks (E10 / B3-13)                                 │
│ 20. Extension & Plugin Packaging (B3-16)                                               │
│ 21. Model Provider Gateway & API Abstraction (B3-18)                                   │
│ 22. Dynamic Model Routing & Cascading (B3-20)                                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Layer 4: Safety, Governance & Trust (8 Capabilities)                                   │
│ 23. Hermetic Isolated Execution (B4-01)                                                │
│ 24. Autonomy Calibration & Least-Privilege Policy (E7 / B4-04)                         │
│ 25. Human-in-the-Loop (HITL) Interruption & Approval Gates (E8 / B4-19)                 │
│ 26. Zero-Trust Secret Governance & Ephemeral Brokering (B4-08)                         │
│ 27. Execution Provenance & Immutable Audit (B4-14)                                     │
│ 28. Deterministic Execution Replayability (B4-17)                                     │
│ 29. State Reversibility & Side-Effect Compensation (E11 / B4-20)                       │
│ 30. Supply-Chain Integrity & Manifest Verification (B4-23)                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Layer 5: DX, Observability & Meta (6 Capabilities)                                     │
│ 31. Context Window Budget Governance (B2-B10)                                          │
│ 32. Harness Complexity & Financial Budget Enforcement (B5-25)                          │
│ 33. Empirical Evaluation & Task Benchmarking (B5-16)                                   │
│ 34. Meta-Evaluation & Judge Calibration (B5-19)                                        │
│ 35. Autonomous Self-Improvement & Strategy Adaptation (B5-21)                           │
│ 36. Autonomous Harness Governance (AHG) Master Gate (B5-30)                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Non-Capability Elements Summary

The remaining **65 candidate elements** do not belong in the top-level capabilities list and are mapped to their supporting abstraction tiers:

- **Protocols & Standards (7):** MCP Spec ([`B3-01`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L25)), MCP Data Primitives ([`B3-05`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L29)), Function Calling JSON Schema ([`B3-22`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L46)), Trust-Labeled Content Model (`S-B4`), SLSA Attestation Standard ([`B4-24`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md#L47)), Harness-as-Code Spec ([`B5-11`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L32)), Deprecation Protocol ([`B5-27`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L48)).
- **Mechanisms (30):** Git Worktree Isolation (`M1/S2`), Container Sandbox (`B4-02`), Progressive Disclosure (`B3-09`), Rule Dedup Traversal (`B3-12`), Deterministic Policy Gates (`B3-14`), Priority Scoping Cascade (`B3-24`), CapBAC Model (`B4-05`), Policy-as-Code Engine (`B4-06`), JIT Credential Injection (`B4-09`), DLP Masking (`B4-11`), Dual-LLM Sanitizer (`B4-13`), Flight Recorder WAL (`B4-15`), Virtual Clock Interception (`B4-18`), Saga Coordinator (`B4-22`), Static AST Scanner (`B4-26`), Statusline Projection (`B5-03`), Output Streaming (`B5-04`), FS Snapshots (`B5-05`), Context Rewind (`B5-06`), Tool Inversion (`B5-07`), Hard-Stop Gate (`B5-09`), HaC Schema Evolution (`B5-12`), Multi-Env Parity Synchronizer (`B5-13`), Loop Watchdog (`B5-15`), Adversarial Task Synthesizer (`B5-20`), Instinct Mining (`B5-22`), Prompt Auto-Tuning (`B5-23`), Rule Pruner (`B5-26`), Hard Sunset Tombstoning (`B5-28`), P0–P10 Prompt Assembly (`M-Budget-a`).
- **Frameworks & Runtimes (12):** MCP Client Subsystem (`B3-02`), MCP Server Runtime (`B3-03`), Sandbox Runtimes (gVisor/Bubblewrap/Wasmtime) (`B4-03`), Policy Runtimes (OPA/Cedar) (`B4-07`), Multi-Agent Orchestrators (LangGraph/CrewAI/AutoGen) (`F1..F3`), Memory Runtimes (Letta/Mem0/Graphiti) (`F-B3..F-B4`), Retrieval Runtimes (LlamaIndex/Haystack) (`F-B2`), Evaluation Execution Engine (`B5-17`), Crash Resilience Supervisor (`B5-14`), Headless CI Runner Mode (`B5-10`), Claude Agent SDK (`F5`), Cascade Runtime (`F7`).
- **Resources & Artifacts (9):** `SKILL.md` ([`B3-07`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L31)), `AGENTS.md` / `.cursorrules` ([`B3-11`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L35)), `hooks.json` ([`B3-15`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L39)), `plugin.json` ([`B3-17`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md#L41)), `transcript.jsonl` ([`B4-16`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md#L39)), `manifest.sig` ([`B4-25`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md#L48)), OTel Spans & Traces ([`B5-02`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L23)), Cost Ledger ([`B5-08`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L29)), Benchmark Task Manifest ([`B5-18`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md#L39)).
- **Tools, Products & Repos (7):** MCP Registries (`B3-04`), Skills Repositories (`B3-08`), Multi-Provider Proxies (LiteLLM/Portkey) (`B3-19`), Model Routers (RouteLLM/OpenRouter) (`B3-21`), Secret Vaults (Vault/AWS KMS) (`B4-10`), Sigstore/Cosign (`B4-24`), Interactive CLI Shell Host (`B5-29`).

---

## 6. Verification Sources & Grounding

The audit is grounded in and cross-verified against the converged batch slices on disk:
- [`phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md)
- [`phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md)
- [`phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md)
- [`phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md)
- [`phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md)
- [`phase-0/ARCHETYPES_AND_CRITERIA.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-0/ARCHETYPES_AND_CRITERIA.md)
- [`the harness/plan.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/plan.md)

The audited synthesis report is persisted at [`phase-1/synthesis/MASTER_D2.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/synthesis/MASTER_D2.md) for final Gate **P1-43** review and Phase 2 ranking.
