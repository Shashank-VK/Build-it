# 05a — Multi-Agent Systems & Orchestration + Harness Engineering & Autonomous Software Development

> Workstream #9 catalog · Part 9 (Multi-Agent Systems and Orchestration) + Part 10 (Harness Engineering and Autonomous Software Development).
> Verification date for all records: **2026-10-10** · Confidence recorded per item.

## Intro — sources searched and search themes

Research was conducted 2026-10-10 via `browser.search` (15+ thematic queries) and `browser.open` against primary GitHub sources. Search themes, in order:

1. **General multi-agent frameworks**: LangGraph architecture; Microsoft AutoGen 2026 status; CrewAI status; OpenAI Agents SDK; Google ADK hierarchical systems; MetaGPT 2026 status; AWS Strands Agents; PydanticAI; HuggingFace smolagents; IBM BeeAI; Hermes Agent (Nous Research); Meta Llama Stack.
2. **Agent-to-agent protocols and standards**: A2A specification; IBM ACP status; AG-UI protocol; AGNTCY; AP2 payments protocol; ANP/W3C AI Agent Protocol CG; name-collision disambiguation (4 different "ACP"s).
3. **Harness engineering**: Munder Difflin GOD orchestrator; GitHub Spec Kit; OpenSpec; BMAD-METHOD; Kiro; cc-sdd; SpecWeave; Agent OS.
4. **Autonomous coding agents**: SWE-agent; mini-SWE-agent; OpenHands; SWE-ReX; SWE-smith; EnIGMA; Aider.
5. **Evaluation benchmarks**: SWE-bench family (Verified/Pro/Live/Multilingual/Multimodal), SWE-rebench V2, Multi-SWE-bench, Terminal-Bench, TerminalWorld, TUA-Bench, GAIA, gray311/awesome-agentic-benchmarks.
6. **Agent telemetry/cost tracking**: Langfuse, AgentOps, LangSmith, Arize Phoenix, Helicone, OpenLLMetry, W&B Weave.

Primary sources inspected directly (full page text via `browser.open`): `langchain-ai/langgraph` README + repo metadata; `a2aproject/A2A` README + repo metadata; `github/spec-kit` README + repo metadata; `microsoft/autogen` README + repo metadata (maintenance-mode banner confirmed verbatim); `SWE-agent/SWE-agent` README + repo metadata (supersession notice confirmed verbatim). Other items verified via exact README excerpts in search results (secondary capture of primary docs); inspection method is stated per record.

**Dedup policy applied**: items already catalogued in the OpenCode-centric catalog and loop-engineering workstreams were not re-researched in depth; they appear as cross-references. Notable new (not previously catalogued) finds: Munder Difflin harness, Hermes Agent, AG-UI v1.0, AGNTCY stack detail, SWE-bench Pro/Live/SWE-rebench V2, TerminalWorld, TUA-Bench, Commerce ACP vs IBM ACP disambiguation, MetaGPT org migration (geekan → FoundationAgents), auto-architected record of AutoGen→Microsoft Agent Framework succession.

---

## PART 9 — MULTI-AGENT SYSTEMS AND ORCHESTRATION

### 9.1 General multi-agent frameworks

---

**Resource name:** LangGraph
**Canonical identity:** langchain-ai/langgraph (LangChain Inc.)
**Category:** Multi-agent systems and orchestration — graph-based agent runtime
**Type:** Open-source framework (Python + TypeScript)
**Official URL:** https://github.com/langchain-ai/langgraph · Docs: https://docs.langchain.com
**Description:** Low-level orchestration framework for building stateful, long-running agents. Agents, tools, and checkpoints are *nodes* in a directed graph; transitions are *edges* (including conditional and cyclic edges). Reached v1.0 GA on 2026-10-22 (per secondary reports of Oct 22, 2025 release; repo active, ~42,967 stars at inspection).
**Contents inspected:** Full README.md + repository metadata (stars, license, topics, root files) via browser.open, 2026-10-10. Secondary: ADR documents showing supervisor→parallel-agents→synthesise→critic topologies.
**Actual capabilities:** Durable execution (persist through failures, resume from checkpoint); human-in-the-loop (inspect/modify state mid-execution); short- and long-term memory; checkpointing with time-travel replay; streaming; subgraph composition; deployment via LangSmith platform. Multi-agent patterns: supervisor/worker, parallel fan-out with reducer state merges, conditional critic loops, interrupts (`interrupt_before`) for approvals.
**Usage domain:** Production agent systems needing explicit control, audit trails, branching logic, long-running human review steps.
**Integration method:** `pip install -U langgraph`; code-first API (`StateGraph`, `add_node`, `add_edge`, `add_conditional_edges`, `CompiledStateGraph.ainvoke/astream`).
**Compatibility:** Model-agnostic (any LLM provider via LangChain integrations); Python and JS/TS parity (LangGraph.js).
**Dependencies:** Python ≥3.10 era stack (langgraph packages on PyPI); pairs with LangChain integrations, LangSmith.
**Availability:** Active. Not archived (confirmed at inspection).
**Maintenance:** Active; 7,151 commits, 569 releases.
**License:** MIT.
**Limitations:** Boilerplate-heavy (a simple ReAct agent takes ~3× the code of Smolagents); developers work directly with graph state; steeper learning curve than role-based frameworks.
**Related resources:** LangChain, LangSmith (observability/deploy), Deep Agents (higher-level package on LangGraph), LangGraph.js.
**Sources:** https://github.com/langchain-ai/langgraph (inspected 2026-10-10); https://github.com/vicesaber/langgraph-multi-agent-workflow-showcase; https://opendatascience.com/ai-agent-orchestration-frameworks-github/
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** Microsoft AutoGen
**Canonical identity:** microsoft/autogen (Microsoft)
**Category:** Multi-agent systems and orchestration — conversational multi-agent framework
**Type:** Open-source framework (Python + .NET)
**Official URL:** https://github.com/microsoft/autogen
**Description:** Framework for creating multi-agent AI applications where agents communicate as participants in structured conversations (two-agent chat, group chat, sequential/swarm patterns). Pioneered the "agents as chat participants" model. **Now in maintenance mode** — README banner confirmed verbatim: "AutoGen is now in maintenance mode. It will not receive new features or enhancements and is community managed going forward. New users should start with Microsoft Agent Framework."
**Contents inspected:** Full README.md + repository metadata via browser.open, 2026-10-10. License files: docs under CC-BY-4.0; code under MIT (LICENSE-CODE).
**Actual capabilities (v0.4+ architecture, 3 layers):** Core API (message passing, event-driven agents, local/distributed runtimes, .NET + Python); AgentChat API (`AssistantAgent`, teams: `RoundRobinGroupChat`, `SelectorGroupChat`, `Swarm`, `MagenticOneGroupChat`; message types `TextMessage`/`HandoffMessage`/`ToolCallSummaryMessage`); Extensions API (model clients, code execution, MCP workbenches). Tooling: AutoGen Studio (no-code GUI, explicitly *not* production-ready per README), AutoGen Bench (benchmarking suite), Magentic-One reference team (web browsing, code execution, file handling).
**Usage domain:** Multi-agent research/prototyping; existing maintained deployments.
**Integration method:** `pip install -U "autogen-agentchat" "autogen-ext[openai"]`; async Python API; `autogenstudio ui --port 8080` for Studio.
**Compatibility:** OpenAI, Azure OpenAI, other model clients via extensions; MCP servers; .NET runtime.
**Dependencies:** Python 3.10+; model provider API keys.
**Availability:** Available but **maintenance mode since ~2025-10-02**; last Microsoft release `autogen-agentchat` 0.7.5 (2025-09-30) per secondary sources.
**Maintenance:** Community-managed; contributions limited to bug fixes/security/docs.
**License:** Code MIT (LICENSE-CODE); docs CC-BY-4.0.
**Limitations:** No new features; new projects directed to Microsoft Agent Framework; conversational model can produce circular/hallucinated loops without structured schemas.
**Related resources:** Microsoft Agent Framework (successor), AG2 (community fork), AutoGen Studio, AutoGen Bench, Magentic-One, Semantic Kernel.
**Sources:** https://github.com/microsoft/autogen (inspected 2026-10-10); https://intelligenttools.co/blog/what-happened-to-autogen; https://github.com/alex8791-cyber/cognithor/blob/HEAD/docs/competitive-analysis/autogen.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** AG2 (AutoGen fork)
**Canonical identity:** Community fork by the original AutoGen authors (exact org URL not confirmed in this pass)
**Category:** Multi-agent systems and orchestration — community continuation of AutoGen
**Type:** Open-source fork
**Official URL:** Not verified (PyPI package name `autogen` is owned by this fork per intelligenttools.co, 2026-10-06)
**Description:** Fork of Microsoft AutoGen maintained by the original AutoGen authors after Microsoft moved the upstream into maintenance mode. Owns the `autogen` package name on PyPI.
**Contents inspected:** Secondary only (intelligenttools.co install survey, 2026-10-05/06; cognithor competitive analysis, 2026-04-25).
**Actual capabilities:** Continues the AutoGen conversational multi-agent line outside Microsoft. Specific capabilities not inspected in this pass.
**Usage domain:** Drop-in continuity for AutoGen users who do not want Microsoft Agent Framework.
**Integration method:** `pip install autogen` (PyPI name ownership).
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** Active per secondary reports.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Fork-vs-upstream divergence risk; smaller maintainer base than Microsoft-backed successor.
**Related resources:** microsoft/autogen, Microsoft Agent Framework.
**Sources:** https://intelligenttools.co/blog/what-happened-to-autogen; https://github.com/alex8791-cyber/cognithor/blob/HEAD/docs/competitive-analysis/autogen.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** Microsoft Agent Framework (MAF)
**Canonical identity:** Microsoft Agent Framework (Microsoft)
**Category:** Multi-agent systems and orchestration — enterprise agent SDK
**Type:** Open-source SDK (Python + .NET)
**Official URL:** Migration guide: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/ (repo URL not confirmed in this pass)
**Description:** Microsoft's production successor to AutoGen, merging AutoGen's agent abstractions with Semantic Kernel's enterprise plumbing. Reached 1.0 on PyPI 2026-04-02; Python package ~1.19.0 / .NET ~1.22.0 as of 2026-09-18 (per tech-insider.org setup guide, 2026-09-28). Adds graph-based workflows, middleware, telemetry, A2A/MCP interop.
**Contents inspected:** Secondary only (README banner on microsoft/autogen; migration guide reference; cognithor analysis; tech-insider.org).
**Actual capabilities:** Multi-agent orchestration, graph-based workflows, enterprise state management, middleware, telemetry, multi-provider model support, cross-runtime interop via A2A and MCP.
**Usage domain:** Azure/Microsoft-shop production agents; enterprise multi-agent fleets.
**Integration method:** Python package (PyPI) and .NET package; migration guide from AutoGen.
**Compatibility:** A2A, MCP; multi-model providers.
**Dependencies:** Not verified.
**Availability:** Active; current supported platform.
**Maintenance:** Active (Microsoft).
**License:** Not verified in this pass.
**Limitations:** Newer API surface with early-preview churn reported by users; enterprise/Azure gravity.
**Related resources:** microsoft/autogen, Semantic Kernel, AG2.
**Sources:** https://github.com/microsoft/autogen (successor banner, inspected 2026-10-10); https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/; https://tech-insider.org/microsoft-agent-framework-setup-2026/; https://www.analyticsinsight.net/artificial-intelligence/microsoft-autogen-explained-building-multi-agent-ai-systems
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Partially verified

---

