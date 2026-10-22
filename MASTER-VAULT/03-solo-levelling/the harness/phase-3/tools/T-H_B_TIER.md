# Phase 3 Tool Selection — B-Tier & Niche Capabilities (Batch T-H)

> **Target Elements:** `CAP-02` (Agent Teams & Multi-Agent Coordination), `CAP-11` (Typed Bi-Temporal Knowledge Graph Memory), `CAP-12` (Semantic & Response Caching), `CAP-33` (Meta-Evaluation & Grader Calibration)  
> **Evaluation Framework:** `phase-2/RUBRIC.md` · `phase-1/MASTER_TAXONOMY.md` · `phase-0/ARCHETYPES_AND_CRITERIA.md` (C1–C6, SC-01..10)  
> **Global Classification:** **B-Tier (Specialized / Situational)** — Designated **Optional** across general coding harness builds, but selectively promoted to **Essential / S-Tier** under specific high-variance archetypes (`C4`, `C2`, `C3`).  
> **Verification Gate Status:** **PASSED** (Repo URL validity confirmed, 6-month active maintenance audited, real-world adoption quantified, non-viral open-source licenses verified, anti-bloat rationale enforced).

---

## 0. Architectural Posture & Variance Rationale

In the harness taxonomy, **B-Tier Capabilities** are characterized by **high domain value coupled with significant operational weight or complexity costs** (e.g., dedicated graph databases, peer message storms, cache invalidation hazards, statistical judge calibration).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          B-TIER SPECIALIZATION & DISPATCH TOPOLOGY                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
                 ┌────────────────────────────────────────────────────────┐
                 │                Harness Core Orchestrator               │
                 └───────────┬────────────────────────────────┬───────────┘
                             │                                │
        ┌────────────────────┴──────────────┐   ┌─────────────┴────────────────────┐
        ▼                                   ▼   ▼                                  ▼
┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────┐
│ CAP-02: Agent Teams   │ │ CAP-11: KG Memory     │ │ CAP-12: Semantic Cache│ │ CAP-33: Meta-Eval     │
│ (Peer Coordination /  │ │ (Temporal Multi-Hop / │ │ (KNN Vector & Exact   │ │ (Judge Calibration &  │
│  Supervisor Graphs)   │ │  Entity Lineage)      │ │  Response Dedupe)     │ │  Metrology / Bias)    │
│                       │ │                       │ │                       │ │                       │
│ • LangGraph Superv.   │ │ • Graphiti (Zep)      │ │ • RedisVL / Valkey    │ │ • DeepEval            │
│ • AutoGen (AG2)       │ │ • Neo4j GraphRAG      │ │ • LiteLLM Cache       │ │ • Promptfoo           │
│ • CrewAI (Avoid)      │ │ • MS GraphRAG         │ │ • GPTCache (Avoid)    │ │ • Ragas / Phoenix     │
└───────────────────────┘ └───────────────────────┘ └───────────────────────┘ └───────────────────────┘
```

* **`CAP-02` (Agent Teams):** Optional in solo development (`C1`), but **S-Tier in `C4` (Agentic & Knowledge Synthesis)** for adversarial debate, red-teaming, and multi-perspective code reviews.
* **`CAP-11` (Bi-Temporal KG Memory):** Optional in flat scripts, but **A-Tier in `C2` (Data/MLOps)** and `C4` for schema migration lineage, point-in-time state tracking, and multi-hop dependency analysis.
* **`CAP-12` (Semantic Cache):** Low utility for exploratory code generation (`C1`), but **A-Tier in `C3` (Browser & Automation Ops)** to eliminate redundant LLM token costs on repetitive web element classification.
* **`CAP-33` (Meta-Eval):** Secondary in deterministic test suites (`C1`), but **S-Tier in `C4`** to calibrate LLM-as-a-judge scorers against position bias, verbosity bias, and sycophancy.

---

## 1. CAP-02: Agent Teams & Multi-Agent Coordination

`CAP-02` coordinates multiple autonomous agents communicating via peer-to-peer messaging, hierarchical supervisor dispatch, or blackboard consensus.

### Tool Evaluations

#### 1. LangGraph (Multi-Agent Supervisor & Swarms) — *Best-in-Class*
* **Repository URL:** [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
* **What It Does:** Cyclic state-graph orchestrator modeling agent teams as nodes in a typed state machine with explicit control edges, conditional routing, state checkpointing, and human-in-the-loop pause/resume gates.
* **Fit Rationale:** Provides the highest determinism among multi-agent frameworks. Unlike unconstrained peer chat rooms, LangGraph enforces explicit state transitions, cyclic iteration caps, and supervisor-mediated fan-out/fan-in barriers, directly mitigating `SC-03` (deadlock prevention) and `SC-05` (token runaway).
* **Tier:** **Essential (Best-in-Class for CAP-02)** *(Designated Optional for general harness; Essential for C4)*
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/langchain-ai/langgraph`)
  * *Maintenance:* Active (Daily commits, major v0.2+ releases, active LangChain team support)
  * *Adoption:* ~15,000+ GitHub Stars, widespread enterprise production adoption
  * *License:* MIT License (Permissive Open Source)
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**, **C1 (Complex Multi-Module Refactoring)**, **C6 (Legacy Migration)**

