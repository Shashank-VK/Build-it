# 05b — Context & Memory, Repository Intelligence, Documentation Grounding

**Workstream researcher #10 (Part 11) · Written 2026-10-10 · Read-only research: no install/execute/build**

## Scope & sources

Three categories: (A) context and memory systems — memory frameworks, vector databases, embedding models, RAG frameworks, memory-evaluation benchmarks, long-context/context-compression research; (B) repository intelligence — codebase indexing, symbol indexing, AST analysis, dependency/code knowledge graphs, semantic code search, repo-map and code-packaging tools; (C) documentation grounding — live docs access, version-specific/API docs retrieval, schema discovery, llms.txt ecosystem, doc-grounding MCP services, docs-generation tooling.

Research method: `browser.search` + `browser.open` on primary sources (GitHub READMEs, docs pages, product pages) where feasible, secondary curated sources (awesome-lists, skill files, ADRs, comparison writeups) otherwise. Primary-over-secondary; star counts are approximate as-of dates shown, not tracked live. Resources already catalogued by sibling workstreams are listed once under "Already catalogued (cross-reference only)" and not re-researched in depth per the dedup list: Graphify-Labs/graphify, Opencode-DCP/opencode-dynamic-context-pruning, tickernelz/opencode-mem, 0xranx/OpenContext, thedotmack/claude-mem, upstash/context7 (and its MCP-workstream alternatives: arabold/docs-mcp-server, DeepWiki-alternatives cluster, Docfork, Ref Tools), oc-mnemoria, supamem, Hipocampo, opencode-short-term-memory, MrDoe/OpenCodeRAG, opencode-skillful, cortexkit/magic-context, g1331/opencode-magic-context, aerovato/magic-compact, kdcokenny/opencode-background-agents, code-yeongyu/oh-my-openagent, [REDACTED-caveman].

Verification labels used exactly: Verified / Partially verified / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved. "Confidence" is High/Medium/Low about record accuracy (not about whether the product works).

Per-record mechanism field values: local index / external service / vector DB / graph DB / AST / direct retrieval / hybrid / benchmark, as documented.

---

## A. CONTEXT AND MEMORY

### A1. Mem0 (mem0ai/mem0)

- **Resource name:** Mem0
- **Canonical identity:** `mem0ai/mem0` (GitHub); mem0.ai
- **Category:** A — Context and Memory (persistent agent memory layer)
- **Type:** Open-source library + self-hosted server + managed cloud platform (+ CLI, agent skills)
- **Official URL:** https://github.com/mem0ai/mem0 · https://mem0.ai · https://docs.mem0.ai
- **Description:** Drop-in persistent memory layer for AI agents and apps. Extracts, stores, and retrieves user/agent memories across sessions, with multi-level memory (User, Session, Agent state) and adaptive personalization.
- **Contents inspected:** Full README text on GitHub (repo details, README outline, Quickstart, benchmark tables, integration docs sections) — primary source read 2026-10-10.
- **Actual capabilities:** Memory add/search/update/delete/history via Python `Memory` class or `MemoryClient` (platform); hybrid multi-signal retrieval (semantic + BM25 keyword + entity matching, entity linking across memories); temporal reasoning in retrieval; agent-generated facts stored first-class; Mem0 Platform (managed) and self-hosted Docker server; CLI (`@mem0/cli`); Agent Skills installable via `npx skills add` for coding assistants incl. OpenCode; evaluations submodule open-sourced; evaluation via LoCoMo/LongMemEval/BEAM self-reported (LoCoMo 92.5, LongMemEval 94.4 with new April-2026 algorithm — vendor-reported).
- **Usage domain:** AI assistants, customer support, healthcare, productivity/gaming, autonomous agents — anything needing cross-session personal memory.
- **Mechanism:** Hybrid — vector DB + BM25 keyword + entity graph/linking; pluggable LLM providers and embedders (defaults: OpenAI gpt-5-mini LLM, text-embedding-3-small).
- **Integration method:** Python SDK (`pip install mem0ai`), npm SDK, REST/server Docker compose, MCP-adjacent plugin directories (`.claude-plugin`, `.cursor-plugin`, `.codex-plugin`), CLI, hosted API.
- **Compatibility:** Works with any LLM via supported providers; integrations documented for LangGraph, CrewAI, ChatGPT browser extension, Strands (`strands-mem0` MemoryStore).
- **Dependencies:** LLM provider + embedding provider (required to function); Qdrant/graph backends for platform tier; Python 3.x / Node.
- **Availability:** Public GitHub repo, active; PyPI `mem0ai`, npm `mem0ai`; Mem0 Platform (managed cloud) and self-hosted server.
- **Maintenance:** Actively maintained — 2,671 commits, 416 releases, 66,891 stars at direct read on 2026-10-10; Y Combinator S24.
- **License:** Apache-2.0 (repo metadata + README).
- **Limitations:** Requires external LLM for extraction (not offline by default); best benchmark numbers are vendor-reported on the managed platform with proprietary optimizations, open-source users should expect directionally similar but not identical numbers (per README); platform graph features are tier-gated.
- **Related resources:** Zep/Graphiti, Letta, LangMem, Cognee, Hindsight, supamem (sibling workstream), opencode-mem (dedup), OpenMemory (by same team, in-repo `openmemory`).
- **Sources:** https://github.com/mem0ai/mem0 (primary, read 2026-10-10); https://github.com/jasonkneen/mem0/blob/HEAD/docs/integrations/strands.mdx; https://www.analyticsvidhya.com/blog/2026/09/github-projects-on-ai-memory/
- **Verification date:** 2026-10-10 · **Label:** Verified · **Confidence:** High

### A2. Zep (managed) / Graphiti (open-source engine)

- **Resource name:** Zep (cloud platform); Graphiti (open-source framework)
- **Canonical identity:** `getzep/graphiti` (GitHub, Apache-2.0); getzep.com
- **Category:** A — Context and Memory (temporal knowledge-graph memory)
- **Type:** Managed cloud service (Zep) + open-source Python framework (Graphiti)
- **Official URL:** https://github.com/getzep/graphiti · https://www.getzep.com
- **Description:** Temporal knowledge graphs for AI agents ("context graphs"): facts carry validity windows, so the graph tracks what is true now vs. what was true before, with full provenance. Zep is the managed product built on Graphiti.
- **Contents inspected:** Full README text on GitHub (repo details, README outline, Graphiti-vs-Zep table, installation, backend support, telemetry) — primary source read 2026-10-10; arXiv paper referenced (arxiv.org/abs/2501.13956).
- **Actual capabilities:** Incremental real-time graph construction from conversational and structured data (episodes → entities/facts); bi-temporal fact management with automatic invalidation; prescribed (Pydantic) and learned ontologies; hybrid retrieval (semantic embeddings + BM25 keyword + graph traversal); MCP server in-repo; REST service; pluggable graph backends: Neo4j, FalkorDB (incl. embedded falkordblite), Amazon Neptune, Kuzu (deprecated, upstream unmaintained); optional LLM providers as extras (Anthropic, Groq, Google Gemini); Zep Cloud claims sub-200ms P95 retrieval at large scale and adds user/conversation management, dashboard visualization, Python/TypeScript/Go SDKs.
- **Usage domain:** Production agent memory: customer support, personalization, decision-making, compliance/auditing where temporal reasoning matters.
- **Mechanism:** Graph DB (temporal) + vector embeddings + keyword index; hybrid retrieval; incremental updates without batch recomputation.
- **Integration method:** Python package `graphiti-core` (pip/uv); Docker Compose; MCP server; Zep via REST + SDKs (`zep-cloud`).
- **Compatibility:** Works with any LLM supporting structured output (OpenAI, Anthropic, Gemini); BYO graph DB.
- **Dependencies:** Graph database (Neo4j/FalkorDB/Neptune); LLM + embedding provider API keys.
- **Availability:** Public GitHub, active; Zep Cloud (managed, freemium tiers) + BYOK/self-hosted.
- **Maintenance:** Actively maintained — 31,590 stars at direct read 2026-10-10; 1,011 commits, 200 releases. Note: Zep Community Edition was deprecated April 2025; the `getzep/zep` repo now hosts examples/integrations; open-source effort concentrates on Graphiti (per third-party research notes, agentscamp zep.md).
- **License:** Apache-2.0 (Graphiti).
- **Limitations:** Self-hosted Graphiti needs a graph DB and LLM; "millions of graphs, sub-200ms" claims are vendor marketing for Zep Cloud, not independently verified; Kuzu backend deprecated.
- **Related resources:** Mem0, Letta, LangMem, Cognee, FalkorDB, Neo4j, Kuzu.
- **Sources:** https://github.com/getzep/graphiti (primary, read 2026-10-10); https://github.com/imtiazrayhan/agentscamp/blob/HEAD/src/content/tools/zep.md; https://github.com/marcusschimizzi/nacre/blob/HEAD/docs/research-agentic-memory-landscape-2026.md
- **Verification date:** 2026-10-10 · **Label:** Verified · **Confidence:** High

### A3. Letta (formerly MemGPT)

- **Resource name:** Letta
- **Canonical identity:** `letta-ai/letta` (GitHub); letta.com
- **Category:** A — Context and Memory (stateful agents with self-editing memory)
- **Type:** Open-source agent platform + managed cloud (stateful agent harness)
- **Official URL:** https://github.com/letta-ai/letta · https://www.letta.com · https://docs.letta.com
- **Description:** Platform for building stateful agents with advanced, agent-managed memory. Based on the MemGPT research (arXiv:2310.08560, UC Berkeley Sky Lab). Core analogy: LLM as OS — context window as RAM, external stores as disk, agent-managed paging.
- **Contents inspected:** Secondary research notes (context-efficient-wiki memgpt-letta.md, SebDuffy structured-memory-layers SKILL.md, clawbot wiki, agentscamp tool entry) — primary README not opened; identity and architecture corroborated across 5+ independent secondary sources.
- **Actual capabilities:** Hierarchical memory: core memory (labeled, always-in-context memory blocks like `human`/`persona`, plus custom/shared blocks, editable by agent and developer), recall memory (searchable conversation history), archival memory (external semantic store for overflow, paged in/out on demand); agent self-editing via memory tools (`core_memory_append`, `core_memory_replace`, `archival_memory_insert`, `archival_memory_search`, `conversation_search`); sleep-time agents consolidate memory in background; state persists server-side keyed by agent_id; model-agnostic (any tool-calling LLM); Letta Evals open-source eval framework (released Oct 2025 per clawbot wiki — not independently verified).
- **Usage domain:** Long-lived conversational agents, personalized assistants, any agent needing persistent self-managed state.
- **Mechanism:** Hybrid — in-context labeled memory blocks + external vector DB (archival) + searchable message history; agent-driven memory tools (self-editing).
- **Integration method:** Self-hosted Docker (`docker run letta/letta`), Python client (`letta-client`), TypeScript client (`@letta-ai/letta-client`), CLI (`@letta-ai/letta-code`), cloud API.
- **Compatibility:** Any tool-calling LLM; embedding via OpenAI or others.
- **Dependencies:** Self-host: Docker; or Letta Cloud API key.
- **Availability:** Public GitHub, active; Letta Cloud (developer platform) + self-hosted.
- **Maintenance:** Actively maintained; ~22k stars cited in 2026 research notes; Apache-2.0.
- **License:** Apache-2.0.
- **Limitations:** Memory quality depends on the underlying model's tool-use discipline; self-hosted setup requires Docker/server ops; eval-framework release claim not independently verified today.
- **Related resources:** MemGPT (original name/research), Mem0, LangMem, Graphiti/Zep, OpenMemory.
- **Sources:** https://github.com/letta-ai/letta (canonical; not directly read today); https://github.com/adamcelove/context-efficient-wiki/blob/HEAD/entities/ai-memory/memgpt-letta.md; https://github.com/sebduffy-prog/sebduffy/blob/HEAD/skills/context-engineering/structured-memory-layers/SKILL.md; https://clawbot.ai/wiki/voice-memory/memgpt-letta-long-term-memory-management.html; https://github.com/mohamedabdallah-14/unslop/blob/HEAD/docs/research/20-memory-personalization/SYNTHESIS.md
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A4. LangMem

