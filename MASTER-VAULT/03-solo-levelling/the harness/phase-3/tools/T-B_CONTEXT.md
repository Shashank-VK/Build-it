# Phase 3 Tool Selection — S-Tier Context & Memory Layer

> **Document Type:** Phase 3 Concrete Tool Selection & Architectural Evaluation  
> **Target Capabilities:** `CAP-08` (Working Memory Management & Isolation), `CAP-09` (Context Compaction & Pinned Preservation), `CAP-13` (External Knowledge Retrieval / RAG), `CAP-15` (Build-Time Knowledge Curation & Indexing)  
> **Grounding:** `phase-2/RANKINGS.md` · `phase-1/MASTER_TAXONOMY.md` · `phase-0/ARCHETYPES_AND_CRITERIA.md` (C1–C6, SC-01..10)  
> **Verification Gate Status:** **STRICT ENFORCEMENT PASSED** (All URLs verified, licenses audited, repository health checked, SaaS lock-in traps classified)

---

## 0. Executive Summary & Context Layer Architecture

Layer 2 (Context, Memory & Knowledge) serves as the **cognitive state substrate** of the autonomous development harness. While Layer 1 governs non-deterministic execution and Layer 4 enforces safety boundaries, Layer 2 prevents **attention dilution**, **context rot**, **hallucinatory drift**, and **"lost-in-the-middle" reasoning failures** across long execution horizons (>30k–100k+ tokens).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         LAYER 2: CONTEXT & MEMORY STACK ARCHITECTURE                             │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
                                 ┌────────────────────────┐
                                 │   P0-P4 Context Budget │ ◄── [CAP-16] Tiktoken / Tokenizers
                                 │   & Prompt Assembly    │
                                 └───────────┬────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
          ┌──────────────────────────┐                ┌──────────────────────────┐
          │  CAP-08 Working Memory   │                │   CAP-09 Compaction &    │
          │  Active Turn Scratchpad  │ ◄── Letta ──►  │   Pinned Preservation    │
          │  (Bounded Spatial Turn)  │                │  (LLMLingua / Anchored)  │
          └────────────┬─────────────┘                └────────────┬─────────────┘
                       │                                           │
         ┌─────────────┴─────────────┐               ┌─────────────┴─────────────┐
         ▼                           ▼               ▼                           ▼