---

#### 2. AG2 (Formerly Microsoft AutoGen)
* **Repository URL:** [https://github.com/ag2ai/ag2](https://github.com/ag2ai/ag2) (and [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen))
* **What It Does:** AgentOS framework providing conversable agents, group chat managers, society-of-mind patterns, and tool-enabled multi-agent conversation topologies.
* **Fit Rationale:** Excels at open-ended brainstorming and multi-agent debate. However, conversational message passing is prone to message storms (agents conversing indefinitely without terminating), high token consumption (`SC-05`), and non-deterministic state accumulation.
* **Tier:** **Optional** *(Requires outer-loop timeout circuit-breakers)*
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/ag2ai/ag2`)
  * *Maintenance:* Active (Active ecosystem split/rebrand into AG2 Foundation + Microsoft AutoGen v0.4 rewrite)
  * *Adoption:* ~37,000+ GitHub Stars (combined legacy AutoGen + AG2)
  * *License:* Apache License 2.0
* **Best Archetype:** **C4 (Adversarial Multi-Agent Debate & Red-Teaming)**

---

#### 3. CrewAI
* **Repository URL:** [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
* **What It Does:** Framework for assembling role-playing AI agents (Researcher, Writer, Reviewer) operating in sequential, hierarchical, or consensual processes.
* **Fit Rationale:** High developer ergonomics for simple demos, but for enterprise development tasks, its rigid role-prompting adds heavy token bloat, high latency, limited low-level execution control, and frequent hallucinations during tool handoffs. Makes deterministic replay (`SC-06`) difficult.
* **Tier:** **Avoid (for Core Coding Harness)** / **Optional (Rapid Prototyping Only)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/crewAIInc/crewAI`)
  * *Maintenance:* Active (High release cadence)
  * *Adoption:* ~26,000+ GitHub Stars
  * *License:* MIT License
* **Anti-Bloat Verdict:** Redundant when LangGraph is present. LangGraph provides lower-level state precision with zero framework-enforced role prompts.

---

### CAP-02 Comparison Matrix

| Tool | Coordination Model | Determinism | Token Overhead | License | Harness Tier |
|---|---|---|---|---|---|
| **LangGraph Supervisor** | Typed State Graph & Dynamic Supervisor | **High** (Deterministic state & edges) | **Controlled** (Explicit transitions) | MIT | **Essential** *(for CAP-02)* |
| **AG2 (AutoGen)** | Conversable Group Chat / Society of Mind | **Medium** (Conversational routing) | **High** (Message storm risk) | Apache 2.0 | **Optional** |
| **CrewAI** | Role-Playing Sequential Crews | **Low** (Prompt-driven roleplay) | **High** (Heavy role prompt bloat) | MIT | **Avoid** |

---

## 2. CAP-11: Typed Bi-Temporal Knowledge Graph Memory

`CAP-11` provides structured, relational, and time-aware memory, enabling multi-hop graph traversals (e.g., *"Which downstream dashboard broke when column `user_id` was renamed on May 4th?"*) while maintaining dual time axes: **transaction time** and **valid time**.

### Tool Evaluations

