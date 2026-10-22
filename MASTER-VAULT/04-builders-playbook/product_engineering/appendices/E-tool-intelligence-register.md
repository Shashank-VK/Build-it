# Appendix E — Tool Intelligence Register (merged)

**Source:** merge of `research/cases-product/12-tool-intelligence.md` (24 records, researched 2026-10-10, status checked against public sources as of that date) with the key records of `research/expansion-tools/` (18 stage files, 230 records, same date). Read-only research; neutral records — no rankings, no recommendations.

**Merge method:** one row per tool; where both streams recorded the same tool, the fuller record is canonical and the other is folded in as a merge note (no finding lost). Use labels: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Evidence labels preserved as assigned (Verified / Corroborated / Inferred / Proposed / Unknown). Status checked as of 2026-10-10.

---

## Part 1 — Records from the cases-product tool intelligence (TI-01–TI-24)

Dedupe map: TI-20 (Linear/Slack/Notion/Databricks/Datadog as agent context sources) → folded into the corresponding expansion rows as merge notes (Slack and Databricks have no expansion row and are retained here); TI-21 (Replit Agent) → merged into the expansion Replit row (DS-08); TI-23 (Backstage plugin ecosystem) → folded into the Backstage row below and cross-referenced. All other TI records are unique to this stream.

### PostgreSQL — ACTIVE
- **Purpose:** Open-source relational database; transactional core for ChatGPT/API and Stripe's ledger-adjacent workloads.
- **Maintenance:** Active (community releases; PostgreSQL 17/18 line current in 2026).
- **Limitations:** Single-primary write scaling ceiling; MVCC bloat/vacuum under heavy writes; replica fan-out cost (per OpenAI).
- **Real vs proposed use:** U(Verified) — OpenAI (single-primary + ~50 replicas, Jan 2026 disclosure); U(Verified) — Stripe (sharded Postgres in data layer, per secondary architecture narrative). Switching costs high at scale.
- **Record:** TI-01 · `research/cases-product/12-tool-intelligence.md`

### PgBouncer — ACTIVE
- **Purpose:** PostgreSQL connection pooler; cut OpenAI's connection setup 50ms→5ms.
- **Maintenance:** Active (long-standing community project, ISC licence).
- **Limitations:** Transaction-pooling mode restricts session-level features (prepared statements, advisory locks); runs with DB credentials — must be in the trust boundary.
- **Real vs proposed use:** U(Verified) — OpenAI (named in eng disclosure via reporting).
- **Record:** TI-02 · `research/cases-product/12-tool-intelligence.md`

### Azure Cosmos DB — ACTIVE
- **Purpose:** Globally distributed multi-model database; reported migration target for OpenAI's write-heavy/shardable workloads.
- **Maintenance:** Active commercial service (Microsoft Azure).
- **Limitations:** Cost-model complexity; consistency/latency trade-offs per API; high switching costs (data model + cloud lock-in).
- **Real vs proposed use:** U(Proposed) — reported as OpenAI's migration direction for shardable workloads (single secondary source); not verified as completed.
- **Record:** TI-03 · `research/cases-product/12-tool-intelligence.md`

### Codex CLI (openai/codex) — ACTIVE (governance caveat)
- **Purpose:** OpenAI's terminal coding agent; reads repos, edits files, runs commands in sandboxed loops; `codex exec` for CI/scripting; MCP support; AGENTS.md instructions.
- **Maintenance:** Active as of 2026 (rewritten TypeScript→Rust mid-2025; ~0.155 line, 1,100+ releases per Oct 2026 secondary review). **Notable:** repo reportedly no longer accepts external pull requests — open-source in licence, not in governance.
- **Limitations:** Trust-domain choices (sandbox modes); `--yolo` disables approvals (dangerous by design); no external PR acceptance limits community fixes.
- **Real vs proposed use:** U(Verified) — OpenAI uses it internally for its own development ("no private version," per product lead via press).
- **Record:** TI-04 · `research/cases-product/12-tool-intelligence.md`

