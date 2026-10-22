# §30 — Agent Frameworks & Orchestration Runtimes (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## AF-01 — LangChain / LangGraph — ACTIVE (narrative: "dead" — evidence: alive)
- Purpose / problem: LLM app orchestration: chains, agents, tool calling, 1,000+ integrations (LangChain = DX layer); LangGraph = stateful graph execution runtime (Pregel/Beam-inspired) with durable state, checkpointing, human-in-the-loop interrupts.
- OSS/commercial: OSS MIT (~100k+ stars LangChain; ~34k LangGraph). Commercial companion: LangSmith (observability/evals).
- Integration: Python/TypeScript; 600+ model/tool integrations; LCEL; `create_agent`.
- Maintenance: Active. **LangChain 1.0 + LangGraph 1.0 GA Oct 22, 2025**; langchain-core 1.6.6 / LangGraph 1.2.12 (Oct 2026 per Uvik guide). Since Oct 2025 `create_agent` runs on the LangGraph runtime under the hood — layered, not either/or.
- Availability: Public OSS; LangChain Inc. raised **$125M @ $1.25B valuation Oct 2025** (round driven by LangSmith, not the framework).
- Limitations: Historical criticism — over-abstraction, opaque state, "debugging the framework instead of your logic"; 1.0 addressed part of it. Frontier model providers' native tool-calling reduced the original need.
- Security: Prompt-injection/tool-permission surface is the app's, not the framework's; LangSmith tracing helps audit.
- Alternatives: LlamaIndex (RAG), Pydantic AI, CrewAI, Mastra, raw APIs, Claude/OpenAI Agent SDKs.
- Switching costs: Medium (abstractions permeate app code).
- Use: U(Verified) — vendor claims 35% of Fortune 500 use it (self-reported; treat as Corroborated-weak); tens of millions of monthly downloads (cited in community analyses).
- Note on narrative: recurring "LangChain is dead" discourse (2024–2026) is community narrative, not maintenance reality; Kieran Klaassen's "where good AI projects go to die" quote captures the sentiment side.