**Resource name:** CrewAI
**Canonical identity:** crewAIInc/crewAI (CrewAI Inc., founded by Joao Moura)
**Category:** Multi-agent systems and orchestration — role-based crew framework
**Type:** Open-source framework (Python), open-core commercial (CrewAI AMP)
**Official URL:** https://github.com/crewAIInc/crewAI · https://www.crewai.com/
**Description:** Python-native framework where agents are defined like human team members (role, goal, backstory, toolset) and organized into *Crews* (autonomous collaboration: sequential, parallel, hierarchical with automatic manager, consensual processes) and *Flows* (event-driven workflows with conditional branching and state). Built from scratch with no LangChain dependency (dependency removed in v1.14). ~52k–59k stars across reports (Sept 2026).
**Contents inspected:** Secondary: products/crewai.md catalog entry (status Active, v1.14.5, MIT, Python ≥3.10,<3.14); dev.to comparison (streaming since 1.10.1, A2A protocol compatibility, MCP integration); chaitanyagiri blog post (enterprise AMP platform).
**Actual capabilities:** Role-based agent definition; crews with sequential/hierarchical/parallel execution; Flows for precise control; task delegation between agents; streaming; A2A protocol support; MCP integration; LiteLLM-compatible backends (OpenAI default, Ollama local). Managed deployment/observability/governance via commercial AMP.
**Usage domain:** Explicit multi-agent collaboration, role-based delegation, rapid prototyping of agent teams.
**Integration method:** `pip install crewai`; Python API (`Agent`, `Task`, `Crew`, `Flow`); BYO LLM API key.
**Compatibility:** 100+ LLMs via LiteLLM; MCP; A2A.
**Dependencies:** Python 3.10+; LLM API key (or local via Ollama).
**Availability:** Active. Last release v1.15.22 (2026-09-16) per tech-insider.org.
**Maintenance:** Active; ~$18M funding (seed + Series A, Oct 2024); ~29 employees (2025).
**License:** MIT.
**Limitations:** Error handling reported as too coarse-grained for serious production; abstraction favors simplicity over fine-grained control; several teams prototype in CrewAI and migrate to LangGraph for complex state management.
**Related resources:** CrewAI AMP (commercial), LangGraph, AutoGen.
**Sources:** https://github.com/crewAIInc/crewAI; https://github.com/ciferateam/awesome-agents-team/blob/HEAD/products/crewai.md; https://dev.to/saaro_net/multi-agent-orchestration-2026-langgraph-crewai-and-autogen-compared-34bd; https://github.com/chaitanyagiri/munder-difflin/blob/HEAD/blog/src/posts/crewai-autogen-vs-a-local-agent-harness.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** OpenAI Agents SDK
**Canonical identity:** openai/openai-agents-python (OpenAI) + openai/openai-agents-js
**Category:** Multi-agent systems and orchestration — handoff-based lightweight SDK
**Type:** Open-source SDK (Python + TypeScript)
**Official URL:** https://github.com/openai/openai-agents-python
**Description:** Lightweight production-ready framework built around three primitives: **Agents** (LLMs with instructions + tools), **Handoffs** (agents delegating control to specialized agents), **Guardrails** (input/output validation). Production-grade evolution of the experimental OpenAI Swarm framework (released March 2025). Provider-agnostic despite the name (100+ LLMs via Chat Completions API / LiteLLM).
**Contents inspected:** Secondary: ai-tool-review entry (26.9k stars, active, last verified 2026-06-03); SKILL.md references (core pattern: coordinator with handoffs, guardrails, sessions, tracing); senior-engineer roadmap (dynamic peer handoffs, turnkey guardrails).
**Actual capabilities:** Dynamic peer handoffs (first-class primitive); input/output guardrail interceptors (prompt-injection scanning, PII, budget limits); `Runner` manages loop execution and turn counts; sessions (conversation history across runs); tracing (built-in + Logfire/AgentOps/Braintrust); realtime voice agents (`@openai/agents-realtime`); structured tool schemas.
**Usage domain:** Customer-support swarms, triage→specialist routing, low-latency realtime voice agents, moderate-complexity (3–5 agent) systems.
**Integration method:** `pip install openai-agents` / `npm install @openai/agents`; `Agent(...)`, `handoff(...)`, `Runner.run/run_sync/run_streamed`.
**Compatibility:** Provider-agnostic (OpenAI, Anthropic, Gemini via LiteLLM); MCP; works with AG-UI frontends.
**Dependencies:** Model provider API key (or LiteLLM).
**Availability:** Active.
**Maintenance:** Active (OpenAI).
**License:** MIT (per ai-tool-review; TypeScript SDK packages `@openai/agents@0.2.1`).
**Limitations:** Simpler by design — less built-in machinery for complex cyclic workflows than LangGraph; multi-agent model is handoff-centric (no native shared blackboard/state kernel).
**Related resources:** OpenAI Swarm (predecessor, archived), AG-UI, Mastra.
**Sources:** https://github.com/openai/openai-agents-python; https://github.com/achisolomon/ai-tool-review/blob/HEAD/data/_tools/developers/agent-frameworks/code-first/openai-agents-sdk.md; https://github.com/hezzicode/hackathon-v-research-agent/blob/HEAD/.claude/skills/openai-agents-sdk/SKILL.md; https://github.com/dip4k/senior-engineer-to-ai-engineer-roadmap/blob/HEAD/04-agentic-systems-and-orchestration/07-agent-development-platforms-and-adks.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** OpenAI Swarm
**Canonical identity:** openai/swarm (OpenAI)
**Category:** Multi-agent systems and orchestration — experimental predecessor
**Type:** Open-source (experimental)
**Official URL:** https://github.com/openai/swarm
**Description:** Lightweight experimental framework for agent handoffs, context variables, and function-calling patterns. Superseded by the OpenAI Agents SDK (March 2025).
**Contents inspected:** Secondary mentions only.
**Actual capabilities:** Agent handoff primitives, context variables; research/experimental scope.
**Usage domain:** Historical reference; prototyping lineage for Agents SDK.
**Integration method:** Not applicable (superseded).
**Compatibility:** Not applicable.
**Dependencies:** Not applicable.
**Availability:** Superseded; repo status not re-checked in this pass.
**Maintenance:** None (experimental).
**License:** Not verified.
**Limitations:** Experimental; replaced by OpenAI Agents SDK.
**Related resources:** OpenAI Agents SDK.
**Sources:** https://github.com/openai/swarm (via https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026)
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Historical

---

**Resource name:** Google Agent Development Kit (ADK)
**Canonical identity:** google/adk-python (+ adk-go, adk-java, adk-typescript, adk-kotlin) (Google)
**Category:** Multi-agent systems and orchestration — hierarchical multi-agent framework
**Type:** Open-source framework (Python, Go, Java, TypeScript, Kotlin)
**Official URL:** https://github.com/google/adk-python · Release notes: https://github.com/google/adk-python/releases/tag/v2.0.0
**Description:** Open-source, code-first toolkit for building, evaluating, debugging, and deploying AI agents and multi-agent systems. Model-agnostic (optimized for Gemini; LiteLLM for others). v2.0 GA (2026-05-19) moved from strict hierarchy to a **directed execution-graph engine** with dual orchestration (graph-based workflows with fixed logical gates + dynamic programmatic workflows), formal Task API for agent-to-agent delegation, native A2A support, and human-in-the-loop as graph primitives. Kotlin ADK 1.0 (2026-09-09) brought on-device/Android support.
**Contents inspected:** Secondary: v2.0.0 release notes (multi-agent workflow engine, dynamic agent collaboration); ADK Python SKILL.md (LlmAgent, SequentialAgent, ParallelAgent, LoopAgent, sub_agents, deployment to Vertex AI/Cloud Run); Kotlin 1.0 press coverage (hierarchical multi-agent, context compaction, session resumability, `@Tool`/`@Param` compile-time schemas).
**Actual capabilities:** `LlmAgent` (dynamic routing), `SequentialAgent`, `ParallelAgent`, `LoopAgent`; parent→child delegation trees; graph execution engine with checkpoints and resume-from-checkpoint; HITL gates as native primitives; context compaction; session pause/serialize/restore; built-in eval; deployment to Vertex AI Agent Engine / Cloud Run; enterprise hooks (Vertex AI session, RAG memory).
**Usage domain:** Production multi-agent systems, especially GCP/Gemini environments; polyglot enterprise backends; on-device agents (Kotlin).
**Integration method:** `pip install google-adk`; Python/Go/Java/TS/Kotlin APIs; agents communicate cross-language via A2A.
**Compatibility:** A2A protocol native; MCP tools; LiteLLM model backends; works with AG-UI frontends.
**Dependencies:** Python/Go/Java/TS/Kotlin runtimes; optional Vertex AI.
**Availability:** Active. v2.0 GA 2026-05-19; Kotlin 1.0 2026-09-09; Go 1.0 March 2026.
**Maintenance:** Active (Google).
**License:** Not verified in this pass (reported open source).
**Limitations:** Deep Google Cloud coupling in practice despite model-agnosticism; v2.0 rewrote the execution layer — upgrading from 1.x has incompatibilities (storage, event schema).
**Related resources:** A2A protocol, Vertex AI Agent Engine, LangGraph, CrewAI.
**Sources:** https://github.com/google/adk-python/releases/tag/v2.0.0; https://github.com/majiayu000/claude-skill-registry (SKILL.md); https://www.opensourceforu.com/2026/09/google-unveils-agent-development-kit/; https://news.ssbcrack.com/google-releases-adk-for-kotlin-1-0-for-production-ai-agents-on-android-and-jvm/
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** MetaGPT
**Canonical identity:** FoundationAgents/MetaGPT (formerly geekan/MetaGPT) — DeepWisdom
**Category:** Multi-agent systems and orchestration — SOP-driven software-company simulation
**Type:** Open-source framework (Python)
**Official URL:** https://github.com/FoundationAgents/MetaGPT (new org) · https://github.com/geekan/MetaGPT (legacy) · https://www.deepwisdom.ai · https://mgx.dev (commercial MGX)
**Description:** Multi-agent framework encoding human Standard Operating Procedures into agent systems ("Code = SOP(Team)"). Simulates a software company: Product Manager → Architect → Project Manager → Engineer → QA. Agents communicate via **structured documents** (PRDs, system designs, task breakdowns, unified diffs) instead of free-form chat, to avoid circular logic. Takes a one-line requirement and generates requirements docs, data structures, APIs, code, and unit tests. Commercial product: MGX (MetaGPT X), "AI agent development team" (mgx.dev, launched Feb 2025).
**Contents inspected:** Secondary: its-all-about-agents spec pages (MetaGPT + MetaGPT Studio); AgentoolRank activity analysis (last commit Jan 2026, ~70.7k stars); legacy repo README (winnie0618/metagpt mirror; News: GovTrace-Agent prototype Jul 2026); czyarl THIRD_PARTY_NOTICES (upstream now FoundationAgents/MetaGPT, MIT).
**Actual capabilities:** SOP role pipeline (PM→architect→engineer→QA); structured communication schema (PRD, architecture, tasks, diffs); MetaGPT Studio (visual IDE: artifact inspector, role customization, one-click project export); research artifacts (AFlow — automating agentic workflow generation, ICLR 2025 oral; SPO/AOT papers).
**Usage domain:** Automating full software-development workflows end-to-end from requirements.
**Integration method:** Python package / CLI; Studio web UI.
**Compatibility:** Not verified.
**Dependencies:** LLM API key.
**Availability:** Repository migrated from `geekan/MetaGPT` to `FoundationAgents/MetaGPT`; activity reduced (last commit reported Jan 2026).
**Maintenance:** Uncertain — flagship appears to be commercial MGX; open-source repo quiet since Jan 2026.
**License:** MIT.
**Limitations:** Pipeline rigidity (limited human-in-the-loop by design); open-source line appears deprioritized vs MGX; verify current state before adoption.
**Related resources:** MGX (mgx.dev), MetaGPT Studio, ChatDev (similar lineage), AutoGen.
**Sources:** https://github.com/FoundationAgents/MetaGPT; https://github.com/viveknimbolkar/its-all-about-agents/blob/HEAD/agents/multi-agent-systems/metagpt.md; https://dev.to/agentoolrank/stars-lie-669-open-source-ai-agent-repos-ranked-by-what-they-actually-do-1fdb; https://github.com/czyarl/devs_gen_code/blob/HEAD/THIRD_PARTY_NOTICES.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** AWS Strands Agents
**Canonical identity:** strands-agents/sdk-python (AWS) · strandsagents.com
**Category:** Multi-agent systems and orchestration — model-driven agent SDK/harness
**Type:** Open-source SDK (Python + TypeScript), Apache-2.0
**Official URL:** https://github.com/strands-agents/sdk-python · https://strandsagents.com
**Description:** Open-source, **model-driven** SDK: the LLM drives tool selection and planning autonomously (no hardcoded task flows). Created from production systems inside Amazon (powers Amazon Q Developer, AWS Glue, VPC Reachability Analyzer); announced May 2025, 1.0 July 2025. PyPI `strands-agents` v1.50.2 (2026-07-27) per secondary research; org consolidating into `strands-agents/harness-sdk` monorepo.
**Contents inspected:** Secondary: cu-aaii/ai-dlc-workshop research doc (verified Aug 2026 state); everydev.ai overview; cline/skills design ref; jithinkk/ai-harnesses patterns doc.
**Actual capabilities:** `Agent(model=..., tools=[...], system_prompt=...)` + model-driven loop; multi-agent primitives — Agents-as-Tools (hierarchical), Swarms (collaborative), Graphs (deterministic); A2A protocol support; sessions (durable persistence: S3/file/custom DAO); hooks/guardrails incl. `HumanInTheLoop(allowed_tools=[...])`; conversation managers; observability; hardened shell execution, file read/write tools, web search, subagent handoff protocols; unique session IDs with resume across restarts. Deploys on Bedrock AgentCore Runtime (microVM isolation, 8-hour sessions, auto-scaling).
**Usage domain:** AWS-native production agents; multi-model multi-agent systems.
**Integration method:** `pip install strands-agents`; `@tool` decorator; Python/TS API.
**Compatibility:** Model-agnostic (Bedrock default; Anthropic, OpenAI incl. Responses API, Gemini, Ollama, llama.cpp, LiteLLM, Cohere, Mistral, SageMaker); MCP; A2A.
**Dependencies:** Python ≥3.10; model provider credentials (Bedrock default).
**Availability:** Active (~6.8k stars, ~2,300 commits at Aug 2026 check).
**Maintenance:** Active (AWS).
**License:** Apache-2.0.
**Limitations:** AWS gravity for the full deployment story (AgentCore); multi-agent state is pattern-based rather than a shared kernel.
**Related resources:** Amazon Bedrock AgentCore, MCP, A2A.
**Sources:** https://github.com/strands-agents/sdk-python; https://github.com/cu-aaii/ai-dlc-workshop/blob/HEAD/docs/aidlc/builder-mcp/construction/strands-research.md; https://github.com/cline/skills/blob/HEAD/skills/gcp-to-aws/references/design-refs/design-ref-agentic-to-agentcore.md; https://github.com/jithinkk/ai-harnesses/blob/HEAD/strands_harness/README.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** PydanticAI
**Canonical identity:** pydantic/pydantic-ai (Pydantic team)
**Category:** Multi-agent systems and orchestration — type-safe agent engine
**Type:** Open-source framework (Python), MIT
**Official URL:** https://github.com/pydantic/pydantic-ai (repo URL standard; package: `pydantic-ai` on PyPI)
**Description:** Lightweight Python agent framework from the Pydantic team applying FastAPI-style engineering rigor to agents: **type safety, dependency injection, and schema validation** at every step. `Agent` is generic (`Agent[DepsType, OutputType]`); model outputs validated against Pydantic models; run modes `run/run_sync/run_stream/iter` (graph node iteration). v2.x line in 2026 (v2.46 per aiagentskit). Not a full multi-agent orchestrator — multi-agent via delegation/handoff patterns built in user code; has a graph extension (`pydantic-graph`) and evals/durable-execution support.
**Contents inspected:** Secondary: kingsidharth/skills SKILL.md (architecture, install, reference files incl. multi-agent.md, advanced.md); aiagentskit comparison; ainexislab analysis; cirocampos1 skill page.
**Actual capabilities:** Typed agents with `output_type`/`deps_type`; `@agent.tool` function tools; toolsets; deferred tools; built-in tools; MCP support; structured/streaming output with validation; model/provider strings with fallback; capabilities and hooks; agent specs (YAML/JSON); AG-UI adapter (`pydantic-ai-slim[ag-ui]`); Logfire observability extra; multi-agent delegation/handoff docs; Temporal integration for durable agents (per secondary).
**Usage domain:** Production services embedding agents as components (FastAPI backends, validated event processors, structured decision engines).
**Integration method:** `uv add pydantic-ai` (+ provider extras); Python API; global agent instantiation like FastAPI app.
**Compatibility:** Model-agnostic (OpenAI, Anthropic, Google, Groq, Mistral, Cohere, Bedrock, HuggingFace, Ollama); MCP; AG-UI; Logfire.
**Dependencies:** Python 3.9+; pydantic v2.
**Availability:** Active.
**Maintenance:** Active (Pydantic team).
**License:** MIT.
**Limitations:** Not a complete multi-agent orchestrator out of the box; no built-in tool marketplace; strictness can slow rapid prototyping.
**Related resources:** Pydantic, Logfire, LangGraph (often paired), AG-UI.
**Sources:** https://github.com/kingsidharth/skills/blob/HEAD/pydantic-ai-python/SKILL.md; https://aiagentskit.com/blog/pydantic-ai-vs-langchain-vs-langgraph/; https://ainexislab.com/crewai-vs-langgraph-vs-pydanticai-agent-picks-2026/; https://www.speakeasy.com/blog/ai-agent-framework-comparison
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** Smolagents
**Canonical identity:** huggingface/smolagents (Hugging Face)
**Category:** Multi-agent systems and orchestration — minimal code-first agent library
**Type:** Open-source library (Python), Apache-2.0
**Official URL:** https://github.com/huggingface/smolagents · Docs: https://huggingface.co/docs/smolagents
**Description:** Minimal (~1,000 lines of core logic) agent library where **agents act by writing and executing Python code** rather than emitting JSON tool calls. Two paradigms: `CodeAgent` (writes code as actions; any Python library becomes a tool via authorized imports) and `ToolCallingAgent` (structured JSON tool calls). Launched Jan 2025; ~26k stars; 200+ contributors; very actively maintained (mid-2026).
**Contents inspected:** Secondary: altan2026/smolagents README mirror (full feature list); api-evangelist/smolagents catalog entry; francisezhang deployment guide; skill-suggestion issue.
**Actual capabilities:** Code-first actions; model-agnostic (local transformers/Ollama, HF Inference Providers, OpenAI, Anthropic, LiteLLM 100+, Azure OpenAI, Bedrock, MLX); sandboxed code execution (Blaxel, E2B, Modal, Docker, Pyodide+Deno WASM); Hub integration (share/pull tools and agents as Gradio Spaces); multi-agent hierarchical orchestration (manager agents coordinating sub-agents); modality-agnostic (text, vision, video, audio); tool-agnostic (MCP servers, LangChain tools, Hub Spaces as tools); built-in web search.
**Usage domain:** Research and code-execution agents; data-analysis pipelines; HF-ecosystem users; lightweight lane agents.
**Integration method:** `pip install smolagents`; `CodeAgent(tools=[...], model=...)`; `agent.run("...")`.
**Compatibility:** Any LLM via LiteLLM; MCP; LangChain tools; Gradio Spaces.
**Dependencies:** Python; model provider or local model.
**Availability:** Active.
**Maintenance:** Active (Hugging Face).
**License:** Apache-2.0.
**Limitations:** Model-quality dependent — below ~7B parameters code bugs creep in; any-Python-as-tool widens the sandboxing attack surface (sandbox choice is on the user).
**Related resources:** Hugging Face Hub, Gradio, E2B, LiteLLM.
**Sources:** https://github.com/huggingface/smolagents; https://github.com/altan2026/smolagents; https://huggingface.co/docs/smolagents; https://github.com/api-evangelist/smolagents
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** BeeAI Framework
**Canonical identity:** i-am-bee/beeai-framework (IBM Research)
**Category:** Multi-agent systems and orchestration — production-grade multi-agent toolkit
**Type:** Open-source framework (Python + TypeScript), LF AI & Data hosted
**Official URL:** https://framework.beeai.dev/ · Org: https://github.com/i-am-bee
**Description:** Open-source toolkit from IBM Research for building production-grade multi-agent systems; donated to LF AI & Data (with Docling, Data Prep Kit). "First open-source agent-to-agent platform" for building, discovering, running, and composing agents and multi-agent workflows; originally powered by IBM's Agent Communication Protocol (ACP), now aligned with A2A.
**Contents inspected:** Secondary: future-agi/traceai BeeAI integration README (quick start, `beeai-framework` PyPI); IBM Developer comparison (CrewAI/LangGraph/BeeAI); traceloop/openllmetry feature request (observability schema); PR Newswire induction notice.
**Actual capabilities:** Agent + workflow constructs for designing custom agent architectures (no one-size-fits-all); role/instructions-based agents; tool integration; multi-provider LLM support (optimized for IBM Granite and Llama, others supported); ACP/A2A serving (`ACPServer` exposes agents; `beeai-framework[acp]`); built-in OpenInference instrumentation; Python and TypeScript.
**Usage domain:** Enterprise multi-agent systems, especially IBM Granite/Llama stacks; ACP/A2A-interoperable agent services.
**Integration method:** `pip install beeai-framework`; `Agent(llm=ChatModel.from_name(...), role=..., instructions=...)`; `agent.run(...)`.
**Compatibility:** MCP; ACP; A2A; OpenInference/OpenTelemetry observability.
**Dependencies:** Model backend (incl. `ollama:granite3.1-dense:8b` example).
**Availability:** Active; LF AI & Data project.
**Maintenance:** Active (IBM Research).
**License:** Not verified in this pass (reported open source).
**Limitations:** ACP→A2A migration in progress; smaller ecosystem than LangGraph/CrewAI.
**Related resources:** ACP (IBM, merged into A2A), A2A, IBM Granite, Docling.
**Sources:** https://framework.beeai.dev/; https://github.com/future-agi/traceai/blob/HEAD/python/frameworks/beeai/README.md; https://github.com/traceloop/openllmetry/issues/2804; https://pypi.org/project/traceai-beeai/
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Verified

