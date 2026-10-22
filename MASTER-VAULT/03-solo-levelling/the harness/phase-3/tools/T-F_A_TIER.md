# Phase 3 Tool Selection Report — A-Tier Capabilities

> **Document Type:** Tool Evaluation & Architecture Integration Report  
> **Evaluation Scope:** `CAP-05` (Background/Async), `CAP-10` (Memory Consolidation), `CAP-14` (Experiential Recall), `CAP-16` (Budget Governance), `CAP-23` (Model Routing)  
> **Target Archetypes:**  
> - **`C1`**: Single-Turn CLI / Ephemeral Developer Tool  
> - **`C2`**: Autonomous Code Worker / Repository Refactoring  
> - **`C3`**: Long-Horizon Background Agent / Async CI/CD & Pipeline  
> - **`C4`**: Interactive Multi-Turn Coding Environment (IDE / REPL)  
> - **`C5`**: Multi-Agent Swarm / Distributed System  
> - **`C6`**: Autonomous Production Ops / SRE Diagnostic Agent  

---

## Executive Summary & Selection Methodology

A-Tier capabilities bridge the gap between reactive single-loop LLM interactions and resilient, cost-governed autonomous agents. To equip these capabilities without introducing latency degradation, vendor lock-in, or maintenance traps, tools are evaluated across five mechanical criteria:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    VERIFICATION GATE CRITERIA                                   │
│  1. Architecture & Latency Fit  ──►  2. Maintenance Cadence  ──►  3. Adoption & Ecosystem       │
│  4. OSS License / Compliance    ──►  5. Archetype Suitability (C1–C6) ──► Final Tiering         │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Classification Tiers
- 🟢 **Essential**: Foundational core; zero-compromise baseline for target archetypes.
- 🟡 **Optional**: Specialized or scale-dependent; recommended only for high-complexity, distributed setups.
- 🔴 **Avoid**: Anti-pattern for developer-agent harnesses due to licensing restrictions, GUI-coupled runtimes, or excessive architectural bloat.

---

## 1. CAP-05: Background & Async Task Execution / Workflows

