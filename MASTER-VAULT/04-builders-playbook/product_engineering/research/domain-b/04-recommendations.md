# Domain B — 04: Recommendation and Ranking Systems

> Scope: products whose core value is personalized ranking/recommendation (feeds, homepages, "for you" rows). This is the oldest production-AI product category — pre-LLM, but now absorbing LLMs. Research date: 2026-10-10.

## 1. The canonical architecture (plain English → mechanics)

**Plain English:** No model can score ten million items in a tenth of a second, so recommenders work as a *funnel*: cheap fast models shrink the pool, expensive careful models pick the winners, and business rules clean up the result.

**Concrete example:** You open TikTok. In under ~50–100ms the system filters ~100M candidate videos to ~50 shown. It does this in three stages:

1. **Retrieval / candidate generation (~10ms):** pull ~500 roughly-matching items using ANN (approximate nearest neighbor) search over embeddings — optimized for *recall* (don't miss good stuff).
2. **Ranking (~30ms):** a heavyweight neural model scores those ~500 with hundreds of features each — optimized for *precision*.
3. **Re-ranking (~10ms):** enforce diversity (not five thrillers in a row), freshness, exploration, sponsored slots, and business rules.

**Deeper mechanics:** Retrieval usually uses *two-tower* neural networks — one tower embeds the user (history, context), the other embeds items; candidates are found by vector similarity (this is the design YouTube popularized at scale). The ranker is typically a deep multi-task model predicting several objectives at once (click, watch time, completion, satisfaction). Training data is implicit feedback: plays, abandons, dwell, skips, rewinds, thumbs — not star ratings. The pivotal trade-off is *quality vs. serving latency, mediated by funnel width at each stage*. Supporting infrastructure: feature stores (kill training-serving skew), streaming feature pipelines (Flink/Kafka), ANN indexes (Faiss/ScaNN), and experimentation platforms running hundreds of concurrent A/B tests.

## 2. Netflix — the deepest public case

- **The stack (composite from Netflix engineering posts, 2015–2023):** multi-retriever fan-out (collaborative filtering, content-based, two-tower neural, similar-to-recent, popularity) → candidate union → multi-objective ranker → diversity/business-rules/bandit post-processing → personalized rows on every surface (home, search, push, trending).
- **Three load-bearing decisions:** (1) personalization at *every* surface, not just home; (2) multi-objective ranking — optimizing only click probability produces clickbait, so they optimize completion, watch time, post-watch satisfaction, and session balance; (3) causal experimentation as infrastructure — hundreds of A/B tests in flight, with statistical machinery for overlap.
- **Training signals:** watch/complete/abandon, pause/rewind, thumbs, watchlist adds, searches, time-of-day, device, even re-watched scenes. Netflix has stated personalization is worth >$1B/year in retention value; YouTube reports ~70% of watch time comes from recommendations.
- **GenRec (2026, Netflix Tech Blog):** Netflix's LLM-native ranker. Off-the-shelf LLMs fail as recommenders — they over-recommend popular items, hallucinate out-of-catalog items, ignore business constraints, and personalize weakly. Netflix's answer: take an internal foundation LLM, do domain-adaptation training on Netflix data (stable, infrequent), then post-train for ranking with reward signals (frequent). User histories and item metadata are verbalized as text prompts; the model runs on vLLM in prefill-only mode and scores catalog items. Result: matches or exceeds the mature production system with far fewer labeled examples and input signals.
- **Why it matters for Domain B:** even the most mature classical recommender org is moving rankers to LLMs — but *as rankers over a closed catalog with constrained outputs*, not as open-ended chatbots. The catalog constraint is what makes it safe.
- **Evidence:** primary technical (Netflix Technology Blog — GenRec post by Ying Li, Arjun Rao, Shradha Sehgal; classic "Beyond the 5 stars" posts); secondary synthesis (systems-design deep dives). Accessed 2026-10-10. Confidence: **Verified** on architecture and GenRec's existence/design; **Corroborated** on the $1B/70% figures (company-reported, widely repeated).

## 3. TikTok / YouTube / Spotify — the pattern holds

- **TikTok:** the canonical real-time recommender — every scroll/pause/skip immediately reshapes the session via streaming features; two-tower retrieval with multiple parallel retrieval paths; frozen item embeddings with real-time-adjustable user/context embeddings.
- **YouTube (2016 deep neural recommender):** the paper/system that established two-tower retrieval + deep ranker as the industry template; the shift from clicks to watch time as the objective "quietly changed every piece of media on Earth" (watch-time optimization rewards retention-shaped content).
- **Spotify:** playlist continuation via two-tower encoders (the Google Cloud tutorial uses the Spotify Million Playlist Dataset as the worked example); same funnel architecture.
- **Evidence:** primary technical (Google Cloud blog on two-tower retrieval; YouTube's published system descriptions); secondary (engineering handbooks). Accessed 2026-10-10. Confidence: **Corroborated**.

## 4. Training/fine-tuning data (what's public)

- **Implicit feedback at massive scale** is the training data: billions of interaction events, not human labels. Labels are *derived* (did they finish? rewatch?).
- **Cold start** is the structural weakness: new users/items have no history → fall back to popularity, content features, or exploration (contextual bandits, epsilon-greedy).
- **What vendors don't disclose:** exact feature lists, model sizes, retraining cadence, or per-surface objective weights. Netflix's GenRec post is unusually open about *method* while disclosing no weights or data.

## 5. Evaluations

- **Offline:** precision/recall, NDCG, held-out interaction prediction. Known gap: *offline wins often don't move online engagement* — the metric that matters is the A/B test on retention/watch time.
- **Online:** interleaving and A/B tests with causal inference; guardrail metrics (diversity, creator equity, harmful-content rates).
- **LLM rankers:** evaluated on ranking quality vs. the production baseline with far fewer labels — GenRec's headline result.
- **Negative evidence:** optimizing a single objective (clicks) produces clickbait; popularity bias; filter-bubble/rabbit-hole dynamics (variable-reward schedules that maximize time-spent raise well-documented wellbeing concerns — a product-safety dimension, not just a quality one).

## 6. Latency, cost, reliability

- **Latency:** the funnel exists because of the ~100–200ms budget; every stage has a width knob that trades quality for milliseconds.
- **Cost:** recommenders are among the cheapest AI per request (small specialized models, heavy caching, precomputation) — the opposite economics of LLM chat. LLM rankers (GenRec) change this: prefill-only scoring on vLLM is the cost-control move.
- **Reliability:** deterministic models, versioned features, and the experimentation platform *is* the safety system — bad models are caught by A/B guardrails, not by prompt review.

## 7. Security

- **Data leakage:** interaction histories are sensitive; embedding stores and logs need access control. (Less prompt-injection surface than LLM chat — the attack surface is training-data poisoning and feedback-loop manipulation, e.g., brigading.)
- **Manipulation:** fake engagement can shift rankings; integrity teams and anomaly detection sit beside the ranker.

## 8. UX: how recommendations are presented

- **Explainability as trust:** "Because you watched X" rows; thumbs up/down that visibly retune the feed.
- **Control:** "not interested," "don't recommend," topic controls — the user-facing levers that make a black-box ranker feel governable.
- **The rabbit-hole problem:** the same real-time adaptation that delights can trap; progressive disclosure of "why am I seeing this" is the honest UX answer.

## 9. Domain boundary note

Recommenders are Domain B's *classical* wing: products built *using* ML/AI where the AI is the product engine. They differ from LLM features in failure modes (no hallucinations — a ranker can't invent an item if the catalog constrains it; GenRec's catalog-scoring design exists precisely to prevent that) and in economics (cheap per-request, expensive to build). See file 11.

## 10. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Recommender funnel: retrieval (~10ms) → ranking (~30ms) → re-rank; two-tower + ANN | https://dev.to/danielsamfdo/the-10-millisecond-trick-how-recommenders-search-millions-of-items-before-you-blink-4dkp | practitioner / DEV | 2026-10 | 2026-10-10 | Corroborated | corroborating |
| Netflix: multi-retriever fan-out, multi-objective ranker, experimentation at scale | https://github.com/lourdhu02/systems-design/blob/HEAD/14-case-studies-deep-dives/netflix-recommendations-deep-dive.md | secondary synthesis | 2026-09 | 2026-10-10 | Corroborated | secondary interpretation |
| Netflix GenRec: LLM-backed ranker, post-trained, matches/exceeds production with fewer labels | https://noise.getoto.net/author/netflix-technology-blog/ (syndicated from netflixtechblog.com) | primary technical / Netflix (Li, Rao, Sehgal) | 2026 | 2026-10-10 | Verified | primary technical |
| Two-tower retrieval on Google Cloud; Spotify playlist example | https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture | primary technical / Google Cloud | ~2023 | 2026-10-10 | Verified | primary technical |
| TikTok real-time feedback loop; multi-stage serving at ms latency | https://www.linkedin.com/pulse/anatomy-large-scale-recommender-systems-jo-kristian-bergum-a3eef | practitioner / J.K. Bergum | 2025-01-20 | 2026-10-10 | Corroborated | first-hand practitioner |

**Gaps / Unknowns:** exact Netflix/YouTube/TikTok model architectures and objective weights (proprietary); GenRec's training data composition and serving cost; independent replication of GenRec's "matches production" claim.
