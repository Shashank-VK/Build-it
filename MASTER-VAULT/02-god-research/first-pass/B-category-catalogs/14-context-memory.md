# 14 — Context-Memory (Embeddings · Vector/Semantic/Hybrid/RAG · Vector DBs · Ingestion · Compression/Pruning · Cross-Session Memory · Indexing · AST/Graphs · Repo Maps · Semantic Search · Docs Grounding — Mechanism Recorded)

> Part 3 · B-category catalog · Agents-Harness researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/repos
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> Mechanism classes: **local-index** (on-disk/embedded, no service) · **service** (managed/self-hosted DB) · **vector** (ANN/HNSW) · **graph** (AST/knowledge-graph/code-graph) · **direct-retrieval** (read/grep/LSP/fetch at call time, no index). Each record states its mechanism with evidence.

## Index (24 resources)

Embeddings/models: OpenAI text-embedding · Gemini embeddings · Cohere/Voyage rerank · Sentence-Transformers local · FastEmbed/SPLADE/ColBERT sparse-multi
Stores: pgvector · Pinecone · Weaviate · Qdrant (+Edge) · Milvus/Zilliz · Chroma · LanceDB/Turbopuffer note · Elasticsearch/OpenSearch BM25+vector
Frameworks/pipelines: LlamaIndex · LangChain retrieval (incl. Pinecone/Chroma/pgvector integrations) · RAG cookbook (Qdrant+OpenAI)
Code-specific: Repo maps (Aider tree-sitter) · tree-sitter (+WASMs) · ast-grep/ctags/LSP code intelligence · Sourcegraph-style code search · repomix packing · Context7 live-docs
Agent memory: Claude Memory/CLAUDE.md+compact · Cline Memory Bank · Copilot persistence/remote · OpenCode snapshots/exports · Gemini context files (GEMINI.md) · Compression/pruning (compact/summarize/mistake-limits)

---

### 01 — OpenAI embeddings (text-embedding-3-small/large, ada-002 lineage)
- **Canonical identity:** `api:openai-embeddings` — https://platform.openai.com/docs/guides/embeddings
- **Category:** Context-memory → Embedding models (dense vectors)
- **Type:** Commercial API
- **Official URL:** https://platform.openai.com/docs/guides/embeddings (+ cookbook vector-DB guides)
- **Description:** `text-embedding-3-small` (1536d, Matryoshka-truncatable) / `-large` (3072d); cosine/dot; batch ingestion; dims declared per collection (e.g. Pinecone/Qdrant cookbook `dimension=1536, metric=cosine`); powers semantic search + RAG chunk retrieval.
- **Contents inspected:** WebSearch-verified excerpts (Qdrant+OpenAI cookbook: embedding model const, collection vector config, nearest-neighbour query flow).
- **Capabilities:** Query/doc vectorization; multilingual; truncatable dims for cost/recall trade.
- **Mechanism:** **vector** (producer) — consumed by service/local-index stores below. Evidence: cookbook wires model output directly into vector collections.
- **Usage domain:** Default embedding for Pinecone/LangChain/Qdrant pipelines in this file.
- **Integration:** official (LangChain `OpenAIEmbeddings`, LlamaIndex readers)
- **Compatibility:** Compatible with all stores (dim+metric must match).
- **Deps:** API key; tokenizer parity.
- **Availability:** API.
- **Maintenance:** Active.
- **License:** Commercial.
- **Security/limits:** Don't embed secrets you wouldn't store; PII in vectors is still PII.
- **Related:** Gemini/Cohere/Sentence-Transformers, rerank.
- **Sources:** platform.openai.com; developers.openai.com/cookbook (Qdrant guides).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Gemini embeddings (`gemini-embedding-001`, 3072d)
- **Canonical identity:** `api:gemini-embeddings` — https://ai.google.dev/gemini-api/docs/embeddings
- **Category:** Context-memory → Embedding models
- **Type:** Commercial API (Google)
- **Official URL:** https://ai.google.dev/gemini-api/docs/embeddings
- **Description:** `gemini-embedding-001` (3072d per Qdrant-community demo); task-type-tuned (retrieval/classification); alternative to OpenAI for Gemini-centric stacks; Qdrant demo compares local-ST vs Gemini quality/cost.
- **Contents inspected:** WebSearch-verified via Qdrant community RAG demo excerpt (model name + 3072 dims + local-vs-cloud decision table).
- **Capabilities:** High-quality semantic vectors; pairs with Qdrant/Weaviate.
- **Mechanism:** **vector** (producer). Evidence: demo stores Gemini vectors in Qdrant collection.
- **Usage domain:** Gemini CLI/agent stacks grounding on Workspace/docs.
- **Integration:** Compatible (LangChain/LlamaIndex Google integrations)
- **Compatibility:** Compatible.
- **Deps:** Google API key.
- **Availability:** API.
- **Maintenance:** Active.
- **License:** Commercial.
- **Security/limits:** Same PII note as 01; egress cost for large corpora.
- **Related:** OpenAI embeddings, Qdrant inference.
- **Sources:** ai.google.dev; qdrant.tech RAG demo (community).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (via community demo; official page not re-fetched this pass)