- **Resource name:** LangMem
- **Canonical identity:** `langchain-ai/langmem` (GitHub)
- **Category:** A — Context and Memory (long-term memory SDK for agents)
- **Type:** Open-source library (Python)
- **Official URL:** https://github.com/langchain-ai/langmem
- **Description:** LangChain's SDK for agentic long-term memory: extract, store, and retrieve semantic (facts/knowledge), episodic (past experiences/events), and procedural (evolving behaviors/prompt updates) memories across threads.
- **Contents inspected:** Secondary research notes (misaelzapata/memoirs memory features doc — detailed per-field identity record; pogan314/logan-mem langmem wiki note; mnemoverse awesome-agent-memory; ankurkumarz solutions table) — primary README not opened.
- **Actual capabilities:** Three memory types: semantic (collections/profiles), episodic (full interaction context → few-shot examples), procedural (updated prompt instructions, via metaprompt/gradient/prompt_memory algorithms); synchronous (hot-path, per-message) or deferred/background extraction (background memory manager consolidates/updates after conversations); agent-controlled search via `create_search_memory_tool`; deletion is opt-in and never automatic; depends on LangGraph `BaseStore` for storage (extraction/consolidation layer, not a standalone DB); works with `InMemoryStore` (dev) or `AsyncPostgresStore` (production).
- **Usage domain:** LangGraph/LangChain agents needing long-term memory without a separate memory service.
- **Mechanism:** Extraction/consolidation layer over LangGraph `BaseStore`; LLM-driven updates; namespace-scoped memory tools; optional vector retrievers for search.
- **Integration method:** pip package; LangGraph-native.
- **Compatibility:** Any LangChain-supported LLM provider; any LangGraph `BaseStore`.
- **Dependencies:** langgraph; vector store of choice.
- **Availability:** Public GitHub, active; MIT.
- **Maintenance:** Actively maintained but small — ~1.4–1.6k stars across notes; last push ~Aug 2026 per one live-API-checked note (pogan314/logan-mem, 2026-08-21).
- **License:** MIT.
- **Limitations:** Tightly coupled to LangChain/LangGraph ecosystem; small community; less battle-tested than Mem0/Graphiti; not a standalone database (storage delegated to BaseStore).
- **Related resources:** langchain/langgraph, langmem's deprecated predecessors (ConversationBufferMemory lineage), Mem0, Letta.
- **Sources:** https://github.com/langchain-ai/langmem (canonical; not directly read today); https://github.com/misaelzapata/memoirs/blob/HEAD/docs/memory_apps_features_part_a.md; https://github.com/pogan314/logan-mem/blob/HEAD/docs/wiki/seed-repos/langmem.md; https://github.com/ankurkumarz/agentic-ai-knowledge-base/blob/HEAD/docs/AgentMemory/solutions.md
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A5. Cognee (incl. cognee-rs)

- **Resource name:** Cognee
- **Canonical identity:** `topoteretes/cognee` (GitHub); cognee.ai; Rust port `topoteretes/cognee-rs`
- **Category:** A — Context and Memory (memory control plane / knowledge-graph memory)
- **Type:** Open-source library (Python) + Rust CLI/port + managed cloud option
- **Official URL:** https://github.com/topoteretes/cognee · https://www.cognee.ai · https://docs.cognee.ai
- **Description:** Open-source AI memory control plane / "knowledge engine" that replaces flat-chunk RAG with structured knowledge graphs via an ECL (Extract → Cognify → Load) pipeline, combining vector and graph retrieval.
- **Contents inspected:** Secondary research (rishabhsharmagit personal-workspace-os cognee research notes — synthesis + ECL detail; iressi awesome-agentic-knowledge-base survey: 16,951 stars, v1.0.3, 2026-05-01; cognee-rs CLI docs); primary README not opened.
- **Actual capabilities:** Minimal public API (`cognee.add`, `cognee.cognify`, `cognee.search`); LLM extracts entity-relation triplets committed as graph edges + parallel vector index; retrieval by graph traversal rather than k-NN alone (multi-hop); Memify post-processing reweights edges, prunes stale nodes, derives relationships (self-improvement loop); pluggable backends: graph store (Kuzu default; Neo4j, FalkorDB, Memgraph, Neptune), vector store (LanceDB default; Pinecone, Qdrant, ChromaDB, pgvector), relational (SQLite default; PostgreSQL); MCP server; integrations for LlamaIndex, LangGraph, LangChain, CrewAI; session + permanent memory types; Rust CLI (`cognee-cli`) with remember/recall/improve/forget verbs.
- **Usage domain:** Agent long-term memory, knowledge graphs over docs/traces/sessions, research/policy evidence graphs (noted deployments: Bayer, University of Wyoming — vendor claims).
- **Mechanism:** Hybrid — graph DB + vector DB + relational store; ECL pipeline; memify consolidation.
- **Integration method:** pip (`cognee`), CLI, MCP server, framework integrations.
- **Compatibility:** Any LLM (pluggable); broad backend choices.
- **Dependencies:** LLM API; chosen graph/vector/relational backends.
- **Availability:** Public GitHub, active; managed offering on cognee.ai.
- **Maintenance:** Actively maintained; ~16–17k stars per May-2026 surveys; Python 3.10–3.14.
- **License:** Apache-2.0 (Python); cognee-rs dual MIT/Apache-2.0.
- **Limitations:** Heavier dependency tree (~30+ extras noted); graph features free at all tiers (vs. gated elsewhere); production-traction numbers are vendor claims.
- **Related resources:** Graphiti/Zep, LangMem, Mem0, Kuzu, FalkorDB, Neo4j, LanceDB.
- **Sources:** https://github.com/topoteretes/cognee (canonical); https://github.com/rishabhsharmagit/personal-workspace-os/blob/HEAD/workspaces/second-brain/research/2026-05-14-cognee-knowledge-graph-memory-for-ai-app.md; https://github.com/irresi/awesome-agentic-knowledge-base/blob/HEAD/surveys/topoteretes__cognee.md; https://github.com/topoteretes/cognee-rs/blob/HEAD/docs/tools/cli.md
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A6. Hindsight

- **Resource name:** Hindsight
- **Canonical identity:** `vectorize-io/hindsight` (GitHub)
- **Category:** A — Context and Memory (long-term agent memory with parallel retrieval)
- **Type:** Open-source memory system
- **Official URL:** https://github.com/vectorize-io/hindsight
- **Description:** Long-term memory system for agents built around remembering, recalling, and reflecting; runs four parallel retrieval strategies per query: semantic search, BM25 keyword matching, graph traversal, and temporal reasoning.
- **Contents inspected:** Listings in mnemoverse awesome-agent-memory and analyticsvidhya 2026 agent-memory roundup — not researched in depth.
- **Actual capabilities:** Per secondary: four-strategy retrieval; long-term memory and reflection orientation. Benchmark runs on LoCoMo/LongMemEval tracked in zytech97/awesome-agent-memory-bench.
- **Usage domain:** Agents needing robust recall over accumulated experience.
- **Mechanism:** Hybrid — semantic + BM25 + graph + temporal.
- **Integration method:** Not verified.
- **Compatibility:** Not verified.
- **Dependencies:** Not verified.
- **Availability:** Public GitHub.
- **Maintenance:** Not verified in depth; appears active in 2026 benchmark-tracking lists.
- **License:** MIT (per mnemoverse listing).
- **Limitations:** Depth of this record limited to secondary listings.
- **Related resources:** Mem0, LangMem, Zep, Mnemis.
- **Sources:** https://github.com/vectorize-io/hindsight (canonical); https://github.com/mnemoverse/awesome-agent-memory/blob/HEAD/README.md; https://www.analyticsvidhya.com/blog/2026/09/github-projects-on-ai-memory/; https://github.com/zytech97/awesome-agent-memory-bench
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A7. A-Mem

- **Resource name:** A-Mem (Agentic Memory)
- **Canonical identity:** `agiresearch/A-mem` (GitHub)
- **Category:** A — Context and Memory (agentic, Zettelkasten-inspired memory)
- **Type:** Open-source research project/library
- **Official URL:** https://github.com/agiresearch/A-mem
- **Description:** Agentic memory system inspired by Zettelkasten note-taking; builds evolving, interconnected knowledge-note networks that the agent curates over time.
- **Contents inspected:** Listings in mnemoverse awesome-agent-memory and mem0 community references — not researched in depth.
- **Actual capabilities:** Per secondary: Zettelkasten-style evolving note network for agents; memory evolution over interactions.
- **Usage domain:** Research/experimental agentic memory.
- **Mechanism:** Graph-like note network; hybrid (documented as agentic memory).
- **Integration method:** Not verified.
- **Compatibility:** Not verified.
- **Dependencies:** LLM provider (per project design).
- **Availability:** Public GitHub; ~2.6k stars per 2025 listings.
- **Maintenance:** Not verified in depth.
- **License:** Not verified.
- **Limitations:** Depth of this record limited to secondary listings; research-grade.
- **Related resources:** Zettelkasten workflows, Mem0, Letta.
- **Sources:** https://github.com/agiresearch/A-mem (canonical); https://github.com/mnemoverse/awesome-agent-memory/blob/HEAD/README.md
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A8. Qdrant

- **Resource name:** Qdrant
- **Canonical identity:** `qdrant/qdrant` (GitHub); qdrant.tech
- **Category:** A — Context and Memory (vector database)
- **Type:** Open-source vector search engine + managed cloud
- **Official URL:** https://github.com/qdrant/qdrant · https://qdrant.tech
- **Description:** High-performance vector database written in Rust, built around HNSW indexing with rich payload filtering.
- **Contents inspected:** General web-research survey level — primary README not opened this session.
- **Actual capabilities:** Filter-aware HNSW search (filters applied during traversal), quantization (scalar/binary/product) for memory efficiency, sharding and distributed deployment, payload metadata + filtering, sparse + dense hybrid, snapshots; Qdrant Cloud managed offering; Edge/minimal builds.
- **Usage domain:** Vector memory backing for agents, RAG retrieval layers, semantic search.
- **Mechanism:** Vector DB (local self-host or external managed service).
- **Integration method:** REST/gRPC API, official clients (Python, JS/TS, Rust, Go, .NET, Java), Docker.
- **Compatibility:** Integrations with LlamaIndex, LangChain, Haystack, Mem0 stack (documented ecosystem).
- **Dependencies:** None (self-contained binary); optional cluster peers.
- **Availability:** Public GitHub, active; Qdrant Cloud managed.
- **Maintenance:** Actively maintained; large community (stars not re-verified this session).
- **License:** Apache-2.0.
- **Limitations:** Self-hosted cluster ops for large scale; licensing of some cloud-adjacent components should be checked per deployment.
- **Related resources:** Weaviate, Milvus, Chroma, LanceDB, pgvector, Pinecone.
- **Sources:** https://github.com/qdrant/qdrant (canonical); https://qdrant.tech (product docs)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A9. Weaviate

- **Resource name:** Weaviate
- **Canonical identity:** `weaviate/weaviate` (GitHub); weaviate.io
- **Category:** A — Context and Memory (vector database)
- **Type:** Open-source vector database + managed cloud
- **Official URL:** https://github.com/weaviate/weaviate · https://weaviate.io
- **Description:** Vector database written in Go with a module system for vectorizers, rerankers, and generative modules.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Hybrid search (BM25 keyword + vector), module system (text2vec vectorizers for many providers, rerankers, generative Q&A modules), GraphQL + REST APIs, multi-tenancy, replication/sharding, Weaviate Cloud managed.
- **Usage domain:** RAG retrieval layers, semantic search, agent knowledge stores.
- **Mechanism:** Vector DB (self-host or managed service).
- **Integration method:** REST/GraphQL/gRPC APIs; clients (Python, TS, Go, Java); Docker/Kubernetes.
- **Compatibility:** Ecosystem integrations (LangChain, LlamaIndex, Haystack).
- **Dependencies:** None required self-hosted.
- **Availability:** Public GitHub, active; Weaviate Cloud managed.
- **Maintenance:** Actively maintained.
- **License:** BSD-3-Clause (core).
- **Limitations:** Generative-search modules couple retrieval to LLM providers (cost/latency); module maturity varies.
- **Related resources:** Qdrant, Milvus, Chroma, pgvector.
- **Sources:** https://github.com/weaviate/weaviate (canonical); https://weaviate.io (product docs)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A10. Chroma

- **Resource name:** Chroma
- **Canonical identity:** `chroma-core/chroma` (GitHub); trychroma.com
- **Category:** A — Context and Memory (embedded vector database)
- **Type:** Open-source library (Python-first)
- **Official URL:** https://github.com/chroma-core/chroma · https://www.trychroma.com
- **Description:** Embedded, Python-first vector database aimed at AI-native developers; in-process or client/server modes.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Collections, metadata filtering, pluggable embedding functions (incl. local defaults), persistent local storage, client/server mode, JS client.
- **Usage domain:** Prototyping agent memory and RAG; local-first vector memory.
- **Mechanism:** Vector DB (local index — embedded in-process, or client/server).
- **Integration method:** Python/JS SDK (`pip install chromadb`), HTTP server mode.
- **Compatibility:** LangChain, LlamaIndex integrations.
- **Dependencies:** Python; optional ONNX runtime for default embeddings.
- **Availability:** Public GitHub, active; Chroma Cloud/hosted options exist.
- **Maintenance:** Actively maintained.
- **License:** Apache-2.0.
- **Limitations:** Not designed for massive distributed scale; single-source 2026 claim of a "Context Rot" discussion in Chroma circles is noted but not verified in depth — Unresolved.
- **Related resources:** LanceDB, Qdrant, Mem0 (uses Qdrant in platform).
- **Sources:** https://github.com/chroma-core/chroma (canonical); https://www.trychroma.com
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A11. LanceDB

