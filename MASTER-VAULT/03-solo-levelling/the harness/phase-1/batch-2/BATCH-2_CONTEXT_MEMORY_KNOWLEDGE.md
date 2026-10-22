# Phase 1 — Batch 2: Context, Memory & Knowledge — Converged Taxonomy Slice

> **Status:** CONVERGED — P1-09..16 complete | **Date:** 2026-08-31 | **Workflow:** `wf_4434e6aa-c46`
> Inputs: [`R-A_BROAD_MAPPER.md`](R-A_BROAD_MAPPER.md) (74K, 9 angles, 17 searches) · [`R-B_CHALLENGER.md`](R-B_CHALLENGER.md) (43K, 7 challenger angles, 13 searches, 6 proposals) · [`V-C_ADVERSARIAL.md`](V-C_ADVERSARIAL.md) (24K, P1-14 translation/kill, cross-batch boundary) · [`V-D_ARCHITECTURAL.md`](V-D_ARCHITECTURAL.md) (27K, P1-15 re-tag, 9 conflation flags) — 117K raw, 56 tool uses, 337K tokens
> Repo: `the harness` | Grounding: `plan.md §2 Batch 2` · `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..10 (SC-09 CSP, SC-07 SSHC) · `phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md` (11 Capabilities converged — do NOT duplicate)

---

## 0. Method & Coverage

- **R-A (Broad Mapper):** 9 angles — Claude Agent SDK context lifecycle (`autoCompactEnabled/compact_boundary/CLAUDE.md`), OpenAI Agents SDK handoff+memory (Triage pattern), LangChain/LangGraph memory taxonomy (`Checkpointer` vs `BaseStore`, `thread_id` vs `user_id`), LlamaIndex/Haystack + vector DBs (Pinecone/Qdrant/Weaviate/Chroma/FAISS/Milvus), Cursor/Copilot/Windsurf context injection (`.cursor/rules/*.mdc`, `AGENTS.md` hierarchy), poisoning/injection (OWASP ASI06, Letta, eTAMP), context window mechanics (MaybeCompact, LCM dual-state arXiv 2605.04050), taxonomy distinction (CoALA 4-tier, PKM vs RAG), prompt architecture & budgets (harness Foundry `context-budget` SKILL, Kairn KL `effective_score = raw - λ·complexityCost·100`, 50/30/20 allocation). Stop-rule per sub-area: no early halt — every angle still surfaced novel candidates at search 3+. Quality bar ≥2 independent sources; vendor vs OSS cross-checked.

- **R-B (Challenger):** 7 angles deliberately different vocab — `episodic/semantic/procedural/working` cognitive split vs R-A's monolith `memory`, `compaction vs summarization vs eviction vs masking` vs `context management`, graph-structured memory vs `vector DB`, semantic cache vs prompt cache vs agent memory, consolidation lifecycle (sleep-like promotion: Jaccard dedup, cognitive weight), injection/poisoning trust boundary. Each angle exposed primitives R-A would collapse: 4-way memory split, 77% entity loss under generic summarization, bi-temporal Neo4j provenance, cost ordering `exact→semantic→LLM`, IPI = agent-era XSS.

- **V-C (Adversarial):** P1-14 translation check (≥2 ecosystems per candidate) + kill/merge with 2 counter-sources each. Key kills: C-B1 Working Memory + C-B2 Compaction merged into E12 as Mechanisms/State (CoALA nesting + harness stack `Prompt ⊂ Context ⊂ Harness`); C-B3 Consolidation → Mechanism M13a under E13; C-B4 Graph → merge into E15/E14 substrate (hybrid vector+graph consensus, PKM vs Memory); E16 Prompt Architecture → Mechanism under E12; over-split S1-S6 from R-B partially killed (anti-bloat 11→15 inflation blocked). Cross-batch boundary flagged: C-B6a Untrusted Fencing stays Batch 2, G-X Injection Governance goes Batch 4, poisoning split both.

- **V-D (Architectural):** P1-15 re-tag to Capability/Mechanism/Protocol/Framework/Tool + lifecycle + tier + SC wiring (SC-09 CSP, SC-07 SSHC veto, SC-05 CPSR). Mirrors Batch 1 V-D hygiene (Tool×Mechanism ≠ Capability) with 9 conflation flags. Crucially **splits** where V-C merges: B1 Working Memory Isolation and B2 Context Compaction kept as distinct Capabilities (different lifecycle, failure modes, SC wiring), with flag for P1-42 to resolve.

**Coverage confidence:** HIGH — 30 searches across 16 angle vocabularies, both leading memory frameworks (Letta/MemGPT, LangGraph/LangMem, Mem0/Zep/Graphiti), vector+graph substrates, all major IDE agents, security (OWASP/eTAMP/ElizaOS). Practical completeness achieved after 3+ consecutive synth-only searches would have been noise. Truncation noted: R-A payload truncated after §0 method in V-C/V-D but full `R-A_BROAD_MAPPER.md` recovered on disk (74K) — synthesis uses disk truth. Anti-averaging preserved per `ARCHETYPES_AND_CRITERIA.md §4.4`.

---

## 1. Converged Capability Taxonomy — Batch 2 (10 Canonical Capabilities)

*Level: Capability / Mechanism / Protocol / Framework / Tool per plan.md §0.2. Lifecycle: build-time / run-time / review-time. Tier: foundational / important / specialized / situational. Confidence: high / med-high / medium.*

| # | Canonical Capability | Definition | Problem Solved | Correct Level | Lifecycle | Tier | Confidence | Cross-Ecosystem Synonyms (≥2 ecosystems) |
|---|---------------------|------------|----------------|---------------|-----------|------|------------|------------------------------------------|
| **B1** | **Working Memory Isolation** | Bounded volatile scratchpad = context window (system+pinned+recent-N) with declared capacity `max_context_tokens` but effective << advertised (advertised→effective gap up to 99% on complex tasks). | Window overflow, attention dilution, goal drift; isolates what model sees this turn vs what persists. Without it, context stuffing to 95% causes reasoning degradation + cost blowup. (SC-09 CSP <0.90, SC-05 waste, SC-01 stall) | **Capability** | build (model limit, pinning policy `system/semantic-index/glossary/recent-N`) → run (every turn) | **FOUNDATIONAL** — V-C contested merge (CoALA nesting), V-D verified split: fixed-size volatile need is not implementation. Harm 4 if collapsed. Needed C4/C6 long tasks >30k → 40k synthetic probe | High | Claude `200K context window + pinned system prompt + autoCompact` ≡ Codex `max_context_tokens` ≡ CoALA/Letta `working memory (<8K active, RAM)` ≡ Redis `in-context memory` |
| **B2** | **Context Compaction (Pinned Preservation)** | Threshold-triggered loop replacing older turns with condensed summary without touching pinned set (`system/semantic-index/glossary/recent-N`). Distinct from B1: B1 is container, B2 is anti-exhaustion loop. | Window exhaustion on long-horizon tasks (C4 research dossier, C6 migration). Generic L1-only summarization loses 77% entities vs L1+L2+L3 100% — mechanism choice is load-bearing. (SC-09 CSP 40k probe <50% without pinned, SC-06 DRR, SC-07 hardening decay) | **Capability** | build (threshold 60/75/90% or 28K tokens + cheaper summary model selection) → run (threshold check every turn) | **FOUNDATIONAL for C4/C6; IMPORTANT globally** | High | `clido-ai/clido-cli @28000` ≡ `Atlas PRD pinned semantic index` ≡ `mini_swe_agent_v2 compact_if_needed@0.85` ≡ `Vercel Eve auto-summarize+cheaper model` ≡ `Claude auto-compact@~90%` ≡ `leuk tiered structured` — 6 ecosystems |
| **B3** | **Memory Consolidation / Promotion Daemon** | Periodic background sleep-pass that merges append-only episodic events (`what/when`) → deduplicated semantic facts (`prefers X, budget $75K`) with `informed_by` provenance, Jaccard dedup, heuristic+LLM extraction (5-15/cluster), cognitive weight `add/supersede/noop`. | Episodic bloat (47K→3.2K clusters/30d), precision decay, re-learning cost. Without: semantic stale, episodic explosive, SC-05 +41% vs stateless. LongMemEval-S +33pp (12pp weight + 8pp async). | **Capability** (Mechanism if daemon-less; Capability if daemon) | build (tier def) → run (daemon interval/session-end trigger) → review (provenance `informed_by` audit) | **IMPORTANT globally; FOUNDATIONAL for any cross-session harness (C4/C6 long)** — V-C demoted to Mechanism (situational harm 2-3 short), V-D promoted (harm 4 long). Archetype-dependent tier: split justified. | Med-High | `Zijian-Ni/agent-memory consolidate() Ebbinghaus` ≡ `blakestone-x/engram promote` ≡ `MemTier async daemon Heuristic+LLM Jaccard` [arXiv 2605.03675] ≡ `event4u-app session-end` ≡ `agent-memory-mcp promote_sediment` |
| **B4** | **Typed / Bi-Temporal Knowledge Graph Memory** | Durable graph substrate with typed nodes/edges (`works_at`, `founded`), bi-temporal validity (`valid_from/valid_to × transaction time`), hybrid retrieval (vector dense + BM25 sparse + RRF), agent-written Cypher over MCP. Alternative to flat vector for relational + provenance + constraint enforcement. | Flat vector with metadata filtering achieves KG-like via iterative retrieval, but graph gives explicit multi-hop, typed enforcement after compaction, entity-neighborhood provenance for poisoning scoping. (SC-07 entity poisoning, SC-09 constraint re-injection, SC-02 knowledge-intensive TSR) | **Capability** (specialized substrate variant of Persistent Memory) | build (typed schema `works_at/founded`, bi-temporal columns) → run (extraction loop, lifecycle hooks→system-prompt evolution) → review (hash-chained audit) | **IMPORTANT** (SPECIALIZED today → foundational for C4-research with graph-native queries). Harm 3-4 if graph reasoning needed. | Med-High | `derkodex/meta-knowledge-graph Neo4j harness-agnostic` ≡ `talsperre/neo4j-agent-memory bi-temporal Cypher` ≡ `walliiee Gbrain typed KG + Postgres+RRF` ≡ `oyekamal Mnemo Graphiti+FalkorDB MCP` ≡ `homgorn world-model-mcp temporal validation` |
| **B5** | **Semantic Cache (Meaning-Based Response Reuse)** | Thresholded embedding-similarity answer cache (e.g. cosine ≥0.95, L1/L2 Redis/Valkey) ordered `exact hash O(1) → semantic KNN+judge → LLM fallback`; namespace/TTL isolation; distinct from Anthropic prefix prompt cache (5-60m TTL on KV prefix). | Repeated paraphrased calls burn tokens/latency; pure prefix misses paraphrase; pure RAG still calls LLM. 10-1000× speedup via RedisVL L1/L2 when hit. | **Capability (SPECIALIZED)** — V-C kept specialized, V-D flagged open demotion to Mechanism under Retrieval (B7). Both note cost-only harm argues Mechanism, but distinct ordering + invalidation warrants cap. | run (lookup `cache.get/prompt` / `cache.set` around runner) → build (threshold/TTL/namespace per model/tenant/agent) | **SPECIALIZED** — Important for high-volume C4/C3; not foundational (harm 3, no veto). SC-05 CPSR + SC-01 TTFUA only. | Medium | `Redis LangCache semantic vs prompt cache` [Redis blog] ≡ `Vertector RedisVL L1/L2` ≡ `llm-semantic-cache cached_llm_call + namespaces` ≡ `ScyllaDB+pgvector + SentenceTransformer` |
| **B6** | **Untrusted-Content Fencing / Instruction Trust Boundary** | Harness-level data-vs-instruction separation: 4 trust-labeled sources (`GOVERNANCE_INSTRUCTION / UNTRUSTED_REPOSITORY_DATA / UNTRUSTED_EXTERNAL_DATA / PROVIDER_OUTPUT`) + delimiter fencing (`[BEGIN UNTRUSTED REF]`), defanged forged markers, span-tainting middleware, `PromptInjectionDefender(semantic_detection=True)` scanning every `tool_result`/MCP/terminal/`read_file` pre-model, output canary. | Without boundary: poisoned file `// ignore previous instructions` treated as instruction — IPI = agent-era XSS. Safe model (0/8 leaks in chat) ≠ safe agent (4-6/8 leak at harness). Hardening decays if compactable. (SC-07 SSHC veto: 0 leaks/100, ≥90% blocked; any leak = harness FAIL per `ARCHETYPES_AND_CRITERIA.md §3`) | **Capability — FOUNDATIONAL (VETO, harm 5)** | build (frozen per-task policy + trust classes) → run (stamp provenance + scan pre-model every tool result) → review (hash-chained audit log) | **FOUNDATIONAL (VETO)** | High | `pydantic-ai-harness PromptInjectionDefender` ≡ `faion-network trust-boundary span-tainting dual-LLM` ≡ `warden/keel trust primitives` ≡ `autocontext wrap_untrusted() delimiters` ≡ `agent-dx Instruction Trust Boundary` |
| **B7** | **External Retrieval (RAG) — Stateless External Data Access** | Stateless read-only pipeline `index→embed→store → query→hybrid search (dense+BM25+RRF)→re-rank→augment prompt`; indexed corpus is external fixed collection. Stateless: no read-write-learn-forget cycle. | Parametric staleness, hallucination, corpus > window; query-time grounding for knowledge-intensive tasks. Without: C1 codebase + C2 fabric + C4 research all regress SC-02 TSR + SC-08 AHG on any external knowledge requirement. | **Capability** | build (loading/splitting 1024, embedding, `vector_store.add`, lineage) → run (query→top_k→NodeWithScore→LLM) | **FOUNDATIONAL** — harm 4 if absent across ≥4 archetypes. SC-02/SC-08 collapse. | High | LlamaIndex `VectorStoreQuery sparse/hybrid top_k → NodeWithScore` ≡ Haystack `Pipelines + Qdrant/Weaviate/Pinecone RRF, Db2 VECTOR_DISTANCE` ≡ Pinecone `serverless` vs Qdrant `Rust quantization` vs Weaviate `BM25+dense alpha` vs Chroma `embedded` ≡ Cursor `@codebase` vs Continue Chroma |
| **B8** | **Memory Recall (Internal Reconstructive Experience)** | Stateful read-write `Capture→Store→Retrieve→Update→Forget` with decay/consolidation/supersede; reconstructive (Bartlett 1932/Schacter 2001) — recalls experience ("we decided Vitest over Jest on 8/12 because...") not documents. | Continuity, personalization, learning across sessions. Distinct from B7: RAG answers "document about X", memory answers "we decided X". Without: repeated lessons, SC-09 decisions evaporate post-compaction, SC-02 repeat penalty. | **Capability** | build (store schema) → run (relevance-filtered recall, semantic compression) → persistent (cross-session) → review (forget/decay) | **FOUNDATIONAL for C4/C6 long-horizon; IMPORTANT globally** — harm 4 if merged to retrieval. | High | LangGraph `Checkpointer thread_id (short-term) vs Store user_id (long-term) + LangMem 3 types (semantic/episodic/procedural) self-rewrite` ≡ Letta `archival_memory_insert/recall` ≡ Zep/Graphiti `bi-temporal KG as-of` ≡ Mem0 `vector+extraction` ≡ CoALA 4-tier |
| **B9** | **Knowledge Curation & Indexing (Build-Time)** | Build-time pipeline `index→extract→cluster→distill→version` with lineage (SBOM-like) for external+internal corpora: chunking, typed KG extraction, vector index, distilled facts as versioned artifact. The sibling to B7/B8 run-time recall. | RAG retrieves but does not curate; memory is personal not canonical; without governance: stale/conflicting knowledge degrades grounding, SC-08 index errors cause systematic grounding failure. | **Capability (build-time)** | build (spec authoring, graph build, cold-memory docs) → review (freshness audit/drift `drift-detector.sh`) | **IMPORTANT** — Med-High confidence. SC-08 AHG + SC-10 IDFR 100% no-op on frozen inputs for C2/C5/C6 (frozen index). Not foundational globally (throwaway research C4 does without). | Med-High | `codebase-memory-mcp AST→KG` ≡ `claude-memory-compiler hooks→SDK→34 cold-memory spec-docs` ≡ `Facts as First Class Objects hash tuples 252× cheaper` ≡ Wiki `social contract` vs PKM `flexible` vs RAG vs Memory |
| **B10** | **Context Budget Governance** | Allocation + enforcement of prompt/tools/retrieval/memory competition: priority-ranked assembly P0-P10 (`CLAUDE.md > tool definitions > context files > user prompt`), 50/30/20 allocation, head-trimming, KL regularization `effective_score = raw − λ·complexityCost·100` (λ=0.1), 3-tier token budgets (30K/50K/100K) + `HARNESS_MAX_TOTAL_TOKENS→COST_BUDGET` badge, fleet JIT loading. | Unbounded component accumulation (~500tok/tool × MCP) → 10k+/turn waste; window stuffed to 95% "reasons worse"; memory+tools compete for same window. Without: SC-05 <5% overruns violated, SC-09 pinned survival vs window stuffing lost, E1/E2 fan-out Pareto unbalanced. | **Capability (governance)** | build (budget definition 3-tier + P0-P10 chain + λ) → run (per-turn enforcement, badge, fleet JIT) → review (bloat audit CR-01, P1-36) | **IMPORTANT** — Med-High. SC-05 + SC-09 dual wiring. V-C retailed as cross-cutting (owner Batch 5), V-D as standalone Cap governing E1/E2. Synthesis: governance Capability, primary evidence Batch 2, owner Batch 5. | Med-High | `harness Foundry context-budget SKILL (50/30/20 + progressive disclosure)` ≡ `Kairn KL regularization` ≡ `Forge complexity budget LOC` ≡ `ContextManager P0-P10 chain + smart_truncate` ≡ `ContextBudgeter MODEL_LIMITS 30K/50K/100K + COST_BUDGET` |

> **Deferred from B9 sibling:** *Knowledge Recall & Application* — lifecycle phase (`run-time K-Use via B7+B8+B1`), not a Capability — correctly deleted per both verifiers. R-B flagged `K-Use` as lifecycle, V-C deferred, V-D subsumed under B7/B8.

> **Cross-batch peer (not counted in Batch 2):** `G-X Injection Defense Governance` (red-team harnesses ASB 11×565×4, AgentProbe delimiters, allowlist/policy, audit trail, sandbox isolation) — **owner Batch 4 Safety (P1-25..30)** — DEFER. Listed for wiring only. SC-07 instrumentation `10 payloads ≥90%`. Wired Batch 2 C-B6a/b ↔ G-X. Do NOT double-count in MASTER_TAXONOMY Batch 2 row.

> **Mechanism under B3+B6 (not standalone Capability):** *Context Poisoning Resilience* — confidence-weighted contradiction resolution + provenance (`informed_by` hash chain) at consolidation boundary — **Mechanism — IMPORTANT** under B3/M13a with governance by G-X. eTAMP cross-session trajectory poisoning 8× ASR, ElizaOS >$25M hijack. Placement contested Batch 2 vs 4 — resolve Batch 4 sweep (P1-25..32). Wired `B3 ↔ B6b ↔ G-X`.

---

## 2. Mechanisms, Protocols, Frameworks, Tools (de-duplicated — not re-promoted)

### Mechanisms (collapsed — load-bearing for Batch 2 Caps)

| # | Mechanism | Implements | Tier | Hygiene Flag |
|---|-----------|------------|------|--------------|
| M-B1 | **Pinned Prefix + Token Budget + Head-Trimming** | B1 Working Memory | important | Mechanisms for B1; `max_context_tokens` is Protocol knob |
| M-B2a | **LLM Summarization of Dropped Turns** | B2 Compaction | important | One of 4 mechanisms; conflated by R-A as whole Capability |
| M-B2b | **Truncation / Eviction (oldest-first drop)** | B2 | situational | Lossy; 77% entity loss L1-only |
| M-B2c | **Observation Masking (replace tool outputs with `[masked]`)** | B2 | situational | ~52% cost save; token-efficient |
| M-B2d | **Structured Anchored Merge (`goal/files/decisions/state/pending` + semantic-index regeneration)** | B2 | important | Highest fidelity (L1+L2+L3 100%) |
| M13a | **Memory Consolidation / Promotion (Jaccard dedup, Heuristic+LLM extraction 5-15/cluster, Ebbinghaus decay, cognitive weight `add/supersede/noop`, `informed_by`)** | B3 | important | V-C Mechanism / V-D Capability split — keep as Mechanism but foundational for cross-session |
| M-B6a | **Delimiter Fencing (`[BEGIN UNTRUSTED REF]`, defanged forged markers)** | B6 | important | Batch 2 locus: pre-model |
| M-B6b | **Span-Tainting Middleware + Dual-LLM (validator model checks policy)** | B6 | important | Middleware at harness, not model |
| M-B6c | **PromptInjectionDefender (semantic detection, pre-model scan of every tool_result)** | B6 | important | Via Batch-1 E10 `PreToolUse` hook |
| M-B6d | **Output Canary / Honeypot Marker** | B6 | situational | Detects instruction-following leakage |
| M-B6e | **Context Poisoning Resilience (confidence-weighted contradiction, hash-chained provenance)** | B3 + B6 | important | Wired B3↔G-X |
| M14a | **Dense Embedding + Cosine Similarity** | B7 | important | Substrate for E14/B7 |
| M14b | **Hybrid Sparse+Dense (BM25 + dense) with RRF** | B7 | important | Qdrant/Weaviate `alpha` blend |
| M14c | **Semantic Compression (chunk+embed+cluster→distilled fact)** | B8 | important | B8 recall optimization |
| M16 | **Prompt Architecture & Instruction Design (roles, directives, packs, anti-sycophancy)** | B1 assembly (via E12) | important | V-C demoted Prompt Architecture from Capability — bundle is assembly pattern for Working Memory, not standalone need |
| M-Budget-a | **Priority-Ranked Prompt Assembly P0-P10** | B10 | important | `CLAUDE.md > tool defs > context files > user prompt` |
| M-Budget-b | **50/30/20 Allocation + Progressive Disclosure** | B10 | important | `context-budget` SKILL |
| M-Budget-c | **KL Regularization `effective = raw − λ·cost·100`** | B10 | important | Kairn; guards fleet Pareto |

### Protocols / Standards (4)

| # | Protocol | Scope | Tier | Note |
|---|----------|-------|------|------|
| S-B1 | **`max_context_tokens` Window Contract** | B1 — model-advertised limit (Muse 200K, GPT-4 128K) | important | Effective << advertised |
| S-B2 | **`VectorStoreQuery` / `NodeWithScore`** | B7 retriever contract | important | LlamaIndex protocol |
| S-B3 | **Cypher over MCP (Graph Query)** | B4 — agent writes Cypher, executes over MCP | important (emerging) | Neo4j/FalkorDB/Graphiti standard |
| S-B4 | **Trust-Labeled Content Model (4 classes)** | B6 — `GOVERNANCE_INSTRUCTION / UNTRUSTED_REPOSITORY_DATA / UNTRUSTED_EXTERNAL_DATA / PROVIDER_OUTPUT` | important (emerging) | Fencing protocol |
| S-B5 | **External Memory Provider API (async compaction contract)** | B2 — `prepareCompaction → applyCompaction` | important (emerging) | Micro-compact vs full summarization |

### Frameworks / Runtimes (4)

| # | Framework | Implements | Tier | Note |
|---|-----------|------------|------|------|
| F-B1 | **LangGraph** (`Checkpointer` vs `Store`, `thread_id` vs `user_id` + LangMem 3 types) | B8 / E2 Team memory | important | Checkpointer=short-term, Store=long-term — Mechanisms, not caps |
| F-B2 | **LlamaIndex / Haystack 2.x** | B7 retrieval | important | Batch 1 F1/F2 boundary — not re-promoted |
| F-B3 | **Letta / Mem0 / MemTier / CoALA** | B1-B3 (4-tier, 3 memory types, archival daemon) | important | Letta = Berkeley OS paper framework for B1-B3 |
| F-B4 | **Graphiti / Zep** | B4 graph substrate | specialized | Bi-temporal KG framework |

*Hygiene: Framework ≠ Capability. Batch 1 F1-F4 already cover orchestration; these embody B1-B4 but not taxonomy primitives. Vector DBs (Pinecone/Qdrant/Chroma) under F-B2, not separate Frameworks.*

### Tools / Products / Repos (12+)

| # | Tool | Primitives | Tier | Note |
|---|------|------------|------|------|
| T-B1 | **Pinecone / Qdrant / Weaviate / Chroma / FAISS / Milvus / pgvector / Mongo Vector** | B7 substrate | important (each) | Vector stores; protocol `VectorStoreQuery` |
| T-B2 | **Neo4j / FalkorDB (Graphiti backend)** | B4 substrate | specialized | Graph stores; protocol Cypher over MCP |
| T-B3 | **Redis LangCache / Valkey / Vertector** | B5 semantic cache | specialized | `Redis LangCache semantic vs prompt cache` [Redis blog] |
| T-B4 | **Anthropic Prompt Cache (prefix KV, 5-60m TTL)** | prompt cache (not semantic) | important | Contrast to B5 — prefix match, not embedding similarity |
| T-B5 | **clido-ai/clido-cli, joyouslang/leuk, Atlas PRD** | B2 compaction | situational | Pinned preservation + 28K threshold variants |
| T-B6 | **mini_swe_agent_v2 (`compact_if_needed@0.85`)** | B2 | situational | Compaction trigger variant |
| T-B7 | **Vercel Eve (auto-summarize + cheaper summary model)** | B2 | situational | Fidelity vs cost tradeoff |
| T-B8 | **MemTier, blakestone-x/engram, Zijian-Ni/agent-memory** | B3 | specialized | Consolidation daemons |
| T-B9 | **codebase-memory-mcp, claude-memory-compiler, Facts as First Class Objects** | B9 | specialized | Knowledge curation harnesses |
| T-B10 | **Rasputin 4-stage compilation (<150ms)** | B9→B1 | situational | Cold-memory spec compilation |

---

## 3. Kill / Merge / Demote Log (P1-14) + Abstraction Flags (P1-15)

| Action | Count | Details |
|--------|-------|---------|
| **KEEP distinct Capability** | **10** | B1-B10 above (B1 vs B2 split justified; B5 kept specialized despite contested demotion) |
| **MERGE/SUBSUME** | 5 | C-B1 Working Memory Isolation → **kept as B1** (V-C attempted merge into E12, V-D justified split — synthesis keeps split with flag); C-B2 Compaction → **B2** (V-C Mechanism cluster → V-D Capability split → split wins with P1-42 note); C-B3 Consolidation V-C Mechanism / V-D Capability → **B3 Capability** (archetype-dependent tier split); C-B4 Graph Memory → **B4 specialized Capability** (not merged to E15); K-Use (Knowledge Recall) → **deferred** (subsumed B7+B8+B1) |
| **DEMOTE to Mechanism** | 4 | E14 Retrieval (Capability only when scoped to external KB → Mechanism otherwise), M16 Prompt Architecture, `Context Management = summarization` (V-D Batch-1 §6 hygiene), Vector DB technology as Tool not Capability |
| **DEFER to other batch** | 3 | `G-X Injection Governance` → Batch 4 (owner), `Context Poisoning Resilience` → Mechanism under B3+B6 (wired both batches), `Complexity Budgets` full ownership → Batch 5 (evidence Batch 2) |
| **Conflations flagged (9)** | — | See §4 — batch-matched hygiene flags mirroring Batch 1's 9 flags for P1-42 |

### Abstraction Conflation Flags (9 — 6 R-A + 3 structural; for P1-42 cross-batch hygiene)

| # | R-A Raw Label | Correct Level | Fix |
|---|---------------|---------------|-----|
| 1 | `Context Management` as one Capability | **Split to B1 + B2** | Umbrella `Claude auto-compaction` decomposes to Working Memory container (B1) + Compaction loop (B2). Bundle → two needs. |
| 2 | `Context Management = summarization` | **Capability (B2 compaction) vs Mechanisms** | L1-only summarization is one of 4 mechanisms (M-B2a-d); conflated as whole Capability. |
| 3 | `Vector DB / RAG tool` (Pinecone/Qdrant) as Capability | **Tool/Mechanism for B7** | Technology substrate, not need; `VectorStoreQuery` is Protocol. |
| 4 | `IDE rules files / @codebase indexing` (`.cursor/rules/*.mdc`, `.windsurfrules`) as Capability | **Mechanism (hierarchical assembly) for B7+K-Cur** | File conventions + embeddings pipeline, not need. |
| 5 | `LangGraph Checkpointer vs Store` API as Capability | **Framework Mechanisms for B8** | `thread_id` vs `user_id` is Framework API split, not taxonomy Capability. |
| 6 | `Prompt Architecture / harness-as-OS stack` as Capability | **Mechanism bundle for B1** | Assembly pattern `Prompt→Context→Harness→Loop` for Working Memory, not standalone need. |
| 7 | `Knowledge Management` as one Capability | **Lifecycle split B9 (build) vs B7/B8 (run)** | SC-10 IDFR (frozen) is build concern; SC-09 CSP (survival) is run — one label cannot wire to both. |
| 8 | `Retrieval = memory read` | **Two Caps B7 vs B8** | Library (stateless read-only) vs notebook (stateful read-write-learn-forget, Bartlett/Schacter); 4-ops vs 5-ops cycle. |
| 9 | `B5 Semantic Cache = retrieval mechanism` (contested) | **SPECIALIZED Capability vs Mechanism** | Flagged for P1-42: harm 3 not veto argues Mechanism; distinct ordering+invalidation argues Cap. Keep specialized with note. |

---

## 4. Cross-Batch Overlap & Boundaries

| Candidate | Predominant Batch | Reasoning | Action |
|-----------|-------------------|-----------|--------|
| **C-B6a Untrusted Fencing** (data vs instruction, delimiting, defender at context-assembly) | **Batch 2 Context** | Must run before model sees content; survives compaction; invisible to Batch 4 policy | **PRIMARY Batch 2**, wire to Batch 4 G-X Governance |
| **C-B6b Poisoning Resilience** (ASI06 persisted malicious data, eTAMP, GLOBAL commit_memory) | **Batch 2 Mechanism** under B3 (consolidation) + Batch 4 | Promotion poisons → provenance/confidence needed at store; eTAMP trajectory reuse is governance | **Batch 2 mechanism + Batch 4 governance wiring** |
| **G-X Injection Defense Governance** (ASB benchmarks, red-team, allowlist/audit, sandbox) | **Batch 4 Safety** (P1-25..30) | Evaluation + enforcement surviving harness replacement; SC-07 | **PRIMARY Batch 4**, do NOT list in Batch 2 taxonomy row |
| **M16 Prompt Architecture** | **Batch 2 Mechanism** (but Skills Resource owned Batch 3) | Prompt pack as Resource belongs Batch 3 Integration | Mechanism Batch 2, Resource Batch 3 — hygiene: `Skills` category is Batch 3 Capability |
| **E17/C-Budget Complexity Budgets** | **Batch 5 DX/Governance** (P1-36, CR-01) | Spans cost tracking, versioning, fleet throttling | **Evidence Batch 2, owner Batch 5** |
| **C-B5 Semantic vs Prompt Cache** | **Batch 2 / Batch 5** | Response reuse is cost (Batch 5) + retrieval (Batch 2) | **Tag SPECIALIZED, owner Batch 2 retrieval, Batch 5 cost** |

---

## 5. Translation Evidence (≥2 ecosystems per kept Capability)

| Capability | Claude / Gemini | OpenAI / Codex | LangGraph / LangChain | IDE Agents | OSS Harness | Other |
|------------|-----------------|----------------|----------------------|------------|-------------|-------|
| **B1** | `200K + pinned + autoCompact` | `max_context_tokens` | `CoALA <8K active working memory` | `@codebase` window limit | `Redis in-context` | LCM `Active Context` |
| **B2** | `compact_boundary @~90%` | `summarization fallback` | `Letta paging` | — | `clido @28000`, `leuk tiered`, `mini_swe @0.85` | `Vercel Eve cheaper model` |
| **B3** | — | — | `LangMem self-rewrite` | — | `MemTier Jaccard+cognitive weight` ≡ `engram promote` | `agent-memory-mcp` |
| **B4** | — | — | `Neo4j bi-temporal` | — | `Gbrain typed KG`, `Mnemo Graphiti+FalkorDB` | `meta-knowledge-graph` |
| **B5** | — (prompt cache) | — | — | — | `Redis LangCache` ≡ `Vertector L1/L2` | `Anthropic prefix cache` (contrast) |
| **B6** | `PromptInjectionDefender` | — (trust-boundary) | `span-tainting` | `wrap_untrusted()` | `warden/keel`, `faion dual-LLM` | `wrap_untrusted()` |
| **B7** | — | — | `LlamaIndex VectorStoreQuery` | `@codebase` Chroma | `Qdrant/Weaviate RRF`, `Pinecone` | `ScyllaDB+pgvector` |
| **B8** | `CLAUDE.md + memory_snapshot` | `Sessions` | `Store user_id` | `.cursor/rules` | `Letta archival`, `Mem0 vector+extract` | `Zep bio-temporal` |
| **B9** | `claude-memory-compiler` | — | `LlamaIndex ETL` | `codebase-memory-mcp` | `Facts as First Class Objects` | Wiki `cold-memory` |
| **B10** | `ContextManager P0-P10` | — | `budget chain` | — | `context-budget SKILL 50/30/20` | `Kairn KL`, `Forge LOC` |

Every kept Capability verified ≥2 ecosystems outside vendor marketing; no candidate accepted without 2 counter-source kill attempts.

---

## 6. Tensions & Interactions (not forced DAG)

| Tension | Parties | SC Impact | Note |
|---------|---------|-----------|------|
| **Window vs Budget** | B1 ↔ B10 ↔ B2 | SC-05 vs SC-09 | 200K→1M window (B1) pushes cost without surviving compaction; B10 priority chain + B2 pinned set required. |
| **Compaction vs Fencing survival** | B2 ↔ B6 | SC-07/09 | Hardening prompts decay if compactable; B6 trust labels + pinned set must be compaction-exempt. SC-09 probe must include fencing survival. |
| **Consolidation vs Poisoning** | B3 ↔ B6b ↔ G-X | SC-07/09 | Episodic→semantic promotion is injection point (shared-memory name reuse → cross-user poisoning); needs B6b provenance + Batch 4 governance. |
| **Graph vs Vector substrate** | B4 ↔ B7/B8 | SC-07/02 | Graph gives provenance+enforcement; vector cheaper but merges neighborhoods → distinct harm. Not interchangeable; choose per archetype (C4-research → graph; C1-C3 → vector). |
| **Cache ordering vs Memory staleness** | B5 ↔ B7/B8/B3 | SC-05/01 vs stale-hit | `exact → semantic KNN+judge → LLM` per `playground-chat`; B3 supersede must invalidate B5. |
| **E5+E10 as harness arteries** | B2/B3/B6 via Batch-1 E5/E10 | SC-01/07 | Consolidation sleep pass, async compaction, and defender all run via **Batch-1 E5 Background + E10 Hooks** (`PreCompact/PostCompact/PreToolUse`) — Batch-2 Caps *consume* Batch-1 Mechanisms. Not subsumed — TOFU vs RUN wiring. |
| **E1/E2 fan-out × Budget Pareto** | E1/E2 ↔ B10/B1 | SC-05 vs SC-02 | Fan-out reduces per-agent context (helps B1) but multiplies CPSR; B10 KL regularization + 50/30/20 gates `pass@1 vs $/task`. |
| **Knowledge lifecycle wiring** | B9 ↔ B7/B8 | SC-10 vs SC-09 | SC-10 IDFR (frozen curation) is B9 build; SC-09 CSP (survival) is B7/B8 run — split vindicated (V-D §7). |
| **B1 split contention (V-C vs V-D)** | B1 vs E12 | — | V-C: merge B1+B2 into E12 (anti-bloat, CoALA nesting). V-D: split (different lifecycle, failure modes, thresholds). Synthesis keeps split with **P1-42 flag** — if MASTER_TAXONOMY bloat triggers review, merge is first collapse candidate. |

---

## 7. Archetype Interactions (C1-C6)

| Capability | C1 Product | C2 Data/MLOps | C3 Automation | C4 Agentic/Knowledge | C5 Platform | C6 Migration |
|------------|------------|---------------|---------------|----------------------|-------------|--------------|
| B1 Working Memory | important | important | important | **foundational** | important | **foundational** |
| B2 Compaction | important | important | situational | **foundational** | specialized | **foundational** |
| B3 Consolidation | specialized | important | situational | **foundational** | situational | important |
| B4 Graph Memory | situational | important | situational | **important** | situational | specialized |
| B5 Semantic Cache | situational | specialized | important | **important** | situational | situational |
| B6 Fencing (VETO) | **foundational** | important | important | **foundational** | **foundational** | important |
| B7 Retrieval | **foundational** | important | important | **foundational** | important | important |
| B8 Memory Recall | important | specialized | situational | **foundational** | situational | **foundational** |
| B9 Knowledge Curation | important | **foundational** | situational | **foundational** | **foundational** | important |
| B10 Budget Governance | important | important | specialized | **foundational** | important | specialized |

Full per-archetype SC wiring (SC-09 CSP, SC-07 SSHC, SC-05 CPSR, SC-10 IDFR) in V-D §P1-16; Phase 2 rubric consumes per-archetype deltas not means (anti-averaging per `ARCHETYPES_AND_CRITERIA.md §4.4`).

---

## 8. Sources

- Researcher method 9 angles + 7 challenger angles — [`phase-0/R-A_BROAD_MAPPER.md`](../../phase-0/R-A_BROAD_MAPPER.md) (Phase 0 patterns reused)
- Challenger 6 proposals + 2 cross-checks — [`phase-1/batch-2/R-B_CHALLENGER.md`](R-B_CHALLENGER.md) §1-3
- CoALA Princeton 2023 (4-tier memory); Letta/MemGPT Berkeley OS paper; Memory in Age of AI Agents arXiv 2512.13564 (Forms/Functions/Dynamics); LCM dual-state arXiv 2605.04050
- LangGraph `Checkpointer`/`Store` + LangMem; Mem0; Zep/Graphiti bi-temporal (valid×transaction); MemTier arXiv 2605.03675; `Zijian-Ni/agent-memory`, `blakestone-x/engram`
- LlamaIndex `VectorStoreQuery`/`NodeWithScore`/`Auto-Retrieval`; Haystack 2.x RRF/Weaviate α; Pinecone/Qdrant/Weaviate/Chroma/Milvus/pgvector benchmarks
- Cursor `@codebase`/`.cursor/rules/*.mdc` + local embeddings vs Windsurf full-repo vs Copilot `.github/copilot-instructions.md` vs Continue.dev Chroma
- OWASP ASI06 Memory Poisoning; eTAMP cross-session trajectory poisoning; ElizaOS >$25M hijack; Letta archival bleed
- `pydantic-ai-harness PromptInjectionDefender`, `faion-network trust-boundary span-tainting dual-LLM`, `warden/keel`, `autocontext wrap_untrusted()`, `agent-dx Instruction Trust Boundary`, ASB 11×565×4, AgentProbe
- Redis LangCache vs Anthropic prefix cache [Redis blog](https://redis.io/blog/prompt-caching-vs-semantic-caching); `vertector/llm-semantic-cache`, `ScyllaDB+pgvector`; `clido-ai/clido-cli`, `joyouslang/leuk`, `mini_swe_agent_v2`, `Vercel Eve`
- Harness Foundry `context-budget` SKILL (50/30/20), Kairn `effective_score = raw − λ·cost·100`, Forge LOC budget, `ContextManager` P0-P10, `ContextBudgeter` 30K/50K/100K tiers
- `codebase-memory-mcp`, `claude-memory-compiler` (34 cold-memory specs), `Facts as First Class Objects` 252× cheaper

---

## 9. Batch-Level Deliverables Checklist

- [x] P1-09 sweep (9 angles, 17 searches) — `R-A_BROAD_MAPPER.md` 74K
- [x] P1-10 challenger sweep (7 angles, 13 searches, deliberately different vocab) — `R-B_CHALLENGER.md` 43K
- [x] P1-11 context vs memory vs retrieval vs knowledge — **4-way split vindicated**: B1 vs B2 (V-C contested, split kept), B7 vs B8 (library vs notebook 4 framings convergent), B9 lifecycle split (build vs run)
- [x] P1-12 prompt injection defense placement — **SPLIT**: B6a Batch 2 (trust boundary at context-assembly) + G-X Batch 4 (governance/benchmarks) — not one or the other
- [x] P1-13 prompt architecture & complexity budgets — **identified**: M16 (assembly pattern for B1) + B10 Context Budget Governance (cross-cutting, evidence Batch 2, owner Batch 5)
- [x] P1-14 translation check (≥2 ecosystems per candidate) — `V-C_ADVERSARIAL.md` full table + kill log + anti-bloat merge rationale
- [x] P1-15 abstraction re-tag — `V-D_ARCHITECTURAL.md` 9 conflation flags (umbrella `Context Management`→B1+B2, `Vector DB` as Tool not Cap, etc.)
- [x] P1-16 converge taxonomy slice — **this file** (`BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md`) — 10 Capabilities (B1-B10) + Mechanisms/Protocols/Frameworks/Tools + tensions + archetype matrix

## 10. Open Questions & Verification Gaps

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | B1 vs E12 merge (V-C) vs split (V-D) — P1-42 decides; if MASTER_TAXONOMY bloat review triggers, merge B1+B2→E12 is first collapse candidate. | P1-42 cross-batch dedupe | Before MASTER_TAXONOMY |
| 2 | B5 level: Capability (SPECIALIZED) vs Mechanism under B7 — contested; harm 3 not veto argues Mechanism. P1-42 to rule. | P1-42 | Before gate |
| 3 | B4 promotion sufficiency: vector-metadata-is-enough counter-source needs ≥2 kill attempts by V-C P1-14 — marginal 94.8% vs 93.4% flagged. | V-C on P1-41 | Before gate |
| 4 | R-A truncation rebuild: V-C/V-D both flagged R-A payload truncated in orchestrator; full `R-A_BROAD_MAPPER.md` on disk recovered but inferred R-A2..R-A7 labels need diff against true R-A body before gate. | P1-42 | Before gate |
| 5 | B1 SC: Does SC-09 CSP already capture working-vs-persistent split or need working-specific SC? Architectural decision for Phase 2 rubric. | Phase 2 | Rubric wiring |
