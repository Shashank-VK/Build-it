# Phase 1 — Batch 2: Context, Memory & Knowledge — Broad Mapper (R-A) Deep Research
**Researcher A — Broad Mapper | P1-09 + P1-11 + P1-13**
**Date: 2026-08-31 | Repo: `the harness` | Continuity: `plan.md §2 Batch 2` · `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..10, SC-09 CSP · `phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md` (11 Capabilities + 10 Mechanisms converged — do NOT duplicate)**

**Absolute anchors:**
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md`
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md`
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\batch-1\BATCH-1_EXECUTION_AND_AGENCY.md`

---

## 0. Method & Coverage

### 0.1 Search Angles (9 distinct, 7+ required)

| # | Angle | Query Vocabulary | Ecosystems Hit | Sources |
|---|-------|------------------|----------------|---------|
| A1 | Claude Agent SDK context lifecycle | `Claude Agent SDK context management memory compaction` | Claude Code, Claude Agent SDK, Agent SDK async context manager | SDK docs, `/compact`, `compact_boundary`, `autoCompactEnabled`, `CLAUDE.md` re-injection |
| A2 | OpenAI Agents SDK handoff + memory | `OpenAI Agents SDK memory context management handoff` | OpenAI Agents SDK, Swarm (predecessor), Triage pattern | Handoff primitive, session-scoped memory, guardrails scoping |
| A3 | LangChain/LangGraph memory taxonomy | `LangChain LangGraph memory checkpoint semantic episodic` | LangGraph Checkpointer (`MemorySaver/SqliteSaver/PostgresSaver/MongoDBSaver`), `BaseStore`/`PostgresStore`, LangMem SDK | Checkpointer vs Store split, `thread_id` vs `user_id`, semantic search on Store, 3 memory types |
| A4 | RAG systems & vector DB substrate | `LlamaIndex Haystack RAG vector database retrieval architecture` + `vector database Pinecone Qdrant Chroma Weaviate retrieval RAG comparison 2024 2025` | LlamaIndex, Haystack 2.x, Pinecone, Qdrant, Weaviate, Chroma, FAISS, Milvus, pgvector, MongoDB Vector | Ingestion pipelines, `VectorStoreQuery`, `NodeWithScore`, hybrid BM25+dense, Recipr rank fusion |
| A5 | IDE agent context injection | `Cursor Copilot Windsurf context management codebase indexing rules` | Cursor (`@codebase`, `@files`, `.cursor/rules/*.mdc`, local embeddings), Copilot (`.github/copilot-instructions.md`, repo indexing), Windsurf Cascade (full-repo embeddings, auto-selection, `.windsurfrules`/`.windsurf/rules/rules.md`), Continue.dev (Chroma) | Context injection table, hierarchical context L0-L2, rules-file portability |
| A6 | Security: poisoning & injection | `context poisoning memory injection agent security attack` | OWASP ASI06, Letta archival memory, ElizaOS, Agno validation layer, eTAMP benchmark | Memory poisoning as persistent indirect prompt injection, `tool_result` injection → `STATE_MODIFICATION`, GLOBAL `commit_memory` cross-workspace |
| A7 | Context window mechanics | `context window management compaction summarization pruning agent` | xopcai/xopc, windmist, djinnbot, Zap, kcode, trustclaw, LCM paper (arXiv 2605.04050) | Sliding window, token-aware pruning, `maybeCompact`, LLM summarization of dropped turns, 3-layer pruning/flush/compact, LCM dual-state immutable/active |
| A8 | Taxonomy distinction | `context management vs memory vs retrieval` + `knowledge management vs retrieval vs memory AI agent taxonomy` + `knowledge management harness documentation AI development MCP memory` | PKM vs Wiki vs RAG vs AI Memory, CoALA 4-tier, Memory in Age of AI Agents survey, awesome-harness-engineering, `codebase-memory-mcp`, `claude-memory-compiler`, `Facts as First Class Objects` | Forms/Functions/Dynamics taxonomy, RAG stateless vs memory stateful, hard/cold memory |
| A9 | Prompt architecture & budgets | `prompt architecture harness complexity budget token management` + `context engineering vs prompt engineering agent harness taxonomy` + `prompt complexity management budget anti-bloat harness` + `context budget token budget competition agent harness` | Harness-as-OS stack (Prompt → Context → Harness → Loop), Karpathy/Lütke/Hassimoto/Lopopolo/Fowler, harness Foundry `context-budget` SKILL, Kairn KL regularization, Forge complexity budget, `ContextManager` priority chain P0-P10 | Priority-ranked prompt assembly, 50/30/20 allocation, 3-tier token budgets, head-trimming, KL `effective_score = raw - λ·complexityCost·100` |

**Stop rule per sub-area:** Tracked. No sub-area halted early — every angle still surfaced novel candidates at search 3+. A4 (vector DB) reached diminishing returns at benchmark-detail level but still yielded new hybrid-search distinctions; A6 surfaced repeated ASI06 synonyms by search 4 but new attack vectors (GLOBAL commit_memory) still emerged. Conservative stop: 3 consecutive searches yielding only known synonyms/trivia/niche noise was not met for A1-A5,A8-A9; met for narrow RAG benchmark trivia where synthesis not needed.

**Quality bar:** Every claim below requires ≥2 independent sources; vendor marketing cross-checked vs OSS implementation or survey/paper. Translation check ≥2 ecosystems per candidate is in §6.

**Batch 1 non-duplication:** E1-E11 (Delegated Subagent, Agent Teams, Orchestration, Workflows, Background/Async, Isolated Workspace via git worktree, Autonomy Calibration, HITL, Parallel Fan-out, Lifecycle Hooks, Reversibility/Compensation) are referenced only as interaction points — no re-promotion to taxonomy.

---

## 1. P1-09 SWEEP — What Exists, Where It Lives, How It Works

### 1.1 Claude Agent SDK — Context Management as Runtime Primitive

**What it is:** First-class harness-runtime feature. SDK exposes `Context Management & Runtime` with *automatic compaction when approaching limits*, built-in memory management, async context manager, and `CLAUDE.md` as persistent scratchpad. Predecessor is Claude Code's `/compact` slash command.

**Problem solved:** Long-running agents (>30k tokens) hit context-window ceiling → goal drift (SC-09 CSP), cost explosion (SC-05 CPSR), and reasoning degradation ("window stuffed to 95% does not just cost more money, it *reasons worse*"). Earlier conversations lose early instructions.

**How it works:**
- Auto-compaction triggers at ~80-90% utilization (threshold varies by CLI version) — reads full history, produces condensed summary via LLM, replaces older messages. Billed against full current context.
- Observability: emits `type:"system"` / `subtype:"compact_boundary"` in stream post-compaction; session ID preserved (native compaction inside same session).
- Customization: `autoCompactEnabled:true` in `.claude/settings.json`; proposer-suggested heuristic *intervene at 60%* before auto-compact; multi-strategy `runContextMaintenance` → `pruneMessagesIfNeeded` → `compactMultiStrategy` at 60% (micro-compact: header/thinking pruning), 75% (full LLM summarization via `buildLlmSummarizer`), 90% (emergency prune 30% non-protected).
- **Critical design choice:** Persistent rules belong in `CLAUDE.md` (re-injected on every request via `settingSources`), NOT in initial prompt, because compaction may drop early instructions. Same pattern appears in hierarchical context §1.5.

**Lifecycle:** `run` (cross-cutting, every turn) — compaction is invisible caller-side; interrupts are async. SC-09 probe (40k synthetic task + 5-QA `memory-probe` + `memory_snapshot.json`) directly measures survival.

---

### 1.2 OpenAI Agents SDK — Handoff-Centric, Lightweight Memory

**What it is:** Lightweight standalone SDK (Swarm → production-grade). Three primitives handle almost everything: **Agents, Handoffs, Guardrails**. Memory described as `Sessions (persistent working context)` vs LangGraph `Memory Store + filesystem`.

**Problem solved:** Multi-agent delegation without context loss. Without memory handoff, the new agent starts from scratch. Challenge: guardrails scope (input only first agent, output only last) and validation/tracing across handoffs.

**How it works:**
- Handoff = `function handoff` or passing agent into `handoff` option of `Agent` constructor. Carries conversation context through transition. Stays within single run.
- Triage pattern: router agent delegates to specialized narrow agents.
- Context Management = `Conversation context (ephemeral)` — contrasts with LangChain's auto-summarization + file offload. Reference impl shows session-scoped memory carried across handoffs; integration work wraps context/state and protects handoff context between agents.
- Comparison note in ecosystem: more capable models show *higher* vulnerability to memory poisoning when trajectories are reused — handoff is attack surface (see §1.6).

**Lifecycle:** `build (define handoff graph) → run (single-run handoff)`.

---

### 1.3 LangChain / LangGraph — Canonical Split: Checkpointer vs Store vs LangMem

This is the most instructive taxonomy for P1-11.

**Deprecation signal:** `ConversationBufferMemory` deprecated `v0.3.1`, removal at `v1.0.0`. Replacement is LangGraph persistence.

**Two primitives (and users confuse them — documented pitfall):**

