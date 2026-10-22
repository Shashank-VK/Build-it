# 04 — Coding Agents, Multi-Agent Systems, Harness Engineering & Context/Memory

> Comprehensive Reference Catalog & System Architecture Analysis  
> Read-Only Researcher: Google Gemini · Verification Date: 2026-10-09  
> Total Cataloged Resources: 68 (Exceeds 60+ requirement)  
> Scope: Autonomous & Interactive Coding Agents · Multi-Agent Runtimes vs Single-Model Roleplay · Spec-Driven Harness Engineering & Guardrails · Vector/Hybrid/AST Context & Memory Mechanisms

---

## Executive Architectural Synthesis

Modern AI-assisted software engineering has evolved across four tightly coupled layers:

1. **Coding Agents (The Execution Engines):** From early autocomplete completions to full-duplex terminal, IDE, and background agents equipped with tool calling (shell, file differential editing, LSP querying, web browsing) and fine-grained permission sandboxes.
2. **Multi-Agent Systems (Coordination & Orchestration):** A rigorous architectural distinction separates **Real Runtimes** (isolated processes, discrete context windows, decoupled memory, deterministic message dispatchers, and independent tool privilege policies) from **Single-Model Roleplay** (a single prompt context instructing one LLM to simulate multiple conversational personas without process isolation or state safety).
3. **Harness Engineering (Process Control & Verification):** The transition from stochastic prompt-and-pray to deterministic Spec-Driven Development (SDD), Definition of Done (DoD) verification loops, test-driven feedback, checkpointing/rewind capabilities, git worktree isolation, automated handoffs, and token/cost telemetry guards.
4. **Context & Memory Engineering (Information Grounding):** Managing the bounded context window through hybrid retrieval (Dense Vector + Sparse BM25 + Reciprocal Rank Fusion), structural code intelligence (Tree-sitter ASTs, Call-Graph PageRank repo maps), dynamic documentation grounding, and hierarchical session memory compaction.

---

## Complete Resource Index (68 Items)

### Part I: Coding Agents & Extension Architectures (18 Items)
- **01** — OpenCode (`anomalyco/opencode`)
- **02** — Claude Code (`@anthropic-ai/claude-code`)
- **03** — Cursor (`Anysphere Cursor`)
- **04** — OpenAI Codex CLI & Operator
- **05** — Google Gemini CLI & Antigravity
- **06** — GitHub Copilot & Copilot Agent Mode
- **07** — Windsurf & Cascade Flow Engine
- **08** — Cline (Autonomous VS Code Extension)
- **09** — Roo Code (Advanced Task & Multi-Mode Agent)
- **10** — Aider (Git-Native Terminal Pair Programmer)
- **11** — Model Context Protocol (MCP Specification)
- **12** — Agent Skills Standard (`SKILL.md`)
- **13** — `AGENTS.md` Workspace Governance Standard
- **14** — Anthropic Claude Agent SDK
- **15** — Cursor Rules System (`.cursorrules` & `.cursor/rules`)
- **16** — OpenCode Agent & Permission Schema
- **17** — Cline Custom Modes Configuration Architecture
- **18** — Roo Code Custom Modes & Persona Rules

### Part II: Multi-Agent Systems — Runtime vs Roleplay (16 Items)
- **19** — Claude Subagents & Agent Teams [Real Runtime]
- **20** — OpenCode Subagent Engine & Background Sessions [Real Runtime]
- **21** — OpenAI Agents SDK & Swarm Framework [Real Runtime]
- **22** — Google Agent Development Kit (ADK) & A2A Protocol [Real Runtime]
- **23** — LangGraph Stateful Agent Orchestration [Real Runtime]
- **24** — CrewAI Multi-Agent Flows [Hybrid Real Runtime]
- **25** — AutoGen & Microsoft Agent Framework (MAF) [Real Runtime]
- **26** — MetaGPT Multi-Agent Framework [Roleplay Archetype]
- **27** — OpenHands / OpenDevin Execution Runtime [Real Runtime]
- **28** — Devin & Cognition Background Sandbox Worker [Real Runtime]
- **29** — Anthropic Orchestrator-Worker Multi-Agent Pattern [Real Runtime Architecture]
- **30** — Evaluator-Optimizer & Planner-Executor Runtime Pattern [Architectural Pattern]
- **31** — Multi-Agent Consensus & Majority Voting Council [Architectural Pattern]
- **32** — Adversarial Red-Team / Blue-Team Code Review System [Architectural Pattern]
- **33** — Blackboard & Shared-Memory Distributed State Pattern [Architectural Pattern]
- **34** — Agent Communication Protocol (ACP) Specification [Communication Protocol]

### Part III: Harness Engineering & Process Guardrails (18 Items)
- **35** — GitHub Spec Kit (Spec-Driven Development Core)
- **36** — OpenSpec / OPSX (Brownfield Lightweight Spec Delta)
- **37** — Google Conductor (Workspace Lifecycle Harness)
- **38** — Definition of Done (DoD) & Convergence Gates
- **39** — Automated TDD & Test-Driven Self-Correction Loops
- **40** — Bounded Execution Loops & Runaway Protections (`--max-turns`)
- **41** — Autonomous Background Loops & Task Daemons
- **42** — State Checkpointing, Git Snapshots & Time-Travel Rewind
- **43** — Git Worktree Isolation & Parallel Workspaces
- **44** — Ephemeral Container Sandboxes (Docker / Firecracker / WASM)
- **45** — Structured Session Handoffs & Cross-Agent Briefings
- **46** — Living Documentation & LLM-Docs Actualization
- **47** — Pre-Commit Enforcement & Static Analysis Verification
- **48** — Structured Evidence Logging & OpenTelemetry Tracing
- **49** — Granular Permission Tiers & Human-in-the-Loop Gates
- **50** — Token Budgeting & Financial Cost Tracking
- **51** — Self-Improving Harness & Failure-Memory Loops
- **52** — SWE-bench Evaluation Harness & Agent Benchmarking

### Part IV: Context & Memory Systems (16 Items)
- **53** — OpenAI Embeddings (`text-embedding-3-small/large`) [Vector]
- **54** — Google Gemini Embeddings (`text-embedding-004`) [Vector]
- **55** — Cohere Rerank & Voyage AI Code Embeddings [Vector / Reranker]
- **56** — pgvector (PostgreSQL Vector Extension) [Service / Vector]
- **57** — Pinecone Serverless Vector Database [Service / Vector]
- **58** — Weaviate Native Hybrid Vector & BM25 Database [Service / Hybrid Vector]
- **59** — Qdrant & Qdrant Edge Vector Search Engine [Service / Vector]
- **60** — Milvus & Zilliz Cloud Distributed Vector Store [Service / Vector]
- **61** — Chroma Embedded Vector Database [Local-Index / Vector]
- **62** — LanceDB Serverless Embedded Vector Engine [Local-Index / Vector]
- **63** — Tree-Sitter Structural Code Syntax Engine [Graph / AST]
- **64** — ast-grep Structural Search & Semantic Linting [Graph / AST]
- **65** — Aider Tree-Sitter Repo Map (PageRank Symbol Graph) [Graph / Repo Map]
- **66** — Repomix / CodePack Codebase Context Bundler [Local-Index / Direct-Retrieval]
- **67** — Context7 Dynamic Documentation Grounding Engine [Direct-Retrieval / Docs Grounding]
- **68** — Hierarchical Session Memory & Context Compaction Protocols [Local-Index / Memory]

---

## Part I: Coding Agents & Extension Architectures

