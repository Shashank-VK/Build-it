# Domain B — 08: Evaluations — How Teams Measure AI Product Quality

> Scope: eval harnesses, benchmarks, human evaluation, and regression practices for AI *products* (features, assistants, RAG, agents). Research date: 2026-10-10.

## 1. Why evals exist (plain English → mechanics)

**Plain English:** Traditional software tests check "does the code do exactly X." AI features are non-deterministic — the same input gives different outputs on different days — so you can't assert exact strings. Evals are the replacement: a curated set of test cases with known-good answers, run automatically every time anything changes, scored by rules, models, or humans.

**Concrete example:** A team ships a support agent. A prompt tweak that "seemed promising" caused a 15% regression on architecture questions — discovered *weeks later* from user complaints, because nothing measured quality automatically. The post-incident fix: an eval harness with regression detection, run in CI on every prompt change. (This is the AKR-Evals origin story; the team estimated $200K+ impact from the silent regression.)

**Deeper mechanics:** Eval scores are noisy (the model is stochastic), so serious harnesses use statistical comparison with confidence intervals, not point estimates. The eval set must include happy paths *and* adversarial paths (known failure modes). And you never optimize against the full set — keep a 20–30% holdout split you never look at during development, or you overfit the prompt to the test.

## 2. The eval stack (layers)

### 2.1 Golden datasets

- **What:** 50–1,000+ curated input/output pairs with validated correct answers, versioned like code (never silently change expected outputs — document why, like a schema migration).
- **How built:** sample real user queries from production logs → domain experts write/validate answers → include edge cases, failure modes, adversarial examples → grow it from every production incident ("add the failing input to the eval set").
- **Size guidance (practitioner consensus):** 50–100 minimum viable; 200–500 good coverage; 1,000+ comprehensive with holdout splits.
- **The rule:** your eval is only as good as your golden dataset. Garbage in → misleading scores out. Picking a tool before hand-writing real test cases is the biggest first mistake — the dataset is ~90% of the problem.

### 2.2 Deterministic checks (~60% of the scoring mix)

- Exact match (classification, extraction), schema validation, regex/keyword assertions, BLEU/ROUGE for summarization, embedding similarity, refusal-rate and format-violation rates.
- These are cheap, fast, and non-noisy — use them wherever the criterion is checkable without judgment.

### 2.3 LLM-as-judge (~30%)

- **What:** a strong model (GPT-4o/Claude-class) scores outputs against rubrics (faithfulness, answer relevance, tone) — typically correlating with human judgment 80–85%.
- **Cost:** ~$0.02–0.05 per evaluation call; a 100-question suite ≈ $3 — "the cheapest insurance against a catastrophic prompt regression."
- **Mandatory calibration:** run the judge against human-scored examples first; if it disagrees >20% of the time, fix the judge prompt. Countermeasures for judge bias: swap positions, multiple judges, diverse models. Never rely on LLM-as-judge alone — it stacks judge inconsistency on top of system inconsistency.
- **RAGAS-style metrics** for RAG: faithfulness (is the answer supported by retrieved context?), answer relevance, context precision/recall — measuring retrieval and generation *separately*.

### 2.4 Human evaluation (~10%, but load-bearing)

- **Uses:** calibrating judges, final acceptance before major deploys, nuanced criteria (tone, empathy, creativity), and the 1–5% weekly random-sample audit of production outputs.
- **Why it can't be skipped:** user feedback (thumbs up/down) is sparse and biased by expectations and UI; only deliberate human review establishes the reference standard.
- **Production-to-eval loop:** mine failed/low-rated production traces → add to the golden dataset → LLM-as-judge in CI on every PR. This is how evals stay representative of real traffic instead of fossilizing.

## 3. Evals in CI and deployment gates

- **The gate:** run the golden suite on every prompt/model/retrieval/tool change; block deployment if any category drops beyond threshold (practitioner norms: 5% tolerance on quality, zero tolerance on safety and format compliance; use statistical significance for noisy evals, n>30).
- **The pipeline (minimum for production):** golden dataset → offline eval on every change (RAGAS faithfulness + relevance) → regression gate (deploy only if score ≥ baseline − ~3%) → online: judge-sample ~10% of live queries → track user feedback → feed failures back into the dataset.
- **Tooling landscape (2026):** Promptfoo (CI checks), Braintrust (PM-friendly review + regression tracking), LangSmith/Langfuse/Arize (tracing + online evals), Galileo (own small models for fast evals), RAGAS/G-Eval (metrics), DSPy (prompt optimization against eval sets), plus OTel-native options (Laminar, Langtrace, OpenLIT).
- **Shadow/canary:** run new prompt versions on live production traffic without returning results; compare quality metrics between variants behind a flag before full release.

