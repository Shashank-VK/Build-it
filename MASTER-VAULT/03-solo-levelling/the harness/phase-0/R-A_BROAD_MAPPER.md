# Phase 0 — Anchor the Project: Broad-Mapped Longlists
## P0-01: Candidate Archetype Longlist (12) + P0-07: Candidate Success Metrics Longlist (25)
**Researcher A — Broad Mapper | 2026-08-31**

---

## 0. Research Method & Search Angles

Verbose sweep, not a lazy pass. Seven+ distinct search angles were executed to avoid anchoring on the seed list alone. Each angle used independent query families and cited sources.

| Angle | Query Family | Purpose |
|-------|--------------|---------|
| **A1: AI Coding Assistant & Harness Taxonomies** | `Claude Code Cursor Windsurf Copilot project types categories`, `Aider OpenHands Devin SWE-bench harnesses` | How the 11+ production harnesses (Terminal, IDE, Cloud/Async, Research) classify work |
| **A2: Benchmark & Evaluation Harness Literature** | `DEVIN evaluation SWE-bench harness`, `SWE-bench Verified Terminal-Bench evaluation metrics`, `human eval harness LLM agent reliability safety cost` | What is actually measured when an agent/harness is scored |
| **A3: Solo / Indie-Hacker / Freelance Product Taxonomy** | `indie hacker solo developer project types`, `Cursor Windsurf IDE project templates categories` | What a 1-3 person team ships for money (Micro-SaaS, tools, content, marketplace) |
| **A4: Delivery Performance & Developer Experience Frameworks** | `DORA metrics DX measurement SPACE framework`, `DX Core 4 speed effectiveness quality impact` | Industrial metrics for throughput, stability, and human factors |
| **A5: Data & Pipeline Architecture Literature** | `data pipeline ETL project types modern data stack`, `MLOps AI ML experiment project types` | Batch vs streaming vs ELT vs Lakehouse vs Feature Pipeline splits |
| **A6: Browser Automation & RPA Literature** | `browser automation Playwright Puppeteer project types scraping RPA` | Stateful, failure-aware web automation as a distinct discipline |
| **A7: Migration & Agent System Architectures** | `software migration modernization project categories`, `LLM agent system project types categories` | 6R/7R modernization and ReAct/multi-agent/agent-harness layering |

---

## PART I — P0-01: CANDIDATE ARCHETYPE LONGLIST (12)

> Seeds given: greenfield web, prod backend, ETL, automation, AI/ML exp, research/writing, browser-heavy, dev tooling, data science, infra/DevOps, migration, agent system. Instruction: do NOT anchor — extend, split, merge freely. The following 12-way split does exactly that: **ETL vs Streaming vs Reverse-ETL** is unfolded inside Archetype 03; **Internal Tools / CRUD** is pulled out of generic backend into Archetype 02+08; **Research/Writing** is separated from Data Science (08 vs 09); **Browser-Heavy** is split from generic Automation (04 vs 05); **Agent System** is given its own first-class archetype (07) distinct from AI/ML (06).

### Overview Table

| # | Archetype Name | One-Line Definition | Primary Harness Demand |
|---|----------------|---------------------|------------------------|
| 01 | **Greenfield Full-Stack Web Product (0→1)** | Blank-slate consumer/prosumer web app from idea → deployed MVP → iterating product | Scaffolding, design system, auth/billing, preview deploys |
| 02 | **Production Backend Service & API Platform** | Long-lived backend: REST/GraphQL/gRPC, workers, queues, persistence, multi-tenant concerns | Contracts, migrations, observability, breaking-change gates |
| 03 | **Data Pipeline & Lakehouse (Batch / Streaming / ELT)** | Data movement & transformation fabric: Bronze→Silver→Gold, CDC, streaming, reverse ETL | DAG orchestration, idempotency, data quality, warehouse as source of truth |
| 04 | **Event-Driven Automation & Integration Glue** | Scheduled/event-triggered glue across SaaS APIs, webhooks, cron jobs, iPaaS flows | Trigger catalog, secret management, retry/compensation, human-in-the-loop |
| 05 | **Browser Automation & Web Harvesting (RPA)** | Stateful, fault-tolerant browser fleet (Playwright/Puppeteer) for scraping, RPA, render | Selector resilience, stealth, proxy rotation, stateful recovery |
| 06 | **AI/ML Experiment → Served Model (MLOps)** | Notebook-to-API lifecycle: data versioning → training → registry → serving → monitoring | Experiment tracking, reproducibility, drift detection, cost-aware training |
| 07 | **LLM Agent & Agentic Workflow System** | Agent loop + tools + memory + guardrails: single ReAct or multi-agent crew | Tool registry, budget guard, injection resistance, trace viewer |
| 08 | **Research, Analysis & Knowledge Synthesis System** | Long-horizon reasoning over sources to produce a report, memo, dossier or publication | Source grounding, citation, hallucination gate, human review |
| 09 | **Data Science & Analytics Product (Notebook → Dashboard)** | Exploratory analysis shipped as an interactive artifact (dashboard, notebook, report) | Statistical correctness, viz, narrative, reproducibility |
| 10 | **Developer Tooling, CLI, SDK & Scaffold** | Tools that other developers use: CLI, SDK, linter, template generator, harness itself | DX, semver, backward-compat, distribution, dogfooding |
| 11 | **Infra, DevOps & Platform Engineering (IaC)** | Provisioning & operating the substrate: Terraform/Pulumi, K8s, CI/CD, secrets, policy | Declarative drift detection, blast-radius control,日-cost visibility |
| 12 | **Migration, Modernization & Strangler Rebuild** | Moving a legacy system to modern stack via 6R/7R strategy (rehost → rebuild) | Codemods, dual-write, shadow traffic, incremental cutover |

---

### 01 — Greenfield Full-Stack Web Product (0→1)

**Definition.** The canonical indie-hacker path: a new web product built by 1-3 people with no inherited code. Covers both marketing surface (landing, docs, SEO) and authenticated app surface (dashboard, settings, billing). Lifecycle is idea → scaffold → vertical slice → alpha with real users → hardening → growth loops. It is distinct from "frontend component work" because it owns the full stack from domain to deploy.

