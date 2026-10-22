# Domain B — 02: Retrieval-Augmented Generation (RAG) in Products

> Scope: products whose AI answers are grounded in retrieved documents at query time (support copilots, enterprise search assistants, doc Q&A). Research date: 2026-10-10.

## 1. What RAG is (plain English → mechanics)

**Plain English:** RAG = search first, then generate. Instead of asking the model to answer from its training memory (where it invents things), the product searches the customer's own documents for relevant passages and hands *those* to the model, saying "answer using only this." Every generated claim should trace back to a retrieved chunk.

**Concrete example:** A healthcare SaaS support assistant built on RAG over 40,000 internal policy documents. Demo accuracy was 94%; three weeks into production the failure rate hit 38% — the model was answering confidently and incorrectly because it was faithfully summarizing the *wrong* documents. The fix was retrieval architecture, not a bigger model.

**Deeper mechanics:** The standard pipeline is: chunk documents → embed chunks into vectors → store in a vector index (ANN — approximate nearest neighbor — for speed at scale) → at query time embed the query → retrieve top-k chunks → rerank → stuff into the prompt → generate with citations. Failure concentrates at every seam: chunking splits context mid-thought; ANN returns "slightly worse" neighbors at scale; stale documents linger in the index; queries are vague ("that thing John mentioned Tuesday"). A practitioner who ran a Fortune-500 retrieval platform to 20+ production workflows reports: *almost no incident was a generation failure — they were retrieval failures wearing a generation costume.*

## 2. Why RAG fails in production (negative evidence)

The naive demo assumes: clean static data, one user, predictable queries, a tiny index, and "looks right on my machine" as the metric. Production reality: async document streams, hourly document updates/revokes, vague queries, 500 concurrent users, and p99 latency < 2s with token-cost control. Five recurring fault lines (synthesized from practitioner postmortems):

1. **The small-data trap.** Locally you search a tiny index with exact search; in production ANN approximation returns slightly-worse neighbors — and in RAG, a slightly-worse chunk is the difference between a fact and a confident hallucination.
2. **Silent quality decay.** Accuracy can drop from ~90% to ~60% with no errors, no crashes, no alerts — dashboards stay green while users get garbage. Monitoring must track *quality* signals (refusal rate, schema-validation failures, fallback rate, user edits, thumbs-down), not just uptime.
3. **Document lifecycle drift.** Demo data is static; production documents update, get revoked, or are appended hourly. Stale or contradictory chunks poison answers. Glean's answer: real-time permission-aware indexing, not nightly batch syncs.
4. **Evaluation only on happy paths.** QA sign-off on a hand-curated test set (the healthcare case: 94% demo accuracy) does not survive real query distributions.
5. **Ingestion is a product, not a step.** Crawling, parsing, chunking, dedup, and diagnostics ("why did this return 0 pages?") need their own engineering — see the markcrawl postmortem, where a public benchmark forced six releases in 72 hours over silent-failure ingestion bugs.

## 3. Enterprise RAG as platform (Glean case)

Glean (founded 2019 by ex-Google search engineers) is the clearest enterprise RAG product:

- **Architecture:** connectors pull data from 100+ apps → index/chunk → knowledge graph maps people–documents–topics → hybrid retrieval (semantic + keyword) → rerank → LLM generates cited answers. Permission-awareness is real-time: the LLM only ever sees documents the user is authorized to see.
- **Why not fine-tune:** Glean's engineering writing argues fine-tuning an LLM for enterprise knowledge has too many limits/risks (stale knowledge, data leakage across tenants, catastrophic forgetting); RAG keeps knowledge fresh at query time.
- **Evaluation:** LLM-as-judge and "LLM jury" techniques for answer accuracy.
- **Knowledge graph beyond RAG:** multi-hop questions ("who owns the service that depends on the API in this doc?") need traversable organizational structure, not just similar passages; permissions attach at the fact level.
- **Evidence:** primary technical (Glean engineering blog, glean.com); first-hand practitioner (ex-Slack CPO Tamar Yehoshua interview, tessl.io podcast, ~2024). Accessed 2026-10-10. Confidence: **Corroborated** on architecture; **Inferred** on internals (vendor-described).

## 4. Retrieval design decisions (what teams actually tune)

| Decision | Practice | Why it matters |
|---|---|---|
| Chunking | Small overlapping chunks; structure-aware (headings, tables) | Bad splits break the evidence the model needs |
| Hybrid retrieval | Keyword (BM25) + vector + reranker | Vector alone misses exact terms (IDs, names, codes) |
| Permissions | Enforced at retrieval, real-time | A nightly sync leaks confidential docs into answers |
| Freshness | Incremental re-indexing, TTLs, revocation | Stale policy docs → wrong answers with citations |
| Reranking | Cross-encoder over top-k, gated by p95 budget | Improves top-of-answer precision; costs latency |
| Citations | Every claim links to source chunk | Lets users verify; makes "ungrounded" visible |
| Query rewriting | LLM turns user query into search queries | Handles vague/conversational queries |

