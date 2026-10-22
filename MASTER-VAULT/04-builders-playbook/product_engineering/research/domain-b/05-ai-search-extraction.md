# Domain B — 05: AI Search and Information Extraction

> Scope: products that find things (AI search engines, enterprise search, product search) and products that pull structured facts out of unstructured content (document extraction, OCR pipelines). Research date: 2026-10-10.

## 1. AI search as a product

**Plain English:** An AI search product takes a question, searches a large index (the web, a company's apps, a product catalog), and returns either ranked results or a synthesized answer with citations. The hard engineering is not the answer generation — it's the retrieval and ranking underneath (see 02-RAG and Perplexity's Photon below).

**Concrete example:** Perplexity's answer engine. For each query its stack retrieves and ranks candidate web pages, then a model writes a grounded answer. When Perplexity's index and workload outgrew its adapted open-source retrieval engine, a small team rebuilt the retrieval layer from scratch as **Photon** (Rust, Sept 2026).

### 1.1 Perplexity Photon — deep technical case

- **Why rebuild:** the old system hit hard limits — scaling costs (RAM-bound), poor tail latency (p99 ~800ms, spiking to ~1.2s during index merges due to page faults), and week-long cluster recovery/sync. Fixing these inside the fork meant redesigning the platform anyway.
- **What Photon does:** compact posting-list formats chosen by list length/density (inline, sorted offset arrays, bitmaps); WAND-style bounded candidate traversal within a fixed work budget; per-document "docblob" records (Elias-Fano term lists, field masks, positions) so ranking needs one lookup per document; io_uring batched async disk reads with batch-aware caching; index building separated from query serving with cache warming before live traffic.
- **Measured results (company-reported, with published caveats):** single-search-call latency 160ms p50 / 230ms p95; the "Fast" Search API preset cut estimated model-plus-search cost per task by ~68% at comparable aggregate quality across six public benchmarks; Search API pricing $1.00/1k requests (fast) vs $5.00/1k (standard).
- **Also in the stack:** CobbleDB (distributed key-value store for page records), custom contextual embeddings (int8-quantized, ~1KB/vector at 1024 dims vs ~8KB for a float32 alternative — directly an index-cost decision).
- **Evaluation honesty note:** Perplexity publishes benchmark details but not the full test sets; the Artificial Analysis Search Index (1,700 questions, fixed model, agent harness) scored Perplexity's medium Search API config highest (80 vs 75/74 for rivals, 33 baseline without search) — third-party corroboration of the *search layer's* value.
- **Evidence:** primary technical (Perplexity engineering blog, 2026-09-24); corroborating (Artificial Analysis via cryptobriefing, 2026-08). Accessed 2026-10-10. Confidence: **Verified** on engineering facts; **Corroborated** on benchmark standing.

### 1.2 Algolia — product search + agentic layer

- **Architecture guidance (Algolia's own docs):** apply hard constraints first (tenancy, ACLs), then hybrid retrieval, then business tuning (rules, synonyms, custom ranking); add reranking *only if the p95 budget permits*; treat recommendations as optional layers on a stable retrieval foundation.
- **The agentic pattern:** the LLM decides *what* to retrieve/do; Algolia remains the source of truth for searchable data — keeping agentic search grounded instead of letting the model invent products, availability, etc. (Same brain/body split as Notion in 01.)
- **Evidence:** primary technical (Algolia architecture docs). Accessed 2026-10-10. Confidence: **Verified**.

### 1.3 Enterprise search (Glean) — covered in 02

Glean's differentiator as a *search* product: permission-aware retrieval in real time, knowledge graph over the enterprise, and the explicit argument that enterprise search is a search problem first, an LLM problem second.

### 1.4 Negative evidence in AI search

- **Google AI Overviews (2024):** viral failures — recommending glue on pizza, eating rocks — traced to the model surfacing low-quality sources (Reddit jokes) as authoritative answers. Google scaled back and added guardrails. **Lesson:** answer synthesis inherits the credibility of its worst retrieved source; source-quality gating is a product requirement.
- **Google "What People Suggest" (shut down March 2026):** an AI search feature summarizing crowdsourced health tips from forums. Removed after evidence of misleading health advice (including cases of delayed emergency care); WHO/FDA/EMA pressure. Google framed it as "simplifying search," not a safety retreat — a framing gap worth noting. **Lesson:** some domains (health) need expert-source constraints, not just better retrieval; disclaimers don't fix authoritative tone.
- **Evidence:** secondary (Android Authority, March 2026; AI News). Accessed 2026-10-10. Confidence: **Corroborated** on the shutdown; **Inferred** on internal motivations (Google's stated reason vs. critics' reading).

## 2. Information extraction as a product

**Plain English:** Extraction products turn messy documents into structured data: invoices → {vendor, line items, totals, tax}; contracts → {parties, dates, clauses}; forms → database rows. The product promise is "no more manual data entry."

**Concrete example:** A production invoice pipeline: PDF → page images → OCR (Google Vision DOCUMENT_TEXT_DETECTION) → LLM field extraction (GPT-4.1-class) → structured JSON with per-field confidence scores → validation (type checks, range checks, cross-field arithmetic like subtotal + tax = total) → human review queue for low-confidence fields.

**Deeper mechanics:** OCR accuracy is the ceiling — at ~98% OCR accuracy you can reach ~85–90% field-extraction accuracy; at 60% OCR the whole pipeline degrades. That's why serious pipelines use dedicated OCR (not a vision LLM) for the text layer, then the LLM only for *structuring*. Modern invoice OCR APIs claim 85–95% accuracy depending on document quality; vendor marketing often implies higher — treat unqualified accuracy claims as **Proposed** until measured on your document mix.

### 2.1 Design patterns

- **Two-stage (OCR → LLM):** best accuracy/cost trade for scanned documents; OCR is cheap and deterministic.
- **Vision-LLM direct:** GPT-4o-class models read document images directly — better for complex layouts, worse for bulk cost; field-level accuracy is the eval metric (F1 per field, not vibes).
- **Confidence-gated human review:** every field carries a confidence score; below threshold → human queue. This is the extraction world's human-in-the-loop.
- **Cost engineering:** a practitioner case shows 85–93% per-document cost reduction by (1) baselining with the expensive model, (2) skipping fields a document type can't contain, (3) tiered per-field model routing, (4) field-level caching of unchanged values, (5) scale-to-zero serving. The savings compound because each attacks a different waste.
- **Evidence:** first-hand practitioner (Medium invoice-pipeline build, tested on 500 invoices: 98.7% clean / 92.3% handwritten OCR); practitioner (DEV cost-optimization case). Accessed 2026-10-10. Confidence: **Corroborated** on architecture; **Inferred** on the exact savings generalizing (workload-specific).

### 2.2 Evaluations

- **Field-level F1/accuracy** per document type; character/word error rates for OCR; table-structure accuracy; human adjudication of low-confidence bands.
- **The eval that matters:** measured on *your* document distribution (clean scans vs. photos vs. handwriting) — vendor benchmarks on clean documents don't transfer.

## 3. Cross-cutting engineering lessons

1. **Retrieval is the product; generation is the narrator.** Perplexity rebuilt retrieval, not the model. Algolia keeps the index as source of truth. Glean says it's a search problem.
2. **Source quality is answer quality.** AI Overviews' glue-pizza and "What People Suggest"'s health tips both failed at the *source selection* layer.
3. **Extraction is a pipeline with a ceiling:** OCR accuracy caps everything downstream; confidence scores + human review are the reliability system.
4. **Cost lives in the retrieval/extraction layer** (index RAM, OCR calls, per-field model routing) more than in any single model call.

## 4. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Photon: in-house Rust retrieval engine; 160ms p50/230ms p95; −68% cost; old system p99 800ms–1.2s | https://www.perplexity.ai/hub/blog/photon | primary technical / Perplexity | 2026-09-24 | 2026-10-10 | Verified | primary technical |
| Artificial Analysis Search Index: Perplexity 80, rivals 75/74, no-search baseline 33 | https://cryptobriefing.com/perplexity-tops-artificial-analysis-search-index/ | secondary / CryptoBriefing | 2026-08 | 2026-10-10 | Corroborated | corroborating |
| Algolia: constraints → hybrid retrieval → tuning → rerank only within p95; LLM decides, index is truth | https://www.algolia.com/resources/asset/architecture-data-foundations-for-ai-powered-search | primary technical / Algolia | 2026 | 2026-10-10 | Verified | primary technical |
| Google shut "What People Suggest" (Mar 2026) after health-misinformation evidence | https://www.androidauthority.com/google-discontinues-what-people-suggest-feature-3649683/ | secondary / Android Authority | 2026-03 | 2026-10-10 | Corroborated | corroborating |
| Invoice pipeline: OCR accuracy is the ceiling; 98.7% clean / 92.3% handwritten (n=500) | https://medium.com/@vaidehivasudev3082/how-i-built-an-invoice-extraction-pipeline-with-google-vision-api-gpt-4-1-aa9fd95e7981 | first-hand practitioner | 2026-04 | 2026-10-10 | Corroborated | first-hand practitioner |
| Extraction cost −85–93% via routing/caching/adaptive fields | https://dev.to/avneet_bansal_a65b3f31fc4/cut-llm-document-extraction-cost-by-85-without-losing-accuracy-34ip | practitioner / DEV | 2026-10 | 2026-10-10 | Inferred (workload-specific) | community observations |

**Gaps / Unknowns:** Perplexity's index size and exact ranking signals; any vendor's measured production faithfulness rate for AI answers; independent audits of extraction-accuracy marketing claims.
