# Context, Memory & Knowledge — Per-Element Knowledge Base (Phase 4, Batch D-2)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md`
> **Template:** 18-section per element. Consolidated for the Context/Memory layer.

---

## CAP-08 — Working Memory Management & Isolation
1. **Overview:** Bounded active scratchpad (context window) with `max_context_tokens`; isolates attention vs persistent.
2. **Why matters:** Prevents attention dilution/lost-in-middle; cost control (SC-05).
3. **How works:** Pinned system+tools+recent-N in window; eviction policy.
4. **When use:** Every turn of every agent (universal).
5. **When NOT:** Never (baseline substrate).
6. **Importance:** S-tier (universal). All archetypes S.
7. **Essential:** tiktoken token counter.
8. **Optional:** langchain memory.
9. **Rules:** Enforce token budget; pin invariants; head-trim old.
10. **Deps:** CAP-16 budget.
11. **Integration:** Feeds compaction (CAP-09).
12. **Failure modes:** Window stuffing → reasoning degrade; cost blowup.
13. **Security:** Pin security rules (non-evictable).
14. **Maintenance:** Tune limits per model.
15. **Sources:** Batch-2 B1.
16. **Links:** tiktoken (openai).
17. **Last verified:** 2026-09-01.
18. **Re-check:** Model window-size changes.

---

## CAP-09 — Context Compaction & Pinned Preservation
1. **Overview:** Threshold-triggered loop summarizing/evicting history while preserving pinned invariants.
2. **Why matters:** Long-horizon survival (SC-09); 77% entity loss if summarize poorly.
3. **How works:** 60/75/90% thresholds; structured merge (goal/files/decisions/pending); semantic-index regen.
4. **When use:** Long tasks >30k tokens; C4/C6.
5. **When NOT:** Short single-turn.
6. **Importance:** S-tier. C4/C6=S; C1/C2=A; C3/C5=B.
7. **Essential:** Letta (MemGPT).
8. **Optional:** Summarizer libs.
9. **Rules:** Never compact pinned; multi-strategy (L1+L2+L3); budget summary model.
10. **Deps:** CAP-08, CAP-16, hooks.
11. **Integration:** PreCompact hook (E10).
12. **Failure modes:** Pinned loss; entity drop; cost.
13. **Security:** Fencing must survive compaction (B6↔B2).
14. **Maintenance:** Review thresholds.
15. **Sources:** Batch-2 B2.
16. **Links:** https://github.com/letta-ai/letta.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Compaction algorithm change.

---

## CAP-10 — Memory Consolidation & Fact Promotion
1. **Overview:** Background daemon merging episodic events → deduplicated semantic facts (hash-chained provenance).
2. **Why matters:** Long-term learning; episodic bloat control (47K→3.2K/30d; +33pp LongMemEval).
3. **How works:** Jaccard dedup, heuristic+LLM extraction, `informed_by` links, cognitive weight.
4. **When use:** Persistent/cross-session agents (C4/C6).
5. **When NOT:** Stateless/ephemeral tasks.
6. **Importance:** A-tier (B: short; S: C4/C6). C4=S; C2/C6=A.
7. **Essential:** Mem0, Zep.
8. **Optional:** engram, MemTier.
9. **Rules:** Provenance hash-chain; dedup threshold; weight supersede.
10. **Deps:** CAP-14 recall.
11. **Integration:** Runs in background (CAP-05); session hook.
12. **Failure modes:** Poisoning at consolidation boundary.
13. **Security:** Input validation before promotion (B6b).
14. **Maintenance:** Daemon cadence tuning.
15. **Sources:** Batch-2 B3.
16. **Links:** https://mem0.ai; https://getzep.com.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Memory framework versions.

---

## CAP-11 — Typed Bi-Temporal Knowledge Graph Memory
1. **Overview:** Durable graph (nodes/typed edges) with valid×transaction time; multi-hop + provenance.
2. **Why matters:** Relational reasoning, constraint enforcement after compaction (C4 research).
3. **How works:** Neo4j/FalkorDB/Graphiti; Cypher over MCP; hybrid vector+BM25+RRF entry.
4. **When use:** Knowledge-intensive C4/C2; graph-native queries.
5. **When NOT:** Simple RAG-suffices (C1/C3).
6. **Importance:** B-tier (specialized). C4=A; C2=B; rest C.
7. **Essential:** (Optional-tier) Neo4j/Graphiti.
8. **Optional:** Zep.
9. **Rules:** Typed schema; temporal columns; provenance.
10. **Deps:** CAP-13/15.
11. **Integration:** Substrate for memory/recall.
12. **Failure modes:** Entity-neighborhood poisoning; schema drift.
13. **Security:** Trust boundary for graph writes.
14. **Maintenance:** Schema migrations.
15. **Sources:** Batch-2 B4.
16. **Links:** https://neo4j.com.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Graph DB changes.

---