---

**Resource name:** Mastra
**Canonical identity:** mastra (mastra.ai)
**Category:** Multi-agent systems and orchestration — TypeScript-native agent framework
**Type:** Open-source framework (TypeScript), Apache-2.0
**Official URL:** Not verified in this pass (mastra.ai referenced in secondary sources)
**Description:** TypeScript-native agent framework for Next.js/Node.js/Bun environments. ReAct and graph workflows; multi-agent via **Agent Networks**; 4 memory types + observational memory; Mastra Cloud (beta) managed hosting.
**Contents inspected:** Secondary only: eboot/vibes-plug SKILL.md (Agent + MastraMemory example); speakeasy.com comparison table (Apache 2.0, Agent Networks, Mastra Cloud beta).
**Actual capabilities:** TS-native agents with instructions/models/memory; `createTool` with zod schemas; agent networks for multi-agent; workflow graphs; observability hooks.
**Usage domain:** Full-stack TypeScript teams building agents into web apps.
**Integration method:** npm (`@mastra/core`).
**Compatibility:** Anthropic, OpenAI, others via model config; storage adapters (e.g., Supabase).
**Dependencies:** Node.js/Bun; model provider.
**Availability:** Active per secondary reports.
**Maintenance:** Not verified.
**License:** Apache-2.0.
**Limitations:** TypeScript-only; cloud in beta.
**Related resources:** Vercel AI SDK, OpenAI Agents SDK (JS), AG-UI.
**Sources:** https://github.com/eboot/vibes-plug/blob/HEAD/skills/multi-agent-orchestration/SKILL.md; https://www.speakeasy.com/blog/ai-agent-framework-comparison
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** Hermes Agent (Nous Research)
**Canonical identity:** hermes-agent (Nous Research) — exact repo URL not verified in this pass
**Category:** Multi-agent systems and orchestration — self-improving personal agent
**Type:** Open-source framework
**Official URL:** Not verified
**Description:** Framework designed around a **closed learning loop**: main agent receives messages, delegates to subagents for parallel work, and persists learnings automatically. Four-tier memory pipeline (working → episodic → semantic → procedural); creates skills from experience and improves them during use; 40+ built-in tools; cron scheduler for unattended automations; unified multi-platform gateway (Telegram, Discord, Slack, WhatsApp, Signal) from a single process; terminal backends for seven environments (local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox).
**Contents inspected:** Secondary only: driphtyio/hermes-tutorials comparison (hermes-vs-langchain-vs-crewai-2026.mdx).
**Actual capabilities:** As described; parallel subagent delegation; automatic learning persistence; scheduled automations; multi-platform messaging gateway.
**Usage domain:** Personal agent / learning-loop systems.
**Integration method:** Not verified.
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** Status unclear from a single secondary source.
**Maintenance:** Not verified.
**License:** MIT (per secondary comparison).
**Limitations:** Star-count claim in the single secondary source (~167k) is implausible without corroboration — treated as unreliable; all details single-sourced.
**Related resources:** LangChain/LangGraph, CrewAI, AutoGen.
**Sources:** https://github.com/driphtyio/hermes-tutorials/blob/HEAD/src/content/blog/hermes-vs-langchain-vs-crewai-2026.mdx
**Verification date:** 2026-10-10
**Confidence:** Low
**Verification label:** Unresolved

---

**Resource name:** Meta Llama Stack
**Canonical identity:** Meta Llama Stack (Meta)
**Category:** Multi-agent systems and orchestration — standardized API stack for open-weight models
**Type:** Open-source API specification + implementation
**Official URL:** Not verified in this pass
**Description:** Modular standardized API provider architecture making open-weight models (Llama 3/4) first-class enterprise citizens: standardized REST/gRPC interfaces for Inference API (vLLM, Ollama, TGI, cloud), Agent API (autonomous ReAct loops), Tool Runtime API (sandboxed Python/shell), Memory API (vector/hybrid/graph), Safety API (integrated Llama Guard 3).
**Contents inspected:** Secondary only: dip4k/senior-engineer roadmap section 3.4.
**Actual capabilities:** Provider-agnostic agent runtime behind standard APIs; memory and safety services.
**Usage domain:** On-premise/air-gapped deployments; defense/finance; self-hosted open-weight GPU clusters.
**Integration method:** Not verified.
**Compatibility:** vLLM, Ollama, TGI; Llama Guard 3.
**Dependencies:** Not verified.
**Availability:** Active per secondary reports.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced in this pass; enterprise/on-prem focus.
**Related resources:** vLLM, Ollama, Llama Guard.
**Sources:** https://github.com/dip4k/senior-engineer-to-ai-engineer-roadmap/blob/HEAD/04-agentic-systems-and-orchestration/07-agent-development-platforms-and-adks.md
**Verification date:** 2026-10-10
**Confidence:** Low-Medium
**Verification label:** Partially verified

---

### 9.2 Agent-to-agent protocols and standards

---

**Resource name:** A2A — Agent2Agent Protocol
**Canonical identity:** a2aproject/A2A (Linux Foundation; contributed by Google)
**Category:** Agent communication — agent-to-agent protocol standard
**Type:** Open protocol specification + SDKs
**Official URL:** https://github.com/a2aproject/A2A · Spec: https://a2a-protocol.org/latest/specification/
**Description:** Open standard for communication between **opaque** agentic applications: agents advertise skills, exchange messages, delegate and track work, stream progress, and return artifacts **without exposing private reasoning or internal tools**. Launched by Google April 2025, donated to the Linux Foundation June 2025; **v1.0 released 2026-03-12** (v1.0.1 May 2026); 150+ supporting organizations; integrations in Google Cloud, Microsoft Copilot Studio/Foundry, Amazon Bedrock AgentCore. IBM's ACP merged into A2A (Aug 2025).
**Contents inspected:** Full README.md + repository metadata via browser.open, 2026-10-10 (26,086 stars, Apache-2.0, 647 commits, spec/ + docs/ directories). Secondary: v1.0 explainer articles; agent-card spec pages.
**Actual capabilities:** Discovery via Agent Cards (`/.well-known/agent-card.json`; required fields: name, description, version, supportedInterfaces, capabilities, defaultInputModes/OutputModes, skills); transports: JSON-RPC 2.0 over HTTP(S) (+ SSE streaming), gRPC, HTTP+JSON bindings; canonical data model (Task, Message, AgentCard, Part, Artifact, Extension); task lifecycle, push notifications, auth declaration, version negotiation. SDKs: Python (`a2a-sdk`), Go (`a2a-go`), JS (`@a2a-js/sdk`), Java, .NET (`A2A` NuGet), Rust (`a2a-lf`). Explicitly does NOT define: internal agent architecture, reasoning loop, memory, tool-selection policy, orchestration, trust policy.
**Usage domain:** Cross-vendor/cross-framework agent interop; enterprise multi-agent delegation.
**Integration method:** Host an Agent Card; implement JSON-RPC endpoints; use official SDKs; expose existing agents (LangGraph, ADK, BeeAI) as A2A servers.
**Compatibility:** Complements MCP (MCP = agent→tools; A2A = agent→agent); framework bridges exist for LangGraph, ADK, BeeAI, CrewAI.
**Dependencies:** HTTP(S) endpoint; TLS/auth per deployment.
**Availability:** Active; v1.0 stable.
**Maintenance:** Active (Linux Foundation governance).
**License:** Apache-2.0.
**Limitations:** Protocol only — scheduling, routing, retries, conflict resolution are the system designer's job; early examples used `/.well-known/agent.json`, now standardized to `agent-card.json` (migration caveat).
**Related resources:** MCP, AGNTCY, ACP (IBM, merged), AP2 (payments extension), AG-UI.
**Sources:** https://github.com/a2aproject/A2A (inspected 2026-10-10); https://a2a-protocol.org/latest/specification/; https://www.turingpost.com/p/a2a; https://www.mintmcp.com/blog/a2a-protocol-explained
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** ACP — Agent Communication Protocol (IBM / BeeAI)
**Canonical identity:** IBM Agent Communication Protocol (originated in BeeAI ecosystem; March 2025)
**Category:** Agent communication — legacy agent-to-agent protocol
**Type:** Open specification (OpenAPI 3.1.1), spec v0.2.0
**Official URL:** https://agentcommunicationprotocol.dev (reported to now describe ACP as "part of A2A"); IBM research page redirects to A2A
**Description:** IBM's open standard for agent-to-agent communication via **REST/HTTP** (OpenAPI-defined), emphasizing auditability, session continuity, and trajectory tracking (`TrajectoryMetadata`: every response can carry reasoning/tool-call logs). Four discovery methods; simpler `AgentManifest` than A2A's Agent Card. **Merged into A2A in August 2025; repository archived.** IBM's own docs redirect adopters to A2A; BeeAI (Agent Stack) adopted A2A as its interop protocol.
**Contents inspected:** Secondary: agent-sh/agent-knowledge comparison doc; boldare.com explainer; plurigrid/zig-syrup deep-dive (incl. ACP name-collision table); tjlsmith0831 AGENTS.md (BeeAI ACPServer usage).
**Actual capabilities (historical):** REST/JSON API; streaming; async; agent registry discovery; SDKs for Python/TypeScript (`acp-sdk`); BeeAI `ACPServer` hosting for ReAct agents.
**Usage domain:** Historical reference; legacy ACP deployments.
**Integration method:** Not applicable for new builds — target A2A.
**Compatibility:** MCP-compatible message types.
**Dependencies:** Not applicable.
**Availability:** Archived/merged.
**Maintenance:** None — independent development ended.
**License:** Not verified.
**Limitations:** Deprecated; do not design new architecture around it. Name collision: "ACP" also = OpenAI/Stripe Agentic Commerce Protocol, Zed's Agent Client Protocol, AGNTCY's Agent Connect Protocol (archived Apr 2026) — always disambiguate.
**Related resources:** A2A (successor), BeeAI, AGNTCY.
**Sources:** https://github.com/agent-sh/agent-knowledge/blob/HEAD/acp-with-codex-gemini-copilot-claude.md; https://www.boldare.com/blog/agent-communication-protocol-acp-explained-what-it-is-and-why-it-matters/; https://github.com/plurigrid/zig-syrup/blob/HEAD/agentic-protocols-research/04-acp-deep-dive.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Archived