## 4. What good eval culture looks like (vs. bad)

| Good | Bad |
|---|---|
| Evals run in CI on every prompt change | "It looked fine in the playground" |
| Golden dataset grows from production incidents | Static 20-question set from launch week |
| Judge calibrated against humans | Uncalibrated LLM-as-judge as the only signal |
| Retrieval and generation measured separately | One blended score hides which layer broke |
| Holdout split; no prompt-tuning against full set | Overfit prompt that aces the eval, fails users |
| Quality signals monitored in production (regenerate rate, edits, thumbs-down) | Dashboard green while users get garbage (see 02) |

## 5. Benchmarks vs. product evals

- **Public benchmarks** (MMLU, HotpotQA, tau-bench, MCP-Universe, Artificial Analysis Search Index) are useful for *model/tool selection* and for sanity-checking vendor claims.
- **They do not replace product evals:** generic benchmarks often don't correlate with production performance. Always build the domain-specific benchmark (50–200 questions with ground truth) for the actual task, users, and risk profile.
- **Vendor benchmarks** (Fin Apex's 73.1%, Perplexity's Photon numbers) are company-run; treat as *corroborating*, not *verified*, until independently reproduced.

## 6. Negative evidence about evals themselves

- **Silent regressions are the norm without evals:** the AKR case (15% regression found weeks later, $200K+ impact) and the healthcare RAG case (94% → 38% failure) both trace to "no systematic quality measurement."
- **Judge bias:** position bias, verbosity bias, self-preference — uncalibrated judges *create* false confidence.
- **Eval rot:** datasets fossilize while traffic shifts; without the production-to-eval loop, evals measure last year's product.
- **Metric gaming:** optimizing a vendor-defined "resolution rate" or a single offline metric produces Goodhart failures (see Klarna: great efficiency metrics, eroding trust).

## 7. Per-finding metadata (selected)

| Claim | URL | Source type / author | Pub date | Accessed | Confidence | Evidence class |
|---|---|---|---|---|---|---|
| Silent 15% regression → AKR-Evals harness; $200K+ impact claim | https://github.com/rbabbell/akr-evals | primary technical | 2026-04 | 2026-10-10 | Corroborated (self-reported impact) | primary technical |
| Production-to-eval loop; judge correlates 80–85% with humans; $3 per 100-Q suite | https://mehaisi.com/blog/llm-observability-tracing-and-evals | practitioner | 2026-08 | 2026-10-10 | Corroborated | first-hand practitioner |
| Scoring mix ~60/30/10; dataset is 90% of the problem; never judge-alone | https://www.explainx.ai/blog/ai-evals-for-engineers-and-pms-explained-2026 | practitioner synthesis | 2026-10-01 | 2026-10-10 | Corroborated | corroborating |
| Golden dataset practices; holdout; regression gates; calibrate judges | https://github.com/hareli26/claude-exam-prep/blob/HEAD/subjects/evals.md | practitioner handbook | 2026-04 | 2026-10-10 | Corroborated | corroborating |
| Min production eval pipeline: golden → offline → gate → online 10% → feedback loop | https://github.com/gerfru/dev-best-practices/blob/HEAD/plugins/dev/skills/design-llm/references/evaluation-framework.md | practitioner reference | 2026-09 | 2026-10-10 | Corroborated | corroborating |
| Observability tooling landscape (Langfuse, Braintrust, Galileo, etc.) | https://github.com/devilking7x/awesome-llm-observability | curated list | 2026-09 | 2026-10-10 | Verified (existence) | secondary interpretation |

**Gaps / Unknowns:** no vendor publishes its full golden dataset or judge prompts (all proprietary); independent studies of judge-human correlation on *product* tasks (vs. academic) are thin; the 80–85% correlation figure is practitioner-cited, not sourced to a specific study in the material found.