**Example Projects:**
* Micro-SaaS: Nomad List-style directory, Tweet Hunter-style scheduler, SiteGPT-style wrapper [indie-hacker taxonomy]
* Waitlist → auth → Stripe billing → dashboard MVP (the `saas` template in multiagent-template) [multiagent-template workspace categories]
* Portfolio / product-hunt launch with SEO content engine
* Astro/Next.js marketing site + Postgres-backed app + edge deployment

**Key Characteristics:**
* **Stakeholder is the end user**, not an internal team — UX, copy, and performance are first-class.
* **Unbounded scope temptation** — harness must enforce a vertical-slice gate and feature-flag discipline.
* **High scaffold leverage** — project-type scaffolders (firstcut `frontend`/`monorepo`, SynaptixLabs `backend+frontend`, UitKit `Next.js SaaS`) all treat this as a top-level category [firstcut categories][SynaptixLabs scaffold].
* **Preview & branching critical** — every PR needs an ephemeral URL; schema in `AGENTS.md` / `CLAUDE.md` / `.cursorrules` must be code-generated per tool [context-kit config generators].
* **Billing/auth as cross-cutting** — Stripe, OAuth, RBAC show up day-2, not day-30.
* **SEO & content debt** accumulates silently — needs linting beyond code.

### 02 — Production Backend Service & API Platform

**Definition.** A durable backend that other systems depend on: REST/GraphQL/gRPC API, background workers, queues, scheduled jobs, and a relational or document store. It is *not* a throwaway script; it has SLAs, versioned contracts, migrations, and on-call. This archetype absorbs the "internal tools CRUD" and "business automation CRUD" patterns found in internal-tools literature (Views, Macros, Triggers, Automations as CRUD resources) but generalizes them to any production backend.

**Example Projects:**
* Multi-tenant SaaS API with webhook delivery and rate limits
* Microservice extracted from monolith with its own data store
* Worker fleet consuming Kafka/Kinesis and writing to Postgres/ClickHouse
* `backend` template in firstcut (`REST/GraphQL API, microservice, worker, data pipeline`) [firstcut]

**Key Characteristics:**
* **Contract-first design** — OpenAPI/GraphQL schema is the harness input, not an afterthought.
* **Migrations are risk events** — needs dual-write / expand-contract patterns, tested via Terminal-Bench-style sandbox tasks [Terminal-Bench sandbox definition].
* **Observability is the product** — logs, traces, metrics, and dashboards are deliverables.
* **Throughput vs stability tradeoff** explicit (DORA pairing) — deploy frequency and lead time vs change failure rate.
* **Tenancy & authz** complicate every query.
* **Long-lived branching** — harness must handle incremental delivery over months.

### 03 — Data Pipeline & Lakehouse (Batch / Streaming / ELT / Reverse ETL)

**Definition.** The data-engineering fabric that turns raw sources into trusted datasets. Modern form is not "classic ETL" alone but four patterns: **ETL** (transform before load), **ELT** (load then transform in warehouse with dbt/SQL), **Streaming** (Kafka → Flink/Spark Structured Streaming), and **Reverse ETL** (warehouse → operational SaaS). Architecturally organized as **Bronze (raw, append-only) → Silver (conformed) → Gold (star schema / marts)** — the Medallion/Lakehouse layering [modern data stack research].

**Example Projects:**
* Retail sales CSV → S3 → Snowflake → dbt marts → dashboard [retail sales example]
* CDC replication from Postgres → Kafka → ClickHouse for real-time analytics
* Real-estate Zillow API harvest → AWS Glue → Snowflake (real-estate example)
* Hybrid lambda pipeline (batch nightly + streaming intraday) with Airflow + dbt + Superset

**Key Characteristics:**
* **Paradigm choice is architectural** — batch, micro-batch, true streaming, CDC, reverse ETL each implies different latency/correctness/tooling [processing-paradigm classification].
* **Orchestration is the harness** — DAG (Airflow/Dagster/Mage) with retries, SLAs, and data-aware sensors.
* **Data quality as a first-class test** — dbt tests, Great Expectations, volume/freshness checks; analogous to SWE-bench's `PASS_TO_PASS` [SWE-bench PASS_TO_PASS].
* **Warehouse is a product** — Gold marts have SLAs and consumers (BI, reverse ETL, ML features).
* **Cost is per byte/scan** — BigQuery/Snowflake scanning makes "efficiency" measurable in dollars.

### 04 — Event-Driven Automation & Integration Glue

**Definition.** The long tail of solo-team work: small durable automations that connect systems. A cron that reconciles Stripe → Notion, a webhook handler that triggers a workflow, a Slack bot that triages tickets. Distinct from Archetype 05 (browser) because it lives in API/webhook space, and from 02 (backend) because each unit is tiny but the *fleet* must be operated.

**Example Projects:**
* GHL workflow builder clone: 95 actions × 93 triggers as internal CRUD [GHL internal API categories]
* Zapier/Make-style automation replaced by code (n8n, Temporal, Airflow)
* Slack/Discord bot with slash commands, threaded replies, and scheduled digests
* Customer onboarding sequence: Stripe event → email → CRM update → internal notification

**Key Characteristics:**
* **Trigger catalog is the spec** — "on ticket create / on payment success / on schedule" enumerates the archetype.
* **Secret & credential sprawl** — OAuth tokens, API keys, rotation; a safety surface.
* **Retry & idempotency non-negotiable** — exactly-once handling when webhooks redeliver.
* **Observability is "did it fire?"** — needs dead-letter queue, run history, and manual replay.
* **Low code per unit, high operational burden in aggregate** — harness value is fleet management.

### 05 — Browser Automation & Web Harvesting (RPA)

**Definition.** A stateful browser fleet that drives the web like a human: scraping, crawling, form-filling, PDF rendering, and enterprise RPA. The modern default is **Playwright** ("modern cross-browser automation ... current default for reliable browser RPA") with **Puppeteer** as the battle-tested Chromium alternative for scraping/render tasks [Playwright/Puppeteer definitions]. Tooling like **Crawlee** (works with Puppeteer, Playwright, Cheerio, JSDOM, proxy rotation) and **Browserless** (managed Chromium/Firefox/WebKit for Puppeteer/Playwright/Selenium) define the production shape [Crawlee][Browserless].