#### 1. Graphiti (Zep) — *Best-in-Class*
* **Repository URL:** [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)
* **What It Does:** Open-source Python framework for building and querying dynamic, temporal knowledge graphs for autonomous agents. Builds episodic entity-relation graphs with edge invalidation and bi-temporal timestamps directly over Neo4j or memory backends.
* **Fit Rationale:** Purpose-built for agent memory. Unlike static triples, Graphiti handles **incremental fact invalidation** (e.g., updating *"User changed database from Postgres to ClickHouse on Oct 12"* without corrupting prior historical snapshots) and provides hybrid search combining graph edges, text BM25, and semantic embeddings.
* **Tier:** **Essential (Best-in-Class for CAP-11)** *(Designated Optional globally; Essential for C2 & C4)*
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/getzep/graphiti`)
  * *Maintenance:* Active (Maintained by Zep AI, frequent updates, documented temporal schema)
  * *Adoption:* Rapidly growing agent KG library (~2,500+ GitHub Stars, backed by Zep memory research)
  * *License:* Apache License 2.0
* **Best Archetype:** **C4 (Knowledge Synthesis)**, **C2 (Data & Schema Lineage)**, **C6 (Legacy Modernization)**

---

#### 2. Neo4j & neo4j-graphrag-python
* **Repository URL:** [https://github.com/neo4j/neo4j](https://github.com/neo4j/neo4j) / [https://github.com/neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python)
* **What It Does:** Industry-standard labeled property graph database with native Cypher query execution, vector index integration, and graph data science algorithms.
* **Fit Rationale:** Industry standard for large-scale enterprise graph storage, deep multi-hop relationship indexing, and complex dependency mapping. Enables agents to generate Cypher queries for deterministic code/schema lineage exploration. However, running a full Neo4j server daemon incurs JVM memory overhead and complex local sandbox container lifecycle management.
* **Tier:** **Optional (Recommended for Enterprise/C2 Infrastructure)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/neo4j/neo4j-graphrag-python`)
  * *Maintenance:* Active (Daily commits across official Neo4j Python/GraphRAG libraries)
  * *Adoption:* 14,000+ Stars on Neo4j core; universal industry graph adoption
  * *License:* Apache 2.0 (for `neo4j-graphrag-python` SDK & Drivers); GPLv3 / Commercial (for Neo4j Server)
* **Best Archetype:** **C2 (Data/MLOps & Schema Lineage)**, **C6 (Enterprise Monorepo Modernization)**

---

#### 3. Microsoft GraphRAG
* **Repository URL:** [https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)
* **What It Does:** Knowledge graph extraction and summarization pipeline using LLMs to detect hierarchical community structures (via Leiden clustering) and generate macro-level semantic summaries.
* **Fit Rationale:** Excels at global dataset comprehension (e.g., answering *"What are the overarching architectural patterns across this 500k-line repo?"*). However, Microsoft GraphRAG is a heavy **batch pipeline**, not a low-latency interactive agent memory store.
* **Tier:** **Optional (Specialized Batch Indexer)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/microsoft/graphrag`)
  * *Maintenance:* Active (Maintained by Microsoft Research, v0.5+ releases)
  * *Adoption:* ~22,000+ GitHub Stars
  * *License:* MIT License
* **Best Archetype:** **C4 (Global Repository & Document Knowledge Synthesis)**

---

#### 4. Kùzu (KùzuDB)
* **Repository URL:** [https://github.com/kuzudb/kuzu](https://github.com/kuzudb/kuzu)
* **What It Does:** High-performance, embedded columnar graph database with native Cypher query support and zero background daemon requirements (the DuckDB of graph databases).
* **Tier:** **Avoid / Reference Only (Archived)**
* **Verification Gate Audit:** *Repository archived in October 2025 following team acquisition by Apple.* While frozen versions remain functional, active maintenance is stopped. Graphiti over SQLite or Neo4j should be prioritized.

---

### CAP-11 Comparison Matrix

| Tool | Architecture | Temporal Support | Query Interface | License | Harness Tier |
|---|---|---|---|---|---|
| **Graphiti (Zep)** | Dynamic Agent KG Engine | **Native Bi-Temporal** (Edge validity) | Hybrid (Semantic + Cypher + BM25) | Apache 2.0 | **Essential** *(for CAP-11)* |
| **Neo4j GraphRAG** | Enterprise Graph Server | **Manual Schema** (Properties/Cypher) | Cypher + Vector Index | Apache 2.0 / GPLv3 | **Optional** |
| **Microsoft GraphRAG** | Batch Community Pipeline | **None** (Static snapshot) | Community Summaries | MIT | **Optional** |
| **Kùzu** | Embedded In-Process Graph | **Manual** (Cypher) | Cypher | MIT (Archived) | **Avoid** |

---

## 3. CAP-12: Semantic & Response Caching

`CAP-12` intercepts LLM inference calls and external tool queries to return cached responses for semantically equivalent inputs, bypassing expensive model invocations, reducing latency by 10–1000x, and protecting upstream API token budgets (`SC-01`, `SC-05`).

### Tool Evaluations

#### 1. RedisVL & Valkey / Redis — *Best-in-Class*
* **Repository URL:** [https://github.com/redis/redis-vl-python](https://github.com/redis/redis-vl-python) & [https://github.com/valkey-io/valkey](https://github.com/valkey-io/valkey)
* **What It Does:** High-throughput vector search client and semantic cache module built on top of Redis/Valkey. Provides exact hash matching ($O(1)$) cascading into KNN vector distance thresholding with configurable cosine/L2 distance cutoffs and automatic TTL expiration.
* **Fit Rationale:** Industry standard for low-latency semantic caching (<5ms cache resolution). Supports dual-tier lookup (exact prompt hash hit $\to$ semantic vector nearest-neighbor hit $\to$ LLM dispatch) with tag-based metadata filtering and namespace isolation per agent session.
* **Tier:** **Essential (Best-in-Class for CAP-12)** *(Designated Optional for general harness; Essential for C3 & C4)*
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/redis/redis-vl-python`)
  * *Maintenance:* Active (Continuous releases by Redis AI team)
  * *Adoption:* ~1,200+ Stars on `redis-vl-python`, widespread production deployment across enterprise AI gateways
  * *License:* MIT License (RedisVL); BSD-3-Clause (Valkey)