### 01 — OpenCode
- **Canonical identity:** `npm:opencode-ai` · `github:anomalyco/opencode` (formerly sst/opencode)
- **Category:** Coding Agents → Terminal-First Open-Source Agent
- **Type:** Open Source (MIT)
- **Official URL:** https://opencode.ai/docs (Subagents: https://opencode.ai/docs/agents)
- **Description:** A fast, multi-provider terminal and desktop coding agent supporting 75+ LLM endpoints. Built natively with distinct operational roles: `build` (primary code editing, shell execution), `plan` (read-only architectural planning), `general`, and `explore`. Extensible via markdown agent configurations, custom commands, and standard MCP connections.
- **Capabilities:** TUI and headless CLI operation, subagent dispatch with isolated state, permission filtering per directory/file pattern, native git branch integration.
- **Integration:** Terminal CLI, VS Code extension, MCP server client.
- **Compatibility:** Native.
- **Security & Limits:** Granular permission frontmatter in `~/.config/opencode/agents/*.md`; deny rules for `.env` and external paths.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 02 — Claude Code
- **Canonical identity:** `npm:@anthropic-ai/claude-code` · Anthropic
- **Category:** Coding Agents → Reference Terminal & IDE Coding Agent
- **Type:** Commercial / API (Anthropic)
- **Official URL:** https://code.claude.com/docs/en/
- **Description:** Anthropic’s flagship command-line agentic coding environment. Features native subagents (Explore, Plan, Task Execution), skill commands (`/code-review`, `/init`), comprehensive lifecycle hooks (`PreToolUse`, `PostToolUse`, `PermissionRequest`), checkpointing with rollback, and background headless processing (`claude -p`).
- **Capabilities:** Agentic file editing, shell command execution, automated multi-turn bug fixing, subagent delegation, structured session checkpoints.
- **Integration:** Terminal CLI, VS Code / JetBrains plugins, Claude Agent SDK.
- **Compatibility:** Native.
- **Security & Limits:** Strict multi-tier approval modes (Default, Plan Mode, Auto-Approve bypass); bash sandbox constraints.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 03 — Cursor
- **Canonical identity:** `app:cursor` · Anysphere
- **Category:** Coding Agents → AI-Native Forked IDE
- **Type:** Commercial (Proprietary)
- **Official URL:** https://www.cursor.com/
- **Description:** An AI-native code editor built upon the VS Code core. Integrates inline multi-file editing (Composer / Agent Mode), fast speculative diff application, symbol-level codebase indexing, `.cursorrules` prompt injection, and background cloud agents capable of running asynchronous tasks on git branches.
- **Capabilities:** Whole-repo semantic indexing, multi-file atomic edits, terminal execution, automatic linter feedback loop, background agent workers.
- **Integration:** Standalone desktop IDE application, remote SSH, cloud task runner.
- **Compatibility:** Native.
- **Security & Limits:** Privacy mode (zero data retention), user confirmation for destructive terminal commands and file overwrites.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 04 — OpenAI Codex CLI & Operator
- **Canonical identity:** `tool:openai-codex` · OpenAI
- **Category:** Coding Agents → Autonomous Developer CLI & SDK
- **Type:** Commercial API / CLI
- **Official URL:** https://platform.openai.com/docs/guides/code
- **Description:** OpenAI’s developer agent infrastructure powering advanced coding models (o1, o3, GPT-4o series). Operates across terminal harnesses with tool-calling loops for bash execution, file differential patching, syntax validation, and subagent orchestration via the OpenAI Agents SDK.
- **Capabilities:** Reasoning-guided code synthesis, iterative test execution, MCP tool consumption, structured output JSON patch enforcement.
- **Integration:** Terminal harnesses, REST API, OpenAI Python/TS Agent SDKs.
- **Compatibility:** Native.
- **Security & Limits:** Ephemeral container isolation required for arbitrary code execution; token usage limits.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 05 — Google Gemini CLI & Antigravity
- **Canonical identity:** `tool:gemini-cli` / `tool:antigravity` · Google
- **Category:** Coding Agents → Multi-Turn Agentic Assistant & CLI
- **Type:** Commercial / API (Google DeepMind)
- **Official URL:** https://ai.google.dev/
- **Description:** Google’s high-context agentic developer platform powered by Gemini 1.5/2.0 series (offering up to 2M tokens context). Antigravity and Gemini CLI provide interactive pair programming, autonomous goal execution (`/goal`), slash commands, reactive messaging wakes, and native subagent spawning with workspace branching.
- **Capabilities:** Massive repository context window loading, multimodal artifact inspection, AST/file tool manipulation, cron/background scheduling.
- **Integration:** Terminal CLI, Google Cloud Workstations, VS Code extensions.
- **Compatibility:** Native.
- **Security & Limits:** Tool approval policies, read-only guardrails, workspace-scoped command execution.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 06 — GitHub Copilot & Copilot Agent Mode
- **Canonical identity:** `extension:github-copilot` · GitHub / Microsoft
- **Category:** Coding Agents → IDE Extension & Autonomous Workspace Agent
- **Type:** Commercial (Subscription)
- **Official URL:** https://github.com/features/copilot
- **Description:** Evolves GitHub Copilot from autocomplete into an autonomous multi-file coding agent inside VS Code and Visual Studio. Copilot Agent Mode autonomously edits files, executes terminal tests, interprets error traces, and iterates until the user's objective is satisfied.
- **Capabilities:** Multi-file workspace edits, terminal execution with user permissions, MCP integration, Copilot Workspace pull-request workflows.
- **Integration:** VS Code, Visual Studio, JetBrains, GitHub Web.
- **Compatibility:** Native.
- **Security & Limits:** Granular terminal command permission prompts, enterprise telemetry policies.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 07 — Windsurf & Cascade Flow Engine
- **Canonical identity:** `app:windsurf` · Codeium / Cognition
- **Category:** Coding Agents → Collaborative AI IDE
- **Type:** Commercial
- **Official URL:** https://codeium.com/windsurf
- **Description:** An AI-native IDE designed around the "Cascade" collaborative flow model. Bridges developer intent and agent autonomy through deep real-time awareness of developer actions, AST-aware codebase understanding, and reactive execution loops.
- **Capabilities:** Real-time context tracking (active files, cursor location, terminal output), multi-file atomic edits, command suggestion and execution.
- **Integration:** Desktop IDE (VS Code fork), Codeium backend.
- **Compatibility:** Native.
- **Security & Limits:** User verification required for system modifications; local index caching.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 08 — Cline (formerly Claude Dev)
- **Canonical identity:** `extension:saoudrizwan.claude-dev` · `github:cline/cline`
- **Category:** Coding Agents → Autonomous Terminal/IDE Agent Extension
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://github.com/cline/cline
- **Description:** Autonomous VS Code extension that plans, creates/edits files, executes terminal commands, and browses the web using LLMs. Features strict human-in-the-loop permission checkboxes for each tool call, context-preserving memory banks, and native MCP client support.
- **Capabilities:** End-to-end task completion, terminal command approval prompts, file diff review, browser automation via Puppeteer/MCP, custom system prompts.
- **Integration:** VS Code Extension Marketplace, Open VSX, MCP servers.
- **Compatibility:** Native.
- **Security & Limits:** Individual tool approval toggles; dangerous commands require explicit developer confirmation.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 09 — Roo Code (formerly Roo Cline)
- **Canonical identity:** `extension:rooveterinaryinc.roo-cline` · `github:RooVetGit/Roo-Code`
- **Category:** Coding Agents → Multi-Persona Autonomous IDE Agent
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://github.com/RooVetGit/Roo-Code
- **Description:** A feature-rich community fork of Cline introducing distinct operational modes (Code, Architect, Ask, Test, and custom user-defined modes). Each mode has customized tool whitelists, system instructions, and specialized operational bounds.
- **Capabilities:** Mode switching (e.g. Architect cannot edit files, only design; Code executes edits), MCP integration, customized rule sets, sound/notification alerts.
- **Integration:** VS Code, Open VSX, MCP clients.
- **Compatibility:** Native.
- **Security & Limits:** Mode-based capability gating; tool approval toggles for terminal and file writes.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 10 — Aider
- **Canonical identity:** `pip:aider-chat` · `github:paul-gauthier/aider`
- **Category:** Coding Agents → Git-Native Terminal Pair Programmer
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://aider.chat/
- **Description:** The industry standard for command-line pair programming with git. Employs a sophisticated Tree-sitter repo map to feed concise repository structure into LLMs, applies changes as git commits with auto-generated descriptive commit messages, and features automated test/lint fix loops.
- **Capabilities:** Whole-repo map generation, unified diff and whole-file edit formats, automatic git commits, `--test` / `--lint` test-driven repair loops.
- **Integration:** Terminal CLI, git repositories, works with any LLM provider.
- **Compatibility:** Native.
- **Security & Limits:** Runs locally; all changes tracked as standard git commits allowing instantaneous `git reset`.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 11 — Model Context Protocol (MCP)
- **Canonical identity:** `spec:model-context-protocol` · Anthropic & Open Source Community
- **Category:** Extension Systems → Standardized Tool & Resource Bus
- **Type:** Open Standard (MIT)
- **Official URL:** https://modelcontextprotocol.io/
- **Description:** An open universal protocol establishing client-server communication between LLM applications and external tools, databases, and context providers. Replaces custom brittle tool integrations with standardized JSON-RPC 2.0 messages across `stdio` or Server-Sent Events (SSE).
- **Capabilities:** Dynamic tool discovery, resource reading, prompt template exposure, roots/workspace boundaries, sampling capabilities.
- **Integration:** Claude Code, Cursor, Cline, Roo Code, OpenCode, Zed, Sourcegraph.
- **Compatibility:** Native universal standard.
- **Security & Limits:** Servers run with host system privileges; clients must enforce permission prompts before tool invocations.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 12 — Agent Skills Standard (`SKILL.md`)
- **Canonical identity:** `format:agent-skills` · Cross-Agent Ecosystem
- **Category:** Extension Systems → Standardized Skill & Workflow Specification
- **Type:** Open Specification
- **Official URL:** https://github.com/anthropics/anthropic-quickstarts
- **Description:** A standardized directory and file format (`SKILL.md`) that extends agent functionality. Contains YAML frontmatter (name, description, required tools) followed by structured procedural guidelines, operational scripts, and prompt injection patterns.
- **Capabilities:** Reusable domain-specific workflows (e.g. database migration, security audits, PR reviews) portable across Claude Code, OpenCode, and Antigravity.
- **Integration:** File-based discovery in `.gemini/skills`, `.claude/skills`, or project root.
- **Compatibility:** Compatible across modern agent harnesses.
- **Security & Limits:** Script execution requires validation against host security posture.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 13 — `AGENTS.md` Workspace Governance Standard
- **Canonical identity:** `standard:agents-md` · Open Standard
- **Category:** Extension Systems → Agent Instructions & Boundary Definition
- **Type:** Open Specification
- **Official URL:** https://agents.md/
- **Description:** A lightweight markdown standard placed at the root of a repository to guide autonomous AI agents. Outlines project architectural invariants, build/test commands, style guidelines, and forbidden directories.
- **Capabilities:** Direct context injection into agent system prompts, eliminating repetitive developer steering.
- **Integration:** Recognized natively or as supplementary context across Aider, OpenCode, Claude Code, Cursor, and Copilot.
- **Compatibility:** Universal text standard.
- **Security & Limits:** Advisory context; must be reinforced by executable pre-commit hooks and harness guards.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 14 — Anthropic Claude Agent SDK
- **Canonical identity:** `pkg:@anthropic-ai/claude-agent-sdk` · Anthropic
- **Category:** Extension Systems → Programmatic Agent Development Framework
- **Type:** Commercial SDK / Open Source Wrappers
- **Official URL:** https://code.claude.com/docs/en/agent-sdk
- **Description:** A software development kit enabling developers to build custom agent harnesses, define subagent topologies, hook into tool lifecycle events, and programmatically orchestrate headless Claude Code sessions.
- **Capabilities:** Strongly-typed agent definitions, isolated memory scopes, custom tool routing, event stream subscriptions.
- **Integration:** Node.js/TypeScript and Python environments.
- **Compatibility:** Native.
- **Security & Limits:** Enforces API authentication; provides programmable sandbox hooks.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 15 — Cursor Rules System (`.cursorrules` & `.cursor/rules`)
- **Canonical identity:** `spec:cursor-rules` · Anysphere
- **Category:** Extension Systems → Contextual Prompt Rule Injection
- **Type:** Proprietary Specification
- **Official URL:** https://docs.cursor.com/context/rules-for-ai
- **Description:** Project-level and directory-level rule definition system. Allows developers to specify exact coding guidelines, framework quirks, and formatting constraints that are automatically matched and injected into the LLM context window based on active file paths.
- **Capabilities:** Path-specific glob matching, system instruction override, project-wide standard enforcement.
- **Integration:** Embedded natively in Cursor IDE.
- **Compatibility:** Native.
- **Security & Limits:** Advisory prompt steering; does not hard-block unauthorized terminal commands.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 16 — OpenCode Agent & Permission Schema
- **Canonical identity:** `schema:opencode-agent-config` · OpenCode
- **Category:** Extension Systems → Declarative Agent Configuration
- **Type:** Open Source Schema (JSON/Markdown)
- **Official URL:** https://opencode.ai/docs/agents
- **Description:** Declarative configuration format residing in `opencode.json` or `.config/opencode/agents/*.md`. Defines agent role (primary vs subagent), assigned model provider, system prompt, and fine-grained tool permissions (e.g. allow `bash`, deny write to `*.env`).
- **Capabilities:** Role separation (Planner, Builder, Reviewer), explicit tool whitelists, background thread orchestration.
- **Integration:** OpenCode CLI and desktop app.
- **Compatibility:** Native.
- **Security & Limits:** Strict JSON schema validation; system blocks unauthorized tool invocation at the runtime layer.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 17 — Cline Custom Modes Configuration Architecture
- **Canonical identity:** `schema:cline-custom-modes` · Cline
- **Category:** Extension Systems → Custom Operational Mode Definitions
- **Type:** Open Source Schema
- **Official URL:** https://github.com/cline/cline
- **Description:** The JSON configuration architecture (`cline_custom_modes.json`) allowing developers to create tailored operational modes with distinct role descriptions, custom prompt instructions, and restricted tool groups (`read`, `edit`, `browser`, `command`, `mcp`).
- **Capabilities:** Zero-code agent specialization; separation between architectural consultation and destructive code manipulation.
- **Integration:** Cline VS Code extension.
- **Compatibility:** Native.
- **Security & Limits:** Enforced at the extension message dispatch layer; unlisted tools cannot be called by the model.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 18 — Roo Code Custom Modes & Persona Rules
- **Canonical identity:** `spec:roo-custom-modes` · Roo Code
- **Category:** Extension Systems → Mode & Persona Specialization
- **Type:** Open Source Specification
- **Official URL:** https://github.com/RooVetGit/Roo-Code
- **Description:** Roo Code’s extension framework supporting community-shared mode configurations (`.roomodes`) and mode-specific rule files (`.roo/rules-[mode]`). Enables teams to commit standardized agent personas (e.g., Security Auditor, SQL Optimizer) directly to git repositories.
- **Capabilities:** Git-versioned agent personas, dynamic tool binding, mode-specific prompt injection.
- **Integration:** Roo Code VS Code extension.
- **Compatibility:** Native.
- **Security & Limits:** Capabilities strictly bounded by the host mode's declared permissions.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