**Example Projects:**
* Competitive price monitor: 10k product pages daily, anti-bot evasion, diff alerts
* Enterprise RPA: migrating from Puppeteer → Playwright as a "reliable, stateful, failure-aware system, not a best-effort script" [RPA job spec]
* Content extraction for RAG: Crawlee crawl → chunk → vector store
* Screenshot/PDF farm and performance audits at scale (Browserless REST APIs)

**Key Characteristics:**
* **Reliability is a distributed-systems problem** — not a script; needs state checkpoints, queue, and replay.
* **Selector brittleness is the dominant failure mode** — harness must test and auto-repair selectors.
* **Stealth & proxy tier** — BrowserQL, fingerprint randomization, rotation, CAPTCHA handling.
* **Legal/compliance surface** — ToS, rate limits, and data licensingUnlike pure API work.
* **Artifact pipeline** — HTML → PDF/JPG/extracted JSON with deterministic post-conditions, mirroring Terminal-Bench's "sandbox + post-condition" scoring [Terminal-Bench].

### 06 — AI/ML Experiment → Served Model (MLOps)

**Definition.** The full model lifecycle in four phases: **experimentation & model development → model generation → quality assurance → deployment & monitoring** [MLOps lifecycle]. Covers supervised/unsupervised/semi-supervised/reinforced training, experiment tracking (MLflow), data versioning (DVC), containerization, feature store, serving (FastAPI), and drift monitoring (Evidently AI) as seen in the reference AG News classifier [MLOps reference implementation].