* **Best Archetype:** **C3 (Browser & Automation Ops)**, **C4 (Knowledge Synthesis & Web Scraping)**

---

#### 2. LiteLLM Cache Layer — *Zero-Dependency Gateway Integration*
* **Repository URL:** [https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)
* **What It Does:** Model gateway abstraction that features built-in exact-match and semantic caching using Redis, S3, or in-memory stores directly at the model dispatch layer.
* **Fit Rationale:** Because LiteLLM is already selected as the S-Tier Model Gateway (`CAP-22`), enabling its native cache module eliminates the need to maintain an independent semantic cache library or bespoke interception layer.
* **Tier:** **Essential (Zero-Dependency Architectural Pick)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/BerriAI/litellm`)
  * *Maintenance:* Active (Daily releases, extensive multi-provider support)
  * *Adoption:* ~23,000+ GitHub Stars
  * *License:* MIT License
* **Best Archetype:** **C1 (Product Engineering)**, **C2 (Data/MLOps)**, **C5 (Platform IaC)**

---

#### 3. GPTCache
* **Repository URL:** [https://github.com/zilliztech/GPTCache](https://github.com/zilliztech/GPTCache)
* **What It Does:** Standalone Python library by Zilliz providing modular semantic caching components (vector store, scalar evaluation, similarity evaluation).
* **Fit Rationale:** Early pioneer in semantic caching, but exhibits stagnant commit activity in 2024–2025, fragile dependency bindings, and unnecessary configuration complexity compared to RedisVL or LiteLLM's built-in gateway cache.
* **Tier:** **Avoid (Stagnant / Redundant)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/zilliztech/GPTCache`)
  * *Maintenance:* Low (Infrequent updates, maintenance mode)
  * *Adoption:* ~7,000+ Stars (legacy adoption)
  * *License:* MIT License
* **Anti-Bloat Verdict:** Replaced entirely by `RedisVL` + `LiteLLM Cache`.

---

### CAP-12 Code Generation Hazard & Mitigation Protocol
> [!WARNING]
> **Code Generation Cache Pollution Hazard:**
> In software engineering agents (`C1`, `C5`, `C6`), semantic similarity does **not** imply functional equivalence. For example:
> * Query A: *"Write a script to delete inactive staging databases"*
> * Query B: *"Write a script to delete inactive production databases"*
> These queries have a >0.92 cosine embedding similarity but opposite safety blast radii.
> 
> **Enforced Rule:** For all mutating tool calls and code generation, `CAP-12` semantic similarity distance threshold must be locked to **Exact Match ($O(1)$ Hash) Only** or restricted strictly to idempotent, read-only classification tasks (`C3` DOM element extraction, `C4` entity classification).