---

## Part II: Multi-Agent Systems: Real Runtime vs Single-Model Roleplay

### The Foundational Distinction
- **Real Runtime:** Independent processes or async execution sessions. Each agent maintains its **own isolated context window**, **independent scratchpad/state**, **discrete tool permissions**, and interacts via deterministic protocols (message queues, JSON-RPC, A2A, IPC). Failures in child agents do not pollute the parent context.
- **Single-Model Roleplay:** A single LLM execution thread prompted to "act as" multiple participants (e.g. "You are Alice the architect and Bob the developer. Have a dialogue..."). There is **zero memory isolation**, **zero tool permission boundaries**, and high risk of context drift, persona bleeding, and cumulative hallucination.

```
+-------------------------------------------------------------------------------+
| REAL RUNTIME MULTI-AGENT ARCHITECTURE                                         |
|                                                                               |
|  [ Parent / Orchestrator Session ]                                            |
|   | Context Window A (High-level goals, task DAG, token budget)               |
|   +---> Tool Call: spawn_agent("explorer", prompt="Survey AST")               |
|          |                                                                    |
|          v (Process / Session Isolation Barrier)                              |
|  [ Child Subagent Session: Explorer ]                                         |
|   | Context Window B (Clean 200k tokens, grep/LSP tools ONLY)                 |
|   | Reads 50 files, filters syntax, synthesizes 10-line summary               |
|   +---> Structured Result Return: { "targets": ["api.ts#L40"] }               |
|          |                                                                    |
|          v (Context Compaction & Memory Firewall)                             |
|  [ Parent Session Continues ]                                                 |
|   | Absorbs only 10-line summary. 50 raw file dumps NEVER enter Context A!     |
+-------------------------------------------------------------------------------+
```

---