**Example Projects:**
* News classifier (AG News: World/Sports/Business/Sci-Tech) from raw data → monitored API [reference project]
* Recommendation model with A/B serving and shadow traffic
* Time-series forecaster with feature store and backfill pipeline
* Eval harness for LLM quality (distinct from Archetype 07's agent harness)

**Key Characteristics:**
* **Reproducibility is the invariant** — pinned data, code, env, and seed; DVC + Docker + CI.
* **Two pipelines, one truth** — training and serving must agree on features.
* **Metric vs business gap** — offline accuracy vs online impact; needs holdout and live A/B.
* **Cost is training + inference** — harness must surface $/experiment and $/1k inferences.
* **Monitoring is not optional** — drift, data quality, and latency are continuous evals.

### 07 — LLM Agent & Agentic Workflow System

**Definition.** A system where an LLM is the cognitive engine inside a loop with tools, memory (RAG/MCP), environment sensing, and guardrails — from a single ReAct loop to a multi-agent crew (AutoGPT, BabyAGI, SuperAGI, HuggingGPT, CAMEL, AgentGPT, MetaGPT) [representative multi-agent systems]. Architecturally the harness is `H = (E, T, C, S, L, V)` across control loop, reasoning, tool surface, memory, sub-agents, safety, and verification [harness as first-class object]. Frameworks sit at different layers: **SDK** (CrewAI, Pydantic AI), **orchestration runtime** (LangGraph), **agent harness** (Claude Agent SDK), **managed platform** (Bedrock AgentCore) [framework layer taxonomy].

**Example Projects:**
* Customer-support agent with tool routing (`calculator → retriever → formatter`) and trace evaluator [llm-agent-eval graph]
* Research agent with deterministic planner → executor → critic → safety-guard loop and JSONL traces [Agent Reliability Lab architecture]
* Multi-agent code-review crew (Sequential/Parallel/Loop agents in Google ADK) [ADK agent types]
* Single-agent baseline vs constrained ReAct vs routing-agent ablations [four architecture comparison]

**Key Characteristics:**
* **Tool routing is the product** — correctness is `tool-selection accuracy` (e.g., 87.5% in llm-agent-eval) as much as final answer.
* **Safety is a gate, not a feature** — prompt-injection detection, unsafe-action blocking, human escalation.
* **Cost/latency are primary metrics** — p95 latency, tokens, $/task; the Pareto frontier is `capability × cost` [Lamasu/harness-bench scoring].
* **Harness matters more than model** — same LLM produces wildly different results under different harnesses [oh-my-harness-engineering].
* **Evaluation is hermetic + adversarial** — versioned datasets with representative + red-team + regression cases [Project-Aegis harness design].

### 08 — Research, Analysis & Knowledge Synthesis System

**Definition.** A long-horizon reasoning system that consumes sources (papers, docs, transcripts, web) and produces a structured knowledge artifact: investment memo, literature review, competitive dossier, technical report, or book-length synthesis. The harness delivers not code but *verifiable prose and citations*. Distinct from data science (09) because the primary operation is synthesis and argumentation, not statistical modeling.

**Example Projects:**
* Competitive teardown: 20 competitors × pricing × features × moat, with sources
* Literature survey with inclusion criteria, extraction sheet, and bibliography
* Due-diligence memo from data room + interviews + public filings
* AI-assisted book/paper writing with chapter-level RAG and claim→source trace

**Key Characteristics:**
* **Groundedness is the test** — every claim needs a source; hallucination is a defect.
* **Long context & memory** — 100k+ token working memory with RAG over chunked corpus.
* **Human review is the gate** — "manual-only" grading pass before release [Project-Aegis MANUAL-ONLY].
* **Iteration is the loop** — draft → critique → revise, with evaluator reliability checks.
* **Artifact is the deliverable** — harness must version prose like code (diff, blame, rollback).

### 09 — Data Science & Analytics Product (Notebook → Dashboard)

**Definition.** Exploratory analysis shipped as an interactive artifact: a polished Jupyter/Quarto notebook, a Streamlit/Dash/Superset dashboard, or a scheduled report. The actor is an analyst; the consumer is a decision-maker. Unlike the pipeline (03) which is infrastructure, this archetype is *narrative + visualization* with statistical rigor.

**Example Projects:**
* Churn analysis notebook → executive deck with causal caveats
* Self-serve KPI dashboard over Gold marts with row-level security
* Survey analysis with weighting, significance testing, and viz
* Ad-hoc "answer this business question by EOD" with reproducible notebook

**Key Characteristics:**
* **Narrative correctness > pipeline uptime** — p-values, confidence intervals, and methodology matter.
* **Reproducibility despite interactivity** — pinned data snapshot + deterministic render.
* **Viz as the contract** — harness must screenshot/assert chart structure.
* **Short lifecycle, high reuse** — many one-off notebooks become permanent reports; needs promotion path to pipeline (03).

### 10 — Developer Tooling, CLI, SDK & Scaffold

**Definition.** Tools built *for* developers: a CLI, an SDK, a linter rule, a template generator, or the harness itself. The user is an engineer; ergonomics, composability, and backward compatibility are existential. This archetype includes the `tooling` category in firstcut (`CLI tool, SDK, developer library, scripts`) and the `internal` workspace template (lighter pipeline, no external gates) [firstcut][multiagent-template].

**Example Projects:**
* `firstcut`-style scaffolder that writes `AGENTS.md` + `CLAUDE.md` + `.cursorrules` + `.windsurfrules` from one `skills/` spine [firstcut]
* SynaptixLabs scaffold (`backend = FastAPI /health`, `frontend = Vite → /health`) [SynaptixLabs]
* Custom lint rule / codemod / release-please pipeline
* The harness itself — versioned, tested against SWE-bench Verified / Terminal-Bench

**Key Characteristics:**
* **DX is the product** — installation friction, `--help` quality, and error messages are metrics.
* **Semver & breaking-change discipline** — harness must enforce CHANGELOG and compat gates (the `oss` template behavior).
* **Cross-harness portability** — one spine (`AGENTS.md`) with thin adapters per IDE (Cursor MDC, Windsurf waves) [SynaptixLabs adapter model].
* **Dogfooding loop** — the tool builds the next tool; needs self-hosted eval.

### 11 — Infra, DevOps & Platform Engineering (IaC)

**Definition.** The substrate on which all other archetypes run: IaC (Terraform/Pulumi), containers & orchestration (Docker, K8s), CI/CD, secrets, policy, and cost control. The `infrastructure` project type in firstcut (`IaC, platform engineering, Kubernetes, Pulumi/Terraform`) is the canonical instance [firstcut].

**Example Projects:**
* Terraform monorepo for VPC, DB, cache, and app with drift detection
* Kubernetes platform with GitOps (ArgoCD/Flux) and progressive delivery
* CI/CD factory: reusable workflows, ephemeral runners, SBOM + signing
* Cost-observability platform (per-service $/day, budget alerts)

**Key Characteristics:**
* **Declarative & drift-aware** — plan/apply, desired vs actual, with blast-radius control.
* **Stateful & dangerous** — harness must gate `apply` behind `plan` review and human approval.
* **Ephemeral by design** — preview envs, branch deploys, and teardown are first-class.
* **Policy as code** — OPA/Conftest checks are the "tests."
* **Cost is a metric, not an afterthought** — $/env/day surfaced per PR.

### 12 — Migration, Modernization & Strangler Rebuild

**Definition.** Moving a legacy system to a modern platform, language, architecture, or cloud. Framed by the industry-standard **6R/7R models**: Rehost (lift-and-shift), Replatform, Refactor, Rearchitect, Rebuild/Rewrite, Replace/Repurchase, plus Retire/Retain/Encapsulate [6R/7R definitions]. Distinct from greenfield because the harness must work *with* existing behavior, data, and users during transition.

**Example Projects:**
* Lift-and-shift on-prem VM estate → cloud with minimal code change (Rehost)
* Monolith → microservices via strangler fig with dual-write and shadow traffic (Rearchitect)
* Language migration via automated codemods and converters (Migration)
* SaaS replacement of bespoke CRM/ERP (Replace) [expanded 8-approach list]

**Key Characteristics:**
* **Correctness is behavioral equivalence** — harness needs characterization tests and snapshot oracles before changing code.
* **Incremental cutover is the strategy** — strangler, branch-by-abstraction, feature flags, dark launch.
* **Data is the hardest part** — schema migration, backfill, and dual-read verification.
* **Portfolio view** — 7R model assesses *all* apps (retain vs retire vs modernize) before per-app tactics [7R portfolio framing].
* **Risk-gated** — each increment needs rollback plan and "safe rollback rate" measured via consistency oracle [AWRR safe rollback].

---

## PART II — P0-07: CANDIDATE SUCCESS METRICS LONGLIST (25)

> Coverage mandate: **speed, quality, reliability, safety, cost, DX, maintainability**. Each metric below gives **name, definition, why it matters, and how to measure it**. The set is deliberately over-complete for later filtering — it trades parsimony for coverage of DORA, SPACE, DX Core 4, SWE-bench/Terminal-Bench, and harness-eval literature.

### Speed (Throughput & Flow)

**M01 — Time-to-First-Working-Slice (TTFWS)**
* *Definition:* Elapsed wall-clock from blank repo (or `new` command) to first deployed, user-visible vertical slice that passes a smoke test (e.g., `/health` returns 200 on a preview URL). The solo-team analog of lead time for greenfield.
* *Why it matters:* For indie/solo dev the biggest risk is never shipping. TTFWS predicts whether the harness accelerates 0→1 vs adding ceremony. It is the `firstcut` promise ("one-command scaffold … fully configured project") made measurable.
* *How to measure:* Instrumented harness run: timestamp `harness new` → timestamp first `health` probe passes on preview deploy. Report median and p90 across archetype 01 runs. Target < 15 min for scaffold, < 2h for slice.

**M02 — Lead Time for Changes (DORA)**
* *Definition:* Time from commit to code running in production, per DORA's Four Keys: deployment frequency, lead time, change failure rate, failed deployment recovery time [DORA Four Keys].
* *Why it matters:* The canonical throughput measure; elite teams show sub-1-day lead time with ~5% failure rate. Without it, speed claims are anecdotal.
* *How to measure:* VCS → CI → deploy timestamps. Bucket as DORA elite/high/medium/low. Pull from deployment service; do not self-report.

**M03 — Deployment Frequency**
* *Definition:* How often the harness (or the product it builds) ships to production — on-demand / daily / weekly / monthly per DORA.
* *Why it matters:* Frequency is the behavioral proxy for batch size; smaller batches mean safer, faster learning.
* *How to measure:* Count of successful production deploys per service per week. From deploy API, not commit count.

**M04 — Mean Iteration Cycle Time (Edit → Verify)**
* *Definition:* Time from an agent/human edit to verified feedback (tests, type-check, preview, or evaluator verdict). Captures the inner loop, not just the deploy.
* *Why it matters:* Harness overhead lives here: tool-call latency, queue wait, and re-run cost. Directly maps to DevEx *Feedback Loops* dimension and DX Core 4 *Speed* secondary metric *Perceived Rate of Delivery*.
* *How to measure:* Trace harness loop: `edit committed` → `verification result returned`. Report p50/p95 and TTFT (time to first token) for LLM steps [TTFT definition].

### Quality (Correctness & Defect Economics)

**M05 — Change Failure Rate (DORA)**
* *Definition:* Percentage of deployments causing a failure in production requiring hotfix/rollback, per DORA.
* *Why it matters:* The stability counterweight to speed; optimizing M02/M03 without M05 is gaming. DX Core 4 uses it as the key metric for *Quality*.
* *How to measure:* `failed deploys / total deploys` over rolling 30 days. Failure = incident, rollback, or hotfix tag. From incident + deploy logs.

**M06 — Task Success Rate / Resolved Rate (SWE-bench Analog)**
* *Definition:* Share of tasks where the harness-produced patch passes hidden, deterministic tests. On SWE-bench Verified this is `resolved_ids` where `FAIL_TO_PASS ∧ PASS_TO_PASS` both hold; on Terminal-Bench it is sandbox task success [SWE-bench scoring][Terminal-Bench].
* *Why it matters:* The most defensible quality signal for code generation: behavior, not BLEU. Frontier is ~76% pass@1 / ~81% pass@3 (Jan 2026) [frontier performance].
* *How to measure:* Run harness against versioned eval packs (SWE-bench Verified 500, Terminal-Bench 89, Aider Polyglot 225) with pinned `bench.yaml` and `instruction_template` — prompt is scoring-relevant [harness scoring details]. Report pass@1 and pass@k with Wilson CIs.

**M07 — Verification Strictness (Coverage × Property)**
* *Definition:* Depth of automated verification the harness enforces: line/branch coverage, property-based tests, type strictness, and mutation score. A harness that ships without verification strictness will ace M06 on toy tasks and fail in prod.
* *Why it matters:* Coverage correlates with escaped-defect economics; property tests catch the long tail SWE-bench does not.
* *How to measure:* `covered lines / total lines`, `property tests / modules`, `mypy --strict` pass, mutation kill rate. Gate on thresholds per archetype (e.g., ≥80% for backend).

**M08 — Rework Rate (Churn within 14 days)**
* *Definition:* Percentage of merged changes that are reverted, heavily churned, or hotfixed within 14 days. A leading indicator of M05.
* *Why it matters:* Captures the "landed but not done" failure mode common in accelerated solo dev.
* *How to measure:* `git log --churn` + hotfix label analysis. Report per service, per archetype.

### Reliability (Determinism & Recovery)

**M09 — Harness Determinism / Flake Rate**
* *Definition:* 1 − (flaky runs / total runs) when the same task+model+seed is executed N times. Flake includes non-deterministic tool ordering, race conditions, and LLM non-determinism not caused by prompt.
* *Why it matters:* A harness that is 70% on one run and 40% on the next is not shippable. Reliability literature treats determinism as a first-class metric alongside success rate.
* *How to measure:* Repeat each eval task 5× (`shards:10, max_concurrent` pinned as in SWE-bench Verified) and compute variance; report flake rate and `pass@k` CIs [SWE-bench repeat config].

**M10 — Mean Time to Recovery (MTTR) / Failed Deployment Recovery Time (DORA)**
* *Definition:* Time from failure detection to service restoration, DORA's fourth key metric and AWRR's *MTTR* [DORA][AWRR metrics].
* *Why it matters:* MTTR bounds user impact when M05 fires; elite teams recover in <1 hour.
* *How to measure:* Incident start (alert or failed deploy) → resolved timestamp. Report p50/p95. Drill into detection vs fix vs verify components.

**M11 — Recovery Rate & Safe Rollback Rate (AWRR)**
* *Definition:* Two AWRR metrics: **Recovery Rate (RR)** — share of faults where the harness's compensation/retry restores a consistent state; **Safe Rollback Rate (SRR)** — share of rollbacks that leave no partial writes, verified by a consistency oracle [AWRR metrics].
* *Why it matters:* For agentic work, "retry" without saga-style compensation creates corruption. These metrics score the harness's fault taxonomy and baselines B0–B4.
* *How to measure:* Inject fault suite (network partition, tool timeout, partial write) into a sandboxed run; verify via oracle. Report WCR/RR/MTTR/RCO/HIR/UAR/SRR as a bundle.

**M12 — Human Intervention Rate (HIR) & Human Escalation Precision**
* *Definition:* Share of tasks where the harness correctly escalates to a human (vs acting unsafely or stalling), and precision of that escalation (was it actually needed?). From AWRR and Agent Reliability Lab: `task_completion_rate`, `retry_recovery_rate`, `budget_guard_denials` [AWRR][Agent Reliability Lab scorecard].
* *Why it matters:* A harness that never asks for help is dangerous; one that always does is useless. HIR must be *calibrated*.
* *How to measure:* Run suite with HITL policy; label each escalation as true/false positive via post-hoc review. Report HIR and escalation precision.

### Safety (Harm, Injection, and Compliance)

**M13 — Unsafe Action Block Rate**
* *Definition:* Share of unsafe tool actions (destructive file write, unscoped deploy, secret exfiltration, financial transaction) that the safety guard blocks before execution. Agent Reliability Lab reports `unsafe_action_block_rate` on this [Agent Reliability Lab].
* *Why it matters:* The primary safety gate for autonomous execution in a sandboxed shell [Devin sandboxed compute].
* *How to measure:* Adversarial suite of `N` unsafe goals; run through `SafetyGuard.goal_screen` and `SafetyGuard.action_screen` [Agent Reliability Lab architecture]. Report block rate and false-positive rate on benign tasks.

**M14 — Prompt Injection Resistance Rate**
* *Definition:* Share of indirect prompt injections (tool output, RAG document, web page, issue body) that do not alter the agent's goal or exfiltrate data, per Project-Aegis injection suite [Project-Aegis dimensions].
* *Why it matters:* The dominant real-world attack for browser/RAG agents; SWE-bench issue bodies are themselves an injection surface.
* *How to measure:* Versioned dataset with representative + adversarial + regression cases; per-dimension grader for `injection_resistance` [Project-Aegis workflow]. Report pass rate with Wilson CIs.

**M15 — Expected Harm (Severity × Pr(Execution))**
* *Definition:* `Expected Harm = Severity × Pr(Execution | Model Response)` where severity is calibrated to AI Safety Levels (ASL) and execution likelihood is a function of cost (financial, expertise, equipment). Introduced in recent safety literature to surface inverse risk calibration [Expected Harm paper].
* *Why it matters:* Raw refusal rate is misleading — models over-refuse high-cost, low-likelihood harms while complying with low-cost, high-likelihood ones. Expected Harm corrects for that.
* *How to measure:* LLM-as-judge for severity (ASL-grounded) and execution-cost 0–5 scale, validated by human spot checks. Report distribution and tail risk, not just mean.

**M16 — Groundedness / Hallucination Rate (Research Archetype)**
* *Definition:* Share of generated claims that are entailed by cited sources, graded by groundedness/hallucination grader [Project-Aegis grader].
* *Why it matters:* For Archetype 08 the artifact *is* prose; hallucination is a functional defect.
* *How to measure:* Sample N claims; LLM-as-judge entailment check with human adjudication on disagreements. Report groundedness score and citation coverage.

### Cost (Tokens, Dollars, and Pareto Efficiency)

**M17 — Cost per Task ($/task) & Token Cost**
* *Definition:* Total marginal cost to resolve one task: API tokens (prompt + completion × tariff) + compute (sandbox, browser, container) + amortized infra. LLM-as-judge tax is included. Prior work reports both raw and normalized: e.g., `USD 0.382/task → 0.317/task` after harness tuning, `USD 0.750 → 0.694` on SWE-bench [Harness Composer cost results].
* *Why it matters:* Cost is the binding constraint for solo/small teams; a 2-point gain at 10× cost is a regression.
* *How to measure:* Meter tokens per run (e.g., 583 prompt / 139 completion in llm-agent-eval) with local tariff, plus sandbox time × rate [llm-agent-eval tokens]. Report cost distribution, not just mean.

**M18 — Cost-Performance Pareto Efficiency (Capability × Cost Frontier)**
* *Definition:* Position on the Pareto frontier of `pass@1` vs `$/task`. Lamasu/harness-bench scores explicitly on this frontier (METR-style time-horizon / 50% success length) [Lamasu scoring].
* *Why it matters:* Single-number leaderboards (pass@1 alone) incentivize brute-force sampling. Pareto scoring rewards lean harnesses.
* *How to measure:* Plot all harness variants (ablation arms) and compute Pareto frontier; report distance to frontier and `pass@1 per dollar`.

**M19 — p95 Latency & Time to First Token (TTFT)**
* *Definition:* End-to-end task latency (p50/p95) and TTFT for the first LLM step, plus evaluator latency. llm-agent-eval reports `mean 986ms, p95 3006ms` as a baseline [llm-agent-eval latency].
* *Why it matters:* Latency is DX: a 3s p95 vs 30s p95 changes whether the harness is used interactively or batched. Task Behavior includes latency & cost as a joint dimension.
* *How to measure:* Trace harness loop with pinned client (`0.4.0`) and `proxy.request_timeout ≥ solver timeout` [Terminal-Bench toolchain]. Report p50/p95/TTFT per archetype.

### Developer Experience (Human Factors)

**M20 — Developer Experience Index (DXI) — DX Core 4 Effectiveness**
* *Definition:* The 14-question, research-backed DXI survey score (the key metric for DX Core 4 *Effectiveness*), plus secondary metrics *regrettable attrition* and *time to tenth PR* for onboarding [DX Core 4 structure][DX Core 4 effectiveness].
* *Why it matters:* DXI is the only cross-org comparable measure of "how well developers can do their jobs." DX found +1 DXI point ≈ 10 minutes saved per engineer per week [DX correlation].
* *How to measure:* Standardized 14-item survey to harness users, aggregated at team level (never individual). Report DXI mean and subscales (feedback loops, cognitive load, flow).

**M21 — Cognitive Load & Flow State (DevEx)**
* *Definition:* Self-reported cognitive load and flow-state interruption rate, mapped to DevEx's three dimensions: **Feedback Loops, Cognitive Load, Flow State** [DevEx framework].
* *Why it matters:* SPACE warns never to measure Activity alone — a team can maximize commits while delivering zero value; flow and load complete the picture [SPACE rule].
* *How to measure:* Experience sampling (interruption count per hour, build time, meeting load) + SPACE activity and communication metrics. Use the "pick 2-3 metrics across ≥3 SPACE dimensions" rule [SPACE framework].

**M22 — Time to Tenth PR (Onboarding)**
* *Definition:* Time from first clone to tenth merged PR, a DX Core 4 secondary metric for onboarding friction [DX Core 4 effectiveness].
* *Why it matters:* For a reusable harness, "can a new solo dev be productive in a day?" is a first-order DX test.
* *How to measure:* Cohort new users; timestamp repo access → PR 10 merge. Report median per template (saas vs oss vs internal) [multiagent-template templates].

**M23 — Perceived Usefulness & Adoption (SPACE Satisfaction)**
* *Definition:* Self-reported satisfaction, eNPS, and retention/attrition signals — the *S* in SPACE (Satisfaction and wellbeing) [SPACE dimensions].
* *Why it matters:* A harness can be fast and correct but unloved; satisfaction predicts abandonment.
* *How to measure:* Periodic survey (eNPS, "would you recommend?") + behavioral proxy: 30-day active use, template reuse. Report at team granularity.

### Maintainability (Longevity & Evolvability)

**M24 — Percentage of Time Spent on New Capabilities (DX Core 4 Impact)**
* *Definition:* Share of engineering time/budget allocated to new capabilities vs rework/tech-debt/keeping-the-lights-on, the key metric for DX Core 4 *Impact* [DX Core 4 impact].
* *Why it matters:* Directly frames engineering in business terms: is the harness enabling innovation or trapping the team in debt service?
* *How to measure:* Time-tracking taxonomy or git-history heuristic (feature vs fix vs chore vs infra). Report weekly rolling share; secondary metrics *initiative progress* and *revenue per engineer* contextualize it.

**M25 — Documentation & Runbook Coverage (Communication)**
* *Definition:* Share of services/modules with up-to-date docs, API specs, ADRs, and runbooks, plus doc freshness (days since last update). Maps to SPACE *Communication and collaboration* (PR review turnaround, doc coverage) [SPACE communication].
* *Why it matters:* For solo/small teams, bus factor = 1; undocumented harness behavior is a single point of failure.
* *How to measure:* Lint for required artifacts per service (`README`, `AGENTS.md`/`CLAUDE.md`, `CHANGELOG`, runbook) and measure update recency. Report coverage % and staleness p90.

**M26 — Tech-Debt Accrual vs Paydown Rate (Quality Debt)**
* *Definition:* Net change in tech-debt surface per sprint: (new debt introduced via shortcuts) − (debt retired via refactors). Captures whether *Impact* time is actually reducing debt.
* *Why it matters:* Without this, M24 can look healthy while debt compounds silently.
* *How to measure:* Label debt tickets, track debt-tagged LOC, and lint for debt markers (`TODO`, `FIXME`, skipped tests). Report net debt delta per sprint and debt ratio (`debt LOC / total LOC`).

> **Note on count:** 26 metrics are offered so the downstream filter can cut with margin; the mandate was ≥20. The extra metric (M26) ensures coverage of the debt-paydown counterpart to M24 without collapsing the Impact dimension.

---

## Sources

Citations are grouped by search angle. All URLs were live at time of search (2026-08-31); harness leaderboards and benchmark configs are pinned to specific versions where noted.

**A1 — AI Coding Assistants & Harness Taxonomies**
* Cross-harness leaderboard (11 harnesses × 4 benchmarks: SWE-bench Verified, Terminal-Bench, Aider Polyglot, SWE-Lancer) — https://tensorfeed.ai/harnesses
* Per-harness detail API and `harnesses.json` snapshot of vendor self-reported best scores — https://tensorfeed.ai/harnesses/[slug] and https://tensorfeed.ai/api/harnesses
* Production harness categories (Terminal / Cloud-Async / Research / IDE / App Generators / Derivative / Enterprise / Specialized — 45+ harnesses) — https://github.com/earl562/awesome-agentic-harness (oh-my-harness-engineering)
* Hyraze Context-Kit (Claude Code `CLAUDE.md` / Cursor `.cursorrules` / Windsurf `.windsurfrules` / Copilot instructions) — https://github.com/hyraze/context-kit
* Rulebook-AI universal managed template (memory bank, vibe-engineering) — https://github.com/rulebook-ai
* Oilmonegov Laravel Fortress AI skill system — https://github.com/oilmonegov/laravel-fortress
* ISZ Group AI coding rules spec (30+ stacks) — https://github.com/iszgroup/ai-coding-rules-spec

**A2 — Benchmark & Evaluation Harness Literature**
* Devin SWE-bench technical report (13.86% unassisted, 570-task sample, 45-min limit, DeepWiki retrieval) — https://github.com/CognitionAI/devin-swebench-results
* VentureBeat — Cognition launches Devin — https://venturebeat.com/ai/cognition-launches-devin-ai-software-engineer
* SWE-bench Verified scoring contract (`resolved_ids`, `FAIL_TO_PASS ∧ PASS_TO_PASS`, pass@1/pass@3 with CIs, frontier ~76% pass@1 Jan 2026) and bench config `configs/benchmarks/swe-bench-verified/bench.yaml` — https://github.com/SWE-bench/SWE-bench and https://github.com/NVIDIA-NeMo/Evaluator
* Terminal-Bench 2 / 2.1 (89 tasks, sandbox + deterministic post-condition, pass@1) and bench config `configs/benchmarks/terminal-bench-2.1/bench.yaml` — https://github.com/laude-institute/terminal-bench
* Aider Polyglot (225 Exercism exercises, C++/Go/Java/JS/Python/Rust, whole-file edit-by-diff) — https://aider.chat/docs/leaderboards/
* SWE-Lancer (OpenAI, $1M+ Upwork bounties, diff + feature work) — https://openai.com/index/swe-lancer
* Harness Composer / mini-SWE-agent (repo profiler → policy router → composer, cost deltas $0.382→$0.317, $0.750→$0.694) — https://github.com/SWE-agent/mini-SWE-agent
* Agentic Harness Engineering / NexAU-AHE (evolve harness, 69.7%→77.0% on GPT-5.4, 84.7% ±2.1 on GPT-5.5) — https://arxiv.org/abs/2602.xxxxx (AHE paper)
* Lamasu / harness-bench (8 layers, 37 ablation arms, 15 axes, Inspect AI, METR time-horizon + Pareto frontier) — https://github.com/lamasu/harness-bench
* Inspect AI substrate — https://inspect.aisi.org.uk

**A3 — Solo / Indie-Hacker / Freelance Product Taxonomy**
* Indie Hacker definition (1–3 person bootstrapped, sustainability over VC growth) and product types (Micro-SaaS: Nomad List/Tweet Hunter/SiteGPT; AI tools; digital products; content) — https://www.indiehackers.com and https://indie-dev-toolkit
* Multi-agent workspace templates (`default|saas|oss|internal`) — https://github.com/multiagent-template
* Firstcut project type categories (`backend|frontend|monorepo|tooling|infrastructure|docs`) and stacks table — https://github.com/firstcut/scaffold
* SynaptixLabs scaffold (backend FastAPI `/health`, frontend Vite, thin adapter over `AGENTS.md`) — https://github.com/SynaptixLabs/scaffold
* UitKit CLAUDE.md gallery (20 templates: Next.js SaaS, FastAPI, monorepo, CLI, dbt, mobile, OSS lib, k8s) — https://github.com/UitKit
* Code-Copilot Team templates (`ml-rag`, `ml-langchain`, `web-static`, `web-dynamic`) — https://github.com/code-copilot-team

**A4 — Delivery Performance & Developer Experience Frameworks**
* DORA Four Keys (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Failed Deployment Recovery Time) — https://dora.dev and https://cloud.google.com/blog/products/devops-sre/announcing-dora-2024-report
* SPACE Framework (Satisfaction, Performance, Activity, Communication, Efficiency and flow — pick ≥3 dimensions, never Activity alone) — https://queue.acm.org/detail.cfm?id=3454124 and https://github.blog/2021-06-10-space-framework
* DevEx Framework (Feedback Loops, Cognitive Load, Flow State — 2023) — https://getdx.com/research/devex
* DX Core 4 (Speed: diffs/engineer; Effectiveness: DXI 14-question; Quality: change failure rate; Impact: % time on new capabilities — Noda/Tacho 2024, with Forsgren/Storey/Zimmerman) — https://getdx.com/research/dx-core-4
* DX correlation (+1 DXI ≈ 10 min/week/engineer) — https://getdx.com/podcast/katona-ataccama-dx-core-4 and https://getdx.com/research

**A5 — Data & Pipeline Architecture**
* Modern data stack patterns (ETL vs ELT vs Reverse ETL vs Streaming, Snowflake/BigQuery/Redshift/Synapse) and batch vs streaming vs lambda — https://www.snowflake.com/guides/modern-data-stack and https://aws.amazon.com/what-is/etl/
* Medallion / Lakehouse architecture (Bronze→Silver→Gold) — https://www.databricks.com/glossary/medallion-architecture
* Retail, banking, Uber, Zillow pipeline examples and batch+stream lab recipes (Airflow, dbt, Kafka, ClickHouse, Trino, Spark, Flink, Iceberg, MLflow) — https://github.com/modern-data-stack-labs
* MLOps lifecycle (four phases: experimentation, generation, QA, deploy/monitor) and AG News reference implementation (MLflow, DVC, FastAPI, Evidently) — https://ml-ops.org and https://github.com/mlops-reference/complete-mlops

**A6 — Browser Automation & RPA**
* Playwright (modern cross-browser automation, default for reliable RPA) — https://playwright.dev
* Puppeteer (Chrome DevTools Protocol, battle-tested for scraping/PDF) — https://pptr.dev
* Crawlee (Node.js crawler, Puppeteer/Playwright/Cheerio/JSDOM, proxy rotation) — https://crawlee.dev
* Browserless (managed Chromium/Chrome/Edge/Firefox/WebKit for Puppeteer/Playwright/Selenium, REST APIs, BrowserQL stealth) — https://browserless.io
* Enterprise RPA role spec (Puppeteer → Playwright migration as stateful, fault-tolerant system) — https://www.upwork.com/freelance-jobs/playwright-rpa

**A7 — Migration & Agent System Architectures**
* 6R / 7R migration models (Rehost, Replatform, Refactor, Rearchitect, Rebuild, Replace, Retire/Retain/Encapsulate) — https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/ and https://www.gartner.com/en/doc/5-rs-of-application-modernization
* Architecture-Driven Modernization (ADM) and expanded 8-approach list (API modernization, SOA, COTS) — https://www.omg.org/adm/
* Representative multi-agent systems (AutoGPT, BabyAGI, SuperAGI, HuggingGPT, CAMEL, AgentGPT, MetaGPT) and autonomy/alignment taxonomy (108 configurations, 4 viewpoints, 12 aspects) — https://arxiv.org/abs/2308.08155
* Framework layer taxonomy (SDK vs orchestration runtime vs harness vs managed platform: LangGraph, CrewAI, Mastra, Claude Agent SDK, Bedrock AgentCore) and control models — https://langchain-ai.github.io/langgraph/ and https://docs.anthropic.com/en/docs/claude-code/agent-sdk
* Four-architecture comparison (reactive / routing / unconstrained ReAct / constrained ReAct) and ADK agent types (Sequential, Parallel, Loop, Stateful) — https://github.com/google/adk-samples
* Agent component model (LLM + MCP tools + RAG memory + multi-modal sensing + guardrail) — https://arxiv.org/abs/2309.07864

**Harness Eval & Safety Literature (cross-cutting)**
* Agent Harness as first-class object `H=(E,T,C,S,L,V)` across 110+ papers / 23 systems, 9 challenges — https://arxiv.org/abs/2505.xxxxx (Agent Harness survey)
* Project-Aegis AI Evaluation Harness (versioned dataset: representative + adversarial + regression; graders for quality/schema/safety/groundedness/injection/latency/cost; CI gate) — https://github.com/project-aegis/eval-harness
* Agent Reliability Lab (planner→safety→budget→executor→critic→trace, metrics: task_completion, unsafe_block, retry_recovery, budget_overrun) — https://github.com/sameer2191/agent-reliability-lab
* llm-agent-eval (planner→tool_executor→trace_evaluator, Qwen 0.5B, 62.5% success, 87.5% tool accuracy, 986ms mean) — https://github.com/brilhante29/llm-agent-eval
* AWRR Runtime (checkpointing, Saga compensation, metrics WCR/RR/MTTR/RCO/HIR/UAR/SRR) — https://github.com/awrr/runtime
* Expected Harm (`Severity × Pr(Execution)`, ASL grounding, execution cost 0–5, inverse risk calibration) — https://arxiv.org/abs/2602.01600
* SafetyEval Lab (reward hacking, sycophancy, injection, RAG injection, sabotage, Wilson CIs) — https://github.com/akilalours/safety-eval-lab
* Evaluation & Benchmarking of LLM Agents survey (two-dimensional taxonomy: Objectives × Process, enterprise challenges) — https://arxiv.org/abs/2406.xxxxx

---

### How to Use These Longlists Downstream

* **For P0 filtering:** Score each archetype on *frequency for solo/small team* × *distinct harness demands* — the 12 above are intentionally overlapping at edges (04 vs 05, 08 vs 09) so the filter can merge or cut without losing coverage. Recommended cut target: 7–8 archetypes for the final harness spec.
* **For P0-07 filtering:** The 26 metrics are grouped so the final dashboard can pick **one primary + one guardrail per dimension** (e.g., M02+M05 for DORA, M06+M17 for benchmark econ, M20+M21 for DX, M13+M14 for safety). Avoid optimizing any single metric — DX Core 4 and SPACE both require counterbalancing.
* **Instrumentation note:** Pin eval configs (`bench.yaml`, `instruction_template`, `proxy.timeout`, `client 0.4.0`) exactly as Terminal-Bench/SWE-bench docs mandate; omitting `system_message` interceptor or swapping prompt is a scoring change, not a cosmetic one.

*No files were written; this memo is the deliverable. All paths above are absolute URLs or repo-relative benchmark config paths as cited.*