┌───────────────────┐       ┌──────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│ CAP-13 Ext. RAG   │       │ CAP-14 Recall &  │ │ CAP-15 Curation   │ │ Vector / Embedded │
│ (LlamaIndex /     │       │ Fact Promotion   │ │ (Tree-sitter /    │ │ Substrate (Qdrant │
│  Hybrid Search)   │       │ (Mem0)           │ │  Repomix AST)     │ │  / LanceDB)       │
└───────────────────┘       └──────────────────┘ └───────────────────┘ └───────────────────┘
```

---

## 1. Concrete Tool Selection by Capability

---

### Category A: Vector Databases & Retrieval Substrates (`CAP-13` / `CAP-15`)

```
========================================================================================
1. Qdrant — High-Performance Rust Vector Engine & Hybrid Search
========================================================================================
```
* **Name:** Qdrant
* **Repository URL:** `https://github.com/qdrant/qdrant`
* **What It Does:** Production-grade, Rust-based vector search engine providing high-throughput similarity search, dense/sparse hybrid search (BM25 + SPLADE/Dense), scalar and product quantization, and rich JSON payload filtering.
* **Fit Rationale (`CAP-13` / `CAP-15`):** Codebase search requires deep payload filtering (by branch, file path, commit hash, and AST symbol type). Qdrant executes filtered vector search without post-retrieval performance cliffs, provides native sparse-dense hybrid search for exact code symbol matching, and runs as an unprivileged, low-footprint container in hermetic sandboxes.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/qdrant/qdrant`)
  * *Last Commit / Activity:* Active (Daily commits, release cycle v1.13+)
  * *GitHub Stars:* ~34,000+
  * *License:* Apache License 2.0 (Permissive OSS)
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**, **C6 (Migration & Modernization)**, **C2 (Data & MLOps)**

---

```
========================================================================================
2. LanceDB — Embedded Serverless Columnar Vector Database
========================================================================================
```
* **Name:** LanceDB
* **Repository URL:** `https://github.com/lancedb/lancedb`
* **What It Does:** Lightweight, embedded vector database built on top of the Lance columnar data format. Executes vector search directly on disk without requiring an external database server process or daemon.
* **Fit Rationale (`CAP-13` / `CAP-08`):** Ideal for local CLI harnesses and ephemeral subagent workspaces (`.agents/<id>/lancedb`). Requires zero network sockets or background daemons, eliminating connection management complexity while delivering sub-millisecond retrieval across embedded codebase indices.
* **Tier:** **Essential** (for local/embedded workloads); **Optional** (for multi-tenant cloud).
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/lancedb/lancedb`)
  * *Last Commit / Activity:* Active (v0.18+, regular multi-language SDK releases)
  * *GitHub Stars:* ~10,000+
  * *License:* Apache License 2.0
* **Best Archetype:** **C1 (Product Engineering 0→1)**, **C3 (Browser & Automation Ops)**, **C5 (Platform/IaC)**

---

```
========================================================================================
3. Chroma — Developer-First Open-Source Embeddable Vector Store
========================================================================================
```
* **Name:** Chroma
* **Repository URL:** `https://github.com/chroma-core/chroma`
* **What It Does:** Open-source AI application database designed for simple local and client-server embedding storage, document collection management, and cosine/L2 nearest-neighbor search.
* **Fit Rationale (`CAP-13`):** Excellent developer ergonomics for rapid prototyping and local unit-test fixtures. However, for large enterprise monorepos (>100k files) and complex hybrid sparse-dense code retrieval, it exhibits higher memory usage and fewer advanced index quantization options than Qdrant or LanceDB.
* **Tier:** **Optional**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/chroma-core/chroma`)
  * *Last Commit / Activity:* Active (Rust-core transition v0.6+)
  * *GitHub Stars:* ~29,000+
  * *License:* Apache License 2.0
* **Best Archetype:** **C1 (Product Engineering 0→1)**

---

```
========================================================================================
4. Weaviate — Cloud-Native Modular Vector Database
========================================================================================
```
* **Name:** Weaviate
* **Repository URL:** `https://github.com/weaviate/weaviate`
* **What It Does:** Go-based open-source vector database featuring built-in vectorization pipelines, GraphQL/REST APIs, hybrid search, multi-tenancy, and object-storage backups.
* **Fit Rationale (`CAP-13`):** Powerful for enterprise data lakes and multi-tenant RAG systems, but carries heavy operational complexity (GraphQL schemas, Go runtime memory footprints, separate vectorizer modules) that adds unnecessary harness weight for developer-focused coding agents.
* **Tier:** **Optional**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/weaviate/weaviate`)
  * *Last Commit / Activity:* Active (v1.28+, active enterprise development)
  * *GitHub Stars:* ~17,000+
  * *License:* BSD 3-Clause
* **Best Archetype:** **C2 (Data, Analytics & MLOps Fabric)**

---

```
========================================================================================
5. Pinecone (Python SDK / Managed Service)
========================================================================================
```
* **Name:** Pinecone
* **Repository URL:** `https://github.com/pinecone-io/python-sdk`
* **What It Does:** Fully managed, closed-source SaaS vector database accessible via REST/gRPC client SDKs.
* **Fit Rationale (`CAP-13`):** Fails the hermetic execution and local sandbox requirements. External SaaS calls introduce network latency on agent tool loops, expose proprietary codebase embeddings to third-party endpoints, create vendor lock-in, and cannot run in air-gapped CI/CD runners (`RUN-01`).
* **Tier:** **Avoid** (for local/hermetic development harnesses; strictly relegated to optional SaaS backends)
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/pinecone-io/python-sdk`)
  * *Last Commit / Activity:* Active (SDK updates)
  * *GitHub Stars:* ~450+ (SDK repo)
  * *License:* Apache-2.0 (Client SDK only; backend server engine is proprietary closed-source)
* **Best Archetype:** None (SaaS convenience only)

---

### Category B: RAG Stacks & Retrieval Orchestrators (`CAP-13` / `CAP-15`)

```
========================================================================================
1. LlamaIndex — Data Framework & Agentic RAG Pipeline Engine
========================================================================================
```
* **Name:** LlamaIndex
* **Repository URL:** `https://github.com/run-llama/llama_index`
* **What It Does:** Comprehensive data framework providing connectors, hierarchical document chunkers, AST-aware code node parsers, hybrid retrieval algorithms, sub-question query engines, and agentic retrieval tools.
* **Fit Rationale (`CAP-13` / `CAP-15`):** The benchmark standard for structuring unstructured data. Directly implements `CAP-13` (Hybrid dense/BM25 retrieval + Reciprocal Rank Fusion) and `CAP-15` (Build-time codebase indexing). Provides specialized code splitters that respect function/class boundaries and multi-document synthesis routines.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/run-llama/llama_index`)
  * *Last Commit / Activity:* Active (Continuous daily commits, v0.12+)
  * *GitHub Stars:* ~52,000+
  * *License:* MIT License
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**, **C6 (Migration & Strangler Rebuild)**, **C1 (Product Engineering)**

---

```
========================================================================================
2. Haystack — Modular Directed Graph RAG Framework
========================================================================================
```
* **Name:** Haystack (by deepset)
* **Repository URL:** `https://github.com/deepset-ai/haystack`
* **What It Does:** Modular, component-based orchestration framework (Haystack 2.x) that models search, indexing, and RAG pipelines as explicit Directed Acyclic Graphs (DAGs).
* **Fit Rationale (`CAP-13`):** Outstanding for strict, deterministic production pipelines (`CAP-04`) with high observability and custom reranking steps. While slightly less code-AST-specialized out of the box than LlamaIndex, its explicit DAG components provide clean type safety and deterministic execution control.
* **Tier:** **Optional** (Primary alternative to LlamaIndex for enterprise DAG-centric pipelines)
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/deepset-ai/haystack`)
  * *Last Commit / Activity:* Active (Regular monthly releases, Haystack 2.x)
  * *GitHub Stars:* ~26,000+
  * *License:* Apache License 2.0
* **Best Archetype:** **C2 (Data, Analytics & MLOps)**, **C5 (Platform & DevOps)**

---

### Category C: Working Memory, Compaction & Long-Term Stores (`CAP-08` / `CAP-09` / `CAP-14`)

```
========================================================================================
1. Letta (formerly MemGPT) — Hierarchical Agent Memory Operating System
========================================================================================
```
* **Name:** Letta
* **Repository URL:** `https://github.com/letta-ai/letta`
* **What It Does:** Agent operating system that provides hierarchical tiered memory management (active context window vs archival storage vs recall memory), self-editing memory tool calls, and persistent agent state across sessions.
* **Fit Rationale (`CAP-08` / `CAP-09`):** Directly implements `CAP-08` (Working Memory Isolation) and `CAP-09` (Context Compaction). Letta treats LLM context like RAM: it virtualizes memory by allowing agents to explicitly page information into and out of the active prompt window, preventing context overflow while maintaining persistent project invariants.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/letta-ai/letta`)
  * *Last Commit / Activity:* Active (Daily commits, Letta v0.1+)
  * *GitHub Stars:* ~24,000+
  * *License:* Apache License 2.0
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**, **C1 (Product Engineering)**, **C6 (Migration Rebuild)**

---

```
========================================================================================
2. Mem0 — Dynamic Experiential Fact & User Memory Layer
========================================================================================
```
* **Name:** Mem0
* **Repository URL:** `https://github.com/mem0ai/mem0`
* **What It Does:** Intelligent long-term memory engine that automatically extracts user preferences, project conventions, and operational decisions from conversational traces, dynamically resolving contradictions and updating semantic memory graphs.
* **Fit Rationale (`CAP-14` / `CAP-10` / `CAP-08`):** Provides the concrete implementation for Experiential Memory Recall (`CAP-14`) and Fact Promotion (`CAP-10`). Extracts project-specific coding conventions (`"User prefers pytest with async-io fixtures"`) and injects them into working memory without retaining thousands of tokens of noisy raw chat logs.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/mem0ai/mem0`)
  * *Last Commit / Activity:* Active (Continuous daily updates, v1.0+)
  * *GitHub Stars:* ~64,500+
  * *License:* Apache License 2.0
* **Best Archetype:** **C1 (Product Engineering)**, **C3 (Browser & Surface Ops)**, **C4 (Agentic Systems)**

---

```
========================================================================================
3. LangMem — Long-Term Memory Optimization for Agent Graphs
========================================================================================
```
* **Name:** LangMem (LangChain Ecosystem)
* **Repository URL:** `https://github.com/langchain-ai/langmem`
* **What It Does:** Lightweight library designed to extract, maintain, and query conversational memory, semantic profiles, and episodic summaries within agent execution graphs.
* **Fit Rationale (`CAP-08` / `CAP-14`):** Seamless integration if the harness is already built on LangGraph. However, if using standalone agent loops or LiteLLM gateways, it introduces unnecessary dependency entanglement with LangChain internals.
* **Tier:** **Optional**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/langchain-ai/langmem`)
  * *Last Commit / Activity:* Active (Frequent commits)
  * *GitHub Stars:* Emerging / Maintained by LangChain org
  * *License:* MIT License
* **Best Archetype:** **C4 (Agentic & Knowledge Synthesis)**

---

```
========================================================================================
4. Zep — Fast Temporal Memory Server
========================================================================================
```
* **Name:** Zep
* **Repository URL:** `https://github.com/getzep/zep`
* **What It Does:** Memory engine providing low-latency chat history storage, automatic entity extraction, semantic search over messages, and temporal knowledge graphs.
* **Fit Rationale (`CAP-08` / `CAP-09`):** Strong for human-to-AI chatbot conversational history, but less suited for deep codebase AST indexing, file-tree synchronization, or hermetic offline developer harnesses due to cloud/enterprise service shifts.
* **Tier:** **Optional**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/getzep/zep`)
  * *Last Commit / Activity:* Active (v2.0 / Zep Cloud updates)
  * *GitHub Stars:* ~4,800+
  * *License:* Apache License 2.0
* **Best Archetype:** **C3 (Automation & Surface Ops)**

---

### Category D: Context Compaction, Token Budgeting & Code Curation (`CAP-08` / `CAP-09` / `CAP-15` / `CAP-16`)

```
========================================================================================
1. LLMLingua / LongLLMLingua — Neural Context & Prompt Compression
========================================================================================
```
* **Name:** LLMLingua / LongLLMLingua (Microsoft Research)
* **Repository URL:** `https://github.com/microsoft/LLMLingua`
* **What It Does:** Task-aware prompt and document compression engine using small, fast language models (e.g. LLaMA/GPT-2) to prune non-essential tokens and whitespace, achieving up to 5x–20x context compression with minimal loss in reasoning accuracy.
* **Fit Rationale (`CAP-09` / `CAP-16`):** Directly powers Context Compaction (`CAP-09`) and Token Budget Governance (`CAP-16`). Compresses massive retrieved document corpora and intermediate tool execution outputs before injecting them into the active working memory prompt, eliminating context stuffing costs.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/microsoft/LLMLingua`)
  * *Last Commit / Activity:* Active (Regular maintenance & releases)
  * *GitHub Stars:* ~6,600+
  * *License:* MIT License
* **Best Archetype:** **C4 (Knowledge Synthesis)**, **C6 (Migration/Modernization)**, **C2 (Data & MLOps)**

---

```
========================================================================================
2. Tree-sitter — Incremental Concrete Syntax Tree (AST) Parser
========================================================================================
```
* **Name:** Tree-sitter
* **Repository URL:** `https://github.com/tree-sitter/tree-sitter`
* **What It Does:** High-performance, incremental parsing engine generating robust syntax trees across 50+ programming languages, supporting real-time syntax queries via S-expressions.
* **Fit Rationale (`CAP-15`):** The non-negotiable mechanical foundation for Build-Time Knowledge Curation (`CAP-15`). Enables semantic code chunking (keeping functions, classes, and type definitions intact rather than arbitrary token boundaries), call-graph extraction, and symbol table generation for precise code retrieval.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/tree-sitter/tree-sitter`)
  * *Last Commit / Activity:* Highly Active (Daily commits, v0.25+)
  * *GitHub Stars:* ~27,000+
  * *License:* MIT License
* **Best Archetype:** **ALL Archetypes (C1–C6)**

---

```
========================================================================================
3. Repomix — AI-Optimized Codebase Context Packing & Distillation
========================================================================================
```
* **Name:** Repomix (formerly Repopack)
* **Repository URL:** `https://github.com/yamadashy/repomix`
* **What It Does:** Fast tool that analyzes, filters (respecting `.gitignore`), and packs entire codebases or target subtrees into clean, structured, token-counted XML/Markdown context bundles for LLMs.
* **Fit Rationale (`CAP-15` / `CAP-08`):** Crucial for build-time knowledge curation (`CAP-15`) and working memory initialization. Packs repository structure and file contents into compact, machine-parseable schemas with token counts, removing noise (binaries, lockfiles, node_modules) deterministically.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/yamadashy/repomix`)
  * *Last Commit / Activity:* Highly Active (Daily commits, v0.2+)
  * *GitHub Stars:* ~28,000+
  * *License:* MIT License
* **Best Archetype:** **C1 (Product Engineering)**, **C5 (Platform/IaC)**, **C6 (Migration)**

---

```
========================================================================================
4. Tiktoken & Tokenizers — Sub-Millisecond Token Budgeting Primitives
========================================================================================
```
* **Name:** Tiktoken (OpenAI) / HuggingFace Tokenizers
* **Repository URL:** `https://github.com/openai/tiktoken` & `https://github.com/huggingface/tokenizers`
* **What It Does:** Extremely fast Byte-Pair Encoding (BPE) and subword token counting/encoding engines in Rust and Python.
* **Fit Rationale (`CAP-08` / `CAP-16`):** Provides the mechanical enforcement for turn-level Working Memory budgets. Enables pre-flight verification that system prompts (P0), security delimiters (P1), tool schemas (P2), memory (P3), and user inputs (P4) strictly fit within the 50/30/20 token envelope before making LLM API calls.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Valid (`github.com/openai/tiktoken` · `github.com/huggingface/tokenizers`)
  * *Last Commit / Activity:* Highly Active (Stable core libraries)
  * *GitHub Stars:* ~13,000+ (Tiktoken) · ~10,000+ (Tokenizers)
  * *License:* MIT License (Tiktoken) / Apache License 2.0 (Tokenizers)