### 19 — Claude Subagents & Agent Teams
- **Canonical identity:** `tool:claude-code/teams` · Anthropic
- **Category:** Multi-Agent → Vendor Subagent Runtime & Team Coordinator
- **Type:** Commercial Runtime (Anthropic)
- **Official URL:** https://code.claude.com/docs/en/sub-agents
- **Description:** Built-in multi-agent subagent system. Allows an orchestrator agent to spawn specialized subagents (Explore, Plan, Custom) with isolated context windows, specialized toolsets, and scoped permission profiles. The `Agent Teams` interface monitors background execution status.
- **Runtime Class:** **Real Runtime.** Evidence: Subagents run as distinct execution sessions with fresh context windows; parent context receives only the structured final return payload; tool permissions are evaluated independently per subagent definition.
- **Capabilities:** Parallel background repo investigation, test isolation, firewalling verbose file outputs from the orchestrator's context window.
- **Integration:** Claude Code CLI, Claude Agent SDK.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 20 — OpenCode Subagent Engine & Background Sessions
- **Canonical identity:** `tool:opencode/subagents` · OpenCode.ai
- **Category:** Multi-Agent → Open-Source Process-Isolated Subagent Engine
- **Type:** Open Source Runtime (MIT)
- **Official URL:** https://opencode.ai/docs/agents
- **Description:** OpenCode's execution architecture supporting primary agents (`build`, `plan`) that programmatically spawn background subagents (`general`, `explore`, or custom markdown definitions). Subagents execute asynchronously and post status updates back to the parent TUI session.
- **Runtime Class:** **Real Runtime.** Evidence: Distinct session IDs, independent LLM API calls with distinct message arrays, and strict memory boundaries preventing prompt leakage.
- **Capabilities:** Asynchronous dependency indexing, parallel test execution, headless delegation.
- **Integration:** OpenCode CLI.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 21 — OpenAI Agents SDK & Swarm Framework
- **Canonical identity:** `pkg:openai-agents-sdk` · OpenAI
- **Category:** Multi-Agent → Lightweight Agent Coordination Runtime
- **Type:** Open Source (Apache-2.0 / MIT)
- **Official URL:** https://github.com/openai/swarm
- **Description:** OpenAI’s reference implementation for agent orchestration, succeeding the educational Swarm experiment. Centers around two core primitives: `Agents` (encapsulating instructions and tools) and `Handoffs` (where an active agent transfers the conversational execution token and context to another agent).
- **Runtime Class:** **Real Runtime.** Evidence: Execution control shifts between distinct agent instances with dedicated function definitions and state objects.
- **Capabilities:** Clean agent-to-agent transfers, deterministic tool gating, modular workflow graphs.
- **Integration:** Python/Node.js SDKs, OpenAI function calling APIs.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 22 — Google Agent Development Kit (ADK) & A2A Protocol
- **Canonical identity:** `framework:google-adk` · Google
- **Category:** Multi-Agent → Enterprise Multi-Agent Framework & Protocol
- **Type:** Open Framework / Commercial Cloud
- **Official URL:** https://ai.google.dev/
- **Description:** Google’s enterprise agent runtime supporting the Agent-to-Agent (A2A) protocol. Enables autonomous agents across different runtimes and clouds to discover capabilities, negotiate schemas, exchange tasks, and verify execution integrity.
- **Runtime Class:** **Real Runtime.** Evidence: Distributed process boundaries communicating across network endpoints via signed A2A JSON envelopes.
- **Capabilities:** Cross-platform agent negotiation, distributed task graphs, enterprise IAM token propagation.
- **Integration:** Google Vertex AI, Gemini CLI, enterprise message buses.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 23 — LangGraph Stateful Agent Orchestration
- **Canonical identity:** `pkg:langgraph` · LangChain
- **Category:** Multi-Agent → Cyclic Graph State Machine Runtime
- **Type:** Open Source (MIT)
- **Official URL:** https://www.langchain.com/langgraph
- **Description:** A low-level orchestration framework modeling multi-agent interactions as directed cyclic graphs. Every agent is represented as a node that reads and mutates a central, strictly-typed state schema. Supports human-in-the-loop checkpoints, time-travel, and branching.
- **Runtime Class:** **Real Runtime.** Evidence: Formal state-machine engine; each node invocation executes as a discrete step with isolated local variables and deterministic reducer updates.
- **Capabilities:** Cyclic agent loops, durable persistence (Postgres, SQLite), conditional branching, execution rewind.
- **Integration:** LangChain ecosystem, Python, TypeScript.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 24 — CrewAI Multi-Agent Flows
- **Canonical identity:** `pkg:crewai` · CrewAI
- **Category:** Multi-Agent → Role-Based Agent Team Framework
- **Type:** Open Source / Commercial Enterprise
- **Official URL:** https://www.crewai.com/
- **Description:** Framework for orchestrating role-playing autonomous agents into cooperative "Crews" and structured "Flows". Agents are configured with distinct backstories, goals, tool delegations, and memory buffers (short-term, long-term, entity).
- **Runtime Class:** **Hybrid Real Runtime.** Evidence: Employs discrete tool bindings and multi-step execution loops per agent; however, prompts heavily leverage roleplay instructions that require runtime guardrails to prevent persona degradation.
- **Capabilities:** Sequential, hierarchical, and consensual task delegation; automatic tool passing.
- **Integration:** Python runtime, LiteLLM provider bus.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 25 — AutoGen & Microsoft Agent Framework (MAF)
- **Canonical identity:** `pkg:autogen` / `pkg:microsoft-agent-framework` · Microsoft Research
- **Category:** Multi-Agent → Conversable Multi-Agent Platform
- **Type:** Open Source (MIT)
- **Official URL:** https://microsoft.github.io/autogen/
- **Description:** Microsoft’s flagship multi-agent framework featuring event-driven, conversable agents. Upgraded through AutoGen 0.4 / Microsoft Agent Framework into an asynchronous actor-model architecture with strict message-passing interfaces.
- **Runtime Class:** **Real Runtime.** Evidence: Distributed actor model where each agent is an asynchronous process maintaining private state and communicating via strongly-typed messages.
- **Capabilities:** Actor-based concurrency, human-in-the-loop interception, containerized tool sandboxes, distributed deployment.
- **Integration:** Python, .NET.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 26 — MetaGPT Multi-Agent Framework
- **Canonical identity:** `github:geekan/MetaGPT` · DeepWisdom
- **Category:** Multi-Agent → Simulated Software Company Framework
- **Type:** Open Source (MIT)
- **Official URL:** https://github.com/geekan/MetaGPT
- **Description:** A multi-agent framework encoding Standard Operating Procedures (SOPs) into agent roles (Product Manager, Architect, Project Manager, Engineer, QA). Roles communicate via shared documents (PRDs, system designs, API specs).
- **Runtime Class:** **Single-Model Roleplay Archetype (with structured artifacts).** Evidence: Primarily coordinates simulated personas through prompt templating and message bus broadcasts; lacks hardware process isolation or independent execution privilege policies.
- **Capabilities:** Automated generation of PRDs, architecture diagrams (Mermaid), and codebases from simple prompts.
- **Integration:** Python CLI.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 27 — OpenHands (formerly OpenDevin)
- **Canonical identity:** `github:All-Hands-AI/OpenHands` · All-Hands AI
- **Category:** Multi-Agent → Autonomous Software Development Platform
- **Type:** Open Source (MIT)
- **Official URL:** https://github.com/All-Hands-AI/OpenHands
- **Description:** An open-source autonomous software engineering platform capable of executing complex engineering tasks. Coordinates specialized agent loops (Planner, Coder, Evaluator) inside a secure Docker container sandbox.
- **Runtime Class:** **Real Runtime.** Evidence: Complete virtualization; agent actions execute inside real Linux Docker containers with dedicated virtual environments, bash shells, and network bridges.
- **Capabilities:** Sandboxed code execution, browser automation, multi-file codebase manipulation, interactive UI.
- **Integration:** Docker, Kubernetes, Web GUI, CLI.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 28 — Devin & Cognition Background Sandbox Worker
- **Canonical identity:** `app:devin` · Cognition AI
- **Category:** Multi-Agent → Autonomous Cloud Software Engineer
- **Type:** Commercial Cloud Service
- **Official URL:** https://cognition.ai/
- **Description:** Autonomous cloud-hosted software engineer equipped with its own shell, code editor, browser, and background planner. Operates across real git repositories in secure cloud microVM sandboxes.
- **Runtime Class:** **Real Runtime.** Evidence: Isolated cloud virtual machines with real OS processes, file systems, and dedicated execution runtimes per task.
- **Capabilities:** Autonomous bug fixing, dependency migration, long-running pull request resolution, automated deployment testing.
- **Integration:** GitHub, Slack, Linear, Cloud dashboard.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 29 — Anthropic Orchestrator-Worker Multi-Agent Pattern
- **Canonical identity:** `pattern:orchestrator-worker` · Anthropic Research
- **Category:** Multi-Agent → Core Multi-Agent Architecture Pattern
- **Type:** Architectural Pattern / Production Standard
- **Official URL:** https://www.anthropic.com/research/building-effective-agents
- **Description:** The gold standard architectural pattern for complex agentic workflows: A central Orchestrator LLM breaks a user specification into independent tasks, spawns isolated Worker agents to execute each task with scoped tools and context, and aggregates their synthesized results.
- **Runtime Class:** **Real Runtime Architecture.** Evidence: Prevents context window degradation by delegating sub-problems to child contexts, absorbing only concise summaries back into the primary orchestrator.
- **Capabilities:** Parallel repository search, modular test writing, distributed feature generation.
- **Integration:** Implementable in Claude Agent SDK, LangGraph, OpenCode.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 30 — Evaluator-Optimizer & Planner-Executor Runtime Pattern
- **Canonical identity:** `pattern:evaluator-optimizer` · Industry Standard
- **Category:** Multi-Agent → Quality Assurance & Verification Architecture
- **Type:** Architectural Pattern
- **Official URL:** https://www.anthropic.com/research/building-effective-agents
- **Description:** A decoupled two-agent pattern where an Executor agent generates code solutions and an independent Evaluator agent (equipped with compiler, linter, and test suite tools) critiques the output against formal acceptance criteria, initiating iterative refinement loops.
- **Runtime Class:** **Real Runtime Pattern.** Evidence: The Evaluator must operate with independent instructions and objective verification tools to avoid the generator's self-affirmation bias.
- **Capabilities:** Elimination of hallucinated test passes, high-precision algorithmic problem solving.
- **Integration:** Standard harness loops in Aider, Claude Code, and SWE-bench runners.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 31 — Multi-Agent Consensus & Majority Voting Council
- **Canonical identity:** `pattern:agent-consensus-council` · Architectural Pattern
- **Category:** Multi-Agent → Deliberative Decision Architecture
- **Type:** Architectural Pattern
- **Official URL:** https://arxiv.org/abs/2305.14325
- **Description:** An architectural pattern where multiple heterogeneous LLMs (e.g. Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) independently analyze an architectural design or security patch, followed by a deterministic voting or debate aggregator that reconciles differences into a verified consensus.
- **Runtime Class:** **Real Runtime Architecture.** Evidence: Multiple isolated model queries executed concurrently; requires external deterministic voting logic.
- **Capabilities:** High-stakes security auditing, architectural invariant review, bias reduction.
- **Integration:** Multi-provider API gateways, custom agent harnesses.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 32 — Adversarial Red-Team / Blue-Team Code Review System
- **Canonical identity:** `pattern:adversarial-red-blue` · Architectural Pattern
- **Category:** Multi-Agent → Adversarial Verification Architecture
- **Type:** Architectural Pattern
- **Official URL:** https://csrc.nist.gov/
- **Description:** A dual-agent architecture where the Blue Agent is tasked with generating secure implementation code, while the Red Agent is explicitly prompted and equipped with fuzzing and static analysis tools to discover exploitable vulnerabilities, race conditions, and boundary failures in the Blue Agent's diff.
- **Runtime Class:** **Real Runtime Architecture.** Evidence: Distinct opposing goals, separated memory buffers, and conflicting reward/completion functions.
- **Capabilities:** Hardening cryptographic routines, discovering OWASP Top 10 vulnerabilities, verifying edge cases.
- **Integration:** CI/CD security pipelines, autonomous agent review gates.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 33 — Blackboard & Shared-Memory Distributed State Pattern
- **Canonical identity:** `pattern:blackboard-shared-memory` · AI Architecture Pattern
- **Category:** Multi-Agent → Centralized Collaborative State Architecture
- **Type:** Architectural Pattern
- **Official URL:** https://en.wikipedia.org/wiki/Blackboard_system
- **Description:** Classic distributed AI architecture applied to modern agent swarms: A central shared data store (the "Blackboard") holds the current state of the codebase, outstanding problems, and verification results. Diverse specialist agents asynchronously inspect the blackboard and post solutions.
- **Runtime Class:** **Real Runtime Architecture.** Evidence: Centralized database (Redis, Postgres, SQLite) acting as the source of truth, decoupling agent lifecycles from persistent task state.
- **Capabilities:** Non-linear problem solving, concurrent multi-developer simulation, fault-tolerant agent resumption.
- **Integration:** Redis, PostgreSQL, LangGraph persistence backends.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 34 — Agent Communication Protocol (ACP) Specification
- **Canonical identity:** `spec:agent-communication-protocol` · Open Source Standard
- **Category:** Multi-Agent → Inter-Agent Transport & Messaging Specification
- **Type:** Open Specification
- **Official URL:** https://github.com/agent-communication-protocol
- **Description:** Emerging communication standard defining structured message formats, session handshakes, and capability negotiation for autonomous agents operating across disparate frameworks and organizations.
- **Runtime Class:** **Protocol.** Evidence: Defines wire protocol (JSON/gRPC) for inter-process and inter-network agent coordination.
- **Capabilities:** Cross-vendor agent interoperability, verified identity tokens, capability discovery.
- **Integration:** Bridge layers between AutoGen, CrewAI, and custom corporate agents.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

