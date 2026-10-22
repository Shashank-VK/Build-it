# Domain A — Area 1: Product Research and Planning (AI-assisted)

*How AI assists product teams with market/competitor research, ideation, and roadmap planning — i.e., AI used in the process of deciding what to build.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## Claim labels used
- **Verified** — primary technical source or direct evidence confirms it
- **Corroborated** — two or more independent sources agree
- **Inferred** — reasoned from available evidence, not directly stated
- **Proposed** — a source proposes it as an approach, without evidence of adoption
- **Unknown** — no reliable evidence found

## 1. What teams demonstrably do

### Competitive/landscape research via agent skills
- **Claim (Corroborated):** Engineering/product teams build reusable "research" agent skills (versioned instruction cards, e.g. a `competitive-research` skill) that tell a coding agent when and how to combine web search with internal document search, with rules like "never invent URLs or cite without a source" and tool-round caps (e.g. 8 rounds) before human escalation.
- **Concrete example:** A documented skill card named `competitive-research` instructs the agent: identify competitor name and internal doc path from the request, plan sub-questions (products, pricing signals, roadmap overlap), run web + doc search, reflect on a coverage score, and deliver a cited report — distinguishing skills (playbooks) from MCP tools (executable functions) and one-off prompts.
- Source: https://github.com/vinod-donthi/hands-on-llm-engineering/blob/HEAD/week-04/theory/agent-skills-and-harness.md (GitHub, community curriculum; evidence class: corroborating; updated ~Aug 2026)

### Pipeline-built roadmap generators
- **Claim (Corroborated):** Individual practitioners wire LLM pipelines over internal data sources (product analytics exports, NPS/support tickets, competitor RSS) to draft roadmap tables: normalize sources to JSON, use few-shot prompt templates with past roadmaps, low temperature (0.2) for determinism, parse Markdown tables into DataFrames, rank by Impact/Effort score, and expose via Slack slash commands / Lambda webhooks.
- **Concrete example:** A Medium practitioner piece documents a weekend-built roadmap generator using OpenAI API (gpt-4-turbo), pandas parsing, and an AWS Lambda + API Gateway + Slack slash command deployment, reporting ~70% planning-time reduction on drafting (self-reported, unverified scale).
- Source: https://medium.com/@ranajawadai/i-built-an-ai-powered-project-roadmap-generator-that-cuts-planning-time-by-70-86ccabbd25b9 (evidence class: first-hand practitioner; Sep 2026)

### Governance over LLM-generated planning artifacts
- **Claim (Corroborated):** Some enterprise product teams explicitly treat LLM brainstorming / market-synthesis output as the lowest rung of evidence — usable only as "initial ideation vectors and null-hypothesis generators," with **zero engineering capital permitted** on that basis alone (no sprint tickets, no production code) until higher-rung evidence (telemetry, controlled experiments, customer feedback) validates it.
- **Concrete example:** A "5-Rung Evidence Ladder" governance model published by a dev practitioner (dev.to, Oct 2026) places "Synthetic Ideation & LLM Speculation" at Rung 1, capping customer-interview signals at Rung 2 to <5% discovery bandwidth.
- Source: http://dev.to/tarikmostafa/how-enterprise-product-teams-enforce-operational-ai-governance-using-the-5-rung-evidence-ladder-1jm2 (evidence class: practitioner proposal with governance framing; treat as Proposed-to-Corroborated)
- **Engineering implication:** AI-assisted planning output needs an explicit "trust boundary" in the workflow; otherwise LLM-generated plans get mistaken for validated plans.

### Deep research tracks for build-vs-buy decisions
- **Claim (Corroborated):** Small teams run large LLM-assisted research programs (100k+ words across ~11 tracks: orchestration frameworks, cost analysis, entity extraction benchmarking, gap detection, ingestion pipelines) with documented success criteria: decision clarity with rationale, POC validation on real workload, cost confidence within ±20%, and explicit risk acceptance.
- **Concrete example:** peermesh/knowledge-graph-lab's `POST-RESEARCH-ROADMAP.md` records ~140,000 words across 11 research tracks with per-track status and decision gates.
- Source: https://github.com/peermesh/knowledge-graph-lab/blob/HEAD/docs/research/ai-pipeline/POST-RESEARCH-ROADMAP.md (GitHub repo; evidence class: primary technical; Nov 2025)

