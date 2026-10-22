# Domain B — 09: Cost, Latency, and Reliability

> Scope: inference economics, latency engineering, and reliability practices for AI products. Research date: 2026-10-10.

## 1. Cost — inference economics (plain English → mechanics)

**Plain English:** Every LLM call costs money per token — input tokens (what you send, including the whole conversation history re-sent each turn) and output tokens (what the model writes, usually priced higher). A chat feature's bill is: tokens per request × requests × price. Agent loops multiply it: 10 tool-call turns = 10× the tokens, plus history growth.

**Concrete example:** A support agent handling 12,000 sessions/day. A template change adds 60 output tokens per call and triggers a second model call on 15% of sessions (800 input tokens each). At $10/M output and $2.50/M input tokens, that's $7.20 + $3.60 = ~$10.80/day in added cost from one template edit — small, but the *method* (multiplying deltas by volume) is how cost postmortems are actually written. The real danger is the runaway: the $63/31M-token overnight loop (see 07) — no ceiling, no alert, just a morning invoice.

**Deeper mechanics:** Andreessen Horowitz's widely-cited framing: AI inference is the single largest line item in the AI application stack once you scale past prototype. Costs compound because (a) usage grows faster than per-token prices fall, (b) conversation history is re-sent every turn, (c) agent loops multiply calls, and (d) long contexts (RAG) inflate input tokens.

### 1.1 The cost-optimization stack (ordered by effort)

| Technique | Typical saving | Complexity | Notes |
|---|---|---|---|
| Prompt caching (prefix) | 60–90% on cached tokens | Low | Same system prompt reused across requests; providers discount heavily |
| Batch APIs | 50% flat | Low | For anything tolerating delay (offline evals, bulk extraction) |
| Output length control | 15–30% on output | Low | Cap max_tokens; ask for concise formats |
| Model routing | 40–70% on routed requests | Medium | Easy requests → small model; hard → frontier; requires a router + evals of the router |
| Semantic caching | 31–47% fewer LLM calls | Medium | Embedding-keyed cache for FAQ-like traffic; tune similarity threshold + TTL or get stale/wrong hits |
| Context compression | 20–40% on input | Medium | Top-k RAG trimming, history summarization |
| Quantization (self-host) | 30–60% on compute | High | INT8/INT4 with small quality loss on many tasks |
| OSS models for narrow tasks | 70–95% on targeted workloads | High | Only where the narrow task is well-eval'd; broad tasks degrade and rework eats the savings |
| Distillation | varies | High | Train small model on big model's outputs for a narrow task |

**The sequencing rule:** instrument first (you can't cut what you can't see — cost attribution per team/feature is the prerequisite), then caching, then routing, then model substitution. Every optimization risks quality — evaluate before/after each change; never trade correctness for cents blind.

### 1.2 Real cost cases

- **Fin Apex (Intercom):** purpose-trained small model runs at ~1/5 the inference cost of frontier models at *higher* task resolution — the strongest public evidence that task-shaped models beat frontier economics at volume.
- **Perplexity Photon + Fast preset:** −68% model-plus-search cost per task at comparable quality — but the win came from *retrieval infrastructure*, not model choice.
- **Extraction pipeline:** −85–93% per-document cost via adaptive field selection + tiered per-field routing + field-level caching (see 05).
- **The $63 loop:** the canonical "no ceiling" failure — cost controls (spend/token ceilings per trigger, alerts on repeated states) are reliability controls.
- **Cheapest token:** "the cheapest token of all is the one you never send — some features are better served by plain software than a model call."
- **Evidence:** practitioner (CloudZero, DEV, NeuralTrust, interview-prep synthesis). Accessed 2026-10-10. Confidence: **Corroborated** on techniques; **Inferred** on exact percentages generalizing (workload-dependent).

## 2. Latency (plain English → mechanics)

**Plain English:** Users feel *time to first token* (how fast something starts appearing) more than total time. Streaming (tokens appearing as generated) changes *perceived* latency, not cost. For voice, sub-second response is the bar; for chat, a few seconds; for agents doing 10 tool calls, the budget explodes.

**Concrete example:** If one LLM call's p95 is 2s, a three-step agent chain's p95 is 6–8s — tail latencies *add*. Tracking span hierarchies (which call in the chain was slow) is non-negotiable; per-call averages hide the session that fanned out into 40 calls.