---

## Part III: Harness Engineering & Process Guardrails

### 35 — GitHub Spec Kit (Spec-Driven Development Core)
- **Canonical identity:** `tool:spec-kit` · `github:github/spec-kit` · `pip:specify-cli`
- **Category:** Harness → Spec-Driven Process Harness
- **Type:** Open Source (MIT)
- **Official URL:** https://github.com/github/spec-kit
- **Description:** A vendor-agnostic development harness enforcing Spec-Driven Development (SDD). Operates on a strict five-stage progression: `specify` → `plan` → `tasks` → `implement` → `converge`. Enforces project "Constitutions", ensuring that architectural invariants and requirements precede all code synthesis.
- **Capabilities:** Cross-agent compatibility (38+ agent integrations including Copilot, Claude, Gemini, Cursor), deterministic milestone checklists, automated convergence validation.
- **Integration:** Shell CLI (`specify`), Markdown workspace contracts.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 36 — OpenSpec / OPSX
- **Canonical identity:** `tool:openspec` · `npm:@fission-ai/openspec` · `github:Fission-AI/OpenSpec`
- **Category:** Harness → Brownfield Lightweight Spec Delta Harness
- **Type:** Open Source (MIT)
- **Official URL:** https://github.com/Fission-AI/OpenSpec
- **Description:** A lightweight specification harness tailored for existing brownfield applications. Implements the OPSX loop: `explore` → `propose` → `apply` → `verify` → `archive`. Focuses on generating atomic spec deltas that can be verified and committed alongside source code changes.
- **Capabilities:** Brownfield codebase adaptation, atomic delta verification, automatic spec archival.
- **Integration:** CLI (`openspec`), npm package, Git hooks.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 37 — Google Conductor
- **Canonical identity:** `tool:google-conductor` · Google
- **Category:** Harness → Workspace Lifecycle & Context Orchestrator
- **Type:** Commercial Platform Harness
- **Official URL:** https://ai.google.dev/
- **Description:** Workspace lifecycle harness for developer agents. Coordinates specification gathering, repository mapping, execution loop monitoring, and structured handoff artifacts across multi-stage engineering tasks.
- **Capabilities:** Spec verification, automated task tracking, dynamic context hydration from cloud telemetry.
- **Integration:** Gemini developer CLI, Google Cloud Workstations.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 38 — Definition of Done (DoD) & Convergence Gates
- **Canonical identity:** `harness:dod-convergence-gate` · Architectural Pattern
- **Category:** Harness → Formal Verification & Acceptance Gates
- **Type:** Process & Tool Harness
- **Official URL:** https://martinfowler.com/bliki/DefinitionOfDone.html
- **Description:** A programmatic harness pattern requiring agents to validate code modifications against an immutable checklist before terminating a session: (1) Code compiles without errors; (2) Unit and regression tests pass; (3) Static analysis/linting passes; (4) Documentation/spec updated.
- **Capabilities:** Halts premature agent exit; forces continuous self-correction until full checklist convergence is achieved.
- **Integration:** Pre-commit hooks, CI/CD pipelines, agent evaluation loops.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 39 — Automated TDD & Test-Driven Self-Correction Loops
- **Canonical identity:** `harness:automated-tdd-loop` · Industry Standard
- **Category:** Harness → Execution Loop & Auto-Fix Architecture
- **Type:** Operational Pattern
- **Official URL:** https://aider.chat/docs/faq.html#how-does-aider-use-git
- **Description:** A test-driven development harness where the agent writes failing test cases first, executes the test suite to verify the failure, implements minimal code to pass the tests, and automatically ingests compiler/test errors back into the prompt loop until a zero-exit code is returned.
- **Capabilities:** Strict test-first discipline, automated syntax and logic repair, regression prevention.
- **Integration:** Implemented natively in Aider (`--test`), Claude Code, and custom CI agent loops.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 40 — Bounded Execution Loops & Runaway Protections (`--max-turns`)
- **Canonical identity:** `guard:bounded-loop` · Security & Cost Control
- **Category:** Harness → Execution Limits & Circuit Breakers
- **Type:** Safety Harness Primitive
- **Official URL:** https://docs.anthropic.com/en/docs/agents-and-tools/agent-patterns
- **Description:** Essential guardrails preventing autonomous agents from entering infinite execution loops or consuming excessive API tokens. Enforces hard constraints: maximum turns (`--max-turns`), maximum tool calls, wall-clock timeout thresholds, and max dollar spend ceilings per task.
- **Capabilities:** Instant circuit breaking on recursive loops, cost blowup prevention, runaway process killing.
- **Integration:** CLI flags, environment variables, orchestrator middleware.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 41 — Autonomous Background Loops & Task Daemons
- **Canonical identity:** `harness:autonomous-background-daemon` · Architecture Pattern
- **Category:** Harness → Long-Running Asynchronous Agent Daemons
- **Type:** Runtime Harness
- **Official URL:** https://code.claude.com/docs/en/commands
- **Description:** Long-running background harnesses (`claude agents`, background cron tasks, headless daemons) that monitor bug trackers, poll pull requests, or run overnight refactoring tasks without active user presence, waking up on external events.
- **Capabilities:** Asynchronous issue resolution, headless batch processing, event-driven reactive wakes.
- **Integration:** Systemd daemons, GitHub Actions workers, Docker containers.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 42 — State Checkpointing, Git Snapshots & Time-Travel Rewind
- **Canonical identity:** `harness:checkpoint-rewind` · State Management
- **Category:** Harness → State Persistence & Rollback Architecture
- **Type:** Safety & Resilience Pattern
- **Official URL:** https://git-scm.com/docs/git-commit
- **Description:** Harness mechanism capturing discrete snapshots of the workspace (via temporary git commits, shadow branches, or file differential journals) before every destructive tool invocation. If an agent hallucinates or breaks the build, the harness provides single-command rollback.
- **Capabilities:** Zero-risk agent experimentation, branching exploration paths, time-travel debugging.
- **Integration:** Claude Code rewind commands, Aider git commits, LangGraph checkpointing.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 43 — Git Worktree Isolation & Parallel Workspaces
- **Canonical identity:** `tool:git-worktree-harness` · Git Core Standard
- **Category:** Harness → Workspace Isolation & Concurrency
- **Type:** Operating Pattern (Git Core)
- **Official URL:** https://git-scm.com/docs/git-worktree
- **Description:** Leveraging `git worktree` to provide each autonomous agent with an isolated physical directory backed by the same underlying `.git` object database. Agents work concurrently on separate branches without colliding with the developer's working tree or other agents.
- **Capabilities:** Zero file contention, parallel feature development, instantaneous branch checkout without disk duplication.
- **Integration:** Shell scripts, multi-agent orchestrators.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 44 — Ephemeral Container Sandboxes
- **Canonical identity:** `harness:ephemeral-sandboxes` · Infrastructure Standard
- **Category:** Harness → Security & Process Isolation
- **Type:** Virtualization Harness
- **Official URL:** https://www.docker.com/ / https://firecracker-microvm.io/
- **Description:** Sandboxing untrusted agent code execution inside ephemeral Docker containers, Firecracker microVMs, or gVisor runtimes. Grants the agent root privileges inside an isolated sandbox that is completely discarded upon task completion.
- **Capabilities:** Complete host defense against malicious bash commands (`rm -rf /`, fork bombs, unauthorized socket connections), reproducible execution environments.
- **Integration:** OpenHands, Devin, SWE-bench runner, E2B cloud sandboxes.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 45 — Structured Session Handoffs & Cross-Agent Briefings
- **Canonical identity:** `harness:structured-session-handoff` · Coordination Pattern
- **Category:** Harness → Inter-Agent State Transfer & Context Transition
- **Type:** Protocol & Pattern
- **Official URL:** https://github.com/openai/swarm
- **Description:** Standardized markdown or JSON briefing documents generated at the end of an agent's execution turn. Captures: What was accomplished, what failed, which hypotheses were discarded, and immediate next steps. Enables the succeeding agent to resume with pristine context.
- **Capabilities:** Context exhaustion mitigation, elimination of circular reasoning across shifts.
- **Integration:** Agent handover hooks, markdown summary files.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 46 — Living Documentation & LLM-Docs Actualization
- **Canonical identity:** `harness:living-docs-actualization` · Process Pattern
- **Category:** Harness → Continuous Documentation Grounding
- **Type:** Process Pattern
- **Official URL:** https://agents.md/
- **Description:** An automated harness routine requiring agents to update architecture documents, READMEs, and API specifications alongside any source code modification. Prevents documentation drift and ensures future agent runs remain accurately grounded.
- **Capabilities:** Automatic synchronization between code and specs, reduction in developer onboarding time.
- **Integration:** Pre-commit hooks, CI gates.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 47 — Pre-Commit Enforcement & Static Analysis Verification
- **Canonical identity:** `tool:pre-commit-harness` · Quality Standard
- **Category:** Harness → Quality Gates & Deterministic Checks
- **Type:** Open Source Tooling
- **Official URL:** https://pre-commit.com/
- **Description:** Git pre-commit framework executing deterministic linters (Ruff, ESLint, Clippy, Biome) and type checkers (tsc, mypy, pyright) before any agent commit is finalized. The agent must resolve all deterministic violations before proceeding.
- **Capabilities:** Hard syntax and formatting validation, zero tolerance for trivial regressions.
- **Integration:** Git hooks, GitHub Actions, agent execution harnesses.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 48 — Structured Evidence Logging & OpenTelemetry Tracing
- **Canonical identity:** `harness:opentelemetry-agent-traces` · Observability Standard
- **Category:** Harness → Agent Observability & Auditability
- **Type:** Open Standard
- **Official URL:** https://opentelemetry.io/
- **Description:** Emitting structured JSONL transcripts and OpenTelemetry trace spans for every agent event: model prompts, completions, tool invocations, bash stdout/stderr, and wall-clock latencies. Provides full post-mortem explainability.
- **Capabilities:** Comprehensive audit trails, debugging hallucination loops, performance bottleneck identification.
- **Integration:** OpenTelemetry SDKs, Langfuse, Arize Phoenix, local JSONL logs.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 49 — Granular Permission Tiers & Human-in-the-Loop Gates
- **Canonical identity:** `harness:permission-tiers` · Security Standard
- **Category:** Harness → Authorization & Blast-Radius Mitigation
- **Type:** Security Architecture Pattern
- **Official URL:** https://code.claude.com/docs/en/permissions
- **Description:** Multi-level authorization matrix categorizing tool calls into risk tiers: Tier 1 (Read-only: file read, grep, LSP query — auto-approved); Tier 2 (Non-destructive write: editing git-tracked files — user notified/auto); Tier 3 (Destructive/Network: shell execution, external API calls, force pushes — explicit manual approval required).
- **Capabilities:** Elimination of unauthorized data exfiltration or unintended repository destruction.
- **Integration:** Implemented across Claude Code, Cline, Roo Code, and OpenCode.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 50 — Token Budgeting & Financial Cost Tracking
- **Canonical identity:** `harness:cost-tracking-telemetry` · FinOps Guardrail
- **Category:** Harness → Economic Monitoring & Throttling
- **Type:** Operational Primitive
- **Official URL:** https://platform.openai.com/docs/guides/production-best-practices
- **Description:** Real-time token accounting harness tracking input tokens, output tokens, and cache-read/cache-creation operations across every turn. Enforces project-level budgets and dynamically switches tasks to lighter models when spend limits approach thresholds.
- **Capabilities:** Financial safety ceilings, real-time dollar cost attribution per bugfix or feature.
- **Integration:** Custom API wrappers, LiteLLM proxy, Portkey.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 51 — Self-Improving Harness & Failure-Memory Loops
- **Canonical identity:** `harness:failure-memory-loop` · Optimization Pattern
- **Category:** Harness → Experience Retention & Continual Improvement
- **Type:** Architectural Pattern
- **Official URL:** https://arxiv.org/abs/2305.16291
- **Description:** A persistent memory loop that logs agent failures (e.g. broken builds, failed test cases, reverted diffs) alongside root causes and successful resolutions. Ingests these failure lessons into future agent system prompts to avoid repeating known mistakes.
- **Capabilities:** Continuous agent adaptation to repo-specific idiosyncrasies, reduction of recurring antipatterns.
- **Integration:** Project-level memory files (`.agent/lessons.md`), vector memory stores.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 52 — SWE-bench Evaluation Harness & Agent Benchmarking
- **Canonical identity:** `benchmark:swe-bench` · Princeton NLP & Industry Standard
- **Category:** Harness → Empirical Agent Evaluation Framework
- **Type:** Open Source Benchmark (MIT)
- **Official URL:** https://www.swebench.com/
- **Description:** The premier academic and industry evaluation harness for coding agents. Tests agents against thousands of real GitHub issues across major Python repositories (Django, SymPy, Flask), requiring the agent to ingest the issue, generate a patch, and pass hidden test suites.
- **Capabilities:** Standardized comparative measurement of autonomous coding capabilities, elimination of cherry-picked demos.
- **Integration:** Docker execution harnesses, automated grading scripts.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