## AF-02 — Microsoft AutoGen — DEPRECATED (maintenance mode) → three-way split
- Purpose / problem: Multi-agent conversation framework (Microsoft Research, Wu et al. 2023): conversable agents, group chat, code execution.
- OSS/commercial: OSS (MIT/Apache mix), ~55–59k stars.
- Maintenance: **Maintenance mode since ~Oct 2025** — "stable API, critical bug fixes and security patches, no significant new features" (microsoft/autogen discussion #7066). Last feature line: 0.7.5 (Sep 2025). Microsoft redirects new users to Microsoft Agent Framework.
- **The three-way split (2026):**
  1. **microsoft/autogen** — maintenance only.
  2. **AG2** (ag2ai/ag2) — community fork; owns the legacy `autogen` PyPI package; v0.12.2 mid-2026; nine orchestration patterns + MCP client. Migration path for users not moving to MAF.
  3. **Microsoft Agent Framework (MAF)** — official successor; **1.0 GA Apr 3, 2026**; Python 1.15.0 / .NET 1.19.0 (Aug 2026); unifies AutoGen multi-agent patterns + Semantic Kernel enterprise foundations; MCP + A2A protocol; `pip install agent-framework`. ~11.6k stars, weekly cadence.
- Also: **Semantic Kernel** consolidated into MAF (same teams); **Prompt Flow** (Azure/Foundry) **retires Apr 20, 2027** with published migration to Agent Framework; AutoGen Studio tagged "reference application."
- Alternatives: LangGraph, CrewAI, AG2, MAF.
- Switching costs: Medium–high (MAF migration guide exists but is Python-only; .NET mappings community-derived — per maf-doctor review).
- Use: U(Verified) — historically one of the most-used multi-agent frameworks; existing enterprise codebases.

## AF-03 — CrewAI — ACTIVE
- Purpose / problem: Role-based multi-agent orchestration (agents with role/goal/backstory; crews with sequential/hierarchical/consensual processes); built-in eval tooling; AMP Suite commercial.
- OSS/commercial: OSS MIT (~59k stars Sep 2026; ~47k per other sources). Raised $18M (seed + Series A, Oct 2024; boldstart, Insight Partners; backers incl. Andrew Ng, Dharmesh Shah).
- Integration: Python; A2A protocol + MCP support (since ~v1.10, early 2026); streaming.
- Maintenance: Active — v1.15.22 (Sep 16, 2026); **LangChain dependency removed in v1.14** (now standalone/leaner).
- Limitations: Coarse-grained error handling; abstraction prioritizes simplicity over control — common prototype→LangGraph migration path reported.
- Security: Agent tool permissions per deployment; sandbox CVE reported Oct 2026 (per AI Agents Directory brief — single source, Corroborated-weak).
- Alternatives: LangGraph, AutoGen/AG2, OpenAI Agents SDK.
- Switching costs: Low–medium.
- Use: U(Proposed) — 2B agent executions/12mo claimed (vendor); no named enterprises located in this pass.

## AF-04 — Agno (ex-Phidata) — ACTIVE
- Purpose / problem: "Fastest" multimodal agent framework + AgentOS self-hosted runtime (FastAPI runtime + control plane; data stays in your infra).
- OSS/commercial: OSS Apache-2.0; ~40k+ stars. Rebranded from Phidata Jan 2025.
- Maintenance: Active (2026).
- Alternatives: LangGraph, CrewAI, Strands.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-05 — SmolAgents (Hugging Face) — ACTIVE
- Purpose / problem: Minimal agent framework (code-first agents; ~1k lines); Hugging Face ecosystem native.
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: LangChain, raw APIs.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-06 — DSPy — ACTIVE
- Purpose / problem: Programming (not prompting) language models: declarative LM pipelines compiled/optimized via metrics (Stanford NLP).
- OSS/commercial: OSS (research).
- Maintenance: Active (2026).
- Alternatives: LangChain LCEL, raw prompting.
- Use: U(Verified) — research community; production use proposed. (Lightly researched — depth debt.)

## AF-07 — Haystack (deepset) — ACTIVE
- Purpose / problem: LLM/RAG pipeline framework (document search, retrieval pipelines); deepset commercial cloud.
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: LlamaIndex, LangChain.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-08 — LlamaIndex — ACTIVE
- Purpose / problem: Data indexing + RAG framework (document loaders, indices, query engines); LlamaCloud managed parsing/indexing.
- OSS/commercial: OSS MIT (~52k stars Sep 2026); v0.14.25 (Sep 2026).
- Maintenance: Active.
- Alternatives: LangChain RAG, Haystack.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-09 — Dify — ACTIVE
- Purpose / problem: LLM app development platform (visual workflow builder, RAG pipelines, agent orchestration, model management); self-hostable.
- OSS/commercial: OSS (Apache-2.0 historically; note: dev.to 2026-10-09 survey flags Dify among apps with non-standard/custom license terms — verify current LICENSE before building on it).
- Integration: Docker Compose; 16-service stack; ~4GB RAM floor.
- Maintenance: Active — fast release pace; established.
- Limitations: Ships on plain HTTP :80 (needs TLS/proxy in front); heavyweight stack.
- Security: Self-hostable; review license terms for commercial redistribution.
- Alternatives: Langflow, Flowise, n8n (automation overlap).
- Use: U(Proposed). (Depth debt on license verification.)

## AF-10 — Langflow — ACTIVE (acquired)
- Purpose / problem: Visual drag-and-drop builder for LangChain/RAG/agent flows.
- OSS/commercial: OSS; **acquired by DataStax Apr 2024** (one-stop GenAI stack with Astra DB).
- Maintenance: Active under DataStax (2026).
- Alternatives: Flowise, Dify.
- Use: U(Proposed).

## AF-11 — Flowise — ACTIVE
- Purpose / problem: Drag-and-drop UI for LangChain agent/chatflow building; self-hostable.
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: Langflow, Dify.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-12 — Rasa — MAINTAINED (ownership changed)
- Purpose / problem: Open-source conversational AI framework (NLU dialogue management).
- OSS/commercial: OSS; company acquired (details vary by source — treat as Reported; verify).
- Maintenance: Community-maintained; enterprise focus shifted.
- Alternatives: Botpress, LangGraph-based assistants.
- Use: U(Proposed). (Depth debt — verify current ownership/maintenance.)

## AF-13 — AutoGPT — ACTIVE (narrative correction: NOT dead)
- Purpose / problem: Autonomous agent platform (goal-driven agents, "go-do-it" model); plugin/provider registry; MCP provider path.
- OSS/commercial: OSS; Significant Gravitas company; Pro tier ($60) with Stripe billing.
- Maintenance: **Active — commits within Sep 2026** (PR #14495 Sep 2026; billing fixes; LLM model retirement migrations; frontend Helm chart removed Dec 2025, Vercel-only deploy). The "AutoGPT is dead" narrative is false for the platform repo.
- **But:** companion repo **Auto-GPT-Plugins archived by owner Jun 9, 2024** (read-only) — the original plugin ecosystem is dead.
- Alternatives: OpenHands, LangGraph.
- Use: U(Proposed).

## AF-14 — Pydantic AI — ACTIVE
- Purpose / problem: Type-safe, Pythonic agent framework from the Pydantic team; lean alternative to LangChain.
- OSS/commercial: OSS.
- Maintenance: Active (2026); gaining share per community analyses.
- Alternatives: LangChain, LangGraph.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-15 — Mastra — ACTIVE
- Purpose / problem: TypeScript-native agent framework.
- OSS/commercial: OSS.
- Maintenance: Active (2026).
- Alternatives: LangChain.js, Vercel AI SDK.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-16 — Strands (AWS) — ACTIVE
- Purpose / problem: AWS open-source agent framework (model-driven, lightweight).
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: LangGraph, Bedrock Agents.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-17 — OpenAI Agents SDK / Swarm — ACTIVE
- Purpose / problem: OpenAI's agent SDK (handoffs, guardrails; successor to experimental Swarm).
- OSS/commercial: OSS (MIT).
- Maintenance: Active (2026).
- Alternatives: LangGraph, Claude Agent SDK.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-18 — Claude Agent SDK (Anthropic) — ACTIVE
- Purpose / problem: Anthropic's agent SDK (native state management, tool use, sub-agents; the harness behind Claude Code).
- OSS/commercial: OSS.
- Maintenance: Active (2026).
- Alternatives: OpenAI Agents SDK, LangGraph.
- Use: U(Proposed). (Lightly researched — depth debt.)

## AF-19 — Semantic Kernel — SUPERSEDED (consolidated)
- Purpose / problem: Microsoft's enterprise LLM orchestration SDK (.NET/Python).
- Maintenance: Consolidated into **Microsoft Agent Framework** (same teams); do not start new projects on it.
- Alternatives: MAF.
- Use: U(Verified) — existing .NET enterprise codebases.

## AF-20 — BabyAGI — DEPRECATED (historical)
- Purpose / problem: 2023 task-driven autonomous agent demo (Yohei Nakajima); vector-DB task loop.
- Maintenance: **Abandoned** — historical artifact of the 2023 agent hype wave.
- Alternatives: LangGraph, CrewAI.
- Use: Historical only. (Lightly researched — accepted as historical record.)

## Notable status findings (agent frameworks)
- Microsoft AutoGen — **maintenance mode** (Oct 2025) → MAF 1.0 GA Apr 2026; AG2 community fork holds legacy PyPI name.
- Semantic Kernel — **superseded** by MAF. Prompt Flow — **retires Apr 20, 2027**.
- AutoGPT — **alive** (platform repo active Sep 2026); Auto-GPT-Plugins repo **archived Jun 2024**.
- LangChain — "dead" narrative vs **1.0 GA Oct 2025 + $125M raise** reality.
- BabyAGI — dead (2023 hype artifact).