---

**Resource name:** AG-UI — Agent-User Interaction Protocol
**Canonical identity:** ag-ui-protocol (CopilotKit) · https://ag-ui.com
**Category:** Agent communication — agent↔user-application protocol
**Type:** Open protocol specification + SDKs, MIT
**Official URL:** https://ag-ui.com/ · Spec: https://ag-ui.com/spec · Repo: https://github.com/CopilotKit/CopilotKit (AG-UI lives in the CopilotKit monorepo)
**Description:** Open standard for the **bidirectional event stream between agent backends and user-facing applications** — the "last mile" that standardizes streaming tokens, tool lifecycles, shared state sync, subagents, and human-in-the-loop interrupts so one agent can drive web/mobile/terminal/Slack surfaces without per-framework glue. Created by CopilotKit (Seattle; $27M Series A May 2026 led by Glilot Capital, NFX, SignalFire); **v1.0 spec released 2026-09-30**. Adopted per CopilotKit's announcement by Google, Microsoft, Amazon, Oracle; works with LangChain, Mastra, Google ADK, OpenAI Agents SDK, Strands Agents, Microsoft Agent Framework, Pydantic AI.
**Contents inspected:** Secondary: agentfirst.directory tool entry (verificationLevel documentation-reviewed, 2026-09-03); abhisheksharma-17 research doc (spec 1.0 data model: RUN_STARTED/FINISHED/ERROR, TEXT_MESSAGE_*, TOOL_CALL_*, STATE_SNAPSHOT/DELTA (RFC 6902 JSON Patch), MESSAGES_SNAPSHOT, SUBAGENT_*, CUSTOM, HITL interrupts); sitepoint 1.0 article; geekwire funding article; cianfhoghlaim SKILL.md (wire format, install).
**Actual capabilities:** SSE transport with JSON event schema; lifecycle, text streaming, tool-call lifecycle (incl. multimodal tool results), state snapshot/delta sync, subagent events, HITL interrupts with id/reason/responseSchema/expiresAt; TS/Python/.NET SDKs generated from JSON Schema; framework bridges; resumable stream recovery via sequence numbers (declared capability).
**Usage domain:** Teams connecting an agent backend to an interactive frontend needing streamed output, shared state, tool calls, approvals, generative UI.
**Integration method:** Backend bridge emits AG-UI events → endpoint streams them; frontend AG-UI client validates events against spec. `bun add @ag-ui/core` / `uv add ag-ui` / `uv add 'pydantic-ai-slim[ag-ui]'`.
**Compatibility:** Framework bridges for LangChain/LangGraph, Mastra, Google ADK, OpenAI Agents SDK, Strands, MAF, Pydantic AI, Agno, BAML.
**Dependencies:** SSE-capable backend; frontend SDK.
**Availability:** Active; v1.0 stable (2026-09-30).
**Maintenance:** Active (CopilotKit).
**License:** MIT.
**Limitations:** Supplies the interaction contract, not a hosted agent or complete application; adopters operate their own backend/security; no formal conformance certification program found.
**Related resources:** CopilotKit, MCP Apps / A2UI (generative UI layers above AG-UI), A2A, MCP.
**Sources:** https://github.com/bradvin/agentfirst.directory/blob/HEAD/tools/ag-ui.md; https://www.sitepoint.com/ag-ui-1-0-stable-spec-agent-user-interaction/; https://www.geekwire.com/2026/seattles-copilotkit-raises-27m-as-some-of-the-biggest-names-in-tech-adopt-its-ai-agent-protocol/; https://github.com/cianfhoghlaim/cianchosaint/blob/HEAD/.agents/skills/ag-ui/SKILL.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** AGNTCY
**Canonical identity:** agntcy (Linux Foundation) · https://agntcy.org · https://github.com/agntcy
**Category:** Agent communication — Internet-of-Agents infrastructure stack
**Type:** Open-source stack + standards (Linux Foundation)
**Official URL:** https://agntcy.org · https://github.com/agntcy
**Description:** Linux Foundation project building "Internet of Agents" infrastructure — the **broader org-level stack** around A2A: discovery, identity, messaging, and observability across vendors and frameworks. 80+ member organizations (Cisco lead, Google, Oracle, Dell, Red Hat; frameworks: LangChain, LlamaIndex, CrewAI, AG2; eval: Galileo, Arize; observability: Traceloop). Components: **OASF** (Open Agentic Schema Framework — OCI-based agent description, superset of A2A Agent Cards), **Agent Directory** (federated cross-framework discovery; Kademlia DHT; Go SDK `github.com/agntcy/dir/client`), **SLIM** (Secure Low-Latency Interactive Messaging), **Identity** (DIDs + Verifiable Credentials), **Observability** (OpenTelemetry-based agent telemetry), **Security** (MLS encryption, trust verification). Its own Agent Connect Protocol was archived April 2026; A2A is now its preferred agent-invocation standard.
**Contents inspected:** Secondary: hop-top/aps gap-analysis doc (six components); kevin-biot OBO composability doc; sinaghadermarzi agent-protocol-landscape appendix; chgaowei/ai-agent-infra-list; alan-botts workflow explainer.
**Actual capabilities:** Federated agent discovery, decentralized identity, secure messaging, OTel observability, trust verification — complementary to A2A (wire) and MCP (tools).
**Usage domain:** Cross-vendor agent identity/discovery/observability substrate; enterprises needing governed multi-agent interop.
**Integration method:** Go SDK for directory client; OCI artifacts via ORAS for OASF records; opt-in per profile.
**Compatibility:** Works alongside A2A, MCP, SLIM.
**Dependencies:** Not verified.
**Availability:** Active; Linux Foundation-governed since July 2025.
**Maintenance:** Active.
**License:** Not verified.
**Limitations:** Broader scope than A2A = more moving parts; newer and less deployed than A2A/MCP.
**Related resources:** A2A, MCP, OASF, AP2, W3C AI Agent Protocol CG.
**Sources:** https://agntcy.org; https://github.com/agntcy; https://github.com/hop-top/aps/blob/HEAD/docs/plans/2026-03-01-agntcy-integration-gap-analysis.md; https://github.com/chgaowei/ai-agent-infra-list/blob/HEAD/ai-agent-infra-list.md
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Verified

---

**Resource name:** AP2 — Agent Payments Protocol
**Canonical identity:** google-agentic-commerce/AP2 · https://ap2-protocol.org
**Category:** Agent communication — agent payments/authorization extension
**Type:** Open protocol (A2A extension)
**Official URL:** https://ap2-protocol.org · https://github.com/google-agentic-commerce/AP2
**Description:** Google-led open protocol (with payments-industry partners; FIDO Alliance donation noted) for secure, interoperable AI-driven payments and authorization between agents and merchants. Ships as an **extension of A2A**: carries W3C Verifiable-Credential "Mandates" (Intent, Cart, Payment) so a merchant gets cryptographic proof an agent was authorized for *that* purchase. Production-grade in 2026 per secondary landscape docs.
**Contents inspected:** Secondary only (agent-protocol-landscape appendix; nth-dao landscape table; ai-agent-infra-list).
**Actual capabilities:** VDC-based mandates; checkout/payment mandate flows over A2A.
**Usage domain:** Agentic commerce — agents paying on behalf of users.
**Integration method:** Not verified.
**Compatibility:** A2A extension; complements MCP.
**Dependencies:** Not verified.
**Availability:** Active per secondary reports.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Payments-specific; not a general agent-to-agent task protocol.
**Related resources:** A2A, MCP, Commerce ACP (OpenAI/Stripe), UCP.
**Sources:** https://ap2-protocol.org; https://github.com/google-agentic-commerce/AP2; https://github.com/sinaghadermarzi/agentic-lab/blob/HEAD/appendices/R-agent-protocol-landscape.md; https://github.com/chgaowei/ai-agent-infra-list/blob/HEAD/ai-agent-infra-list.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** ANP — Agent Network Protocol / W3C AI Agent Protocol Community Group
**Canonical identity:** W3C Community Group — https://www.w3.org/community/agentprotocol/ · Drafts: https://w3c-cg.github.io/ai-agent-protocol/
**Category:** Agent communication — web-native agent protocol incubation
**Type:** Community-group drafts (W3C CG)
**Official URL:** https://www.w3.org/community/agentprotocol/
**Description:** W3C Community Group developing open, interoperable protocols so agents can discover, identify, and collaborate on the Web. ANP / `did:wba` (decentralized identifiers for web-based agents) work is incubated here. Early-stage relative to A2A.
**Contents inspected:** Secondary only (ai-agent-infra-list entry).
**Actual capabilities:** Not verified — drafts stage.
**Usage domain:** Long-term web-native agent interop.
**Integration method:** Not applicable yet.
**Compatibility:** Not verified.
**Dependencies:** Not applicable.
**Availability:** In development (drafts).
**Maintenance:** Active community group.
**License:** W3C CG licensing (not verified).
**Limitations:** Draft-stage; not deployable as a standard today.
**Related resources:** A2A, AGNTCY Identity (DIDs/VCs).
**Sources:** https://www.w3.org/community/agentprotocol/; https://github.com/chgaowei/ai-agent-infra-list/blob/HEAD/ai-agent-infra-list.md
**Verification date:** 2026-10-10
**Confidence:** Low-Medium
**Verification label:** Partially verified

---

**Resource name:** Zed Agent Client Protocol
**Canonical identity:** Zed (editor) — introduced August 2025
**Category:** Agent communication — editor↔agent interop protocol
**Type:** Open protocol (per secondary reports)
**Official URL:** Not verified in this pass
**Description:** Protocol introduced by the Zed editor (Aug 2025) for editor-to-agent interoperability — a distinct "ACP" from IBM's (name collision). Listed as one of four different ACPs in industry disambiguation guides.
**Contents inspected:** Secondary only (plurigrid/zig-syrup ACP chronology; medium.com ACP disambiguation).
**Actual capabilities:** Editor↔agent communication; details not verified.
**Usage domain:** Editor integrations with coding agents.
**Integration method:** Not verified.
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** Active per secondary reports (Acp.Net package family 0.1.1, Aug 2026 — .NET process/runtime/diagnostics support).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Name collision with IBM ACP and Commerce ACP causes persistent confusion; verify context before citing.
**Related resources:** Zed editor, MCP (overlapping problem space for editor tools).
**Sources:** https://github.com/plurigrid/zig-syrup/blob/HEAD/agentic-protocols-research/04-acp-deep-dive.md; https://medium.com/@mertbasar30/acp-is-not-one-protocol-a-chronological-guide-to-four-different-acps-and-where-acp-net-fits-41952bfef80e
**Verification date:** 2026-10-10
**Confidence:** Low-Medium
**Verification label:** Partially verified

---

**Resource name:** Commerce ACP (OpenAI/Stripe Agentic Commerce Protocol)
**Canonical identity:** OpenAI + Stripe — https://agenticcommerce.dev
**Category:** Agent communication — agentic commerce checkout protocol (NOT agent-to-agent)
**Type:** Open standard (Apache-2.0 per secondary), live since 2026-02-16
**Official URL:** https://agenticcommerce.dev (per secondary)
**Description:** 5-endpoint REST API enabling ChatGPT (800M+ WAU) chat-to-buy flows: checkout session lifecycle, Stripe Shared Payment Tokens, 4% OpenAI + Stripe fee model. Backers: OpenAI, Stripe, Visa, Etsy, PayPal. Governed by Stripe/OpenAI. A different protocol from IBM's ACP — the name collision is a known industry confusion source. Google's UCP (Universal Commerce Protocol, with Shopify) is the parallel search-to-buy standard.
**Contents inspected:** Secondary only (zig-syrup comparison table).
**Actual capabilities:** Checkout sessions; shared payment tokens; MCP tool exposure.
**Usage domain:** Merchants capturing chat-to-buy agentic commerce traffic.
**Integration method:** Stripe dashboard integration; REST endpoints.
**Compatibility:** MCP integration path.
**Dependencies:** Stripe merchant ID.
**Availability:** Live (Feb 2026).
**Maintenance:** Active (Stripe/OpenAI-controlled).
**License:** Apache-2.0.
**Limitations:** Commerce-scoped, not agent-to-agent; fee-bearing; governed by two companies (not a neutral foundation).
**Related resources:** AP2, UCP (Google/Shopify), MCP.
**Sources:** https://github.com/plurigrid/zig-syrup/blob/HEAD/agentic-protocols-research/04-acp-deep-dive.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Cross-reference — MCP (Model Context Protocol):** Anthropic's open standard for agent→tool/data/API connections (stdio, SSE, streamable HTTP). Governed by the Agentic AI Foundation (AAIF) since Dec 2025. Explicitly *not* an agent-to-agent protocol — complementary to A2A/ACP/AG-UI. Presumed catalogued elsewhere in the Atlas; not researched in depth here. Sources: agent-sh/agent-knowledge comparison; boldare.com explainer.

---

## PART 10 — HARNESS ENGINEERING AND AUTONOMOUS SOFTWARE DEVELOPMENT

### 10.1 Coding-agent harnesses and autonomous dev loops

---

