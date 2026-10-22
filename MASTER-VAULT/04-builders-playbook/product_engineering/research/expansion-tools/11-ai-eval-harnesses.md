# §30 — AI Eval Harnesses & LLM Observability (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

Market context (2026): rapid consolidation — acquisitions by OpenAI, Anthropic, ClickHouse, Mintlify, Palo Alto Networks, CoreWeave; archival of independents. (HackerNoon consolidation analysis, Aug 2026.)

---

## EV-01 — Promptfoo — ACTIVE (acquired by OpenAI)
- Purpose / problem: Open-source LLM eval + red-teaming: declarative configs, prompt/model/RAG comparisons, graded assertions, adversarial probes (prompt injection, jailbreaks, PII leakage; OWASP LLM Top 10 mapped), CI regression gates, MCP proxy, code scanning.
- OSS/commercial: OSS **MIT** (CLI stays open source post-acquisition); commercial Cloud/Enterprise (Team $50/mo; Enterprise/on-prem custom).
- Integration: CLI (Node), Web UI, CI/CD; runs locally (no data leaves env by default).
- Maintenance: Active. **Acquired by OpenAI Mar 9, 2026** (announced; close not publicly confirmed); to fold into "OpenAI Frontier"; ~130k MAU; $23M raised pre-acquisition (Series A $18.4M Jul 2025, Insight Partners).
- Limitations: Roadmap now set inside OpenAI; enterprise features commercial.
- Security: Local-first eval = data stays local; red-team probes test your own apps.
- Alternatives: DeepEval, Ragas, LangSmith evals, Braintrust.
- Switching costs: Low (config-file driven; importable test files).
- Use: U(Verified) — 25%+ of Fortune 500 used it (vendor claim, Corroborated-weak).