- **Resource name:** LanceDB
- **Canonical identity:** `lancedb/lancedb` (GitHub); lancedb.com
- **Category:** A — Context and Memory (embedded multimodal vector database)
- **Type:** Open-source library (Python/JS/Rust)
- **Official URL:** https://github.com/lancedb/lancedb · https://lancedb.com
- **Description:** Embedded, serverless vector database built on the Lance columnar format (Apache Arrow-compatible), with hybrid full-text search.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Embedded zero-ops vector search, multimodal storage (vectors + images + blobs in Lance format), hybrid FTS (Tantivy-based) + vector, versioning via Lance; LanceDB Cloud managed; used as Cognee's default vector backend.
- **Usage domain:** Local-first agent memory, RAG over multimodal data.
- **Mechanism:** Vector DB (local index — embedded; optional cloud).
- **Integration method:** Python/JS/Rust SDKs; object-storage-backed tables.
- **Compatibility:** LangChain, LlamaIndex; Cognee default vector store.
- **Dependencies:** None (embedded); object storage optional.
- **Availability:** Public GitHub, active; LanceDB Cloud.
- **Maintenance:** Actively maintained.
- **License:** Apache-2.0.
- **Limitations:** Embedded model limits horizontal scaling (cloud tier for scale).
- **Related resources:** Chroma, Qdrant, Cognee, Tantivy.
- **Sources:** https://github.com/lancedb/lancedb (canonical); https://lancedb.com
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A12. pgvector