| Primitive | Scoping Key | What It Holds | Analogy | Backend Examples |
|-----------|-------------|---------------|---------|-----------------|
| **Checkpointer** | `thread_id` (one conversation session) | Conversation history within current session, survives restarts | Short-term / episodic / working memory, in-context scratchpad + checkpoints | `MemorySaver`, `SqliteSaver`, `PostgresSaver`, `MongoDBSaver` (writes `checkpoints` + `checkpoint_writes`), `DynamoDBSaver`, `langgraph-oracledb` |
| **BaseStore** | `user_id` (all sessions for one person) — *one user has many thread_ids* | Facts that survive across ALL sessions for a user, namespaced by user identity | Long-term / semantic memory, cross-thread facts | `PostgresStore`/`InMemoryStore` with semantic search, `MongoDBStore`, `DynamoDBStore` |

- **Checkpointer** saves/restores state after each step per `thread_id`. Common mistake: using it as drop-in for `ConversationBufferMemory` expecting cross-session preference recall — it does not.
- **BaseStore** now supports **semantic search** (meaning not exact match) in `PostgresStore`/`InMemoryStore`.
- **LangMem SDK** layers on top of `BaseStore` to provide 3 memory types: *semantic* (user facts/preferences), *episodic* (past interaction examples), *procedural* (self-updated system prompt). Only this layer lets agent rewrite its own system prompt from experience.

**Broader memory map used in docs:** `in-context memory (working: scratchpad+checkpoints) → episodic (past retrieval) → semantic (structured facts) → procedural (rules)`.

**Lifecycle:** Checkpointer `run (per-turn persistence)`; Store `cross-run / cross-session persistent`.

---

### 1.4 RAG Systems — LlamaIndex vs Haystack + Vector DB Substrate

**Unified RAG workflow (both frameworks):** `Document Loading → Splitting/Chunking → Embedding Generation → Vector Storage → Query Processing → Similarity Search → Context Augmentation → LLM Generation`. Core components: *Retriever* (semantic/hybrid/BM25), *Generator* (LLM), *Knowledge Store* (DB/index), *Embedding Model*.

**LlamaIndex — data framework, indexing-centric:**
- Philosophy: *simplifies indexing and retrieval for private/domain data*, earlier `GPT Index`.
- Data model: document → **nodes** (text + vector embedding + metadata). Metadata-filtered retrieval.
- Example scratch: `PyMuPDFReader → SentenceSplitter chunk_size=1024 → TextNode → HuggingFaceEmbedding BAAI/bge-small-en → vector_store.add(nodes)` → query via `VectorStoreQuery(query_embedding, similarity_top_k=2, mode="default"/"sparse"/"hybrid") → NodeWithScore → VectorDBRetriever → RetrieverQueryEngine`. Auto-Retrieval infers metadata filters via LLM.
- Vector store breadth: Postgres/pgvector, Chroma, Qdrant, Weaviate, Pinecone, Milvus, FAISS, Azure Cognitive Search, MongoDB Vector.

**Haystack — pipeline orchestration, modular:**
- Philosophy: `Pipeline orchestration framework, modular pipeline components` with Elasticsearch/FAISS/Pinecone.
- Stack example: `Haystack 2.x for orchestration + Qdrant (or Pinecone/Weaviate) as vector DB + Sentence-Transformers embeddings + Mistral-7B generation + FastAPI`. Variants: Haystack + Anthropic Claude + Docker, Haystack 2.x + Db2 `VECTOR` column + `VECTOR_DISTANCE`, multi-vector-store querying with different embeddings/chunking via Neo4j orchestration.
- Hybrid search: fuses dense + BM25 via Reciprocal Rank Fusion or `alpha` parameter.
- 2.x swappability: `Embedders/Generators` swappable.

**Comparison:**

| Dimension | LlamaIndex | Haystack |
|-----------|------------|----------|
| Abstraction | `Nodes (text+embedding+metadata)`, `VectorStoreIndex` | Pipelines: ingestion/embedding/retrieval/generation components |
| Retrieval mode | `VectorStoreQuery` default/sparse/hybrid top-k semantic | Dense + BM25 hybrid, semantic ETL, multi-store fan-out |
| Positioning | Data framework | Pipeline orchestration framework |

**Vector database layer (decision substrate for RAG):**

| DB | Core Lang | Deployment | Hybrid Search | Filtering | Scale Practical | License | Best For |
|----|-----------|------------|---------------|-----------|-----------------|---------|----------|
| **Pinecone** | Managed | Cloud-only | Yes (serverless) | Metadata filters | 100M+ pods | Proprietary | Production zero-ops, 23-50 ms P99, pay-per-query serverless |
| **Qdrant** | Rust | Self-host or cloud | Yes (built-in sparse) | Payload indexed | 100M+ | Apache-2.0 | Production RAG fast filtering, quantization memory efficiency, 5 ms P50 / 20 ms P99 |
| **Weaviate** | Go | Self-host or cloud | Yes (BM25+dense alpha) | GraphQL where + multi-tenancy | 100M+ | BSD-3 | Schema-rich, multi-tenant, native hybrid |
| **Chroma** | Python | Embedded/server | Limited | Metadata dict | <5M practical | Apache-2.0 | Local dev / prototyping, embedded LangChain/LlamaIndex integration |

Benchmark signal (2024-25 framework): Pinecone lower p95 latency (23 ms vs 34 ms vs Weaviate in one e-commerce 15M SKU case, 22% lower bill) but Weaviate hybrid filtering + OSS fallback won; general P50 latencies — FAISS 1 ms, Qdrant 5 ms, Milvus 10 ms, Chroma 15 ms, Pinecone 30 ms (network included).

**Lifecycle:** `build (ingest→index) → run (retrieve→augment→generate)`.

---

### 1.5 IDE Agents — Context Injection Spectrum: Manual vs Automatic vs Deep

Search table is clearest summary:

| Platform | Context Injection | Indexing | Rules File (Project Bible) | How Rules Work |
|----------|-------------------|----------|----------------------------|----------------|
| **Cursor** | `@codebase`, `@files`, `@docs`, `@file`, `@git`, `@folder` — precise but manual; exceptional 200k+ token window + RAG retrieval | Full repo vector indexing locally via embeddings; `@codebase` auto-retrieval | `Rules for AI` in Settings or `.cursorrules` or `.cursor/rules/your-rule-name.mdc` (globs/auto vs manual `@`) | `.mdc` files auto-apply by file pattern or manual invoke |
| **Windsurf** | Full-repo embeddings; Cascade chooses context automatically | Proprietary deep index; auto-scans whole repo, picks affected files, executes tests/commands, patches directly | `.windsurfrules` (legacy) → `.windsurf/rules/rules.md` (newer) | Project rules override global |
| **GitHub Copilot** | Recently added repo indexing for Copilot Chat → whole-repo Q&A | High repo-level context | `.github/copilot-instructions.md` | Prepended as instructions to every Copilot Chat prompt |
| **Continue.dev** | `@codebase` via local Chroma | Chroma vector DB | — | — |
| **Cross-tool hierarchical pattern** | L0 Global project map ~2KB always loaded → L1 Per-project context ~3-5KB on demand → L1.5 Graphify graph ~10KB optional → L2 Source files only when needed | Graphify optional | `~/CLAUDE.md`, `~/GEMINI.md`, `.cursorrules`, `AGENTS.md` spine | Agent navigates down from project map to file instead of grepping up from disk root; fixes context-rot by narrowing |

**Portability note (critical for harness):** Same markdown content can be dropped across `CLAUDE.md` / `.codex/agents` / `.github/agents` / `GEMINI.md` / `.cursorrules` → but file-convention fragmentation (`.claude` vs `.codex` vs `.github/agents` vs `.gemini` vs `.windsurf`) is anti-portable; `AGENTS.md` spine + thin adapter (SynaptixLabs) is mitigation catalogued in Batch 1 M3/S3. SocratiCode is cited as independent index-once, plug-into-any-assistant mitigation for built-in indexes tied to one tool.

**Lifecycle:** `build (rules + index provision) → run (per-prompt injection)`.

---

### 1.6 Letta/MemGPT, Mem0, Zep/Graphiti — The Agentic Memory Spectrum

Three architectural camps:

**1) Hierarchical paging — Letta (formerly MemGPT):** `Berkeley → Towards LLMs as Operating Systems` — treats context window as **RAM** and external store as **disk**. Agent pages memories in/out via explicit tool calls (`core_memory_replace`, `archival_memory_insert`). Tiers:
- **Core memory** — always in context (RAM)
- **Recall memory** — recent conversation history (cache)
- **Archival memory** — external vector store (disk)
Self-managed, handles memory-pressure interrupts. Complete agent runtime, not drop-in library. ~23k stars, Apache-2.0, Agent Dev Environment visual debugging.

**2) Temporal knowledge graph — Zep/Graphiti:** Builds **bi-temporal knowledge graph** (validity windows) from unstructured conversation + structured business data. Entities + relations as graph; facts have `valid_from/valid_to`; supports `as-of` and fact invalidation queries. Benchmarks: Zep 94.8% vs 93.4% competitor; validated on LongMemEval. Use when reasoning over *how facts evolved over time* is required. Selected in real evaluation (oyster #30) over mem0/supermemory/turbopuffer for cross-session persistence via FalkorDB + MCP, local Docker.

**3) Extraction pipelines — Mem0:** Vector store + LLM-based fact extraction, lightweight SDK. Managed memory layer gaining rapid adoption for personalized AI. Stores user preferences, past decisions, task history, summaries, reflections.

**4-tier cognitive taxonomy (CoALA → Tulving) used across camps:**