**Resource name:** Munder Difflin
**Canonical identity:** chaitanyagiri/munder-difflin
**Category:** Harness engineering — local multi-agent coding harness
**Type:** Open-source desktop app (Electron, MIT), macOS/Windows/Linux
**Official URL:** https://github.com/chaitanyagiri/munder-difflin
**Description:** Local-first multi-agent harness framed as "an office of agents." Unlike frameworks you import, **the harness is the product**: it drives the agent CLIs you already run (Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Cursor, etc.) so it rides existing subscriptions. Each agent runs as a **real CLI process in its own `node-pty` PTY** (rendered with xterm.js), optionally in **per-agent git worktrees**. A **GOD orchestrator** routes tasks, adjudicates traffic, and escalates; "the hive" provides per-agent memory, atomic-file mailboxes, a shared blackboard, an append-only event log, and single-committer git; semantic recall mines markdown memory into a searchable "memory palace" with condensation. Control & safety: human gates (spend/scope/destructive ops), steer→constrain→stop circuit breaker, per-agent token budgets, real cost from transcripts, durable ledger, OTel spans, tool waterfall. Multiple "floors" (0.5.3+) = separate offices per folder.
**Contents inspected:** Full README excerpts via search results (architecture sections: the floor, memory & coordination, control & safety); companion blog post comparing CrewAI/AutoGen vs harness approach (crewai-autogen-vs-a-local-agent-harness.md).
**Actual capabilities:** Multi-CLI agent orchestration; PTY-isolated agents; git-worktree isolation; GOD orchestrator routing; shared blackboard + mailboxes + event log; semantic memory with condensation; enterprise knowledge graph; human approval gates; circuit breaker; per-agent budgets/telemetry/OTel; voice control ("Talk" button); multi-floor isolation.
**Usage domain:** Running a team of coding agents against local repos today with no code to write; local-first autonomous dev teams.
**Integration method:** Download app; onboarding wizard detects/installs agent CLIs; agents spawn as CLI subprocesses.
**Compatibility:** Claude Code, Antigravity (Gemini), OpenAI Codex, xAI Grok, Kimi Code, Gemini CLI, Qwen, OpenCode, Crush, pi.dev, GitHub Copilot CLI, Cursor, custom commands; BYO keys and local LLMs as options.
**Dependencies:** Installed agent CLIs; git; Electron runtime.
**Availability:** Active (README updated ~8 days before 2026-10-10).
**Maintenance:** Active.
**License:** MIT (per companion blog post).
**Limitations:** Harness, not a framework — not importable into your own app; local-machine bound (no cloud fleet); licensed (one licence covers all floors).
**Related resources:** CrewAI, AutoGen, LangGraph (frameworks — compared explicitly in its blog); OpenCode harnesses catalogued elsewhere.
**Sources:** https://github.com/chaitanyagiri/munder-difflin; https://github.com/chaitanyagiri/munder-difflin/blob/HEAD/blog/src/posts/crewai-autogen-vs-a-local-agent-harness.md; https://github.com/uguratadargun/office/blob/HEAD/blog/src/posts/crewai-autogen-vs-a-local-agent-harness.md
**Verification date:** 2026-10-10
**Confidence:** High (README inspected via search-result excerpts; repo page not opened directly)
**Verification label:** Partially verified

---

**Resource name:** Aider
**Canonical identity:** Aider-AI/aider
**Category:** Harness engineering — terminal pair-programming agent
**Type:** Open-source CLI (Python), free/BYOK
**Official URL:** https://github.com/Aider-AI/aider
**Description:** Veteran terminal-based AI pair programmer. Connects to your git repo, builds a **repository map** (compressed codebase summary for model navigation beyond context windows), and makes clean, well-structured commits. Chat-driven: `/add` files to context, `/architect` (propose-then-confirm), `/ask` (read-only questions), `/run` shell commands with output fed back to the model, `/diff`, `/undo` (reverts last AI commit via git), `/map`. Entire workflow is git-based (offers `git init` if absent; chat history kept out of commits via .gitignore).
**Contents inspected:** Secondary: afloat16/ai-dev-steward survey (~49.3k stars); betterstack guide (setup, DeepSeek Coder example, git workflow); teliaz CLI command table; aiproductweekly roundup. Note: one search hit pointed at `pietrosperoni/aider` (outdated mirror text) — canonical is Aider-AI/aider.
**Actual capabilities:** Repo-map context compression; file add/drop context management; architect/ask modes; shell execution with feedback loop; git-native commits/undo/diff; broad model support (any LLM via API key, `--model` flag); Aider polyglot edit benchmark (multi-language edit tasks).
**Usage domain:** Terminal-native developers; greenfield features; git-clean workflows; edit-task quality.
**Integration method:** `pip install aider-chat` (typical); run `aider` in repo; `--model <name>`.
**Compatibility:** Any LLM provider via API key; reads AGENTS.md/CONVENTIONS.md as read-only context.
**Dependencies:** Python; git; model API key.
**Availability:** Active, though a 2026-10 HF agents list noted slower activity (release page at v0.86.0, latest push reported 2026-05-22) — treat maintenance tempo as "slower but present."
**Maintenance:** Active (slower cadence).
**License:** Apache-2.0 (per HF agents list).
**Limitations:** Single-agent pair-programming model (not a multi-agent team); bring-your-own-key (no subscription riding); repo-map accuracy ~85% on dependency edges per one analysis.
**Related resources:** OpenCode, Cline, Cursor; Aider polyglot benchmark.
**Sources:** https://github.com/Aider-AI/aider; https://github.com/afloat16/ai-dev-steward/blob/HEAD/tools/stewardcheck/docs/research.md; https://betterstack.com/community/guides/ai/aider-ai-pair-programming/; https://blog.teliaz.com/2026/10/04/the-terminal-wars-comparing-the-major-cli-ai-coding-agents/; https://huggingface.co/blog/tegridydev/ai-agents-list-2026-frameworks-agentic-harnesses
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Partially verified

---