- **Resource name:** pgvector
- **Canonical identity:** `pgvector/pgvector` (GitHub)
- **Category:** A — Context and Memory (vector extension for Postgres)
- **Type:** Open-source Postgres extension
- **Official URL:** https://github.com/pgvector/pgvector
- **Description:** Open-source vector similarity extension for PostgreSQL; brings vector search into existing relational deployments.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** `vector` data type; exact and approximate nearest-neighbor search; HNSW and IVFFlat indexes; distance operators (L2, inner product, cosine); works alongside relational filters/joins; widely adopted by memory frameworks as optional backend (Cognee, LangMem's Postgres store).
- **Usage domain:** Agent memory where Postgres already exists; hybrid relational+vector retrieval.
- **Mechanism:** Vector index inside Postgres (local index).
- **Integration method:** Postgres extension (`CREATE EXTENSION vector`); any Postgres client/driver.
- **Compatibility:** PostgreSQL 11+ (version support per release); Supabase/Neon/RDS pgvector variants.
- **Dependencies:** PostgreSQL.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** PostgreSQL license (permissive).
- **Limitations:** Index build times and recall tuning at very large scale; not a standalone distributed vector engine.
- **Related resources:** Supabase pgvector, Neon, Cognee, LangMem (AsyncPostgresStore).
- **Sources:** https://github.com/pgvector/pgvector (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A13. Milvus

- **Resource name:** Milvus
- **Canonical identity:** `milvus-io/milvus` (GitHub); milvus.io
- **Category:** A — Context and Memory (distributed vector database)
- **Type:** Open-source distributed vector DB + managed cloud (Zilliz)
- **Official URL:** https://github.com/milvus-io/milvus · https://milvus.io
- **Description:** Distributed, cloud-native vector database built for billion-scale similarity search with a wide index menu.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Wide index menu (HNSW, IVF variants, GPU_CAGRA, DiskANN, sparse); scalar filtering; multi-vector/hybrid search; Milvus Lite (embedded single-file Python) for local dev; Attu admin UI; Zilliz Cloud managed.
- **Usage domain:** Large-scale agent/RAG vector memory; billion-vector corpora.
- **Mechanism:** Vector DB (distributed cluster; Milvus Lite = local index).
- **Integration method:** gRPC/REST (pymilvus, Node SDK), Docker Compose / K8s (milvus-operator).
- **Compatibility:** LangChain, LlamaIndex, Haystack, Spark/Flink connectors.
- **Dependencies:** etcd + MinIO/S3 + Pulsar/Kafka for full cluster; Lite needs only Python.
- **Availability:** Public GitHub, active; Zilliz Cloud managed.
- **Maintenance:** Actively maintained (LF AI & Data Foundation).
- **License:** Apache-2.0.
- **Limitations:** Full cluster has significant operational surface; Lite is single-node only.
- **Related resources:** Qdrant, Weaviate, Zilliz, Attu.
- **Sources:** https://github.com/milvus-io/milvus (canonical); https://milvus.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A14. Pinecone

- **Resource name:** Pinecone
- **Canonical identity:** Pinecone (company); pinecone.io
- **Category:** A — Context and Memory (managed vector database)
- **Type:** Proprietary managed service (serverless vector DB)
- **Official URL:** https://www.pinecone.io · https://docs.pinecone.io
- **Description:** Fully managed, serverless vector database; no open-source core — managed-only proprietary service.
- **Contents inspected:** Survey level — product docs not opened this session.
- **Actual capabilities:** Serverless indexes, namespaces for multitenancy, metadata filtering, hybrid dense+sparse search, Pinecone Inference (hosted embedding/rerank models), disaster-recovery namespaces (DRN); supported as optional backend by Cognee and others.
- **Usage domain:** Zero-ops vector memory for agents/RAG.
- **Mechanism:** Vector DB (external managed service only).
- **Integration method:** REST/gRPC API; official SDKs (Python, JS, Go, Java, .NET); ecosystem integrations.
- **Compatibility:** LangChain, LlamaIndex, Haystack, Cognee.
- **Dependencies:** Pinecone account/API key; network.
- **Availability:** Commercial SaaS, active; free tier available (per product docs).
- **Maintenance:** Actively maintained by vendor.
- **License:** Proprietary (no OSS core).
- **Limitations:** Vendor lock-in; data leaves your infrastructure; cost at scale; no self-host.
- **Related resources:** Qdrant Cloud, Weaviate Cloud, Zilliz Cloud, Upstash Vector.
- **Sources:** https://www.pinecone.io (canonical); https://docs.pinecone.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A15. FAISS

- **Resource name:** FAISS (Facebook AI Similarity Search)
- **Canonical identity:** `facebookresearch/faiss` (GitHub); Meta FAIR
- **Category:** A — Context and Memory (similarity-search library)
- **Type:** Open-source library (C++ with Python bindings) — NOT a database
- **Official URL:** https://github.com/facebookresearch/faiss · https://faiss.ai
- **Description:** Library for efficient similarity search and clustering of dense vectors; the foundational ANN toolkit underpinning many vector systems. Library, not a database — no persistence/server layer of its own.
- **Contents inspected:** README content as returned via web search snippets (primary content: "Faiss is a library for efficient similarity search and clustering of dense vectors") — full README not opened this session.
- **Actual capabilities:** Exact + approximate indexes (Flat, IVF, HNSW, PQ/OPQ, LSH, GPU indexes), index composition, on-disk (memory-mapped) indexes, batch search, range search; GPU acceleration.
- **Usage domain:** Embedded ANN inside applications; baseline for benchmarks; powering other vector DBs' techniques.
- **Mechanism:** Local index (in-process library).
- **Integration method:** C++ library; Python wheels (`pip install faiss-cpu` / `faiss-gpu`); conda.
- **Compatibility:** Python 3.x, C++; used inside LangChain/LlamaIndex local vector stores.
- **Dependencies:** BLAS/LAPACK; CUDA for GPU builds; SWIG for bindings build.
- **Availability:** Public GitHub, active.
- **Maintenance:** Maintained by Meta FAIR; widely deployed.
- **License:** MIT (per repo).
- **Limitations:** No server, auth, replication, or filtering engine — you build the database around it; GPU builds need CUDA.
- **Related resources:** ScaNN (Google), Annoy, HNSWLIB, DiskANN.
- **Sources:** https://github.com/facebookresearch/faiss (canonical; README text via search snippet)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A16. OpenAI Embeddings (Embeddings API)

- **Resource name:** OpenAI Embeddings
- **Canonical identity:** OpenAI API — `text-embedding-3-small` / `text-embedding-3-large` / `text-embedding-ada-002` (legacy)
- **Category:** A — Context and Memory (embedding provider)
- **Type:** Proprietary managed API
- **Official URL:** https://platform.openai.com/docs/guides/embeddings
- **Description:** Hosted text-embedding API; the de-facto default embedding provider across agent memory stacks (Mem0 defaults to `text-embedding-3-small`).
- **Contents inspected:** Survey level — API docs not opened this session.
- **Actual capabilities:** Embedding endpoints with configurable dimensions (Matryoshka-style truncation on 3-series); batch input; widely supported as default embedder in frameworks (Mem0, LlamaIndex, LangChain).
- **Usage domain:** Default vectorization layer for agent memory and RAG.
- **Mechanism:** External service (embedding API).
- **Integration method:** REST API; official SDKs; ecosystem defaults.
- **Compatibility:** Universal framework support.
- **Dependencies:** OpenAI API key; network.
- **Availability:** Commercial API, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary API.
- **Limitations:** Data sent to third party; per-token cost; rate limits; no self-host.
- **Related resources:** Voyage AI, Cohere Embed, Jina, Azure OpenAI embeddings.
- **Sources:** https://platform.openai.com/docs/guides/embeddings (canonical); https://github.com/mem0ai/mem0 (default embedder, primary read 2026-10-10)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A17. Voyage AI (embeddings)

- **Resource name:** Voyage AI
- **Canonical identity:** Voyage AI; voyageai.com
- **Category:** A — Context and Memory (embedding provider)
- **Type:** Proprietary managed API (embedding models)
- **Official URL:** https://www.voyageai.com
- **Description:** Embedding-model company (voyage-3 / voyage-3-large / code-3 etc.) positioned on retrieval quality, incl. code-specific embeddings; frequently cited as a quality upgrade over generic embeddings for RAG/code search.
- **Contents inspected:** Survey level — product docs not opened this session.
- **Actual capabilities:** General, code, and multilingual embedding models; rerankers; hosted inference API.
- **Usage domain:** High-quality retrieval for RAG and semantic code search.
- **Mechanism:** External service (embedding API).
- **Integration method:** REST API; ecosystem integrations (LlamaIndex, LangChain, vector DBs).
- **Compatibility:** Broad framework support.
- **Dependencies:** Voyage API key; network.
- **Availability:** Commercial API, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary (model weights/API).
- **Limitations:** Third-party data flow; cost; no self-host of flagship models.
- **Related resources:** OpenAI Embeddings, Cohere Embed, Jina, BGE.
- **Sources:** https://www.voyageai.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A18. Cohere Embed

- **Resource name:** Cohere Embed
- **Canonical identity:** Cohere; cohere.com — `embed-english-v3.0` / `embed-multilingual-v3.0` / Embed 4
- **Category:** A — Context and Memory (embedding provider)
- **Type:** Proprietary managed API
- **Official URL:** https://cohere.com · https://docs.cohere.com/docs/cohere-embed
- **Description:** Cohere's embedding API family, paired with the well-known Cohere Rerank models; a staple of enterprise RAG stacks.
- **Contents inspected:** Survey level — docs not opened this session.
- **Actual capabilities:** Multilingual and English embedding models; input-type hints (search_document/search_query); companion Rerank API used in two-stage retrieval pipelines.
- **Usage domain:** Enterprise RAG retrieval and rerank pipelines.
- **Mechanism:** External service (embedding + rerank APIs).
- **Integration method:** REST API; SDKs; ecosystem integrations.
- **Compatibility:** LangChain, LlamaIndex, vector DBs.
- **Dependencies:** Cohere API key; network.
- **Availability:** Commercial API, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary API.
- **Limitations:** Third-party data flow; cost at scale.
- **Related resources:** OpenAI Embeddings, Voyage AI, Jina Reranker.
- **Sources:** https://docs.cohere.com/docs/cohere-embed (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A19. Jina AI Embeddings

- **Resource name:** Jina AI (embeddings)
- **Canonical identity:** Jina AI; jina.ai — jina-embeddings-v3 / v4, jina-reranker
- **Category:** A — Context and Memory (embedding provider, open-weight models)
- **Type:** Open-weight models + managed API
- **Official URL:** https://jina.ai · https://github.com/jina-ai
- **Description:** Embedding and reranker models with open weights (jina-embeddings series), usable self-hosted or via the Jina Embeddings API; known for multilingual and late-interaction/ColBERT-style retrieval research.
- **Contents inspected:** Survey level — repo/docs not opened this session.
- **Actual capabilities:** Open-weight embedding models (incl. multilingual), rerankers, Reader/Search foundation APIs adjacent to retrieval; models on Hugging Face for self-host.
- **Usage domain:** Self-hostable high-quality embeddings for RAG/agent memory.
- **Mechanism:** Local index (self-hosted weights) or external service (API).
- **Integration method:** Hugging Face weights + sentence-transformers/transformers; REST API.
- **Compatibility:** sentence-transformers ecosystem; LangChain/LlamaIndex.
- **Dependencies:** GPU optional for self-host; API key for managed.
- **Availability:** Public (models + API), active.
- **Maintenance:** Actively maintained.
- **License:** Varies by model (open-weight licenses — check per release; not re-verified here).
- **Limitations:** License terms differ per model release; self-host needs GPU for throughput.
- **Related resources:** BGE, E5, Nomic, sentence-transformers.
- **Sources:** https://jina.ai (canonical); https://github.com/jina-ai (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A20. Open-source embedding model families

- **Resource name:** Open embedding families — sentence-transformers, BGE, E5, Nomic, mixedbread-ai, GTE, Qwen3-Embedding, NV-Embed
- **Canonical identity:** Multiple: `UKPLab/sentence-transformers`; `BAAI/bge-*`; `intfloat/e5-*` (Microsoft); `nomic-ai/nomic-embed-*`; `mixedbread-ai/mxbai-embed-*`; `Alibaba-NLP/gte-*`; `Qwen/Qwen3-Embedding-*`; `nvidia/NV-Embed-*`
- **Category:** A — Context and Memory (embedding models, open weights)
- **Type:** Open-weight models + libraries
- **Official URL:** https://www.sbert.net · https://huggingface.co/BAAI · https://huggingface.co/nomic-ai · https://huggingface.co/mixedbread-ai · https://huggingface.co/Qwen
- **Description:** The open-weight embedding ecosystem that powers self-hosted agent memory: sentence-transformers (the standard library), and model families — BGE (BAAI), E5 (Microsoft), Nomic Embed, mxbai (mixedbread), GTE (Alibaba), Qwen3-Embedding, NV-Embed (NVIDIA) — traded off on MTEB leaderboards and adopted as defaults across RAG stacks.
- **Contents inspected:** Survey level — individual model cards not opened this session.
- **Actual capabilities:** Pretrained text (and some code/multimodal) embedding models with Matryoshka/truncatable dimensions; runnable locally via sentence-transformers/transformers; standard backends for Chroma, LanceDB, Qdrant self-host, Mem0 OSS, Cognee.
- **Usage domain:** Self-hosted vectorization for agent memory and RAG; offline/private deployments.
- **Mechanism:** Local index (self-hosted model inference).
- **Integration method:** Hugging Face Hub weights; sentence-transformers/transformers; ONNX exports.
- **Compatibility:** Python ecosystem; vector DB embedding-function hooks.
- **Dependencies:** Python; GPU optional.
- **Availability:** Public (Hugging Face), active; new generations through 2025–2026 (Qwen3-Embedding).
- **Maintenance:** Actively maintained by respective orgs.
- **License:** Varies: Apache-2.0 or MIT for most (BGE, E5, sentence-transformers, mxbai); check per model (NV-Embed has NVIDIA-specific terms) — not re-verified per model here.
- **Limitations:** Quality/cost tradeoff vs. proprietary APIs; per-model license checks needed; versioning churn on leaderboards.
- **Related resources:** Jina embeddings, Voyage AI, OpenAI Embeddings, MTEB leaderboard.
- **Sources:** https://www.sbert.net (canonical); https://huggingface.co/BAAI; https://huggingface.co/nomic-ai; https://huggingface.co/Qwen
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A21. LlamaIndex

- **Resource name:** LlamaIndex
- **Canonical identity:** `run-llama/llama_index` (GitHub); llamaindex.ai
- **Category:** A — Context and Memory (RAG framework / data framework for LLMs)
- **Type:** Open-source framework (Python + TypeScript)
- **Official URL:** https://github.com/run-llama/llama_index · https://docs.llamaindex.ai
- **Description:** Data framework for connecting LLMs to external data: document ingestion, indexing, and query engines for RAG and agentic retrieval.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** 160+ data connectors/loaders; node parsing/chunking; index structures (vector, tree, keyword, knowledge-graph); query engines with routing; hybrid retrieval; agents (ReAct) over indexes; LlamaParse (document parsing service); LlamaCloud managed platform; integrations for Cognee and others.
- **Usage domain:** RAG pipelines, document-grounded agents, knowledge assistants.
- **Mechanism:** Hybrid — document ingestion + vector DB / graph / keyword indexes; direct retrieval.
- **Integration method:** pip (`llama-index`), npm (`llamaindex`); LlamaCloud managed.
- **Compatibility:** 40+ LLM providers, 50+ vector stores.
- **Dependencies:** LLM + embedding provider; chosen vector store.
- **Availability:** Public GitHub, active; LlamaCloud managed.
- **Maintenance:** Actively maintained; ~44k stars per 2026 surveys (not re-verified today).
- **License:** MIT.
- **Limitations:** Framework breadth means API churn across versions; managed parsing (LlamaParse) is commercial.
- **Related resources:** LangChain, Haystack, Cognee, LlamaParse, RAGFlow.
- **Sources:** https://github.com/run-llama/llama_index (canonical); https://docs.llamaindex.ai
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A22. LangChain retrieval layer (incl. LangGraph)

- **Resource name:** LangChain (retrieval components) / LangGraph
- **Canonical identity:** `langchain-ai/langchain` (GitHub); langchain.com
- **Category:** A — Context and Memory (RAG/retrieval framework) — *cross-cutting with agent-architecture workstream; recorded here for retrieval mechanisms only*
- **Type:** Open-source framework (Python + JS)
- **Official URL:** https://github.com/langchain-ai/langchain · https://python.langchain.com/docs/how_to/#retrievers
- **Description:** The retriever/document-loader/vector-store abstraction layer of the LangChain ecosystem: standardized interfaces over 100+ retrievers and vector stores, plus LangGraph's persistent `BaseStore` (the storage substrate LangMem builds on).
- **Contents inspected:** Survey level — docs not opened this session.
- **Actual capabilities:** Retriever interface (vector, BM25, multi-query, contextual compression, parent-document, ensemble); 100+ integrations; document loaders; text splitters; LangGraph `BaseStore`/`AsyncPostgresStore` persistent namespaced storage for agent memory.
- **Usage domain:** RAG pipelines; agent long-term memory storage substrate.
- **Mechanism:** Abstraction over vector DB / keyword / hybrid / graph retrieval; direct retrieval.
- **Integration method:** pip (`langchain`, `langchain-community`, `langgraph`).
- **Compatibility:** Broadest integration catalog in the ecosystem.
- **Dependencies:** Provider packages per integration.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** MIT.
- **Limitations:** Abstraction overhead; version migration churn (v0.x→v1); quality depends on chosen backends.
- **Related resources:** LlamaIndex, Haystack, LangMem, LangSmith (observability, adjacent).
- **Sources:** https://github.com/langchain-ai/langchain (canonical); https://python.langchain.com/docs/how_to/#retrievers
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A23. Haystack (deepset)

- **Resource name:** Haystack
- **Canonical identity:** `deepset-ai/haystack` (GitHub); haystack.deepset.ai
- **Category:** A — Context and Memory (RAG/agent pipeline framework)
- **Type:** Open-source framework (Python)
- **Official URL:** https://github.com/deepset-ai/haystack · https://haystack.deepset.ai
- **Description:** Component-pipeline framework for RAG and agentic NLP: composable retrievers, converters, rankers, generators wired as DAG pipelines.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Pipeline DAGs of components (converters, chunkers, embedders, retrievers, rerankers, generators, validators); 40+ integrations; Haystack 2.x component model; deepset Cloud managed platform; evaluation components.
- **Usage domain:** Production RAG systems; document-grounded agents.
- **Mechanism:** Pipeline over vector DB / keyword / hybrid retrieval; direct document retrieval.
- **Integration method:** pip (`haystack-ai`, `farm-haystack` legacy); deepset Cloud.
- **Compatibility:** Major LLM providers and vector DBs.
- **Dependencies:** Provider packages per component.
- **Availability:** Public GitHub, active; deepset Cloud managed.
- **Maintenance:** Actively maintained; ~25k stars per 2026 surveys (not re-verified today).
- **License:** Apache-2.0.
- **Limitations:** Pipeline abstraction learning curve; 1.x→2.x migration.
- **Related resources:** LangChain, LlamaIndex, deepset Cloud.
- **Sources:** https://github.com/deepset-ai/haystack (canonical); https://haystack.deepset.ai
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A24. LoCoMo (benchmark)

- **Resource name:** LoCoMo (Long Conversational Memory benchmark)
- **Canonical identity:** `snap-research/locomo` (GitHub); dataset "locomo10"
- **Category:** A — Context and Memory (memory evaluation benchmark)
- **Type:** Open dataset + evaluation harness
- **Official URL:** https://github.com/snap-research/locomo
- **Description:** Benchmark for very-long conversational memory: locomo10 = 10 conversations averaging ~600 turns / ~9k tokens each, with 1,986 questions testing single/multi-hop reasoning, temporal reasoning, and adversarial unanswerable queries.
- **Contents inspected:** Survey level via benchmark-tracking lists and Mem0's README (which reports LoCoMo scores for its algorithm: 71.4 old → 92.5 new, April 2026 — vendor-reported).
- **Actual capabilities:** Long-dialogue QA tasks over multi-session conversations; used by Mem0 and others to score memory systems.
- **Usage domain:** Evaluating agent memory recall quality.
- **Mechanism:** Benchmark (dataset + metrics).
- **Integration method:** Dataset download; eval scripts.
- **Compatibility:** Model-agnostic evaluation.
- **Dependencies:** Not verified.
- **Availability:** Public.
- **Maintenance:** Static dataset (2024 origin); still cited in 2026 vendor benchmarks.
- **License:** Not verified.
- **Limitations:** Vendor-reported scores (e.g., Mem0's) are self-reported; 10-conversation scale is small by 2026 standards.
- **Related resources:** LongMemEval, BEAM, RULER.
- **Sources:** https://github.com/snap-research/locomo (canonical); https://github.com/zytech97/awesome-agent-memory-bench
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A25. LongMemEval (benchmark)

- **Resource name:** LongMemEval
- **Canonical identity:** `xiaowu0162/LongMemEval` (GitHub); ICLR 2025
- **Category:** A — Context and Memory (memory evaluation benchmark)
- **Type:** Open dataset + evaluation harness (research artifact)
- **Official URL:** https://github.com/xiaowu0162/LongMemEval
- **Description:** 500-question benchmark for long-term conversational memory across extended multi-session histories; presented at ICLR 2025.
- **Contents inspected:** Survey level via benchmark-tracking lists and Mem0's README (reports 67.8 → 94.4 with new algorithm, 98.2 on assistant memory recall — vendor-reported).
- **Actual capabilities:** Tests information extraction, abstention, and multi-session temporal reasoning over long histories.
- **Usage domain:** Evaluating long-term agent memory systems.
- **Mechanism:** Benchmark (dataset + metrics).
- **Integration method:** Dataset + eval scripts.
- **Compatibility:** Model-agnostic.
- **Dependencies:** Not verified.
- **Availability:** Public.
- **Maintenance:** Static research artifact.
- **License:** Not verified.
- **Limitations:** Self-reported vendor scores; fixed 500-question set may saturate.
- **Related resources:** LoCoMo, BEAM, Mem0.
- **Sources:** https://github.com/xiaowu0162/LongMemEval (canonical); https://github.com/zytech97/awesome-agent-memory-bench
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A26. BEAM (benchmark)

- **Resource name:** BEAM (Benchmark for Extended Agentic Memory)
- **Canonical identity:** `mohammadtavakoli78/BEAM` (GitHub) — 2025
- **Category:** A — Context and Memory (memory evaluation benchmark)
- **Type:** Open dataset + evaluation harness
- **Official URL:** https://github.com/mohammadtavakoli78/BEAM
- **Description:** Production-scale memory evaluation over very long histories — up to 1M and 10M tokens — cited in Mem0's April-2026 algorithm announcement (64.1 @1M, 48.6 @10M — vendor-reported).
- **Contents inspected:** Only via Mem0 README benchmark table — not researched in depth.
- **Actual capabilities:** Per secondary: evaluates memory retrieval over million-to-10M-token histories.
- **Usage domain:** Stress-testing agent memory at production scale.
- **Mechanism:** Benchmark.
- **Integration method:** Not verified.
- **Compatibility:** Not verified.
- **Dependencies:** Not verified.
- **Availability:** Public GitHub (2025).
- **Maintenance:** Not verified.
- **License:** Not verified.
- **Limitations:** Single-source (2026) claims; scores cited are vendor-reported; thin independent coverage — Unresolved depth.
- **Related resources:** LoCoMo, LongMemEval, RULER, InfiniteBench.
- **Sources:** https://github.com/mohammadtavakoli78/BEAM (canonical); https://github.com/mem0ai/mem0 (benchmark table, primary read 2026-10-10)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A27. LLMLingua family (prompt/context compression)

- **Resource name:** LLMLingua / LongLLMLingua / LLMLingua-2
- **Canonical identity:** `microsoft/LLMLingua` (GitHub); Microsoft Research
- **Category:** A — Context and Memory (context compression / prompt compression)
- **Type:** Open-source research models + code
- **Official URL:** https://github.com/microsoft/LLMLingua
- **Description:** Family of small-model prompt compressors that prune low-information tokens from prompts before they reach the main LLM — up to ~20× compression reported in papers (EMNLP 2023; ACL 2024 for LongLLMLingua).
- **Contents inspected:** Survey level — papers/code not opened this session.
- **Actual capabilities:** Token-level compression with question-aware coarse-to-fine pruning (LongLLMLingua); task-agnostic compression (LLMLingua-2, no LLM needed at compress time); budget controllers for target ratios.
- **Usage domain:** Context-window management, cost/latency reduction for long prompts and RAG contexts.
- **Mechanism:** Local index/compression — small compressor model filters context (pre-retrieval/post-retrieval compression).
- **Integration method:** pip; Hugging Face compressor checkpoints; integrates into RAG pipelines.
- **Compatibility:** Model-agnostic downstream.
- **Dependencies:** transformers; compressor checkpoint.
- **Availability:** Public GitHub/papers, active research line.
- **Maintenance:** Research artifact; maintained by MSR authors.
- **License:** MIT (per repo).
- **Limitations:** Compression can drop task-critical tokens at high ratios; extra inference step; quality varies by domain.
- **Related resources:** Selective Context, RECOMP, "context pruning" OpenCode plugins (dedup list: opencode-dynamic-context-pruning, aerovato/magic-compact, [REDACTED-caveman]).
- **Sources:** https://github.com/microsoft/LLMLingua (canonical); arXiv EMNLP 2023 / ACL 2024 papers (canonical research record)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### A28. RULER (long-context benchmark)

- **Resource name:** RULER
- **Canonical identity:** `NVIDIA/RULER` (GitHub); NVIDIA; COLM 2024
- **Category:** A — Context and Memory (long-context evaluation)
- **Type:** Open benchmark suite
- **Official URL:** https://github.com/NVIDIA/RULER
- **Description:** Synthetic long-context evaluation suite (13 tasks: retrieval, multi-hop, aggregation, QA) measuring effective context utilization at increasing lengths; v2 noted in 2026 sources.
- **Contents inspected:** Survey level — repo not opened this session.
- **Actual capabilities:** Configurable-length synthetic tasks isolating retrieval vs. reasoning failures in long contexts.
- **Usage domain:** Evaluating LLM long-context claims; guiding context-budget decisions for agents.
- **Mechanism:** Benchmark (synthetic tasks).
- **Integration method:** Eval harness + configs.
- **Compatibility:** Any LLM API.
- **Dependencies:** Python eval stack.
- **Availability:** Public GitHub.
- **Maintenance:** Maintained by NVIDIA; v2 per 2026 notes (single-source — not independently verified).
- **License:** Not verified.
- **Limitations:** Synthetic tasks may not transfer to real agent workloads; v2 details Unresolved.
- **Related resources:** InfiniteBench, LongBench v2, Needle-in-haystack evals.
- **Sources:** https://github.com/NVIDIA/RULER (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### A29. InfiniteBench (long-context benchmark)

- **Resource name:** InfiniteBench
- **Canonical identity:** `OpenBMB/InfiniteBench` (GitHub); OpenBMB
- **Category:** A — Context and Memory (long-context evaluation)
- **Type:** Open benchmark suite
- **Official URL:** https://github.com/OpenBMB/InfiniteBench
- **Description:** Long-context benchmark with 100K+ token contexts across retrieval, reasoning, and dialogue tasks.
- **Contents inspected:** Survey level — repo not opened this session.
- **Actual capabilities:** Tasks (passkey/code retrieval, long-book QA/summarization, dialogue) at 100K+ lengths.
- **Usage domain:** Long-context model evaluation for agent backbones.
- **Mechanism:** Benchmark.
- **Integration method:** Eval harness.
- **Compatibility:** Any LLM API.
- **Dependencies:** Not verified.
- **Availability:** Public GitHub.
- **Maintenance:** Static research artifact (2024).
- **License:** Not verified.
- **Limitations:** Fixed-length tasks; newer models may saturate.
- **Related resources:** RULER, LongBench v2, LoCoMo.
- **Sources:** https://github.com/OpenBMB/InfiniteBench (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

---

## B. REPOSITORY INTELLIGENCE

### B1. Serena

- **Resource name:** Serena
- **Canonical identity:** `oraios/serena` (GitHub); community project (author: Olaf Rausch / oraios)
- **Category:** B — Repository Intelligence (semantic coding agent toolkit / code-intelligence MCP server)
- **Type:** Open-source MCP server + CLI + framework integrations
- **Official URL:** https://github.com/oraios/serena
- **Description:** Free, open-source coding-agent toolkit that turns an LLM into a code specialist: symbol-level code retrieval and editing via Language Server Protocol, exposed as MCP tools (plus an Agno-based agent). Built-in memory system for project knowledge.
- **Contents inspected:** Full README text on GitHub (repo details, README outline, architecture/TOC, installation, configuration, MCP tools sections) — primary source read 2026-10-10.
- **Actual capabilities:** LSP-backed retrieval/editing: `find_symbol`, `find_referencing_symbols`, `replace_symbol_body`, `insert_after_symbol`, `search_for_pattern`; 40+ languages via any LSP; JetBrains plugin backend alternative; built-in project memory (`.serena/memories`); onboarding flow that maps a repo on first run; MCP server, CLI, Agno integration; dashboard.
- **Usage domain:** AI coding agents needing precise, low-token symbol operations instead of full-file reads.
- **Mechanism:** AST/symbol index via LSP (live language-server analysis) + project memory store; direct retrieval of symbols; MCP tool exposure.
- **Integration method:** MCP server config (Claude Code, Codex, OpenCode, etc.); CLI; Docker; `uvx`/pipx.
- **Compatibility:** Any MCP client; 40+ languages; JetBrains IDEs via plugin.
- **Dependencies:** Language servers per language (auto-provisioned); Python/uv.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained — 30,125 stars at direct read 2026-10-10.
- **License:** **GPL-3.0-or-later** (README license badge; repo metadata shows "Other/NOASSERTION" — the README badge is authoritative). **Correction:** some secondary sources list MIT; the primary source says GPL-3.0-or-later.
- **Limitations:** Copyleft license (GPL-3.0) affects derivative/commercial embedding; LSP quality varies by language server; large monorepos need tuning.
- **Related resources:** ast-grep, SCIP, Kythe, ctags, tree-sitter, Chamnan (repo-local memory, related), Aider repo-map.
- **Sources:** https://github.com/oraios/serena (primary, read 2026-10-10)
- **Verification date:** 2026-10-10 · **Label:** Verified (license: Corrected vs. secondary MIT claims) · **Confidence:** High

### B2. ast-grep

- **Resource name:** ast-grep (sg)
- **Canonical identity:** `ast-grep/ast-grep` (GitHub)
- **Category:** B — Repository Intelligence (structural code search and rewriting)
- **Type:** Open-source CLI (+ editor integrations, NAPI/WASM)
- **Official URL:** https://github.com/ast-grep/ast-grep · https://ast-grep.github.io
- **Description:** CLI tool for structural search and rewrite of code using tree-sitter grammars — "grep, but syntax-aware": patterns match AST structure, not text.
- **Contents inspected:** Survey level — primary README not opened this session.
- **Actual capabilities:** Structural pattern search with metavariables (`$A`), rule engine (YAML rules: pattern/constraints/fix), codemod rewriting, JSON output, editor integrations (VS Code, Neovim), pre-commit/lint usage.
- **Usage domain:** Semantic code search, codemods, custom lint rules, codebase exploration for agents.
- **Mechanism:** AST (tree-sitter parsing per file, no persistent index — on-demand analysis).
- **Integration method:** CLI binary (`sg`); NAPI/WASM bindings; editor extensions.
- **Compatibility:** Languages with tree-sitter grammars (dozens).
- **Dependencies:** None (single binary, Rust).
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** MIT (per secondary; not independently re-verified).
- **Limitations:** No cross-file persistent index (per-invocation); grammar quality varies by language.
- **Related resources:** tree-sitter, comby, Semgrep, ripgrep, Serena.
- **Sources:** https://github.com/ast-grep/ast-grep (canonical); https://ast-grep.github.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B3. Sourcegraph Cody context engine (historical)

- **Resource name:** Sourcegraph Cody (context/retrieval engine)
- **Canonical identity:** Sourcegraph; `sourcegraph/cody` (archived), `sourcegraph/sourcegraph` (archived)
- **Category:** B — Repository Intelligence (AI code assistant context engine) — Historical
- **Type:** Proprietary product (formerly open-source components)
- **Official URL:** https://sourcegraph.com/cody (product; repos archived)
- **Description:** Cody's context engine assembled repository context for code AI: notably, Sourcegraph publicly documented **dropping embeddings in Feb 2024** in favor of BM25 + code-graph context — a significant industry datapoint on retrieval for code.
- **Contents inspected:** Secondary coverage only — repos not browsed this session.
- **Actual capabilities (historical):** Context assembly from code graph + keyword (BM25) search after the embedding removal; IDE integrations.
- **Usage domain:** AI code assistance context (historical reference).
- **Mechanism:** Direct retrieval — BM25 keyword + code graph (post-Feb-2024); embeddings explicitly removed.
- **Integration method:** Was: IDE extensions, API.
- **Compatibility:** N/A (historical).
- **Dependencies:** N/A.
- **Availability:** Cody Free/Pro tiers closed Jun–Jul 2025; `sourcegraph/cody` and `sourcegraph/sourcegraph` repos archived (per sibling verification notes).
- **Maintenance:** Archived/discontinued as open artifacts.
- **License:** Was Apache-2.0 for OSS parts (not re-verified).
- **Limitations:** Historical record only; product direction changed (Amp acquisition era).
- **Related resources:** Sourcegraph code search (historical), SCIP, Bloop.
- **Sources:** https://sourcegraph.com/cody; https://github.com/sourcegraph/cody (archived); Sourcegraph Feb-2024 embeddings-removal announcement (secondary coverage)
- **Verification date:** 2026-10-10 · **Label:** Historical · **Confidence:** Medium

### B4. Aider repo-map

- **Resource name:** Aider repository map
- **Canonical identity:** `Aider-AI/aider` (GitHub) — repo-map subsystem
- **Category:** B — Repository Intelligence (repository map for coding agents)
- **Type:** Open-source subsystem of a coding agent (Python)
- **Official URL:** https://github.com/Aider-AI/aider · https://aider.chat/docs/repomap.html
- **Description:** Aider's repo-map: a compact whole-repository summary (definitions + call signatures ranked by personalized PageRank over the call graph) injected into the agent's context so file selection stays token-efficient.
- **Contents inspected:** Survey level via aider docs/secondary — source not opened this session.
- **Actual capabilities:** tree-sitter AST extraction of definitions/signatures; personalized PageRank over the reference graph seeded from mentioned files; `--map-tokens` budget (default 1024); refresh on file changes; ctags fallback for unsupported languages.
- **Usage domain:** Coding-agent repository orientation; low-token whole-repo context.
- **Mechanism:** AST (tree-sitter) + graph ranking (PageRank) — computed on demand, no persistent DB.
- **Integration method:** Built into Aider; invocable via CLI flags; algorithm reused/imitated by other agent tools.
- **Compatibility:** Languages with tree-sitter grammars; ctags fallback.
- **Dependencies:** tree-sitter, networkx (PageRank), grep-ast.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** Apache-2.0 (Aider).
- **Limitations:** Heuristic ranking; token budget truncates large repos; no semantic understanding.
- **Related resources:** repomix, gitingest, Serena, Graphify-Labs/graphify (dedup — cross-ref).
- **Sources:** https://github.com/Aider-AI/aider (canonical); https://aider.chat/docs/repomap.html
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B5. repomix

- **Resource name:** repomix
- **Canonical identity:** `yamadashy/repomix` (GitHub)
- **Category:** B — Repository Intelligence (repository packaging / repo-to-prompt)
- **Type:** Open-source CLI + MCP server
- **Official URL:** https://github.com/yamadashy/repomix
- **Description:** Packs a repository into a single AI-friendly file (XML/markdown/plain) with file tree, respecting .gitignore; exposes an MCP server mode for agents.
- **Contents inspected:** Survey level via listings — README not opened this session.
- **Actual capabilities:** Repo → single-file pack with configurable include/exclude, compression/token-count estimation, remote GitHub URL packing, MCP server mode.
- **Usage domain:** Feeding whole repos to LLMs; repo summarization inputs.
- **Mechanism:** Direct retrieval (file walk + concatenation; no index).
- **Integration method:** CLI (`npx repomix`); MCP server config.
- **Compatibility:** Any repo; MCP clients.
- **Dependencies:** Node.js.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** MIT (per secondary; not independently re-verified).
- **Limitations:** No semantic selection — size-bounded; token costs for large repos.
- **Related resources:** gitingest, Aider repo-map, Serena.
- **Sources:** https://github.com/yamadashy/repomix (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B6. gitingest

- **Resource name:** gitingest
- **Canonical identity:** `cyclotruc/gitingest` (GitHub)
- **Category:** B — Repository Intelligence (repository digest / repo-to-prompt)
- **Type:** Open-source tool (Python)
- **Official URL:** https://github.com/cyclotruc/gitingest
- **Description:** Turns any Git repository (URL or path) into a digest: directory tree + file contents formatted for LLM ingestion, with include/exclude patterns.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** URL/path ingestion, tree + content digest, pattern filtering, token counting.
- **Usage domain:** Quick repo-to-prompt digests for analysis/Q&A.
- **Mechanism:** Direct retrieval (no index).
- **Integration method:** CLI; Python API.
- **Compatibility:** Git repos.
- **Dependencies:** Python; git.
- **Availability:** Public GitHub.
- **Maintenance:** Community-maintained.
- **License:** MIT (per secondary; not independently re-verified).
- **Limitations:** No semantic filtering; large repos produce huge digests.
- **Related resources:** repomix, Aider repo-map.
- **Sources:** https://github.com/cyclotruc/gitingest (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### B7. Universal Ctags

- **Resource name:** Universal Ctags
- **Canonical identity:** `universal-ctags/ctags` (GitHub)
- **Category:** B — Repository Intelligence (symbol indexing)
- **Type:** Open-source CLI (C)
- **Official URL:** https://github.com/universal-ctags/ctags · https://ctags.io
- **Description:** Maintained ctags implementation generating tag indexes of language objects (functions, classes, variables) across 100+ languages — the classic symbol index behind editor navigation and Aider's repo-map fallback.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Tag file generation (ctags/etags/JSON), 100+ language parsers (regex + dedicated), incremental workflows via editor plugins.
- **Usage domain:** Symbol navigation, lightweight codebase indexing for agents/editors.
- **Mechanism:** Local index (tags file) via source-code analysis (parsers, not full AST for all languages).
- **Integration method:** CLI; editor plugins; consumed by tools (Aider fallback).
- **Compatibility:** 100+ languages; editors (Vim/Emacs/VS Code via plugins).
- **Dependencies:** C toolchain to build; prebuilt binaries available.
- **Availability:** Public GitHub, active.
- **Maintenance:** Community-maintained, active.
- **License:** Not independently re-verified (historically GPLv2+ lineage — treat as Unverified here).
- **Limitations:** Tags are name-based, not semantic (no type-aware references); license needs care for redistribution.
- **Related resources:** tree-sitter, SCIP, Aider repo-map, Serena.
- **Sources:** https://github.com/universal-ctags/ctags (canonical); https://ctags.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B8. tree-sitter

- **Resource name:** tree-sitter
- **Canonical identity:** `tree-sitter/tree-sitter` (GitHub); tree-sitter.github.io
- **Category:** B — Repository Intelligence (incremental parsing framework)
- **Type:** Open-source library + grammar ecosystem (C/Rust)
- **Official URL:** https://github.com/tree-sitter/tree-sitter · https://tree-sitter.github.io
- **Description:** Incremental parsing library with a large ecosystem of language grammars; produces concrete syntax trees with error recovery — the substrate for ast-grep, Aider repo-map, and many agent code tools.
- **Contents inspected:** Survey level (Wikipedia + GitHub org noted in research) — primary README not opened this session.
- **Actual capabilities:** Fast incremental re-parsing, error-tolerant concrete syntax trees, query language (S-expressions) for pattern matching, WASM builds, grammar DSL.
- **Usage domain:** Syntax-aware tooling: search, highlighting, codemods, repo mapping.
- **Mechanism:** AST (on-demand parsing; no persistent index itself).
- **Integration method:** C/Rust library; WASM; bindings (Python, JS, Go, etc.); CLI.
- **Compatibility:** 100+ community grammars.
- **Dependencies:** C compiler for grammars.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** MIT.
- **Limitations:** Concrete (not abstract) syntax trees; grammar quality varies; no name resolution/type info.
- **Related resources:** ast-grep, Aider repo-map, comby, Helix/Neovim (editors).
- **Sources:** https://github.com/tree-sitter/tree-sitter (canonical); https://tree-sitter.github.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B9. SCIP (Sourcegraph Code Intelligence Protocol)

- **Resource name:** SCIP
- **Canonical identity:** `sourcegraph/scip` (GitHub); Sourcegraph
- **Category:** B — Repository Intelligence (code-intelligence index format/protocol)
- **Type:** Open protocol + indexers (protobuf schema)
- **Official URL:** https://github.com/sourcegraph/scip
- **Description:** Language-agnostic protocol for indexing code intelligence (definitions, references, hover, diagnostics); per-language indexers emit SCIP indexes consumed by code hosts and IDEs.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Protobuf schema for occurrences/symbols; indexer implementations per language (scip-java, scip-python, scip-typescript, etc.); powers precise code navigation.
- **Usage domain:** Precise cross-repo code navigation; indexer backend for code search UIs.
- **Mechanism:** Local index (SCIP index files) via source-code analysis (compiler-accurate where indexers hook into build).
- **Integration method:** Indexer CLIs in CI; index consumers (Sourcegraph, editors).
- **Compatibility:** Languages with SCIP indexers (Java, Python, TS/JS, Go, Rust, C++, etc.).
- **Dependencies:** Language toolchains for compiler-accurate indexers.
- **Availability:** Public GitHub; Sourcegraph archived its main repos in 2025 — SCIP protocol/indexers status should be re-checked (Unresolved as of this write).
- **Maintenance:** Unresolved (Sourcegraph archival wave 2025).
- **License:** Not independently re-verified.
- **Limitations:** Indexer coverage uneven; build integration needed for precision.
- **Related resources:** Kythe, LSIF (predecessor), Serena, Sourcegraph Cody (historical).
- **Sources:** https://github.com/sourcegraph/scip (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### B10. Kythe

- **Resource name:** Kythe
- **Canonical identity:** `kythe/kythe` (GitHub); Google; kythe.io
- **Category:** B — Repository Intelligence (pluggable code-intelligence platform)
- **Type:** Open-source platform (indexers + serving)
- **Official URL:** https://github.com/kythe/kythe · https://kythe.io
- **Description:** Google's pluggable system for code intelligence: language-agnostic graph schema with build-integrated indexers producing cross-reference data for navigation and analysis.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Extraction during builds (build-system integration), language-neutral graph schema, serving pipeline for xrefs/hover/documentation, Verifier for indexer testing.
- **Usage domain:** Large-scale precise code intelligence (Google-internal heritage).
- **Mechanism:** Graph DB-ish index (Kythe graph) via source-code analysis (build-integrated).
- **Integration method:** Bazel/CMake build integration; serving stack.
- **Compatibility:** C++, Java, Go, Python, TypeScript, Protobuf, etc.
- **Dependencies:** Build system integration; significant setup.
- **Availability:** Public GitHub; pre-1.0, slow-moving.
- **Maintenance:** Low activity in recent years (not re-verified today).
- **License:** Apache-2.0 (per secondary; not independently re-verified).
- **Limitations:** Heavy setup; build integration required; not agent-oriented out of the box.
- **Related resources:** SCIP, CodeQL, Joern.
- **Sources:** https://github.com/kythe/kythe (canonical); https://kythe.io
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### B11. CodeQL

- **Resource name:** CodeQL
- **Canonical identity:** `github/codeql` (GitHub); GitHub
- **Category:** B — Repository Intelligence (semantic code analysis / data-flow)
- **Type:** Open-source engine + query packs (GitHub Advanced Security commercial tier for private repos)
- **Official URL:** https://github.com/github/codeql · https://codeql.github.com
- **Description:** Semantic code analysis engine: builds relational snapshots of codebases and queries them in QL (datalog-like) for vulnerabilities, data-flow, and architecture questions; 11+ languages.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Database creation per codebase snapshot; QL queries for taint tracking, data-flow, control-flow; 2000+ bundled security queries; variant analysis across repos; code scanning integration.
- **Usage domain:** Security auditing, data-flow analysis, architecture/dependency queries.
- **Mechanism:** Local index (CodeQL database — relational snapshot) via source-code analysis.
- **Integration method:** CLI; GitHub code scanning; VS Code extension.
- **Compatibility:** 11+ languages (per research notes).
- **Dependencies:** Language toolchains for DB creation.
- **Availability:** Public engine/queries; GHAS commercial for private repos.
- **Maintenance:** Actively maintained by GitHub.
- **License:** CodeQL engine/queries under GitHub's CodeQL license terms (not simple OSS — check per use; not re-verified here).
- **Limitations:** Database build cost on large repos; QL learning curve; license nuances for commercial use.
- **Related resources:** Joern, Semgrep, Kythe.
- **Sources:** https://github.com/github/codeql (canonical); https://codeql.github.com
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B12. Joern

- **Resource name:** Joern
- **Canonical identity:** `joernio/joern` (GitHub)
- **Category:** B — Repository Intelligence (code property graph platform)
- **Type:** Open-source platform (Scala)
- **Official URL:** https://github.com/joernio/joern · https://joern.io
- **Description:** Open-source code analysis platform building Code Property Graphs (AST + CFG + DDG fused) queryable via a Scala DSL; the "code knowledge graph" approach for deep program analysis.
- **Contents inspected:** README content via search snippets (primary text) — full README not opened this session.
- **Actual capabilities:** CPG construction for 10+ languages; interactive Scala/DSL queries (joern-scan); data-flow/taint queries; flatgraph v4 storage; import/export; used in vuln research.
- **Usage domain:** Deep static analysis, vulnerability research, architecture extraction.
- **Mechanism:** Graph DB (flatgraph-backed CPG, local) via source-code analysis.
- **Integration method:** CLI/REPL; Scala API; Docker.
- **Compatibility:** 10+ languages (C/C++, Java, JS, Python, Go, etc. — per notes).
- **Dependencies:** JVM; language frontends.
- **Availability:** Public GitHub, active.
- **Maintenance:** Actively maintained.
- **License:** Not independently re-verified (Apache-2.0 lineage per secondary — treat as Unverified here).
- **Limitations:** JVM/Scala learning curve; CPG build time/memory on large codebases.
- **Related resources:** CodeQL, Semgrep, Kythe, Graphify-Labs/graphify (dedup — cross-ref).
- **Sources:** https://github.com/joernio/joern (canonical; README text via search snippet)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B13. Semgrep

- **Resource name:** Semgrep
- **Canonical identity:** `semgrep/semgrep` (GitHub); Semgrep Inc.
- **Category:** B — Repository Intelligence (semantic code search / SAST)
- **Type:** Open-source engine (OSS) + commercial platform (Semgrep Cloud)
- **Official URL:** https://github.com/semgrep/semgrep · https://semgrep.dev
- **Description:** Semantic code search and static analysis with YAML-defined patterns over ASTs; taint mode for data-flow; large public rule registry.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** YAML pattern rules (search + autofix), taint tracking, secrets detection, supply-chain, 30+ languages, CI integration, rule registry (1000s of rules).
- **Usage domain:** Security scanning, semantic code search, custom lint/codemod rules.
- **Mechanism:** AST (on-demand scanning; no persistent index).
- **Integration method:** CLI (`semgrep`); CI; editor extensions; Semgrep Cloud Platform.
- **Compatibility:** 30+ languages.
- **Dependencies:** None for OSS CLI (single binary distribution).
- **Availability:** Public GitHub, active; commercial platform.
- **License:** Engine LGPL-2.1 (Dec 2024 relicense noted in research — per secondary; not independently re-verified); rules registry licensing varies.
- **Limitations:** Deep data-flow needs Pro engine for some features; rule authoring learning curve.
- **Related resources:** OpenGrep (community fork), CodeQL, ast-grep, comby.
- **Sources:** https://github.com/semgrep/semgrep (canonical); https://semgrep.dev
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### B14. OpenGrep

- **Resource name:** OpenGrep
- **Canonical identity:** `opengrep/opengrep` (GitHub); community fork
- **Category:** B — Repository Intelligence (semantic code search / SAST)
- **Type:** Open-source community fork of Semgrep OSS
- **Official URL:** https://github.com/opengrep/opengrep · https://opengrep.dev
- **Description:** Community fork of the Semgrep open-source engine, stewarded by a vendor consortium after Semgrep's licensing/monetization shifts; aims to keep a fully-open AST search engine.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Per secondary: Semgrep-OSS-compatible rule syntax and scanning; community governance.
- **Usage domain:** Same as Semgrep OSS (SAST, semantic search).
- **Mechanism:** AST (on-demand).
- **Integration method:** CLI; CI.
- **Compatibility:** Semgrep rule-compatible (per project claims).
- **Dependencies:** Not verified.
- **Availability:** Public GitHub, active (2025 origin).
- **Maintenance:** Community-maintained.
- **License:** LGPL-2.1 (community fork — per secondary; not independently re-verified).
- **Limitations:** Young fork; rule-registry and engine parity evolving.
- **Related resources:** Semgrep, CodeQL.
- **Sources:** https://github.com/opengrep/opengrep (canonical); https://opengrep.dev
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### B15. comby

- **Resource name:** comby
- **Canonical identity:** `comby-tools/comby` (GitHub)
- **Category:** B — Repository Intelligence (structural search and rewrite)
- **Type:** Open-source CLI (OCaml)
- **Official URL:** https://github.com/comby-tools/comby · https://comby.dev
- **Description:** Template-based structural search-and-rewrite: patterns with holes (`:[x]`) match syntax-aware spans across languages without full parsing.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Match templates with metavariables, rewrite rules, language-aware matching, JSON output.
- **Usage domain:** Codemods, structural search, refactoring.
- **Mechanism:** Source-code analysis (template matching; lighter than full AST).
- **Integration method:** CLI; library.
- **Compatibility:** Many languages via generic matching.
- **Dependencies:** None (binary).
- **Availability:** Public GitHub; maintenance slowed in recent years (not re-verified today).
- **Maintenance:** Low activity (per research notes).
- **License:** Apache-2.0 (per secondary; not independently re-verified).
- **Limitations:** Less precise than full-AST tools; slower maintenance.
- **Related resources:** ast-grep, Semgrep, Coccinelle.
- **Sources:** https://github.com/comby-tools/comby (canonical); https://comby.dev
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### B16. Bloop (archived)

- **Resource name:** Bloop
- **Canonical identity:** `BloopAI/bloop` (GitHub, archived)
- **Category:** B — Repository Intelligence (codebase Q&A / semantic code search) — Archived
- **Type:** Was: open-source codebase Q&A (Rust)
- **Official URL:** https://github.com/BloopAI/bloop (archived)
- **Description:** "Answer questions about your codebase": local semantic code search over repos with an LLM Q&A layer; notable early attempt at repo-scale semantic code search.
- **Contents inspected:** Secondary/archival notes only.
- **Actual capabilities (historical):** Repo indexing, semantic search, GPT-4-powered Q&A over code.
- **Usage domain:** Codebase Q&A (historical reference).
- **Mechanism:** Vector DB + LLM (historical).
- **Integration method:** Was: CLI/app.
- **Compatibility:** N/A (archived).
- **Dependencies:** N/A.
- **Availability:** Archived January 2025; Apache-2.0 code remains readable.
- **Maintenance:** None (archived).
- **License:** Apache-2.0 (code).
- **Limitations:** Dead project; reference value only.
- **Related resources:** Sourcegraph Cody (historical), Serena.
- **Sources:** https://github.com/BloopAI/bloop (archived)
- **Verification date:** 2026-10-10 · **Label:** Archived · **Confidence:** Medium

### B17. Sourcetrail (archived)

- **Resource name:** Sourcetrail
- **Canonical identity:** `CoatiSoftware/Sourcetrail` (GitHub, archived)
- **Category:** B — Repository Intelligence (code visualization / dependency graphs) — Archived
- **Type:** Was: open-source interactive code explorer (C++)
- **Official URL:** https://github.com/CoatiSoftware/Sourcetrail (archived)
- **Description:** Interactive source explorer visualizing call graphs, include graphs, and dependencies; indexed codebases into a local DB for graph navigation.
- **Contents inspected:** Secondary/archival notes only.
- **Actual capabilities (historical):** Full-project indexing, interactive dependency/call graphs, cross-language (C++, Java, Python).
- **Usage domain:** Architecture extraction, onboarding visualization (historical).
- **Mechanism:** Local index (project DB) via source-code analysis.
- **Integration method:** Was: desktop app.
- **Compatibility:** N/A (archived).
- **Dependencies:** N/A.
- **Availability:** Archived 2021 (development ceased; Coati shut down).
- **Maintenance:** None (archived).
- **License:** Was GPL (not re-verified).
- **Limitations:** Dead since 2021; reference value only.
- **Related resources:** Joern, CodeQL, modern IDE call hierarchies.
- **Sources:** https://github.com/CoatiSoftware/Sourcetrail (archived)
- **Verification date:** 2026-10-10 · **Label:** Archived · **Confidence:** Medium

### B18. ripgrep

- **Resource name:** ripgrep (rg)
- **Canonical identity:** `BurntSushi/ripgrep` (GitHub)
- **Category:** B — Repository Intelligence (local code search substrate)
- **Type:** Open-source CLI (Rust)
- **Official URL:** https://github.com/BurntSushi/ripgrep
- **Description:** Line-oriented recursive search tool; the fast text-search substrate underlying countless repo-intelligence pipelines (respecting .gitignore, parallel).
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Regex search, .gitignore-aware, parallel, encoding detection, JSON output, multiline/PCRE2 modes.
- **Usage domain:** Local code search; grep substrate for agent tooling.
- **Mechanism:** Direct retrieval (no index; brute-force parallel scan).
- **Integration method:** CLI; library (grep-regex crate).
- **Compatibility:** All text.
- **Dependencies:** None (single binary).
- **Availability:** Public GitHub, active; v15.2.0 per research notes.
- **Maintenance:** Actively maintained.
- **License:** MIT/UNLICENSE (dual).
- **Limitations:** Text-level only — no syntax/semantic awareness (pair with ast-grep/Serena for that).
- **Related resources:** ast-grep, The Silver Searcher, Serena (uses rg for text fallback).
- **Sources:** https://github.com/BurntSushi/ripgrep (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

---

## C. DOCUMENTATION GROUNDING

### C1. Mintlify

- **Resource name:** Mintlify
- **Canonical identity:** Mintlify; mintlify.com
- **Category:** C — Documentation Grounding (docs platform with AI/agent surfaces)
- **Type:** Proprietary SaaS docs platform
- **Official URL:** https://mintlify.com · https://mintlify.com/docs
- **Description:** Documentation platform that auto-generates agent-consumable surfaces: per-site `llms.txt` / `llms-full.txt` / `skill.md`, plus a per-site MCP server exposing the docs to AI assistants, and AI-traffic analytics.
- **Contents inspected:** Survey level via product pages/secondary — docs not opened this session.
- **Actual capabilities:** Markdown-based docs authoring; auto-generated llms.txt + llms-full.txt + skill.md per site; hosted MCP server per documentation site; AI search/traffic analytics; API reference components.
- **Usage domain:** Vendor docs that need to be agent-readable (versioned, structured).
- **Mechanism:** Direct retrieval (hosted docs + MCP tools over the doc corpus).
- **Integration method:** Mintlify-hosted sites; MCP server URL per site; llms.txt files fetched by agents.
- **Compatibility:** Any MCP client; any HTTP client for llms.txt.
- **Dependencies:** Mintlify subscription (per product pricing).
- **Availability:** Commercial SaaS, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary platform.
- **Limitations:** Vendor lock-in for the MCP/analytics layer; quality depends on docs authoring.
- **Related resources:** llms.txt convention, Fern, ReadMe, GitBook, DeepWiki.
- **Sources:** https://mintlify.com (canonical); https://mintlify.com/docs
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### C2. llms.txt (convention)

- **Resource name:** llms.txt
- **Canonical identity:** llmstxt.org — proposal by Jeremy Howard / Answer.AI, 2024-09-03
- **Category:** C — Documentation Grounding (agent-readable docs convention)
- **Type:** Open convention/proposal (NOT an RFC or standard)
- **Official URL:** https://llmstxt.org
- **Description:** Proposed convention: websites ship `/llms.txt` (a structured index/summary) and `/llms-full.txt` (full content) so LLMs can consume documentation without HTML scraping.
- **Contents inspected:** Survey level — llmstxt.org not opened this session.
- **Actual capabilities:** File-format convention (markdown index + full dump); adoption tooling by docs platforms (Mintlify, Fern auto-generate); `skill.md` variant for agent skills.
- **Usage domain:** Making product/framework docs agent-ingestible.
- **Mechanism:** Direct retrieval (static files over HTTP).
- **Integration method:** Serve files at site root; agents fetch via HTTP.
- **Compatibility:** Any HTTP client/agent.
- **Dependencies:** None.
- **Availability:** Open proposal; growing adoption 2024–2026.
- **Maintenance:** Community convention; not a standards body.
- **License:** N/A (convention).
- **Limitations:** Not a standard — no enforcement; staleness depends on site regeneration; no versioning semantics built in.
- **Related resources:** Mintlify, Fern, ReadMe, llms.txt generators.
- **Sources:** https://llmstxt.org (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Medium

### C3. DeepWiki

- **Resource name:** DeepWiki
- **Canonical identity:** deepwiki.com; Cognition (company)
- **Category:** C — Documentation Grounding (AI-generated repo wikis) — *dedup: cross-reference only; catalogued by MCP workstream*
- **Type:** Proprietary service
- **Official URL:** https://deepwiki.com
- **Description:** Auto-generates browsable wiki-style documentation from GitHub repos (architecture overviews, diagrams, Q&A) — "DeepWiki-style" is the shorthand for repo-to-docs AI services.
- **Contents inspected:** Not researched in depth (dedup).
- **Actual capabilities:** Per secondary: repo → structured wiki with diagrams and ask-questions UI.
- **Usage domain:** Repository understanding/documentation.
- **Mechanism:** Direct retrieval (generated docs) over repo analysis.
- **Integration method:** Web UI; URL pattern per repo.
- **Compatibility:** Public GitHub repos.
- **Dependencies:** None (service-side).
- **Availability:** Commercial service (Cognition), active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary.
- **Limitations:** Generated docs can go stale; private-repo coverage tiered.
- **Related resources:** Mintlify, Kapa.ai, repo summarizers.
- **Sources:** https://deepwiki.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C4. Kapa.ai

- **Resource name:** Kapa.ai
- **Canonical identity:** Kapa.ai; kapa.ai
- **Category:** C — Documentation Grounding (RAG answer engine for docs)
- **Type:** Proprietary SaaS
- **Official URL:** https://www.kapa.ai
- **Description:** RAG-powered technical support/answer engine grounded in a company's docs: ingests 30+ source types (docs, GitHub, Slack/Discord, Stack Overflow) and answers with citations; exposes a hosted MCP server for agent access.
- **Contents inspected:** Survey level — product pages not opened this session.
- **Actual capabilities:** Multi-source ingestion, cited answers, support deflection analytics, hosted MCP endpoint, Slack/Discord bots.
- **Usage domain:** Product support copilots; grounded Q&A over versioned docs.
- **Mechanism:** Vector DB + RAG (external managed service).
- **Integration method:** Hosted widget/API; MCP server; chat integrations.
- **Compatibility:** 30+ source connectors.
- **Dependencies:** Kapa subscription.
- **Availability:** Commercial SaaS, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary.
- **Limitations:** Answer quality bounded by source quality; vendor lock-in; cost.
- **Related resources:** Inkeep, Algolia DocSearch, Mintlify.
- **Sources:** https://www.kapa.ai (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C5. Inkeep

- **Resource name:** Inkeep
- **Canonical identity:** Inkeep; inkeep.com
- **Category:** C — Documentation Grounding (support copilot over docs)
- **Type:** Proprietary SaaS
- **Official URL:** https://inkeep.com
- **Description:** AI support copilot grounded in product documentation and knowledge sources; search + chat + agent handoff for docs-driven support.
- **Contents inspected:** Survey level — product pages not opened this session.
- **Actual capabilities:** Docs-grounded chat/search widgets, source management, analytics.
- **Usage domain:** Docs-driven customer support.
- **Mechanism:** RAG (external managed service).
- **Integration method:** Hosted widget/API.
- **Compatibility:** Docs sites, help centers.
- **Dependencies:** Inkeep subscription.
- **Availability:** Commercial SaaS, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary.
- **Limitations:** Same class limits as Kapa (source quality, lock-in).
- **Related resources:** Kapa.ai, Algolia DocSearch.
- **Sources:** https://inkeep.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C6. Algolia DocSearch

- **Resource name:** Algolia DocSearch
- **Canonical identity:** Algolia DocSearch; docsearch.algolia.com
- **Category:** C — Documentation Grounding (docs search indexing)
- **Type:** Free service for open-source docs (Algolia program)
- **Official URL:** https://docsearch.algolia.com
- **Description:** Free documentation search: Algolia crawls qualifying public docs sites and provides a hosted search index + search UI widget.
- **Contents inspected:** Survey level — program page not opened this session.
- **Actual capabilities:** Crawler configs for docs sites, hosted Algolia index, drop-in search UI, analytics.
- **Usage domain:** Search over versioned framework/library docs.
- **Mechanism:** External service (crawled search index; keyword + typo-tolerant, not vector by default).
- **Integration method:** Apply for program; JS widget; API.
- **Compatibility:** Static docs sites (Docusaurus etc.).
- **Dependencies:** Acceptance into the free program (open-source docs).
- **Availability:** Active program.
- **Maintenance:** Maintained by Algolia.
- **License:** Free for qualifying OSS docs; commercial otherwise.
- **Limitations:** Eligibility-gated; keyword search (not semantic) in classic form; crawl freshness on Algolia's schedule.
- **Related resources:** Kapa.ai, Inkeep, Mintlify search.
- **Sources:** https://docsearch.algolia.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C7. Fern

- **Resource name:** Fern
- **Canonical identity:** Fern; buildwithfern.com
- **Category:** C — Documentation Grounding (API docs + SDK generation)
- **Type:** Proprietary SaaS (+ open-source CLI/generators)
- **Official URL:** https://www.buildwithfern.com · https://github.com/fern-api
- **Description:** Docs platform generating SDKs and documentation from API definitions; noted in research for improved llms.txt output that embeds full OpenAPI specs for agent consumption.
- **Contents inspected:** Survey level — product pages not opened this session.
- **Actual capabilities:** OpenAPI → docs site + typed SDKs (multiple languages); llms.txt generation with full OpenAPI specs; API reference, guides, changelogs.
- **Usage domain:** API-first products needing agent-readable references and SDKs.
- **Mechanism:** Direct retrieval (generated docs/llms.txt); SDK codegen.
- **Integration method:** Fern CLI; GitHub integration; hosted docs.
- **Compatibility:** OpenAPI/AsyncAPI inputs; SDK targets (TS, Python, Java, Go, etc.).
- **Dependencies:** Fern subscription for hosted features.
- **Availability:** Commercial SaaS, active; open-source generators.
- **Maintenance:** Actively maintained.
- **License:** Proprietary platform; generators open (per repo — not re-verified).
- **Limitations:** Best value tied to OpenAPI-driven workflows; hosted lock-in.
- **Related resources:** ReadMe, Redocly, Mintlify, Stainless (adjacent SDK-gen).
- **Sources:** https://www.buildwithfern.com (canonical); https://github.com/fern-api
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C8. ReadMe

- **Resource name:** ReadMe
- **Canonical identity:** ReadMe; readme.com
- **Category:** C — Documentation Grounding (API docs hubs)
- **Type:** Proprietary SaaS
- **Official URL:** https://readme.com
- **Description:** API documentation hubs: interactive API reference, guides, `rdme` CLI for syncing OpenAPI, and usage Metrics.
- **Contents inspected:** Survey level — product pages not opened this session.
- **Actual capabilities:** OpenAPI-synced reference docs, "try it" API explorer, guides/recipes, rdme CLI, Metrics dashboards.
- **Usage domain:** Developer-facing API documentation.
- **Mechanism:** Direct retrieval (hosted docs/API explorer).
- **Integration method:** Hosted hubs; rdme CLI in CI.
- **Compatibility:** OpenAPI inputs.
- **Dependencies:** ReadMe subscription.
- **Availability:** Commercial SaaS, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary.
- **Limitations:** API-docs-centric (less for conceptual guides); hosted lock-in.
- **Related resources:** Fern, Redocly, Mintlify.
- **Sources:** https://readme.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C9. Redocly / Redoc (OSS)

- **Resource name:** Redocly (platform) / Redoc (open-source)
- **Canonical identity:** `Redocly/redoc` (GitHub, OSS); redocly.com
- **Category:** C — Documentation Grounding (API reference generation)
- **Type:** Open-source API reference renderer + commercial platform
- **Official URL:** https://github.com/Redocly/redoc · https://redocly.com
- **Description:** Redoc: open-source OpenAPI → beautiful API reference docs; Redocly: commercial platform around it (developer portals, governance, MCP/docs-as-API surfaces).
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** OpenAPI 3.x → static reference HTML (Redoc OSS); Redocly platform adds portals, linting/governance, hosting.
- **Usage domain:** API reference publishing; agent-readable OpenAPI sources.
- **Mechanism:** Direct retrieval (static generated docs from OpenAPI).
- **Integration method:** npm (`redoc-cli`); CI; Redocly hosted.
- **Compatibility:** OpenAPI 3.x.
- **Dependencies:** Node.js for CLI.
- **Availability:** Public GitHub (OSS) + commercial platform, active.
- **Maintenance:** Actively maintained.
- **License:** MIT (Redoc OSS, per secondary — not independently re-verified); platform proprietary.
- **Limitations:** Reference-focused (needs companion guides for concepts); OSS renderer vs. platform feature split.
- **Related resources:** Fern, ReadMe, Swagger UI, Mintlify.
- **Sources:** https://github.com/Redocly/redoc (canonical); https://redocly.com
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C10. GitBook

- **Resource name:** GitBook
- **Canonical identity:** GitBook; gitbook.com
- **Category:** C — Documentation Grounding (docs platform with Git sync)
- **Type:** Proprietary SaaS
- **Official URL:** https://www.gitbook.com
- **Description:** Documentation platform with bidirectional Git Sync (docs as Markdown in repo), plus llms.txt generation and MCP access for agents.
- **Contents inspected:** Survey level — product pages not opened this session.
- **Actual capabilities:** Git-synced docs authoring, versioning, llms.txt output, MCP server for agent access, AI search.
- **Usage domain:** Product/framework documentation kept in Git.
- **Mechanism:** Direct retrieval (hosted docs + MCP over doc corpus).
- **Integration method:** GitHub/GitLab sync; MCP endpoint; hosted site.
- **Compatibility:** Git repos; MCP clients.
- **Dependencies:** GitBook subscription.
- **Availability:** Commercial SaaS, active.
- **Maintenance:** Actively maintained.
- **License:** Proprietary.
- **Limitations:** Hosted lock-in; agent surfaces depend on authoring discipline.
- **Related resources:** Mintlify, ReadMe, Fern.
- **Sources:** https://www.gitbook.com (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

### C11. readme-ai (eli64s)

- **Resource name:** readme-ai
- **Canonical identity:** `eli64s/readme-ai` (GitHub)
- **Category:** C — Documentation Grounding (documentation generation)
- **Type:** Open-source CLI (Python)
- **Official URL:** https://github.com/eli64s/readme-ai
- **Description:** AI README generator: analyzes a repository and generates/updates README.md with badges, TOC, and structured sections.
- **Contents inspected:** Survey level — README not opened this session.
- **Actual capabilities:** Repo analysis → README scaffolding; badge/TOC generation; template customization.
- **Usage domain:** Bootstrapping project documentation.
- **Mechanism:** Source-code analysis + LLM generation (direct retrieval of repo facts, then generation).
- **Integration method:** CLI (`pip install readme-ai`).
- **Compatibility:** Git repos; LLM providers.
- **Dependencies:** LLM API key; Python.
- **Availability:** Public GitHub.
- **Maintenance:** Community-maintained (activity not re-verified today).
- **License:** MIT (per secondary — not independently re-verified).
- **Limitations:** README-only (not full docs); output needs human review.
- **Related resources:** DeepWiki, repo summarizers.
- **Sources:** https://github.com/eli64s/readme-ai (canonical)
- **Verification date:** 2026-10-10 · **Label:** Partially verified · **Confidence:** Low

---

## Already catalogued by sibling workstreams (cross-reference only — not re-researched)

Per the dedup list: Graphify-Labs/graphify (codebase-to-knowledge-graph, /graphify command, OpenCode native); Opencode-DCP/opencode-dynamic-context-pruning; tickernelz/opencode-mem; 0xranx/OpenContext; thedotmack/claude-mem (explicit OpenCode support); upstash/context7 (+ MCP-workstream alternatives: arabold/docs-mcp-server, DeepWiki, Docfork, Ref Tools); oc-mnemoria; supamem; Hipocampo; opencode-short-term-memory; MrDoe/OpenCodeRAG; opencode-skillful; cortexkit/magic-context; g1331/opencode-magic-context; aerovato/magic-compact; kdcokenny/opencode-background-agents (delegation persistence); code-yeongyu/oh-my-openagent (context injection); [REDACTED-caveman] (compression).

Minor related mentions surfaced during research (not full records — candidates for future passes): A-mem variants (Memary, Memobase, agentmemory, oracleagentmemory), OpenMemory (Mem0 team), MemClaw, Mengram, memonto, ReMe, MemoryBank, EM-LLM, XMem, MemPalace, MemEngine, Chamnan (repo-local memory for coding agents — related to B), sentence-transformers (covered under A20), Upstash Vector, ScaNN, Annoy, HNSWLIB, DiskANN, Coccinelle, Stainless (SDK-gen adjacent to C7), LlamaParse/RAGFlow (document ingestion adjacent to A21), LangSmith (observability adjacent to A22), deepset Cloud (adjacent to A23), Neo4j/FalkorDB/Kuzu/Memgraph/Neptune (graph backends — covered as backends in A2/A5, not as standalone records), Docfork/Ref Tools/context7 alternatives (dedup).

---

## Coverage note

- **Counts:** 58 full records — A: 29 (A1–A29), B: 18 (B1–B18), C: 11 (C1–C11).
- **Verification mix:** 3 records Verified against primary sources read directly on 2026-10-10 (Mem0: 66,891★ Apache-2.0; Graphiti: 31,590★ Apache-2.0; Serena: 30,125★ GPL-3.0-or-later — with a Corrected license vs. secondary MIT claims); 2 Archived (Bloop, Sourcetrail); 1 Historical (Sourcegraph Cody context); remainder Partially verified from secondary sources.
- **Key gaps / limitations:**
  1. Star counts and maintenance claims for Partially-verified records come from secondary sources with varying crawl dates — only the three primary-read numbers are current as of 2026-10-10.
  2. Licenses not independently re-verified: universal-ctags, ast-grep, Joern, SCIP, CodeQL terms, Redoc OSS, readme-ai, most embedding-model weights — recorded as reported-or-Unverified.
  3. Thin coverage: architecture-extraction tools beyond Joern/CodeQL (e.g., code2flow-class tools); graph databases as standalone resources (Neo4j, FalkorDB, Kuzu, Memgraph, Neptune appear only as backends); stale-document detection as a standalone category (only implied via llms.txt freshness and Kapa/Inkeep); embedding-benchmark/leaderboard resources (MTEB mentioned only in passing).
  4. 2026 single-source claims (BEAM details, RULER v2, Chroma "Context Rot" discussion) are flagged Unresolved/low-confidence.
  5. Dedup items (OpenCode-specific memory/context plugins, context7 + alternatives) are intentionally cross-referenced only.
- **More work warranted?** Yes, modestly: a second pass could (a) primary-verify the top-10 Partially-verified records (Qdrant, Weaviate, LlamaIndex, LangMem, Cognee, tree-sitter, CodeQL, Semgrep, Mintlify, llms.txt); (b) add standalone graph-DB records; (c) deepen stale-doc detection and doc-sync tooling (C); (d) verify the flagged licenses. No blockers for Atlas assembly — the catalog is structurally complete for Part 11.