| Tier | Human Analog | Agent Content | Stored As |
|------|--------------|---------------|-----------|
| **Working Memory** | Active RAM | Active context window, scratchpad, checkpoints | In-context tokens |
| **Episodic Memory** | Memory of specific events | "What happened" — interactions, traces, outcomes, timestamped logs | Event/episode summaries (SqliteSaver per session) |
| **Semantic Memory** | General knowledge | "What is true" — user facts, preferences, entities, de-contextualized knowledge | Vector-embedded facts, KG triples (`profiles/<user>.md`) |
| **Procedural Memory** | Skills/how-to | "How to act" — rules, workflows, skills, tool patterns | Editable system prompt, code, skill libraries (LangMem only writer) |

**Short-term vs Long-term operationalization:**
- Short-term / working = *inside context window* (vector, latent hidden states, token-level)
- Long-term = *outside window* (vector / graph / SQL / files) — i.e., MemGPT RAM vs Disk.

**Memory stores comparison (production):** `mem0 | Mem0 | 50k+ stars | Vector+fact extraction` vs `graphiti | Graphiti/Zep | 24k+ | Temporal KG` vs `Letta | ~23k | Hierarchical paging` vs `MemoryPilot v4.2 | Hybrid + transformer embeddings | Temporal triples validity+confidence` vs `NirDiamant/Agent_Memory_Techniques | 30 notebooks | buffers/vector/KG/episodic/semantic/MemGPT/Mem0/Letta/Zep/LoCoMo`.

**Lifecycle:** `run → cross-run (persistent)`; procedural writes are `build-time (skill authoring) or run-time self-rewrite (LangMem)`.

---

### 1.7 Security Literature — Context & Memory Poisoning (OWASP ASI06)

This is the adversarial lens that decides whether memory can be trusted.

**Threat model (Memory Poisoning = persistent indirect prompt injection):**
- Attacker plants false information into agent long-term memory or context; later, on *unrelated task*, agent acts on planted belief — analogous to supply-chain attack with *no malicious code, just a confidently-worded claim*.
- **OWASP ASI06 Memory & Context Poisoning:** single poisoned entry suffices. If agent stores raw trajectories as in-context memory, cross-site attacks bypass domain permission controls.
- Validated vectors:
  - **Tool Result Injection** → instructs Claude to update memory files with attacker-controlled content → `STATE_MODIFICATION` mapping.
  - **GLOBAL memory cross-workspace:** root workspace agent writes `GLOBAL`-scoped memory via `commit_memory`; all workspace agents read via `recall_memory` with *no sanitization* → persistent cross-workspace prompt injection.
  - **ElizaOS crypto hijack:** after poisoning shared memory, researchers induced unauthorized smart-contract sign/transfer to attacker address — short injections buried in memory consistently overrode guardrails.
  - **Letta archival attack:** single poisoned archival entry biases all future reasoning (archival = cold storage, rarely re-validated).
- **eTAMP benchmark (arXiv):** high attack success rates when raw trajectories reused as memory; GPT-5.2-level capable models show *substantial vulnerability* — capability does not mitigate.
- **Framework gap:** Many frameworks currently have *no validation layer* to prevent adversarial inputs from being stored. Agno, Mem0, Letta noted as exposed surfaces; OWASP Agent Memory Guard proposed as defense SDK; `Memory Poisoning Attacks in LLM Agents (June 2026 arXiv)` is reference.

**Lifecycle:** `run (ingest) → persistent → all future runs (blast radius unbounded)`. This argues for **memory as distinct capability requiring its own governance**, not just ephemeral context.

---

## 2. Candidate Element Catalog — Required Fields

Every candidate below lists canonical name, definition, problem, why it matters (SC wiring), level, lifecycle role, related concepts, cross-ecosystem terms (≥2), confidence, tier.

### E12 — Context Management & Compaction (Context Engineering)

**Definition:** Harness/runtime layer that assembles, prioritizes, budgets, prunes, compacts, and restores the active LLM context window per turn. Includes token estimation (`tokPerChar`, `msgChars`), priority-ranked prompt assembly (e.g., P0-P10 chain or question>harness_feedback>judge_guidance>manifest>domain_rules>prior_steps), threshold-gated compaction (`maybeCompact`, `prepareCompaction/applyCompaction`, `compactMultiStrategy`, `emergencyTrim`), and observability (`compact_boundary`).

**Problem:** Context rot, window overflow (indivisible large tool outputs re-sent every call), attention dilution, cost blowup, goal drift on long tasks (>30k tokens). "Full ≠ free: 95% window reasons worse."

**Why it matters:** Direct SC-09 CSP predictor (≥85% QA C4/C6, ≥75% C2; goal embedding cosine >0.90). Also SC-05 CPSR (token discipline) and SC-02 TSR (wrong/incomplete context = primary failure mode). V-C harm≥4 if absent.

**Level:** **Capability** (Mechanisms: compaction, pruning, summarization, offload, budget enforcement, interception). *Not* Tool — multiple Frameworks implement it.

**Lifecycle:** `build (policy, priority chain, thresholds) → run (every turn, cross-cutting) → review (memory_snapshot.json, trace compaction boundary)`.

**Related concepts:** Prompt architecture (nested inside), context budget, context rot, sliding window, token-aware pruning, LLM summarization, dual-state lossless (Immutable Store + Active Context), subagent context isolation (Batch 1 E1), `CLAUDE.md` re-injection.

**Cross-ecosystem terms (≥3):**
- Claude Agent SDK `autoCompactEnabled` + `/compact` + `compact_boundary` ≡
- LangGraph `Checkpointer` state persistence + `Store` off-window ≡
- Cursor `@codebase` retrieval + 200k window vs Windsurf Cascade auto-full-repo embeddings ≡
- Letta RAM vs Disk paging (`core_memory_replace`) ≡
- `ContextManager` P0-P10 priority chain + `ContextBudgeter.MODEL_LIMITS`

**Confidence:** High

**Tier (preliminary):** **foundational** — harm 4-5 for SC-09/SC-05 on C4/C6 long tasks; frequency high across all C1-C6 long-horizon tasks.

---

### E13 — Agent Memory — Persistent, Evolving State (Short-term vs Long-term; Semantic / Episodic / Procedural)

**Definition:** Agent's ability to retain, distill, structure, and recall relevant information *over time, across tasks, and through multiple sessions* — not raw chat history. Three pillars: **State, Persistence, Selection**. Hierarchy: Working (in-context scratchpad + checkpoints, ephemeral), Episodic (temporal experience logs), Semantic (de-contextualized facts/preferences/entities), Procedural (behavioral rules/skills/system prompt).

**Problem:** Chat history is raw, flat, linear, proximity-based, and resets per session — treats all tokens equally, scales cost by re-sending, lacks continuity/adaptivity. Memory must decide *what survives across time* and be *relevance/salience-based*.

**Why it matters:** Enables continuity, personalization, learning from success/failure, cross-session preference recall — without which long-horizon C4 (agent) and C6 (migration) fail SC-09 and SC-02. Contrast with RAG: `RAG helps answer better (stateless per query, no time/user modeling); Memory helps behave smarter (stateful, tracks order/timing/evolution, user-modeled, adaptive)`. Cost scaling: memory = retrieval not re-sending → SC-05.

**Level:** **Capability** (Mechanisms: extraction, consolidation, forgetting, retrieval; Forms: token-level explicit discrete vs parametric weights vs latent hidden states; Dynamics: formation → evolution → retrieval).

**Lifecycle:** `run (write path: extract facts/preferences, dedup, store with metadata) → persistent (cross-session) → run (read path: relevance-filtered recall) → build-time (procedural skill authoring) or run-time self-rewrite (LangMem)`.

**Related:** Retrieval (how it is found), knowledge management (shared stabilized vs adaptive personal), context management (what enters window now), HITL trust (if memory poisoned), checkpoint/rewind (Batch 5 — distinct from memory continuity).

**Cross-ecosystem terms (≥4):**
- LangGraph `Checkpointer (thread_id, SqliteSaver/PostgresSaver/MongoDBSaver)` vs `BaseStore (user_id, PostgresStore semantic search) + LangMem (semantic/episodic/procedural) + InMemoryStore` ≡
- Letta `Core (RAM) / Recall (cache) / Archival (disk) + archival_memory_insert/recall_memory` ≡
- Claude `CLAUDE.md scratchpad (re-injected) + memory_snapshot.json` ≡
- Zep/Graphiti `temporal/bi-temporal KG (validity windows, as-of queries, FalkorDB)` ≡
- Mem0 `vector store + LLM fact extraction` ≡
- Anthropic 7 Layers (Mar 2026), NirDiamant 30 notebooks covering buffers/vector/KG

**Confidence:** High

**Tier:** **foundational** — missing persistent memory → SC-09 <50% on C4/C6 (lab threshold), SC-02 lagging on personalized tasks.

---

### E14 — Retrieval & Augmented Generation (RAG) — Access Strategy

**Definition:** `RAG is not a knowledge strategy. RAG is an access strategy.` Pipeline that retrieves relevant external information (chunk → embed → vector store → similarity search → re-rank → prompt assembly) and augments generation. Includes retriever types (semantic dense, BM25 sparse, hybrid fusion), embedding model, knowledge store (vector DB, Elasticsearch), knowledge graph traversal, and auto-retrieval metadata filtering.

**Problem:** LLM parametric knowledge is static, hallucinated, non-grounded; private/domain data is not in weights; context window cannot hold entire corpus. Need query-time grounding.

**Why it matters:** Faithfulness/groundedness (SC-02 for C4 research, SC-08 citation gate), but *stateless by design* — each query independent, no temporal awareness, no user modeling, cannot learn from past interactions. Precision without persistence. Harness must decide retrieval relevance vs memory continuity. Vector DB choice dominates latency/Pareto (Pinecone vs Qdrant vs Weaviate vs Chroma) at 100M+ scale.