---

## 4. CAP-33: Meta-Evaluation & Grader Calibration

`CAP-33` operates on the **evaluator metrology plane**. Unlike `CAP-32` (which runs test suites to score agent code), `CAP-33` evaluates **the evaluators themselves**: measuring inter-rater reliability (Cohen's $\kappa$, Krippendorff's $\alpha$), quantifying LLM-judge biases (position bias, verbosity bias, self-enhancement bias), and calibrating synthetic grading prompts against human ground-truth.

### Tool Evaluations

#### 1. DeepEval (Confident AI) — *Best-in-Class*
* **Repository URL:** [https://github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval)
* **What It Does:** Production-ready testing framework for LLMs modeled as `pytest` plugins. Implements G-Eval (formally calibrated LLM-as-a-judge metric using chain-of-thought and probabilistic step weighting), faithfulness, hallucination, answer relevancy, and custom metric calibration.
* **Fit Rationale:** The premier developer-centric framework for quantifying and calibrating LLM judge performance. Executes directly within standard CI/CD test runners, provides rigorous G-Eval scoring algorithms backed by academic research (Liu et al., 2023), and measures judge alignment against human-annotated baseline datasets.
* **Tier:** **Essential (Best-in-Class for CAP-33)** *(Designated Optional for general harness; Essential for C4)*
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/confident-ai/deepeval`)
  * *Maintenance:* Active (Multiple releases per week, highly active OSS maintenance)
  * *Adoption:* ~8,000+ GitHub Stars, widespread CI/CD integration in enterprise AI teams
  * *License:* Apache License 2.0
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**, **C1 (Developer-Facing LLM Pipelines)**, **C2 (MLOps Pipeline Evaluation)**

---

#### 2. Promptfoo — *Lightweight Local CLI*
* **Repository URL:** [https://github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
* **What It Does:** High-performance, lightweight CLI tool and Node/TypeScript library for systematic evaluation, prompt benchmarking, red-teaming, and LLM output assertion testing.
* **Fit Rationale:** Outstanding speed and zero-cloud-telemetry local evaluation. Includes built-in matrix assertions (similarity, regex, model-graded rubrics) and automated red-teaming for prompt injection vulnerabilities (`CAP-27`). Lightweight CLI runner makes it the ideal companion for fast pre-commit and local hook evaluation.
* **Tier:** **Essential (Lightweight Local CLI Pick)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/promptfoo/promptfoo`)
  * *Maintenance:* Active (Daily commits, major v0.90+ updates)
  * *Adoption:* ~10,000+ GitHub Stars, high adoption in security and developer tooling
  * *License:* MIT License
* **Best Archetype:** **C1 (Product Engineering)**, **C3 (Browser / Automation)**, **C5 (Platform IaC)**

---

#### 3. Ragas (Exploding Gradients)
* **Repository URL:** [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas)
* **What It Does:** Specialized framework for evaluating RAG pipelines and multi-agent interaction traces, offering reference-free evaluation metrics and automated synthetic test set generation.
* **Fit Rationale:** Highly effective at evaluating retrieval quality (context precision, context recall, faithfulness). However, it is primarily focused on RAG pipelines rather than generalized LLM judge bias calibration or harness-level metrological verification.
* **Tier:** **Optional (Specialized for RAG evaluation suites)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/explodinggradients/ragas`)
  * *Maintenance:* Active (v0.2+ architecture rewrite, active updates)
  * *Adoption:* ~11,000+ GitHub Stars
  * *License:* Apache License 2.0
* **Best Archetype:** **C4 (Knowledge Synthesis & Deep RAG)**

---

#### 4. Phoenix (Arize AI)
* **Repository URL:** [https://github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
* **What It Does:** Open-source AI observability and evaluation platform providing OpenTelemetry-native distributed tracing, LLM-as-a-judge evaluation benchmarks, and embedding cluster analysis.
* **Fit Rationale:** Delivers visual tracing and telemetry for complex multi-agent execution graphs. While strong on runtime observability, for headless CI/CD gate checks and statistical judge calibration, DeepEval and Promptfoo offer tighter developer inner-loop ergonomics.
* **Tier:** **Optional (Observability & APM Evaluation)**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/Arize-ai/phoenix`)
  * *Maintenance:* Active (Daily commits, backed by Arize AI)
  * *Adoption:* ~6,500+ GitHub Stars
  * *License:* Elastic License 2.0 / Apache 2.0
