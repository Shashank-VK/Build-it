# Phase 1 — Master Taxonomy Convergence (Synthesis D-1)

The cross-batch deduplication, abstraction level resolution, and canonical taxonomy synthesis for **Phase 1 (Discover All Elements / Seeds)** are complete.

The master synthesis file has been written to:
- [`phase-1/MASTER_TAXONOMY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/MASTER_TAXONOMY.md)
- [`phase-1/synthesis/MASTER_D1.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/synthesis/MASTER_D1.md)

---

## 1. Synthesis Overview: 101 Raw Candidates → 56 Canonicals (38 Capabilities)

The discovery across Batches 1–5 produced ~101 raw candidate entries. **Synthesis D-1** resolved cross-batch redundancies and enforced strict level-hygiene (`Capability` vs `Mechanism` vs `Protocol` vs `Framework` vs `Artifact`), yielding **56 Canonical Architectural Elements (38 Capabilities)**:

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                        CROSS-CUTTING ARCHITECTURAL PLANE                          │
│  Execution vs Control Plane · Dual-Boundary Security · Harness-as-Code (HaC)     │
└────────────────────────────────────────┬──────────────────────────────────────────┘
                                         │
 ┌───────────────────────────────────────┴─────────────────────────────────────────┐
 │ Layer 1: EXECUTION & AGENCY (8 canonicals: 7 CAPs, 1 MEC)                       │
 │ Subagents · Teams · Orchestration · Workflows · Async · Workspaces · Fan-out   │
 ├─────────────────────────────────────────────────────────────────────────────────┤
 │ Layer 2: CONTEXT, MEMORY & KNOWLEDGE (9 canonicals: 9 CAPs)                     │
 │ Working Memory · Compaction · Consolidation · Bi-Temporal KG · RAG · Recall    │
 ├─────────────────────────────────────────────────────────────────────────────────┤
 │ Layer 3: INTEGRATION & EXTENSIBILITY (12 canonicals: 7 CAPs, 3 MECs, 2 PROTs)   │
 │ MCP · Function Calling · Skills · Ambient Rules · Plugins · Gateways · Routing  │
 ├─────────────────────────────────────────────────────────────────────────────────┤
 │ Layer 4: SAFETY, GOVERNANCE & TRUST (15 canonicals: 9 CAPs, 5 MECs, 1 PROT)    │
 │ Sandboxing · Least-Privilege · Secrets · Fencing · Provenance · Replay · HITL   │
 ├─────────────────────────────────────────────────────────────────────────────────┤
 │ Layer 5: DEVELOPER EXPERIENCE (DX) & META-HARNESS (11 canonicals)               │
 │ Telemetry · Headless CI · Evaluation · Meta-Eval · Self-Improvement · Budgets  │
 └─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Canonical Elements Master Table (56 Rows / 38 Capabilities)