## EV-02 — Langfuse — ACTIVE (acquired by ClickHouse)
- Purpose / problem: LLM observability: end-to-end tracing (waterfall views), prompt management/versioning, LLM-as-judge evals, datasets, session replay, cost tracking.
- OSS/commercial: OSS **MIT core** (enterprise modules — SSO/RBAC/audit/retention — separately licensed). YC W23; $4M seed (Lightspeed, La Famiglia, YC).
- Integration: OpenTelemetry-native (SDK v4 on OTel), LangChain, LlamaIndex, OpenAI SDK, LiteLLM, Vercel AI SDK, Haystack, Mastra; self-host via Docker Compose.
- Maintenance: Active. **Acquired by ClickHouse Jan 16, 2026** (announced alongside ClickHouse's $400M Series D @ $15B); "remains 100% open-source," self-hostable, Cloud continues standalone (acquirer statement); v3 requires ClickHouse (Langfuse already ran on ClickHouse). v4 claims up to 165x faster dashboards (vendor claim).
- Limitations: No infra monitoring (pairs with OpenObserve etc.); enterprise features paywalled; cloud pricing grows with event volume.
- Security: PII masking in SDK before export; self-hostable for data residency.
- Alternatives: LangSmith, Braintrust, Arize Phoenix, Helicone.
- Switching costs: Low–medium (OTLP export keeps traces portable).
- Use: U(Proposed) — most-adopted OSS LLM observability per community analyses.

## EV-03 — LangSmith — ACTIVE
- Purpose / problem: LangChain's tracing/eval/dataset/prompt-experimentation platform; framework-agnostic observability.
- OSS/commercial: Commercial SaaS (Plus $39/seat/mo; free Developer plan 5k traces/mo). LangChain Inc.: $260M raised, ~$16M ARR (per awesome-list trackers; Corroborated-weak).
- Integration: LangChain/LangGraph native; OTLP ingest + SDK export; works with non-LangChain frameworks.
- Maintenance: Active (2026); the product behind LangChain's $125M Oct 2025 raise.
- Limitations: Enterprise add-ons for self-hosting; commercial-only.
- Security: Client-side hiding/anonymizers; PII controls.
- Alternatives: Langfuse, Braintrust, Arize Phoenix.
- Switching costs: Medium.
- Use: U(Proposed).

## EV-04 — Braintrust — ACTIVE
- Purpose / problem: Evaluation-first platform: datasets, scoring, experiments, production monitoring for LLM apps.
- OSS/commercial: Commercial SaaS. **~$800M valuation, $121M raised (Series B)**; Pro $249/mo; free Starter (1GB data/mo, 10k scores/mo).
- Maintenance: Active (2026).
- Alternatives: LangSmith, Langfuse, Confident AI.
- Switching costs: Medium.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-05 — Arize Phoenix — ACTIVE (independent)
- Purpose / problem: OSS LLM tracing/evaluation (OpenTelemetry + OpenInference based); LLM/code/human evaluators; built-in price tables.
- OSS/commercial: OSS (Elastic License 2.0 — note: not OSI-approved); in-house product of Arize AI. **Arize raised $70M Series C Feb 2025**; not acquired.
- Integration: Docker/K8s self-host; OTel native.
- Maintenance: Active (2026).
- Limitations: ELv2 license restricts competitive hosting; narrower community than Langfuse.
- Alternatives: Langfuse, LangSmith.
- Switching costs: Low–medium.
- Use: U(Proposed).

## EV-06 — DeepEval / Confident AI — ACTIVE
- Purpose / problem: OSS Python eval framework (Apache-2.0): 50+ plug-and-play metrics, pytest-style, RAG/agent/MCP evals, synthetic data; Confident AI commercial cloud (CI gates, red-teaming, guardrails, SOC 2, HIPAA).
- OSS/commercial: OSS Apache-2.0 core + commercial cloud (Starter $19.99/user/mo; Pro/Team $499–2,000/mo).
- Maintenance: Active (2026).
- Alternatives: Promptfoo, Ragas.
- Switching costs: Low.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-07 — Ragas — ACTIVE
- Purpose / problem: OSS RAG evaluation metrics (faithfulness, answer relevancy, context precision/recall).
- OSS/commercial: OSS (Apache-2.0).
- Maintenance: Active (2026).
- Alternatives: DeepEval, Phoenix evaluators.
- Switching costs: Low.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-08 — Helicone — MAINTAINED (acquired, maintenance mode)
- Purpose / problem: One-line LLM proxy + observability (Apache-2.0); AI gateway with OTel support.
- OSS/commercial: OSS Apache-2.0 gateway; managed platform.
- Maintenance: **Maintenance mode after Mintlify acquisition (Mar 3, 2026)** — security/bug fixes/new models only; customers being migrated; no OSS/self-host commitment stated. ~16k orgs affected.
- Alternatives: Portkey, LiteLLM, Langfuse.
- Switching costs: Low (one-line proxy) — migration traffic ("moving off Helicone") is live.
- Use: U(Proposed).

## EV-09 — TensorZero — DEPRECATED (archived)
- Purpose / problem: Rust gateway + observability + evals + experimentation (Apache-2.0).
- Maintenance: **Archived Jun 12, 2026** (~11.7k stars); code forkable, unmaintained.
- Alternatives: Bifrost, LiteLLM, Portkey.
- Use: Historical.

## EV-10 — Humanloop — SUPERSEDED (acqui-hired)
- Purpose / problem: Prompt engineering + evaluation collaboration platform.
- OSS/commercial: Was commercial (~$7.9M raised, ~$3.8M ARR per trackers).
- Maintenance: **Acqui-hired by Anthropic** (per awesome-list market notes, 2026); standalone product wound down.
- Alternatives: LangSmith, Braintrust.
- Use: Historical.

## EV-11 — Portkey — ACTIVE (acquisition announced)
- Purpose / problem: AI gateway (Apache-2.0 since Mar 2026) + managed observability/routing/guardrails platform.
- OSS/commercial: OSS gateway + commercial platform ($49/mo Pro; ~$5M ARR per trackers).
- Maintenance: Active; **acquisition announced by Palo Alto Networks** (2026, per market notes — verify close).
- Alternatives: LiteLLM, Helicone, Kong AI Gateway.
- Use: U(Proposed).

## EV-12 — Weights & Biases Weave — ACTIVE (acquired)
- Purpose / problem: LLM trace/eval layer inside W&B MLOps platform (SDK Apache-2.0; OTLP endpoint; Presidio redaction).
- OSS/commercial: Commercial. **W&B acquired by CoreWeave** (~$1.25B valuation, ~$60M revenue per trackers).
- Maintenance: Active under CoreWeave (2026).
- Alternatives: LangSmith, Langfuse.
- Use: U(Proposed).

## EV-13 — Comet Opik — ACTIVE (independent)
- Purpose / problem: OSS LLM eval/observability; in-house product of Comet ML (not acquired).
- OSS/commercial: OSS + commercial.
- Maintenance: Active (2026).
- Alternatives: Langfuse, Phoenix.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-14 — Evidently AI — ACTIVE
- Purpose / problem: OSS ML/LLM evaluation and monitoring (reports, test suites).
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: DeepEval, Phoenix.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-15 — Patronus AI — ACTIVE
- Purpose / problem: LLM evaluation and guardrails (finance/regulated focus).
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: Braintrust, Guardrails AI.
- Use: U(Proposed). (Lightly researched — depth debt.)

## EV-16 — SWE-bench / Terminal-Bench — ACTIVE (benchmarks, not products)
- Purpose / problem: Standard benchmarks for coding agents (SWE-bench: GitHub issue→PR tasks; Terminal-Bench: terminal-based agentic tasks; SWE-bench Verified subset).
- OSS/commercial: Open research artifacts.
- Maintenance: Active; cited across vendor claims (Devin, OpenHands, Cline, Cursor comparisons).
- Limitations: Benchmark gaming risk; vendor-reported numbers need independent reproduction.
- Use: U(Verified) — industry-standard reference points.

## Notable status findings (eval harnesses)
- Promptfoo → **OpenAI (Mar 2026)**; Langfuse → **ClickHouse (Jan 2026)**; Helicone → **Mintlify (Mar 2026, maintenance mode)**; Humanloop → **Anthropic (acqui-hire)**; Portkey → **Palo Alto Networks (announced)**; W&B → **CoreWeave**.
- TensorZero — **archived Jun 2026**.
- Consolidation thesis: winner-take-most around full-stack LLMOps suites, not standalone tools.