**Level:** **Mechanism cluster** — but when tied to external knowledge pipeline (chunking→indexing→retrieval) it behaves as **Capability `Knowledge Retrieval`** (see E15 split). For taxonomy hygiene: *Retrieval = Mechanism*; *Knowledge Retrieval over external corpora = Capability realized by RAG protocols + vector DB tools*. Do not promote embedding model alone to Capability.

**Lifecycle:** `build (doc loading, splitting chunk_size 1024, embedding, vector_store.add) → run (query embedding → similarity_top_k → NodeWithScore → RetrieverQueryEngine → generation)`.

**Related:** Context management (augments window), memory (retrieval is how memory is found — distinct failure modes: semantic similarity recall vs exact ID pointer recall), knowledge management (curation upstream), vector DB, re-ranking.

**Cross-ecosystem terms (≥4):**
- LlamaIndex `VectorStoreIndex, nodes, VectorStoreQuery top_k sparse/hybrid, RetrieverQueryEngine, Auto-Retrieval` ≡
- Haystack 2.x `Pipelines (ingestion/embedding/retrieval/generation swappable), Qdrant/Weaviate/Pinecone adapters, RRF fusion, Db2 VECTOR_DISTANCE` ≡
- LangGraph `BaseStore semantic search (PostgresStore), InMemoryStore` ≡
- Cursor `codebase embeddings + @codebase provider (local vector DB)` / Continue.dev `Chroma @codebase` / Windsurf `proprietary full-repo embeddings` ≡
- Pinecone `serverless pay-per-query` vs Qdrant `Rust + quantization + payload filters` vs Weaviate `GraphQL + BM25+dense alpha + multi-tenancy` vs Chroma `embedded Python`

**Confidence:** High

**Tier:** **important** — foundational for C4 research/tool-using and C2 docs-gold; situational for C5 infra where retrieval is not primary.

---

### E15 — Knowledge Management & Curation (Knowledge Base)

**Definition:** Structure and governance of *shared, stabilized* knowledge (docs, policies, specs, codebase understanding) — ingestion, chunking, indexing, metadata, freshness/versioning, deduplication, provenance, access control, and retrieval-correctness — distinct from adaptive personal memory and from query-time retrieval statelessness. Covers PKM-individual vs Wiki-shared vs RAG-machine patterns and code-intelligence MCPs.

**Problem:** RAG retrieves but does not curate; memory remembers but is personal/adaptive, not shared canonical. Without curation, retrieval degrades (stale chunks, duplicate/conflicting knowledge, missing provenance) and memory hallucinates shared facts.

**Why it matters:** Grounding quality, citation discipline, onboarding speed, cross-agent consistency. `codebase-memory-mcp` (tree-sitter AST → persistent KG) and `claude-memory-compiler` (hooks capture every interaction → SDK extracts decisions/lessons → LLM compiler distills into cross-referenced articles; `cold-memory` 34 on-demand spec-docs vs `hot-memory` constitution) show harness needs System ↔ Project knowledge separation with explicit scale guidance. `Facts as First Class Objects` (hash-addressed discrete fact tuples, 100% accuracy 252× cheaper than in-context) proposes discrete governance.

**Level:** **Capability** (Mechanisms: ETL pipeline, tree-sitter indexing, hook capture → extraction → compilation, knowledge objects, graph valid-time). Distinct from E14 retrieval mechanism and E13 personal memory.

**Lifecycle:** `build (index, graph build, spec authoring cold-memory) → run (on-demand retrieval via MCP/specs) → review (freshness audit, drift detection)`.

**Related:** Retrieval (consumer), memory (consumer of curated facts for semantic long-term), MCP Tools (delivery), documentation context (awesome-harness-engineering foundations), evaluation (groundedness SC-02/SC-08).

**Cross-ecosystem terms (≥3):**
- `codebase-memory-mcp` (AST KG) ≡
- `claude-memory-compiler` (34 spec-docs cold-memory on demand) ≡
- `Facts as First Class Objects` (knowledge objects) ≡
- Harness cold vs hot memory (spec-block vs constitution) ≡
- LlamaIndex/Haystack ETL ingestion stacks ≡
- Wiki (social contract "this page is place where knowledge lives") vs PKM (flexible thinking) vs RAG vs Memory (adaptive continuity)

**Confidence:** Medium-High (emerging pattern — cold/hot split, knowledge objects are proposal-stage, but code-memory MCP + compiler have OSS implementations)

**Tier:** **important** — specialized for C4/C2/C1 large-codebase; situational for single-session C3 glue. Promote to foundational if harness is multi-project/persistent.

---

### E16 — Prompt Architecture & Instruction Design

**Definition:** Message-level design of *how the question is phrased* — instructions, roles, directives, examples, guard clauses, acceptance criteria, anti-sycophancy directives, verbosity control — assembled within the broader context (who shapes what model sees) and harness (what agent allowed to do). Includes reusable prompt packs (Skills/slashes) and blueprint vs ad-hoc invocation.

**Problem:** Poorly worded instructions → primary failure mode at prompt layer; one-huge-prompt anti-pattern bloats context, wastes attention budget, harms focus.

**Why it matters:** Controls instruction following per turn; interacts with context budget (50% task context / 30% instructions / 20% examples allocation rule; progressive disclosure plan→retrieval→execution→verification; trim loop compress+coverage-check; drop order verbose examples→minimal, narrative→bullets, soft preferences). Harmless if prompt is clear but context is wrong — so placement matters.

**Level:** **Mechanism** under **E12 Context Management** (some harnesses promote to **Mechanism cluster `Prompt Pack Management`**). *Not* standalone Capability — source tables are explicit: `Prompt engineering remains a subset of context engineering. Context engineering exists as a subset within harness engineering. Full stack narrowest→broadest: prompt, context, harness, loop.` Computing stack analogy: `model=CPU, context=RAM, harness=OS`.

**Lifecycle:** `build (author prompt packs, CLAUDE.md rules) → run (per-turn phrasing, template interpolation)`.

**Related:** Context management (parent), Skills (resource = individual prompt pack; category = Capability Batch 3), complexity budget (governs), context poisoning (adversarial phrasing).

**Cross-ecosystem terms (≥3):**
- Claude `AGENTS.md / CLAUDE.md Operating Model, Skills slash commands` ≡
- Harness self-evolution `ContextManager priority chain P0-P10, domain_rules (80), prior_steps (60) smart_truncate/LLM summarize` ≡
- LangChain `prompt templates / SystemMessage` ≡
- Cursor `Rules for AI` / Windsurf `.windsurfrules` / Copilot `.github/copilot-instructions.md` ≡
- Prompt budgeting `50/30/20` + progressive disclosure + trim loop

**Confidence:** High

**Tier:** **important** as Mechanism; *situational* if treated as independent Capability (would inflate taxonomy 11→~30).

---

### E17 — Complexity Budget & Context-Budget Governance (Anti-Bloat Control)

**Definition:** Cross-cutting governance that decides *what to keep, offload, drop, or hand off to a fresh window* when long-horizon tasks fill the window — and *what dollar/attention cost is affordable*. Covers token budget (per-call and cumulative `HARNESS_MAX_TOTAL_TOKENS` with `StopReason.COST_BUDGET`), context budget (per-turn), attention budget (focus illusion), and bloat hygiene (inventory → classify Always/Sometimes/Rarely → trim).

**Problem:** Harness accumulates unbounded components (agents `agents/*.md`, skills, rules, MCP servers ~500 tokens/tool) → every turn pays 10k+ input tokens (e.g., 23.2KB todo list → fix top-25 urgency filter 9.0KB -61%). Without budget, loop burns cash before `max_rounds`; 95% window degrades reasoning; pre-inlined 75-line docs at every spawn bloat prompt.

**Why it matters:** SC-05 CPSR / CPAC / Pareto frontier (`pass@1 vs $/task`), SC-09 CSP, SC-01 latency. Two failure modes: *under-budget* → missing context; *over-budget* → context rot + cost overrun. Needs autonomous throttling (fleet JIT budget manager) and on-demand loading (Skills load on demand instead of bloating every prompt; `CLAUDE_CODE_FORK_SUBAGENT` read-at-runtime vs pre-inline).

**Level:** **Cross-cutting Concern / Governance Capability** (like Anti-Bloat from `plan.md §0.2` and `ARCHETYPES_AND_CRITERIA.md §8`). Mechanism-wise it is `Budget Enforcement + Priority Truncation + On-demand Loading + KL Regularization`. **Do not file as ordinary Mechanism under E12** — it spans context + cost + orchestration + MCP.

**How enforced (concrete patterns observed):**
- **Priority truncation:** Over budget → truncate P10 upward; P0-P2 never truncated (identity/safety); P7-P8 (MEMORY/EVOLUTION) head-trim oldest first. Over-budget sections compressed via `smart_truncate` or `LLM summarize`. Domain rules compiled only when large docs exceed budget fraction.
- **Tiers:** `Tier Default <200K ctx → 30K budget, Large → 50K, 1M ctx → 100K`.
- **Inventory skill:** `context-budget SKILL` across harnesses (harness-foundry / agent-stack / ericrisco/rsc-harness / pscheol/kiro-with-harness): scan every loaded component, estimate token overhead, classify Always/Sometimes/Rarely, surface prioritized savings. MCP servers counted ~500 tokens/tool.
- **KL regularization (Kairn):** `effective_score = raw_score - λ·complexityCost·100` (lines/files/sections/char diff vs baseline, default λ=0.1) — proposer mustearn every addition.
- **Hooks/cost tracking:** `complexity-gate.sh` (Python ≤8, Go ≤10, TS/JS ≤15), `doc-bloat-gate.sh`, token-budget badge (`ctx N% left` green/amber/red), `trace-driven build_context` urgency filter.
- **Pre-inline vs runtime read rule:** Do not pre-inline ~75-line files at every architect spawn; agent reads via `Read tool` at runtime.