### Claude Code — ACTIVE
- **Purpose:** Anthropic's agentic coding harness (CLI/desktop/IDE); MCP; filesystem-coordinated agent teams (experimental).
- **Maintenance:** Active; Dynamic Workflows research preview with Opus 4.8 (May 2026, single secondary source).
- **Limitations:** Context-window management is the discipline (per Anthropic's own guidance); privacy controls that also slow debugging (per Anthropic postmortem).
- **Real vs proposed use:** U(Verified) — Anthropic's own product; agent-team filesystem pattern documented by community.
- **Record:** TI-05 · `research/cases-product/12-tool-intelligence.md`

### MCP (Model Context Protocol) — ACTIVE
- **Purpose:** Open protocol for connecting agents to tools/data (servers expose schemas); Anthropic-originated, community-maintained open specification.
- **Maintenance:** Active; growing ecosystem in 2026.
- **Limitations:** Schema bloat inflates context/cost (Uber's 2026 cost work targeted exactly this); each server is a new attack surface — central policy enforcement via gateway recommended (Uber pattern).
- **Real vs proposed use:** U(Verified) — Uber routes 1,000+ MCP server interactions through a unified gateway (Sep 2026, via Uber eng blog reporting).
- **Record:** TI-06 · `research/cases-product/12-tool-intelligence.md`

### Chaos Monkey / Simian Army (Netflix) — RETIRED
- **Purpose:** Random instance termination to force failure-tolerant design (AWS; Spinnaker + MySQL dependencies per community docs).
- **Maintenance:** **SimianArmy: RETIRED** (official repo status, read 2026-10-10). Standalone Netflix/chaosmonkey exists but shows sparse recent activity — treat as low-maintenance; verify before use.
- **Limitations:** AWS/Spinnaker-coupled; retired suite has no support; terminates production instances by design — needs tight scoping/RBAC.
- **Real vs proposed use:** U(Verified) — Netflix (historical; suite retired, functionality moved to other Netflix projects).
- **Record:** TI-07 · `research/cases-product/12-tool-intelligence.md`

### Security Monkey (Netflix) — DEPRECATED (archived)
- **Purpose:** AWS security-posture monitoring (Apache-2.0).
- **Maintenance:** **Archived by owner Sep 17, 2021 — read-only.** Deprecated; do not adopt.
- **Limitations:** No support; superseded by Prowler, CloudSploit, AWS Security Hub, Wiz.
- **Real vs proposed use:** U(Verified) — Netflix (historical).
- **Record:** TI-08 · `research/cases-product/12-tool-intelligence.md`

### Backstage (Spotify → CNCF) — ACTIVE
- **Purpose:** Internal developer portal framework (service catalog, golden-path templates, docs-as-code); React/TypeScript frontend, Node backend (New Backend System stable since Sep 2024).
- **Maintenance:** Active — monthly releases (as of Sep 2026), 1,000+ contributors; CNCF Incubation; legacy backend removed Dec 2024.
- **Limitations:** Real adoption cost (React/Node platform team); golden-path secrets handling needs care (see CVE-2025-55285, Scaffolder fetch:template log flaw, fixed 2.1.1, Aug 2025 — keep updated; audit template inputs).
- **Real vs proposed use:** U(Verified) — Spotify (origin, ~90% daily internal usage reported); 3,400+ orgs per 2026 reporting. **Merge note:** TI-23 (Backstage observability/plugin ecosystem — Prometheus, Grafana, Datadog, PagerDuty, Kubernetes plugin) folded here: all active; U(Verified) as Backstage plugins in production IDPs (Corroborated via Backstage docs/ADR evidence). See also Grafana (OB-02), Datadog (OB-01), PagerDuty (IM-01) in Part 2.
- **Record:** TI-09 (+TI-23) · `research/cases-product/12-tool-intelligence.md`

### Sorbet (Stripe) — ACTIVE (status-check debt)
- **Purpose:** Gradual type checker for Ruby (Apache-2.0); gradual sigils; VS Code extension.
- **Maintenance:** Open-source project from Stripe; **2026 activity not verified in this pass — status check incomplete (debt).**
- **Limitations:** Gradual-typing overhead; ecosystem smaller than TypeScript.
- **Real vs proposed use:** U(Verified) — Stripe (Ruby monolith; first-party SED transcript + ex-employee accounts).
- **Record:** TI-10 · `research/cases-product/12-tool-intelligence.md`

### TypeScript — ACTIVE
- **Purpose:** Typed superset of JavaScript (Apache-2.0, Microsoft).
- **Maintenance:** Active.
- **Limitations:** Migration suppression debt (Stripe: 97k→37k suppressions); type-system soundness gaps; medium–high switching costs at millions of lines.
- **Real vs proposed use:** U(Verified) — Stripe Dashboard (3.7M+ lines migrated from Flow/JS).
- **Record:** TI-11 · `research/cases-product/12-tool-intelligence.md`

### React Native — ACTIVE
- **Purpose:** Cross-platform mobile (React → native); MIT (Meta); New Architecture (Fabric/JSI/TurboModules) from 0.76+.
- **Maintenance:** Active.
- **Limitations:** 2018-era bridge issues (async init, debugging) are the ones behind Airbnb's sunset; New Architecture changes the calculus; high switching costs (Airbnb's 3-platform-support lesson).
- **Real vs proposed use:** U(Verified) — Airbnb (2016–2018, sunset); U(Verified) — Shopify/Discord/Meta/Coinbase ship RN at scale per 2025 counter-analysis (Corroborated, not independently verified here).
- **Record:** TI-12 · `research/cases-product/12-tool-intelligence.md`

### Apache Kafka — ACTIVE
- **Purpose:** Distributed event streaming; Uber's GPS-ping shock absorber (Apache-2.0).
- **Maintenance:** Active.
- **Limitations:** Operational complexity (ZooKeeper/KRaft ops); exactly-once semantics need care; high switching costs (pipeline rewiring).
- **Real vs proposed use:** U(Verified) — Uber (driver location ingestion).
- **Record:** TI-13 · `research/cases-product/12-tool-intelligence.md`

### H3 (Uber) — ACTIVE (minor debt)
- **Purpose:** Hexagonal hierarchical geospatial index (Apache-2.0); libraries in multiple languages.
- **Maintenance:** Active (public repo; 2026 activity not re-verified this pass — minor debt).
- **Limitations:** Approximation by design; edge cases at cell boundaries.
- **Real vs proposed use:** U(Verified) — Uber (matching/ETA).
- **Record:** TI-14 · `research/cases-product/12-tool-intelligence.md`

### Schemaless (Uber) — ACTIVE (internal only)
- **Purpose:** Internal key-value-over-sharded-MySQL with buffered writes, triggers, global indexes.
- **Maintenance:** Internal (Uber); no public open-source release located — treat as not publicly available.
- **Limitations:** Not adoptable externally; schema-flexibility traded for query power.
- **Real vs proposed use:** U(Verified) — Uber (internal datastore; first-party eng blog).
- **Record:** TI-15 · `research/cases-product/12-tool-intelligence.md`

### EVCache (Netflix) — ACTIVE (debt)
- **Purpose:** Distributed in-memory cache (memcached-based) for low-latency reads.
- **Maintenance:** Public repo exists; **2026 activity not verified — debt.**
- **Limitations:** Cache-consistency design burden.
- **Real vs proposed use:** U(Verified) — Netflix.
- **Record:** TI-16 · `research/cases-product/12-tool-intelligence.md`

### Spinnaker (Netflix-origin) — ACTIVE
- **Purpose:** Multi-cloud continuous delivery (now community-governed; Netflix-origin); Kubernetes/VM targets.
- **Maintenance:** Active community project.
- **Limitations:** Heavyweight to operate; high switching costs.
- **Real vs proposed use:** U(Verified) — Netflix (chaos tooling dependency per community docs).
- **Record:** TI-17 · `research/cases-product/12-tool-intelligence.md`

### nginx / OpenResty + Lua — ACTIVE
- **Purpose:** Edge throttle (leaky bucket), queue page, signed cookies for flash-sale protection.
- **Maintenance:** Active (open source).
- **Limitations:** Lua scripting ops burden.
- **Real vs proposed use:** U(Verified) — Shopify (edge throttle per playbook citing Shopify eng blog).
- **Record:** TI-18 · `research/cases-product/12-tool-intelligence.md`

### MySQL / InnoDB — ACTIVE
- **Purpose:** Relational store under Schemaless and Shopify pods (GPL; commercial editions exist).
- **Maintenance:** Active.
- **Limitations:** Feature set vs Postgres for some workloads; operational sharding needed at scale; high switching costs at scale.
- **Real vs proposed use:** U(Verified) — Uber (Schemaless substrate); U(Verified) — Shopify (pod databases).
- **Record:** TI-19 · `research/cases-product/12-tool-intelligence.md`

### Slack / Databricks (agent context sources) — ACTIVE
- **Purpose:** Comms and data platforms consumed as agent context (from TI-20, which also covered Linear, Notion, Datadog — those folded into Part 2 rows PM-01, PM-10, OB-01 as merge notes).
- **Maintenance:** Active commercial SaaS.
- **Limitations:** Context bloat; access-permission sprawl when agents read everything; agent access = new insider-threat surface (scope tokens, audit reads).
- **Real vs proposed use:** U(Verified) — OpenAI (Codex context sources per Pragmatic Engineer interview).
- **Record:** TI-20 (partial; Linear/Notion/Datadog portions merged into Part 2) · `research/cases-product/12-tool-intelligence.md`

### GitHub Copilot (product + metrics APIs) — ACTIVE
- **Purpose:** AI pair programmer; code review agent; IDE plugins, CLI, metrics APIs (org/enterprise/user reports).
- **Maintenance:** Active; Rust runtime migration 2026 (single secondary source).
- **Limitations:** Acceptance ≠ quality; vendor-graded review metrics need independent benchmarks.
- **Real vs proposed use:** U(Verified) — GitHub (own product; telemetry published in peer-reviewed research).
- **Record:** TI-22 · `research/cases-product/12-tool-intelligence.md`

### Toxiproxy — ACTIVE (debt)
- **Purpose:** Chaos/fault-injection proxy for Game Days (Shopify-origin, MIT); TCP proxy with toxic behaviours (latency, down, bandwidth).
- **Maintenance:** Community-maintained; **2026 activity not re-verified — debt.**
- **Real vs proposed use:** U(Verified) — Shopify (Game Days).
- **Record:** TI-24 · `research/cases-product/12-tool-intelligence.md`

---

## Part 2 — Expansion-tools records by lifecycle stage (230 records)

Generated from the 18 stage files; one row per record. Merge notes flag where a cases-product TI record, forensics narrative, or cross-stream finding touches the same tool (no finding lost; the fuller record stays canonical).

## Stage: Coding agents & AI IDEs (`research/expansion-tools/01-coding-agents.md`)

### Cursor (Anysphere) — ACTIVE / CONTROVERSIAL
- **Purpose:** AI-first code editor (VS Code fork) with agent mode, tab completion, codebase chat; agent workflows for multi-step tasks.
- **Maintenance:** Active. Cursor 2.0 released Oct 2025 (parallel agents via git worktrees/remote machines). Claude Code v2.1.x-era comparisons list it at $20/mo Pro.
- **Limitations:** Agent cost is metered — heavy manual model selection drains the $20 credit pool in days; overage billed at API rates (no markup).
- **Real vs proposed use:** U(Verified) — Nvidia, Adobe, Uber, Shopify named as clients (thingshavehistory, 2026); ~4M active developers, ~50k enterprise customers (ai-news tracker citing TechCrunch).
- **Record:** EA-01 · `research/expansion-tools/01-coding-agents.md`

### Windsurf (Codeium) → Devin Desktop (Cognition) — ACTIVE (acquired, rebranded) / CONTROVERSIAL
- **Purpose:** Agentic IDE (VS Code fork lineage from Codeium); Cascade agent, multi-file editing; enterprise distribution.
- **Maintenance:** Active under Cognition. **Rebranded to Devin Desktop June 2026.**
- **Real vs proposed use:** U(Verified) — 350 enterprises pre-acquisition; Cognizant partnership Jan 2026 integrating Devin + Windsurf into Flowsource (Cognition blog).
- **Merge note:** Cognition's acquisition arc also appears in the forensics narrative (Cursor/Cognition context); Windsurf is named as a Codex CLI alternative in TI-04.
- **Record:** EA-02 · `research/expansion-tools/01-coding-agents.md`

### Devin (Cognition) — ACTIVE
- **Purpose:** Autonomous cloud "AI software engineer": ticket→PR on dedicated microVMs (own kernel, hypervisor-level snapshot/restore), plus Devin CLI/Local, Devin Desktop (ex-Windsurf IDE), API/MCP surface.
- **Maintenance:** Active. Series E Sep 2026: $2B+ raised @ **$48B valuation** (a16z, Accel); run-rate revenue $73M (Jul 2025) → $492M (May 2026) → ~$900M (Sep 2026) — company-reported, unaudited.
- **Limitations:** Closed model stack (no BYO keys); cloud-only brain (hosted on Azure); premium pricing.
- **Real vs proposed use:** U(Verified) — Goldman Sachs (first AI software engineer Jul 2025, scaling to thousands of instances per Forkast/CNBC); NVIDIA, GE Aerospace, Citi, Mercedes-Benz, Itaú (17k engineers); Cognizant (30% of code AI-generated, targeting 50%). RSA-260 factored Sep 2026 using GPU implementation built with Devin (Cognition).
- **Record:** EA-03 · `research/expansion-tools/01-coding-agents.md`

### Amazon Q Developer → Kiro — DEPRECATED (sunset in progress)
- **Purpose:** AWS AI coding assistant (ex-CodeWhisperer): completions, chat, security scanning in IDE.
- **Maintenance:** **DEPRECATED.** Primary source (AWS DevOps Blog): IDE plugins + paid subscriptions reach **end of support April 30, 2027**; **new signups blocked May 15, 2026** (free tier via Builder ID + new subscriptions); Opus 4.6 removed from Q Pro May 29, 2026 (Opus 4.5 remains; Opus 4.7+ exclusive to Kiro). Plugins remain listed with deprecation notice; critical bugfixes only through window.
- **Real vs proposed use:** U(Verified) — AWS's own product; enterprise AWS shops.
- **Merge note:** Amazon Q Developer deprecated: IDE plugins + paid subscriptions end of support Apr 30, 2027; new signups blocked May 15, 2026. Succeeded by Kiro (EA-11).
- **Record:** EA-04 · `research/expansion-tools/01-coding-agents.md`

### Continue.dev — SUPERSEDED (acquired, product discontinued)
- **Purpose:** Open-source AI coding assistant (VS Code/JetBrains extensions): autocomplete, chat, edit; connect any model; custom context (Jira/Confluence); "Hub" for sharing assistants.
- **Maintenance:** **Product discontinued after acquisition by Cursor** (reported Jun 24, 2026): users given **July 15 export deadline** before data deletion; recurring billing disabled; **codebase remains Apache-2.0** for community. Co-founder Nate Sesti joined Cursor; Ty Dunn had departed earlier. (Corroborated: startupnews.fyi; dev.to Jun 2026.)
- **Real vs proposed use:** U(Proposed) — was "loved by hundreds of thousands of developers" per company (vendor claim).
- **Merge note:** Acquired by Cursor (Jun 2026); product discontinued; codebase remains Apache-2.0.
- **Record:** EA-05 · `research/expansion-tools/01-coding-agents.md`

### Sourcegraph Cody / Amp — ACTIVE (enterprise-only; consumer tiers DEPRECATED)
- **Purpose:** Codebase-aware AI chat/completions/edits grounded in Sourcegraph code search; Amp is the agentic coding agent (split into separate company Dec 2025).
- **Maintenance:** Active for enterprise. Dec 2025: Sourcegraph and Amp became separate companies (Amp Inc. = coding agents; Sourcegraph = code search).
- **Limitations:** No standalone/free tier; enterprise-contract only; plan discontinuation alienated individual developers (community criticism).
- **Real vs proposed use:** U(Verified) — 4/6 top US banks, 15+ government agencies, Palo Alto Networks, Qualtrics (battle-card; treat customer claims as vendor-corroborated).
- **Record:** EA-06 · `research/expansion-tools/01-coding-agents.md`

### Cline (ex-Claude Dev) — ACTIVE
- **Purpose:** Open-source autonomous coding agent as IDE extension (VS Code/JetBrains) + CLI; plan→act loop with human-in-the-loop approvals; MCP extensible.
- **Maintenance:** Active. May 14, 2026: extracted `@cline/sdk` open-source TypeScript agent runtime (powers CLI + Kanban products); Terminal-Bench 2.0: Cline CLI 74.2% on claude-opus-4.7 vs 69.4% published for Claude Code (vendor/press claim — treat as Corroborated-weak).
- **Limitations:** BYO-key cost exposure; approval-gating adds friction at scale.
- **Real vs proposed use:** U(Proposed) — broad community adoption; no named enterprise customers located.
- **Record:** EA-07 · `research/expansion-tools/01-coding-agents.md`

### Aider — ACTIVE
- **Purpose:** Terminal AI pair programmer; git-native (AI edits committed with auto messages; diff/undo via git); repo-map via tree-sitter; any LLM via BYO key; polyglot benchmark leaderboard.
- **Maintenance:** Active — weekly release cadence (v0.82.1 era Apr 2026; 0.x versioning with occasional breaking CLI-flag changes). ~44k GitHub stars; ~6.8M PyPI installs; ~15B tokens/wk (per 2026 video review — Corroborated-weak). One-person bus factor is the structural risk; no SOC 2 (matters for team adoption).
- **Limitations:** 0.x instability; terminal-only; single maintainer.
- **Real vs proposed use:** U(Proposed) — individual developers; no named enterprise customers located. NOTE: one tracker (ai-whatchelin, 2026-08-12) claimed "no releases since Aug 2025" — contradicts weekly-cadence evidence; treat that claim as unreliable.
- **Record:** EA-08 · `research/expansion-tools/01-coding-agents.md`

### OpenHands (ex-OpenDevin) — ACTIVE (architecture in transition)
- **Purpose:** Open-source autonomous software-development agent platform (plan/code/test/PR in sandboxed Docker runtimes); event-sourced architecture; microagents; GitHub resolver action.
- **Maintenance:** Active but **mid-transition V0→V1**: Python harness last shipped tag 0.62.0; main repo repurposed into "Agent Canvas" (TypeScript/Electron control center); V1 agent core extracted to `software-agent-sdk` repo; V0 marked legacy with removal scheduled April 2026 (per Sep 2026 survey; treat date as Reported). SWE-bench 77.6% claimed (vendor/community). 25k+ stars.
- **Limitations:** Heavyweight architecture (maximal-harness design); transition creates migration uncertainty; Docker-socket access = root-equivalent (run on disposable infra).
- **Real vs proposed use:** U(Proposed) — research/community; no named enterprise production customers located.
- **Record:** EA-09 · `research/expansion-tools/01-coding-agents.md`

### Tabnine — ACTIVE (enterprise-only pivot)
- **Purpose:** Privacy-first AI code assistant: completions, chat, agents; private models; four deployment modes incl. fully air-gapped.
- **Maintenance:** Active; Gartner 2026 Magic Quadrant "Visionary" for Enterprise AI Coding Agents (vendor-credited claim).
- **Limitations:** Weaker raw generation vs Copilot/Cursor per third-party reviews; premium pricing.
- **Real vs proposed use:** U(Proposed) — defense/finance/healthcare positioning; no named customers located in this pass.
- **Merge note:** Named as a GitHub Copilot alternative in TI-22 (cases-product).
- **Record:** EA-10 · `research/expansion-tools/01-coding-agents.md`

### Kiro (AWS) — ACTIVE (successor product)
- **Purpose:** Spec-driven agentic IDE: write structured spec (requirements/design/tasks) → agent executes task graph; hooks, steering files, custom subagents, Powers; autonomous background agents opening PRs.
- **Maintenance:** Active. Announced Jul 2025; GA May 7, 2026. Latest models (Opus 4.7) exclusive to Kiro.
- **Limitations:** New product (2026); AWS-centric; pricing/migration tooling still maturing (per aitechconnect FAQ).
- **Real vs proposed use:** U(Verified) — AWS's strategic successor; adoption data not yet public.
- **Merge note:** The Kiro incident (agent autonomously deleting/rebuilding a production environment, 13-hour AWS Cost Explorer outage, Sep 2026) is forensically covered in the Amazon file (forensics/04-amazon.md) — see Appendix D.
- **Record:** EA-11 · `research/expansion-tools/01-coding-agents.md`

### Supermaven — SUPERSEDED (acquired, wound down)
- **Purpose:** AI code completion startup (fast inference).
- **Maintenance:** **Acquired by Cursor Nov 2024** (undisclosed sum); team folded in; **standalone product wound down late 2025**. (Wikipedia.)
- **Real vs proposed use:** Historical.
- **Merge note:** Acquired; wound down (superseded).
- **Record:** EA-12 · `research/expansion-tools/01-coding-agents.md`

### Gemini CLI — ACTIVE (with tier changes)
- **Purpose:** Google's open-source terminal coding agent (Apache-2.0); Gemini 2.5/3.x; built-in Google Search grounding; generous free tier (1,000 req/day personal).
- **Maintenance:** Active; bi-weekly releases. **Legacy individual tiers stop serving Jun 18, 2026** (per securityboulevard comparison, Jun 2026 — Corroborated-weak; verify before citing).
- **Real vs proposed use:** U(Proposed).
- **Record:** EA-13 · `research/expansion-tools/01-coding-agents.md`

### OpenCode — ACTIVE
- **Purpose:** Open-source terminal coding agent (MIT); 75+ models via BYO key; provider-agnostic.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EA-14 · `research/expansion-tools/01-coding-agents.md`

### SWE-agent / mini-swe-agent — ACTIVE (research reference)
- **Purpose:** Minimal academic agent harness (~190-line core for mini) for software-engineering tasks; the "minimal-harness" pole vs OpenHands' maximal design.
- **Maintenance:** Maintained as research artifact; widely forked.
- **Real vs proposed use:** U(Verified) — research community standard baseline. (Lightly researched — depth debt.)
- **Record:** EA-15 · `research/expansion-tools/01-coding-agents.md`


## Stage: Agent frameworks & orchestration runtimes (`research/expansion-tools/02-agent-frameworks.md`)

### LangChain / LangGraph — ACTIVE (narrative: "dead" — evidence: alive)
- **Purpose:** LLM app orchestration: chains, agents, tool calling, 1,000+ integrations (LangChain = DX layer); LangGraph = stateful graph execution runtime (Pregel/Beam-inspired) with durable state, checkpointing, human-in-the-loop interrupts.
- **Maintenance:** Active. **LangChain 1.0 + LangGraph 1.0 GA Oct 22, 2025**; langchain-core 1.6.6 / LangGraph 1.2.12 (Oct 2026 per Uvik guide). Since Oct 2025 `create_agent` runs on the LangGraph runtime under the hood — layered, not either/or.
- **Limitations:** Historical criticism — over-abstraction, opaque state, "debugging the framework instead of your logic"; 1.0 addressed part of it. Frontier model providers' native tool-calling reduced the original need.
- **Real vs proposed use:** U(Verified) — vendor claims 35% of Fortune 500 use it (self-reported; treat as Corroborated-weak); tens of millions of monthly downloads (cited in community analyses).
- **Merge note:** Narrative correction: NOT dead (1.0 GA Oct 2025, $125M raise).
- **Record:** AF-01 · `research/expansion-tools/02-agent-frameworks.md`

### Microsoft AutoGen — DEPRECATED (maintenance mode) → three-way split
- **Purpose:** Multi-agent conversation framework (Microsoft Research, Wu et al. 2023): conversable agents, group chat, code execution.
- **Maintenance:** **Maintenance mode since ~Oct 2025** — "stable API, critical bug fixes and security patches, no significant new features" (microsoft/autogen discussion #7066). Last feature line: 0.7.5 (Sep 2025). Microsoft redirects new users to Microsoft Agent Framework.
- **Real vs proposed use:** U(Verified) — historically one of the most-used multi-agent frameworks; existing enterprise codebases.
- **Merge note:** Deprecated (maintenance mode) → three-way split.
- **Record:** AF-02 · `research/expansion-tools/02-agent-frameworks.md`

### CrewAI — ACTIVE
- **Purpose:** Role-based multi-agent orchestration (agents with role/goal/backstory; crews with sequential/hierarchical/consensual processes); built-in eval tooling; AMP Suite commercial.
- **Maintenance:** Active — v1.15.22 (Sep 16, 2026); **LangChain dependency removed in v1.14** (now standalone/leaner).
- **Limitations:** Coarse-grained error handling; abstraction prioritizes simplicity over control — common prototype→LangGraph migration path reported.
- **Real vs proposed use:** U(Proposed) — 2B agent executions/12mo claimed (vendor); no named enterprises located in this pass.
- **Record:** AF-03 · `research/expansion-tools/02-agent-frameworks.md`

### Agno (ex-Phidata) — ACTIVE
- **Purpose:** "Fastest" multimodal agent framework + AgentOS self-hosted runtime (FastAPI runtime + control plane; data stays in your infra).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-04 · `research/expansion-tools/02-agent-frameworks.md`

### SmolAgents (Hugging Face) — ACTIVE
- **Purpose:** Minimal agent framework (code-first agents; ~1k lines); Hugging Face ecosystem native.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-05 · `research/expansion-tools/02-agent-frameworks.md`

### DSPy — ACTIVE
- **Purpose:** Programming (not prompting) language models: declarative LM pipelines compiled/optimized via metrics (Stanford NLP).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Verified) — research community; production use proposed. (Lightly researched — depth debt.)
- **Record:** AF-06 · `research/expansion-tools/02-agent-frameworks.md`

### Haystack (deepset) — ACTIVE
- **Purpose:** LLM/RAG pipeline framework (document search, retrieval pipelines); deepset commercial cloud.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-07 · `research/expansion-tools/02-agent-frameworks.md`

### LlamaIndex — ACTIVE
- **Purpose:** Data indexing + RAG framework (document loaders, indices, query engines); LlamaCloud managed parsing/indexing.
- **Maintenance:** Active.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-08 · `research/expansion-tools/02-agent-frameworks.md`

### Dify — ACTIVE
- **Purpose:** LLM app development platform (visual workflow builder, RAG pipelines, agent orchestration, model management); self-hostable.
- **Maintenance:** Active — fast release pace; established.
- **Limitations:** Ships on plain HTTP :80 (needs TLS/proxy in front); heavyweight stack.
- **Real vs proposed use:** U(Proposed). (Depth debt on license verification.)
- **Record:** AF-09 · `research/expansion-tools/02-agent-frameworks.md`

### Langflow — ACTIVE (acquired)
- **Purpose:** Visual drag-and-drop builder for LangChain/RAG/agent flows.
- **Maintenance:** Active under DataStax (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** AF-10 · `research/expansion-tools/02-agent-frameworks.md`

### Flowise — ACTIVE
- **Purpose:** Drag-and-drop UI for LangChain agent/chatflow building; self-hostable.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-11 · `research/expansion-tools/02-agent-frameworks.md`

### Rasa — MAINTAINED (ownership changed)
- **Purpose:** Open-source conversational AI framework (NLU dialogue management).
- **Maintenance:** Community-maintained; enterprise focus shifted.
- **Real vs proposed use:** U(Proposed). (Depth debt — verify current ownership/maintenance.)
- **Record:** AF-12 · `research/expansion-tools/02-agent-frameworks.md`

### AutoGPT — ACTIVE (narrative correction: NOT dead)
- **Purpose:** Autonomous agent platform (goal-driven agents, "go-do-it" model); plugin/provider registry; MCP provider path.
- **Maintenance:** **Active — commits within Sep 2026** (PR #14495 Sep 2026; billing fixes; LLM model retirement migrations; frontend Helm chart removed Dec 2025, Vercel-only deploy). The "AutoGPT is dead" narrative is false for the platform repo.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Narrative correction: NOT dead (platform repo active Sep 2026; only Auto-GPT-Plugins archived Jun 2024).
- **Record:** AF-13 · `research/expansion-tools/02-agent-frameworks.md`

### Pydantic AI — ACTIVE
- **Purpose:** Type-safe, Pythonic agent framework from the Pydantic team; lean alternative to LangChain.
- **Maintenance:** Active (2026); gaining share per community analyses.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-14 · `research/expansion-tools/02-agent-frameworks.md`

### Mastra — ACTIVE
- **Purpose:** TypeScript-native agent framework.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-15 · `research/expansion-tools/02-agent-frameworks.md`

### Strands (AWS) — ACTIVE
- **Purpose:** AWS open-source agent framework (model-driven, lightweight).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-16 · `research/expansion-tools/02-agent-frameworks.md`

### OpenAI Agents SDK / Swarm — ACTIVE
- **Purpose:** OpenAI's agent SDK (handoffs, guardrails; successor to experimental Swarm).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-17 · `research/expansion-tools/02-agent-frameworks.md`

### Claude Agent SDK (Anthropic) — ACTIVE
- **Purpose:** Anthropic's agent SDK (native state management, tool use, sub-agents; the harness behind Claude Code).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** AF-18 · `research/expansion-tools/02-agent-frameworks.md`

### Semantic Kernel — SUPERSEDED (consolidated)
- **Purpose:** Microsoft's enterprise LLM orchestration SDK (.NET/Python).
- **Maintenance:** Consolidated into **Microsoft Agent Framework** (same teams); do not start new projects on it.
- **Real vs proposed use:** U(Verified) — existing .NET enterprise codebases.
- **Merge note:** Superseded: consolidated into Microsoft Agent Framework.
- **Record:** AF-19 · `research/expansion-tools/02-agent-frameworks.md`

### BabyAGI — DEPRECATED (historical)
- **Purpose:** 2023 task-driven autonomous agent demo (Yohei Nakajima); vector-DB task loop.
- **Maintenance:** **Abandoned** — historical artifact of the 2023 agent hype wave.
- **Real vs proposed use:** Historical only. (Lightly researched — accepted as historical record.)
- **Merge note:** Deprecated (historical).
- **Record:** AF-20 · `research/expansion-tools/02-agent-frameworks.md`


## Stage: Testing (E2E, unit, load) (`research/expansion-tools/03-testing.md`)

### Playwright — ACTIVE
- **Purpose:** Cross-browser end-to-end testing (Chromium/Firefox/WebKit); auto-waiting, trace viewer, UI mode; now also a target for AI agents driving browsers.
- **Maintenance:** Active — **v1.62.1 (Jul 30, 2026)**.
- **Limitations:** Flakiness management still on the user; heavier than unit tests.
- **Real vs proposed use:** U(Verified) — ADRs in real repos (atlasppm ADR-0047, ispf-lab ADR-0006, raidan-ai testing SKILL; Sep 2026).
- **Record:** TE-01 · `research/expansion-tools/03-testing.md`

### Cypress — ACTIVE (financially stressed, shipping)
- **Purpose:** Developer-friendly browser E2E/component testing (Electron/Chromium runner, time-travel debugging).
- **Maintenance:** Active but turbulent: **20% layoffs Jan 2023; no Series C raised**; still shipping — **Cypress 16.0.0 (Sep 1, 2026)**. Financial stress is the watch item, not maintenance.
- **Limitations:** Single-tab, Chromium-centric historically (Firefox/WebKit support added later); Cloud pricing for parallelization.
- **Real vs proposed use:** U(Proposed).
- **Record:** TE-02 · `research/expansion-tools/03-testing.md`

### Selenium — MAINTAINED
- **Purpose:** The original browser-automation standard (WebDriver); grid for distributed runs.
- **Maintenance:** Maintained — **v4.48 (Aug 27, 2026)**; innovation pace slower than Playwright.
- **Real vs proposed use:** U(Verified) — legacy enterprise grids.
- **Record:** TE-03 · `research/expansion-tools/03-testing.md`

### Grafana k6 — ACTIVE (license caveat: AGPL-3.0)
- **Purpose:** Load testing as code (Go engine, JS/TS test scripts); thresholds fail builds on percentiles; browser module for Web-Vitals UX testing; cloud scale via Grafana Cloud.
- **Maintenance:** Active — **v2.2.0 (Aug 10, 2026)**; **k6 2.0 brought AI helpers** (`k6 x agent` script generation, `k6 x mcp` agent-run tests, `k6 x docs`, `k6 x explore`) and a serious browser-testing upgrade (Playwright-aligned APIs, `expect()` assertions).
- **Limitations:** AGPL-3.0; not a browser tool by default (browser mode separate, more expensive); cloud metering → runaway-test/runaway-invoice risk.
- **Real vs proposed use:** U(Verified) — ADRs in real repos (atlasppm ADR-0047, Sep 2026: k6 chosen for load baselines; raidan-ai testing SKILL).
- **Merge note:** License caveat: AGPL-3.0.
- **Record:** TE-04 · `research/expansion-tools/03-testing.md`

### Vitest — ACTIVE
- **Purpose:** Vite-native unit testing (ESM-first, fast, TS-first-class); the Jest successor in Vite/Next ecosystems.
- **Maintenance:** Active (2026).
- **Limitations:** Vite-ecosystem coupled.
- **Real vs proposed use:** U(Verified) — ADR in real repo (ispf-lab ADR-0006, Sep 11, 2026: "127 tests run in ~2 s").
- **Record:** TE-05 · `research/expansion-tools/03-testing.md`

### Jest — MAINTAINED
- **Purpose:** The incumbent JS unit-test framework (Meta).
- **Maintenance:** Maintained; mindshare shifting to Vitest.
- **Real vs proposed use:** U(Verified) — enormous legacy base.
- **Record:** TE-06 · `research/expansion-tools/03-testing.md`

### Gatling — ACTIVE
- **Purpose:** Scala/Java-based load testing; enterprise cloud offering.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** TE-07 · `research/expansion-tools/03-testing.md`

### Locust — ACTIVE
- **Purpose:** Python-based distributed load testing.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** TE-08 · `research/expansion-tools/03-testing.md`

### Detox — MAINTAINED
- **Purpose:** Gray-box E2E testing for React Native.
- **Maintenance:** Maintained (2026). (Depth debt on releases.)
- **Real vs proposed use:** U(Proposed).
- **Record:** TE-09 · `research/expansion-tools/03-testing.md`

### Maestro (mobile.dev) — ACTIVE
- **Purpose:** YAML-driven mobile UI testing (no SDK, no flakiness-prone selectors).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** TE-10 · `research/expansion-tools/03-testing.md`

### BrowserStack / Sauce Labs — ACTIVE
- **Purpose:** Real-device/browser cloud grids for cross-browser/mobile testing.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** TE-11 · `research/expansion-tools/03-testing.md`

### Chromatic (Storybook) — ACTIVE
- **Purpose:** Visual regression testing for Storybook (screenshot diffing, UI review).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** TE-12 · `research/expansion-tools/03-testing.md`

### MSW (Mock Service Worker) — ACTIVE
- **Purpose:** API mocking at the network level for tests and dev.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** TE-13 · `research/expansion-tools/03-testing.md`


## Stage: Feature flags & experimentation (`research/expansion-tools/04-feature-flags-experimentation.md`)

### LaunchDarkly — ACTIVE
- **Purpose:** Category-defining feature management: sophisticated targeting (rules, segments, scheduling), percentage rollouts, audit logging, experimentation add-ons.
- **Maintenance:** Active (2026).
- **Limitations:** Price reflects category leadership — expensive at scale; experimentation is an add-on, not native core.
- **Real vs proposed use:** U(Proposed) — widely adopted; no single named customer verified in this pass.
- **Record:** FF-01 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Split → Harness FME — ACTIVE (acquired, rebranded)
- **Purpose:** Feature flagging + experimentation with statistical engine for comparative experiments in production; audience segmentation.
- **Maintenance:** Active inside Harness; integration completed (Feb 2025: six new FME features announced).
- **Limitations:** Standalone Split customers must migrate into Harness platform; SDK naming lag creates confusion.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Split acquired by Harness (Jun 2024), rebranded FME.
- **Record:** FF-02 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Statsig — ACTIVE (acquired TWICE: OpenAI → Amplitude)
- **Purpose:** All-in-one product experimentation: feature flags, A/B testing, product analytics, session replay; 1T+ events/day claimed; Warehouse Native mode (BigQuery/Snowflake/Databricks/Redshift).
- **Maintenance:** not separately stated (see status line)
- **Limitations:** Roadmap ownership uncertainty post-double-acquisition; competitor migration guides actively target Statsig customers.
- **Real vs proposed use:** U(Verified) — Notion, Vercel named as customers (vendor/press); OpenAI itself used Statsig pre-acquisition.
- **Merge note:** Acquired twice: OpenAI $1.1B (Sep 2025) → Amplitude took brand/customers (May 2026); engineering team stayed at OpenAI.
- **Record:** FF-03 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Unleash — ACTIVE
- **Purpose:** Open-source feature management platform (self-host or managed); gradual rollouts, variants, constraints, segments, environments.
- **Maintenance:** Active. **$35M Series B Mar 2026** (One Peak; total $51.5M); 500+ paying customers; 13k+ GitHub stars; "FeatureOps" positioning for AI-generated code governance. Customers cited: Prudential, Lloyds Banking Group, Wayfair, Lenovo.
- **Limitations:** Self-hosting ops burden; experimentation not native (flags-first).
- **Real vs proposed use:** U(Verified) — Prudential, Lloyds Banking Group, Wayfair, Lenovo (vendor-cited).
- **Record:** FF-04 · `research/expansion-tools/04-feature-flags-experimentation.md`

### GrowthBook — ACTIVE
- **Purpose:** Open-source, warehouse-native experimentation + feature flags: Bayesian/frequentist/CUPED stats engine, sequential testing; no event-ingestion duplication (runs SQL against your warehouse).
- **Maintenance:** Active.
- **Limitations:** Most valuable with reliable warehouse/event data; governance/SSO on paid tiers; small-team overkill.
- **Real vs proposed use:** U(Proposed) — actively courting Statsig migrants post-acquisition.
- **Record:** FF-05 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Flagsmith — ACTIVE
- **Purpose:** Feature flags + remote config + segmentation with compliance/governance posture; self-hostable.
- **Maintenance:** Active (2026).
- **Limitations:** Self-hosting heavier (requires PostgreSQL); A/B testing leans on integrations (no built-in stats engine).
- **Real vs proposed use:** U(Proposed).
- **Record:** FF-06 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Flipt — ACTIVE
- **Purpose:** Lightweight open-source feature flag service (Go); Git-backed/declarative config; gRPC streaming updates.
- **Maintenance:** Active (2026); appears in OpenFeature provider evaluations.
- **Limitations:** Targeting less rich than LaunchDarkly/Unleash (per ADR comparison).
- **Real vs proposed use:** U(Proposed). (Depth debt: license + version verification.)
- **Record:** FF-07 · `research/expansion-tools/04-feature-flags-experimentation.md`

### flagd — ACTIVE
- **Purpose:** Reference OpenFeature-native feature flag daemon (CNCF-adjacent); file-backed, gRPC streaming; simplest self-hosted OpenFeature provider.
- **Maintenance:** Active (2026); recommended as default self-hosted provider in recent ADRs.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** FF-08 · `research/expansion-tools/04-feature-flags-experimentation.md`

### OpenFeature — ACTIVE (standard)
- **Purpose:** Vendor-neutral feature-flag API/SDK standard (CNCF); swap providers without changing application code.
- **Maintenance:** Active — spec v0.8.0 (early 2026); Node SDK v1.20.2; CNCF incubating→graduated (one source says graduated; treat maturity as Incubating+).
- **Limitations:** Standardizes the read path only, not flag authoring/governance; provider-specific features may not surface through the abstraction.
- **Real vs proposed use:** U(Proposed) — adoption pattern visible in 2025–2026 ADRs (LaunchDarkly→Flagsmith/Unleash/Flipt swaps).
- **Record:** FF-09 · `research/expansion-tools/04-feature-flags-experimentation.md`

### ConfigCat — ACTIVE
- **Purpose:** Developer-centric feature flag SaaS; simple setup; unlimited team size positioning.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** FF-10 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Eppo — ACTIVE
- **Purpose:** Warehouse-native experimentation (stats engine on your data warehouse).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** FF-11 · `research/expansion-tools/04-feature-flags-experimentation.md`

### Spotify Confidence — ACTIVE
- **Purpose:** Spotify's internal experimentation platform (15 years) productized; flags, experiments, CUPED (Negi–Wooldridge estimator), group sequential tests, sample-ratio-mismatch checks.
- **Maintenance:** Active (2026).
- **Limitations:** Newer commercial entrant vs Statsig/GrowthBook mindshare.
- **Real vs proposed use:** U(Verified) — Spotify (origin; 15 years internal).
- **Record:** FF-12 · `research/expansion-tools/04-feature-flags-experimentation.md`

### DevCycle — ACTIVE
- **Purpose:** Feature management with OpenFeature built into SDKs; edge architecture, local bucketing.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** FF-13 · `research/expansion-tools/04-feature-flags-experimentation.md`


## Stage: CI/CD & GitOps (`research/expansion-tools/05-cicd-gitops.md`)

### Dagger — ACTIVE (with a documented exit case)
- **Purpose:** Programmable CI engine: pipelines as TypeScript/Go/Python functions running in containers via BuildKit — same pipeline locally and in CI (`dagger call build`).
- **Maintenance:** Active (2026).
- **Limitations:** 4–12 hours to rewrite YAML pipelines as modules (per 2026 evaluation); distributed caching paywalled; another abstraction to debug.
- **Real vs proposed use:** U(Verified) — adopted by some; exited by others (both documented).
- **Record:** CI-01 · `research/expansion-tools/05-cicd-gitops.md`

### Depot — ACTIVE
- **Purpose:** Fast Docker builds: managed remote builders with persistent layer caching; GitHub Actions drop-in (`depot/build-push-action`); Turborepo remote cache on GHA runners.
- **Maintenance:** Active (2026); 2–10x faster Docker builds claimed (cache-dependent).
- **Limitations:** $20/mo hard to justify until Docker builds are a proven bottleneck (per 2026 evaluation); build infra is now a vendor dependency.
- **Real vs proposed use:** U(Verified) — evaluated/adopted in real repos (mattbutlerengineering CI/CD evaluation, Feb 2026).
- **Record:** CI-02 · `research/expansion-tools/05-cicd-gitops.md`

### Buildkite — ACTIVE
- **Purpose:** Hybrid CI/CD: pipelines in YAML (static or dynamically generated); agents run on your infra, UI in cloud.
- **Maintenance:** Active (2026).
- **Limitations:** You operate the agents (K8s agents, queues, admission control); dynamic pipeline generation is powerful but complex.
- **Real vs proposed use:** U(Verified) — shepherdjerred/monorepo ran Buildkite with Kueue admission (80Gi/24CPU) until the Jul 2026 CI strip.
- **Record:** CI-03 · `research/expansion-tools/05-cicd-gitops.md`

### Woodpecker CI — ACTIVE
- **Purpose:** Lightweight community CI engine; **fork of Drone** (post-license-change).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** CI-04 · `research/expansion-tools/05-cicd-gitops.md`

### Drone (Harness) — MAINTAINED
- **Purpose:** Container-native CI (was the OSS standard); now under Harness.
- **Maintenance:** Maintained under Harness (2026). (Depth debt on license/versions.)
- **Real vs proposed use:** U(Proposed).
- **Record:** CI-05 · `research/expansion-tools/05-cicd-gitops.md`

### Earthly — ACTIVE
- **Purpose:** "Makefile + Dockerfile" reproducible builds (Earthfiles); local/CI parity.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** CI-06 · `research/expansion-tools/05-cicd-gitops.md`

### GitHub Actions — ACTIVE
- **Purpose:** The default CI/CD for GitHub repos; 6,000+ marketplace actions; OIDC to clouds.
- **Maintenance:** Active (2026).
- **Limitations:** Runner minutes pricing; YAML sprawl; marketplace action supply-chain risk (pin SHAs).
- **Real vs proposed use:** U(Verified) — ubiquitous.
- **Record:** CI-07 · `research/expansion-tools/05-cicd-gitops.md`

### Argo CD — ACTIVE (GitOps standard)
- **Purpose:** Declarative GitOps continuous delivery for Kubernetes (desired-state in Git, drift detection, sync).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Verified) — GitOps standard alongside Flux.
- **Record:** CI-08 · `research/expansion-tools/05-cicd-gitops.md`

### FluxCD — ACTIVE (narrative correction: NOT archived)
- **Purpose:** GitOps for Kubernetes (source/helm/kustomize controllers).
- **Maintenance:** **Active — CNCF graduated**; the "Flux is archived/dead" narrative confuses Weaveworks' 2024 commercial shutdown with the project. (Per summary correction.)
- **Real vs proposed use:** U(Verified) — CNCF project.
- **Merge note:** Narrative correction: NOT archived (CNCF graduated).
- **Record:** CI-09 · `research/expansion-tools/05-cicd-gitops.md`

### Tekton — MAINTAINED
- **Purpose:** Kubernetes-native CI/CD building blocks (Pipelines, Triggers).
- **Maintenance:** Maintained (2026); slower innovation vs GitHub Actions.
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** CI-10 · `research/expansion-tools/05-cicd-gitops.md`

### Jenkins — MAINTAINED
- **Purpose:** The extensible automation server (1,800+ plugins).
- **Maintenance:** Maintained (2026); new projects rarely choose it.
- **Real vs proposed use:** U(Verified) — massive legacy installed base.
- **Record:** CI-11 · `research/expansion-tools/05-cicd-gitops.md`

### CircleCI — ACTIVE
- **Purpose:** Cloud-native CI/CD with Docker layer caching and parallelism.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** CI-12 · `research/expansion-tools/05-cicd-gitops.md`

### Harness — ACTIVE
- **Purpose:** AI-powered software delivery platform (CI, CD, feature flags via FME, cost governance); acquirer of Drone and Split.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** CI-13 · `research/expansion-tools/05-cicd-gitops.md`

### Spacelift — ACTIVE
- **Purpose:** CI/CD for infrastructure (Terraform, Pulumi, OpenTofu, CloudFormation).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** CI-14 · `research/expansion-tools/05-cicd-gitops.md`

### Travis CI — DEPRECATED (effectively)
- **Purpose:** Once the default OSS CI.
- **Maintenance:** **Effectively dead for OSS — free tier for open source killed Nov 2020**; exodus to GitHub Actions. (Per summary.)
- **Real vs proposed use:** Historical.
- **Merge note:** Deprecated (effectively).
- **Record:** CI-15 · `research/expansion-tools/05-cicd-gitops.md`


## Stage: Observability, monitoring & error tracking (`research/expansion-tools/06-observability.md`)

### Datadog — ACTIVE (CONTROVERSIAL: pricing)
- **Purpose:** All-in-one observability (infra, APM, logs, RUM, security); broadest integration catalog.
- **Maintenance:** Active (2026).
- **Limitations:** Cost at scale is THE limitation; per-host metering punishes label cardinality.
- **Real vs proposed use:** U(Verified) — enterprise standard.
- **Merge note:** Also recorded in cases-product TI-20 (Codex agent context source, U(Verified)) and TI-23 (Backstage plugin surface, U(Verified)).
- **Record:** OB-01 · `research/expansion-tools/06-observability.md`

### Grafana (LGTM stack: Loki/Grafana/Tempo/Mimir) — ACTIVE
- **Purpose:** OSS observability platform: metrics (Mimir/Prometheus), logs (Loki), traces (Tempo), dashboards; Grafana Cloud managed.
- **Maintenance:** Active (2026); k6 and Pyroscope under the same roof.
- **Limitations:** Three stores, three query languages (PromQL/LogQL/TraceQL) — correlation happens in the dashboard layer; self-operating the trio is real platform work (per Pydantic Logfire guide, 2026).
- **Real vs proposed use:** U(Verified) — Delivery Hero migration (1H25); de-facto OSS standard.
- **Merge note:** Also recorded in cases-product TI-23 as a Backstage plugin-surface component (U(Verified)).
- **Record:** OB-02 · `research/expansion-tools/06-observability.md`

### SigNoz — ACTIVE
- **Purpose:** OpenTelemetry-native, open-source Datadog alternative: traces, logs, metrics in one self-hosted app (ClickHouse-based, OTLP-native); APM views, dashboards, alerting; LLM observability over GenAI semantic conventions; SigNoz MCP + AI teammate (Cloud).
- **Maintenance:** Active (2026).
- **Limitations:** You operate ClickHouse + ingestion yourself (or pay for Cloud); ad-hoc analysis beyond the query builder = ClickHouse SQL against their schema.
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-03 · `research/expansion-tools/06-observability.md`

### Honeycomb — ACTIVE
- **Purpose:** Trace-first debugging of high-cardinality systems: wide events, "group by any attribute" investigation; OTLP ingest.
- **Maintenance:** Active (2026).
- **Limitations:** SaaS-only (data leaves your infra); proprietary query model (skills/questions are Honeycomb-shaped); pricing meters events + metric datapoints + processing separately.
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-04 · `research/expansion-tools/06-observability.md`

### Sentry — ACTIVE (license saga)
- **Purpose:** Error tracking + performance monitoring + session replay; dev-workflow native (issue → fix).
- **Maintenance:** Active (2026).
- **Limitations:** Won't watch your servers (pairs with Grafana Cloud/Better Stack per 2026 guides); license restricts competitive hosting.
- **Real vs proposed use:** U(Verified) — ubiquitous in web/mobile.
- **Merge note:** License saga: BSD-3 → BSL → FSL (see Appendix B §2).
- **Record:** OB-05 · `research/expansion-tools/06-observability.md`

### Highlight — ACTIVE
- **Purpose:** Open-source full-stack monitoring: error monitoring, session replay, logging, distributed tracing.
- **Maintenance:** Active (2026). (Depth debt on versions.)
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-06 · `research/expansion-tools/06-observability.md`

### New Relic — ACTIVE
- **Purpose:** All-in-one observability, usage-based; 100 GB free ingest/mo; no per-host fee.
- **Maintenance:** Active; PE-owned since **$6.5B take-private (Jul 2023)**.
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-07 · `research/expansion-tools/06-observability.md`

### Lightstep (ServiceNow) — MAINTAINED
- **Purpose:** Distributed-tracing-first observability (OpenTelemetry pioneers).
- **Maintenance:** Maintained inside ServiceNow's observability story (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-08 · `research/expansion-tools/06-observability.md`

### OpenTelemetry — ACTIVE (standard)
- **Purpose:** The vendor-neutral telemetry standard (traces/metrics/logs; Collector; semantic conventions incl. GenAI).
- **Maintenance:** Active (2026); the substrate everything above integrates with.
- **Real vs proposed use:** U(Verified) — industry standard.
- **Record:** OB-09 · `research/expansion-tools/06-observability.md`

### Better Stack — ACTIVE
- **Purpose:** Uptime monitoring + on-call + status pages + telemetry bundles; the "two-person team" pick in 2026 guides.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-10 · `research/expansion-tools/06-observability.md`

### Last9 — ACTIVE
- **Purpose:** BYOC observability: high-cardinality telemetry with cost control at ingestion; one license, infra on your cloud bill; no charge per label/metric name.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** OB-11 · `research/expansion-tools/06-observability.md`

### Pydantic Logfire — ACTIVE
- **Purpose:** LLM/Python-native observability from the Pydantic team; OTel-based.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** OB-12 · `research/expansion-tools/06-observability.md`

### Checkly — ACTIVE
- **Purpose:** Synthetic monitoring + API checks as code (Playwright-based checks).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** OB-13 · `research/expansion-tools/06-observability.md`


## Stage: Incident management, on-call & status (`research/expansion-tools/07-incident-management.md`)

### PagerDuty — ACTIVE (stagnant-growth, restructuring)
- **Purpose:** On-call management, alert routing/escalation, event intelligence/AIOps, incident response automation (Operations Cloud, being rebranded "PD Reliability Platform").
- **Maintenance:** Active. Q2 FY27 (ended Jul 31, 2026): ARR **$501M** (first time over $500M), revenue $124.4M (+0.8% YoY), 15,506 paid customers, 884 customers >$100k ARR, dollar-based net retention 98% (inflection after quarters of erosion), 5th consecutive GAAP-profitable quarter. **15% workforce reduction (~173 of 1,155) announced Aug 2026** — concentrated in non-customer-facing roles; restructuring charges $5.
- **Limitations:** Growth essentially flat; expensive add-on model vs newer bundled competitors; not Slack-native at its core.
- **Real vs proposed use:** U(Verified) — Twilio, Anthropic, CoreWeave, Anduril, Palo Alto Networks, Delivery Hero, GM, Perplexity (vendor earnings).
- **Merge note:** Also recorded in cases-product TI-23 as a Backstage plugin-surface component (U(Verified)).
- **Record:** IM-01 · `research/expansion-tools/07-incident-management.md`

### Atlassian Opsgenie — DEPRECATED (sunset Apr 5, 2027)
- **Purpose:** Alerting and on-call scheduling with deep Atlassian integration.
- **Maintenance:** **End of sale Jun 4, 2025; service shutdown Apr 5, 2027.** Migrations directed to Jira Service Management alerting/ops.
- **Real vs proposed use:** U(Verified) — existing Atlassian shops in migration planning.
- **Merge note:** Sunset Apr 5, 2027 (Atlassian).
- **Record:** IM-02 · `research/expansion-tools/07-incident-management.md`

### incident.io — ACTIVE (independent)
- **Purpose:** Slack-native all-in-one incident management: on-call (40+ alert sources), incident response, status pages; AI SRE for investigation, triage, RCA, drafted fixes, call transcription, auto post-mortems.
- **Maintenance:** Active; independent (not acquired). Cited customers: Netflix, Airbnb (per community sources, Corroborated-weak).
- **Limitations:** Proprietary; on-call is an add-on to per-seat pricing; no self-host.
- **Real vs proposed use:** U(Proposed) — widely regarded in 2026 buyer's guides; named customers via vendor/community claims.
- **Record:** IM-03 · `research/expansion-tools/07-incident-management.md`

### Rootly — ACTIVE (independent, AI-native)
- **Purpose:** AI-native incident management platform: Incident Response, On-Call, and a dedicated AI SRE product (confidence-scored RCA, similar-incident surfacing, suggested fixes, AI meeting bot for incident bridges, reasoning trace shown before acting).
- **Maintenance:** Active; independent. Cited users: NVIDIA, Replit, Canva, Cisco (per Rootly positioning; Corroborated-weak).
- **Limitations:** Proprietary; pricing sales-led for AI tier.
- **Real vs proposed use:** U(Proposed).
- **Record:** IM-04 · `research/expansion-tools/07-incident-management.md`

### FireHydrant — ACTIVE (acquired by Freshworks)
- **Purpose:** Incident management with service-catalog-driven runbook automation; Signals (on-call); status pages; AI summaries/transcription/retrospectives.
- **Maintenance:** not separately stated (see status line)
- **Limitations:** AI locked to Enterprise; no autonomous investigation; roadmap now inside Freshworks.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Acquired by Freshworks (Dec 2025/Jan 2026).
- **Record:** IM-05 · `research/expansion-tools/07-incident-management.md`

### Grafana OnCall / IRM — ACTIVE (consolidated)
- **Purpose:** OSS-friendly on-call + incident response inside the Grafana stack (now Grafana IRM: on-call, incidents, status pages).
- **Maintenance:** Active (2026).
- **Limitations:** Narrower than PagerDuty feature set; best inside Grafana shops.
- **Real vs proposed use:** U(Proposed). (Depth debt — verify current naming: OnCall → IRM consolidation.)
- **Record:** IM-06 · `research/expansion-tools/07-incident-management.md`

### Squadcast — ACTIVE
- **Purpose:** SRE-focused on-call + incident response (Squadcast Reliability Workflow).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** IM-07 · `research/expansion-tools/07-incident-management.md`

### xMatters (Everbridge) — ACTIVE
- **Purpose:** Intelligent alerting/on-call; Everbridge critical-event management.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** IM-08 · `research/expansion-tools/07-incident-management.md`

### Statuspage (Atlassian) — ACTIVE
- **Purpose:** Hosted status pages + incident communication.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** IM-09 · `research/expansion-tools/07-incident-management.md`

### Cachet / cState — MAINTAINED (OSS status pages)
- **Purpose:** Self-hosted open-source status pages (Cachet: PHP; cState: static/Hugo-based).
- **Maintenance:** Community-maintained (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** IM-10 · `research/expansion-tools/07-incident-management.md`


## Stage: Design, prototyping & front-end generation (`research/expansion-tools/08-design-prototyping.md`)

### Figma — ACTIVE (post-IPO, post-Adobe-deal, CONTROVERSIAL on trust/AI)
- **Purpose:** Browser-based collaborative product design + prototyping + design systems; now expanding into a full "idea → product" platform (Design, FigJam, Dev Mode, Slides, Draw, Make, Sites, Buzz).
- **Maintenance:** Active. Timeline of verified events:
- **Limitations:** Proprietary file format; vendor lock-in; seat-based pricing; AI features priced on paid tiers; sprawling product surface (trust concern about beta features ever maturing).
- **Real vs proposed use:** U(Verified) — dominant share (80%+ vs Adobe XD 5–10% per 2026 analyses); named enterprise users: NAB, SafetyCulture, Atlassian (AU data residency); 80%+ of customers use 2+ products.
- **Merge note:** Post-IPO (Jul 2025, $68B); $20B Adobe deal killed Dec 2023 ($1B fee); stock ~$19 by Jun 2026; AI-training class action (Khan v. Figma, Nov 2025).
- **Record:** DS-01 · `research/expansion-tools/08-design-prototyping.md`

### Penpot — ACTIVE (open-source challenger, EU-backed)
- **Purpose:** Open-source, self-hostable design + prototyping platform on open web standards (SVG/CSS/HTML/JSON); "design as code"; W3C-aligned design tokens (DTCG), CSS Grid/Flex layouts; official MCP server for AI-agent read/write of design files (merged into main monorepo at v2.16).
- **Maintenance:** Active. GitHub Trending Jun 21, 2026; releases through 2026 (self-host via Docker).
- **Limitations:** Plugin/third-party ecosystem smaller than Figma's; MCP rides a browser session (no persistent server process — CI-driven sync must use REST, per a Jul 2026 ADR).
- **Real vs proposed use:** U(Verified) — ADRs in real repos (penpot-throughline, 2026-07-14: "remove Figma license dependency"; RallyOn design-token workflow, Jul 2026).
- **Record:** DS-02 · `research/expansion-tools/08-design-prototyping.md`

### v0 (Vercel) — ACTIVE
- **Purpose:** Prompt-to-UI generation tuned for React/Next.js: production-ready React + Tailwind + shadcn/ui components; Design Mode visual edits; GitHub sync; deploys to Vercel.
- **Maintenance:** Active (2026); part of Vercel's AI platform push.
- **Limitations:** Frontend-only (no backend generation); Vercel deployment lock-in for one-click flow (hosting billed separately).
- **Real vs proposed use:** U(Proposed) — considered the code-quality reference in the category.
- **Record:** DS-03 · `research/expansion-tools/08-design-prototyping.md`

### Lovable — ACTIVE
- **Purpose:** Prompt-to-full-stack-app: frontend + backend + auth + database (auto-wired Supabase), hosting included; aimed at non-technical builders.
- **Maintenance:** Active (2026).
- **Limitations:** Generated apps can be "monolithic," need refactoring at scale; credit-burn cost complaints; vendor lock-in for hosting (code export available).
- **Real vs proposed use:** U(Proposed) — massive user base; no named enterprise verified in this pass.
- **Record:** DS-04 · `research/expansion-tools/08-design-prototyping.md`

### Bolt.new (StackBlitz) — ACTIVE
- **Purpose:** AI web-dev agent in the browser (WebContainers): full filesystem access, live code execution, error self-repair; multi-framework (React, React Native/Expo — the only one in class supporting mobile).
- **Maintenance:** Active (2026).
- **Limitations:** Token metering scales with project size; backend partial (BYO).
- **Real vs proposed use:** U(Proposed).
- **Record:** DS-05 · `research/expansion-tools/08-design-prototyping.md`

### bolt.diy — ACTIVE (community OSS fork)
- **Purpose:** Self-hosted, any-LLM variant of the Bolt.new prompt-to-app builder.
- **Maintenance:** Active (2026).
- **Limitations:** Community support; feature lag vs commercial Bolt.new.
- **Real vs proposed use:** U(Proposed).
- **Record:** DS-06 · `research/expansion-tools/08-design-prototyping.md`

### Dyad — ACTIVE
- **Purpose:** Local-first open-source AI app builder (dyad-sh/dyad); alternatives to cloud vibe-coding tools.
- **Maintenance:** Active (2026; HN Show HN traction).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DS-07 · `research/expansion-tools/08-design-prototyping.md`

### Replit Agent — ACTIVE
- **Purpose:** Cloud IDE + AI agent (Agent 4, parallel tasks): writes, tests, deploys full-stack apps; zero-setup built-in services (auth, DB, hosting); imports from Bolt/Lovable/Figma.
- **Maintenance:** Active (2026).
- **Limitations:** **Pricing complaints — ~$55 per app generation cited as expensive vs competitors**; 2025 effort-pricing + Agent 3 credit-burn backlash (per summary).
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Merged with cases-product TI-21 (Replit Agent platform): post-Jul-2025 guardrails (automatic dev/prod separation, staging envs, chat-only mode); agent root-cause ability at infra layer is weak (Helium postmortem); pre-2025 design allowed prod DB access from dev (U(Verified) — Replit).
- **Record:** DS-08 · `research/expansion-tools/08-design-prototyping.md`

### Base44 — ACTIVE (acquired by Wix)
- **Purpose:** Prompt-to-app builder (no-code AI apps).
- **Maintenance:** Active under Wix.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DS-09 · `research/expansion-tools/08-design-prototyping.md`

### Framer — ACTIVE
- **Purpose:** Design-to-site publishing (Figma-like canvas → live site), CMS, AI generation features.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DS-10 · `research/expansion-tools/08-design-prototyping.md`

### Webflow — ACTIVE
- **Purpose:** Visual web development platform (designer → CMS → hosting).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DS-11 · `research/expansion-tools/08-design-prototyping.md`

### Sketch — MAINTAINED (niche)
- **Purpose:** Mac-native vector UI design (the pre-Figma incumbent).
- **Maintenance:** Maintained (2026); cross-platform reach lost to Figma/Penpot.
- **Limitations:** Mac-only; file-lock-in; plugin ecosystem aging.
- **Real vs proposed use:** U(Proposed).
- **Record:** DS-12 · `research/expansion-tools/08-design-prototyping.md`

### Lunacy (Icons8) — ACTIVE
- **Purpose:** Free native design app (Windows/macOS/Linux) reading .sketch files.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DS-13 · `research/expansion-tools/08-design-prototyping.md`

### Modyfi — SUPERSEDED (acquired by Figma)
- **Purpose:** Browser-based motion design tool.
- **Maintenance:** **Acquired by Figma (2026)** — standalone future uncertain; folded into Figma's motion push.
- **Real vs proposed use:** Historical.
- **Merge note:** Superseded: acquired by Figma (2026).
- **Record:** DS-14 · `research/expansion-tools/08-design-prototyping.md`

### Payload CMS — SUPERSEDED (acquired by Figma)
- **Purpose:** Headless CMS (TypeScript).
- **Maintenance:** **Acquired by Figma (2026)** — backing Figma Sites' CMS.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Superseded: acquired by Figma (2026).
- **Record:** DS-15 · `research/expansion-tools/08-design-prototyping.md`

### Adobe XD — DEPRECATED (effectively)
- **Purpose:** Adobe's desktop UI design tool.
- **Maintenance:** Effectively abandoned post-Figma-deal-collapse (5–10% share vs Figma 80%+); Adobe's design focus shifted to competing via other products.
- **Real vs proposed use:** U(Verified) — legacy enterprise installs.
- **Merge note:** Deprecated (effectively).
- **Record:** DS-16 · `research/expansion-tools/08-design-prototyping.md`


## Stage: Documentation & developer portals (`research/expansion-tools/09-documentation.md`)

### Mintlify — ACTIVE (acquiring; repriced 2026)
- **Purpose:** Hosted docs-as-a-service: MDX-based docs sites with AI-assisted writing, API references from OpenAPI, custom React components, analytics.
- **Maintenance:** Active; **acquired Helicone (Mar 3, 2026)** — expanding from docs into AI/LLM observability.
- **Limitations:** Vendor lock-in (hosted, proprietary); migration cost high (conversion + lock-in per 2026 evaluation); AI extraction but no docstring renderer.
- **Real vs proposed use:** U(Verified) — Trophy (dev.to case study) chose Mintlify for docs while managing SDKs with Fern.
- **Merge note:** Acquiring (Helicone); repriced 2026.
- **Record:** DC-01 · `research/expansion-tools/09-documentation.md`

### Fern — ACTIVE (acquired by Postman; OSS future unclear)
- **Purpose:** API-first docs + SDK generation from an API definition (Fern definition or OpenAPI).
- **Maintenance:** Under Postman (2026); watch for roadmap absorption into Postman's API platform.
- **Limitations:** Post-acquisition uncertainty; historically Fern-definition vs OpenAPI portability debate.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Acquired by Postman (Jan 2026); OSS future unclear.
- **Record:** DC-02 · `research/expansion-tools/09-documentation.md`

### Docusaurus — MAINTAINED (v4 stalled; feature freeze)
- **Purpose:** React-based static docs sites with versioning, i18n (Meta).
- **Maintenance:** **Effectively feature-frozen on v3**: last stable **v3.9.2 (Oct 17, 2025)**; v4 umbrella issue (opened Feb 6, 2026) only **20% complete** (6/30), requires Node 24+/React 19.2+/TS 6+/Rspack v2 — no timeline announced. 64k stars, 414k npm/week, but migration momentum away is documented: Glasskube/Distr → Starlight (HN, May 2025), others → Fumadocs (OpenAPI, customization); 30+ minute builds on large
- **Limitations:** Build performance at scale; v3 feature freeze; plugin maintenance costs estimated $500–2,000/mo (Featurebase).
- **Real vs proposed use:** U(Verified) — still the category star-count leader; widely deployed.
- **Record:** DC-03 · `research/expansion-tools/09-documentation.md`

### Starlight (Astro) — ACTIVE
- **Purpose:** Performance-first docs framework (Astro): zero client JS, 12kB bundle, 0.8s LCP.
- **Maintenance:** Active (2026); 2x YoY growth; the DX/performance leader per 2026 analyses.
- **Limitations:** Documentation-only (no marketing pages); no versioned docs (per community review); smaller npm footprint than Fumadocs.
- **Real vs proposed use:** U(Verified) — Glasskube/Distr migration (HN May 2025, 58 pts).
- **Record:** DC-04 · `research/expansion-tools/09-documentation.md`

### Fumadocs — ACTIVE
- **Purpose:** Next.js-based docs framework; strong OpenAPI + customization story.
- **Maintenance:** Active (2026); leading Starlight on npm downloads.
- **Real vs proposed use:** U(Proposed).
- **Record:** DC-05 · `research/expansion-tools/09-documentation.md`

### VitePress — ACTIVE
- **Purpose:** Vue-powered static docs (Vite); 17k stars, 218k npm/week.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** DC-06 · `research/expansion-tools/09-documentation.md`

### MkDocs Material — ACTIVE (maintenance-mode claim disputed)
- **Purpose:** Pythonic docs (Markdown + mkdocstrings); huge polish.
- **Maintenance:** A 2026 catalog claimed "maintenance mode" — **the underlying evidence disputes it** (26k stars, 1 open issue cited as counter-evidence). Treat as active; the "maintenance mode" claim is contested.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Maintenance-mode claim disputed.
- **Record:** DC-07 · `research/expansion-tools/09-documentation.md`

### Scalar — ACTIVE (rising)
- **Purpose:** Modern API reference docs (OpenAPI); 14k stars; momentum vs Swagger UI stagnation.
- **Maintenance:** Active (2026); ranked as potentially #1–2 in API docs subcategory by 2026 momentum.
- **Real vs proposed use:** U(Proposed).
- **Record:** DC-08 · `research/expansion-tools/09-documentation.md`

### DocsGPT — ACTIVE (AI-native wave)
- **Purpose:** Open-source AI docs assistant (18k stars): chat over docs, AI-generated documentation.
- **Maintenance:** Active (2026); early leader of the AI-native docs wave (with Promptless YC W25, Context7).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DC-09 · `research/expansion-tools/09-documentation.md`

### GitBook — ACTIVE
- **Purpose:** Hosted docs collaboration with Git sync.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** DC-10 · `research/expansion-tools/09-documentation.md`

### ReadMe — ACTIVE
- **Purpose:** Interactive API docs hub with analytics.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DC-11 · `research/expansion-tools/09-documentation.md`

### llms.txt — EXPERIMENTAL (emerging standard)
- **Purpose:** Proposed standard (Sep 2024→) for AI-consumable documentation (a /llms.txt manifest for agents).
- **Maintenance:** Emerging; slow adoption through 2026.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** DC-12 · `research/expansion-tools/09-documentation.md`


## Stage: Product & web analytics (`research/expansion-tools/10-analytics.md`)

### PostHog — ACTIVE
- **Purpose:** All-in-one product analytics for developers: event tracking/autocapture, funnels, session replay, feature flags, experiments, surveys, data warehouse — one SDK.
- **Maintenance:** Active. **Sacra (2026): $57.5M revenue, $1.4B valuation, $182M raised, 138% YoY growth.**
- **Limitations:** Event volume (not users) drives cost — cap volume early; self-host production path de-emphasized.
- **Real vs proposed use:** U(Verified) — ADRs in real repos (thaichess ADR-0003, Jul 31, 2026: chose PostHog free cloud over Plausible Cloud/Umami; ResumeSpyWeb issue #65, May–Jun 2026: Plausible/Umami + PostHog stack adopted).
- **Record:** AN-01 · `research/expansion-tools/10-analytics.md`

### Amplitude — ACTIVE (absorbed Statsig brand)
- **Purpose:** Enterprise product analytics: behavioral cohorts, experimentation, CDP; aggressive AI-agent push in 2026 (agents sifting usage data, auto-recommendations).
- **Maintenance:** Active; **took over the Statsig brand and customer base (May 2026)** while Statsig's engineering team stayed at OpenAI.
- **Real vs proposed use:** U(Proposed).
- **Record:** AN-02 · `research/expansion-tools/10-analytics.md`

### Mixpanel — ACTIVE
- **Purpose:** Self-serve event analytics: funnels/retention, AI Copilot, **warehouse-native (Mirror)**.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** AN-03 · `research/expansion-tools/10-analytics.md`

### Plausible — ACTIVE (bootstrapped, EU)
- **Purpose:** Privacy-first web analytics: cookieless, no consent banner, 2.5KB script, single-page dashboard.
- **Maintenance:** Active (2026).
- **Limitations:** CE self-host is "free of licensing cost, not free of operating cost" (ClickHouse + Postgres + backups); funnels only on top tiers.
- **Real vs proposed use:** U(Verified) — thaichess ADR evaluated Plausible (consent-gated wiring existed); ResumeSpyWeb adopted Plausible/Umami for pageviews.
- **Record:** AN-04 · `research/expansion-tools/10-analytics.md`

### Umami — ACTIVE
- **Purpose:** Minimal self-hosted web analytics (deliberately bare); deploys to Vercel/Railway in minutes.
- **Maintenance:** Active (2026).
- **Limitations:** Bare feature set (no funnels/replay depth).
- **Real vs proposed use:** U(Verified) — ResumeSpyWeb issue #65 (2026).
- **Record:** AN-05 · `research/expansion-tools/10-analytics.md`

### Fathom — ACTIVE
- **Purpose:** Simple privacy-first analytics; entry $15/mo (100k pageviews, 50 sites).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** AN-06 · `research/expansion-tools/10-analytics.md`

### Matomo — ACTIVE
- **Purpose:** Full-suite self-hostable analytics (heatmaps, session recording, goals); 15-year track record; the regulated-industry pick.
- **Maintenance:** Active (2026).
- **Limitations:** Heaviest of the group to run.
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** AN-07 · `research/expansion-tools/10-analytics.md`

### Heap — ACTIVE
- **Purpose:** Automatic data capture (autocapture) product analytics.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** AN-08 · `research/expansion-tools/10-analytics.md`

### Pendo — ACTIVE
- **Purpose:** B2B product analytics + in-app guides, NPS, roadmaps.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** AN-09 · `research/expansion-tools/10-analytics.md`

### June — ACTIVE
- **Purpose:** Lightweight B2B product analytics on top of Segment.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** AN-10 · `research/expansion-tools/10-analytics.md`


## Stage: AI eval harnesses & LLM observability (`research/expansion-tools/11-ai-eval-harnesses.md`)

### Promptfoo — ACTIVE (acquired by OpenAI)
- **Purpose:** Open-source LLM eval + red-teaming: declarative configs, prompt/model/RAG comparisons, graded assertions, adversarial probes (prompt injection, jailbreaks, PII leakage; OWASP LLM Top 10 mapped), CI regression gates, MCP proxy, code scanning.
- **Maintenance:** Active. **Acquired by OpenAI Mar 9, 2026** (announced; close not publicly confirmed); to fold into "OpenAI Frontier"; ~130k MAU; $23M raised pre-acquisition (Series A $18.4M Jul 2025, Insight Partners).
- **Limitations:** Roadmap now set inside OpenAI; enterprise features commercial.
- **Real vs proposed use:** U(Verified) — 25%+ of Fortune 500 used it (vendor claim, Corroborated-weak).
- **Merge note:** Acquired by OpenAI.
- **Record:** EV-01 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Langfuse — ACTIVE (acquired by ClickHouse)
- **Purpose:** LLM observability: end-to-end tracing (waterfall views), prompt management/versioning, LLM-as-judge evals, datasets, session replay, cost tracking.
- **Maintenance:** Active. **Acquired by ClickHouse Jan 16, 2026** (announced alongside ClickHouse's $400M Series D @ $15B); "remains 100% open-source," self-hostable, Cloud continues standalone (acquirer statement); v3 requires ClickHouse (Langfuse already ran on ClickHouse). v4 claims up to 165x faster dashboards (vendor claim).
- **Limitations:** No infra monitoring (pairs with OpenObserve etc.); enterprise features paywalled; cloud pricing grows with event volume.
- **Real vs proposed use:** U(Proposed) — most-adopted OSS LLM observability per community analyses.
- **Merge note:** Acquired by Langfuse → ClickHouse.
- **Record:** EV-02 · `research/expansion-tools/11-ai-eval-harnesses.md`

### LangSmith — ACTIVE
- **Purpose:** LangChain's tracing/eval/dataset/prompt-experimentation platform; framework-agnostic observability.
- **Maintenance:** Active (2026); the product behind LangChain's $125M Oct 2025 raise.
- **Limitations:** Enterprise add-ons for self-hosting; commercial-only.
- **Real vs proposed use:** U(Proposed).
- **Record:** EV-03 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Braintrust — ACTIVE
- **Purpose:** Evaluation-first platform: datasets, scoring, experiments, production monitoring for LLM apps.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-04 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Arize Phoenix — ACTIVE (independent)
- **Purpose:** OSS LLM tracing/evaluation (OpenTelemetry + OpenInference based); LLM/code/human evaluators; built-in price tables.
- **Maintenance:** Active (2026).
- **Limitations:** ELv2 license restricts competitive hosting; narrower community than Langfuse.
- **Real vs proposed use:** U(Proposed).
- **Record:** EV-05 · `research/expansion-tools/11-ai-eval-harnesses.md`

### DeepEval / Confident AI — ACTIVE
- **Purpose:** OSS Python eval framework (Apache-2.0): 50+ plug-and-play metrics, pytest-style, RAG/agent/MCP evals, synthetic data; Confident AI commercial cloud (CI gates, red-teaming, guardrails, SOC 2, HIPAA).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-06 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Ragas — ACTIVE
- **Purpose:** OSS RAG evaluation metrics (faithfulness, answer relevancy, context precision/recall).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-07 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Helicone — MAINTAINED (acquired, maintenance mode)
- **Purpose:** One-line LLM proxy + observability (Apache-2.0); AI gateway with OTel support.
- **Maintenance:** **Maintenance mode after Mintlify acquisition (Mar 3, 2026)** — security/bug fixes/new models only; customers being migrated; no OSS/self-host commitment stated. ~16k orgs affected.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Acquired by Mintlify; maintenance mode.
- **Record:** EV-08 · `research/expansion-tools/11-ai-eval-harnesses.md`

### TensorZero — DEPRECATED (archived)
- **Purpose:** Rust gateway + observability + evals + experimentation (Apache-2.0).
- **Maintenance:** **Archived Jun 12, 2026** (~11.7k stars); code forkable, unmaintained.
- **Real vs proposed use:** Historical.
- **Merge note:** Archived Jun 2026.
- **Record:** EV-09 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Humanloop — SUPERSEDED (acqui-hired)
- **Purpose:** Prompt engineering + evaluation collaboration platform.
- **Maintenance:** **Acqui-hired by Anthropic** (per awesome-list market notes, 2026); standalone product wound down.
- **Real vs proposed use:** Historical.
- **Merge note:** Acqui-hired by Anthropic.
- **Record:** EV-10 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Portkey — ACTIVE (acquisition announced)
- **Purpose:** AI gateway (Apache-2.0 since Mar 2026) + managed observability/routing/guardrails platform.
- **Maintenance:** Active; **acquisition announced by Palo Alto Networks** (2026, per market notes — verify close).
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Acquisition announced: Portkey → Palo Alto Networks.
- **Record:** EV-11 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Weights & Biases Weave — ACTIVE (acquired)
- **Purpose:** LLM trace/eval layer inside W&B MLOps platform (SDK Apache-2.0; OTLP endpoint; Presidio redaction).
- **Maintenance:** Active under CoreWeave (2026).
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Acquired by CoreWeave.
- **Record:** EV-12 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Comet Opik — ACTIVE (independent)
- **Purpose:** OSS LLM eval/observability; in-house product of Comet ML (not acquired).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-13 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Evidently AI — ACTIVE
- **Purpose:** OSS ML/LLM evaluation and monitoring (reports, test suites).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-14 · `research/expansion-tools/11-ai-eval-harnesses.md`

### Patronus AI — ACTIVE
- **Purpose:** LLM evaluation and guardrails (finance/regulated focus).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** EV-15 · `research/expansion-tools/11-ai-eval-harnesses.md`

### SWE-bench / Terminal-Bench — ACTIVE (benchmarks, not products)
- **Purpose:** Standard benchmarks for coding agents (SWE-bench: GitHub issue→PR tasks; Terminal-Bench: terminal-based agentic tasks; SWE-bench Verified subset).
- **Maintenance:** Active; cited across vendor claims (Devin, OpenHands, Cline, Cursor comparisons).
- **Limitations:** Benchmark gaming risk; vendor-reported numbers need independent reproduction.
- **Real vs proposed use:** U(Verified) — industry-standard reference points.
- **Record:** EV-16 · `research/expansion-tools/11-ai-eval-harnesses.md`


## Stage: Workflow orchestration & durable execution (`research/expansion-tools/12-workflow-orchestration.md`)

### Temporal — ACTIVE
- **Purpose:** Durable workflow execution at infrastructure scale: workflows as code with replay-based state recovery, timers, signals, sagas; polyglot SDKs (Go/Java/Python/PHP/.NET/TypeScript); self-hostable cluster or Temporal Cloud.
- **Maintenance:** **Very active — verified directly from primary source.** Server **v1.32.0** (Sep 2026; api v1.63.5; go 1.26.8); SDK versions mid-2026: sdk-go 1.41.1, sdk-python 1.33.0; PRs merged within days of 2026-10-10 (e.g., auto-scaled-workers binary-size cut Sep 28, 2026; ~23.4k stars on temporalio/temporal). Third-party upgrade PRs (shepherdjerred monorepo) show real-world adoption tracking releases.
- **Limitations:** Operational complexity (cluster ops, visibility store); learning curve (determinism constraints on workflow code); Build-ID versioning being removed in v1.33 — migration to Worker Deployment APIs required.
- **Real vs proposed use:** U(Verified) — third-party repos tracking upgrades; Temporal Cloud customers (vendor). GitHub PR evidence: real production usage (upgrade discipline documented).
- **Record:** WO-01 · `research/expansion-tools/12-workflow-orchestration.md`

### Inngest — ACTIVE (CONTROVERSIAL: 2025 outage)
- **Purpose:** Durable functions in your own app: event-driven step functions (`step.run()`, `step.waitForEvent()` human-in-the-loop), automatic retries, concurrency controls, built-in scheduling; runs on Vercel/Cloudflare/any serverless host — no workers to run.
- **Maintenance:** Active (2026); longest track record in the class; official SvelteKit support cited in ADRs.
- **Limitations:** Hosted pricing scales with chattiness (step count); self-hosting "more involved than the managed service suggests"; managed-service outage = your jobs pause.
- **Real vs proposed use:** U(Verified) — ADRs in real repos (v10r jobs.md, Sep 2026: chosen for reactive job orchestration; foundryai ADR-0016 evaluated and rejected for v1 on sovereignty grounds).
- **Record:** WO-02 · `research/expansion-tools/12-workflow-orchestration.md`

### Trigger.dev — ACTIVE
- **Purpose:** Long-running background tasks on managed compute (or self-hosted): durable runs, retries, delays/schedules, batching; TypeScript-first; AI-workload friendly (tasks that break serverless timeouts — AI agents, media processing, big syncs).
- **Maintenance:** Active (2026); v3 is the durable-execution rewrite (use v3 in 2026).
- **Limitations:** Compute-time billing punishes slow/waiting tasks (holding a machine while waiting on a slow API); Trigger.dev v3 CLI requires Node (friction in Bun-first projects; experimental Bun runtime has broken OpenTelemetry — per v10r ADR).
- **Real vs proposed use:** U(Proposed) — evaluated in ADRs; community skill repos (agentic-awesome-skills) treat it as standard.
- **Record:** WO-03 · `research/expansion-tools/12-workflow-orchestration.md`

### DBOS — ACTIVE
- **Purpose:** Durable execution on Postgres (workflows as code backed by transactional state).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** WO-04 · `research/expansion-tools/12-workflow-orchestration.md`

### Camunda / Zeebe — ACTIVE
- **Purpose:** BPMN-based process orchestration (Zeebe: cloud-native workflow engine).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** WO-05 · `research/expansion-tools/12-workflow-orchestration.md`

### AWS Step Functions — ACTIVE
- **Purpose:** Serverless state-machine orchestration inside AWS.
- **Maintenance:** Active.
- **Real vs proposed use:** U(Verified) — AWS ecosystem standard. (Lightly researched — depth debt.)
- **Record:** WO-06 · `research/expansion-tools/12-workflow-orchestration.md`

### BullMQ — ACTIVE
- **Purpose:** Node.js queue on Redis (job queues, not durable workflows per se).
- **Maintenance:** Active (2026).
- **Limitations:** Needs persistent Redis (serverless-hostile); not durable execution (no replay).
- **Real vs proposed use:** U(Verified) — standard Node queue. (Lightly researched — depth debt.)
- **Record:** WO-07 · `research/expansion-tools/12-workflow-orchestration.md`

### pg-boss — MAINTAINED
- **Purpose:** Postgres-backed job queue for Node.
- **Maintenance:** Maintained (2026).
- **Limitations:** Neon PgBouncer breaks LISTEN/NOTIFY + advisory locks silently (per v10r ADR); polling worker has up-to-60s delay.
- **Real vs proposed use:** U(Proposed).
- **Record:** WO-08 · `research/expansion-tools/12-workflow-orchestration.md`

### Airflow — ACTIVE
- **Purpose:** Batch/data-pipeline orchestration (DAGs).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Verified) — data-engineering standard. (Lightly researched — depth debt.)
- **Record:** WO-09 · `research/expansion-tools/12-workflow-orchestration.md`

### Dagster — ACTIVE
- **Purpose:** Data orchestration with software-defined assets.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** WO-10 · `research/expansion-tools/12-workflow-orchestration.md`

### Prefect — ACTIVE
- **Purpose:** Pythonic workflow orchestration.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** WO-11 · `research/expansion-tools/12-workflow-orchestration.md`


## Stage: Secrets management (`research/expansion-tools/13-secrets-management.md`)

### HashiCorp Vault — ACTIVE (license saga: MPL-2.0 → BSL 1.1)
- **Purpose:** The secrets-management standard: dynamic secrets, PKI, encryption-as-a-service, identity-based access; HCP Vault / Vault Enterprise.
- **Maintenance:** Active (HashiCorp/IBM — IBM as licensor line per Mar 2026 sources).
- **Limitations:** Operational complexity (unseal, HA, storage backends); BSL restricts competitive hosting.
- **Real vs proposed use:** U(Verified) — enterprise standard.
- **Merge note:** License saga: MPL-2.0 → BSL 1.1; OpenBao (SM-02) is the community fork.
- **Record:** SM-01 · `research/expansion-tools/13-secrets-management.md`

### OpenBao — ACTIVE (the fork)
- **Purpose:** Community fork of Vault (pre-BSL codebase), Linux Foundation; drop-in compatibility goal.
- **Maintenance:** Active — **v2.7.0 (Sep 23, 2026)**.
- **Limitations:** Younger ecosystem; enterprise features lag Vault Enterprise.
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-02 · `research/expansion-tools/13-secrets-management.md`

### Infisical — ACTIVE
- **Purpose:** Developer-first secrets platform: open-source core (self-host free forever), dynamic secrets, secret scanning, PKI/SSH, broad integrations; expanding into identity/access management and **security infrastructure for AI agents/workloads**.
- **Maintenance:** Active (2026).
- **Limitations:** RBAC/SSO/audit logs are paid gates; enterprise surface younger than Vault.
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-03 · `research/expansion-tools/13-secrets-management.md`

### Doppler — ACTIVE (name collision warning)
- **Purpose:** Developer-centric secrets sync: clean UX, dependable propagation across environments/platforms, integrations, config syncs.
- **Maintenance:** Active (2026); best-in-class onboarding polish per 2026 comparisons.
- **Limitations:** SaaS-only (no self-host); static-secrets focused (no dynamic secrets/PKI/SSH vs Infisical); governance features paywalled.
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-04 · `research/expansion-tools/13-secrets-management.md`

### 1Password (Secrets Automation) — ACTIVE
- **Purpose:** Secrets management via Connect server, service accounts, CLI; built on SecretHub acquisition.
- **Maintenance:** Active (2026).
- **Limitations:** No true free plan (14-day trial); explicitly documented zero-knowledge model is the differentiator.
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-05 · `research/expansion-tools/13-secrets-management.md`

### AWS Secrets Manager / Parameter Store — ACTIVE
- **Purpose:** Native AWS secrets storage with rotation, IAM integration.
- **Maintenance:** Active.
- **Limitations:** AWS-coupled; per-secret/API-call pricing at scale.
- **Real vs proposed use:** U(Verified) — AWS standard.
- **Record:** SM-06 · `research/expansion-tools/13-secrets-management.md`

### Akeyless — ACTIVE
- **Purpose:** SaaS secrets management with DFC (distributed fragments cryptography); zero-knowledge architecture.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-07 · `research/expansion-tools/13-secrets-management.md`

### sops (Mozilla) — MAINTAINED
- **Purpose:** Encrypt secrets in Git (age/PGP + KMS); GitOps-native.
- **Maintenance:** Maintained (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-08 · `research/expansion-tools/13-secrets-management.md`

### External Secrets Operator — ACTIVE
- **Purpose:** Sync secrets from external managers (Vault, AWS SM, Doppler, Infisical) into Kubernetes.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** SM-09 · `research/expansion-tools/13-secrets-management.md`


## Stage: Discovery & user research (`research/expansion-tools/14-discovery-research.md`)

### Maze — ACTIVE
- **Purpose:** Quantitative user testing at the design phase: prototype tests, surveys, card sorting, tree tests with actionable KPIs; AI-assisted analysis.
- **Maintenance:** Active. **$40M Series B (Jun 13, 2022, Felicis; total $60M)** — investors incl. HubSpot Ventures, Atlassian Ventures, Zoom Ventures, Emergence Capital. 60k+ brands cited (Sony, Nubank, BNY Mellon, Uber, Hertz); 130+ employees across 35 countries (2022 figures). No newer funding found in this pass (depth debt on 2023–2026).
- **Limitations:** Prototype-testing focused (not a full research repository); quantitative lens misses qualitative depth.
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-01 · `research/expansion-tools/14-discovery-research.md`

### Dovetail — ACTIVE
- **Purpose:** AI-native customer-intelligence/research repository: ingests call transcripts, surveys, support tickets, usability tests; synthesizes thematic reports + real-time alerts; Slack/Teams/Notion/Zapier integrations; 3M+ verified participant panel for recruitment.
- **Maintenance:** Active (2026). Customers cited: Shopify, Canva, Mayo Clinic; Fortune 500s incl. Amazon, Deloitte, Atlassian (per secondary sources, Corroborated-weak).
- **Limitations:** Per-seat pricing at scale; AI synthesis quality needs human validation.
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-02 · `research/expansion-tools/14-discovery-research.md`

### Sprig — ACTIVE (verify)
- **Purpose:** In-product surveys + concept/user testing (ex-UserLeap).
- **Maintenance:** **Unknown — no 2026 primary source pulled in this pass** (depth debt; verify status/funding before citing).
- **Real vs proposed use:** U(Unknown).
- **Record:** DR-03 · `research/expansion-tools/14-discovery-research.md`

### UserTesting — ACTIVE
- **Purpose:** Moderated/unmoderated video-first user testing with participant panel.
- **Maintenance:** Active (2026). (Depth debt on current status.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-04 · `research/expansion-tools/14-discovery-research.md`

### Hotjar — ACTIVE
- **Purpose:** Heatmaps, session recordings, surveys (behavior analytics for web).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-05 · `research/expansion-tools/14-discovery-research.md`

### Microsoft Clarity — ACTIVE
- **Purpose:** Free heatmaps + session recordings.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-06 · `research/expansion-tools/14-discovery-research.md`

### Optimal Workshop — ACTIVE
- **Purpose:** Card sorting, tree testing, first-click testing (information architecture).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-07 · `research/expansion-tools/14-discovery-research.md`

### Great Question — ACTIVE
- **Purpose:** Research participant recruitment + study management.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DR-08 · `research/expansion-tools/14-discovery-research.md`


## Stage: Project management & issue tracking (`research/expansion-tools/15-project-management.md`)

### Linear — ACTIVE
- **Purpose:** Fast, opinionated issue tracking for software teams (keyboard-first, cycles, triage, GitHub/GitLab sync).
- **Maintenance:** Active (2026). (Depth debt on funding updates.)
- **Limitations:** Opinionated workflow (Jira refugees must adapt); no self-host.
- **Real vs proposed use:** U(Proposed) — the 2020s default for startups; no single named customer verified in this pass.
- **Merge note:** Also recorded in cases-product TI-20 as an agent context source consumed by OpenAI's Codex (U(Verified)).
- **Record:** PM-01 · `research/expansion-tools/15-project-management.md`

### Jira (Atlassian) — ACTIVE
- **Purpose:** Enterprise issue tracking + agile boards; Jira Service Management absorbing Opsgenie alerting.
- **Maintenance:** Active (2026).
- **Limitations:** Configurability = complexity; performance complaints at scale.
- **Real vs proposed use:** U(Verified) — enterprise standard.
- **Record:** PM-02 · `research/expansion-tools/15-project-management.md`

### Shortcut (ex-Clubhouse) — ACTIVE
- **Purpose:** Project management for software teams (stories, epics, iterations).
- **Maintenance:** Active (2026). (Depth debt on current status.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-03 · `research/expansion-tools/15-project-management.md`

### Plane — ACTIVE (OSS Linear alternative)
- **Purpose:** Open-source project management (Linear-like UX); self-hostable.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-04 · `research/expansion-tools/15-project-management.md`

### Height — DEPRECATED (shut down)
- **Purpose:** AI-assisted project management.
- **Maintenance:** **Shut down Sep 24, 2025.** (Per summary.)
- **Real vs proposed use:** Historical.
- **Merge note:** Deprecated: shut down Sep 24, 2025.
- **Record:** PM-05 · `research/expansion-tools/15-project-management.md`

### Pivotal Tracker — DEPRECATED (retired)
- **Purpose:** Agile story tracking (the XP-era standard).
- **Maintenance:** **Retired Apr 30, 2025** (Broadcom/Tanzu Labs). (Per summary.)
- **Real vs proposed use:** Historical.
- **Merge note:** Deprecated: retired Apr 30, 2025.
- **Record:** PM-06 · `research/expansion-tools/15-project-management.md`

### Asana — ACTIVE
- **Purpose:** Work management for cross-functional teams.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-07 · `research/expansion-tools/15-project-management.md`

### Monday.com — ACTIVE
- **Purpose:** Work OS (boards, automations, dashboards).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-08 · `research/expansion-tools/15-project-management.md`

### ClickUp — ACTIVE
- **Purpose:** All-in-one productivity (docs, tasks, goals, chat).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-09 · `research/expansion-tools/15-project-management.md`

### Notion — ACTIVE
- **Purpose:** Wiki + docs + lightweight project tracking; databases.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Also recorded in cases-product TI-20 as an agent context source consumed by OpenAI's Codex (U(Verified)). Statsig (FF-03) names Notion as a customer.
- **Record:** PM-10 · `research/expansion-tools/15-project-management.md`

### OpenProject — ACTIVE (OSS)
- **Purpose:** Open-source project management (Gantt, agile boards); EU public-sector pick.
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-11 · `research/expansion-tools/15-project-management.md`

### Taiga — ACTIVE (OSS)
- **Purpose:** Open-source agile project management (Kaleidos — same org as Penpot).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** PM-12 · `research/expansion-tools/15-project-management.md`


## Stage: Databases, caching & data infrastructure (`research/expansion-tools/16-databases-caching.md`)

### Supabase — ACTIVE (acquiring Turso; $1B+ raised)
- **Purpose:** Open-source Postgres development platform: managed Postgres + auth, storage, edge functions, realtime, vector search (pgvector); "Firebase alternative on Postgres."
- **Maintenance:** Active; extreme growth. Verified timeline:
- **Limitations:** Postgres-at-scale ops still surface (connection pooling, long-tail perf); usage-based billing can surprise at agent-driven scale; counting methodology for growth claims undisclosed.
- **Real vs proposed use:** U(Verified) — Lovable integration; 13M developers claimed (company-reported).
- **Merge note:** Agreed to acquire Turso (announced Oct 2, 2026); $150M round. See Appendix B.
- **Record:** DB-01 · `research/expansion-tools/16-databases-caching.md`

### Turso — ACTIVE (being acquired by Supabase)
- **Purpose:** SQLite rebuilt in Rust; edge-replicated, per-database isolation; "a single server can manage millions of databases" — the database-per-agent pattern (create/query/discard via API).
- **Maintenance:** Active; **acquisition by Supabase announced Oct 2, 2026** (terms/close date undisclosed). Turso says platform, APIs, workflows continue; no pricing/licensing change announced. Analyst guidance circulating: take independent backups, request 12-month price lock + change-of-control termination rights.
- **Limitations:** libSQL→Rust-rewrite transition incomplete (pre-1.0); post-acquisition roadmap/pricing uncertainty (standard).
- **Real vs proposed use:** U(Proposed).
- **Merge note:** Being acquired by Supabase (announced Oct 2, 2026).
- **Record:** DB-02 · `research/expansion-tools/16-databases-caching.md`

### Neon — ACTIVE
- **Purpose:** Serverless Postgres (separate storage/compute, autoscaling, branching, scale-to-zero).
- **Maintenance:** Active (2026). (Depth debt on funding/valuation updates.)
- **Limitations:** Cold starts on scale-from-zero; connection handling (PgBouncer breaks LISTEN/NOTIFY — cited in the v10r ADR for pg-boss); egress costs.
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-03 · `research/expansion-tools/16-databases-caching.md`

### PlanetScale — ACTIVE
- **Purpose:** Serverless MySQL (Vitess-based): branching, non-blocking schema changes, scale-to-zero.
- **Maintenance:** Active (2026). (Depth debt on current status.)
- **Limitations:** MySQL-only; no stored procedures/triggers in some tiers historically.
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-04 · `research/expansion-tools/16-databases-caching.md`

### Redis — ACTIVE (license saga: BSD → RSALv2/SSPLv1, then AGPLv3 added)
- **Purpose:** In-memory data store (caching, queues, streams, vectors).
- **Maintenance:** Active (Redis Inc./Redis Ltd.).
- **Limitations:** License complexity for distributors/cloud providers; ecosystem split with Valkey.
- **Real vs proposed use:** U(Verified) — still ubiquitous; Valkey winning new defaults.
- **Merge note:** License saga: BSD → RSALv2/SSPLv1, then AGPLv3 added; Valkey (DB-06) is the fork that won.
- **Record:** DB-05 · `research/expansion-tools/16-databases-caching.md`

### Valkey — ACTIVE (the fork that won)
- **Purpose:** BSD-licensed Redis fork (Linux Foundation, Mar 2024) preserving open-source Redis trajectory.
- **Maintenance:** Active (2026); adopted as default by major distros and AWS.
- **Real vs proposed use:** U(Verified) — AWS/distro defaults. (Corroborated.)
- **Record:** DB-06 · `research/expansion-tools/16-databases-caching.md`

### Dragonfly — ACTIVE (source-available)
- **Purpose:** Drop-in Redis replacement (multi-threaded, higher throughput).
- **Maintenance:** Active (2026) per community standing. (Depth debt — verify current releases.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-07 · `research/expansion-tools/16-databases-caching.md`

### KeyDB — MAINTAINED (Snap-owned)
- **Purpose:** Multithreaded Redis fork (Snap Inc. acquired May 2022).
- **Maintenance:** Maintained under Snap; slower public cadence than Valkey/Dragonfly. (Depth debt — verify 2026 commits.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-08 · `research/expansion-tools/16-databases-caching.md`

### Garnet (Microsoft) — ACTIVE
- **Purpose:** MIT-licensed Redis alternative from Microsoft Research (high performance).
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-09 · `research/expansion-tools/16-databases-caching.md`

### TimescaleDB — ACTIVE (dual-license model)
- **Purpose:** Time-series on Postgres (hypertables, compression, continuous aggregates).
- **Maintenance:** Active (2026). (Depth debt on versions.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-10 · `research/expansion-tools/16-databases-caching.md`

### MongoDB — ACTIVE (SSPL originator)
- **Purpose:** Document database.
- **Maintenance:** Active (MongoDB Inc., public).
- **Real vs proposed use:** U(Verified) — enterprise standard.
- **Merge note:** SSPL originator; DocumentDB is the AWS response.
- **Record:** DB-11 · `research/expansion-tools/16-databases-caching.md`

### Elasticsearch — ACTIVE (SSPL saga resolved toward openness)
- **Purpose:** Search + analytics engine.
- **Maintenance:** Active.
- **Real vs proposed use:** U(Verified).
- **Merge note:** SSPL saga resolved toward openness: OpenSearch (DB-13, Linux Foundation) + AGPLv3 added.
- **Record:** DB-12 · `research/expansion-tools/16-databases-caching.md`

### OpenSearch — ACTIVE
- **Purpose:** Apache-2.0 Elasticsearch fork (AWS → Linux Foundation Sep 2024).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-13 · `research/expansion-tools/16-databases-caching.md`

### CockroachDB — ACTIVE (BSL; free Core retired)
- **Purpose:** Distributed SQL (Postgres-compatible).
- **Maintenance:** Active.
- **Real vs proposed use:** U(Proposed).
- **Merge note:** BSL; free Core retired.
- **Record:** DB-14 · `research/expansion-tools/16-databases-caching.md`

### ClickHouse — ACTIVE
- **Purpose:** Columnar OLAP database; acquirer of Langfuse (Jan 2026); $400M Series D @ $15B.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-15 · `research/expansion-tools/16-databases-caching.md`

### DuckDB — ACTIVE
- **Purpose:** In-process analytical SQL (the "SQLite for analytics").
- **Maintenance:** Active (2026). (Depth debt.)
- **Real vs proposed use:** U(Proposed).
- **Record:** DB-16 · `research/expansion-tools/16-databases-caching.md`


## Stage: PaaS, deploy platforms & self-hosted alternatives (`research/expansion-tools/17-paas-deploy.md`)

### Vercel — ACTIVE (CONTROVERSIAL: pricing)
- **Purpose:** Frontend cloud: git-push deploys, preview environments, serverless/edge functions, image optimization; home of Next.js and v0.
- **Maintenance:** Active (2026); massive scale; Next.js recommended by React team for RSC.
- **Limitations:** Aggressive pricing at scale; proprietary Next.js features (ISR behavior, Edge Config, Vercel KV) create lock-in; AI streaming/agent loops chew bandwidth and invocations; Hobby function duration limits (5 min default, up to 800s Pro, 30 min extended beta).
- **Real vs proposed use:** U(Verified) — dominant Next.js host; v0 deploys.
- **Merge note:** CONTROVERSIAL: ongoing pricing bill-shock saga.
- **Record:** PA-01 · `research/expansion-tools/17-paas-deploy.md`

### Netlify — ACTIVE
- **Purpose:** The original git-push-to-deploy platform (JAMstack): forms, identity, split testing, edge functions.
- **Maintenance:** Active (2026); most feature-complete in class per 2026 comparisons.
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-02 · `research/expansion-tools/17-paas-deploy.md`

### Cloudflare Pages / Workers — ACTIVE
- **Purpose:** Static hosting + edge compute on Cloudflare's network; famously **no egress fees** on typical CDN usage; unlimited bandwidth on free tier for static.
- **Maintenance:** Active (2026).
- **Limitations:** Workers runtime is not Node (compatibility shims); Durable Objects/ KV have their own semantics.
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-03 · `research/expansion-tools/17-paas-deploy.md`

### Fly.io — ACTIVE
- **Purpose:** Run containers close to users globally (Firecracker microVMs "Machines"); Heroku-Procfiles-friendly (`flyctl` builds with buildpacks; Procfile → fly.toml [processes]); published Migrate-from-Heroku guide.
- **Maintenance:** Active (2026).
- **Limitations:** DIY-er than Heroku (more knobs); usage-based bills need monitoring.
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-04 · `research/expansion-tools/17-paas-deploy.md`

### Render — ACTIVE
- **Purpose:** Heroku-style managed PaaS with predictable pricing: web services, Postgres, Redis, cron; render.yaml; native runtimes (no Procfile — Dockerfile or prebuilt for custom).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-05 · `research/expansion-tools/17-paas-deploy.md`

### Railway — ACTIVE
- **Purpose:** Developer-UX-first PaaS; per-second usage billing; Railpack builder (Nixpacks successor) detects Procfiles; per-service model like old Heroku dashboard.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-06 · `research/expansion-tools/17-paas-deploy.md`

### Koyeb — ACTIVE
- **Purpose:** Global edge deployment PaaS; free Nano instance (no sleep); serverless containers.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-07 · `research/expansion-tools/17-paas-deploy.md`

### Zeabur — ACTIVE
- **Purpose:** Simple-deploy PaaS; $5/mo free credit, no sleep; "Top Pick 2026" in community hosting guides.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-08 · `research/expansion-tools/17-paas-deploy.md`

### Northflank — ACTIVE
- **Purpose:** Container/K8s-style control with managed UX; free plan (1 service + 1 DB); BYOC path.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-09 · `research/expansion-tools/17-paas-deploy.md`

### Dokku — ACTIVE (OSS Heroku clone)
- **Purpose:** "Open source PaaS alternative to Heroku" — push Heroku-compatible apps over Git to your own single host; herokuish + Cloud Native Buildpacks; Procfile respected; Postgres/Redis via official plugins.
- **Maintenance:** Active, mature (2026).
- **Limitations:** Single-host model (not HA); you own the ops.
- **Real vs proposed use:** U(Proposed) — "closest thing to Heroku that exists" per 2026 migration guides.
- **Record:** PA-10 · `research/expansion-tools/17-paas-deploy.md`

### Coolify — ACTIVE (OSS)
- **Purpose:** Self-hosted Heroku/Netlify alternative (VPS → push-to-deploy, DBs, previews).
- **Maintenance:** Active (2026); central to the "deployment arbitrage" movement off Vercel.
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-11 · `research/expansion-tools/17-paas-deploy.md`

### Dokploy — ACTIVE (OSS)
- **Purpose:** Self-hosted PaaS (Docker-based, VPS-friendly); chosen by teams leaving Vercel in 2025–2026 teardowns.
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-12 · `research/expansion-tools/17-paas-deploy.md`

### Qovery — ACTIVE (BYOC)
- **Purpose:** Heroku-like DX deploying into YOUR cloud account (BYOC): managed control plane + your AWS/GCP.
- **Maintenance:** Active (2026).
- **Limitations:** Per-cluster floor cost; needs your cloud account.
- **Real vs proposed use:** U(Proposed).
- **Record:** PA-13 · `research/expansion-tools/17-paas-deploy.md`

### Porter — ACTIVE (BYOC)
- **Purpose:** PaaS on your own AWS/GCP (deploy into your cloud).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-14 · `research/expansion-tools/17-paas-deploy.md`

### Heroku — MAINTAINED (post-free-tier)
- **Purpose:** The original git-push PaaS (Salesforce).
- **Maintenance:** Maintained; dynos restart ~24h (masks memory leaks — migration gotcha documented in 2026 guides).
- **Real vs proposed use:** U(Verified) — legacy installs; renewals drive BYOC evaluations.
- **Merge note:** MAINTAINED (post-free-tier).
- **Record:** PA-15 · `research/expansion-tools/17-paas-deploy.md`

### Cloud 66 — ACTIVE
- **Purpose:** Deploy/manage apps on your own cloud (Rails/node focus).
- **Maintenance:** Active (2026).
- **Real vs proposed use:** U(Proposed). (Lightly researched — depth debt.)
- **Record:** PA-16 · `research/expansion-tools/17-paas-deploy.md`


## Stage: Game engines & creative runtimes (`research/expansion-tools/18-game-creative-runtimes.md`)

### Godot — ACTIVE (ascendant)
- **Purpose:** Open-source 2D/3D game engine (GDScript + C#/.NET 8/9, Vulkan/GL Compatibility renderers, XR tools).
- **Maintenance:** Active — 4.7.x line current (4.7.2 referenced in 2026 skill docs); Godot 4.0 brought Vulkan, new tilemap, XR.
- **Limitations:** No official console export (platform SDK NDAs vs open license) — must go through **W4 Games' W4 Consoles** (Switch, Xbox Series X|S, PS5; Switch 2 beta since early 2026; per-title/per-platform negotiated pricing); C# web export unsupported in 4.6 (stay on GDScript for web); mobile ad/IAP/analytics tooling less mature than Unity's; asset library smaller; many tutorials target incompatible Godot 3.x
- **Real vs proposed use:** U(Verified) — jam data + commercial titles (gameworldobserver, outlookindia, LinkedIn/Diversion post).
- **Merge note:** GMTK Game Jam 2026: Godot #1 (47%) vs Unity 34% — first time in 9 years Unity did not lead (see Appendix B).
- **Record:** GE-01 · `research/expansion-tools/18-game-creative-runtimes.md`

### Unity — ACTIVE (CONTROVERSIAL: trust)
- **Purpose:** Proprietary cross-platform engine (C#/.NET, IL2CPP); 20-year ecosystem: Asset Store, LevelPlay/AdMob/IAP, AR Foundation, XRI.
- **Maintenance:** Active — **Unity 6.0 LTS reaches end of support Oct 2026** (per itamde 2026 guide — plan upgrades).
- **Limitations:** Proprietary license; trust overhang; build footprint 8–30GB+ (Hub + modules); older Asset Store content version-rot.
- **Real vs proposed use:** U(Verified) — still the mobile/console commercial standard (34% of GMTK 2026).
- **Merge note:** Sep 2023 per-install runtime fee: backlash, cancelled Sep 2024, CEO departed (see Appendix B).
- **Record:** GE-02 · `research/expansion-tools/18-game-creative-runtimes.md`

### Unreal Engine — ACTIVE
- **Purpose:** AAA 3D engine (C++/Blueprints, Nanite/Lumen); Epic.
- **Maintenance:** Active (2026). 3% of GMTK 2026 (319 games) — jam-irrelevant, industry-standard for high-end 3D.
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** GE-03 · `research/expansion-tools/18-game-creative-runtimes.md`

### GameMaker — ACTIVE
- **Purpose:** 2D-focused engine (GML); beginner-friendly.
- **Maintenance:** Active (2026); 5% of GMTK 2026 (498 games).
- **Real vs proposed use:** U(Proposed). (Depth debt.)
- **Record:** GE-04 · `research/expansion-tools/18-game-creative-runtimes.md`

### Bevy — ACTIVE (experimental-adjacent)
- **Purpose:** Rust ECS game engine (data-driven, mod-friendly).
- **Maintenance:** Active (2026). (Depth debt on releases.)
- **Real vs proposed use:** U(Proposed).
- **Record:** GE-05 · `research/expansion-tools/18-game-creative-runtimes.md`


STAGE_RECORD_COUNT=230
