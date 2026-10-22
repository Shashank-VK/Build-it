# Domain C — AI Automating Organisational Work: Research & Knowledge Management

**Workstream:** domain-c · **Area 2 of 8** · Researched 2026-10-10

> Scope: AI systems that help the organisation find, synthesise, and preserve its own knowledge — enterprise search, RAG (retrieval-augmented generation) assistants over internal docs, research synthesis for decision-making, knowledge capture from departing staff. Internal-facing; the users are employees.

**Plain-English terms used below:**
- **RAG** — the assistant looks up relevant passages in the company's documents, then writes an answer using those passages. Concrete example: asking "what's our parental leave policy?" and getting an answer quoted from the HR handbook, with a link.
- **Chunking** — splitting documents into searchable pieces. Bad chunking is the #1 cause of "the doc exists but the bot can't find it."
- **Semantic layer / knowledge graph** — a map of how terms and entities relate (e.g. "ARR" in Finance means something different than in Sales). Extraction is expensive and noisy.
- **Confused deputy** — the AI acts with broader permissions than the asking user has, and leaks data the user shouldn't see. The recurring shape behind RAG data-leak incidents.

---

## 1. How organisations actually deploy it

Mature enterprise RAG pipelines (2024–2025) have converged on a multi-stage architecture, a step beyond naive "embed documents and search":

1. **Ingestion**: connectors to SharePoint, Confluence, Google Drive, ServiceNow, tickets; chunking (often ~500 tokens with overlap), metadata tagging, access-control labels attached at index time.
2. **Retrieval**: hybrid search (dense vector + keyword/BM25), reranking, sometimes multi-hop query decomposition for complex questions.
3. **Generation**: model answers only from retrieved context, with citations; hallucination checks (NLI-based faithfulness scoring — i.e. a second model checks whether the answer is actually supported by the quoted sources).
4. **Evaluation**: regression test suites over golden Q&A sets; citation-validity checks.

A lighter alternative gaining traction: compiling the company wiki into a single LLM-readable document consumed by a long-context model ("digital second brain" pattern) — no vector database to maintain, but the whole corpus must fit in context and updates mean recompiling.

## 2. Documented cases

### Enterprise RAG maturity findings
- **Retrieval precision**: hybrid search + reranking improved retrieval precision 15–30% over naive vector search [NStarX industry analysis, secondary interpretation — **Corroborated** as a direction, numbers vendor-adjacent].
- **Evaluation gap**: **70% of RAG systems still lack systematic evaluation frameworks**, making quality regressions undetectable [NStarX citing industry data — **Corroborated**, high significance].
- **Knowledge graph costs**: GraphRAG-style extraction costs **3–5× more LLM calls** than baseline RAG, with entity-recognition accuracy of 60–85% depending on domain [NStarX — **Corroborated**].
- **Gartner (Dec 2024)**: **30% of generative AI projects will be abandoned after proof of concept by end of 2025**; retrieval quality, not model quality, is the most common failure reason [analyst prediction — **Corroborated**].

### ROI claims — marketing vs measured (a cautionary pair)
- A widely-cited consultancy marketing page claims enterprise RAG delivers **300–500% ROI within the first year**, knowledge search time cut from ~25 min to ~3 min, 30–50% productivity gains. **However**, a detailed source audit (athandapani/ai-adoption-wiki, GitHub, July 2026) found: **no methodology, no sample, no citations, no named author** behind those figures; the headline $300k-per-departing-employee figure is not in the cited source; and the 2.5 hrs/day search-time figure is contradicted by another cited source saying 1.8 hrs/day. **Label: Unverified; treat as marketing. Engineering implication: demand sample, method, and baseline before believing any RAG ROI number.**
- An independent GitHub production RAG pipeline (jhondados/rag-enterprise-pipeline, Vertex AI + BigQuery) reports **94.7% answer accuracy vs 67% baseline, 183ms latency at 10k concurrent users, $0.0003/query vs $0.08 naive** [first-hand builder, community evidence — **Corroborated** as an existence proof of achievable engineering, not as a universal benchmark].