* **Best Archetype:** **ALL Archetypes (C1–C6)**

---

## 2. Tool Tier Verification Matrix

| Tool Name | Primary Target Capability | Evaluated Tier | GitHub Stars | License | Link & Health Verification | Primary Archetype |
|---|---|---|---|---|---|---|
| **Qdrant** | `CAP-13` External RAG Substrate | **Essential** | ~34k | Apache-2.0 | `qdrant/qdrant` (Active) | **C4 / C6 / C2** |
| **LanceDB** | `CAP-13` Embedded RAG Store | **Essential** | ~10k | Apache-2.0 | `lancedb/lancedb` (Active) | **C1 / C3 / C5** |
| **LlamaIndex** | `CAP-13` RAG / `CAP-15` Curation | **Essential** | ~52k | MIT | `run-llama/llama_index` (Active) | **C4 / C6 / C1** |
| **Letta** | `CAP-08` Working Memory / `CAP-09` | **Essential** | ~24k | Apache-2.0 | `letta-ai/letta` (Active) | **C4 / C1 / C6** |
| **Mem0** | `CAP-14` Recall / `CAP-10` Consolid. | **Essential** | ~64.5k | Apache-2.0 | `mem0ai/mem0` (Active) | **C1 / C3 / C4** |
| **LLMLingua** | `CAP-09` Compaction / `CAP-16` | **Essential** | ~6.6k | MIT | `microsoft/LLMLingua` (Active) | **C4 / C6 / C2** |
| **Tree-sitter** | `CAP-15` AST Knowledge Curation | **Essential** | ~27k | MIT | `tree-sitter/tree-sitter` (Active) | **ALL (C1–C6)** |
| **Repomix** | `CAP-15` Repo Context Packing | **Essential** | ~28k | MIT | `yamadashy/repomix` (Active) | **C1 / C5 / C6** |
| **Tiktoken** | `CAP-08` / `CAP-16` Token Budget | **Essential** | ~13k | MIT | `openai/tiktoken` (Active) | **ALL (C1–C6)** |
| **Chroma** | `CAP-13` Local Vector Store | **Optional** | ~29k | Apache-2.0 | `chroma-core/chroma` (Active) | **C1 / C3** |
| **Haystack** | `CAP-13` DAG RAG Pipelines | **Optional** | ~26k | Apache-2.0 | `deepset-ai/haystack` (Active) | **C2 / C5** |
| **LangMem** | `CAP-14` LangGraph Memory Store | **Optional** | Emerging | MIT | `langchain-ai/langmem` (Active) | **C4** |
| **Weaviate** | `CAP-13` Multi-Tenant Vector DB | **Optional** | ~17k | BSD-3 | `weaviate/weaviate` (Active) | **C2** |
| **Zep** | `CAP-08` Chat Memory Engine | **Optional** | ~4.8k | Apache-2.0 | `getzep/zep` (Active) | **C3** |
| **Pinecone** | `CAP-13` Proprietary Cloud DB | **Avoid** | ~450 (SDK) | Closed SaaS | `pinecone-io/python-sdk` | None (SaaS Lock-in) |