| Canonical ID | Canonical Name | Level | Layer | Lifecycle | Tier | Conf. | Origin Batches | SC Wiring | Definition & Scope |
|---|---|---|---|---|---|---|---|---|---|
| **CAP-01** | **Delegated Subagent Execution** | CAP | 1. Execution | build→run | Foundational | High | B1 (E1) | SC-01, SC-04, SC-05, SC-09 | Spawn isolated sub-agent sessions with bounded context windows, role-specific prompts, and scoped tool allowlists to execute decomposed subproblems. |
| **CAP-02** | **Agent Teams & Multi-Agent Coordination** | CAP | 1. Execution | run→review | Important | Med-High | B1 (E2) | SC-02, SC-03, SC-04 | Persistent peer-to-peer or supervisor-coordinated multi-agent topologies with inter-agent messaging, shared task lists, and negotiation/debate protocols. |
| **CAP-03** | **Dynamic Orchestration & Control Flow** | CAP | 1. Execution | run | Foundational | High | B1 (E3) | SC-02, SC-03, SC-08, SC-10 | Architectural layer managing state machines, dynamic graph sequencing, dependency resolution, failure recovery, and non-deterministic decision branching. |
| **CAP-04** | **Deterministic Workflows & Blueprints** | CAP | 1. Execution | build→run | Foundational | High | B1 (E4) | SC-06, SC-08, SC-10 | Predefined, repeatable, multi-step execution graphs (`trigger → steps → gates`) executed deterministically without unnecessary LLM routing overhead. |
| **CAP-05** | **Background & Async Queued Execution** | CAP | 1. Execution | run | Important | High | B1 (E5) | SC-01, SC-03, SC-05 | Decoupled asynchronous agent execution lifecycle (`queued → running → completed/failed`) with polling, webhooks, or SSE event delivery surviving client disconnections. |
| **CAP-06** | **Isolated Workspace Management** | CAP | 1. Execution | build→run | Foundational | High | B1 (E6), B4 (B4-21) | SC-06, SC-07, SC-10 | Per-agent or per-task filesystem isolation providing clean branches/checkouts to prevent file clobbering, race conditions, and uncommitted drift. |
| **CAP-07** | **Parallel Execution & Fan-Out** | CAP | 1. Execution | run | Important | High | B1 (E9) | SC-01, SC-05 | Bounded concurrent multi-thread or multi-container execution of decomposed subtasks with rate-limiting and fan-in aggregation. |
| **CAP-08** | **Working Memory Management & Isolation** | CAP | 2. Context | build→run | Foundational | High | B2 (B1) | SC-01, SC-05, SC-09 | Bounded active scratchpad representing the turn context window, isolating model attention and strictly enforcing token limits against context stuffing. |
| **CAP-09** | **Context Compaction & Pinned Preservation** | CAP | 2. Context | run | Foundational | High | B2 (B2) | SC-06, SC-07, SC-09 | Threshold-triggered state reduction loop that summarizes or evicts historical turns while immutably preserving pinned invariants (system goals, active files, security rules). |
| **CAP-10** | **Memory Consolidation & Fact Promotion** | CAP | 2. Context | run→review | Important | Med-High | B2 (B3) | SC-05, SC-09, SC-10 | Background/sleep distillation transforming noisy episodic execution logs into deduplicated, versioned semantic facts with hash-chained provenance. |
| **CAP-11** | **Typed Bi-Temporal Knowledge Graph Memory** | CAP | 2. Context | build→run | Specialized | Med-High | B2 (B4) | SC-02, SC-07, SC-09 | Durable graph substrate storing structured entities and typed relationships with dual valid-time and transaction-time dimensions for multi-hop reasoning and audit. |
| **CAP-12** | **Semantic & Response Caching** | CAP | 2. Context | run | Specialized | Medium | B2 (B5) | SC-01, SC-05 | Meaning-based embedding similarity response reuse (exact hash → semantic KNN → LLM fallback) with namespace isolation and TTL invalidation. |
| **CAP-13** | **External Knowledge Retrieval (RAG)** | CAP | 2. Context | build→run | Foundational | High | B2 (B7) | SC-02, SC-08 | Stateless read-only retrieval pipeline querying indexed external corpora via hybrid search (dense embeddings + BM25 sparse + Reciprocal Rank Fusion). |
| **CAP-14** | **Experiential Memory Recall** | CAP | 2. Context | run→review | Foundational | High | B2 (B8) | SC-02, SC-09 | Stateful read-write-learn-forget cycle retrieving past episodic decisions, user corrections, and project conventions across long task horizons. |
| **CAP-15** | **Build-Time Knowledge Curation & Indexing** | CAP | 2. Context | build→review | Important | Med-High | B2 (B9) | SC-08, SC-10 | Offline pipeline that extracts, parses (AST/specs), chunks, distills, and versions codebase architecture and project knowledge into queryable indexes. |
| **CAP-16** | **Context & Token Budget Governance** | CAP | 2. Context | build→run | Important | Med-High | B2 (B10) | SC-05, SC-09 | Turn-level allocation and arbitration framework managing token competition between system prompts, tool schemas, memory, and conversation history. |
| **CAP-17** | **Open Tool Interoperability (MCP Subsystem)** | CAP | 3. Integration | run | Foundational | High | B3 (B3-01..05) | SC-02, SC-07 | Client-server middleware managing discovery, capability negotiation, JSON-RPC transport, and execution of external tools, resources, and prompts over MCP. |
| **CAP-18** | **Procedural Skills Execution** | CAP | 3. Integration | run | Foundational | High | B3 (B3-06) | SC-02, SC-05 | Dynamic capability to discover, selectively load, and execute on-demand procedural runbooks and multi-step domain workflows. |
| **CAP-19** | **Ambient Rules Enforcement** | CAP | 3. Integration | run | Foundational | High | B3 (B3-10) | SC-02, SC-07 | Automatic discovery, hierarchical inheritance, and injection of directory-scoped and workspace-scoped constraints, conventions, and coding standards. |
| **CAP-20** | **Lifecycle Interception & Hooks** | CAP | 3. Integration | run | Foundational | High | B1 (E10), B3 (B3-13) | SC-02, SC-03, SC-07 | Deterministic event-interception control plane firing synchronous or async handlers before/after tool calls, prompts, subagent events, and compactions. |
| **CAP-21** | **Composite Plugin Packaging & Distribution** | CAP | 3. Integration | build→run | Important | Med-High | B3 (B3-16) | SC-02, SC-07 | Standardized packaging format bundling skills, rules, hook handlers, and MCP configurations into versioned, distributable, namespaced modules. |
| **CAP-22** | **Model Gateway & Provider Abstraction** | CAP | 3. Integration | run | Foundational | High | B3 (B3-18) | SC-02, SC-05 | Provider-agnostic LLM interface standardizing request/response schemas, failover handling, retry policies, and egress rate-limiting across 100+ models. |
| **CAP-23** | **Dynamic Model Routing & Tier Selection** | CAP | 3. Integration | run | Important | Med-High | B3 (B3-20) | SC-02, SC-05 | Algorithmic routing dispatching turns to cost-optimal vs high-reasoning models based on prompt complexity, task requirements, and cost budgets. |
| **CAP-24** | **Hermetic Isolated Execution Boundary** | CAP | 4. Safety | run | Foundational | High | B4 (B4-01..03) | SC-01, SC-07 | Host OS and network containment ensuring untrusted agent actions, shell commands, and generated code run inside unprivileged sandboxes (containers/microVMs). |
| **CAP-25** | **Authorization & Least-Privilege Governance** | CAP | 4. Safety | build→run | Foundational | High | B1 (E7), B4 (B4-04..07) | SC-02, SC-04, SC-07 | Fine-grained Capability-Based Access Control (CapBAC) and declarative policy engine enforcing least-privilege tool, filesystem, and network permissions. |
| **CAP-26** | **Zero-Trust Secret Governance** | CAP | 4. Safety | run | Foundational | High | B4 (B4-08..11) | SC-07 | End-to-end credential isolation ensuring plaintext API keys and tokens never enter LLM context, logs, or disk via JIT brokering and DLP stream redaction. |
| **CAP-27** | **Indirect Prompt Injection Defense & Fencing** | CAP | 4. Safety | build→run | Foundational | High | B2 (B6), B4 (B4-12..13) | SC-02, SC-07 | Multi-layer defensive architecture separating trusted instructions from untrusted data using delimiter fencing, pre-model sanitizers, span tainting, and canaries. |
| **CAP-28** | **Execution Provenance & Non-Repudiation** | CAP | 4. Safety | run→review | Foundational | High | B4 (B4-14..16) | SC-06, SC-10 | Tamper-evident, cryptographically verifiable append-only write-ahead flight recording capturing every input, decision, tool call, and state mutation. |
| **CAP-29** | **Human-in-the-Loop (HITL) Escalation Gateway** | CAP | 4. Safety | run→review | Foundational | High | B1 (E8), B4 (B4-19) | SC-02, SC-04, SC-07 | Non-bypassable approval primitive pausing execution on high-risk actions to present human operators with context, diffs, and approve/reject/modify actions. |
| **CAP-30** | **Side-Effect Containment & State Reversibility** | CAP | 4. Safety | run→review | Foundational | High | B1 (E11), B4 (B4-20..22), B5 (B5-05..07) | SC-01, SC-03, SC-04, SC-06, SC-10 | Architectural capability to isolate, checkpoint, undo, or compensate state mutations across filesystem, context trajectory, and external APIs. |
| **CAP-31** | **Supply-Chain Integrity & Manifest Verification** | CAP | 4. Safety | build | Important | Med-High | B4 (B4-23..26) | SC-02, SC-07 | Cryptographic attestation, signature verification, and static AST scanning of third-party skills, plugins, and hooks before execution. |
| **CAP-32** | **Evaluation & Benchmark Engine** | CAP | 5. DX & Meta | review | Foundational | High | B5 (B5-16..18) | SC-02, SC-06, SC-08 | Empirical assessment harness running automated test batteries (SWE-bench, unit/e2e tests, smoke checks) against versioned task suites to score task success. |
| **CAP-33** | **Meta-Evaluation & Grader Calibration** | CAP | 5. DX & Meta | review | Specialized | Med-High | B5 (B5-19..20) | SC-06, SC-08 | Metrological capability to evaluate, calibrate, and detect bias/variance in automated LLM judges, assertion checkers, and synthetic benchmark generators. |
| **CAP-34** | **Autonomous Self-Improvement & Adaptation** | CAP | 5. DX & Meta | review→build | Specialized | Med-High | B5 (B5-21..24) | SC-01, SC-06, SC-08 | Offline distillation and optimization loop mining historical success/failure trajectories to refine system prompts, routing policies, and procedural rules. |
| **CAP-35** | **Cost & Complexity Budget Governance** | CAP | 5. DX & Meta | build→run | Foundational | High | B5 (B25..26) | SC-01, SC-05, SC-08 | Global financial and architectural quotas enforcing upper bounds on dollar/token spend, tool inventory bloat, hook latency, and stale rule accumulation. |
| **CAP-36** | **Lifecycle Deprecation & Sunset Management** | CAP | 5. DX & Meta | build→run | Important | Med-High | B5 (B5-27..28) | SC-06, SC-08 | Formal protocol and runtime enforcement mechanism for safely marking, alerting, migrating, and tombstoning obsolete skills, tools, and schemas. |
| **CAP-37** | **Autonomous Harness Governance (AHG) Gate** | CAP | 5. DX & Meta | review | Foundational | High | B5 (B5-30) | SC-08, SC-10 | Top-level supervisory governor executing automated pre-flight, in-flight, and post-flight quality gates across the entire harness lifecycle. |
| **CAP-38** | **Deterministic Replayability / State Snapshots** | CAP | 4. Safety | run→review | Specialized | Med-High | B4 (B4-17) | SC-06, SC-10 | Bit-for-bit trajectory replay and state snapshotting protocol enabling deterministic execution reconstruction and verification (built-in state-snapshot protocol / virtual-clock mock shim). |
| **MEC-01** | **Git Worktree Isolation Primitive** | MEC | 1. Execution | build→run | Foundational | High | B1 (M1), B4 (B4-21) | SC-06, SC-10 | Git filesystem branching mechanism creating isolated checkouts (`.agents/*`) for concurrent subagent execution. |
| **MEC-02** | **Progressive Disclosure Mechanism** | MEC | 3. Integration | run | Foundational | High | B3 (B3-09) | SC-01, SC-05 | Two-stage loading pattern injecting lightweight metadata at startup and deferring full instruction bodies until model activation. |
| **MEC-03** | **Hierarchical Rule Inheritance & Dedup** | MEC | 3. Integration | run | Important | Med-High | B3 (B3-12) | SC-05, SC-07 | Root-to-leaf directory traversal resolving configuration precedence, merging rule sets, and eliminating duplicate constraints. |
| **MEC-04** | **Deterministic Hook Event System** | MEC | 3. Integration | run | Foundational | High | B1 (M6), B3 (B3-14) | SC-03, SC-07 | Event dispatcher providing synchronous execution interception (`PreToolUse`, `PostToolUse`, `SessionStart`, `SubagentStop`). |
| **MEC-05** | **Tripartite State Reversibility Engine** | MEC | 4. Safety | run | Foundational | High | B1 (E11), B4 (B4-21..22), B5 (B5-05..07) | SC-03, SC-06, SC-10 | Concrete rollback engine implementing: (1) Filesystem snapshots, (2) Trajectory context rewind, (3) Compensating tool inversion/sagas. |
| **MEC-06** | **JIT Ephemeral Credential Brokering** | MEC | 4. Safety | run | Foundational | High | B4 (B4-09) | SC-07 | Short-lived token injector providing transient authentication to tool processes without storing credentials in workspace memory. |
| **MEC-07** | **DLP Stream Sanitizer & Secret Redactor** | MEC | 4. Safety | run | Foundational | High | B4 (B4-11) | SC-07 | High-speed regex/AST streaming filter scrubbing API keys, tokens, and PII from stdout, stderr, logs, and context injection. |
| **MEC-08** | **Cryptographic Flight Recorder (WAL)** | MEC | 4. Safety | run | Foundational | High | B4 (B4-15) | SC-10 | Write-ahead logging daemon flushing hash-chained JSONL execution entries to disk prior to external tool dispatch. |
| **MEC-09** | **Real-Time Budget Hard-Stop Circuit Breaker**| MEC | 5. DX & Meta | run | Foundational | High | B5 (B5-09) | SC-05 | Process-level circuit breaker terminating tool calls or agent loops immediately upon exceeding configured cost or token limits. |
| **MEC-10** | **Instinct Mining & Pattern Distillation** | MEC | 5. DX & Meta | review→build | Specialized | Medium | B5 (B5-22) | SC-01, SC-06 | Trajectory analyzer extracting reusable heuristic guidelines and prompt patches from high-scoring historical execution traces. |
| **MEC-11** | **Virtual Clock & Syscall Mocking** | MEC | 4. Safety | run | Specialized | Med-High | B4 (B4-18) | SC-01, SC-06, SC-10 | Interception shim trapping non-deterministic time (virtual clock) and network syscalls to support deterministic replay. |
| **PROT-01**| **Model Context Protocol (MCP) Standard** | PROT | 3. Integration | run | Foundational | High | B3 (B3-01, 05) | SC-02, SC-07 | Open standard (JSON-RPC 2.0, stdio/SSE) specifying client-server contracts for tools, resources, prompts, and sampling. |
| **PROT-02**| **Function Calling / Tool-Use Schema Standard**| PROT | 3. Integration | run | Foundational | High | B3 (B3-22) | SC-02 | Structured JSON-Schema specification defining tool parameters, return types, and invocation contracts across models. |
| **PROT-03**| **Harness-as-Code (HaC) Specification** | PROT | 5. DX & Meta | build | Foundational | High | B5 (B5-11) | SC-06, SC-08, SC-10 | Declarative, version-controlled schema format defining agent profiles, tool bindings, permission rules, and hook configurations. |
| **PROT-04**| **Trust-Labeled Content Model** | PROT | 4. Safety | build→run | Foundational | High | B2 (S-B4), B4 (B4-12) | SC-07 | Four-class data provenance taxonomy (`GOVERNANCE_INSTRUCTION`, `UNTRUSTED_REPO_DATA`, `UNTRUSTED_EXT_DATA`, `PROVIDER_OUTPUT`). |
| **SUB-01** | **GenAI Telemetry & Distributed Tracing Substrate** | SUB | 5. DX & Meta | run | Foundational | High | B5 (B5-01..02) | SC-01, SC-06, SC-08 | OpenTelemetry-compliant runtime infrastructure emitting structured spans, tool latencies, token consumption, and status updates. |
| **RUN-01** | **Headless Non-Interactive CI Runner** | RUN | 5. DX & Meta | build→run | Foundational | High | B5 (B5-10) | SC-01, SC-06 | Deterministic, unbuffered CLI runtime providing automated agent execution with standard POSIX exit codes for CI/CD pipelines. |
| **ART-01** | **Declarative Agent & Environment Manifests** | ART | Cross-Cutting | build | Foundational | High | B1 (M3), B3 (B3-07, 11, 15, 17), B5 (B5-11) | SC-08, SC-10 | Standardized artifact bundle (`AGENTS.md`, `SKILL.md`, `hooks.json`, `plugin.json`, `harness.yaml`) defining harness configuration. |