### Security incidents — the negative evidence
- **EchoLeak (CVE-2025-32711, late 2025) [Verified — CVE record; analysed by Aim Security/arXiv]**: a specially crafted *un-clicked* email manipulated Microsoft 365 Copilot's enterprise RAG pipeline — the assistant retrieved the attacker's content plus private organisational data, and exfiltrated data via an auto-loaded Markdown image URL. No employee interaction needed. Shows RAG pipelines are a data-exfiltration surface, not just a Q&A tool.
- **Vector-database exposures (2024–2025) [Corroborated — CSO Online reporting]**: exposed API keys; in one fintech breach, "reconstruction attacks" reverse-engineered embeddings back into millions of original client investment portfolios; a Pinecone access-control bypass exposed 200,000+ healthcare records. Implication: embeddings are not anonymisation — they can be inverted.
- **ServiceNow RAG connector ACL failure [first-hand practitioner — dev.to, Oct 2026]**: ServiceNow's *user criteria* (its access-control mechanism) is ignored at **ingestion** by the connector role the documentation itself instructs you to assign, and never rebuilt afterwards. In a mixed knowledge base, "non-ACL data sources return results to every user." The practitioner notes: "this is not a connector bug, it is its published contract, and designing around it is your job." Textbook confused-deputy failure with a real incident trail (index destroyed in staging before end-user exposure).
- **OWASP AISVS (2025)**: formalises the pattern — retrieve-then-filter (filtering *after* retrieval) leaks through candidate counts, scores, latency, and empty-answer patterns; authorisation must be recomputed before every retrieval expansion [standards-track — **Corroborated**].

## 3. Measured outcomes

| Metric | Value | Label |
|---|---|---|
| Retrieval precision gain, hybrid+rerank | +15–30% | Corroborated |
| Answer accuracy, production RAG vs naive | 94.7% vs 67% | First-hand builder — Corroborated (single deployment) |
| Cost per query, optimised vs naive GPT-4 | $0.0003 vs $0.08 | First-hand builder — Corroborated (single deployment) |
| Two-stage retrieval accuracy gain | 70% → 92%, hallucinations −85% | Vendor (Chat Data) — Unverified |
| Knowledge search time | 25 min → 3 min (−88%) | Consultancy marketing — Unverified |
| Employee productivity gain | 30–50% | Consultancy marketing — Unverified |

## 4. Failure modes

1. **Retrieval failure, not model failure** (most common per Gartner): wrong chunking, stale index, or semantic drift means the right document never reaches the model — the answer is then fluent and wrong.
2. **Temporal blindness**: outdated information served (policies change; index lags). Real-time index updates are the fix; 24–48h lags are the norm in naive setups.
3. **Permission leakage / confused deputy**: ACLs attached at query time but not enforced at retrieval; multi-hop expansion pivoting into unauthorised resources; federated connectors with different ACL contracts.
4. **Prompt-injection via retrieved content** (EchoLeak): retrieved documents are attacker-controlled input; the model treats them as instructions.
5. **No evaluation framework**: 70% of deployments can't detect regressions — the silent failure mode.
6. **Organisational amnesia persists**: employees paste the same context into every session because nothing is captured back into the shared layer (dev.to practitioner essay).

## 5. Human oversight / approval design

- **Evaluation gates**: golden Q&A suites run on every index/prompt change; regression = block deploy.
- **Citation requirements**: answers must cite source documents; unresolved citations rejected (pattern from production orchestration case studies).
- **Faithfulness scoring**: automated NLI check that the answer is entailed by cited sources; low scores route to human review or refusal.
- **Access pre-filters**: caller's tenant/user/role/data-classification computed by trusted server code and pushed into the vector query as a pre-filter — never filter after retrieval.
- **Freshness SLAs**: index-lag budgets per source type; time-sensitive answers carry "as of" timestamps.

## 6. Cost vs benefit

- Infrastructure is cheap at query time when optimised (sub-cent per query) but graph extraction and eval harnesses are the real costs (3–5× for knowledge graphs; eval frameworks are engineering time most teams skip).
- The biggest cost is failure: a RAG system nobody trusts reverts the organisation to manual search — the 70%-without-evaluation figure suggests most deployments are flying blind.

## 7. Data governance / privacy

- RAG indexes concentrate the company's sensitive data in one searchable surface — classification, tenant isolation, and per-user ACL enforcement are the entire game.
- Embeddings are reversible (reconstruction attacks) — treat vector stores as holding the original data's sensitivity.
- Retrieved content can contain PII the model then repeats; PII redaction at ingestion is a standard control.
- EU AI Act / GDPR: logging of what was retrieved for whom is needed for both audit and breach assessment.

## 8. Open gaps

- No standardised audit method for agent retrieval decisions in regulated industries.
- ROI literature is dominated by methodology-free vendor claims; independent measurement is rare.
- Cross-connector ACL semantics (ServiceNow vs SharePoint vs Drive) are inconsistent and under-documented — each connector is a separate trust decision.