---

## 3. Capability-to-Tool Implementation Blueprint

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             EQUIPPED S-TIER CONTEXT/MEMORY HARNESS                               │
├───────────────────┬───────────────────────────────────┬──────────────────────────────────────────┤
│ Canonical Cap ID  │ Selected Concrete Tool Stack      │ Harness Integration & Runtime Role       │
├───────────────────┼───────────────────────────────────┼──────────────────────────────────────────┤
│ CAP-08 (Memory)   │ Letta + Tiktoken                  │ Enforces turn scratchpad boundaries;     │
│                   │                                   │ pages archival state into context RAM    │
├───────────────────┼───────────────────────────────────┼──────────────────────────────────────────┤
│ CAP-09 (Compact)  │ LLMLingua + Anchored Pinned Merge │ Neural prompt compression at 80% capacity│
│                   │                                   │ while immutably locking system invariants│
├───────────────────┼───────────────────────────────────┼──────────────────────────────────────────┤
│ CAP-13 (Ext RAG)  │ LlamaIndex + Qdrant / LanceDB     │ Hybrid dense/BM25 retrieval over docs    │
│                   │                                   │ and codebases with Reciprocal Rank Fusion│
├───────────────────┼───────────────────────────────────┼──────────────────────────────────────────┤
│ CAP-15 (Curation) │ Tree-sitter + Repomix             │ Offline AST symbol extraction, structural│
│                   │                                   │ code packaging, and metadata indexing   │
└───────────────────┴───────────────────────────────────┴──────────────────────────────────────────┘
```

### Archetype Mapping Rationale:
* **C1 (Product Engineering):** `LanceDB` (embedded, zero-server overhead) + `Repomix` (fast context pack) + `Mem0` (user style persistence).
* **C2 (Data, Analytics & MLOps):** `Qdrant` (high-throughput payload filtering) + `Haystack` (DAG data pipelines).
* **C3 (Browser & Surface Ops):** `Mem0` (session entity tracking) + `LanceDB` (ephemeral scrapers).
* **C4 (Agentic & Knowledge Synthesis):** `Letta` (hierarchical RAM) + `LlamaIndex` (agentic query engine) + `Qdrant` (vector/sparse RRF) + `LLMLingua` (neural context compression).
* **C5 (Platform, Infra & IaC):** `Repomix` + `Tree-sitter` (manifest & Terraform AST analysis) + `Tiktoken` (hard token budget limits).
* **C6 (Migration & Strangler Rebuild):** `Tree-sitter` (multi-language AST parser) + `LlamaIndex` (legacy code mapping) + `Qdrant` (cross-repo dependency indexing) + `Letta` (multi-step migration state).

---

## 4. Verification Gate Compliance Summary

1. **Verification Gate Status:** **100% PASSED**.
2. **License Compliance:** All `Essential` and `Optional` tools are strictly open source under **MIT**, **Apache-2.0**, or **BSD-3-Clause** licenses, ensuring complete freedom from proprietary runtime restrictions.
3. **Hermetic Execution Guarantee:** The selected core stack (`Qdrant` / `LanceDB`, `LlamaIndex`, `Letta`, `Mem0`, `Tree-sitter`, `LLMLingua`, `Repomix`) can execute entirely within local containers and hermetic development sandboxes without unmonitored external SaaS dependencies.

---

### Sources
* [Qdrant GitHub Repository](https://github.com/qdrant/qdrant)
* [LanceDB GitHub Repository](https://github.com/lancedb/lancedb)
* [Chroma GitHub Repository](https://github.com/chroma-core/chroma)
* [Weaviate GitHub Repository](https://github.com/weaviate/weaviate)
* [Pinecone Python SDK](https://github.com/pinecone-io/python-sdk)
* [LlamaIndex GitHub Repository](https://github.com/run-llama/llama_index)
* [Haystack by deepset GitHub Repository](https://github.com/deepset-ai/haystack)
* [Letta (formerly MemGPT) GitHub Repository](https://github.com/letta-ai/letta)
* [Mem0 GitHub Repository](https://github.com/mem0ai/mem0)
* [LangMem GitHub Repository](https://github.com/langchain-ai/langmem)
* [Zep GitHub Repository](https://github.com/getzep/zep)
* [LLMLingua Microsoft GitHub Repository](https://github.com/microsoft/LLMLingua)
* [Repomix GitHub Repository](https://github.com/yamadashy/repomix)
* [Tree-sitter GitHub Repository](https://github.com/tree-sitter/tree-sitter)
* [Tiktoken OpenAI GitHub Repository](https://github.com/openai/tiktoken)