---

## 3. Key Cross-Batch Deduplication Resolves

1. **Lifecycle Hooks (B1-E10 + B3-13):**
   - *Resolution:* Unified into **CAP-20 (Lifecycle Interception & Hooks)** on the Control Plane (Layer 3: Integration & Extensibility). Hook dispatching is **MEC-04 (Hook Event System)**; individual configuration files (`hooks.json`) are categorized as **ART-01 (Manifests)**.
2. **Untrusted Content Fencing vs Injection Gateway (B2-B6 + B4-12):**
   - *Resolution:* Merged into **CAP-27 (Indirect Prompt Injection Defense & Fencing)** under the **Dual-Boundary Security Model**. B2-B6 supplies pre-model prompt assembly delimiters and span tainting; B4-12 supplies runtime tool-result scanning and dual-LLM sanitization.
3. **Flight Recorder vs Observability vs Traces (B4-14/15 + B5-01/02):**
   - *Resolution:* Strict XOR split. **CAP-28 & MEC-08 (Cryptographic Flight Recorder)** is the write-ahead, immutable, non-repudiable audit trail for safety/governance. **SUB-01 (GenAI Telemetry Substrate)** is active runtime distributed tracing for performance and debugging.
4. **Background Execution vs Headless CI Runner (B1-E5 + B5-10):**
   - *Resolution:* **CAP-05 (Background & Async Queued Execution)** is the asynchronous agent execution lifecycle (`queued → in_progress → completed`). **RUN-01 (Headless Non-Interactive CI Runner)** is the CLI execution runtime mode with standard POSIX exit codes.