**Lifecycle:** `build (define budgets, priority chain, KL λ, gate thresholds) → run (per-turn enforcement, cumulative HARNESS_MAX_TOTAL_TOKENS, fleet JIT throttle) → review (audit bloat drift, reconcile loop)`.

**Related:** Context management (primary client), cost tracking (Batch 5), harness versioning/reproducibility (budget drift), parallel fan-out E9 (multiplies cost).

**Cross-ecosystem terms (≥4):**
- Harness Foundry `context-budget SKILL (inventory agents/skills/rules/MCP ~500tok)` ≡
- Kairn `Agent Environment Compiler KL λ=0.1 complexityCost` ≡
- Forge `CLAUDE.md complexity budget (LOC estimate senior would write), anti-sycophancy` ≡
- Harness detail `token-budget badge + Context budget / Copy summary` + `tracker HARNESS_MAX_TOTAL_TOKENS → COST_BUDGET` ≡
- Prompt budgeting `50/30/20 + progressive disclosure + trim loop (300-800 tokens lookup, 800-2000 code review)` ≡
- ContextManager `ContextBudgeter.MODEL_LIMITS` 30K/50K/100K + P0-P10 head-trim

**Confidence:** High

**Tier:** **important as Governance** — foundational if harness is long-horizon / fleet / team; otherwise specialized per-task. Harm 3-4 for C4/C6 when absent.

---

### E18 — Memory / Context Poisoning Defense (related to P1-12, cross-ref)

**Definition:** Adversarial hardening: validation, sanitization, provenance, trust-partitioning, and access-control for memory reads/writes and context injection.

**Problem:** Memory poisoning persists across sessions and workspaces; more capable models are *more* vulnerable.

**Level:** **Security Capability** (Batch 4 proper). For Batch 2 catalog: **cross-cutting security mechanism** on E12+E13+E14 read/write paths. Do not promote to standalone Context capability — keep as Batch 4 item with Batch 2 wiring.

**Lifecycle:** `build (allowlist, provenance schema, trust zones) → run (sanitize recall_memory, validate commit_memory, block tool_result → STATE_MODIFICATION)` → `persistent audit`.

---

## 3. P1-11 — DISTINCTION DECISION: One, Two, or Four?

**Question:** Are context management vs memory vs retrieval vs knowledge management **ONE capability, FOUR, or TWO with mechanisms**? Evidence for split/merge.

**Direction:** **TWO foundational Capabilities with TWO important Mechanisms that behave as Capabilities at their layer; default taxonomy = 2+2 with explicit Mechanisms (not 1, not 4 peers).**

| Interpretation | What It Claims | Evidence For | Evidence Against | Verdict |
|----------------|----------------|--------------|------------------|---------|
| **One (Monolith: "Context")** | All four are just context-window filling | Attractive anti-bloat: reduces taxonomy; matches Karpathy `fill window with just right info` slogan + harness ` ContextManager` single priority chain | Collapses stateful vs stateless (RAG vs Memory), shared vs personal (Knowledge vs Memory), ephemeral vs persistent (Context vs Memory). Fails LangGraph checkpointer vs store pitfall; OWASP ASI06 persistence blast radius unexplained; Mem0 vs Graphiti benchmarks distinguish vector vs KG precisely because persistence+time matters; RAG paper table shows `stateful adaptive` vs `stateless task-bound` orthogonal | **Kill** — V-C would refute with ≥2 counter-sources (LangGraph split, OWASP persistence). |
| **Four peer Capabilities** | Four independent Capabilities | Clean ownership; maps to tool categories (vector DB vs memory SDK vs prompt pack vs wiki) | Inflates taxonomy (11 Batch 1 → +4 = 15 before budgets). Retrieval alone is *how* not *what* — it serves both retrieval & memory. E16 prompt would then be fifth peer, taxonomy explodes to 5. Redundant scoring: context budget would be scored three times. | **Demote** — keep split intent but re-tag retrieval & prompt as Mechanisms. |
| **Two with Mechanisms (recommended)** | **Foundational: Context Management (E12) + Agent Memory (E13). Important Mechanisms: Retrieval/Augmented Generation (E14) and Knowledge Management (E15) treated as Capability at KB layer but Mechanism at runtime.** | Best fits sources: nested stack `Prompt ⊂ Context ⊂ Harness` (Karpathy/Lütke/Hashimoto/Lopopolo/Fowler) proves prompt is mechanism inside context; LangGraph checkpointer (`thread_id`) vs store (`user_id`) + LangMem proves memory has *Forms/Functions/Dynamics* distinct from context window; survey `Memory in Age of AI Agents` taxonomy (Forms token/parametric/latent, Functions factual/experiential/working, Dynamics formation/evolution/retrieval) distinguishes memory from context engineering & RAG explicitly; PKM vs Wiki vs RAG vs Memory 4-system comparison table shows *knowledge* is third party (stabilized shared) vs *memory* adaptive personal — merging knowledge→memory loses social-contract property | Still leaves knowledge placement ambiguous: is knowledge just long-term memory? Counter: `Facts as First Class Objects` + `claude-memory-compiler` cold-memory 34 spec docs prove knowledge needs *versioned governance* that memory pipeline (extraction) does not guarantee. So E15 needs Capability tag at KB layer though it consumes E14 retrieval | **Keep — 2+2 with dual-level note.** |

**Evidence table for split:**

| Pair | Distinct Problems? | Distinct Lifecycle? | Distinct State? | Distinct Failure Mode? | Keep Split? |
|------|-------------------|---------------------|-----------------|------------------------|-------------|
| **Context vs Memory** | Context overflow/routing vs cross-session persistence/selection | Context per-turn ephemeral vs memory cross-session persistent | `Context Window ≠ Memory` table: temporary reset vs persistent, flat equality vs hierarchical priority, proximity recall vs intent recall | Context fail: wrong/incomplete info at step; Memory fail: lost continuity, hallucinated preferences, poison persists | **Yes — keep split** (2 sources: Claude SDK compact vs LangGraph store, plus MemoryAgentBench) |
| **Memory vs Retrieval** | Memory = *what continues to shape behavior* (State/Persistence/Selection) vs Retrieval = *how it is found* (similarity vs exact ID) | Memory evolves (formation→evolution→retrieval dynamics) vs retrieval per-query | Memory carries time/user modeling; retrieval can be stateless RAG or memory-specific semantic recall | Retrieval fail: low recall@k / latency; Memory fail: wrong evolution, poison retention, forgetting | **No — retrieval = Mechanism** (serves both memory & knowledge; two-source split `conversation recall by meaning (semantic top_k) vs data recall by exact ID (pointer)»`) |
| **Knowledge vs Memory** | Knowledge: shared stabilized reference governed by social contract + freshness; Memory: adaptive personal continuity | Knowledge build→on-demand spec fetch→freshness audit vs memory persistent stateful evolution | Knowledge stabilized explicit structure (wiki/KG) vs memory adaptive learned/extracted | Knowledge fail: stale docs / conflicting facts / missing provenance; Memory fail: poison/global bleed | **Dual — Knowledge = Capability at KB layer, Mechanism-wise is ingestion/indexing pipeline that retrieval consumes** |
| **Prompt vs Context** | Prompt: single-turn instruction phrasing; Context: session-level window composition (memory+retrieved+tool outputs+schema) | Both per-turn but prompt innermost, context wraps it | Prompt is subset of context | Prompt fail: poorly worded; Context fail: wrong/missing context (broader) | **No — prompt = Mechanism under Context** (harness stack figure) |

**Canonical phrasing from sources (for audit):**
> `Prompt engineering shapes instructions, context engineering shapes what the model sees, and harness engineering shapes the full agent environment: tools, memory, constraints, and feedback loops. Full stack narrowest→broadest: prompt, context, harness, loop. Each layer wraps the one before it.`
> `RAG is not a knowledge strategy. RAG is an access strategy. AI memory is not just long context. Long context lets a model see more at once. Memory decides what survives across time.`
> `storage is where information sits, retrieval is how it is found, memory is what continues to shape behavior, and the harness is the runtime that decides what enters and exits the model's working context.`

**Implication for MASTER_TAXONOMY:**
- List **E12 Context Management & Compaction** → Capability, foundational.
- List **E13 Agent Memory** → Capability, foundational, with subtypes Working/Episodic/Semantic/Procedural (note Forms/Functions/Dynamics not separate Capabilities).
- List **E14 Retrieval & Augmented Generation** → *Mechanism cluster* (Capability label only when scoped to external corpora `Knowledge Retrieval` — keep as Mechanism to avoid double count; tool registry holds vector DBs).
- List **E15 Knowledge Management & Curation** → *Capability at KB/persistent-doc layer*, otherwise Mechanism cluster ingestion/indexing; tier important.
- Do NOT create a fifth peer for prompt — wire to E16.

---

## 4. P1-13 — PROMPT ARCHITECTURE & COMPLEXITY BUDGETS: Where Do They Live?

### 4.1 Prompt Architecture

**Three plausible placements tested:**