**Resource name:** SWE-agent
**Canonical identity:** SWE-agent/SWE-agent (Princeton NLP / Stanford)
**Category:** Harness engineering — autonomous software-engineering agent (research)
**Type:** Open-source (MIT), Python
**Official URL:** https://github.com/SWE-agent/SWE-agent · Docs: https://swe-agent.com
**Description:** Academic autonomous agent that takes a GitHub issue and tries to fix it using your LM of choice. Built on the **ACI (Agent-Computer Interface)** scaffold — minimal constraints, free-form tool use. NeurIPS 2024. **README carries an explicit supersession notice** (confirmed verbatim): "Most of our current development effort is on mini-SWE-agent, which has superseded SWE-agent… Our general recommendation is to use mini-SWE-agent instead of SWE-agent going forward." Also ships **EnIGMA** mode for offensive cybersecurity/CTF (SOTA on multiple cyber benchmarks) and a full **SWE-bench evaluation harness**.
**Contents inspected:** Full README.md + repository metadata via browser.open, 2026-10-10 (20,510 stars, MIT, 2,182 commits, config/ + sweagent/ + tools/ + trajectories/ layout).
**Actual capabilities:** GitHub-issue→autonomous-fix loop; ACI tool bundles installed into sandbox; YAML-configured behavior (`agent:`/`env:`/`problem_statement:`); persistent shell via SWE-ReX; observation capping; history compression; `--actions.open_pr` opens PR with diff; `run-batch` over SWE-bench subsets with `--num_workers`; EnIGMA CTF mode; trajectory recording.
**Usage domain:** Research on autonomous software engineering; benchmarking; reproducible agent experiments.
**Integration method:** `pip install sweagent`; CLI `sweagent run` / `sweagent run-batch`; `sweagent --resume`.
**Compatibility:** Model-agnostic (Claude, GPT, Gemini, open weights); Docker sandboxing.
**Dependencies:** Python; Docker; model API key.
**Availability:** Available; development effort moved to mini-SWE-agent.
**Maintenance:** Reduced (superseded).
**License:** MIT.
**Limitations:** Single-agent only; research-focused, not production-optimized; no daemon/autonomous issue processing; benchmark-specific tooling rather than a delivery platform.
**Related resources:** mini-SWE-agent, SWE-ReX, SWE-bench, SWE-smith, EnIGMA, OpenHands.
**Sources:** https://github.com/SWE-agent/SWE-agent (inspected 2026-10-10); https://github.com/freepeak/devagent/blob/HEAD/docs/research/2026-09-11-competitor-oss-agents.md; https://github.com/hu025/dotfiles/blob/HEAD/skills/swe-agent/SKILL.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** mini-SWE-agent
**Canonical identity:** mini-SWE-agent (SWE-agent team) · https://mini-swe-agent.com
**Category:** Harness engineering — minimal autonomous coding loop
**Type:** Open-source, Python
**Official URL:** https://mini-swe-agent.com
**Description:** Stripped-down successor to SWE-agent: originally a **~100-line ReAct loop** (bash-only, linear history, independent `subprocess.run` actions) that scored 65% on SWE-bench Verified (Claude 3.7 Sonnet) — now the **reference harness for the SWE-bench Verified "Bash Only" leaderboard view**. v2 current (Aug 2026; migration guide at mini-swe-agent.com/latest/advanced/v2_migration/). Sandbox-swappable (local/docker/podman/singularity/bubblewrap).
**Contents inspected:** Secondary: SWE-agent README supersession notice + news ("Mini-SWE-Agent achieves 65% on SWE-bench verified in 100 lines of python!", 2026-07-24); hu025 SKILL.md (v2 migration); tanavaggarwal research (bash-only loop, linear history); spcl/hpcagent-bench (mini-SWE-agent runner integration).
**Actual capabilities:** Minimal bash-tool loop; linear conversation history; pluggable environments; `uvx mini-swe-agent` quick start; serves as the neutral baseline scaffold for benchmark comparisons (Terminus lineage separate).
**Usage domain:** Baseline/reference harness; lightweight autonomous coding; benchmark scaffolding.
**Integration method:** `uvx mini-swe-agent` or `pip install mini-swe-agent`.
**Compatibility:** Model-agnostic; multiple sandbox backends.
**Dependencies:** Python; model API key.
**Availability:** Active (v2, Aug 2026).
**Maintenance:** Active (SWE-agent team's current focus).
**License:** Not verified in this pass.
**Limitations:** Minimal by design — no multi-agent, no memory system, no delivery pipeline.
**Related resources:** SWE-agent, SWE-ReX, SWE-bench, Terminal-Bench (Terminus scaffold).
**Sources:** https://mini-swe-agent.com/latest/; https://github.com/SWE-agent/SWE-agent (inspected 2026-10-10); https://github.com/hu025/dotfiles/blob/HEAD/skills/swe-agent/SKILL.md; https://github.com/tanavaggarwal/shipkit.ai/blob/HEAD/docs/research/04-autonomous-dev-test-harness.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** SWE-ReX
**Canonical identity:** SWE-ReX (SWE-agent team)
**Category:** Harness engineering — agent sandbox runtime
**Type:** Open-source runtime
**Official URL:** Not verified in this pass (referenced from SWE-agent README as sibling project)
**Description:** Separate runtime into which SWE-agent v1.0+ moved **all sandboxing** (deployment/execution split). Backends: Local, Docker, Modal, Fargate. Features sentinel-based shell completion detection (`###SWE-REX-COMPLETE-<id>###`).
**Contents inspected:** Secondary only: freepeak/devagent research (2026-09-11).
**Actual capabilities:** Persistent shell sessions; multi-backend deployment; completion sentinel protocol.
**Usage domain:** Sandboxed execution layer for SWE-agent and compatible harnesses.
**Integration method:** Consumed via SWE-agent config.
**Compatibility:** Local/Docker/Modal/Fargate.
**Dependencies:** Not verified.
**Availability:** Active per secondary reports.
**Maintenance:** Active (SWE-agent team).
**License:** Not verified.
**Limitations:** Runtime only — not an agent.
**Related resources:** SWE-agent, mini-SWE-agent.
**Sources:** https://github.com/freepeak/devagent/blob/HEAD/docs/research/2026-09-11-competitor-oss-agents.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** OpenHands (formerly OpenDevin)
**Canonical identity:** OpenHands/OpenHands (All Hands AI)
**Category:** Harness engineering — open autonomous software-development platform
**Type:** Open-source platform (Apache-2.0 per secondary), Python SDK + CLI + cloud
**Official URL:** https://github.com/OpenHands/OpenHands · Docs: https://docs.openhands.dev
**Description:** Open platform for AI coding agents ("the closest open-source Devin equivalent" per one analysis): autonomous CLI/GUI agent with MCP-first tool dispatch, plan-first loop, any-LLM support; sandboxed cloud VM with browser, terminal, file editing; GitHub integration (issues→PRs); long-horizon planning; evaluation harness with 15+ benchmarks; Python SDK for composable agent definitions (planning, context compression, security analysis, agent-computer interfaces; critic, stuck-detector, convo-goal guides); scales to 1000s of agents; openhands-resolver for automated issue resolution; budgets for cloud orgs.
**Contents inspected:** Secondary: sethdford market research (188+ contributors, 2100+ contributions, MIT); freepeak devagent (docs.openhands.dev sources, SDK paper arXiv:2511.03690, V0 paper arXiv:2407.16741); tanavaggarwal research; czyarl notices (mixed license: MIT for OSS portions, separate license for `enterprise/`).
**Actual capabilities:** Full agent platform: CLI + SDK + cloud; sandboxed browser/terminal/file tools; MCP-first dispatch; planning + context compression; critic/stuck-detection; evaluation harness (15+ benchmarks); session metrics; org budgets; resolver for GitHub issues.
**Usage domain:** Self-hosted autonomous coding agents; research; teams wanting Devin-like capability without proprietary lock-in.
**Integration method:** Docker-based local setup; `openhands serve --mount-cwd`; cloud hosted; Python SDK.
**Compatibility:** Model-agnostic (Claude, GPT, local LLMs); MCP.
**Dependencies:** Docker; model API keys.
**Availability:** Active.
**Maintenance:** Active (All Hands AI; university partnerships).
**License:** Mixed — MIT for open-source portions; separate license for `enterprise/` directory.
**Limitations:** Designed for single agents at scale — lacks multi-agent team orchestration; no daemon-driven autonomous issue processing; no persistent memory system; limited production deployment evidence (per one analysis).
**Related resources:** SWE-agent, mini-SWE-agent, Devin (proprietary analogue), Cline, Goose.
**Sources:** https://github.com/OpenHands/OpenHands; https://github.com/freepeak/devagent/blob/HEAD/docs/research/2026-09-11-competitor-oss-agents.md; https://github.com/sethdford/shipwright/blob/HEAD/docs/strategy/01-market-research.md; https://github.com/czyarl/devs_gen_code/blob/HEAD/THIRD_PARTY_NOTICES.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** EnIGMA
**Canonical identity:** EnIGMA (SWE-agent team) · https://enigma-agent.com
**Category:** Harness engineering — offensive-cybersecurity agent mode
**Type:** Open-source (part of SWE-agent project)
**Official URL:** https://enigma-agent.com
**Description:** SWE-agent mode for solving offensive cybersecurity (capture-the-flag) challenges. Paper: arXiv:2409.16165 (ICML 2025). Achieves SOTA on multiple cybersecurity benchmarks (incl. 13.5% on NYU CTF per secondary). README advises using SWE-agent 0.7 while EnIGMA is updated for 1.0.
**Contents inspected:** SWE-agent README section (inspected 2026-10-10); secondary citation record.
**Actual capabilities:** Interactive CTF-solving agent; summarizer and interactive commands.
**Usage domain:** Cybersecurity research/benchmarking.
**Integration method:** Via SWE-agent 0.7.
**Compatibility:** Model-agnostic.
**Dependencies:** Per SWE-agent.
**Availability:** Available; version-pinned guidance.
**Maintenance:** Maintained by SWE-agent team.
**License:** MIT (inherits SWE-agent).
**Limitations:** Offensive-security scope — dual-use considerations; version lag (0.7 recommended).
**Related resources:** SWE-agent, SWE-bench.
**Sources:** https://github.com/SWE-agent/SWE-agent (inspected 2026-10-10); https://arxiv.org/abs/2409.16165
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

### 10.2 Specification-driven development (SDD) frameworks

---

**Resource name:** GitHub Spec Kit
**Canonical identity:** github/spec-kit (GitHub)
**Category:** Harness engineering — spec-driven development toolkit
**Type:** Open-source toolkit (Python CLI + agent skills), MIT
**Official URL:** https://github.com/github/spec-kit
**Description:** GitHub's official toolkit for spec-driven development: "Build with a spec, fix a bug, or assess an idea — with your coding agent." Philosophy: intent is the source of truth; specifications are executable; code is last-mile output. Three independent entry processes: **SDD** (constitution once per project → specify → plan → tasks → implement → converge; repeat implement→converge until "Converged"), **bug fixing** (assess → fix → test; verdicts: verified/partial/failed), **idea assessment** (intake → research → define → shape → decide → go/needs-clarification/kill). Extensible via extensions, presets, workflows, bundles, community catalogs. ~140,590 stars at inspection; 230 releases; created 2025-08-21; v1.1.0 Sept 2026 (workflow extensibility, catalog safety, version pinning). 30+ supported AI coding agents.
**Contents inspected:** Full README.md + repository metadata via browser.open, 2026-10-10 (root: bundles/, extensions/, presets/, workflows/, templates/, scripts/, src/specify_cli/, spec-driven.md, AGENTS.md). Secondary: lvndrpup ADR (verified real-install corrections: hyphenated `/speckit-*` skill names, no CLAUDE.md sync, no branch creation by default); uvik.net SDD benchmark; juanklagos state-of-the-art doc.
**Actual capabilities:** `specify init` project scaffolding; `/speckit-constitution|specify|clarify|plan|tasks|analyze|implement|converge` agent skills; bug/assess extensions; pin-able catalog releases; local custom workflow step sources; brownfield flows; CI support.
**Usage domain:** Teams standardizing AI-assisted development on explicit specs across any coding agent.
**Integration method:** `uv tool install specify-cli`; `specify init my-project --integration <agent-key>`; invoke `/speckit-*` skills in agent chat.
**Compatibility:** 30+ AI coding agents (Copilot, Claude Code, Codex, Gemini CLI, Cursor, Amazon Q, etc.); Linux/macOS/Windows; Python 3.11+.
**Dependencies:** Python 3.11+, `uv`, a supported AI coding agent.
**Availability:** Active.
**Maintenance:** Very active (GitHub; rapid release cadence).
**License:** MIT.
**Limitations:** Specs add token cost and slow throwaway prototyping; verification of "done" is up to the agent unless paired with enforcement gates; version numbers move fast (treat as snapshot).
**Related resources:** OpenSpec, BMAD-METHOD, Kiro, cc-sdd, Agent OS, spec-workflow-mcp.
**Sources:** https://github.com/github/spec-kit (inspected 2026-10-10); https://github.com/lvndrpup/voice-trainer/blob/HEAD/docs/adr/0005-spec-driven-development-with-spec-kit.md; https://uvik.net/spec-driven-development-benchmark/; https://github.com/juanklagos/spec-driven-development-template/blob/HEAD/docs/en/50-sdd-state-of-the-art-2026.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** OpenSpec
**Canonical identity:** OpenSpec (Fission AI; community open source, MIT)
**Category:** Harness engineering — lightweight spec-driven change workflow
**Type:** Open-source CLI (Node) + slash commands
**Official URL:** Not verified in this pass (community project; referenced as framework-agnostic)
**Description:** Most lightweight SDD framework: enforces a strict **state machine — proposal → apply → archive**; no code is written until the spec has been proposed and approved. Unit of work is a change folder (`proposal.md`, delta specs, `design.md`, `tasks.md`); archiving merges deltas into `openspec/specs/` so specs stay current. Slash commands (`/opsx:propose`, `/opsx:apply`, `/opsx:archive`, plus explore/new/continue/verify/bulk-archive/onboard). "Stores" (beta) put the planning tree in a dedicated repo referenced via Git for cross-repo features.
**Contents inspected:** Secondary: danielvaughan/codex-blog SDD frameworks post; anton-abyzov/specweave comparison table; tomasher/prompting-blueprints tutorial (workflow loop, telemetry notes, model recommendations); juanklagos state-of-art (Thoughtworks Radar blip).
**Actual capabilities:** Propose/apply/archive state machine with human gate at propose; delta-spec merging on archive; onboarding generator for existing codebases; anonymous telemetry (opt-out via config/env); works in most coding agents (Claude Code `/opsx:`, Cursor, Copilot, Amazon Q, Codex `$openspec-propose`).
**Usage domain:** Brownfield iterative changes; developers wanting structure without a full platform.
**Integration method:** Node CLI + slash commands in the coding agent of choice; markdown in-repo.
**Compatibility:** Framework-agnostic (Claude Code, Cursor, Copilot, Amazon Q, Codex).
**Dependencies:** Node.js; a coding agent.
**Availability:** Active.
**Maintenance:** Active (Fission AI/community).
**License:** MIT.
**Limitations:** "Proof a task is done" is up to the agent; telemetry on by default (opt-out available); model choice matters (high-reasoning models recommended).
**Related resources:** GitHub Spec Kit, BMAD-METHOD, Kiro.
**Sources:** https://github.com/danielvaughan/codex-blog/blob/HEAD/_posts/2026-05-22-spec-driven-development-frameworks-codex-cli-spec-kit-kiro-openspec-patterns-best-practices.md; https://github.com/anton-abyzov/specweave/blob/HEAD/docs-site/docs/guides/spec-driven-tools-compared.md; https://github.com/tomasher/prompting-blueprints/blob/HEAD/05-tools/openspec-bmad-tutorial.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** BMAD-METHOD
**Canonical identity:** BMAD-METHOD (BMad Code; open source, MIT)
**Category:** Harness engineering — agile-team agent methodology
**Type:** Open-source methodology (agent personas + workflows), MIT
**Official URL:** Not verified in this pass
**Description:** Community methodology emphasizing a **"constitution"** (project-level rules) and **multi-agent role-play**: simulates an agile team (PM, architect, developer, tester/QA) as agent personas. Loop: Clarify → Plan → Build & Verify → Learn & Adjust, sized adaptively. v6 module ecosystem; ~48k–49k stars (June 2026 arXiv count / augmentcode). Roles map naturally onto subagent types (e.g., Codex CLI subagents; BMAD roles via separate AGENTS.md files).
**Contents inspected:** Secondary: danielvaughan/codex-blog (methodology tier, role mapping, codex.toml example); tomasher tutorial (delivery lifecycle loop); juanklagos (v6, ~49k stars); uvik.net benchmark (BMAD arm: PRD → architecture → story files; v6.x); augmentcode (21+ role-based agents, static docs-as-code).
**Actual capabilities:** Role-based agent personas; adaptive planning depth (quick flow → full PRD/architecture/stories); QA agent review; constitution-based governance; story-status tracking.
**Usage domain:** Framework-heavy enterprise planning; teams wanting agile-ceremony simulation in agent workflows.
**Integration method:** Persona/workflow files consumed by coding agents (Claude Code, Codex CLI, etc.); per-role AGENTS.md.
**Compatibility:** Most coding agents.
**Dependencies:** A coding agent; markdown workflow files.
**Availability:** Active (v6.x).
**Maintenance:** Active (community).
**License:** MIT.
**Limitations:** Heaviest ceremony of the SDD options; static docs-as-code specs; quality depends on role-prompt quality.
**Related resources:** GitHub Spec Kit, OpenSpec, Kiro, cc-sdd.
**Sources:** https://github.com/danielvaughan/codex-blog/blob/HEAD/_posts/2026-05-22-spec-driven-development-frameworks-codex-cli-spec-kit-kiro-openspec-patterns-best-practices.md; https://github.com/tomasher/prompting-blueprints/blob/HEAD/05-tools/openspec-bmad-tutorial.md; https://uvik.net/spec-driven-development-benchmark/; https://www.augmentcode.com/tools/best-spec-driven-development-tools
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** Kiro
**Canonical identity:** Kiro (Amazon Web Services)
**Category:** Harness engineering — agentic IDE with built-in spec workflow
**Type:** Commercial IDE (VS Code base) + CLI, credit-based plans
**Official URL:** Not verified in this pass (AWS product)
**Description:** AWS's agentic IDE (GA since Nov 2025; **replaced Amazon Q Developer**) with spec-driven development built in. Spec format: `requirements.md` in **EARS notation** (+ `bugfix.md` for bugs), `design.md`, `tasks.md` under `.kiro/specs/`; steering files for persistent project context; **property-based testing to verify code against spec**; agent hooks. Free tier: 50 credits/month.
**Contents inspected:** Secondary: uvik.net SDD benchmark (Kiro arm ran in its own IDE, claude-sonnet-5, bugfix vs feature spec tracks); juanklagos state-of-art (GA Nov 2025, replaces Q Developer); augmentcode comparison (static EARS specs, single-agent + hooks orchestration, AWS-native greenfield best-fit); specweave comparison table.
**Actual capabilities:** Spec workflow (requirements/design/tasks); EARS-notation requirements; steering files; spec hooks; property-based test verification; agent mode in IDE and CLI.
**Usage domain:** AWS-native greenfield projects; teams wanting spec workflow inside the IDE.
**Integration method:** Kiro IDE / CLI; credit-based usage.
**Compatibility:** AWS ecosystem; model selectable (Auto router or manual).
**Dependencies:** Kiro app; AWS account/credits.
**Availability:** Active (GA).
**Maintenance:** Active (AWS).
**License:** Commercial.
**Limitations:** Single-agent + hooks (not multi-agent); AWS gravity; credit costs; specs are static (not living).
**Related resources:** GitHub Spec Kit, OpenSpec, BMAD-METHOD, Amazon Q Developer (predecessor).
**Sources:** https://uvik.net/spec-driven-development-benchmark/; https://github.com/juanklagos/spec-driven-development-template/blob/HEAD/docs/en/50-sdd-state-of-the-art-2026.md; https://www.augmentcode.com/tools/best-spec-driven-development-tools; https://github.com/anton-abyzov/specweave/blob/HEAD/docs-site/docs/guides/spec-driven-tools-compared.md
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** cc-sdd (Claude Code SDD Skills)
**Canonical identity:** cc-sdd (community)
**Category:** Harness engineering — SDD slash-command skills
**Type:** Community skill set (slash commands)
**Official URL:** Not verified in this pass
**Description:** Set of slash commands for Claude Code implementing the SDD workflow: `/sdd:specify`, `/sdd:plan`, `/sdd:clarify`, `/sdd:implement`. Patterns transfer to other CLIs (mapped to Spec Kit skills or custom skills).
**Contents inspected:** Secondary only (danielvaughan/codex-blog command mapping table).
**Actual capabilities:** SDD phase commands for Claude Code.
**Usage domain:** Claude Code users wanting SDD without a full toolkit.
**Integration method:** Slash commands in Claude Code.
**Compatibility:** Claude Code (patterns portable).
**Dependencies:** Claude Code.
**Availability:** Not verified.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced; thinnest of the SDD options.
**Related resources:** GitHub Spec Kit, OpenSpec, BMAD-METHOD.
**Sources:** https://github.com/danielvaughan/codex-blog/blob/HEAD/_posts/2026-05-22-spec-driven-development-frameworks-codex-cli-spec-kit-kiro-openspec-patterns-best-practices.md
**Verification date:** 2026-10-10
**Confidence:** Low-Medium
**Verification label:** Partially verified

---

**Resource name:** SpecWeave
**Canonical identity:** SpecWeave (anton-abyzov/specweave)
**Category:** Harness engineering — SDD with evidence ledger
**Type:** Open-source (Node CLI + skills)
**Official URL:** https://github.com/anton-abyzov/specweave
**Description:** Newer SDD entrant differentiating on **evidence-based completion**: one `spec.md` + append-only `ledger.jsonl`; `task done --run "<test>"` stores test output and a failing command is refused as proof. `specweave handoff` / `pickup` for switching tool/account mid-task. Unit of work: an increment.
**Contents inspected:** Secondary only (its own comparison docs-site page: spec-driven-tools-compared.md).
**Actual capabilities:** Evidence ledger; handoff/pickup; works with any agent reading AGENTS.md or running a shell.
**Usage domain:** Teams wanting proof-of-done stronger than checkboxes.
**Integration method:** Node CLI + skills.
**Compatibility:** Any agent reading AGENTS.md / shell-capable.
**Dependencies:** Not verified.
**Availability:** Active per its docs (3.0).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced (project's own comparison); newest/least battle-tested of the set.
**Related resources:** GitHub Spec Kit, OpenSpec.
**Sources:** https://github.com/anton-abyzov/specweave/blob/HEAD/docs-site/docs/guides/spec-driven-tools-compared.md
**Verification date:** 2026-10-10
**Confidence:** Low
**Verification label:** Unresolved

---

**Resource name:** Agent OS
**Canonical identity:** Agent OS (community)
**Category:** Harness engineering — standards-injection for brownfield
**Type:** Community methodology/tooling
**Official URL:** Not verified in this pass
**Description:** "Standards injection" approach: discovers codebase patterns, documents them as standards, and injects them into plan mode. v3; noted as strong for brownfield work.
**Contents inspected:** Secondary only (juanklagos state-of-art table).
**Actual capabilities:** Pattern discovery → standards docs → plan-mode injection.
**Usage domain:** Brownfield codebases needing consistent agent behavior.
**Integration method:** Not verified.
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** v3 per secondary.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced; details thin.
**Related resources:** GitHub Spec Kit, OpenSpec.
**Sources:** https://github.com/juanklagos/spec-driven-development-template/blob/HEAD/docs/en/50-sdd-state-of-the-art-2026.md
**Verification date:** 2026-10-10
**Confidence:** Low
**Verification label:** Partially verified

---

**Resource name:** spec-workflow-mcp
**Canonical identity:** spec-workflow-mcp (community)
**Category:** Harness engineering — MCP-server spec workflow
**Type:** Open-source MCP server
**Official URL:** Not verified in this pass
**Description:** MCP server implementing a spec workflow plus a real-time web dashboard for any MCP client. Described as the active successor of `claude-code-spec-workflow`.
**Contents inspected:** Secondary only (juanklagos state-of-art table).
**Actual capabilities:** Spec workflow over MCP; realtime dashboard.
**Usage domain:** MCP-client users wanting spec workflow + visibility.
**Integration method:** MCP server config.
**Compatibility:** Any MCP client.
**Dependencies:** MCP client.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced.
**Related resources:** GitHub Spec Kit, MCP.
**Sources:** https://github.com/juanklagos/spec-driven-development-template/blob/HEAD/docs/en/50-sdd-state-of-the-art-2026.md
**Verification date:** 2026-10-10
**Confidence:** Low
**Verification label:** Partially verified

---

**Resource name:** Tessl
**Canonical identity:** Tessl (company)
**Category:** Harness engineering — spec-as-source framework (aspirational tier)
**Type:** Commercial (was closed beta)
**Official URL:** Not verified in this pass
**Description:** "Spec-as-source" vision: only the spec is edited; code is a compiled artifact. Had a Spec Registry (10k+ versioned library specs). **Framework never reached GA; company pivoted to agent skills** (per juanklagos, mid-2026).
**Contents inspected:** Secondary only.
**Actual capabilities (historical):** Versioned library spec registry.
**Usage domain:** Historical reference for the spec-as-source tier.
**Integration method:** Not applicable.
**Compatibility:** Not applicable.
**Dependencies:** Not applicable.
**Availability:** Pivoted; framework not GA.
**Maintenance:** None (as framework).
**License:** Not verified.
**Limitations:** Never shipped as a framework; do not evaluate as a current option.
**Related resources:** GitHub Spec Kit, OpenSpec.
**Sources:** https://github.com/juanklagos/spec-driven-development-template/blob/HEAD/docs/en/50-sdd-state-of-the-art-2026.md; https://uvik.net/spec-driven-development-benchmark/
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Historical

---

**Cross-reference — SWE-smith:** Synthetic task generator from the SWE-agent team (generates bug-injection tasks for training/evaluation). Referenced in SWE-agent README sibling-project strip. Not researched in depth. Label: Partially verified.

---

### 10.3 Evaluation benchmarks for agents

---

**Resource name:** SWE-bench family (SWE-bench / Verified / Pro / Multilingual / Multimodal / Live)
**Canonical identity:** SWE-bench/SWE-bench (SWE-bench team) · https://www.swebench.com
**Category:** Evaluation — software-engineering agent benchmarks
**Type:** Open benchmark suites + leaderboards
**Official URL:** https://github.com/SWE-bench/SWE-bench · https://www.swebench.com
**Description:** The de facto standard for coding-agent evaluation: real GitHub issues → agent produces patch → patch must pass the issue's held-out test suite. Tiers: **SWE-bench Verified** (500 Python tasks; now considered contaminated — "use as direction only"); **SWE-bench Pro** (1,865 tasks, 4 languages; official standardized public board at labs.scale.com; scores vary wildly by harness — 23–64%); **SWE-bench Multilingual**; **SWE-bench Multimodal** (GUIRepair + o3 ~35.98% official board); **SWE-bench Live** (continuously refreshed tasks to fight contamination). Leaderboards: swebench.com, Vals (Verified), Scale (Pro public).
**Contents inspected:** Secondary: gray311/awesome-agentic-benchmarks (SOTA table: Verified — Claude Opus 5 97.0%, GPT-5.6 Sol Max 96.2% (Vals, 2026-08-19); Pro public — Muse Spark 1.1 + mini-SWE-agent 61.5%); marktechpost benchmark guide (scaffolding effect ±17 problems; contamination caveats); allanschramm discovery doc; mini-harness BENCHMARKS.md (methodology notes).
**Actual capabilities:** Task datasets with executable verifiers; public + vendor-reported leaderboards; harness-aware score reporting (Pro).
**Usage domain:** Comparing coding agents/harnesses; regression-tracking agent quality.
**Integration method:** Dataset download; harness-specific runners (SWE-agent `run-batch`, mini-SWE-agent, Harbor).
**Compatibility:** Python (Verified); 4 languages (Pro).
**Dependencies:** Containerized eval environments.
**Availability:** Active; Live tier continuously updated.
**Maintenance:** Active.
**License:** Not verified.
**Limitations:** Verified is contaminated (training overlap); scores are harness-dependent (same model ±large gaps); self-reported vendor numbers not comparable to official boards.
**Related resources:** SWE-agent, mini-SWE-agent, SWE-rebench V2, Multi-SWE-bench, Terminal-Bench.
**Sources:** https://github.com/SWE-bench/SWE-bench; https://www.swebench.com/; https://github.com/gray311/awesome-agentic-benchmarks; https://www.marktechpost.com/2026/05/15/best-ai-agents-for-software-development-ranked-a-benchmark-driven-look-at-the-current-field/; https://labs.scale.com/leaderboard/swe_bench_pro_public
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** SWE-rebench V2
**Canonical identity:** SWE-rebench V2 · arXiv:2602.23866
**Category:** Evaluation — contamination-resistant SWE benchmark
**Type:** Open benchmark (paper + dataset)
**Official URL:** https://arxiv.org/abs/2602.23866 (paper; code URL not verified)
**Description:** Direct fix for SWE-bench Verified's training-overlap problem: new tasks, language-agnostic, anti-contamination **by construction** (March 2026).
**Contents inspected:** Secondary only (allanschramm discovery doc).
**Actual capabilities:** Fresh task set; bash-based agent interface.
**Usage domain:** Contamination-free coding-agent ranking.
**Integration method:** Not verified.
**Compatibility:** Language-agnostic.
**Dependencies:** Not verified.
**Availability:** Released (Mar 2026).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced; newest of the SWE-bench alternatives.
**Related resources:** SWE-bench, SWE-bench Live.
**Sources:** https://arxiv.org/abs/2602.23866; https://github.com/allanschramm/local-model-autotuning/blob/HEAD/docs/discovery/real-swe-benchmarks.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** Multi-SWE-bench
**Canonical identity:** multi-swe-bench/multi-swe-bench
**Category:** Evaluation — multilingual SWE benchmark
**Type:** Open benchmark (paper + code)
**Official URL:** https://github.com/multi-swe-bench/multi-swe-bench · Paper: https://arxiv.org/abs/2504.02605
**Description:** Multilingual extension of SWE-bench across languages; paper frontier is per-language (MopenHands + Claude 3.7 Sonnet led most reported language tracks).
**Contents inspected:** Secondary (gray311 table; 359 stars noted).
**Actual capabilities:** Per-language task tracks with executable tests.
**Usage domain:** Non-Python coding-agent evaluation.
**Integration method:** Repo runners.
**Compatibility:** Multiple languages.
**Dependencies:** Not verified.
**Availability:** Active.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** No official aggregate scoreboard; per-language reporting only.
**Related resources:** SWE-bench, SWE-bench Multilingual.
**Sources:** https://github.com/multi-swe-bench/multi-swe-bench; https://arxiv.org/abs/2504.02605; https://github.com/gray311/awesome-agentic-benchmarks
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Verified

---

**Resource name:** Terminal-Bench (and Terminus scaffold / Harbor runner)
**Canonical identity:** harbor-framework/terminal-bench · https://www.tbench.ai · Leaderboard: https://www.frontierbench.ai/
**Category:** Evaluation — terminal/operational agent benchmark
**Type:** Open benchmark (continuous/live)
**Official URL:** https://github.com/harbor-framework/terminal-bench
**Description:** Measures **operational reliability across terminal tasks** (not just code patches): natural-language instruction → complete task using bash in an isolated terminal → task-specific executable tests (pytest) via the **Harbor** runner. v2.0: 89 tasks; v3.0 reported. 2026 leaders: GPT-5.5 73.2% direct / ForgeCode combos 81.8% (v2.0); v3.0 official board: Opus 5 Max + mini-SWE-agent 42.7%. 32,155 total trials across 6 agent scaffolds (Terminus 2 neutral scaffold, Claude Code, Codex CLI, OpenHands, Mini-SWE-Agent, ForgeCode/TongAgents/SageAgent) × 16 models. Easy-vs-hard gap ~49 points — uniform across models. Harness matters: same model scores 57.5% vs 64.7% depending on setup.
**Contents inspected:** Secondary: gray311 docs (continuous/live status, Modal-hosted official execution, task-set tags); explainx.ai 2.0 deep-dive (trial counts, difficulty gap); marktechpost (scaffolding effects); mini-harness BENCHMARKS.md (Harbor 0.20.0 run methodology, dataset sha256).
**Actual capabilities:** Isolated terminal environments; executable task tests; tagged releases with repeated oracle runs; hosted official execution (Modal).
**Usage domain:** Evaluating generalist terminal agents (DevOps, ML ops, sysadmin, data science).
**Integration method:** Harbor runner; task-set tags; agent scaffold adapters.
**Compatibility:** Bash/terminal environments; Docker/Modal.
**Dependencies:** Container runtime.
**Availability:** Active (continuous/live).
**Maintenance:** Active (Harbor framework team).
**License:** Not verified.
**Limitations:** Scores must be attached to task-set tag + scaffold + resource policy to be comparable; vendor self-reports vary.
**Related resources:** TerminalWorld, TUA-Bench, SWE-bench, mini-SWE-agent.
**Sources:** https://github.com/harbor-framework/terminal-bench; https://www.frontierbench.ai/; https://github.com/gray311/awesome-agentic-benchmarks/blob/HEAD/docs/2026-frontier-benchmarks.md; https://explainx.ai/blog/terminal-bench-2-0-ai-agent-benchmark-evaluation
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** TerminalWorld
**Canonical identity:** TerminalWorld · https://terminalworld.ai/
**Category:** Evaluation — reproduced real-world terminal environments
**Type:** Benchmark + leaderboard
**Official URL:** https://terminalworld.ai/
**Description:** 5,035 reproduced real-world software environments, 1,530 with test suites, 200-task human-verified subset; executable tests score completion. 2026-05 leaderboard (200-task): Claude Opus 4.7 + Terminus-2 62.5%, Kimi K2.6 57.5%, GLM 5.1 57.0%.
**Contents inspected:** Secondary only (gray311 frontier-benchmarks doc).
**Actual capabilities:** Reproduced environments; human-verified task subset.
**Usage domain:** Realistic terminal-agent evaluation.
**Integration method:** Not verified.
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** Live (board last updated 2026-05-21 per secondary).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced; board freshness unclear.
**Related resources:** Terminal-Bench, TUA-Bench.
**Sources:** https://terminalworld.ai/; https://github.com/gray311/awesome-agentic-benchmarks/blob/HEAD/docs/2026-frontier-benchmarks.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** TUA-Bench
**Canonical identity:** facebookresearch/TUA-Bench · https://tuabench.ai/
**Category:** Evaluation — terminal/computer-use workflows
**Type:** Open benchmark (Meta/Facebook Research)
**Official URL:** https://github.com/facebookresearch/TUA-Bench · https://tuabench.ai/
**Description:** 120 terminal workflows in five families (document editing, email, live web, scientific/engineering work); deterministic setup; execution-based scoring in general computer-use environments. Released 2026-06. Strongest cited config: Claude Code + Claude Opus 4.8 Max 65.8%.
**Contents inspected:** Secondary only (gray311).
**Actual capabilities:** Deterministic workflow environments; execution scoring.
**Usage domain:** Computer-use / general terminal workflow agents.
**Integration method:** Not verified.
**Compatibility:** Not verified.
**Dependencies:** Not verified.
**Availability:** Released (2026-06).
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** Single-sourced in this pass.
**Related resources:** Terminal-Bench, TerminalWorld.
**Sources:** https://github.com/facebookresearch/TUA-Bench; https://tuabench.ai/; https://github.com/gray311/awesome-agentic-benchmarks/blob/HEAD/docs/2026-frontier-benchmarks.md
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** GAIA
**Canonical identity:** GAIA (466 tasks)
**Category:** Evaluation — general assistant reasoning benchmark
**Type:** Open benchmark
**Official URL:** Not verified in this pass
**Description:** 466 multi-step reasoning QA tasks (e.g., "find country's GDP and convert currency"); answers scored against human-annotated ground truth + LLM judge for paraphrasing. Tests general-assistant reasoning ("can you figure out the answer?"), not action execution. 2026 leaders cited: Claude Mythos Preview 52.3%, GPT-5.4 Pro 50.5%.
**Contents inspected:** Secondary only (explainx.ai comparison section).
**Actual capabilities:** Multi-step QA tasks with human ground truth.
**Usage domain:** General agent reasoning capability.
**Integration method:** Not verified.
**Compatibility:** Not applicable.
**Dependencies:** Not applicable.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** Not verified.
**Limitations:** QA-natured — does not test tool-use/action execution; single-sourced here.
**Related resources:** Terminal-Bench (contrast: action vs reasoning).
**Sources:** https://explainx.ai/blog/terminal-bench-2-0-ai-agent-benchmark-evaluation
**Verification date:** 2026-10-10
**Confidence:** Low-Medium
**Verification label:** Partially verified

---

**Resource name:** awesome-agentic-benchmarks (gray311)
**Canonical identity:** gray311/awesome-agentic-benchmarks
**Category:** Evaluation — curated benchmark index
**Type:** Curated list (CC BY 4.0 data per author)
**Official URL:** https://github.com/gray311/awesome-agentic-benchmarks
**Description:** Curated, evidence-backed map of benchmarks for autonomous agents, AI R&D, and recursive self-improvement — coding/terminal/computer/mobile agents plus 2026 frontier benchmarks doc. Used as a secondary aggregator in this pass; tracks SOTA with dates and primary links.
**Contents inspected:** Search-result excerpts of README tables and docs/2026-frontier-benchmarks.md.
**Actual capabilities:** Indexing/curation only.
**Usage domain:** Benchmark discovery.
**Integration method:** Not applicable.
**Compatibility:** Not applicable.
**Dependencies:** Not applicable.
**Availability:** Active (updated ~44 days before 2026-10-10).
**Maintenance:** Active.
**License:** CC BY 4.0 (data tables, per author).
**Limitations:** Aggregator — verify claims against primary benchmark sources.
**Related resources:** All benchmarks above.
**Sources:** https://github.com/gray311/awesome-agentic-benchmarks
**Verification date:** 2026-10-10
**Confidence:** Medium-High
**Verification label:** Verified

---

### 10.4 Agent telemetry, cost tracking, and observability

---

**Resource name:** Langfuse
**Canonical identity:** Langfuse · https://langfuse.com
**Category:** Harness engineering — LLM/agent observability platform
**Type:** Open-source platform (MIT core; SCIM/audit/retention modules separately licensed) + cloud
**Official URL:** https://langfuse.com
**Description:** Leading open-source AI engineering platform for tracing, evaluating, monitoring, and improving LLM apps and agents. Production-grade hierarchical tracing (LLM calls, tool use, retrieval, sessions, user metadata); OpenTelemetry-native (SDK v4 on OTel, OTLP over HTTP); evaluations & experiments (LLM-as-judge, custom scorers, human annotation, datasets, side-by-side); prompt management (versioned, one-click deploy, rollbacks, playground); analytics & cost control (latency/token/spend/quality dashboards, alerts); 100+ integrations (LangChain, LlamaIndex, CrewAI, OpenAI, Anthropic); self-hostable or cloud; billions of observations/month. Cost caveat (dev.to, Oct 2026): only `generation` and `embedding` observations track cost; tool/agent spans unpriced by design; overlapping usage buckets can double-count.
**Contents inspected:** Secondary: vdf.ai observability comparison (verified Oct 2026 table); Langfuse review video description; dev.to cost-dashboard critique; agent-kernel integration guide.
**Actual capabilities:** Tracing, evals, prompt management, cost/latency analytics, PII masking in SDK, self-hosting.
**Usage domain:** Production agent observability, evals, cost control.
**Integration method:** SDKs; OTLP; 100+ framework integrations.
**Compatibility:** OpenTelemetry-native; LangChain, LlamaIndex, CrewAI, OpenAI, Anthropic.
**Dependencies:** Self-hosted infra or cloud account.
**Availability:** Active.
**Maintenance:** Active.
**License:** MIT core; some enterprise modules separately licensed.
**Limitations:** Tool/agent spans carry no cost by design; double-counting risk on overlapping usage buckets; enterprise modules not MIT.
**Related resources:** LangSmith, Arize Phoenix, Helicone, OpenLLMetry, AgentOps.
**Sources:** https://langfuse.com; https://vdf.ai/blog/llm-observability-tools/; https://dev.to/theagentloop/your-cost-dashboard-cant-tell-you-which-agent-ran-up-the-bill-4eej; https://dev.to/agent-kernel/production-grade-observability-agent-kernel-integrates-langfuse-and-openllmetry-3ab9
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** AgentOps
**Canonical identity:** AgentOps
**Category:** Harness engineering — agent monitoring/replay/cost tracking
**Type:** Open-source (MIT per secondary) + commercial
**Official URL:** Not verified in this pass
**Description:** Agent monitoring with session replay, cost tracking, and framework integrations; time-travel debugging; multi-agent workflow visualization; collaboration tracking and cost optimization. Positioned as agent-specific complement to Langfuse. HF agents list (Oct 2026) notes latest push 2026-06-25 and advises checking SDK-version compatibility before adopting.
**Contents inspected:** Secondary: webpronews comparison; cmu-lib SKILL.md (observability stack layering); huggingface.co agents list maintenance caveat.
**Actual capabilities:** Session replay; cost tracking; framework integrations; time-travel debugging; multi-agent visualization.
**Usage domain:** Agent-specific monitoring/debugging.
**Integration method:** SDK integration per framework.
**Compatibility:** Framework-agnostic integrations (incl. OpenAI Agents SDK tracing).
**Dependencies:** Not verified.
**Availability:** Active with maintenance-tempo caveat (June 2026 push).
**Maintenance:** Uncertain tempo — verify compatibility with current SDK versions.
**License:** MIT (per secondary).
**Limitations:** Slower recent activity; verify before adopting.
**Related resources:** Langfuse, LangSmith, Braintrust.
**Sources:** https://www.webpronews.com/inside-ai-agent-watchdogs-langfuse-agentops-and-the-race-for-unbreakable-autonomy/; https://github.com/cmu-lib/ai_evaluation_framework_tool/blob/HEAD/agent-orchestration/agent-observability/SKILL.md; https://huggingface.co/blog/tegridydev/ai-agents-list-2026-frameworks-agentic-harnesses
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** LangSmith
**Canonical identity:** LangSmith (LangChain Inc.)
**Category:** Harness engineering — agent observability + deployment platform
**Type:** Commercial platform (enterprise add-on for self-hosting; free tier)
**Official URL:** https://www.langchain.com/langsmith (docs: https://docs.langchain.com)
**Description:** LangChain's observability/evals/deployment platform: debugging with run replays and trajectory visualization, evaluators, production monitoring; LangSmith Deployment hosts long-running stateful LangGraph workflows with visual prototyping (LangSmith Studio). Near-zero overhead; natively integrated with LangChain/LangGraph. OTLP ingest + SDK export; client-side PII hiding/anonymizers.
**Contents inspected:** LangGraph README ecosystem section (inspected 2026-10-10); vdf.ai comparison table.
**Actual capabilities:** Tracing/visualization, evals, deployment/scaling of stateful agents, prompt hub, Studio prototyping.
**Usage domain:** LangChain/LangGraph production stacks.
**Integration method:** LangChain/LangGraph native; SDKs; OTLP.
**Compatibility:** LangChain ecosystem first; OTLP ingest for others.
**Dependencies:** LangChain account (free tier → $39/seat/mo per secondary).
**Availability:** Active.
**Maintenance:** Active.
**License:** Commercial (enterprise add-on for self-host).
**Limitations:** LangChain-centric; commercial for full self-host.
**Related resources:** LangGraph, LangChain, Langfuse.
**Sources:** https://github.com/langchain-ai/langgraph (inspected 2026-10-10); https://vdf.ai/blog/llm-observability-tools/; https://tech-insider.org/langchain-vs-llamaindex-vs-crewai-2026/
**Verification date:** 2026-10-10
**Confidence:** High
**Verification label:** Verified

---

**Resource name:** Arize Phoenix
**Canonical identity:** Arize Phoenix (Arize AI)
**Category:** Harness engineering — open-source LLM observability
**Type:** Open-source (Elastic License 2.0), self-hostable (Docker/K8s)
**Official URL:** Not verified in this pass
**Description:** Open-source observability built on OpenTelemetry + OpenInference: tracing, drift detection, LLM/code/human evaluators, built-in price table with custom prices, PII hide settings in instrumentation.
**Contents inspected:** Secondary only (vdf.ai comparison table, verified Oct 2026).
**Actual capabilities:** OTel-native tracing; evals; cost tracking via price tables.
**Usage domain:** Self-hosted LLM observability with evals.
**Integration method:** Docker/Kubernetes deployment; instrumentation SDKs.
**Compatibility:** OpenTelemetry/OpenInference ecosystem.
**Dependencies:** Container runtime.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** Elastic License 2.0 (not OSI open-source; source-available).
**Limitations:** ELv2 license restricts some commercial uses; single-sourced here.
**Related resources:** Langfuse, OpenLLMetry.
**Sources:** https://vdf.ai/blog/llm-observability-tools/
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** Helicone
**Canonical identity:** Helicone
**Category:** Harness engineering — AI gateway + observability
**Type:** Open-source (Apache-2.0), self-hostable (Docker/Helm) + SaaS
**Official URL:** Not verified in this pass
**Description:** Proxy-based AI gateway with OpenTelemetry support, caching (cost savings), evals, cost tracking, and headers to skip storing request bodies (PII control). Flat $25/month SaaS noted in secondary.
**Contents inspected:** Secondary only (vdf.ai table; webpronews).
**Actual capabilities:** Gateway proxying; caching; cost tracking; evals.
**Usage domain:** Cost control via caching + unified gateway observability.
**Integration method:** Proxy endpoint in front of model APIs; Docker/Helm self-host.
**Compatibility:** OpenTelemetry; model-API agnostic via proxy.
**Dependencies:** Gateway deployment.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** Apache-2.0.
**Limitations:** Proxy architecture adds a network hop; single-sourced here.
**Related resources:** Langfuse, LiteLLM proxy.
**Sources:** https://vdf.ai/blog/llm-observability-tools/; https://www.webpronews.com/inside-ai-agent-watchdogs-langfuse-agentops-and-the-race-for-unbreakable-autonomy/
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** OpenLLMetry (Traceloop)
**Canonical identity:** traceloop/openllmetry
**Category:** Harness engineering — OpenTelemetry instrumentation for LLMs
**Type:** Open-source (Apache-2.0) instrumentation
**Official URL:** Not verified in this pass
**Description:** Vendor-neutral OpenTelemetry instrumentation for LLM/agent frameworks — "instrumentation; send to any OTel backend." Native OTel; content captured by default (can be switched off). Used as the tracing layer under platforms like Agent Kernel.
**Contents inspected:** Secondary only (vdf.ai table; agent-kernel integration guide).
**Actual capabilities:** Framework instrumentation emitting OTel spans to any backend.
**Usage domain:** Bring-your-own-backend observability.
**Integration method:** SDK instrumentation packages.
**Compatibility:** Any OTel backend (Traceloop, Datadog, etc.).
**Dependencies:** OTel collector/backend.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** Apache-2.0.
**Limitations:** Instrumentation only — no UI/evals/cost tables of its own; content capture defaults need PII review.
**Related resources:** OpenTelemetry, Langfuse, Datadog.
**Sources:** https://vdf.ai/blog/llm-observability-tools/; https://dev.to/agent-kernel/production-grade-observability-agent-kernel-integrates-langfuse-and-openllmetry-3ab9
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

**Resource name:** W&B Weave (Weights & Biases)
**Canonical identity:** W&B Weave
**Category:** Harness engineering — agent evaluation/tracing
**Type:** Commercial (SDK Apache-2.0); multi-tenant/dedicated/self-managed
**Official URL:** Not verified in this pass
**Description:** Weights & Biases' agent layer: tracing with OTLP endpoint, LLM judges and custom scorers (e.g., HallucinationFreeScorer), multi-agent metrics; Presidio redaction in the Python SDK.
**Contents inspected:** Secondary only (vdf.ai table; webpronews).
**Actual capabilities:** Tracing, scorers/evals, multi-agent metrics, PII redaction.
**Usage domain:** Teams already on W&B extending into agents.
**Integration method:** Python SDK; OTLP endpoint.
**Compatibility:** OTLP; Python-first.
**Dependencies:** W&B account.
**Availability:** Active per secondary.
**Maintenance:** Not verified.
**License:** SDK Apache-2.0; platform commercial.
**Limitations:** Single-sourced here; platform commercial.
**Related resources:** Langfuse, Braintrust, Galileo.
**Sources:** https://vdf.ai/blog/llm-observability-tools/; https://www.webpronews.com/inside-ai-agent-watchdogs-langfuse-agentops-and-the-race-for-unbreakable-autonomy/
**Verification date:** 2026-10-10
**Confidence:** Medium
**Verification label:** Partially verified

---

## Coverage note

**Counts.** Total resources recorded: **57** (55 full Part-21-style records + 2 cross-references).
- Part 9 — Multi-agent frameworks: **16** (LangGraph, AutoGen, AG2, Microsoft Agent Framework, CrewAI, OpenAI Agents SDK, OpenAI Swarm, Google ADK, MetaGPT, AWS Strands Agents, PydanticAI, Smolagents, BeeAI Framework, Mastra, Hermes Agent, Meta Llama Stack).
- Part 9 — Protocols/standards: **8** (A2A, ACP/IBM, AG-UI, AGNTCY, AP2, ANP/W3C CG, Zed Agent Client Protocol, Commerce ACP) + 1 cross-reference (MCP).
- Part 10 — Harnesses/autonomous dev: **16** (Munder Difflin, Aider, SWE-agent, mini-SWE-agent, SWE-ReX, OpenHands, EnIGMA, Spec Kit, OpenSpec, BMAD-METHOD, Kiro, cc-sdd, SpecWeave, Agent OS, spec-workflow-mcp, Tessl) + 1 cross-reference (SWE-smith).
- Part 10 — Benchmarks: **8** (SWE-bench family, SWE-rebench V2, Multi-SWE-bench, Terminal-Bench, TerminalWorld, TUA-Bench, GAIA, awesome-agentic-benchmarks).
- Part 10 — Telemetry/cost tracking: **7** (Langfuse, AgentOps, LangSmith, Arize Phoenix, Helicone, OpenLLMetry, W&B Weave).

**Verification-label distribution:** Verified: 26 · Partially verified: 24 · Historical: 2 (OpenAI Swarm, Tessl) · Archived: 1 (IBM ACP) · Unresolved: 2 (Hermes Agent, SpecWeave) · Inaccessible: 0.

**Key gaps / more-work-warranted:**
1. **Primary-page inspection for ~19 Partially-verified items** — repo READMEs were captured only via search-result excerpts for CrewAI, OpenAI Agents SDK, Google ADK, Strands, PydanticAI, Smolagents, BeeAI, Mastra, Aider, OpenHands, OpenSpec, BMAD, Kiro, Terminal-Bench, and all telemetry tools. A follow-up pass opening each repo page would firm these up.
2. **AG2 canonical repo URL** — fork confirmed to exist and own the `autogen` PyPI name, but the GitHub org URL was not captured; needs one targeted lookup.
3. **Hermes Agent** — single-sourced with an implausible star claim; needs primary verification or removal.
4. **MetaGPT current state** — org migration (geekan → FoundationAgents) confirmed via third-party notices, but live repo activity not directly inspected; commercial MGX vs OSS split needs confirmation.
5. **ANP / W3C CG, AP2, Zed ACP, Commerce ACP** — protocol details thin; spec documents not opened.
6. **Not covered (out of scope or deferred):** commercial autonomous dev products (Devin, Google Jules, GitHub Copilot Coding Agent, Cursor Background Agents) — relevant to "background/scheduled agent infrastructure" but each needs product-page verification; `claude-agent-sdk` subagent architecture (likely belongs to a Claude-Code workstream); LlamaIndex Workflows; Temporal.io durable execution; e2b/Daytona sandboxes; SWE-bench-java / SWE-PolyBench; R2E / commit0; DevEval; OSWorld; τ-bench.
7. **Star counts** are snapshots from secondary sources at varying dates — do not treat as current; recorded as reported with dates where available.
8. No mockups, sample code, installations, or recommendations were produced — read-only research only, per the brief.

**Corrections preserved from prior work:** ngmeyer/council-review LIVE (not archived); KanakMalpani Loop-Engineering vs LoopBench separate; gsd-build/get-shit-done ARCHIVED (not recommended) vs open-gsd/gsd-core safe fork; ruvnet/ruflo (formerly Claude Flow); emilkowalski/skills; teng-lin/notebooklm-py unofficial; Forward-Future/loopy is a skill not an engine; walkinglabs/learn-harness-engineering template structure — none re-researched here; the OpenCode harness catalog was treated as authoritative and not duplicated.