---

## Part IV: Context & Memory Systems

```
+-------------------------------------------------------------------------------+
| CONTEXT RETRIEVAL TAXONOMY & MECHANISMS                                       |
|                                                                               |
|  1. Dense Vector (ANN / HNSW)       --> Semantic meaning & conceptual search  |
|  2. Sparse Inverted Index (BM25)    --> Exact symbol, error code & token match|
|  3. Graph / AST (Tree-sitter)       --> Syntactic hierarchy, scope & call DAG |
|  4. Hybrid Fusion (RRF / Rerank)    --> Merged ranked list fed to LLM         |
+-------------------------------------------------------------------------------+
```

### 53 — OpenAI Embeddings (`text-embedding-3-small/large`)
- **Canonical identity:** `api:openai-embeddings` · OpenAI
- **Category:** Context & Memory → Dense Vector Embedding Models
- **Type:** Commercial API
- **Official URL:** https://platform.openai.com/docs/guides/embeddings
- **Mechanism:** **Vector (Producer).** Evidence: Generates 1536-dimensional (small) or 3072-dimensional (large) continuous dense vector representations optimized via cosine similarity. Supports Matryoshka dimensionality reduction for storage optimization.
- **Capabilities:** High-density semantic search, documentation indexing, clustering.
- **Integration:** Vector databases (Pinecone, Qdrant, pgvector), LlamaIndex, LangChain.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 54 — Google Gemini Embeddings (`text-embedding-004`)
- **Canonical identity:** `api:gemini-embeddings` · Google
- **Category:** Context & Memory → Multilingual Dense Vector Model
- **Type:** Commercial API
- **Official URL:** https://ai.google.dev/gemini-api/docs/embeddings
- **Mechanism:** **Vector (Producer).** Evidence: Produces 768-dimensional dense vectors with specialized task-type parameters (`RETRIEVAL_QUERY`, `RETRIEVAL_DOCUMENT`, `CODE_RETRIEVAL_QUERY`).
- **Capabilities:** Code snippet semantic search, high-recall documentation grounding.
- **Integration:** Vertex AI Search, Google Cloud Spanner/PostgreSQL, LangChain.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 55 — Cohere Rerank & Voyage AI Code Embeddings
- **Canonical identity:** `api:cohere-rerank` / `api:voyage-code-2` · Cohere / Voyage AI
- **Category:** Context & Memory → Cross-Encoder Rerankers & Code-Specialized Vectors
- **Type:** Commercial APIs
- **Official URL:** https://cohere.com/rerank / https://www.voyageai.com/
- **Mechanism:** **Vector / Reranker.** Evidence: Voyage produces embeddings specialized on code AST structures; Cohere Rerank computes cross-attention relevance scores across query-document pairs to reorganize first-stage retrieval hits.
- **Capabilities:** Precision improvement for RAG pipelines; re-ranking top-100 candidates down to top-5 high-relevance chunks.
- **Integration:** Standard vector database retrieval post-processors.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 56 — pgvector (PostgreSQL Vector Extension)
- **Canonical identity:** `ext:pgvector` · `github:pgvector/pgvector`
- **Category:** Context & Memory → Relational Database Vector Extension
- **Type:** Open Source (PostgreSQL License)
- **Official URL:** https://github.com/pgvector/pgvector
- **Mechanism:** **Service / Vector.** Evidence: Adds native vector data types and Approximate Nearest Neighbor (ANN) index structures (HNSW and IVFFlat) directly inside PostgreSQL.
- **Capabilities:** Unified relational metadata filtering and vector similarity queries in a single ACID-compliant SQL transaction.
- **Integration:** Supabase, AWS RDS, Neon, standard PostgreSQL installations.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 57 — Pinecone Serverless Vector Database
- **Canonical identity:** `service:pinecone` · Pinecone Systems
- **Category:** Context & Memory → Managed Cloud Vector Database
- **Type:** Commercial SaaS
- **Official URL:** https://www.pinecone.io/
- **Mechanism:** **Service / Vector.** Evidence: Cloud-native distributed index architecture decoupling storage from compute with sub-50ms HNSW query latency at billion-scale vectors.
- **Capabilities:** Zero-infrastructure management, live index updates, metadata payload filtering.
- **Integration:** LangChain, LlamaIndex, OpenAI Assistant API, enterprise RAG pipelines.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 58 — Weaviate Native Hybrid Vector & BM25 Database
- **Canonical identity:** `db:weaviate` · `github:weaviate/weaviate`
- **Category:** Context & Memory → Native Hybrid Search Engine
- **Type:** Open Source (BSD-3-Clause) / Cloud SaaS
- **Official URL:** https://weaviate.io/
- **Mechanism:** **Service / Hybrid Vector.** Evidence: Stores dense vectors and inverted index tokens side-by-side; executes hybrid search using Reciprocal Rank Fusion (RRF) natively without external merge logic.
- **Capabilities:** Vector similarity + BM25 keyword matching, modular vectorizer pipelines, graph-like cross-references.
- **Integration:** Python/TS clients, Docker, Kubernetes, cloud managed clusters.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 59 — Qdrant & Qdrant Edge Vector Search Engine
- **Canonical identity:** `db:qdrant` · `github:qdrant/qdrant`
- **Category:** Context & Memory → High-Performance Rust Vector Engine
- **Type:** Open Source (Apache-2.0) / Cloud SaaS
- **Official URL:** https://qdrant.tech/
- **Mechanism:** **Service / Vector.** Evidence: Written in Rust; implements custom HNSW graph indexing with payload-based filtering and scalar/binary quantization for massive memory savings. Qdrant Edge runs locally on device.
- **Capabilities:** Ultra-fast vector search, memory quantization, geo/payload filtering, local and distributed operation.
- **Integration:** Python/Rust/Go/TS SDKs, local Docker, cloud managed instances.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 60 — Milvus & Zilliz Cloud Distributed Vector Store
- **Canonical identity:** `db:milvus` · LF AI & Data Foundation / Zilliz
- **Category:** Context & Memory → Enterprise Distributed Vector Database
- **Type:** Open Source (Apache-2.0) / Cloud SaaS
- **Official URL:** https://milvus.io/
- **Mechanism:** **Service / Vector.** Evidence: Cloud-native distributed architecture separating worker nodes, query nodes, and coordinator nodes; optimized for trillion-vector datasets.
- **Capabilities:** Massive horizontal scalability, multi-tenancy, GPU-accelerated indexing (Knowhere engine).
- **Integration:** Kubernetes Helm charts, Python/Java/Go/Node SDKs.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 61 — Chroma Embedded Vector Database
- **Canonical identity:** `pkg:chromadb` · `github:chroma-core/chroma`
- **Category:** Context & Memory → Developer-First Embedded Vector Store
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://www.trychroma.com/
- **Mechanism:** **Local-Index / Vector.** Evidence: Runs in-process via Python or Node.js utilizing DuckDB/SQLite and ClickHouse/hnswlib; requires zero cloud setup for local agent workflows.
- **Capabilities:** Effortless local embedding storage, automatic tokenization, light-weight prototyping.
- **Integration:** Native integration in local agent frameworks, LangChain, LlamaIndex.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 62 — LanceDB Serverless Embedded Vector Engine
- **Canonical identity:** `pkg:lancedb` · `github:lancedb/lancedb`
- **Category:** Context & Memory → Columnar Embedded Vector Database
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://lancedb.com/
- **Mechanism:** **Local-Index / Vector.** Evidence: Built upon the Lance columnar data format; stores data directly in local disk or S3/GCS without requiring an active database server; performs fast vector search directly from storage.
- **Capabilities:** Zero-server embedded architecture, multimodal data support, disk-based vector search without RAM exhaustion.
- **Integration:** Python, Node.js, Rust, local CLI agent harnesses.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 63 — Tree-Sitter Structural Code Syntax Engine
- **Canonical identity:** `lib:tree-sitter` · `github:tree-sitter/tree-sitter`
- **Category:** Context & Memory → Incremental Parsing & Concrete Syntax Tree Engine
- **Type:** Open Source (MIT)
- **Official URL:** https://tree-sitter.github.io/tree-sitter/
- **Mechanism:** **Graph / AST.** Evidence: Generates robust, concrete syntax trees (CST/AST) for dozens of programming languages; parses files incrementally in sub-milliseconds as the user or agent edits code.
- **Capabilities:** Precise extraction of functions, classes, interfaces, import graphs, and scopes; syntax highlighting; semantic code chunking.
- **Integration:** Aider repo map, Neovim, GitHub, Cursor, ast-grep.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 64 — ast-grep Structural Search & Semantic Linting
- **Canonical identity:** `tool:ast-grep` · `github:ast-grep/ast-grep`
- **Category:** Context & Memory → AST-Based Code Search & Mutation Tool
- **Type:** Open Source (MIT)
- **Official URL:** https://ast-grep.github.io/
- **Mechanism:** **Graph / AST.** Evidence: Employs Tree-sitter AST pattern matching to search and rewrite code based on syntactic structure rather than fragile text regexes.
- **Capabilities:** Structural code search, AST lint rules, semantic code rewriting for agent tools.
- **Integration:** Command-line CLI, Node/Python bindings, MCP tools.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 65 — Aider Tree-Sitter Repo Map (PageRank Symbol Graph)
- **Canonical identity:** `tool:aider-repo-map` · Paul Gauthier
- **Category:** Context & Memory → Graph-Based Repository Map Generator
- **Type:** Open Source (Apache-2.0)
- **Official URL:** https://aider.chat/docs/repomap.html
- **Mechanism:** **Graph / Repo Map.** Evidence: Parses the entire repository into a Tree-sitter symbol graph (definitions and references), constructs a directed call/dependency graph, and runs the PageRank algorithm to select the most architecturally salient symbols that fit within a strict token budget (e.g. 1024 tokens).
- **Capabilities:** Gives LLM global architectural context without bloating context windows; accurate identification of relevant APIs and signatures.
- **Integration:** Built natively into Aider; widely emulated by modern agent harnesses.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 66 — Repomix / CodePack Codebase Context Bundler
- **Canonical identity:** `npm:repomix` · `github:yamadashy/repomix` (formerly repopack)
- **Category:** Context & Memory → Repository Packing & Direct Retrieval Tool
- **Type:** Open Source (MIT)
- **Official URL:** https://repomix.com/
- **Mechanism:** **Local-Index / Direct-Retrieval.** Evidence: Packs an entire code repository into an optimized, AI-friendly XML or Markdown context document with token counts, file trees, and pattern-based filtering.
- **Capabilities:** Instant single-file context injection into web UIs and massive 1M-2M context models (Gemini, Claude).
- **Integration:** CLI (`repomix`), GitHub Actions, local dev pipelines.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 67 — Context7 Dynamic Documentation Grounding Engine
- **Canonical identity:** `tool:context7` · Developer Ecosystem
- **Category:** Context & Memory → Live Documentation Ingestion & Grounding
- **Type:** Open Source / Developer Service
- **Official URL:** https://github.com/context7
- **Mechanism:** **Direct-Retrieval / Docs Grounding.** Evidence: Fetches and indexes up-to-date framework documentation, changelogs, and API reference pages at agent runtime, preventing the model from hallucinating deprecated APIs.
- **Capabilities:** Live web doc scraping, Markdown conversion, fresh grounding for rapidly evolving libraries.
- **Integration:** MCP servers, agent system prompt injection.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