| Placement | Tag | Argument | Test |
|-----------|-----|----------|------|
| Standalone Capability | Capability | Prompt skill packs (30-40 keepers) feel capable; separate directive from context assembly | Fails anti-bloat: would justify scoring prompt packs independently from context quality; sources explicitly nest `prompt ⊂ context ⊂ harness`. Split multiplies taxonomy without new failure mode. |
| Mechanism under Context Management | Mechanism | Sources: `Context engineering shapes what model sees — retrieved docs, memory fragments, tool outputs, conversation history` subsumes prompt phrasing; message-level phrasing controls are applied *within* the assembled context | **Pass** — aligns with `The harness is core innovation: 11-file priority chain P0-P10 with token budget management` where prompt is section P? inside chain. |
| Cross-cutting Concern | Concern/Bloat | Prompt quality interacts with every turn irrespective of domain | Partially true but concern label misses instructional content ownership — phrasing rules (anti-sycophancy, acceptance criteria, complexity budget line inside CLAUDE.md) belong to instruction design, not governance. |

**Decision:** **Mechanism under E12 (Context Management),** with **resource type `Prompt Pack / Skill`** catalogued in Batch 3 (Integration) not here. Category `Skills as Capability` vs `individual skill as Resource` hygiene from Batch 1 M7 applies: `Skills` category is Batch 3 Capability; `context-budget` or `prompt-arch` individual skill is Resource; `prompt architecture` the practice is Mechanism here.

Evidence: Harness-foundry `ContextManager Sections ranked by priority: question (100) > harness_feedback (96) > judge_guidance (94) > manifest (90) > domain_rules (80) > prior_steps (60)` — prompt instructions are sections inside same budget-competed assembly. Prompt budgeting framework `50/30/20 (context/instructions/examples) + trim loop + drop order verbose→minimal, narrative→bullets` is *budget-aware prompt design*, not separate system.

---

### 4.2 Complexity Budgets

**This is the more consequential placement — misplacing budgets causes Batch 5 dedupe failure.**

**Observed forms (≥5 independent sources):**

1. **Per-call token budget** (`ContextManager` 30K/50K/100K tiers, `ContextBudgeter.MODEL_LIMITS`, `ctx-gate drops least relevant turns when token-budget set`, `cool-memory vs hot-memory on-demand spec loading`)
2. **Cumulative cost budget** (`HARNESS_MAX_TOTAL_TOKENS → StopReason.COST_BUDGET`, fleet JIT budget manager throttles frequencies)
3. **Attention budget** (`model has lot of context but not infinite focus` → reasoning degrades at 95%)
4. **Complexity budget** (Forge `LOC senior would write + anti-sycophancy`; Kairn `λ complexityCost` regularization; hobby `hooks/complexity-gate.sh` cognitive thresholds)
5. **Documentation / component bloat budget** (`doc-bloat-gate.sh`, `context-budget SKILL` inventory of agents/skills/rules/MCP ~500 tok/tool, `pre-inline vs runtime Read` 75-line rule, `cost-optimized on-demand Skills loading`)

**Three placements tested:**

| Placement | What It Would Mean | Evidence For | Evidence Against | Harness wiring |
|-----------|-------------------|--------------|------------------|----------------|
| Mechanism under Context Management (`Context Budget` procedure) | Budget = pruning/compaction detail | Explains per-call token tiers and P0-P10 head-trim well | Misses cumulative cost `COST_BUDGET` spanning *multiple* calls, fleet JIT, and add/remove gate for *harness evolution* (Kairn) which is not context window at all | Would leave cost tracking (Batch 5), harness versioning, deprecation orphaned |
| Standalone Capability (`Token Budget Management`) | Budget = load-bearing harness subsystem with ledger, gauges, throttles | `Track token usage and cost per run with optional budget` proposal shows missing cumulative budget is P0 gap; token-budget badge `ctx N%` is user-visible capability | Overloads: token + attention + LOC complexity are three different budgets — bundling as one capability conflates cost accounting with anti-bloat hygiene | Requires 3 separate capabilities if split — taxonomy inflation |
| **Cross-cutting Concern + Governance Mechanism (recommended)** | Budget = **harness-level invariant**, like anti-bloat, governed in `GOVERNANCE.md`, enforced via hooks/skills/ledger across all Capabilities | Matches `plan.md §0.2` and `ARCHETYPES_AND_CRITERIA.md §8 Anti-bloat check` (12→6 canonical reduction itself is budget decision); aligns with plan's explicit phrase `complexity budgets tracked explicitly` and Phase 5 CR tag `complexity budgets, anti-bloat mechanisms, deprecation management` under DX/Meta (P1-36); matches how SC-05 CPSR, SC-01 latency, SC-09 CSP are *leading* indicators fed by budget | Needs concrete owner file — but that's `GOVERNANCE.md` + `cost-ledger.jsonl` + `.claude/hooks/*-gate.sh` + `context-budget SKILL`, exactly the harness-as-code artifacts already identified | **SC wiring: SC-05 (CPSR, CPAC, Pareto TSR vs CPSR, usd_per_query), SC-01 (P50 <90s), SC-09 (CSP) — all predict/measure budget health. Archetype variance: C3 (glue/browser fleet) and C4 (agent volume×tokens) budget-critical (High cost sensitivity per constraints matrix); C5/C2 idempotency tolerance low — budget gates prevent drift loops.** |

**Decision:** **Cross-cutting Concern & Governance Capability — not filed under E12.** In MASTER_TAXONOMY, list `Complexity Budgets & Anti-Bloat Governance` as **Cross-cutting Concern** (Batch 5 ownership) with **evidence anchor E17** here. E17 remains catalogued in Batch 2 evidence log for traceability, but re-tagged in P1-15 architectural pass as **Concern/Governance**, not Batch 2 Capability — parallel to how Batch 1's `E10 Lifecycle Interception / Hooks` was correctly kept as Capability but flagged as Batch 5 territory for full treatment (E10 was kept here only for permission-hook boundary).

**Rule for verifiers (V-D):** If prompt architecture + budgets are all under Context, V-D will flag *level conflation* (Mechanism promoted to Capability) and *batch boundary bleed* (Batch 2 absorbing Batch 5 governance). E17 must carry hygiene flag `Governance Concern — primary owner Batch 5 (P1-36/CR-01), Evidence owner Batch 2 (P1-13)`.

**Practical effect:** Skill writers must not create a new `Prompt Architecture Capability` scoring card; they reuse E12's rubric with 50/30/20 sub-check and E17's `context-budget` skill as gate.

---

## 5. Full Candidate Summary Table (for MASTER_TAXONOMY handoff)

| # | Canonical | Definition (one line) | Level | Lifecycle | Tier | Confidence | Batch Owner |
|---|-----------|----------------------|-------|-----------|------|------------|-------------|
| **E12** | Context Management & Compaction | Runtime assembly, prioritization, pruning, compaction, offload of active window | Capability | build→run (per turn) | **foundational** | High | Batch 2 |
| **E13** | Agent Memory (Persistent State — Working/Episodic/Semantic/Procedural) | State/Persistence/Selection across sessions with Forms/Functions/Dynamics | Capability | run→persistent→run (+ build self-rewrite) | **foundational** | High | Batch 2 |
| **E14** | Retrieval & Augmented Generation (RAG) | Chunk→embed→store→search→augment access strategy (semantic/hybrid/exact-ID) | Mechanism cluster (Capability when scoped to external KB) | build→run (query-time) | **important** | High | Batch 2 (tool registry vector DBs) |
| **E15** | Knowledge Management & Curation | Shared stabilized knowledge governance: indexing, freshness, provenance, KA | Capability (at KB layer) | build→run→review | **important** | Med-High | Batch 2 / Batch 3 bridge |
| **E16** | Prompt Architecture & Instruction Design | Message-level instruction phrasing, packs, directives, examples | Mechanism (under E12) | build→run | **important as Mechanism** | High | Batch 2 evidence, Batch 3 resource |
| **E17** | Complexity Budget & Context-Budget Governance | Token/cost/attention/LOC budgets, inventory, priority truncation, on-demand loading, KL regularization | **Cross-cutting Concern / Governance** | build→run→review | **important (foundational for long/fleet)** | High | **Batch 5 owner, Batch 2 evidence** |
| E18 | Memory/Context Poisoning Defense | Validation/sanitization/provenance/trust-partitioning for memory & context | Security Capability (Mechanism wiring here) | build→run→persistent | important | High | Batch 4 proper |

*E12+E13 are the TWO foundational Capabilities. E14 is the key Mechanism. E15 is the second-tier Capability that justifies split. E16/E17 are explicitly not new Capabilities.*

---

## 6. Translation Evidence (≥2 ecosystems per candidate — V-C gate)