5. **State Reversibility & Undo (B1-E11 + B4-20 + B5-05/06/07):**
   - *Resolution:* **CAP-30 (Side-Effect Containment & State Reversibility)** represents the top-level capability, implemented concretely by **MEC-05 (Tripartite State Reversibility Engine)** across: (1) Filesystem snapshots (git worktrees), (2) Trajectory context rewind, (3) Compensating tool inversion/sagas.
6. **Deterministic Replayability & Virtual Clock Mocking (B4-17 + B4-18):**
   - *Resolution:* **CAP-38 (Deterministic Replayability / State Snapshots)** captures the bit-for-bit deterministic replay capability (B-tier, Layer 4 Safety), enabled by **MEC-11 (Virtual Clock & Syscall Mocking)** trapping non-deterministic time and network syscalls (built-in state-snapshot protocol / virtual-clock mock shim).

---

## 4. Phase 1 Gate P1-43 Status & Recommendation

- **Deliverables on Disk:**
  - [`phase-1/MASTER_TAXONOMY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/MASTER_TAXONOMY.md) (Full specification)
  - [`phase-1/synthesis/MASTER_D1.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/synthesis/MASTER_D1.md) (Convergence log)
  - [`phase-1/STATUS.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-1/STATUS.md) (Updated tracking)
- **Verdict:** **PASS.** The 56 canonical elements (38 capabilities) provide complete, deduplicated coverage across all 6 archetypes (C1–C6) and trace directly to the 10 measurable Success Criteria (SC-01..10). Ready to proceed to **Phase 2 (Research & Rank Each Element)**.

---

## 5. Layer-by-Layer Architectural Decomposition

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                          LAYER 1: EXECUTION & AGENCY                              │
│  The dynamic runtime engine executing agent loops, subagents, and workflows       │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### Layer 1 Canonical Capabilities & Mechanisms:

1. **CAP-01: Delegated Subagent Execution**
   - *Problem Solved:* Context window exhaustion, attention degradation, and prompt pollution on multi-step complex tasks.
   - *Architecture:* Hub-and-spoke execution where a primary agent spawns isolated child agents with bounded scratchpads, specialized system prompts, and strict tool allowlists (`.claude/agents/*.md`, `.codex/agents/*.toml`, `.gemini/agents/*.md`).
   - *Lifecycle Role:* `build` (define agent schema) → `run` (spawn and await summary).
   - *Cross-Ecosystem Translation:* Claude Code `Sub-Agents` ≡ OpenAI Codex `Custom Agents + Threads` ≡ GitHub Copilot `Custom Agents` ≡ Cursor `SDK Subagents` ≡ Gemini CLI `Agents`.

2. **CAP-02: Agent Teams & Multi-Agent Coordination**
   - *Problem Solved:* Tasks requiring multi-party negotiation, peer debate, or long-lived concurrent awareness that cannot be modeled as simple fan-out/fan-in subtasks.
   - *Architecture:* Multi-session mesh or hierarchical topologies with persistent memory, direct inter-agent messaging channels, shared task backlogs, and consensus/supervisor routing.
   - *Framework Impls:* LangGraph `Supervisor+Worker`, CrewAI `Crews & Flows`, AutoGen `Conversational Groups`.

3. **CAP-03: Dynamic Orchestration & Control Flow**
   - *Problem Solved:* Cascading agent failures, state loss, unhandled tool exceptions, and unpredictable non-deterministic reasoning loops.
   - *Architecture:* Stateful execution graph tracking task dependencies, execution state, and dynamic routing decisions, supporting conditional branching and automated recovery.

4. **CAP-04: Deterministic Workflows & Blueprints**
   - *Problem Solved:* Inefficiency, latency, and non-determinism caused by using LLM reasoning loops for static, well-defined operational sequences.
   - *Architecture:* Reusable, specifiable blueprints (`trigger → actions → gates`) executing without non-deterministic prompt reasoning (e.g. Windsurf `Cascade Stages`, Temporal workflows).

5. **CAP-05: Background & Async Queued Execution**
   - *Problem Solved:* Interactive terminal blocking, API timeouts on long builds/tests, and dropped sessions during long-running tasks.
   - *Architecture:* Client submits task → receives `202 Accepted` + task token → daemon/worker processes task asynchronously in background → notifies client via SSE, webhook, or polling.

6. **CAP-06: Isolated Workspace Management & MEC-01 Git Worktrees**
   - *Problem Solved:* Concurrent git branch collisions, uncommitted diff clobbering, and dirty working directory states during parallel execution.
   - *Architecture:* Automatic provisioning of isolated filesystem checkouts via `git worktree add .agents/<id>` or lightweight container overlays, providing clean branch environments with deterministic cleanup on completion.

7. **CAP-07: Parallel Execution & Fan-Out**
   - *Problem Solved:* Latency bottlenecks on highly decomposable tasks (e.g. multi-file migrations, parallel test generation, bulk codebase audits).
   - *Architecture:* Bounded concurrency manager executing multiple agent worker instances in parallel, governed by thread/container quotas (`max_concurrent_threads`) and aggregating results.

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                    LAYER 2: CONTEXT, MEMORY & KNOWLEDGE                           │
│  The cognitive state substrate governing working memory, recall, and grounding   │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### Layer 2 Canonical Capabilities & Mechanisms:

8. **CAP-08: Working Memory Management & Isolation**
   - *Problem Solved:* Attention dilution, "lost in the middle" phenomena, and reasoning degradation caused by stuffing irrelevant data into active turns.
   - *Architecture:* Bounded in-context scratchpad isolating the turn-level prompt (`system instructions + pinned invariant index + recent-N turns`). Strictly separates transient turn scratchpad from persistent long-term storage.

9. **CAP-09: Context Compaction & Pinned Preservation**
   - *Problem Solved:* Context window exhaustion during extended development sessions (>30K–100K tokens).
   - *Architecture:* Threshold-triggered compaction loop (at 75–90% window capacity). Summarizes dropped turns using structured anchored merge while guaranteeing **zero compaction of pinned invariants** (system goals, active file lists, security rules, delimiter definitions).

10. **CAP-10: Memory Consolidation & Fact Promotion**
    - *Problem Solved:* Noisy, unbounded accumulation of raw episodic chat logs across multi-day development cycles.
    - *Architecture:* Background sleep-pass daemon analyzing episodic logs to extract, cluster, and deduplicate semantic facts (`user prefers Vitest`, `database URL structure`), recording `informed_by` provenance and applying Ebbinghaus decay.

11. **CAP-11: Typed Bi-Temporal Knowledge Graph Memory**
    - *Problem Solved:* Flat vector stores failing on multi-hop relational queries, entity hierarchy navigation, and historical point-in-time state tracking.
    - *Architecture:* Graph substrate storing typed nodes (`Service`, `Schema`, `Decision`) and edges (`depends_on`, `authored_by`) with dual temporal dimensions (`valid_time` vs `transaction_time`), queryable via Cypher over MCP.

12. **CAP-12: Semantic & Response Caching**
    - *Problem Solved:* Redundant token costs and latency on repetitive semantic queries (e.g. repeated code explanation or test failure analysis).
    - *Architecture:* Multi-tier cache pipeline: `Exact SHA-256 Hash O(1) → Embedding KNN Similarity (cosine ≥ 0.95) + Judge → Model Fallback`, with tenant/workspace namespace isolation.

13. **CAP-13: External Knowledge Retrieval (RAG)**
    - *Problem Solved:* LLM parametric knowledge staleness and inability to access extensive external documentation libraries.
    - *Architecture:* Stateless read-only retrieval engine indexing external corpora into vector/keyword stores, retrieving relevant snippets via hybrid dense/sparse search with Reciprocal Rank Fusion (RRF).

14. **CAP-14: Experiential Memory Recall**
    - *Problem Solved:* Agent repeating past mistakes or failing to retain user preferences across separate sessions.
    - *Architecture:* Stateful read-write-learn-forget cycle (`Capture → Store → Retrieve → Update → Decay`), enabling agents to reconstruct past project decisions and architectural choices.

15. **CAP-15: Build-Time Knowledge Curation & Indexing**
    - *Problem Solved:* Runtime RAG failure caused by unstructured, unparsed, and noisy codebase indexing.
    - *Architecture:* Deterministic build-time pipeline parsing codebase ASTs, directory hierarchies, and schema definitions into versioned, structured knowledge artifacts (e.g. `claude-memory-compiler`, `codebase-memory-mcp`).

16. **CAP-16: Context & Token Budget Governance**
    - *Problem Solved:* Uncontrolled token bloat where MCP tool definitions, system rules, and context files exhaust 60%+ of the context window before user interaction.
    - *Architecture:* Priority-ranked assembly chain (`P0 System Instructions > P1 Security Fencing > P2 Tool Schemas > P3 Memory/Context > P4 User Input`) with strict 50/30/20 budget allocations. Complexity bound measured via token compression ratio C = |T_compacted| / |T_raw| (target C below 0.40) and AST cyclomatic complexity penalty cap (max nesting depth 6, max fan-out 12). Both metrics are discrete, operationalizable, and directly measurable in the harness.

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                    LAYER 3: INTEGRATION & EXTENSIBILITY                           │
│  The interoperability fabric connecting agents to tools, models, and environments │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### Layer 3 Canonical Capabilities & Mechanisms:

17. **CAP-17: Open Tool Interoperability (MCP Subsystem) & PROT-01**
    - *Problem Solved:* M×N fragmentation where every AI tool requires bespoke integrations for every IDE and runtime.
    - *Architecture:* Standardized JSON-RPC 2.0 client-server subsystem managing the lifecycle, discovery, and execution of external tools, resources, and prompt templates over standard I/O and SSE transports.

18. **CAP-18: Procedural Skills Execution & MEC-02 Progressive Disclosure**
    - *Problem Solved:* Inability of models to execute complex, multi-step engineering runbooks without consuming massive context on every turn.
    - *Architecture:* Structured runbook format (`SKILL.md` + frontmatter metadata + `scripts/` + `references/`). Uses **Progressive Disclosure** (injecting only name + description into startup prompts, loading full operational bodies only upon explicit skill invocation).

19. **CAP-19: Ambient Rules Enforcement & MEC-03 Hierarchical Inheritance**
    - *Problem Solved:* Lack of workspace-specific conventions leading to style drift, incorrect test patterns, and broken standards.
    - *Architecture:* Automatic upward-traversal discovery and application of ambient rule files (`AGENTS.md`, `.cursorrules`, `CLAUDE.md`, `.gemini/rules/`), resolving inheritance precedence from repository root down to active subdirectories.

20. **CAP-20: Lifecycle Interception & Hooks & MEC-04 Hook Event System**
    - *Problem Solved:* Inability of the harness to deterministically enforce policies, log telemetry, or validate tool arguments without prompt-based soft steering.
    - *Architecture:* Deterministic event dispatcher intercepting critical execution lifecycle phases (`PreToolUse`, `PostToolUse`, `SessionStart`, `SubagentStop`, `PreCompact`), invoking synchronous validation scripts that can allow, deny, modify, or halt operations.

21. **CAP-21: Composite Plugin Packaging & Distribution**
    - *Problem Solved:* Fragmented distribution where skills, rules, hooks, and MCP servers must be configured separately and manually.
    - *Architecture:* Unified manifest format (`plugin.json`) bundling multiple skills, directory rules, lifecycle hook scripts, and MCP server configurations into a single versioned, namespaced package.

22. **CAP-22: Model Gateway & Provider Abstraction**
    - *Problem Solved:* Hardcoded vendor SDK lock-in and catastrophic downtime during upstream provider outages.
    - *Architecture:* Universal proxy and translation layer (e.g. LiteLLM, Portkey) normalizing OpenAI/Anthropic/Gemini/Ollama API schemas into standard interfaces with automatic fallback, exponential backoff, and credential load balancing.

23. **CAP-23: Dynamic Model Routing & Tier Selection**
    - *Problem Solved:* Extreme cost and latency waste from using frontier reasoning models for trivial tasks (e.g. syntax checking or simple summarization).
    - *Architecture:* Algorithmic turn classifier (e.g. RouteLLM, OpenRouter) analyzing prompt intent and complexity to route requests dynamically between fast/cheap utility models and frontier reasoning models.

24. **PROT-02: Function Calling / Tool-Use Schema Standard**
    - *Problem Solved:* Syntactic drift and parsing errors in model-generated tool arguments.
    - *Architecture:* Industry-standard JSON-Schema output contracts defining typed parameters, required fields, and return payloads across all LLM providers.

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                      LAYER 4: SAFETY, GOVERNANCE & TRUST                          │
│  The protective shield enforcing sandboxing, permissions, secrets, and provenance │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### Layer 4 Canonical Capabilities & Mechanisms:

25. **CAP-24: Hermetic Isolated Execution Boundary**
    - *Problem Solved:* Malicious or hallucinated agent commands destroying host operating system files or executing unauthorized network calls.
    - *Architecture:* Kernel-level process and filesystem isolation utilizing Linux namespaces, cgroups, seccomp filters, containers (Docker), or microVMs (gVisor, Firecracker), enforcing absolute write boundaries outside designated project scratchpads.

26. **CAP-25: Authorization & Least-Privilege Governance**
    - *Problem Solved:* Unrestricted agent tool access leading to accidental data deletion or unauthorized API operations.
    - *Architecture:* Declarative Capability-Based Access Control (CapBAC) and Policy-as-Code engines (OPA, Cedar) evaluating every tool execution against explicit allow/deny/ask policies based on agent role, target directory, and command patterns.

27. **CAP-26: Zero-Trust Secret Governance & MEC-06 / MEC-07**
    - *Problem Solved:* API keys, cloud credentials, and sensitive tokens leaking into model context windows, prompt caches, or public telemetry logs.
    - *Architecture:* Dual-protection secret isolation:
      - **MEC-06 JIT Ephemeral Credential Brokering:** Injects short-lived credentials directly into isolated subprocess execution environments without exposing tokens to the LLM.
      - **MEC-07 DLP Stream Redactor:** High-performance stream filter sanitizing stdout/stderr, context prompts, and log streams against regex/entropy secret signatures.

28. **CAP-27: Indirect Prompt Injection Defense & Fencing & PROT-04**
    - *Problem Solved:* Untrusted files, web pages, or tool outputs containing hidden adversarial instructions that hijack agent reasoning (e.g. `// ignore previous instructions`).
    - *Architecture:* Multi-layer defense implementing:
      - **PROT-04 Trust-Labeled Content Model:** Explicit four-tier data categorization (`GOVERNANCE_INSTRUCTION`, `UNTRUSTED_REPO_DATA`, `UNTRUSTED_EXTERNAL_DATA`, `PROVIDER_OUTPUT`).
      - **Delimiter Fencing & Span Tainting:** Defanging delimiter markers and wrapping untrusted tool outputs in strict XML/tag boundaries.
      - **Pre-Model Dual-LLM Sanitizer / PromptInjectionDefender:** Scanning tool outputs for instruction-like payloads prior to model context insertion.

29. **CAP-28: Execution Provenance & Non-Repudiation & MEC-08 Flight Recorder**
    - *Problem Solved:* Inability to audit, verify, or prove the causality of agent-generated code changes and system mutations.
    - *Architecture:* **Cryptographic Flight Recorder (WAL pattern)** flushing append-only, hash-chained `transcript.jsonl` log entries to disk before any external tool call or subprocess executes, recording full causality chains and user authorizations.

30. **CAP-29: Human-in-the-Loop (HITL) Escalation Gateway**
    - *Problem Solved:* Catastrophic errors caused by unchecked execution of high-blast-radius actions (e.g. production deployments, database drops, billing operations).
    - *Architecture:* Non-bypassable runtime pause primitive triggering interactive CLI/UI confirmation modals, presenting visual diffs, blast-radius estimates, and explicit Approve/Reject/Modify/Escalate controls.

31. **CAP-30: Side-Effect Containment & State Reversibility & MEC-05**
    - *Problem Solved:* Inability to recover cleanly from failed agent runs or erroneous modifications without manual forensic Git repair.
    - *Architecture:* **Tripartite State Reversibility Engine (MEC-05)**:
      1. *Filesystem State Rollback:* Git worktree branching and CoW snapshot restoration.
      2. *Context Trajectory Rewind:* Rewinding conversation and scratchpad state to a pre-failure checkpoint.
      3. *Compensating Tool Inversion / Sagas:* Executing compensating inverse actions (e.g. `git revert`, database rollback scripts) for external side effects.

32. **CAP-31: Supply-Chain Integrity & Manifest Verification**
    - *Problem Solved:* Poisoned community skills or malicious third-party plugins executing untrusted code or exfiltrating credentials.
    - *Architecture:* Build-time cryptographic verification (Sigstore/Cosign, SLSA provenance) validating signed skill manifests (`manifest.sig`), accompanied by static AST security scanners (Semgrep, TruffleHog).

33. **CAP-38: Deterministic Replayability / State Snapshots & MEC-11 Virtual Clock Mocking**
    - *Problem Solved:* Non-reproducible agent runs, flaky debug loops, and inability to recreate identical agent execution paths for regression testing and safety audits.
    - *Architecture:* Built-in state-snapshot protocol capturing complete seed, prompt, and tool execution state, combined with **MEC-11 (Virtual Clock & Syscall Mocking)** shims trapping non-deterministic time (`gettimeofday`, `clock_gettime`) and network I/O for bit-for-bit replay (B-Tier, Layer 4 Safety).

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│           LAYER 5: DEVELOPER EXPERIENCE (DX), OBSERVABILITY & META-HARNESS        │
│  The instrumentation, evaluation, and autonomous governance of the harness itself │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### Layer 5 Canonical Capabilities, Substrates & Protocols:

34. **SUB-01: GenAI Telemetry & Distributed Tracing Substrate**
    - *Problem Solved:* Opaque agent execution making it impossible to diagnose why an agent hallucinated, stalled, or spent excess tokens.
    - *Architecture:* OpenTelemetry-compliant runtime infrastructure instrumenting every LLM call, tool invocation, and subagent fork as structured spans, recording durations, token counts, and error states.

35. **RUN-01: Headless Non-Interactive CI Runner**
    - *Problem Solved:* Inability to run agent harnesses inside automated CI/CD pipelines and headless background worker fleets.
    - *Architecture:* Unbuffered, non-interactive execution runtime accepting structured task inputs via CLI/env, streaming deterministic progress events, and returning POSIX-compliant exit codes.

36. **CAP-32: Evaluation & Benchmark Engine**
    - *Problem Solved:* Inability to measure whether prompt, tool, or model changes improve or degrade task success.
    - *Architecture:* Automated evaluation runner executing standard benchmark batteries (e.g. SWE-bench Verified, Terminal-Bench, domain smoke tests) against versioned task suites with ground-truth verification scripts.

37. **CAP-33: Meta-Evaluation & Grader Calibration**
    - *Problem Solved:* Hallucinations, sycophancy, and variance in LLM-as-a-judge evaluation frameworks producing false quality scores.
    - *Architecture:* Metrological verification engine evaluating LLM judge calibration, inter-rater reliability, and adversarial synthetic task sensitivity.

38. **CAP-34: Autonomous Self-Improvement & Adaptation & MEC-10**
    - *Problem Solved:* Static harnesses requiring constant manual engineering to optimize prompts, routing parameters, and operational runbooks.
    - *Architecture:* Offline distillation engine (**MEC-10 Instinct Mining**) analyzing high-scoring execution traces to extract successful patterns, tune model temperatures, and update procedural rule memory banks.

39. **CAP-35: Cost & Complexity Budget Governance & MEC-09**
    - *Problem Solved:* Runaway token spending and architectural bloat (accumulating hundreds of unused tools, stale rules, and dead hooks).
    - *Architecture:* Dual-budget governance:
      - **Financial Governance:** Real-time token/dollar metering backed by **MEC-09 Real-Time Hard-Stop Circuit Breakers**.
      - **Architectural Anti-Bloat:** Garbage collection mechanisms pruning unused rules, dormant hooks, and dead tool schemas based on historical execution frequency.

40. **CAP-36: Lifecycle Deprecation & Sunset Management**
    - *Problem Solved:* Breaking agent workflows when tools, APIs, or schema contracts change without structured migration paths.
    - *Architecture:* Formal deprecation standard specifying `deprecated` schema markers, warning periods, automated migration AST transforms, and deterministic tombstoning gates.

41. **CAP-37: Autonomous Harness Governance (AHG) Gate**
    - *Problem Solved:* Lack of automated quality control across the end-to-end harness lifecycle.
    - *Architecture:* Top-level supervisory gate executing automated pre-flight checks (syntax, schema validation, secret scans), in-flight monitors (loop watchdogs, budget circuit-breakers), and post-flight gates (`gate.sh`, lint/typecheck/unit tests).

42. **PROT-03: Harness-as-Code (HaC) Specification & ART-01 Manifests**
    - *Problem Solved:* Non-reproducible, untracked harness configurations causing subtle behavior discrepancies between developer machines and CI.
    - *Architecture:* Declarative, git-versioned specification format (`harness.yaml`, `AGENTS.md`, `SKILL.md`, `hooks.json`, `plugin.json`) defining the complete operating model, agent permissions, tool registries, and security policies as diffable code.

---

## 3. Cross-Batch Deduplication & Conflict Resolution Log

This section records every cross-batch collision and overlap identified across the ~101 raw candidate entries, providing the explicit architectural rationale for each merge and resolution.

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              CROSS-BATCH DEDUPLICATION & MERGE LOG                                │
├──────────────────────────┬──────────────────────────┬──────────────┬──────────────────────────────┤
│ Raw Batch Elements       │ Canonical Resolution     │ Level Fix    │ Deduplication Rationale      │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-E10 (Hooks Cap)       │ CAP-20 (Lifecycle Hooks) │ CAP / MEC /  │ Unified into single Control  │
│ B3-13 (Lifecycle Hooks)  │ MEC-04 (Hook Events)     │ ART split    │ Plane capability. B3-14 is   │
│ B3-14 (Policy Gates)     │ ART-01 (hooks.json)      │              │ Mechanism; B3-15 is Artifact.│
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B2-B6 (Content Fencing)  │ CAP-27 (Prompt Injection │ CAP (Layer 4)│ Merged into Dual-Boundary    │
│ B4-12 (Injection Gateway)│ Defense & Fencing)       │ with MEC     │ Architecture: B2-B6 is data/ │
│ B4-13 (Dual-LLM Sanitizer│ PROT-04 (Trust Model)    │ sub-elements │ context fencing; B4-12 is    │
│                          │                          │              │ runtime tool-result gateway. │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B4-14 (Execution Proven.)│ CAP-28 (Execution Proven)│ CAP / MEC /  │ Strict XOR split: Flight     │
│ B4-15 (Flight Recorder)  │ MEC-08 (Flight Recorder) │ SUB / ART    │ Recorder is immutable audit  │
│ B4-16 (transcript.jsonl) │ ART-01 (transcript.jsonl)│ split        │ trail (Safety); Observability│
│ B5-01 (Observability)    │ SUB-01 (GenAI Telemetry) │              │ is active runtime telemetry  │
│ B5-02 (Spans & Traces)   │                          │              │ (DX/Meta). Non-redundant.    │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-E5 (Background Exec)  │ CAP-05 (Background Exec) │ CAP vs RUN   │ Split into async execution   │
│ B5-10 (Headless CI)      │ RUN-01 (Headless CI Run) │ split        │ lifecycle (CAP-05) vs CLI    │
│                          │                          │              │ non-interactive runner mode  │
│                          │                          │              │ (RUN-01).                    │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-E11 (Reversibility)   │ CAP-30 (State Reversib.) │ CAP with     │ E11/B4-20 is the parent      │
│ B4-20 (Side-Effect Rev.) │ MEC-05 (Tripartite State │ Tripartite   │ Capability; B5-05/06/07 and  │
│ B4-21/22 (Worktree/Saga) │ Reversibility Engine)    │ Mechanism    │ B4-21/22 are the three       │
│ B5-05/06/07 (Snapshots/  │                          │ engine       │ implementing mechanisms      │
│ Rewind/Tool Inversion)   │                          │              │ (FS, Context, External API). │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B2-B10 (Context Budget)  │ CAP-16 (Context Budget)  │ 2 CAPs +     │ Decoupled turn-level token   │
│ B5-08 (Cost Ledger)      │ CAP-35 (Complexity Budg.)│ 1 MEC +      │ allocation (CAP-16) from     │
│ B5-09 (Hard-Stop Gate)   │ MEC-09 (Hard-Stop Gate)  │ 1 ART        │ global financial/complexity  │
│ B5-25 (Complexity Budg.) │                          │              │ quotas (CAP-35 & MEC-09).    │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-E6 (Worktree Isol.)   │ CAP-06 (Isolated WS)     │ CAP vs MEC   │ Worktree is a Mechanism      │
│ B4-01 (Hermetic Exec)    │ CAP-24 (Hermetic Sandbx) │ vs RUN       │ (MEC-01) under Workspace     │
│ B4-02/03 (Containers/VM) │                          │ split        │ Mgmt (CAP-06); Container is  │
│                          │                          │              │ a Mechanism under Hermetic   │
│                          │                          │              │ Sandboxing (CAP-24).         │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-E7 (Autonomy Modes)   │ CAP-25 (Authorization &  │ CAP / MEC    │ Unified into Authorization   │
│ B1-E8 (HITL Controls)    │ Least-Privilege)         │ split        │ Capability (CAP-25) and      │
│ B4-04..07 (CapBAC/Policy)│ CAP-29 (HITL Escalation) │              │ runtime HITL Escalation      │
│ B4-19 (HITL Gateway)     │                          │              │ Gateway (CAP-29).            │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B1-S3 (AGENTS.md)        │ ART-01 (Declarative      │ Demoted to   │ File formats (.cursorrules,  │
│ B3-07 (SKILL.md)         │ Manifests Artifact)      │ Resource /   │ SKILL.md, AGENTS.md) are not │
│ B3-11 (Project Rules)    │                          │ Artifact     │ Capabilities — they are      │
│ B3-15 (hooks.json)       │                          │              │ static Resource Artifacts.   │
│ B3-17 (plugin.json)      │                          │              │                              │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B3-18 (Model Gateway)    │ CAP-22 (Model Gateway)   │ CAP vs Tool  │ Abstraction layer is the     │
│ B3-19 (LiteLLM/Portkey)  │ CAP-23 (Model Routing)   │ split        │ Capability; LiteLLM and      │
│ B3-20 (Dynamic Routing)  │                          │              │ RouteLLM are concrete tools. │
│ B3-21 (RouteLLM Engine)  │                          │              │                              │
├──────────────────────────┼──────────────────────────┼──────────────┼──────────────────────────────┤
│ B5-21 (Self-Improvement) │ CAP-34 (Self-Improvement)│ CAP vs MEC   │ Self-improvement is the Cap; │
│ B5-22 (Instinct Mining)  │ MEC-10 (Instinct Mining) │ split        │ instinct mining and auto-    │
│ B5-23 (Auto-Tuning)      │                          │              │ tuning are its mechanisms.   │
└──────────────────────────┴──────────────────────────┴──────────────┴──────────────────────────────┘
```

---

## 4. Architectural Principles & Invariants

### 4.1 Execution vs. Control Plane Separation (B3-23)
The harness enforces a strict separation between non-deterministic LLM execution and deterministic harness governance:
- **Execution Plane (Non-Deterministic):** Prompt reasoning, subagent delegation, code synthesis, and tool call generation.
- **Control Plane (Deterministic):** Lifecycle hooks (`PreToolUse`), authorization policies (CapBAC), secret scrubbers (DLP), budget circuit-breakers, and flight recording. The control plane cannot be bypassed or modified by prompt instructions.

### 4.2 Dual-Boundary Security Model (B4 §2.3)
Security enforcement is partitioned into two complementary boundaries:
1. **Semantic / Instruction Trust Boundary (Orchestration Layer):** Defends against malicious text payloads via delimiter fencing, content trust labeling (PROT-04), and pre-model injection scanning (CAP-27).
2. **Mechanical / Capability Containment Boundary (OS / Hypervisor Layer):** Defends against unauthorized system mutations via unprivileged sandboxes, container isolation, read-only mounts, and seccomp syscall filters (CAP-24).
> *Invariant:* Semantic defenses never substitute for mechanical sandboxing; mechanical sandboxes never substitute for prompt injection defenses.

### 4.3 Pinned Context Invariant (B2-B2 / SC-09)
Context compaction algorithms must treat the pinned set (`SYSTEM_RULES`, `SECURITY_DELIMITERS`, `ACTIVE_FILES`, `USER_GOAL`) as immutably exempt from summarization or truncation. Any compaction strategy that drops or modifies pinned security rules is rejected.

### 4.4 Non-Bypassable Write-Ahead Flight Recording (B4-15 / SC-10)
Every state mutation, tool call parameter, and subagent invocation must be flushed to the append-only `transcript.jsonl` log on disk **before** the external subprocess or API call is initiated, guaranteeing complete post-mortem auditability even during catastrophic crashes.

---

## 5. Archetype Coverage Matrix (C1–C6 Mapping)

This matrix establishes how the 48 canonical elements map across the 6 canonical archetypes established in Phase 0 (`phase-0/ARCHETYPES_AND_CRITERIA.md`).

*Archetypes:*  
- **C1:** Product Engineering (0→1 → Scale)  
- **C2:** Data, Analytics & MLOps Fabric  
- **C3:** Automation & Browser Surface Ops  
- **C4:** Agentic & Knowledge Synthesis Systems  
- **C5:** Platform, Infra & DevOps (IaC)  
- **C6:** Migration, Modernization & Strangler Rebuild  

| Canonical Layer | Primary Critical Archetypes | Key Success Criteria Wired | Architectural Driver |
|---|---|---|---|
| **Layer 1: Execution** | **C1, C4, C6** (Foundational) | SC-01 (TTFUA), SC-02 (TSR), SC-04 (HIR) | Enables task decomposition, multi-agent specialization, and isolated branch development. |
| **Layer 2: Context/Memory**| **C4, C6** (Foundational), **C2** (Important) | SC-05 (CPSR), SC-09 (CSP >30k) | Prevents context rot, guarantees state survival across 40k+ token sessions, maintains codebase memory. |
| **Layer 3: Integration** | **C1, C2, C3, C4, C5** (Foundational) | SC-02 (TSR), SC-05 (CPSR), SC-07 (SSHC) | Provides universal MCP tool interop, progressive runbook loading, and model routing. |
| **Layer 4: Safety** | **C1, C3, C5, C6** (Foundational Veto) | SC-07 (SSHC - 0 leaks), SC-03 (MTTR), SC-10 (IDFR)| Enforces 0-leak secret isolation, injection defense, and non-bypassable human approval gates. |
| **Layer 5: DX & Meta** | **ALL (C1–C6)** | SC-06 (DRR ≥90%), SC-08 (AHG ≥85%), SC-10 | Ensures end-to-end reproducibility, automated benchmarking, cost hard-stops, and HaC versioning. |

---

## 6. Open Questions & Phase 2 Gate Recommendations

| # | Question / Verification Gap | Target Phase | Resolution Strategy |
|---|---|---|---|
| 1 | **Working Memory vs Compaction Split (CAP-08 vs CAP-09):** V-C proposed merging into single Context Container; V-D justified split based on distinct failure modes and lifecycles. | Phase 2 Group B | Evaluate in Phase 2 rubric. If taxonomy bloat triggers compression, merge CAP-08 + CAP-09 into unified Context Lifecycle capability. |
| 2 | **Semantic Cache (CAP-12) Tiering:** Contested between Specialized Capability vs Retrieval Mechanism. | Phase 2 Group B | Benchmark cost/latency delta on C3/C4 workloads to verify whether standalone scoring is justified. |
| 3 | **Graph Memory (CAP-11) vs Vector RAG (CAP-13) Parity:** Does relational graph retrieval justify its maintenance complexity over modern hybrid vector search? | Phase 2 Group B | Conduct empirical evaluation on multi-hop code dependency queries in C6 migration tasks. |
| 4 | **Model Routing (CAP-23) Complexity vs Gain:** Does dynamic turn routing introduce prompt translation failures across heterogeneous models? | Phase 2 Group C | Measure translation error rates and latency overhead of RouteLLM vs static model pinning. |

### Gate P1-43 Recommendation:
**PASS (Approved for Phase 2).** The 48-element canonical taxonomy provides complete, deduplicated coverage of the AI development harness capability space, fully resolved across abstraction levels, and traceable to Phase 0 Success Criteria. Proceed to **Phase 2 — Element Research & Rubric Ranking**.