### 03 — Sentence-Transformers local (`all-MiniLM-L6-v2`, MPNet) + Ollama/LM-Studio path
- **Canonical identity:** `lib:sentence-transformers` — https://www.sbert.net/ (+ `all-MiniLM-L6-v2` 384d)
- **Category:** Context-memory → Local embeddings (no API cost, offline)
- **Type:** OSS (Apache-2.0; HF models)
- **Official URL:** https://www.sbert.net/
- **Description:** `all-MiniLM-L6-v2` (384d, fast) / `all-mpnet-base-v2` (768d, quality); runs on CPU/RAM; Qdrant demo: "fully local, no API cost, fast, good quality / needs RAM, slightly lower quality"; Aider/Cline-compatible local-provider path (Ollama/Vertex/Bedrock/local endpoints).
- **Contents inspected:** WebSearch-verified via Qdrant RAG demo + Aider provider matrix (local-model support).
- **Capabilities:** Private-corpus vectorization; edge/offline retrieval.
- **Mechanism:** **vector** (producer) + **local-index**-friendly (pairs with Chroma/LanceDB/Qdrant-Edge). Evidence: demo runs ST→Qdrant locally.
- **Usage domain:** Air-gapped / cost-sensitive codebases.
- **Integration:** Compatible (HF + LangChain/LlamaIndex embeddings classes)
- **Compatibility:** Compatible.
- **Deps:** Python + RAM; HF weights.
- **Availability:** PyPI/HF.
- **Maintenance:** Active.
- **License:** Apache-2.0 (lib); per-model.
- **Security/limits:** Model weights = supply chain — pin hashes; quality gap vs large APIs on jargon-heavy repos.
- **Related:** FastEmbed, Qdrant Edge, Chroma embedded.
- **Sources:** sbert.net; qdrant community demo; aider.chat providers.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — FastEmbed + SPLADE/ColBERT/miniCOIL (sparse + multi-vector) + rerankers (Cohere/Voyage)
- **Canonical identity:** `lib:fastembed` + sparse/multi-vector family — https://qdrant.tech/documentation/ (FastEmbed, SPLADE, ColBERT, miniCOIL, reranking pages)
- **Category:** Context-memory → Hybrid retrieval primitives (dense+sparse+multi + rerank)
- **Type:** OSS libs + commercial rerank APIs
- **Official URL:** https://qdrant.tech/documentation/
- **Description:** FastEmbed (CPU dense); SPLADE (learned sparse, vocab-size); ColBERT (late-interaction multi-vector) + compressed-multivector search; miniCOIL; rerank top-50→top-5 with cross-encoders (Cohere Rerank 3, Voyage Rerank) — cited as "single biggest RAG quality win for the cost" (modern-ai-guide synthesis).
- **Contents inspected:** WebSearch-verified excerpts (Qdrant docs nav: FastEmbed/quickstart/throughput/miniCOIL/SPLADE/ColBERT/reranking; Pinecone-LlamaIndex hybrid notebook: `add_sparse_vector=True` + FastEmbed sparse model).
- **Capabilities:** Keyword+semantic hybrid; precise code/identifier matching via sparse; quality boost via rerank.
- **Mechanism:** **vector** (dense) + **local-index/service** sparse inverted + **direct-retrieval** rerank call. Evidence: docs separate dense/sparse/multi-vector + rerank stages.
- **Usage domain:** Code search (sparse catches exact symbols; dense catches intent).
- **Integration:** official (Qdrant inference; LlamaIndex hybrid)
- **Compatibility:** Compatible.
- **Deps:** Model weights or rerank API keys.
- **Availability:** OSS + APIs.
- **Maintenance:** Active.
- **License:** Apache-2.0 (libs); commercial (rerank).
- **Security/limits:** Rerankers see raw chunks — scope PII; cache rerank decisions for cost.
- **Related:** Hybrid search in every DB below.
- **Sources:** qdrant.tech/documentation; LlamaIndex Pinecone-hybrid notebook.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 05 — pgvector (Postgres extension) — start-here vector store
- **Canonical identity:** `ext:pgvector` — `github:pgvector/pgvector` (`ankane/pgvector` Docker)
- **Category:** Context-memory → Vector store (relational + vectors)
- **Type:** OSS (PostgreSQL extension)
- **Official URL:** https://github.com/pgvector/pgvector
- **Description:** `vector` column + HNSW/IVFFlat (`vector_cosine_ops/_l2/_ip`); SQL filters out-of-box; sweet spot <10M vectors; pairs with `pg_trgm`/FTS or ParadeDB `pg_search` for hybrid; one-service backup/mental-model; LlamaIndex-pgvector + LangChain-postgres demos.
- **Contents inspected:** WebSearch-verified excerpts (modern-ai-guide scale table + "right starting point" guidance; Qdrant pgvector-migration concept map table/row/column; LlamaIndex-pgvector RAG repo setup).
- **Capabilities:** `ORDER BY embedding <=> $1 LIMIT k` + metadata `WHERE`; transactional ingestion.
- **Mechanism:** **service** (Postgres) + **vector** (HNSW). Evidence: index types + distance ops documented.
- **Usage domain:** Teams already on Postgres needing RAG without new infra.
- **Integration:** official (Supabase/Neon managed; LangChain/LlamaIndex stores)
- **Compatibility:** Compatible. Evidence: first-class integrations in both frameworks.
- **Deps:** Postgres 16+; extension.
- **Availability:** Source/managed.
- **Maintenance:** Active.
- **License:** PostgreSQL license.
- **Security/limits:** Index build/recall wobble >10M hot-QPS vectors (measured) — migrate to Qdrant/Weaviate/Pinecone then.
- **Related:** Qdrant migration path, ParadeDB.
- **Sources:** pgvector repo; modern-ai-guide vector-DBs; Qdrant migrate-from-pgvector.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — Pinecone (managed vector DB, serverless + sparse-dense hybrid)
- **Canonical identity:** `svc:pinecone` — https://docs.pinecone.io/ (integrations: /integrations/llamaindex, /integrations/langchain)
- **Category:** Context-memory → Managed vector service (1M–1B+)
- **Type:** Commercial managed (OSS clients)
- **Official URL:** https://docs.pinecone.io/
- **Description:** Serverless (`ServerlessSpec cloud/region`, `dimension/metric`, e.g. 1536/cosine or 1536/dotproduct-for-hybrid); namespaces; metadata filtering; sparse-dense hybrid; LangChain `PineconeVectorStore.from_documents/add_documents/delete` + RAG guides; LlamaIndex ingest→index→search→evaluate guide (+hybrid `add_sparse_vector` notebook).
- **Contents inspected:** WebSearch-verified excerpts (LangChain setup + index-create + doc-ingest + RAG section; LlamaIndex semantic-search+RAG pipeline + ingestion-pipeline nodes/chunks/upsert; hybrid notebook code).
- **Capabilities:** Scalearburst ingestion; production RAG with managed SLOs.
- **Mechanism:** **service** + **vector** (+hybrid sparse). Evidence: managed index API + distance metrics.
- **Usage domain:** Production RAG needing zero-ops scale.
- **Integration:** official (LangChain/LlamaIndex partners)
- **Compatibility:** Compatible. Evidence: partner guides.
- **Deps:** API key; pre-created index.
- **Availability:** Cloud.
- **Maintenance:** Active.
- **License:** Commercial; clients OSS.
- **Security/limits:** Hosted-only — data leaves VPC (review DPA); `$$` pod/serverless shape.
- **Related:** Qdrant/Weaviate alternatives, rerank.
- **Sources:** docs.pinecone.io/integrations/*; docs.langchain.com Pinecone page.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — Weaviate (OSS + hosted; BM25+vector hybrid best-defaults)
- **Canonical identity:** `svc:weaviate` — `github:weaviate/weaviate` — https://docs.weaviate.io/
- **Category:** Context-memory → Vector DB with first-class hybrid + modules
- **Type:** OSS (BSD-3-Clause) + hosted (Standard/Enterprise)
- **Official URL:** https://weaviate.io/product/integrations/llamaindex (+ docs.weaviate.io)
- **Description:** Objects+vectors; HNSW; BM25+vector hybrid ("cleanest defaults" per synthesis); filters; multi-tenancy; modules (rerank, generative); LlamaIndex `WeaviateVectorStore` + `VectorStoreIndex(nodes, storage_context)` QA system; 1M–100M sweet spot.
- **Contents inspected:** WebSearch-verified excerpts (LlamaIndex+Weaviate RAG setup: ingestion→nodes→index→query; integration resource grid: naive/advanced/agent/memory notebooks).
- **Capabilities:** Hybrid search, generative extraction, agent memory demos (LlamaIndex+Gemini memory notebook).
- **Mechanism:** **service** (self/hosted) + **vector** + keyword hybrid. Evidence: hybrid + vector-index architecture docs.
- **Usage domain:** OSS teams wanting hybrid without assembling_sparse stacks.
- **Integration:** official (LangChain/LlamaIndex)
- **Compatibility:** Compatible.
- **Deps:** Docker/K8s or Cloud.
- **Availability:** Source/Cloud.
- **Maintenance:** Active.
- **License:** BSD-3-Clause (core).
- **Security/limits:** Module API keys (OpenAI/Cohere) need secret hygiene; backup object+vector stores jointly.
- **Related:** Qdrant, Pinecone, rerank.
- **Sources:** weaviate.io + LlamaIndex blog integration.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — Qdrant (+ Edge embedded) — Rust vector engine + inference
- **Canonical identity:** `svc:qdrant` — https://qdrant.tech/documentation/ (Docker `qdrant/qdrant`; clients `qdrant-client`)
- **Category:** Context-memory → Performant vector search (self/hosted/edge)
- **Type:** OSS (Apache-2.0) + Cloud
- **Official URL:** https://qdrant.tech/documentation/
- **Description:** Collections→points (id+vector(s)+payload); HNSW + quantization (product/scalar) + multitenancy + snapshots + filtering built into search phase; Inference (dense/sparse/multi-vector via cloud models); FastEmbed/SPLADE/ColBERT/rerank pages; MCP server + Agent Skills; migration tooling (pgvector/Chroma/Milvus/ES/OpenSearch/S3/Redis/Mongo/FAISS/Solr); Qdrant Edge: in-process, offline, minimal RAM (robots/kiosks/mobile).
- **Contents inspected:** WebSearch-verified excerpts (docs nav: manage/search/inference; embeddings provider table incl. OpenAI/Gemini/Cohere/Voyage; OpenAI cookbook `Articles` collection `title+content` vectors + filter; pgvector-migration flags/gotchas).
- **Capabilities:** Hybrid queries, payload filters, blue-green/incremental-embedding-ops, edge retrieval.
- **Mechanism:** **service** (server) + **local-index** (Edge embedded) + **vector**. Evidence: dual deployment docs + HNSW/quantization pages.
- **Usage domain:** OSS default when leaving pgvector; edge agents needing offline search.
- **Integration:** official (LangChain/LlamaIndex/OpenAI cookbook; MCP server)
- **Compatibility:** Compatible. Evidence: cookbook + migration coverage.
- **Deps:** Docker or Cloud; client lib.
- **Availability:** Source/Cloud/Edge.
- **Maintenance:** Active (2026 docs + Edge launch).
- **License:** Apache-2.0.
- **Security/limits:** Snapshot/restore holds vectors+payload — encrypt; tune quantization vs recall explicitly.
- **Related:** Weaviate/Pinecone, FastEmbed, Edge.
- **Sources:** qdrant.tech/documentation/*; OpenAI cookbook Qdrant guides.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — Milvus/Zilliz + Chroma + LanceDB/Turbopuffer + Vespa/ES note (scale ladder)
- **Canonical identity:** `svc:milvus` (`github:milvus-io/milvus`) · `lib:chroma` · `lib:lancedb` · `svc:turbopuffer` · `svc:vespa` · `svc:elasticsearch|opensearch`
- **Category:** Context-memory → Scale/embedding-shape alternatives
- **Type:** Mixed OSS + managed
- **Official URLs:** https://github.com/milvus-io/milvus ; https://docs.trychroma.com/ ; https://lancedb.com/ ; https://vespa.ai/
- **Description:** Milvus/Zilliz 100M–10B+ (enterprise partitions); Chroma embedded/hosted <1M prod (basic hybrid/filters; `persist_directory` LangChain snippet attested); LanceDB embedded+cloud columnar 1M–1B; Turbopuffer object-storage-cheap 100M+ multi-tenant; Vespa extreme-scale best hybrid/filters (complex ops); ES/OS mature BM25+vector for ops-familiar teams. (Scope: ladder placement, not per-engine tuning.)
- **Contents inspected:** WebSearch-verified via modern-ai-guide comparison table + STACKIT RAG tutorial (Chroma `persist_directory` snippet + Milvus/Qdrant/Weaviate/pgvector production note).
- **Capabilities:** Right-size store by vectors×QPS×tenancy.
- **Mechanism:** **local-index** (Chroma/LanceDB embedded) ↔ **service** (others) + **vector**. Evidence: hosting/scale/hybrid/filter/cost columns.
- **Usage domain:** Ladder: prototype Chroma → team pgvector → scale Qdrant/Weaviate/Pinecone → extreme Milvus/Vespa.
- **Integration:** Compatible (LangChain/LlamaIndex stores for each)
- **Compatibility:** Compatible. Evidence: framework store matrix.
- **Deps:** Per engine.
- **Availability:** OSS/Cloud per engine.
- **Maintenance:** Active.
- **License:** Apache-2.0 (most cores).
- **Security/limits:** Embedded stores inherit app FS permissions — encrypt at rest for code corpora with secrets.
- **Related:** pgvector/Qdrant/Pinecone/Weaviate.
- **Sources:** modern-ai-guide vector-DBs; STACKIT LangChain RAG tutorial.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (ladder synthesis; per-engine docs not re-fetched)

### 10 — LlamaIndex (ingest→index→retrieve→synthesize framework)
- **Canonical identity:** `sdk:llamaindex` — `pip:llama-index` / `npm:llamaindex` — https://www.llamaindex.ai/framework (+ https://developers.llamaindex.ai/)
- **Category:** Context-memory → RAG/agent data framework
- **Type:** OSS (MIT) + LlamaCloud/LlamaParse
- **Official URL:** https://www.llamaindex.ai/framework
- **Description:** Connectors 100+ (pdf/docx/Notion/Slack/BS4), nodes/chunks, indexes (vector/list/tree), query engines (naive→advanced→corrective→auto-retrieval), agents+workflows, eval/observability; Pinecone/Weaviate/Chroma/pgvector vector-store integrations; hybrid notebook (`add_sparse_vector`); memory-with-Weaviate+Gemini notebook; MCP server + agent REST/llms.txt.
- **Contents inspected:** WebSearch-verified excerpts (framework value-prop: production RAG + agents + eval; Pinecone RAG pipeline steps; Weaviate integration notebooks grid; hybrid sparse notebook).
- **Capabilities:** Pre/post-processing-rich RAG; doc-grounded agents (file 12 workers).
- **Mechanism:** Orchestrates **service/vector/local-index/graph** stores + **direct-retrieval** readers. Evidence: store-agnostic `VectorStoreIndex` + connector list.
- **Usage domain:** Docs-grounding layer for every agent in file 11.
- **Integration:** official (all stores above)
- **Compatibility:** Compatible. Evidence: per-store integration pages.
- **Deps:** Python 3.10+/Node; provider+store creds.
- **Availability:** PyPI/npm/source; Cloud optional.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Connector sprawl = secret sprawl — scope per-source tokens; eval before prod cutover.
- **Related:** LangChain, vector DBs, eval.
- **Sources:** llamaindex.ai; developers.llamaindex.ai; Pinecone/Weaviate integration pages.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — LangChain retrieval (documents→split→embed→store→retrieve→RAG)
- **Canonical identity:** `sdk:langchain` — https://docs.langchain.com/ (vectorstores: Pinecone/Chroma/pgvector; retrieval docs; Agentic RAG)
- **Category:** Context-memory → LLM-app framework with retrieval primitives
- **Type:** OSS (MIT) + LangSmith/Platform
- **Official URL:** https://docs.langchain.com/oss/python/integrations/vectorstores/pinecone
- **Description:** `PineconeVectorStore.from_documents/from_texts/add_documents/delete` (uuids), `CharacterTextSplitter`, `OpenAIEmbeddings`; Chroma `persist_directory` runnable; pgvector via `langchain-postgres`; RAG guides (Build a RAG app, Agentic RAG, retrieval docs); LlamaIndex retrievers (`LlamaIndexRetriever/GraphRetriever`) for cross-framework use.
- **Contents inspected:** WebSearch-verified excerpts (Pinecone page: install→index→embed→add→delete→query→RAG links; STACKIT Chroma snippet; LlamaIndex-provider page).
- **Capabilities:** Standard RAG + agentic (retrieval as tool) patterns.
- **Mechanism:** Orchestrates **service/vector/local-index** + **direct-retrieval**. Evidence: store-specific integration code.
- **Usage domain:** Baseline RAG implementation teams already know.
- **Integration:** official (all stores)
- **Compatibility:** Compatible.
- **Deps:** Python/JS; provider+store creds.
- **Availability:** PyPI/npm/source.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Chunk overlap/metadata choices leak context — set allowlists per retriever.
- **Related:** LlamaIndex, LangGraph (runtime), eval.
- **Sources:** docs.langchain.com/*; docs.pinecone.io/integrations/langchain.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 12 — Ingestion: chunking, metadata, upserts, incremental updates (practice)
- **Canonical identity:** `pattern:ingestion` — LlamaIndex Ingestion Pipelines (docs→nodes→vectors→upsert) · Qdrant incremental-embedding-updates + blue-green + snapshots · Pinecone `from_documents` (splitter+overlap)
- **Category:** Context-memory → Write path (load→transform→vectorize→index)
- **Type:** Practice + per-store ops
- **Official URLs:** Pinecone-LlamaIndex guide (ingestion pipelines); Qdrant ops (snapshots/migration/incremental/blue-green); LangChain splitters
- **Description:** Parse (LlamaParse/unstructured) → split (size/overlap; code-aware splitters per language) → enrich (source/line/symbol metadata; LLM-visible vs embedding-only) → embed → upsert (ids stable for re-index) → validate (recall sample) → migrate/blue-green on model change (re-embed, dual-read, cutover).
- **Contents inspected:** WebSearch-verified excerpts (LlamaIndex pipeline paragraph; Qdrant scale/migration ops list; Pinecone splitter+overlap snippet).
- **Capabilities:** Fresh, attributable, re-embeddable corpora.
- **Mechanism:** Write path feeding **service/local-index/vector** stores. Evidence: per-store migration/ops pages.
- **Usage domain:** All RAG/code-search deployments.
- **Integration:** Compatible (framework pipelines)
- **Compatibility:** Compatible.
- **Deps:** Parser + splitter + id scheme.
- **Availability:** Practice.
- **Maintenance:** Stable.
- **License:** N/A.
- **Security/limits:** Ingestion sees raw corpus — run with least-privilege readers; logembedded-model versions for reproducibility.
- **Related:** Stores, eval, docs grounding.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified (as synthesis)

### 13 — Compression & pruning: compaction, summarize, truncate, mistake-limits (context budget)
- **Canonical identity:** `pattern:context-compression` — Claude Pre/PostCompact + compaction agents + `cleanupPeriodDays` · Cline compaction (`agentic|basic|off`) + mistake limits · OpenCode compaction/summary agents + snapshots · Cursor checkpoints/context controls
- **Category:** Context-memory → Fit long work in finite windows
- **Type:** Per-agent Native
- **Official URLs:** code.claude.com (checkpointing/sessions agent-view notes); docs.cline.bot (compaction); file 11/17 session refs
- **Description:** Auto-compact at budget (agentic summarize preserves decisions; basic truncates; off disables); PreCompact dump handoff notes → PostCompact rehydrate; 100-checkpoint/~30-day retention; mistake-limit abort on drift; checkpoints+git cover what summaries drop.
- **Contents inspected:** WebSearch-verified excerpts (Claude retention/sweep + fork/branch preservation; Cline compaction flags; OpenCode snapshot dirs).
- **Capabilities:** Long-horizon work without window overflow.
- **Mechanism:** **direct-retrieval**-adjacent (in-context summarization; no external index required). Evidence: compaction agent docs describe in-session summarization.
- **Usage domain:** Every autonomous loop (file 13/07–08).
- **Integration:** official per agent
- **Compatibility:** Native per harness. Evidence: per-agent compaction pages.
- **Deps:** Handoff-note convention (pre-compact hooks).
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Summaries can drop caveats/secrets-context — keep verifier + evidence pack outside summary.
- **Related:** Cross-session memory, handoffs, cost.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 14 — Cross-session memory: user/project/local scopes + persistence/remote/share
- **Canonical identity:** `pattern:cross-session-memory` — Claude Memory (`user/project/local`, `settingSources`, subagent `memory` field) · Cline Memory Bank · Copilot persistence/resume/remote · OpenCode SQLite + snapshots + `/export` · Gemini `GEMINI.md` context files · Roo sticky models/modes (historical)
- **Category:** Context-memory → Durability across runs/devices
- **Type:** Per-agent Native
- **Official URLs:** code.claude.com (Agent SDK `memory`, sessions); github.com/github/copilot-sdk (persistence/remote); opencode-skills sessions SKILL.md; geminicli extension reference (`contextFileName`)
- **Description:** Persist plans/decisions/conventions per scope; resume (`--resume/--continue`, session IDs) or fork; share to web/mobile (Copilot Remote, Claude Remote Control); project memory committed (`CLAUDE.md/GEMINI.md/AGENTS.md`), user memory global, local memory git-ignored.
- **Contents inspected:** WebSearch-verified excerpts (Claude AgentDefinition `memory` enum; Copilot persistence/remote rows; OpenCode db/log/snapshot paths; Gemini `contextFileName` manifest field).
- **Capabilities:** Org conventions that survive compaction/restart/reinstall.
- **Mechanism:** Files + SQLite + hosted share (not vector by default) — pair with vector stores for semantic recall. Evidence: paths/scopes documented (no ANN implied).
- **Usage domain:** Team lore + long projects.
- **Integration:** official per agent
- **Compatibility:** Native per harness; portable via committed markdown.
- **Deps:** Scope discipline (what's committed vs local).
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent (your content yours).
- **Security/limits:** Memory files are prompt — never store secrets; review project memory in PRs (injection surface).
- **Related:** Compression, skills, rules.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 15 — Indexing strategies: ANN/HNSW, quantization, payload filters, hybrid ranking (how stores stay fast)
- **Canonical identity:** `pattern:indexing` — Qdrant (HNSW+PQ/SQ, payload-index, multitenancy) · pgvector (HNSW/IVFFlat) · Pinecone (managed ANN + namespaces) · Weaviate (HNSW+BM25) · ES/OS (BM25+vector)
- **Category:** Context-memory → Read-path performance + recall control
- **Type:** Per-store Native index config
- **Official URLs:** qdrant.tech/documentation (indexing/quantization/multitenancy); pgvector index docs; Pinecone/Weaviate architecture
- **Description:** Choose distance (cosine/euclid/dot — must match embedding + query); HNSW (`m/ef_construct`) vs IVFFlat (lists/probes); quantization for RAM (recall trade measured); payload/namespace/tenant pruning before ANN; hybrid (BM25+sparse+dense→rerank) for code/identifier queries.
- **Contents inspected:** WebSearch-verified excerpts (Qdrant vectors/manage/indexing/quantization/multitenancy nav; pgvector index-type/recall gotcha in migration guide; modern-ai-guide hybrid/rerank guidance).
- **Capabilities:** p95 latency + recall SLOs for retrieval tools.
- **Mechanism:** **vector** ANN + keyword inverted. Evidence: per-store index+recall docs.
- **Usage domain:** Production tuning for RAG/code-search tools agents call.
- **Integration:** Per store.
- **Compatibility:** Native per store.
- **Deps:** Recall eval set (measure before/after).
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per store.
- **Security/limits:** Tenant filters are security boundaries — test isolation (cross-tenant recall = breach).
- **Related:** Stores, hybrid, eval.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 16 — Aider repo maps (tree-sitter symbol map for whole-repo context)
- **Canonical identity:** `tool:aider-repomap` — https://aider.chat/2023/10/22/repomap.html (+ https://aider.chat/docs)
- **Category:** Context-memory → Code-specific map (classes/functions+signatures, ranked)
- **Type:** OSS (Aider; tree-sitter under the hood)
- **Official URL:** https://aider.chat/2023/10/22/repomap.html
- **Description:** Concise whole-repo map (top symbols + types + call signatures, relevance-ranked) sent with each prompt; built automatically via tree-sitter extraction; lets GPT navigate/edit large repos without dumping files; complements user-`/add`ed files (1–2 relevant files guidance).
- **Contents inspected:** WebSearch-verified excerpts (map purpose + tree-sitter extraction + "self-contained vs repo-aware" rationale).
- **Capabilities:** Cheap global code awareness; scales pairing to large codebases.
- **Mechanism:** **graph** (AST-derived symbols) + **direct-retrieval** (map text in prompt). Evidence: page names tree-sitter as extractor.
- **Usage domain:** Terminal pairing on monorepos; template for other harnesses' repo maps.
- **Integration:** Native to Aider; pattern portable.
- **Compatibility:** Native (Aider) · pattern Compatible. Evidence: dedicated repomap page.
- **Deps:** Git repo; tree-sitter grammars.
- **Availability:** Built-in (`pip:aider-chat`).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Map reveals repo structure — scrub on share; map ≠ permission (still gate reads).
- **Related:** tree-sitter, ast-grep, ctags/LSP.
- **Sources:** aider.chat repomap + tips pages.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — tree-sitter (+ prebuilt WASMs) — incremental AST parsing substrate
- **Canonical identity:** `lib:tree-sitter` — https://tree-sitter.github.io/ (+ `github:repomix/tree-sitter-wasms`)
- **Category:** Context-memory → AST substrate for maps/search/chunking
- **Type:** OSS (MIT)
- **Official URL:** https://tree-sitter.github.io/
- **Description:** Incremental, error-tolerant parsers per language (used by IDEs/LSPs/Aider); query language for symbols (functions/classes/imports); WASM builds let web/Rust/TS harnesses parse without native toolchain; underpins repo maps, code-aware chunking, symbol导航.
- **Contents inspected:** WebSearch-verified via Aider repomap page (tree-sitter attribution) + repomix org (WASM binaries) + Aider language-support note (tree-sitter-language-pack).
- **Capabilities:** Precise def/ref extraction; robust on partial code.
- **Mechanism:** **graph** (syntax trees). Evidence: parser+query architecture.
- **Usage domain:** Build/extend repo maps, chunkers, linters agents rely on.
- **Integration:** Compatible (bindings Py/Rust/WASM/Go)
- **Compatibility:** Compatible. Evidence: multi-harness adoption (editors + Aider + repomix).
- **Deps:** Per-language grammar.
- **Availability:** Source/crates/npm/PyPI.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Grammar supply chain — pin versions; parsers read untrusted code (sandbox fuzzed inputs).
- **Related:** Repo maps, ast-grep, ctags.
- **Sources:** tree-sitter.github.io; repomix org; aider.chat.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 18 — ast-grep + ctags + LSP (precise code intelligence agents can call)
- **Canonical identity:** `tool:ast-grep` (`github:ast-grep/ast-grep`) · `tool:ctags/universal-ctags` · `spec:lsp` (Microsoft LSP) — Copilot "Using LSP servers with CLI" page
- **Category:** Context-memory → Deterministic navigation (defs/refs/rename) grounding generation
- **Type:** OSS (mostly MIT/GPL per tool) + open spec (LSP)
- **Official URLs:** https://ast-grep.github.io/ ; https://docs.github.com/en/copilot (LSP servers with CLI)
- **Description:** ast-grep: structural search/rewrite by AST pattern (find `useEffect` without cleanup across TS); ctags: cheap symbol index (`tags` file) for jump-to-def without service; LSP (`go to definition/find references/rename`) gives Copilot CLI precise cross-file intelligence — cited as accuracy source for refactors.
- **Contents inspected:** WebSearch-verified via Copilot LSP page title + Aider/repomap lineage (tree-sitter adjacent); ast-grep positioning well-established (fetch on demand for flags).
- **Capabilities:** Exact structural queries where vectors guess; safe large renames.
- **Mechanism:** **graph** (AST/symbol graph) + **direct-retrieval** (LSP requests). Evidence: LSP request/response + tags-file architecture.
- **Usage domain:** Ground refactors/migrations agents propose (verify before apply).
- **Integration:** Compatible (CLI tools; LSP via MCP/stdio)
- **Compatibility:** Compatible. Evidence: Copilot documents LSP wiring.
- **Deps:** Language servers / ctags binary.
- **Availability:** Source/binaries.
- **Maintenance:** Active.
- **License:** MIT (ast-grep) / GPL (ctags) / MIT-spec (LSP).
- **Security/limits:** LSP servers execute parsers on repo code — run workspace-trusted servers only.
- **Related:** tree-sitter, repo maps, semantic search.
- **Sources:** ast-grep.github.io; docs.github.com LSP page.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (LSP wiring verified; ast-grep flags not re-fetched this pass)

### 19 — Semantic code search: Sourcegraph-style + Cline marketplace search servers
- **Canonical identity:** `svc:sourcegraph` (Cody/Code Search) + `mkt:cline-mcp-search` (Exa/Parallel/Context7-type servers)
- **Category:** Context-memory → Natural-language code finding at org scale
- **Type:** Commercial (Sourcegraph) + OSS MCP servers
- **Official URLs:** https://sourcegraph.com/docs ; https://cline.bot/mcp-marketplace
- **Description:** Sourcegraph: trigram + embeddings hybrid over monorepos, precise code monitoring, Cody grounded answers with citations; Cline marketplace: one-click Exa/Perplexity/parallel-search/Context7 servers giving agents live web+repo search tools.
- **Contents inspected:** WebSearch-verified excerpts (Cline marketplace categories incl. semantic-search + Context7 up-to-date-docs; Sourcegraph positioning well-known — fetch on demand for最新 parity).
- **Capabilities:** "Where is auth enforced?" answered with file:line evidence.
- **Mechanism:** **service** (hosted index) + **vector** + **direct-retrieval** (live fetch). Evidence: marketplace server contracts (tools returning citations/URLs).
- **Usage domain:** Large-org grounding without cloning every repo into context.
- **Integration:** Compatible (MCP tools; Sourcegraph API)
- **Compatibility:** Compatible. Evidence: MCP marketplace listings.
- **Deps:** Index permissions (repo allowlists).
- **Availability:** SaaS/self-hosted + MCP.
- **Maintenance:** Active.
- **License:** Commercial / per-server OSS.
- **Security/limits:** Search indexes inherit repo ACLs — verify (leak via snippets = breach); scope live-search tools.
- **Related:** Vector DBs, docs grounding, evidence.
- **Sources:** sourcegraph.com/docs; cline.bot/mcp-marketplace.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (marketplace verified; Sourcegraph page not re-fetched this pass)

### 20 — repomix: pack-a-repo for prompt stuffing (measured alternative to retrieval)
- **Canonical identity:** `tool:repomix` — `npm:repomix` — `github:repomix` (repomix.com)
- **Category:** Context-memory → Whole-repo packing (concat + strip + token-count)
- **Type:** OSS (MIT)
- **Official URL:** https://repomix.com (org: github.com/repomix)
- **Description:** Flattens repo to single XML/markdown with file tree + contents; strip comments, ignore via `.repomixignore`, tree-sitter-aware compression options, token counting; Cline marketplace "repomix documentation generator" variant; best for small–medium repos fitting windows; complements RAG (pack hot paths, retrieve cold).
- **Contents inspected:** WebSearch-verified via org profile (TS/JS, WASM + strip-comments repos) + marketplace repomix blurb.
- **Capabilities:** Deterministic full-context baseline; diffable snapshots.
- **Mechanism:** **direct-retrieval** (static pack read; no ANN). Evidence: pack-then-read workflow (no index service).
- **Usage domain:** Audits/migrations where recall gaps are unacceptable and repo fits budget.
- **Integration:** Compatible (CLI output → any agent prompt)
- **Compatibility:** Compatible. Evidence: marketplace + org attest usage with agents.
- **Deps:** Node.
- **Availability:** npm/source.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Packs include everything not ignored — audit ignore rules (secrets!), watch token cost.
- **Related:** Repo maps (cheaper), RAG (larger).
- **Sources:** repomix.com; github.com/repomix; cline.bot/mcp-marketplace.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 21 — Context7 / live-docs grounding (version-correct answers)
- **Canonical identity:** `svc:context7` (`@upstash/context7` — Gemini gallery 63k installs + Cline/Roo MCP listings)
- **Category:** Context-memory → Fresh library-docs retrieval (anti-hallucination)
- **Type:** Managed docs index + OSS MCP servers
- **Official URLs:** https://geminicli.com/extensions/ (context7 spotlight) ; https://cline.bot/mcp-marketplace
- **Description:** "Up-to-date code docs for any prompt" — resolves library + version → fetches current docs/examples into context; Aider `/read`+URL-scrape and LlamaIndex web-scraper connectors are manual equivalents; critical for fast-moving APIs (Tailwind v4, shadcn, SDKs).
- **Contents inspected:** WebSearch-verified excerpts (Gemini gallery install count + tagline; Cline marketplace Context7 blurb "accurate and current programming assistance").
- **Capabilities:** Version-pinned grounding without maintaining scrapers.
- **Mechanism:** **service** (hosted docs index) + **direct-retrieval** (fetch on query). Evidence: install-then-query MCP flow (no local vector build).
- **Usage domain:** Every agent lane touching third-party APIs.
- **Integration:** Compatible (MCP: `gemini extensions install …context7`, `cline mcp install ctx7 …`)
- **Compatibility:** Compatible. Evidence: listings in two independent marketplaces.
- **Deps:** MCP host; network.
- **Availability:** MCP/registry.
- **Maintenance:** Active.
- **License:** MIT (server) + service ToS.
- **Security/limits:** Fetched docs are untrusted content — still verify signatures/flags in primary sources.
- **Related:** RAG, semantic search, skills.
- **Sources:** geminicli.com/extensions/; cline.bot/mcp-marketplace.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 22 — Qdrant MCP Server + Agent Skills / LlamaIndex docs MCP (agents query memory with tools)
- **Canonical identity:** `tool:qdrant-mcp` + `svc:llamaindex-docs-mcp` — https://qdrant.tech/documentation/ (MCP Server, Agent Skills pages) ; https://developers.llamaindex.ai/ (MCP + llms.txt + REST search/grep/read/list)
- **Category:** Context-memory → Agentic memory access (tools, not dumps)
- **Type:** OSS servers + hosted docs
- **Official URLs:** qdrant.tech/documentation (Qdrant Tools: MCP Server/Agent Skills/Prompts-in-Docs); developers.llamaindex.ai (llms.txt, page-as-markdown via `index.md`, MCP endpoint)
- **Description:** Agents call memory (search/filter/fetch) instead of pasting corpora; Qdrant ships MCP + Skills + in-docs prompts; LlamaIndex exposes BM25 search, regex grep, page read, tree list + raw-markdown pages. Pattern: keep vectors in store, stream only top-k evidence into context.
- **Contents inspected:** WebSearch-verified excerpts (Qdrant docs nav: MCP Server/Agent Skills/Prompts-in-Docs; LlamaIndex hybrid notebook footer: llms.txt + `index.md` + MCP server lines).
- **Capabilities:** Token-frugal grounding; citable evidence per answer.
- **Mechanism:** **service** (store/docs) via **direct-retrieval** tool calls (+**vector** inside). Evidence: tool-page contracts.
- **Usage domain:** Template for exposing any store in file 05–09 to file-11 agents.
- **Integration:** official (MCP)
- **Compatibility:** Compatible. Evidence: live MCP endpoints + docs.
- **Deps:** MCP host.
- **Availability:** Source/hosted.
- **Maintenance:** Active.
- **License:** Apache-2.0 / MIT.
- **Security/limits:** Tool descriptions untrusted (MCP rule); scope search namespaces per agent.
- **Related:** MCP, semantic search, evidence.
- **Sources:** qdrant.tech/documentation; developers.llamaindex.ai.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 23 — Graph memory: knowledge/code graphs (LlamaIndex graphs, code-graphs, GraphRAG lineage)
- **Canonical identity:** `pattern:graph-memory` — LlamaIndex `LlamaIndexGraphRetriever`/query engines (Sub-Question/Recursive/Self-Correcting) · code-graph (calls/imports) · GraphRAG-style community summaries
- **Category:** Context-memory → Relational recall (entities + edges)
- **Type:** OSS patterns + framework support
- **Official URLs:** weaviate.io LlamaIndex notebooks (Sub-Question/Recursive/Self-Correcting/Router/Agent-vs-No-Agent); docs.langchain.com LlamaIndexGraphRetriever
- **Description:** Index entities/relations (APIs call, modules import, docs mention) alongside vectors; traverse (callers-of-X, owners-of-Y) then vector-expand; sub-question decomposition for multi-hop ("which services call deprecated auth and have open CVEs?"); complements ANN where relations matter more than similarity.
- **Contents inspected:** WebSearch-verified excerpts (Weaviate notebook grid names each engine; LangChain graph-retriever page).
- **Capabilities:** Multi-hop reasoning with paths as evidence.
- **Mechanism:** **graph** (property/knowledge) + **vector** fallback. Evidence: engine names + graph-retriever API.
- **Usage domain:** Monorepo impact analysis, deprecation hunts, ownership mapping.
- **Integration:** Compatible (LlamaIndex/LangChain graph stores)
- **Compatibility:** Compatible. Evidence: framework retriever APIs.
- **Deps:** Entity extractor + graph store (Neo4j/Memgraph/Weaviate-links).
- **Availability:** OSS.
- **Maintenance:** Active.
- **License:** MIT + store licenses.
- **Security/limits:** Graph leaks org structure — apply edge-level ACLs; validate extracted relations (LLM extraction errors).
- **Related:** AST graphs, vector stores, boards.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (engine grid verified; store tuning not re-fetched)

### 24 — Docs grounding pattern: specs + READMEs + ADRs as first-class context (with llms.txt)
- **Canonical identity:** `pattern:docs-grounding` — OpenSpec spec library · Spec Kit constitution · `llms.txt` doc indexes (Anthropic/MCP/LlamaIndex/Windsurf/Cline) · `AGENTS.md/CLAUDE.md/GEMINI.md`
- **Category:** Context-memory → Curated direct-retrieval grounding (no vectors needed)
- **Type:** Conventions + per-site indexes
- **Official URLs:** openspec.dev (spec library persistence); modelcontextprotocol.io/llms.txt; code.claude.com/llms.txt; developers.llamaindex.ai/llms.txt; docs.windsurf.com/llms.txt; docs.cline.bot/llms.txt
- **Description:** Keep intent (specs/ADRs), usage (READMEs), and agent instructions (AGENTS/CLAUDE/GEMINI.md) as versioned markdown; expose `llms.txt` sitemap + raw-markdown pages so agents fetch exact sections; OpenSpec spec deltas make requirements reviewable; "context doesn't disappear when chat ends or someone leaves".
- **Contents inspected:** WebSearch-verified excerpts (OpenSpec "agent reads the spec; new dev browses library" + tree figure; five independent `llms.txt` fetch lines across doc sites).
- **Capabilities:** Cheapest reliable grounding; human+agent shared source of truth.
- **Mechanism:** **direct-retrieval** (read/fetch exact files). Evidence: file-tree + fetch-index documentation (no embedding step).
- **Usage domain:** Start here before any vector build (most teams over-index on vectors).
- **Integration:** Compatible (git + fetch tools)
- **Compatibility:** Compatible. Evidence: six independent attestations.
- **Deps:** Doc discipline (specs/ADRs kept current).
- **Availability:** Convention.
- **Maintenance:** Ongoing (your docs).
- **License:** N/A.
- **Security/limits:** Docs are prompt — review for secrets/injection; prefer deltas over rewrites for audit.
- **Related:** Spec-driven (13), memory scopes, Context7.
- **Sources:** openspec.dev/docs/concepts; llms.txt endpoints listed.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

---

**Count: 24 resources** (meets 20+ minimum). No install/execute performed. Mechanism recorded per resource with evidence.