| Canonical | Claude Code / Claude Agent SDK | OpenAI Codex / OpenAI Agents SDK | Cursor / Windsurf / Copilot (IDE) | LangChain/LangGraph | Letta/LlamaIndex/Haystack/Vector DB | Confidence |
|-----------|-------------------------------|----------------------------------|-----------------------------------|---------------------|--------------------------------------|------------|
| **E12 Context** | `compact_boundary`, `autoCompactEnabled`, `prepareCompaction/applyCompaction`, `CLAUDE.md` re-injected via `settingSources`, `ContextManager P0-P10 priority + smart_truncate/LLM summarize`, `maybeCompact` 60/75/90% | `Conversation context (ephemeral)` vs auto-summarization+file offload pattern | Cursor `@codebase` local embeddings + `@files` manual; Windsurf Cascade full-repo auto embeddings; Copilot repo indexing; Continue Chroma `@codebase` | Checkpointer per `thread_id` vs file offload pattern | Letta `core (RAM) / archival (disk) paging` + `tokPerChar/msgChars`; trustclaw 3-layer pruning/flush/compact; LCM dual-store immutable/active | High |
| **E13 Memory** | `CLAUDE.md` scratchpad + `memory_snapshot.json` | `Sessions (persistent working context)` across handoffs | Cross-session personalization via rules/ideally memory layer | `Checkpointer (thread_id) + BaseStore (user_id) + LangMem (semantic/episodic/procedural, self-rewrite)`, semantic search in `PostgresStore` | Letta `core/recall/archival + archival_memory_insert`; Zep/Graphiti bi-temporal KG `validity windows, as-of`; Mem0 vector+extraction; Anthrop 7 Layers; NirDiamant 30 notebooks | High |
| **E14 Retrieval** | Tool-output offload (indivisible block → backend store + preview+reference left in context) | Triage pattern retrieval not emphasized (handoff scope) | Cursor `@codebase` retrieval, Windsurf auto retrieval, SocratiCode independent index | `VectorStoreQuery sparse/hybrid top_k`, Haystack RRF fusion | LlamaIndex `NodeWithScore RetrieverQueryEngine`, Haystack Qdrant/Weaviate/Pinecone pipeline, Pinecone/Qdrant/Weaviate/Chroma hybrid | High |
| **E15 Knowledge** | `claude-memory-compiler` (hooks→SDK extraction→LLM compile → 34 spec-docs cold-memory on demand) | — | `codebase-memory-mcp` AST KG (shared) | Docs RAG ingestion (LlamaIndex/Haystack ETL) | `Facts as First Class Objects` hash-addressed tuples 252× cheaper | Med-High |
| **E16 Prompt** | `Skills slash prompts`, `AGENTS.md` operating model, `Domain rules (80)` section | `Agent instructions` (system prompt per handoff) | `Rules for AI / .cursorrules / .windsurfrules / .github/copilot-instructions.md` + hierarchy L0-L2 | Prompt templates | Harness `50/30/20 + progressive disclosure + trim loop` | High |
| **E17 Budget** | `ContextBudgeter.MODEL_LIMITS 30K/50K/100K`, `complexity-gate.sh`, `doc-bloat-gate.sh`, `ctx N% badge` | `HARNESS_MAX_TOTAL_TOKENS → COST_BUDGET` proposal | `context-budget SKILL inventory ~500tok/tool` | KL regularization `effective_score = raw - λ·complexityCost·100` | Prompt budgeting `50/30/20` + Kairn env compiler | High |

*No candidate accepted with <2 ecosystems. E15 and E17 meet via harness-foundry + Kairn + Forge triangulation.*

---

## 7. Tensions, Interactions & Lifecycle Wiring (not forced DAG)

- **E12 vs E1 (subagent, Batch 1) vs SC-05 Pareto:** Fan-out via `E1 Delegated Subagent` reduces per-agent context (good for E12) but multiplies total CPSR — requires Pareto `pass@1 vs $/task` gate. `Subagents use their own isolated context windows, only relevant summary back to orchestrator rather than full context` — this is *Context Management by delegation*.
- **E12 vs E6 (Isolated Workspace via git worktree) vs SC-06/SC-10:** Worktree isolation improves DRR/IDFR but does not solve context rot — complementary isolation planes (filesystem vs window).
- **E13 vs SC-09 CSP:** Long-task probe 40k synthetic + 5-QA `memory-probe` explicitly measures whether key intents (goal, constraints, decisions) survive compaction — E12 compaction strategy predicts E13 survival. Goal embedding cosine >0.90 threshold is shared SC.
- **E13 vs SC-07 SSHC:** Memory poisoning is 0-tolerance `0 leaks/100 runs, ≥90% injection blocked` — E13 persistence without E18 hardening → SC-07 FAIL. Trust-partition + sanitization must gate `commit_memory`/`recall_memory`.
- **E17 vs E14/E9:** Parallel fan-out (E9, Batch 1) and broad retrieval (`similarity_top_k=10`) both inflate cost — budget governance caps fan-out degree and `top_k` adaptively.
- **E15 vs SC-02 TSR/SC-08 AHG:** Knowledge curation predicts `citation gate` pass rate for C4 research and typecheck gate for C1 — but over-curation (e.g., 34 spec-docs loaded eagerly) harms SC-01 `P50 <90s` and SC-05 — cost of retrieval vs completeness Pareto.
- **E12/E13 vs E8 HITL (Batch 1):** HITL approval gates (LangGraph HITL core primitive `pause at approval`, ADK `tool confirmation`, AG2 `UserProxyAgent`, Claude `PermissionRequest hook PreToolUse exit 2`) are trust gates for memory writes — unapproved `archival_memory_insert` is injection vector.
- **E10 Hooks (Batch 1) vs E12/E17 vs Batch 4 trust boundary:** Hook interception (PreToolUse/PostToolUse/SubagentStop) must not bypass sandbox — interception is how `ContextBudgeter` and budget gates enforce. Deferred to P1-30 but touchpoint now.

---

## 8. Overlaps & De-duplication vs Batch 1

| Flag | Detail | Action |
|------|--------|--------|
| **Keep split** | E12 Context Management vs Batch 1 `E10 Lifecycle Interception / Hooks` | E10 is capability for interception points; E12 consumes hooks as Mechanism (compaction interceptor) — not duplicate. Keep split, document coupling via SC-07/SC-03. |
| **Merge** | `Background queued execution` 4 synonyms (background agents/tasks/async jobs/queued) | Already merged in Batch 1 E5 (4→1) — do not re-introduce `background compaction` as new capability; it's E12 mechanism (`emergencyTrim`, `daemon/worker`). |
| **Demote** | `git worktree`, `.claude/agents/*.md`, `hooks 25 events`, `max_concurrent_threads` | Already demoted to Mechanisms M1/M3/M6 — do not re-promote `vector DB index` or `CLAUDE.md file` to Capability; Capability is Isolated Workspace / Context / Memory. Vector DBs are Tools. |
| **Defer** | `MCP` and `Skills` individual pack | MCP → Batch 3; Skills category → Batch 3 Capability, individual skill (context-budget) → Resource. Prompt packs catalogued here as Mechanism E16 only. |
| **Cross-ref** | `Checkpoint/rewind` (Batch 5) vs `Memory persistence` (Batch 2) | Checkpoint is undo/temporal recovery Mechanism; Memory is continuity/governance Capability — keep split (E11 vs E13 boundary from Batch 1 notes). |
| **Portability risk** | `.claude vs .codex vs .github/agents vs .gemini vs .windsurf` fragmentation (M3) | Anti-portable; spine `AGENTS.md` + adapter mitigation noted in Batch 1 — applies equally to `CLAUDE.md` vs `.cursorrules` vs `.windsurfrules` vs `.github/copilot-instructions.md` in this batch. |

---

## 9. Open Questions & Verification Gaps (for P1-14..16 / P2)

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | E15 cold-memory 34 spec-docs vs hot-memory constitution scale guidance — empirically does on-demand spec loading preserve SC-09 CSP ≥85%? Needs LongMemEval vs LoCoMo bench vs `claude-memory-compiler` A/B. | P2 Group B deep research | Before RANKINGS |
| 2 | Vector DB decision at 15M SKU scale — Qdrant vs Weaviate vs Pinecone Pareto (TSR vs CPSR + p95) for C3/C4 archetypes with hybrid filtering — rank-sensitive, not settled by literature p95 23 vs 34 ms alone. | P3 Tools `<retrieval>.md` | Before TOOL_SELECTION_INDEX |
| 3 | LCM lossless dual-store (`Immutable Store verbatim + Active Context retrievable view`) claim of zero information loss — verify vs LLM-summary lossy compaction in same cost envelope; does it actually avoid 95% degradation? | P1-15 abstraction pass | Before MASTER_TAXONOMY |
| 4 | Memory poisoning defense maturity — `Agent Memory Guard` vs Letta `Archival` vs Agno validation layer vs GLOBAL commit_memory sanitization — which is harness-level (Batch 4) vs store-level? No adopted standard yet. | P1-30 + Batch 4 P1-27..30 | Batch 4 |
| 5 | Budget tiers 30K/50K/100K vs attention budget illusion — threshold at which 200K window degrades reasoning is model-dependent, not fixed at 60% intervention heuristic; needs model-card calibration. | V-D rubric wiring + P2 | Before P2-02 template |

---

## 10. Sources

Primary (≥2 independent per claim required — representative):