**Deeper mechanics:** the two latencies that matter are TTFT (time to first token — perceived responsiveness) and TPOT (time per output token — total duration). Levers: streaming (TTFT), smaller/faster models (both), prompt caching (TTFT on long prompts), parallel tool calls (wall-clock, not tokens), prefill-only scoring (GenRec), and infrastructure (Phot
on's io_uring + compact formats took p99 from ~1.2s to 230ms p95). Voice: native speech-to-speech removes two pipeline hops (see 06).

### 2.1 Latency budgets by surface (practitioner norms)

| Surface | Budget | Notes |
|---|---|---|
| Voice agent turn | <800ms–1s | Feels conversational; streaming mandatory |
| Chat response | 2–4s (Fin Apex: 3.7s) | Streaming makes 4s tolerable |
| RAG Q&A | p99 < 2s | Retrieval is usually the long pole |
| AI search call | 160ms p50 / 230ms p95 (Perplexity Fast) | Infrastructure-dominated |
| Recommender funnel | 50–200ms total | The funnel architecture exists for this |
| Agent multi-step task | 10s–minutes | Set expectations; show progress legibly |

### 2.2 What teams get wrong

- "Average latency describes UX" — false; tail latency and time-to-first-*meaningful*-output matter more.
- "Streaming reduces cost" — false; it only improves perceived latency.
- "Token count equals cost" — not by itself; pricing varies by provider, model, token category, caching, and modality.

## 3. Reliability

### 3.1 The reliability stack

1. **Deterministic first:** validate everything (schemas, ranges, entity existence); never let unvalidated model output into a privileged operation.
2. **Defined failure paths:** retry once with a repair instruction → fall back to a deterministic path → surface an honest error. Every LLM call needs the same four answers as any network dependency, plus one more: *what happens when it returns successfully but wrongly?*
3. **Fallback chains:** primary → smaller model → cached response → rule-based fallback → honest "unavailable." (E.g., GPT-4o → GPT-4o-mini on rate limit.)
4. **Timeouts, retries with backoff, circuit breakers** at the API-client layer.
5. **Iteration caps** on every agent loop (the single most important agent reliability measure).
6. **Idempotency and state rollbacks** for multi-step mutations.

### 3.2 What reliability means per product type

- **LLM features:** schema validation + fallbacks; quality signals as drift detectors.
- **RAG:** the failure is silent wrongness → reliability = evals + quality monitoring + fresh indexes.
- **Assistants/agents:** layered guardrails + approval gates + kill switches + human escalation (see 07).
- **Recommenders:** deterministic models + A/B guardrails; bad models caught by experimentation, not review.
- **Voice:** per-modality health checks, circuit breakers, graceful degradation (see 06).

### 3.3 Monitoring (the four pillars)

Monitor **quality, performance, cost, reliability** simultaneously, per prompt/model version: inputs, outputs, model + prompt version, retrieved context, latency percentiles, token usage, cost, refusal/fallback/format-violation rates, user feedback (thumbs, regenerates, edits, copy rate). Alert thresholds (practitioner norms): cost >2× baseline; p95 latency >3× p50; error rate >2%; format violations >0.5%; sudden content-policy spikes (possible attack). Weekly: manually review a 1–5% random sample of production outputs. Quarterly: red-team for safety/injection.

## 4. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Inference is the largest AI-app cost line past prototype; gateway controls | https://neuraltrust.ai/blog/ai-gateway-llm-cost-optimization | vendor-practitioner / NeuralTrust | 2026-09 | 2026-10-10 | Corroborated | corroborating |
| Optimization stack + savings ranges + sequencing (instrument → cache → route → substitute) | https://www.cloudzero.com/blog/llm-cost-optimization/ | practitioner / CloudZero | 2026-10-01 | 2026-10-10 | Corroborated | first-hand practitioner |
| Routing 80/20 small/large → ~72% savings (worked example) | https://github.com/sanigam/ai-ml-interview-prep/blob/HEAD/43_LLM_Inference_Optimization/LLM_Inference_Optimization.md | practitioner synthesis | 2026-05 | 2026-10-10 | Inferred (illustrative math) | community observations |
| p95 chains add; span hierarchies non-negotiable; $3/100-Q eval suite | https://mehaisi.com/blog/llm-observability-tracing-and-evals | practitioner | 2026-08 | 2026-10-10 | Corroborated | first-hand practitioner |
| Monitoring thresholds; fallback chains; weekly 1–5% audits; quarterly red-teams | https://github.com/snowdreamtech/frp/blob/HEAD/.agent/rules/llm-prompt.md | practitioner ruleset | 2026-09 | 2026-10-10 | Corroborated | community observations |
| Photon: p99 1.2s → 230ms p95 via infra work | https://www.perplexity.ai/hub/blog/photon | primary technical / Perplexity | 2026-09-24 | 2026-10-10 | Verified | primary technical |

**Gaps / Unknowns:** any named product's actual inference bill (nobody publishes); the true distribution of cost across techniques in production (percentages are practitioner-reported ranges); reliability SLOs for assistants (no vendor publishes an AI-quality SLO, only uptime SLAs like Fin's 99.8%).