## 2. Tools and workflows
| Tool/pattern | Role | Notes |
|---|---|---|
| Agent "skills" (CLAUDE.md / SKILL.md style cards) | Reusable research playbooks with trigger conditions, rules, ordered steps | Skills call tools; they don't replace them |
| Web search + internal doc search | Public competitor facts vs internal roadmap | Rule: never invent URLs |
| Prompt templates + few-shot examples from past roadmaps | Roadmap drafting | Low temperature (~0.2) for determinism |
| Structured parsing (Markdown → DataFrame) | Ranking by Impact/Effort | Keeps output machine-usable |
| Evidence ladders / trust tiers | Governance of AI-generated plans | Zero-eng-capital rule on Rung 1 |

## 3. Failure modes
1. **Fabricated research inputs.** AI research summaries invent URLs, statistics, and competitor claims unless constrained ("cite only with a source"). **Corroborated** — the competitive-research skill explicitly exists to counter this.
2. **Plans mistaken for validation.** Draft roadmaps look authoritative; governance models flag that speculative LLM output carries no operational grounding. **Corroborated.**
3. **Stale or generic outputs.** Roadmaps generated without fresh internal data revert to generic advice; the working pipelines all start with real data sources (analytics CSVs, support tickets). **Inferred from the pipelines documented.**
4. **Marketing-vs-measured gap on time savings.** "70% planning-time cut" claims are self-reported by builders without independent measurement. **Corroborated pattern; specific numbers Unverified.**

## 4. Costs / latency / reliability
- Inference cost for planning tasks is low relative to coding agents (short sessions, no test loops) — typically cents to a few dollars per run via API. **Inferred** from pipeline descriptions (single LLM call, temperature 0.2).
- Reliability: output is probabilistic prose; value depends entirely on the human review gate. No production-system latency constraints. **Inferred.**

## 5. Human correction burden
- High at first, then falling: pipelines that embed a feedback loop ("let the system learn from the team's decisions") are the ones that persist. Without iteration on weighting/prompts, the draft quality stays generic. **Corroborated (practitioner report).**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** first-draft synthesis over many sources; normalizing heterogeneous inputs (analytics + tickets + competitor feeds) into one schema; producing a structured draft table fast enough to iterate weekly.
- **Creates rework:** when teams treat the draft as the decision; invented citations that must be re-verified; generic recommendations that a human must rewrite with real context.
- **Rule of thumb (Inferred):** AI-assisted planning works when output is treated as *draft + evidence pointers*, and fails when treated as *analysis*.

## 7. Boundary notes (A vs B vs C)
- This area is **Domain A**: AI assists humans in deciding what product to build. It is NOT Domain B (an AI feature inside the shipped product, e.g. a customer-facing research chatbot) and NOT Domain C (AI automating business operations like sales or HR). If a vendor markets an "AI product-research copilot" as a product feature sold to customers, that *product* is Domain B; the *internal workflow described here* is Domain A.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 1.1 | Research skill cards with citation rules and round caps | https://github.com/vinod-donthi/hands-on-llm-engineering/blob/HEAD/week-04/theory/agent-skills-and-harness.md | GitHub curriculum | vinod-donthi (community) | ~Aug 2026 | Medium | corroborating |
| 1.2 | Weekend roadmap-generator pipeline (analytics + tickets + RSS → LLM → ranked table → Slack) | https://medium.com/@ranajawadai/i-built-an-ai-powered-project-roadmap-generator-that-cuts-planning-time-by-70-86ccabbd25b9 | Blog | practitioner (Medium) | Sep 2026 | Low–Medium (self-reported) | first-hand practitioner |
| 1.3 | 5-rung evidence ladder; Rung 1 = LLM speculation, zero eng capital | http://dev.to/tarikmostafa/how-enterprise-product-teams-enforce-operational-ai-governance-using-the-5-rung-evidence-ladder-1jm2 | Blog | tarikmostafa (dev.to) | Oct 2026 | Medium | community observations |
| 1.4 | 140k-word, 11-track AI research program with decision gates | https://github.com/peermesh/knowledge-graph-lab/blob/HEAD/docs/research/ai-pipeline/POST-RESEARCH-ROADMAP.md | GitHub repo docs | peermesh | Nov 2025 | Medium | primary technical |