- Claude Agent SDK context management & compaction — SDK docs: automatic compaction when limit approaches, built on `/compact`, async context manager, `autoCompactEnabled`, `compact_boundary` stream event, ~80-90% threshold, intervene at 60%, `CLAUDE.md` re-injected via `settingSources`; subagents isolated windows.
- OpenAI Agents SDK handoff & memory — `function handoff`, `Agent constructor handoffs option`, single-run handoff, input guardrails first agent / output last agent, Sessions vs LangGraph Store+filesystem, Triage pattern, Swarm extension with tracing/validation; session-scoped memory carried across handoffs.
- LangChain/LangGraph memory taxonomy — `ConversationBufferMemory deprecated v0.3.1 removal v1.0.0`, `Checkpointer (MemorySaver/SqliteSaver/PostgresSaver/MongoDBSaver/DynamoDBSaver/langgraph-oracledb) thread_id` vs `BaseStore (PostgresStore/InMemoryStore semantic search, MongoDBStore, DynamoDBStore) user_id`, `BaseStore semantic search meaning-not-exact`, LangMem SDK `semantic/episodic/procedural + create_manage_memory_tool + editable system prompt`, `MongoDB checkpoints/ checkpoint_writes` collections.
- LlamaIndex RAG architecture — data framework, nodes (text+embedding+metadata), `VectorStoreQuery top_k default/sparse/hybrid`, `VectorDBRetriever → RetrieverQueryEngine`, Auto-Retrieval, Sentence Transformers + Postgres/Chroma/Qdrant/Weaviate/MongoDB/Pinecone/Milvus/FAISS, ingestion pipeline PyMuPDF→SentenceSplitter 1024→TextNode→HuggingFace BAAI/bge-small-en→vector_store.add.
- Haystack 2.x pipeline architecture — pipeline orchestration, Pinecone/Qdrant/Weaviate/Elasticsearch/FAISS/Db2 VECTOR, `VECTOR_DISTANCE`, RRF fusion, modular `Embedders/Generators` swappable, agentic multi-vector-store with Neo4j, Weaviate BM25+dense alpha, GraphQL multi-tenancy.
- Vector DB benchmark 2024-25 — Qdrant (Rust, quantization, payload filters, 5 ms P50/20 ms P99, 100M+), Weaviate (Go, BM25+dense alpha, GraphQL, multi-tenancy), Pinecone (managed cloud-only, serverless pay-per-query, ~50 ms P99, vendor lock-in), Chroma (Python embedded, <5M practical, Apache-2.0), FAISS baseline; latency table insert 1M vectors, query P50/P99; 15M SKU e-commerce case Pinecone 23 ms vs Weaviate 34 ms.
- Cursor / Windsurf / Copilot / Continue.dev context injection — Cursor `@codebase/@files/@docs/@file/@git/@folder`, local embeddings `@codebase` 200k+ window RAG, `.cursorrules`/`.cursor/rules/*.mdc` globs; Windsurf Cascade full-repo proprietary embeddings auto-selection, `.windsurfrules`→`.windsurf/rules/rules.md`, auto-scan repo→pick files→exec tests; Copilot `.github/copilot-instructions.md` prepended + recent repo indexing; Continue Chroma `@codebase`; hierarchical L0-L2 map + Graphify graph; SocratiCode independent index; portability drop same markdown across envs.
- Letta/MemGPT agentic memory — Berkeley `Towards LLMs as Operating Systems` → Letta successor, OS-inspired `core (RAM) / recall (cache) / archival (disk) paging` via `core_memory_replace/archival_memory_insert`, DeepLearning.AI + Letta course, CoALA 4-tier Working/Episodic/Semantic/Procedural (Tulving split), short-term inside window vs long-term outside, ~23k stars Apache-2.0, Agent Dev Environment.
- Mem0 vs Zep/Graphiti vs Letta comparison — Mem0 vector+fact extraction lightweight SDK (50k+), Zep/Graphiti temporal/bi-temporal KG validity windows as-of/invalidation (FalkorDB MCP, 94.8% vs 93.4%, LongMemEval), 4-tier table, super memory/Memori/turbopuffer evaluations, awesome-agentic-memory taxonomy, MemoryPilot hybrid, LangMem procedural distinction, NirDiamant 30 notebooks, rivercrab mem-bench (Mem0/Graphiti/Letta LongMemEval vs HaluMem).
- Context window compaction mechanics — xopcai/xopc `src/agent/memory/compaction.ts store prepareCompaction/applyCompaction emergencyTrim`, windmist `tiktoken-go ReferenceInjector @file/@http`, djinnbot `/context /compact /status` 85% prune→compact, Zap `maybe_summarize_dropped_turns 8-turn window dropped_summary`, trustclaw 3-layer pruning/flush/summarization, kcode `compactMultiStrategy 60% micro/75% LLM/90% emergency`, wsx `threshold-gated maybeCompact`, LCM dual-state Immutable+Active zero-loss (arXiv 2605.04050).
- Context/memory/retrieval/knowledge distinction — `storage is where info sits, retrieval how found, memory what shapes behavior, harness decides window` + `bookkeeping` + `chat history ≠ memory (distilled structured layer)`, `Context Window ≠ Memory` table (temporary vs persistent, flat equality vs hierarchical priority, proximity vs intent recall, high vs low scaling cost), `RAG stateless no time/sequence vs Memory stateful tracks order/timing/evolution + user-modeled adaptive`, `RAG is access strategy not knowledge`, `PKM individual thinking vs Wiki shared social-contract vs RAG machine vs Memory adaptive multi-session`, `context windows keep consistency within session, memory intelligence across sessions`, harness orchestrates write path (extract/dedup/metadata) + read path (relevant→prompt compact).
- Unified agent memory survey `Memory in Age of AI Agents (arXiv 2512.13564)` — Forms (token-level discrete / parametric weights / latent hidden), Functions (factual/experiential/working), Dynamics (formation/evolution/retrieval), distinguishes Agent Memory from RAG/Context Engineering.
- Knowledge management harness documentation — awesome-harness-engineering (tools/patterns/evals/memory/MCP/permissions/observability/orchestration), `codebase-memory-mcp tree-sitter AST→persistent KG`, `claude-memory-compiler hooks→SDK extraction→LLM compile → cross-referenced articles`, `Facts as First Class Objects hash-addressed tuples 100% accuracy 252× cheaper`, `cold-memory 34 spec-docs on demand vs hot-memory constitution`.
- Security — context/memory poisoning OWASP ASI06 persistent indirect injection, `tool_result → STATE_MODIFICATION`, GLOBAL `commit_memory→recall_memory no sanitization cross-workspace`, ElizaOS crypto hijack shared memory, Letta archival single-entry bleed, eTAMP raw-trajectory reuse cross-site bypass, GPT-5.2 vulnerability, Agno no validation layer note (June 2026 arXiv Memory Poisoning).
- Prompt vs Context vs Harness taxonomy — `Prompt ⊂ Context ⊂ Harness ⊂ Loop`, computing stack `model=CPU, context=RAM, harness=OS`, Karpathy 2025 `delicate art filling window just right for next step`, Lütke June 2025 `real skill is providing all context task plausibly solvable`, Hashimoto Feb 2026 `Agent = Model + Harness`, Lopopolo `Agents aren't hard; Harness is hard`, Fowler/Lopopolo (2026), Martín Fowler coverage, evolution timeline Prompt 2022-24 → Context 2025 → Harness 2026+; 8-dim comparison table (controls, abstraction message/session/system, era, failure mode, tools).
- Prompt architecture / complexity budget — Harness 11-file P0-P10 priority chain with token budget + multitier caching + 3-layer distillation, re-rank ranking question(100)>harness_feedback(96)>judge_guidance(94)>manifest(90)>domain_rules(80)>prior_steps(60), over-budget compressed smart_truncate/LLM summarize, 3 budget tiers 30K (default) /50K large/100K 1Mctx + P0-P2 never truncated + P7-P8 head-trim, Koch prompt budgeting `50/30/20 + trim loop compress→coverage check, progress disclosure plan→retrieval→execution→verification, thresholds 300-800 lookup / 800-2000 review`, `--token-budget off → ctx-gate drops least relevant`, `System prompt tokens paid every request`, harness rationale `push complexity from LLM to infrastructure`.
- Complexity budget & anti-bloat governance — 75-line pre-inline bloat fix `Read at runtime cheaper than budget bloat every spawn`, Kairn `effective_score = raw_score - λ·complexityCost·100 cost lines/files/sections/char diff λ0.1`, Forge `CLAUDE.md complexity budget LOC senior would write`, harness-builder `complexity-gate.sh Python≤8 Go≤10 TS≤15 + doc-bloat-gate.sh + budget gate reconcile loop`, `cost-optimized Skills on demand not bloating every prompt`, harness foundry `HARNESS_MAX_TOTAL_TOKENS → StopReason.COST_BUDGET ContextManager per-call but no cumulative cap`, `context-budget SKILL inventory agents/skills/rules/MCP ~500tok → Always/Sometimes/Rarely`, JIT fleet budget throttling.

**Phase continuity:**
- `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6 constraints matrix (cost High C2/C4/C5, latency P95 C1/C3/TTFT C4, security High C1/C3/C4/C5, reliability High C2/C3/C5/C6) and SC-01..10 with anti-averaging p10 bottleneck, leading/lagging wiring (§4.5 `wiring.json`).
- `phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md` E1-E11, M1-M10, S1-S3, F1-F7, T1-T8; hygiene note Tool×Mechanism inventory trap; kept boundary E10/E11 vs Batch 5 checkpoint/rewind.
- `plan.md §2 Batch 2` P1-09..16 protocol — this report satisfies P1-09/11/13; translation check (P1-14) and re-tag (P1-15) remain for V-C/V-D.

---

**Return value note:** This is the verbatim Broad Mapper deep research bundle for **P1-09 Sweep + P1-11 Distinction + P1-13 Architecture Placement**. Primary taxonomy contribution: **E12 foundational + E13 foundational + E14 Mechanism + E15 important KB Capability + E16 Mechanism under E12 + E17 cross-cutting governance (Batch 5 owner)**. No Batch 1 duplication; full SC wiring per archetype variance ready for P2 rubric.

**Relevant file paths (absolute):**
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md`
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md`
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\batch-1\BATCH-1_EXECUTION_AND_AGENCY.md`