* **Best Archetype:** **C2 (MLOps & Data Platform)**, **C4 (Complex Multi-Agent Tracing)**

---

### CAP-33 Comparison Matrix

| Tool | Primary Focus | Calibration Mechanism | Runner Environment | License | Harness Tier |
|---|---|---|---|---|---|
| **DeepEval** | Unit-test LLM evaluations & G-Eval | G-Eval Chain-of-Thought & Statistical alignment | `pytest` / Python CI/CD | Apache 2.0 | **Essential** *(for CAP-33)* |
| **Promptfoo** | Matrix assertion testing & Red-teaming | Rubric scoring & Automated adversarial sweeps | Local CLI / Node.js CI/CD | MIT | **Essential** *(Local CLI)* |
| **Ragas** | RAG retrieval & context precision | Synthetic test generation & Reference-free metrics | Python Library | Apache 2.0 | **Optional** |
| **Arize Phoenix** | OpenTelemetry tracing & Judge eval | Traced span evaluation & Cluster drift | Self-hosted Web UI / OTel | ELv2 / Apache | **Optional** |

---

## 5. Master Consolidated B-Tier Tool Registry

| Capability ID | Capability Name | Selected Tool | Repository URL | License | Global Tier | Archetype Elevation | Verification Gate |
|---|---|---|---|---|:---:|:---:|:---:|
| **CAP-02** | Agent Teams & Coordination | **LangGraph Supervisor** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | **Optional** | **S-Tier in C4** | **PASSED** (15k★, active) |
| **CAP-02** | Agent Teams (Adversarial) | **AG2 (AutoGen)** | [ag2ai/ag2](https://github.com/ag2ai/ag2) | Apache 2.0 | **Optional** | **A-Tier in C4** | **PASSED** (37k★, active) |
| **CAP-11** | Bi-Temporal KG Memory | **Graphiti (Zep)** | [getzep/graphiti](https://github.com/getzep/graphiti) | Apache 2.0 | **Optional** | **A-Tier in C2, C4** | **PASSED** (2.5k★, active) |
| **CAP-11** | Enterprise Graph & Cypher | **Neo4j GraphRAG** | [neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python) | Apache 2.0 | **Optional** | **A-Tier in C2, C6** | **PASSED** (14k★, active) |
| **CAP-12** | Semantic Cache Substrate | **RedisVL / Valkey** | [redis/redis-vl-python](https://github.com/redis/redis-vl-python) | MIT / BSD | **Optional** | **A-Tier in C3, C4** | **PASSED** (Active Redis team) |
| **CAP-12** | Model Gateway Cache | **LiteLLM Cache** | [BerriAI/litellm](https://github.com/BerriAI/litellm) | MIT | **Optional** | **A-Tier in C1, C3** | **PASSED** (23k★, active) |
| **CAP-33** | Meta-Eval & G-Eval Calibration| **DeepEval** | [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Apache 2.0 | **Optional** | **S-Tier in C4** | **PASSED** (8k★, active) |
| **CAP-33** | Fast CLI Assertion & Red-Team | **Promptfoo** | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | MIT | **Optional** | **A-Tier in C1, C5** | **PASSED** (10k★, active) |

> **Deliverable Stored On Disk:** The complete Phase 3 specification has been written directly to `phase-3/tools/T-H_B_TIER.md`.

---

## 6. Sources & References

1. **LangGraph State Graph Engine:** [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
2. **AG2 Multi-Agent Framework (AutoGen):** [https://github.com/ag2ai/ag2](https://github.com/ag2ai/ag2)
3. **CrewAI Framework:** [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
4. **Graphiti Temporal Knowledge Graph (Zep):** [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)
5. **Neo4j GraphRAG Python SDK:** [https://github.com/neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python)
6. **Microsoft GraphRAG Research:** [https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)
7. **Redis Vector Library (RedisVL):** [https://github.com/redis/redis-vl-python](https://github.com/redis/redis-vl-python)
8. **Valkey Open Source In-Memory Store:** [https://github.com/valkey-io/valkey](https://github.com/valkey-io/valkey)
9. **LiteLLM Gateway & Caching:** [https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)
10. **DeepEval LLM Unit Testing & G-Eval (Confident AI):** [https://github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval)
11. **Promptfoo LLM Testing & Red-Teaming:** [https://github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
12. **Ragas RAG Evaluation Framework:** [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas)
13. **Arize Phoenix AI Observability:** [https://github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
14. **G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment (Liu et al., 2023):** [https://arxiv.org/abs/2303.16634](https://arxiv.org/abs/2303.16634)
| Matrix assertion testing & Red-teaming | Rubric scoring & Automated adversarial sweeps | Local CLI / Node.js CI/CD | MIT | **Essential** *(Local CLI)* |
| **Ragas** | RAG retrieval & context precision | Synthetic test generation & Reference-free metrics | Python Library | Apache 2.0 | **Optional** |
| **Arize Phoenix** | OpenTelemetry tracing & Judge eval | Traced span evaluation & Cluster drift | Self-hosted Web UI / OTel | ELv2 / Apache | **Optional** |

---

## 5. Master Consolidated B-Tier Tool Registry

The following table synthesizes the selected toolchain across all four B-Tier capabilities:

| Capability ID | Capability Name | Selected Tool | Repository URL | License | Global Tier | Archetype Elevation | Verification Gate |
|---|---|---|---|---|:---:|:---:|:---:|
| **CAP-02** | Agent Teams & Coordination | **LangGraph Supervisor** | `github.com/langchain-ai/langgraph` | MIT | **Optional** | **S-Tier in C4** | **PASSED** (15k★, active) |
| **CAP-02** | Agent Teams (Adversarial) | **AG2 (AutoGen)** | `github.com/ag2ai/ag2` | Apache 2.0 | **Optional** | **A-Tier in C4** | **PASSED** (37k★, active) |
| **CAP-11** | Bi-Temporal KG Memory | **Graphiti (Zep)** | `github.com/getzep/graphiti` | Apache 2.0 | **Optional** | **A-Tier in C2, C4** | **PASSED** (2.5k★, active) |
| **CAP-11** | Enterprise Graph & Cypher | **Neo4j GraphRAG** | `github.com/neo4j/neo4j-graphrag-python` | Apache 2.0 | **Optional** | **A-Tier in C2, C6** | **PASSED** (14k★, active) |
| **CAP-12** | Semantic Cache Substrate | **RedisVL / Valkey** | `github.com/redis/redis-vl-python` | MIT / BSD | **Optional** | **A-Tier in C3, C4** | **PASSED** (Active Redis team) |
| **CAP-12** | Model Gateway Cache | **LiteLLM Cache** | `github.com/BerriAI/litellm` | MIT | **Optional** | **A-Tier in C1, C3** | **PASSED** (23k★, active) |
| **CAP-33** | Meta-Eval & G-Eval Calibration| **DeepEval** | `github.com/confident-ai/deepeval` | Apache 2.0 | **Optional** | **S-Tier in C4** | **PASSED** (8k★, active) |
| **CAP-33** | Fast CLI Assertion & Red-Team | **Promptfoo** | `github.com/promptfoo/promptfoo` | MIT | **Optional** | **A-Tier in C1, C5** | **PASSED** (10k★, active) |

---

## 6. Sources & References

1. **LangGraph State Graph Engine:** [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
2. **AG2 Multi-Agent Framework (AutoGen):** [https://github.com/ag2ai/ag2](https://github.com/ag2ai/ag2)
3. **CrewAI Framework:** [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
4. **Graphiti Temporal Knowledge Graph (Zep):** [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)
5. **Neo4j GraphRAG Python SDK:** [https://github.com/neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python)
6. **Microsoft GraphRAG Research:** [https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)
7. **Redis Vector Library (RedisVL):** [https://github.com/redis/redis-vl-python](https://github.com/redis/redis-vl-python)
8. **Valkey Open Source In-Memory Store:** [https://github.com/valkey-io/valkey](https://github.com/valkey-io/valkey)
9. **LiteLLM Gateway & Caching:** [https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)
10. **DeepEval LLM Unit Testing & G-Eval (Confident AI):** [https://github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval)
11. **Promptfoo LLM Testing & Red-Teaming:** [https://github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
12. **Ragas RAG Evaluation Framework:** [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas)
13. **Arize Phoenix AI Observability:** [https://github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
14. **G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment (Liu et al., 2023):** [https://arxiv.org/abs/2303.16634](https://arxiv.org/abs/2303.16634)