| Tool | Repo / URL | Tier | License | Primary Archetypes |
| :--- | :--- | :--- | :--- | :--- |
| **Temporal** | [temporalio/temporal](https://github.com/temporalio/temporal) | 🟢 **Essential** *(C3, C5, C6)* | MIT | `C3`, `C5`, `C6` |
| **Trigger.dev (v3)** | [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | 🟢 **Essential** *(C2, C3, C4)* | Apache-2.0 | `C2`, `C3`, `C4` |
| **Prefect** | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | 🟡 **Optional** | Apache-2.0 | `C3`, `C5` |
| **n8n** | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 🔴 **Avoid** | Sustainable Use License (Fair-code) | None (Harness Anti-pattern) |

---

### Tool Evaluations: CAP-05

#### 1. Temporal
- **Repository:** [`https://github.com/temporalio/temporal`](https://github.com/temporalio/temporal)
- **Architectural Fit:** Temporal provides deterministic event-sourcing and durable execution. Workflows withstand process restarts, network outages, and multi-day human-in-the-loop pauses without losing state. It offers polyglot SDKs (Go, TypeScript, Python, Java) and deterministic replay, making it ideal for distributed agent orchestration and mission-critical SRE workflows.
- **Verification Gate:**
  - *Link / Maintenance:* Actively maintained by Temporal Technologies; daily commits; frequent enterprise releases.
  - *Adoption:* 12k+ GitHub stars; industry-standard at Uber, Stripe, Netflix, Datadog.
  - *License:* MIT License (Server & SDKs).
- **Archetype Fit:** `C3` (Long-Horizon), `C5` (Swarms), `C6` (Production Ops).
- **Recommendation:** 🟢 **Essential** for high-reliability, long-running agent workflows requiring distributed durability.

#### 2. Trigger.dev (v3)
- **Repository:** [`https://github.com/triggerdotdev/trigger.dev`](https://github.com/triggerdotdev/trigger.dev)
- **Architectural Fit:** Purpose-built for developers building background tasks with zero serverless timeouts (runs up to hours), real-time log streaming, checkpointing, and native TypeScript/Python task wrappers. Its low cognitive overhead makes it the best developer-facing async job runner for IDEs and CLI agents.
- **Verification Gate:**
  - *Link / Maintenance:* Rapid release cadence (v3 engine written in Rust/Node); weekly updates.
  - *Adoption:* 10k+ GitHub stars; strong traction among modern full-stack and AI agent startups.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C2` (Autonomous Worker), `C3` (Background Pipelines), `C4` (Interactive IDE/CLI).
- **Recommendation:** 🟢 **Essential** for lightweight, code-first background task dispatch in developer environments.

#### 3. Prefect
- **Repository:** [`https://github.com/PrefectHQ/prefect`](https://github.com/PrefectHQ/prefect)
- **Architectural Fit:** Python-native workflow engine with `@flow` and `@task` decorators. Features dynamic task generation, native `asyncio` integration, and state inspection. While flexible for data pipelines and Python-centric agent execution, it introduces heavier orchestration overhead compared to Trigger.dev and lacks Temporal's strict replay determinism.
- **Verification Gate:**
  - *Link / Maintenance:* Active maintenance by PrefectHQ; mature 3.x release series.
  - *Adoption:* 17k+ GitHub stars; broad data engineering and ML ecosystem footprint.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C3` (Long-Horizon Batch), `C5` (Python Swarms).
- **Recommendation:** 🟡 **Optional** — Preferred if the agent harness is exclusively Python and already leverages Prefect for ML pipelines.

#### 4. n8n
- **Repository:** [`https://github.com/n8n-io/n8n`](https://github.com/n8n-io/n8n)
- **Architectural Fit:** Visual node-based workflow automation. Excellent for non-technical low-code integrations, but poorly suited as an embedded capability engine for programmatic agent harnesses. It forces visual DAG paradigms, introduces massive container memory footprints, and creates impedance mismatch with code-first tool invocation.
- **Verification Gate:**
  - *Link / Maintenance:* Actively maintained.
  - *Adoption:* 55k+ GitHub stars.
  - *License:* Sustainable Use License (Fair-code / restrictive commercial redistribution).
- **Archetype Fit:** Avoid for all programmatic agent harnesses (`C1`–`C6`).
- **Recommendation:** 🔴 **Avoid** — Anti-pattern for developer agent harnesses; licensing and visual-first design impede embedding.

---

## 2. CAP-10: Memory Consolidation & State Management

| Tool | Repo / URL | Tier | License | Primary Archetypes |
| :--- | :--- | :--- | :--- | :--- |
| **Mem0** | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 🟢 **Essential** *(C1, C2, C4)* | Apache-2.0 | `C1`, `C2`, `C4`, `C5` |
| **Letta (formerly MemGPT)** | [letta-ai/letta](https://github.com/letta-ai/letta) | 🟢 **Essential** *(C2, C3, C4)* | Apache-2.0 | `C2`, `C3`, `C4` |
| **LangMem** | [langchain-ai/langmem](https://github.com/langchain-ai/langmem) | 🟡 **Optional** | MIT | `C4`, `C5` |
| **Zep / Graphiti** | [getzep/graphiti](https://github.com/getzep/graphiti) | 🟡 **Optional** | Apache-2.0 | `C3`, `C5`, `C6` |

---

### Tool Evaluations: CAP-10

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   MEMORY CONSOLIDATION TOPOLOGY                                  │
│  Episodic Traces (Raw Run)  ──►  Mem0 / Letta Extractor  ──►  Semantic/Graph Store (Graphiti)    │
│  Working Window (Prompt)    ◄──  Tiered Memory Consolidation (Core vs Archival vs Recall)        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 1. Mem0 (Universal Memory Layer)
- **Repository:** [`https://github.com/mem0ai/mem0`](https://github.com/mem0ai/mem0)
- **Architectural Fit:** Provides a scalable, self-updating user/session/agent memory layer. Mem0 continuously extracts salient facts, user preferences, and cross-session constraints from conversation streams, updating vector/graph representations while discarding conversational noise. Supports SQLite/Qdrant/PostgreSQL backends.
- **Verification Gate:**
  - *Link / Maintenance:* Extremely active development; frequent releases in 2024–2026.
  - *Adoption:* 26k+ GitHub stars; rapid integration across modern AI frameworks.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C1` (CLI Developer Profile), `C2` (Repo Preferences), `C4` (Interactive IDE Memory), `C5` (Cross-Agent Knowledge).
- **Recommendation:** 🟢 **Essential** — Best drop-in developer preference and cross-session fact extraction engine.

#### 2. Letta (formerly MemGPT)
- **Repository:** [`https://github.com/letta-ai/letta`](https://github.com/letta-ai/letta)
- **Architectural Fit:** Implements an OS-inspired memory hierarchy (Core Memory in context, Recall Memory for episodic event logs, Archival Memory for unbounded vector search). Agents autonomously manage and edit their own memory via dedicated tool calls (`core_memory_append`, `archival_memory_insert`).
- **Verification Gate:**
  - *Link / Maintenance:* Actively maintained by Letta AI team; complete platform evolution from research paper to production system.
  - *Adoption:* 15k+ GitHub stars; pioneer of LLM OS memory tiering.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C2` (Autonomous Worker), `C3` (Long-Horizon Tasks), `C4` (Stateful Multi-Turn Agents).
- **Recommendation:** 🟢 **Essential** for agents requiring explicit self-editing memory blocks and hierarchical state paging.

#### 3. LangMem
- **Repository:** [`https://github.com/langchain-ai/langmem`](https://github.com/langchain-ai/langmem)
- **Architectural Fit:** Designed as a specialized memory service for LangGraph and custom stateful graphs. It extracts episodic memories in background threads and maintains structured schemas (user profiles, organizational memory, conversation summaries) via prompt-optimized reflection prompts.
- **Verification Gate:**
  - *Link / Maintenance:* Maintained under the LangChain ecosystem umbrella.
  - *Adoption:* Growing adoption within LangGraph production deployments.
  - *License:* MIT License.
- **Archetype Fit:** `C4` (IDE Assistant), `C5` (LangGraph Swarms).
- **Recommendation:** 🟡 **Optional** — Strong candidate if the agent harness is built on LangGraph/LangChain; otherwise, Mem0 provides greater independence.

#### 4. Zep (Graphiti Temporal Knowledge Graph)
- **Repository:** [`https://github.com/getzep/graphiti`](https://github.com/getzep/graphiti) *(Open Source Core)*
- **Architectural Fit:** Graphiti extracts dynamic temporal knowledge graphs from unstructured interactions. Unlike static vector stores, it represents relationships with temporal validity edges (e.g., "Dependency X was updated on date Y, replacing Z").
- **Verification Gate:**
  - *Link / Maintenance:* Active OSS focus on Graphiti (`getzep/graphiti`); commercial SaaS for legacy Zep Server.
  - *Adoption:* 3.5k+ stars on Graphiti; strong technical validation in temporal reasoning.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C3` (Continuous Repositories), `C5` (Enterprise Knowledge Swarms), `C6` (Infrastructure Topology Memory).
- **Recommendation:** 🟡 **Optional** — High-value specialized engine for environments where facts change over time and temporal entity graphs are required.

---

## 3. CAP-14: Experiential Recall & Dynamic Knowledge Retrieval

| Tool | Repo / URL | Tier | License | Primary Archetypes |
| :--- | :--- | :--- | :--- | :--- |
| **LlamaIndex** | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟢 **Essential** | MIT | `C1`, `C2`, `C3`, `C4`, `C5`, `C6` |
| **Haystack (v2)** | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 🟡 **Optional** | Apache-2.0 | `C3`, `C5`, `C6` |
| **Custom Dense/Sparse Embedding Harness (BM25 + Qdrant/Chroma)** | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟢 **Essential** *(Native Layer)* | Apache-2.0 | All (`C1`–`C6`) |

---

### Tool Evaluations: CAP-14

#### 1. LlamaIndex
- **Repository:** [`https://github.com/run-llama/llama_index`](https://github.com/run-llama/llama_index)
- **Architectural Fit:** Provides advanced indexing and retrieval mechanisms: AST code parsing, hierarchical document summarization, sub-question routing, hybrid keyword/vector search, and dynamic tool retrieval. It offers battle-tested loaders for source repositories, markdown docs, and execution traces.
- **Verification Gate:**
  - *Link / Maintenance:* Exceptional release velocity; multi-language (Python, TS); dedicated enterprise backing.
  - *Adoption:* 38k+ GitHub stars; industry de facto standard for advanced RAG and indexing.
  - *License:* MIT License.
- **Archetype Fit:** `C1` through `C6` (Universal code and doc indexing).
- **Recommendation:** 🟢 **Essential** — Comprehensive, flexible knowledge ingestion, chunking, and retrieval engine for codebase search and experiential recall.

#### 2. Haystack (v2)
- **Repository:** [`https://github.com/deepset-ai/haystack`](https://github.com/deepset-ai/haystack)
- **Architectural Fit:** Component-driven pipeline architecture where each indexing and retrieval step is a typed Python component connected via a strict directed graph. It excels in deterministic enterprise search pipelines and custom reranking pipelines with low abstractions.
- **Verification Gate:**
  - *Link / Maintenance:* Highly disciplined engineering by deepset; clean v2 rewrite; continuous enterprise maintenance.
  - *Adoption:* 18k+ GitHub stars; strong European enterprise footprint.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C3` (Batch Indexers), `C5` (Enterprise Search Swarms), `C6` (Documentation & Runbook Retrieval).
- **Recommendation:** 🟡 **Optional** — Top-tier alternative to LlamaIndex for teams preferring explicit typed pipeline graphs over framework abstractions.

#### 3. Native Hybrid Store (BM25 + Dense Vector Engine)
- **Repository:** [`https://github.com/qdrant/qdrant`](https://github.com/qdrant/qdrant) / [`https://github.com/chroma-core/chroma`](https://github.com/chroma-core/chroma)
- **Architectural Fit:** Experiential recall (recalling previous terminal errors, failed test patches, and successful refactor traces) requires hybrid retrieval: exact identifier matching (BM25/sparse) combined with semantic intent (dense embeddings). Qdrant (embedded or standalone Rust engine) or SQLite-VSS provides sub-5ms local lookup.
- **Verification Gate:**
  - *Link / Maintenance:* Actively maintained; sub-millisecond retrieval benchmarks.
  - *Adoption:* Industry standard for production vector engines.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C1`, `C2`, `C4` (Embedded local DB), `C3`, `C5`, `C6` (Clustered).
- **Recommendation:** 🟢 **Essential** — Foundational persistence layer for experiential trace recall.

---

## 4. CAP-16: Budget Governance & Context Quota Enforcement

| Tool | Repo / URL | Tier | License | Primary Archetypes |
| :--- | :--- | :--- | :--- | :--- |
| **LiteLLM Spend & Budget Manager** | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟢 **Essential** | MIT | `C1`, `C2`, `C3`, `C4`, `C5`, `C6` |
| **Tiktoken / Tokenizer Context Governor** | [openai/tiktoken](https://github.com/openai/tiktoken) | 🟢 **Essential** *(In-Memory L0 Gate)* | MIT | All (`C1`–`C6`) |
| **Langfuse (Budget & Cost Analytics)** | [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟢 **Essential** *(Observability L2 Gate)* | MIT / FSL-1.1-Apache-2.0 | `C2`, `C3`, `C5`, `C6` |
| **Ad-Hoc Unbounded Prompting** | N/A | 🔴 **Avoid** | N/A | None |

---

### Tool Evaluations: CAP-16

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 3-TIER BUDGET GOVERNANCE MODEL                                   │
│  Layer 0: In-Memory Tokenizer (tiktoken)      ──► Pre-flight context window enforcement (<1ms)   │
│  Layer 1: Gateway Budget Guard (LiteLLM)       ──► Hard spending caps, RPM/TPM throttling        │
│  Layer 2: Observability & Attribution (Langfuse)──► Trace-level cost auditing & threshold alerts │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 1. LiteLLM Budget Manager & Proxy Spend Controls
- **Repository:** [`https://github.com/BerriAI/litellm`](https://github.com/BerriAI/litellm)
- **Architectural Fit:** Provides deterministic budget quotas per user, team, session, or API key. Supports max dollar budgets (e.g. `$5.00/run`), token limits, automatic cool-downs, and rate-limit handling. When an agent hits 95% of its allocation, LiteLLM triggers soft alerts or hard HTTP 429 blocks, preventing runaway infinite loops.
- **Verification Gate:**
  - *Link / Maintenance:* Multiple daily commits; immediate provider price tracking updates.
  - *Adoption:* 22k+ GitHub stars; foundational AI gateway across thousands of companies.
  - *License:* MIT License (Core & Proxy).
- **Archetype Fit:** `C1` through `C6` (Universal gateway enforcement).
- **Recommendation:** 🟢 **Essential** — Primary gateway for hard cost isolation and budget ceiling enforcement.

#### 2. Tiktoken / Native Context Governor (Layer 0 Guard)
- **Repository:** [`https://github.com/openai/tiktoken`](https://github.com/openai/tiktoken)
- **Architectural Fit:** Sub-millisecond BPE token counting executed directly in the runtime memory prior to dispatching any network request. Enforces sliding context budgets, prefix preservation, tool-definition budget allocation, and payload truncation before hitting model context limits.
- **Verification Gate:**
  - *Link / Maintenance:* Actively maintained by OpenAI; high-performance Rust core with Python bindings.
  - *Adoption:* Hundreds of millions of downloads; ubiquitous across LLM tools.
  - *License:* MIT License.
- **Archetype Fit:** All archetypes (`C1`–`C6`).
- **Recommendation:** 🟢 **Essential** — Non-negotiable L0 component to prevent context overflow exceptions and calculate exact prompt packing.

#### 3. Langfuse
- **Repository:** [`https://github.com/langfuse/langfuse`](https://github.com/langfuse/langfuse)
- **Architectural Fit:** Open-source LLM observability platform. Tracks exact token consumption, model latencies, and dollar costs across multi-step execution trees, subagent invocations, and tool executions. Generates real-time cost attribution and budget exhaustion notifications.
- **Verification Gate:**
  - *Link / Maintenance:* Rapid release cadence; mature web UI and SDKs (Python, JS/TS).
  - *Adoption:* 12k+ GitHub stars; leading open-source LLM telemetry solution.
  - *License:* MIT / FSL-1.1-Apache-2.0.
- **Archetype Fit:** `C2` (Autonomous Workers), `C3` (CI Pipelines), `C5` (Multi-Agent Systems), `C6` (Production SRE).
- **Recommendation:** 🟢 **Essential** for operational cost visibility, telemetry, and post-execution cost analysis.

---

## 5. CAP-23: Dynamic Model Routing & Fallback Orchestration

| Tool | Repo / URL | Tier | License | Primary Archetypes |
| :--- | :--- | :--- | :--- | :--- |
| **LiteLLM Proxy & Router** | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟢 **Essential** | MIT | `C1`, `C2`, `C3`, `C4`, `C5`, `C6` |
| **RouteLLM (LMSYS)** | [lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM) | 🟢 **Essential** *(Cost-Quality Router)* | Apache-2.0 | `C1`, `C2`, `C3`, `C4`, `C5` |
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | 🟡 **Optional** *(Cloud Fallback)* | Proprietary / Open API | `C1`, `C4` |
| **Martian (Model Router)** | [withmartian.com](https://withmartian.com) | 🟡 **Optional** | Proprietary SaaS | `C3`, `C5` |

---

### Tool Evaluations: CAP-23

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   DYNAMIC MODEL ROUTING MATRIX                                   │
│  Inbound Request ──► RouteLLM Complexity Gate ──┬──► Low Complexity  ──► Fast/Cheap (Flash/Mini) │
│                                                 └──► High Complexity ──► Frontier (Claude/GPT-4o)│
│  LiteLLM Gateway Engine: Provider Fallbacks (Direct ──► AWS Bedrock ──► Azure ──► OpenRouter)   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 1. LiteLLM (Proxy & Router Core)
- **Repository:** [`https://github.com/BerriAI/litellm`](https://github.com/BerriAI/litellm)
- **Architectural Fit:** Provides a unified OpenAI-compatible interface across 100+ LLMs (Anthropic, Gemini, OpenAI, Bedrock, Vertex AI, Ollama). Implements dynamic load balancing, health check cooldowns (disabling failing endpoints automatically), fallback cascades (e.g. `claude-3-5-sonnet` -> `gpt-4o` -> `gemini-1.5-pro`), and latency-based routing.
- **Verification Gate:**
  - *Link / Maintenance:* Over 500 releases; industry standard for multi-provider routing.
  - *Adoption:* 22k+ GitHub stars; battle-tested across production workloads.
  - *License:* MIT License.
- **Archetype Fit:** Universally required across `C1` through `C6`.
- **Recommendation:** 🟢 **Essential** — Core mechanical abstraction for model routing, provider failover, and standardized payload schemas.

#### 2. RouteLLM (LMSYS)
- **Repository:** [`https://github.com/lm-sys/RouteLLM`](https://github.com/lm-sys/RouteLLM)
- **Architectural Fit:** Developed by LMSYS (creators of Chatbot Arena). Uses trained preference routers (Matrix Factorization, BERT classifier, or Causal LLM) to dynamically route queries between expensive frontier models (e.g. Claude 3.5 Sonnet / GPT-4o) and fast, economical models (e.g. GPT-4o-mini / Gemini Flash) with zero human intervention, achieving up to 85% cost reduction while retaining 95%+ benchmark quality.
- **Verification Gate:**
  - *Link / Maintenance:* Maintained by LMSYS research foundation; open weights and clear calibration benchmarks.
  - *Adoption:* 4k+ GitHub stars; high academic and production credibility.
  - *License:* Apache-2.0.
- **Archetype Fit:** `C1` (CLI Tools), `C2` (Repo Workers), `C3` (Batch Tasks), `C4` (IDE Code Assistants).
- **Recommendation:** 🟢 **Essential** for dynamic cost-performance optimization without manual prompt classification.

#### 3. OpenRouter
- **Official Site:** [`https://openrouter.ai`](https://openrouter.ai)
- **Architectural Fit:** Cloud-managed multi-model API aggregator. Features automatic price/throughput optimization, unified billing, and automated fallback routing across multiple downstream hosters. While excellent as an external aggregator or secondary fallback, relying solely on a proprietary third-party proxy creates an external dependency for local harnesses.
- **Verification Gate:**
  - *Link / Maintenance:* Active SaaS service; highly reliable with broad developer usage.
  - *Adoption:* Massive indie and developer ecosystem mindshare.
  - *License:* Proprietary cloud service (standard HTTP client integration).
- **Archetype Fit:** `C1` (Fast CLI setup), `C4` (Interactive coding).
- **Recommendation:** 🟡 **Optional** — Excellent as a secondary fallback upstream inside LiteLLM rather than the primary harness router.

#### 4. Martian (Model Router)
- **Official Site:** [`https://withmartian.com`](https://withmartian.com)
- **Architectural Fit:** Enterprise SaaS router that unpacks prompts into model interpretability vectors to route each request to the optimal model for that specific task. High routing accuracy for enterprise workloads, but closed-source and proprietary.
- **Verification Gate:**
  - *Link / Maintenance:* Active VC-backed enterprise startup.
  - *Adoption:* Enterprise deployments; closed-source.
  - *License:* Commercial SaaS.
- **Archetype Fit:** `C3` (High-volume Enterprise Batch), `C5` (Enterprise Swarms).
- **Recommendation:** 🟡 **Optional** — Strong for enterprise procurement requiring managed routing; OSS stack (LiteLLM + RouteLLM) preferred for developer harnesses.

---

## 6. Archetype-to-Tool Synthesis Matrix

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                ARCHETYPE CAPABILITY COMPOSITION                                  │
│                                                                                                  │
│  Archetype      CAP-05 (Workflow)   CAP-10 (Memory)     CAP-14 (Recall)     CAP-16/23 (Gov/Route)│
│  ─────────      ─────────────────   ───────────────     ───────────────     ─────────────────────│
│  C1 (CLI)       Asyncio / Local     Mem0 (Prefs)        LlamaIndex (Lite)   LiteLLM + RouteLLM   │
│  C2 (Worker)    Trigger.dev         Mem0 + Letta        LlamaIndex + Vector LiteLLM + tiktoken   │
│  C3 (Pipeline)  Temporal / Trigger  Letta + Graphiti    LlamaIndex + Qdrant LiteLLM + Langfuse   │
│  C4 (IDE)       Trigger.dev / Async Mem0 (Session/File) LlamaIndex (AST)    LiteLLM + RouteLLM   │
│  C5 (Swarm)     Temporal            Mem0 / LangMem      Qdrant / Haystack   LiteLLM Proxy Gate   │
│  C6 (Ops/SRE)   Temporal            Graphiti (Topology) LlamaIndex Runbooks LiteLLM + Langfuse   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Archetype Architectural Stack Recommendations

1. **`C1` — Single-Turn Developer CLI Assistant**
   - **Stack:** `LiteLLM` (Routing/Budget) + `tiktoken` (Local Context Budget) + `Mem0` (Local Developer Preferences) + `RouteLLM` (Flash vs Frontier Router).
   - **Rationale:** Sub-100ms startup overhead, zero external background daemon dependencies.

2. **`C2` — Autonomous Code Worker / Refactoring Agent**
   - **Stack:** `Trigger.dev` (Task Execution) + `Letta` (Self-editing Working Memory) + `LlamaIndex` (AST Code Retrieval) + `LiteLLM` (Provider Failover) + `Langfuse` (Cost Tracking).
   - **Rationale:** Supports multi-hour refactor runs, checkpointed workspace state, and structured code search.

3. **`C3` — Long-Horizon Background Agent / CI-CD Pipeline**
   - **Stack:** `Temporal` (Durable Execution) + `Letta` / `Graphiti` (Episodic & Temporal State) + `LlamaIndex` + `LiteLLM Proxy` (Hard Budget Caps).
   - **Rationale:** Immune to infrastructure crashes; complete deterministic replay for multi-step agent pipelines.

4. **`C4` — Interactive Multi-Turn IDE / REPL Environment**
   - **Stack:** `Trigger.dev` (Async Background Indexing) + `Mem0` (Session/File Context) + `LlamaIndex` (Workspace Index) + `RouteLLM` (Latency-optimized model switching).
   - **Rationale:** Ultra-responsive user-facing turns with non-blocking background indexing and cross-file memory.

5. **`C5` — Multi-Agent Swarm / Distributed System**
   - **Stack:** `Temporal` (Distributed Coordination) + `Mem0` / `LangMem` (Shared Agent Blackboard) + `Qdrant` + `LiteLLM Proxy` (Team/Agent Token Quotas).
   - **Rationale:** Prevents cascading agent failures and enforces decentralized spend limits across swarm nodes.

6. **`C6` — Autonomous SRE / Production Diagnostic Agent**
   - **Stack:** `Temporal` (Reliable Incident Workflows) + `Graphiti` (Temporal Topology Knowledge Graph) + `Haystack` / `LlamaIndex` (Runbook Search) + `Langfuse` + `LiteLLM`.
   - **Rationale:** High-governance execution with clear temporal tracking of infrastructure state changes and runbook retrieval.

---

## 7. Verification Checklist & Implementation Plan

> [!IMPORTANT]
> ### Phase 3 Integration Directives:
> 1. **L0 Token Safety:** Always execute `tiktoken` context calculation in runtime memory before dispatching to any provider to prevent 400 ContextWindowExceeded errors.
> 2. **Provider Failover Invariant:** Configure `LiteLLM` router with a minimum of 2 backup providers (e.g. Anthropic Direct $\rightarrow$ AWS Bedrock $\rightarrow$ OpenRouter) for all production agents (`C2`–`C6`).
> 3. **Budget Hard-Stop:** Wire `LiteLLM` spend management to terminate sessions immediately if a single run exceeds its allocated cost ceiling (e.g., $2.00 for `C2`, $10.00 for `C3`).

---

## Sources & Reference Documentation

- **Temporal Workflow Engine:** [`https://github.com/temporalio/temporal`](https://github.com/temporalio/temporal) · [Temporal Documentation](https://docs.temporal.io)
- **Trigger.dev v3:** [`https://github.com/triggerdotdev/trigger.dev`](https://github.com/triggerdotdev/trigger.dev) · [Trigger.dev Docs](https://trigger.dev/docs)
- **Prefect Orchestration:** [`https://github.com/PrefectHQ/prefect`](https://github.com/PrefectHQ/prefect) · [Prefect Docs](https://docs.prefect.io)
- **Mem0 Universal Memory:** [`https://github.com/mem0ai/mem0`](https://github.com/mem0ai/mem0) · [Mem0 Documentation](https://docs.mem0.ai)
- **Letta (MemGPT Engine):** [`https://github.com/letta-ai/letta`](https://github.com/letta-ai/letta) · [Letta Documentation](https://docs.letta.com)
- **LangMem Memory Service:** [`https://github.com/langchain-ai/langmem`](https://github.com/langchain-ai/langmem)
- **Graphiti Temporal KG (Zep):** [`https://github.com/getzep/graphiti`](https://github.com/getzep/graphiti)
- **LlamaIndex Data Framework:** [`https://github.com/run-llama/llama_index`](https://github.com/run-llama/llama_index) · [LlamaIndex Documentation](https://docs.llamaindex.ai)
- **Haystack v2:** [`https://github.com/deepset-ai/haystack`](https://github.com/deepset-ai/haystack) · [Haystack Documentation](https://haystack.deepset.ai)
- **LiteLLM Router & Proxy:** [`https://github.com/BerriAI/litellm`](https://github.com/BerriAI/litellm) · [LiteLLM Documentation](https://docs.litellm.ai)
- **RouteLLM (LMSYS):** [`https://github.com/lm-sys/RouteLLM`](https://github.com/lm-sys/RouteLLM)
- **Langfuse LLM Telemetry:** [`https://github.com/langfuse/langfuse`](https://github.com/langfuse/langfuse) · [Langfuse Docs](https://langfuse.com/docs)
