# Sourcegraph — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Sourcegraph's instructive value is "retrieval as the product": a decade of code-search infrastructure became the moat for an AI coding assistant (Cody). Sources are Sourcegraph's own blogs (via secondary synthesis) plus independent RAG teardowns.

## Findings

### Architecture
- Claim: Cody's retrieval layer is a two-stage Context Engine: stage 1 retrieves candidates from multiple heterogeneous sources optimised purely for recall ("cast a wide net"); stage 2 runs a pointwise ranker scoring each candidate for relevance, then applies a token-budget + threshold cutoff — the number of chunks in the prompt is a function of relevance quality and context budget, not a fixed top-k. Label: **Corroborated** — dhruvmakwana RAG teardown synthesising Sourcegraph's blogs.
- Claim: Each Cody feature uses its *own* retrieval strategy rather than one universal pipeline: Chat blends keyword search (BM25 + tuned signals over Sourcegraph's code-search index) with semantic embeddings, explicit @-mention control, and OpenCtx connectors (Slack, Notion, Linear); Autocomplete deliberately avoids embeddings entirely (latency budget), using Jaccard similarity over recently opened files + Tree-sitter structural parsing + Reciprocal Rank Fusion. Label: **Corroborated** (same teardown). Lesson: one retrieval pipeline for all features is a trap — latency budgets differ, so the architectures must differ.
- Claim: Continuous re-indexing architecture: indexes every repository across every connected code host, keeps them fresh, enforces role-based access control and per-repository include/exclude filters *at retrieval time*; runs in production at 300,000+ repos and 90GB+ monorepos. Label: **Corroborated** — Sourcegraph blogs (2024-06-04, 2024-06-25) via finance-research synthesis.
- Claim: Access control is a first-class part of the retrieval layer, not a downstream filter. Label: **Corroborated** (same). Lesson: for enterprise RAG, permission-aware retrieval is the moat — post-filtering leaks and breaks pagination.

### Product discovery
- Claim: Sourcegraph bet that code *search* (understanding where things are) was the unsolved enterprise problem, then rode that infrastructure into AI assistance — the retrieval-first architecture is why Cody differentiates on multi-repo context vs Copilot's open-file context. Label: **Inferred** from consistent secondary framing; no Sourcegraph strategy doc fetched — Unknown primary.

### Business outcomes
- Claim: Cody moved to enterprise-only in 2026 (free and self-serve Pro tiers retired) — a strategic retreat from individual developers toward large orgs. Label: **Corroborated** — awesome-vibe-coding tooling notes, 2026. Interpretation: the retrieval moat pays off in enterprises with sprawling codebases, not with individuals — the business followed the architecture's strength.
- Claim: Third-party evaluations credit Cody with 60% faster migration speed at customers like Reddit and FactSet. Label: **Corroborated** (technewsdaily, 2026); vendor-adjacent — treat as Medium-low.

### Documented failures
1. None located this pass. The strategy pivot (enterprise-only) reads as a business correction, not an engineering postmortem. Label: **Unknown** for engineering postmortems.

### Transferable lessons
- Different latency budgets → different retrieval architectures; don't unify prematurely. Label: **Corroborated**.
- Enforce access control at retrieval time, not as a post-filter. Label: **Corroborated**.
- Threshold + token-budget cutoffs beat fixed top-k for prompt construction. Label: **Corroborated**.
- A decade of unsexy infrastructure (code search indexing) can become the AI moat — compound on boring capabilities. Label: **Inferred**.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| SO-01 | Cody Context Engine teardown (two-stage, per-feature strategies) | https://github.com/dhruvmakwana/rag-deep-dive/blob/HEAD/docs/case-studies/sourcegraph-cody.md | Secondary (technical teardown) | dhruvmakwana | 2026 | 2026-10-10 | Medium |
| SO-02 | Continuous reindexing, 300k repos, RBAC at retrieval | https://github.com/katsuyaito/indx-autoresearch-financeaiready/issues/388 | Secondary (research synthesis) | katsuyaito | 2026 | 2026-10-10 | Medium |
| SO-03 | Enterprise-only pivot 2026 | https://github.com/awesome-vibe-coding/awesome-vibe-coding/blob/HEAD/content/tools/sourcegraph-cody.md | Secondary (tooling notes) | awesome-vibe-coding | 2026 | 2026-10-10 | Low-medium |
| SO-04 | Cody vs Qodo comparison, context claims | https://www.augmentcode.com/tools/sourcegraph-cody-vs-qodo | Secondary (vendor comparison) | Augment Code | 2026 | 2026-10-10 | Low |

## Narrative audit (retrofit 2026-10-10)
- **The enterprise-only pivot is the real postmortem.** Sourcegraph killed its cloud product and went enterprise/self-hosted only — the public telling is "focus," but the receipt is that *code search as a small-team product didn't monetize*. "Code search for everyone" became "code search for companies with procurement departments." The mission narrowed to fit the revenue, not the reverse.
- **Cody and the AI-chasing question.** The AI assistant pivot followed the market hype cycle precisely. The audit doesn't claim cynicism — code search *is* the natural substrate for code AI — but notes the timing coincides with the funding climate, and enterprise-only distribution constrains exactly the individual developers who'd evangelize it.
- **Open source as funnel, not faith.** The core is public; the enterprise features aren't. The open code is the top of the sales funnel — a legitimate model, just not the old "free software" ethos. Don't mistake one for the other.