**Perplexity's Photon (Sept 2026)** is the deepest public retrieval-engineering case: Perplexity outgrew its forked open-source retrieval engine (p99 ~800ms–1.2s, week-long cluster recovery, RAM-bound scaling) and rebuilt in-house (Rust) with compact posting-list formats, WAND-style bounded traversal, per-document "docblob" ranking records, io_uring batched disk reads, and index-build/serve separation. Result: 160ms p50 / 230ms p95 per search call; ~68% lower model-plus-search cost per task at comparable quality. **Engineering implication:** at AI-search scale, retrieval infra — not the model — is the cost/latency battleground. Evidence: primary technical (Perplexity engineering blog, 2026-09-24). Accessed 2026-10-10. Confidence: **Verified** (numbers are company-reported with unusual transparency about measurement caveats).

## 5. Evaluations for RAG (summary; detail in 08)

- Golden datasets of Q/A pairs with required sources; RAGAS-style metrics (faithfulness, answer relevance, context precision/recall); LLM-as-judge calibrated against humans; production mining of failed traces back into evals.
- **Practitioner rule:** the model wasn't shown the answer → measure retrieval recall *separately* from generation faithfulness, or you'll "fix" the wrong layer.

## 6. Cost, latency, reliability notes

- **Latency budget:** p99 < 2s is the commonly cited production target for RAG Q&A; retrieval is usually the long pole, not generation.
- **Cost:** dominated by input tokens (retrieved context re-sent per query) — trim top-k, summarize history, cache shared prefixes (see 09).
- **Reliability:** the markcrawl postmortem and the healthcare case both show RAG's characteristic failure is *silent wrongness*, so the reliability strategy is quality monitoring + evals, not just uptime.

## 7. Security notes (detail in 10)

- RAG ingestion is an injection surface: malicious documents/web pages with hidden instructions get retrieved and obeyed (indirect prompt injection — e.g., Notion AI PDF exfiltration case, 2025).
- Permission-aware retrieval is a security control, not a feature: without it, RAG leaks documents across authorization boundaries.

## 8. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Healthcare RAG: 94% demo → 38% production failure; retrieval, not model, was the fix | https://medium.com/@ailoittetech/we-shipped-a-rag-system-that-worked-perfectly-then-production-happened-53f366af55f2 | first-hand practitioner / Sunil Kumar | 2026-04-01 | 2026-10-10 | Corroborated | first-hand practitioner |
| Naive RAG failure modes: demo/prod gap across ingestion, lifecycle, queries, concurrency | https://blog.stackademic.com/why-most-rag-pipelines-fail-in-production-6dd343b10454?gi=741475b7fea5 | practitioner / Kawal Jain | ~2026-05 | 2026-10-10 | Corroborated | corroborating |
| Enterprise RAG: retrieval failures wearing generation costume; platform > project | https://www.linkedin.com/pulse/making-enterprise-rag-platform-project-what-broke-when-atiqul-islam-bdftc | first-hand practitioner (Fortune 500) | ~2026-08 | 2026-10-10 | Corroborated | first-hand practitioner |
| markcrawl: six releases in 72h driven by benchmark-surfaced ingestion failures | https://github.com/aimlpm/markcrawl/blob/HEAD/docs/POSTMORTEM_v0.10-v0.11.md | primary technical / markcrawl team | 2026-05 | 2026-10-10 | Verified | primary technical |
| Glean: RAG architecture, real-time permission-aware indexing, LLM-jury evals | https://www.glean.com/blog/the-enterprise-ai-copilot-playbook-for-business-leaders | primary technical / Glean | 2026 | 2026-10-10 | Corroborated | primary technical |
| Perplexity Photon: in-house retrieval engine; 160ms p50/230ms p95; −68% cost | https://www.perplexity.ai/hub/blog/photon | primary technical / Perplexity | 2026-09-24 | 2026-10-10 | Verified | primary technical |
| Junior engineer: first RAG deploy crashed repeatedly on quota/CORS/migrations | https://dev.to/blessedefem/i-built-a-production-rag-system-in-3-weeks-heres-what-actually-broke-556m | first-hand practitioner | ~2026-01 | 2026-10-10 | Corroborated | first-hand practitioner |

**Gaps / Unknowns:** exact chunking/embedding configs of Glean or Perplexity (not disclosed); production faithfulness numbers for any vendor's RAG (none publish); cost-per-query for enterprise RAG deployments.