## CAP-12 — Semantic & Response Caching
1. **Overview:** Meaning-based embedding-similarity answer reuse (exact→semantic→LLM), namespace/TTL.
2. **Why matters:** Cost/latency on high-volume paraphrased calls (C3/C4).
3. **How works:** Redis LangCache/Valkey/RedisVL; threshold ~0.95; namespace isolation.
4. **When use:** High-volume C3/C4; repeated near-identical requests.
5. **When NOT:** Low-volume; correctness-critical (staleness).
6. **Importance:** B-tier (specialized). C3=A; C4=B; rest C.
7. **Essential:** (Optional) Redis LangCache.
8. **Optional:** Vertector.
9. **Rules:** Threshold+TTL+namespace; invalidate on supersede.
10. **Deps:** CAP-10 invalidation.
11. **Integration:** Wraps model runner.
12. **Failure modes:** Stale-hit; cache poisoning.
13. **Security:** Namespace tenant isolation.
14. **Maintenance:** Watch staleness.
15. **Sources:** Batch-2 B5.
16. **Links:** Redis blog semantic caching.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Redis versions.

---

## CAP-13 — External Knowledge Retrieval (RAG)
1. **Overview:** Stateless read-only retrieval over indexed external corpora (hybrid dense+BM25+RRF).
2. **Why matters:** Grounding, anti-hallucination, corpus > window (SC-02/SC-08).
3. **How works:** index→embed→store; query→hybrid→re-rank→augment.
4. **When use:** Any external-knowledge task (C1 codebase, C4 research, C2 docs).
5. **When NOT:** No external corpus; embedded knowledge sufficient.
6. **Importance:** S-tier. C1/C4=S; C2/C3/C5/C6=A.
7. **Essential:** Qdrant/pgvector + LlamaIndex/Haystack.
8. **Optional:** Pinecone/Weaviate/Chroma.
9. **Rules:** Hybrid search; pinned chunking; lineage.
10. **Deps:** CAP-15 curation.
11. **Integration:** Augments prompt assembly (CAP-16).
12. **Failure modes:** Stale index; hallucination; latency.
13. **Security:** Injection-defense on retrieved chunks (B6).
14. **Maintenance:** Index refresh cadence.
15. **Sources:** Batch-2 B7.
16. **Links:** https://qdrant.tech; https://www.llamaindex.ai.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Vector DB/RAG major versions.

---

## CAP-14 — Experiential Memory Recall
1. **Overview:** Stateful read-write-learn-forget cycle retrieving past decisions/corrections/conventions.
2. **Why matters:** Long-horizon continuity, no repeat bugs (sc-09). Sharp archetype divergence.
3. **How works:** Capture→store→retrieve→update→forget, decay/consolidation/supersede.
4. **When use:** C4/C6 long-horizon; C1 project conventions.
5. **When NOT:** Stateless C3/C5.
6. **Importance:** A-tier global (S C4/C6; C C3/C5).
7. **Essential:** Mem0/Zep/LangGraph Store.
8. **Optional:** Letta.
9. **Rules:** Provenance; decay policy; supersede.
10. **Deps:** CAP-10 consolidation.
11. **Integration:** Shared via agent teams.
12. **Failure modes:** Amnesia post-compaction; poison.
13. **Security:** Validate external writes.
14. **Maintenance:** Review facts.
15. **Sources:** Batch-2 B8.
16. **Links:** LangGraph Store.
17. **Last verified:** 2026-09-01.
18. **Re-check:** memory API versions.

---

## CAP-15 — Build-Time Knowledge Curation & Indexing
1. **Overview:** Offline pipeline index→extract→cluster→distill→version (SBOM-like lineage).
2. **Why matters:** Index correctness (SC-08), frozen re-run (SC-10), 252× cheaper than runtime.
3. **How works:** AST parse, chunk, embed, versioned artifacts.
4. **When use:** C2/C5/C6 persistent corpora; C4 research.
5. **When NOT:** Throwaway research (C4 short).
6. **Importance:** A-tier. C2/C4/C5=S; C1/C6=A; C3=C.
7. **Essential:** (build-time) indexing pipelines.
8. **Optional:** dbt/DBT-style lineage.
9. **Rules:** Version + verify; lineage log; frozen re-run.
10. **Deps:** CAP-13 consumer.
11. **Integration:** Feeds retrieval.
12. **Failure modes:** Stale/conflicting knowledge.
13. **Security:** Scan indexed content.
14. **Maintenance:** Refresh cadence.
15. **Sources:** Batch-2 B9.
16. **Links:** codebase-memory-mcp, llmsherpa.
17. **Last verified:** 2026-09-01.
18. **Re-check:** index tooling.

---

## CAP-16 — Context & Token Budget Governance
1. **Overview:** Turn-level allocation/arbitration (P0-P10 priority, 50/30/20, KL regularization).
2. **Why matters:** Cost guard (SC-05), pinned survival (SC-09), window competition.
3. **How works:** Priority-ranked prompt assembly; token caps; eviction.
4. **When use:** Every turn (esp C4 long).
5. **When NOT:** Never (universal guardrail).
6. **Importance:** A-tier. C4=S; rest A/B.
7. **Essential:** tiktoken + budget config.
8. **Optional:** context-budget SKILL.
9. **Rules:** P0-P10 order; hard caps; budget guard <5% overruns.
10. **Deps:** CAP-08.
11. **Integration:** Governs all prompt assembly.
12. **Failure modes:** Over-budget, pinned eviction.
13. **Security:** Security instructions prefixed P0 (non-evictable).
14. **Maintenance:** Tune per model.
15. **Sources:** Batch-2 B10.
16. **Links:** (context-budget skill).
17. **Last verified:** 2026-09-01.
18. **Re-check:** model/TTL changes.

---

*End of D-2 (Context/Memory).*