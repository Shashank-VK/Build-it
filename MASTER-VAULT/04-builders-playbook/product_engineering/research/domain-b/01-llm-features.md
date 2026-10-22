# Domain B — 01: LLM-Powered Product Features

> Scope: customer-facing products that embed LLM capabilities as features (not AI used to *build* software — that is Domain A). Research date: 2026-10-10. Read-only research; nothing here is an install/build/recommend instruction.

## 1. What "LLM-powered feature" means in a product

**Plain English:** A product feature is LLM-powered when a user's request is sent, at runtime, to a language model and the model's output becomes part of the product experience — an answer, a draft, a summary, a generated image, a ranked list. The product team does not own the model's weights; they own everything around it: prompts, context assembly, validation, UI, cost, and the fallback when the model is wrong.

**Concrete example:** Notion AI's database agents. Notion's engineering team describes a "brain vs. body" architecture: the LLM is the *brain* (interprets what the user wants), while deterministic Notion Workers are the *body* (execute the actual database operations as code). The LLM never writes rows directly — it translates intent, and code does the mutating. This separation is the central engineering pattern for reliable LLM features: reasoning is probabilistic, execution is deterministic.

**Deeper mechanics:** The reason teams split brain/body is that LLM output cannot be trusted for exact operations (wrong field names, invented IDs, off-by-one logic). Constrained decoding (e.g., OpenAI's structured outputs, strict JSON mode, 2024) guarantees *syntactic* conformance — valid JSON matching a schema — but *semantic* errors (wrong values, invented entity names) still require a validation layer. The industry pattern is: LLM proposes → code validates → code executes → LLM narrates.

## 2. Real product cases

### 2.1 Duolingo Max (education, launched March 2023)

- **What it is:** Premium tier with two AI features: *Explain My Answer* (contextual explanation of why an answer was right/wrong) and *Roleplay* (simulated conversations — ordering coffee in Paris — with feedback). Later expanded with a Video Call with a live AI character.
- **Model selection:** Built with OpenAI starting Sept 2022; GPT-4. Duolingo's launch materials say the collaboration involved training the model for their use case, adding safety guardrails, verifying explanation accuracy, and tuning prompts — i.e., post-training + prompt work, not training a foundation model.
- **Business outcome:** Subscription revenue grew ~50% in 2024 to $607M; paid subscribers 10.3M by Q1 2025. Duolingo English Test uses AI for question generation, scoring, and test security.
- **Negative evidence within the same company:** In April 2025 the CEO declared the company "AI-first," requiring teams to prove AI *couldn't* do a job before getting headcount — a controversial org move that shows the same company can succeed with an AI *product feature* while its AI *workforce policy* generates backlash. Keep product-feature success and org-automation controversy separate.
- **Evidence:** primary technical (company launch press release via GlobeNewswire, March 2023); secondary interpretation (Medium case study, July 2026). Accessed 2026-10-10. Confidence: **Corroborated** — revenue figures reported by company, repeated across outlets; the "trained for our use case" detail is vendor-framed.

### 2.2 Notion AI — simplification beat sophistication

- **What happened:** Notion's engineers first tried advanced code generation, complex schemas, and heavy instruction prompts for agentic features. Trial and error taught them simpler prompts, human-readable representations, and minimal abstraction *improved* model performance. Their customizable AI agents (V3, Sept 2025) became, per their AI engineering lead, the most successful AI tool they've shipped — described as a "step function improvement" in usage.
- **Engineering implication:** Prompt/model complexity is not monotonically better. Simpler, more legible representations often win — consistent with the broader practitioner rule "if accuracy plateaus, the next lever is retrieval, decomposition, a stronger model, or narrowing the feature — not a fifteenth rewording."
- **Evidence:** secondary interpretation (VentureBeat, ~2026, interview with Notion AI engineering lead Ryan Nystrom). Accessed 2026-10-10. Confidence: **Corroborated** (multiple outlets covered the same interview; usage claim is company-reported).

### 2.3 Intercom Fin — custom small model for support (Fin Apex 1.0)

- **What it is:** Fin is Intercom's AI support agent; in 2026 the company built its own post-trained model, Fin Apex 1.0, instead of renting frontier models.
- **Claimed results:** 73.1% resolution rate vs ~71% for GPT-5.4/Claude Opus 4.5 on Intercom's internal benchmark; 65% hallucination reduction vs Claude Sonnet 4.6; 3.7s response time; ~1/5 the inference cost of frontier models. Runs 12,000+ customers, $0.99 per resolved outcome, ~76% average resolution (vendor-reported; independent case studies cited by competitors put real-world figures at 42–50% — **marketing-vs-measured gap**).
- **Corporate note:** Intercom renamed itself Fin (May 2026); Salesforce agreed to acquire it for ~$3.6B (June 2026, not yet closed).
- **Engineering implication:** For a narrow, high-volume task (support resolution), a purpose-trained small model can beat frontier models on task metrics *and* cost. Model selection is task-shaped, not leaderboard-shaped. The resolution-rate definition differs per vendor — headline numbers are not comparable.
- **Evidence:** primary technical (company benchmarks via VentureBeat, ~March 2026); community observations (competitor comparisons). Accessed 2026-10-10. Confidence: **Corroborated** on product/pricing facts; **Inferred** on benchmark independence (company-run, not third-party).

### 2.4 Salesforce Einstein / Agentforce (adjacent note)

- Agentforce (Salesforce's agent platform) absorbed Fin via acquisition. This is a Domain B product (AI agents sold as enterprise software) — covered further in 07 and 11.

## 3. Model selection patterns (cross-product)

| Pattern | Example | Why |
|---|---|---|
| Frontier API model, prompt-tuned | Duolingo Max (GPT-4) | Fastest to market; good for open-ended generation |
| Purpose-trained small model | Fin Apex 1.0 | Narrow task + huge volume → cost and latency win |
| Fine-tuned partner model | Klarna (fine-tuned OpenAI, Feb 2024) | Domain tone + 35 languages |
| Multi-model routing | Glean (Gemini, Claude, GPT mix) | Task-matched selection |
| Cascaded: small first, escalate | General cost practice (see 09) | 40–70% savings on routed requests |

**Training/fine-tuning data:** Products rarely disclose training data. What is public: Duolingo used its curriculum data + prompt tuning; Klarna fine-tuned on support conversations; Fin Apex was post-trained on "billions of customer-experience interactions" (company claim, unverifiable). **Unknown:** exact datasets, sizes, and eval splits for all three — vendors do not publish them.

## 4. How teams present AI features (UX surface)

- **Labeled and bounded:** Duolingo presents Roleplay as a character scenario, not an oracle. Notion shows AI output as editable blocks, never authoritative.
- **Citations:** Glean/Perplexity-style answers link to source documents — the "show the receipts" pattern.
- **Uncertainty display:** Confidence buckets (Confident / Unsure / Needs review); probabilistic phrasing; "I don't know" as a designed first-class response.
- **Human-in-the-loop for consequential actions:** draft-then-approve; approval gates before sends/refunds/deletes.
- Detail in 03 (assistants) and 10 (ops).

## 5. Key engineering lessons

1. **The model is not the product.** The product is prompts + retrieval + validation + execution + UX + evals + ops. Teams that treat "call the API" as the feature ship the failure modes in section 10.
2. **Narrow the feature before enlarging the model.** Klarna and Fin both succeeded by scoping to routine queries and escalating the complex tail to humans.
3. **Simplification can be the breakthrough** (Notion).
4. **Vendor metrics are not comparable** (Fin's 76% vs 42–50% in the wild; definitions of "resolution" differ).

## 6. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date (approx) | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Duolingo Max launched Mar 2023 with Explain My Answer + Roleplay; built with OpenAI from Sept 2022 | https://www.globenewswire.com/news-release/2023/03/14/2627053/0/en/index.html | primary technical / Duolingo | 2023-03-14 | 2026-10-10 | Verified | primary technical |
| Duolingo subscription revenue +50% 2024 to $607M | https://medium.com/insightful-data-stories/the-duolingo-case-study-how-to-launch-ai-without-breaking-your-brand-91e195176775 | secondary interpretation / Kay J | 2026-07-17 | 2026-10-10 | Corroborated | secondary interpretation |
| Notion AI: simple prompts beat complex schemas; V3 agents most successful AI tool | https://venturebeat.com/infrastructure/why-notions-biggest-ai-breakthrough-came-from-simplifying-everything | secondary / VentureBeat (interview) | 2026 | 2026-10-10 | Corroborated | first-hand practitioner (via interview) |
| Fin Apex 1.0: 73.1% resolution, 1/5 cost, beats frontier on internal bench | https://venturebeat.com/technology/intercoms-new-post-trained-fin-apex-1-0-beats-gpt-5-4-and-claude-sonnet-4-6 | secondary / VentureBeat | ~2026-03 | 2026-10-10 | Corroborated (company-run bench) | corroborating |
| Fin pricing $0.99/outcome; ~76% vendor-reported vs 42–50% independent | https://pluno.ai/blog/intercom-fin-ai-vs-ada | secondary / Pluno (competitor) | 2026-10 | 2026-10-10 | Inferred gap | community observations |
| Salesforce to acquire Fin ~$3.6B, June 2026 | https://www.liveagent.com/blog/liveagent-vs-intercom-fin-ai-chatbot-comparison/ | secondary / LiveAgent | 2026 | 2026-10-10 | Corroborated | corroborating |

**Gaps / Unknowns:** exact training datasets for Fin Apex, Klarna fine-tune, Duolingo prompt-tune; per-feature inference cost for any of the three; independent reproductions of vendor benchmarks.