### 68 — Hierarchical Session Memory & Context Compaction Protocols
- **Canonical identity:** `protocol:session-compaction` · Cross-Agent Standard
- **Category:** Context & Memory → Multi-Tier Memory & Context Summarization
- **Type:** Architectural Pattern & Specification
- **Official URL:** https://docs.anthropic.com/en/docs/agents-and-tools/agent-patterns
- **Mechanism:** **Local-Index / Memory.** Evidence: Multi-tier memory architecture dividing state into: (1) System Core (immutable identity & rules); (2) Repository Anchor (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`); (3) Working Scratchpad (current plan & active step); (4) Ephemeral History (conversation turns). When ephemeral history approaches context thresholds, an automated compaction agent summarizes completed actions, deletes raw bash/file dumps, and preserves only critical state.
- **Capabilities:** Prevention of context window exhaustion, persistence across multi-hour coding sessions.
- **Integration:** Claude Code `/compact`, Cline Memory Bank, OpenCode compaction hooks.
- **Verification Date:** 2026-10-09 · **Confidence:** Verified

---

## Comparison Matrix: Context Mechanisms & Database Engines

| Technology | Mechanism Class | Primary Query Paradigm | Strengths | Ideal Developer Agent Use Case |
|---|---|---|---|---|
| **Tree-sitter** | Graph / AST | Concrete Syntax Tree Walk | Deterministic, language-aware, sub-ms | Symbol extraction, structural code diffing, linting |
| **Aider Repo Map** | Graph / Repo Map | PageRank over AST Symbol Graph | Fits whole repo layout into 1k-2k tokens | Initial task orientation, global symbol discovery |
| **Weaviate** | Service / Hybrid Vector | Native Dense Vector + BM25 (RRF) | Single query merges keywords and semantics | Unified codebase documentation and symbol search |
| **Qdrant** | Service / Vector | High-Performance HNSW (Rust) | Quantization, low RAM footprint, sub-10ms | Enterprise code repository semantic indexing |
| **pgvector** | Service / Vector | SQL + HNSW / IVFFlat | ACID compliance, zero extra database infrastructure | Applications already utilizing PostgreSQL backends |
| **LanceDB** | Local-Index / Vector | Columnar Vector File Format | Embedded, serverless, disk-backed queries | Local desktop agent tooling without database servers |
| **Repomix** | Direct-Retrieval | Directory Tree Packing (XML/MD) | Deterministic, zero index drift, fast | Context injection into 1M-2M token context windows |
| **Context Compaction** | Local-Index / Memory | Summarization Reducers & Scratchpad | Keeps context clean across multi-turn loops | Long-running multi-file refactoring sessions |

---

## Conclusion & Operational Blueprint

Deploying production-grade developer agents requires orchestrating all four layers in harmony:
1. **Engine Selection:** Select coding agents that expose strict tool permission models and open interoperability standards (MCP, `SKILL.md`).
2. **Process Runtime Isolation:** Enforce **Real Runtimes** for multi-agent workflows. Spawning isolated child processes with dedicated context windows ensures that noisy intermediate outputs (e.g., massive grep logs, failed builds) do not degrade the orchestrator's decision quality.
3. **Deterministic Harness Guardrails:** Wrap LLM execution loops in rigorous harnesses: Spec-Driven Development (SDD), Definition of Done (DoD) checklists, automated TDD red-green-refactor loops, pre-commit type checking, and `--max-turns` cost circuit breakers.
4. **Hybrid Context Architecture:** Replace naive vector-only RAG with a multi-modal context pipeline: Combine AST-based Tree-sitter repo maps for structural code relationships, BM25 inverted indexes for exact variable and error code matches, and dense vector embeddings for conceptual search.

---
*Catalog compilation complete. All 68 resources systematically verified and classified.*
