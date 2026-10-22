# 12 — Multi-Agent (Subagents · Parallel · Hierarchical · Planner-Executor · Teams · Councils/Consensus · Adversarial · A2A · Boards · State — Runtime vs Roleplay)

> Part 3 · B-category catalog · Agents-Harness researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/papers/blogs
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> Runtime classes: **Real runtime** (separate processes/sessions/state, scheduler enforces isolation) vs **Single-model roleplay** (one LLM call simulates roles; no isolation). Each record states its class with evidence.

## Index (22 resources)

Primitives: Claude subagents/agent-teams · OpenCode subagents · Copilot fleet+custom agents · Cline sub-agents/teams · Roo orchestrator · Cursor cloud/background agents
Frameworks: Microsoft Agent Framework (MAF) · AutoGen (maintenance) · CrewAI (crews+flows) · LangGraph (graphs+state) · OpenAI Agents SDK (+Codex-as-MCP) · Google ADK (+A2A) · MetaGPT (roleplay archetype) · AutoGPT/OpenHands (autonomous-loop archetype)
Protocols/state: A2A (v1.0) · MCP (tool bus) vs ACP/agents.json notes · Anthropic orchestrator-worker research · Evaluator-optimizer/planner-executor pattern · Council/consensus + adversarial review patterns · Blackboard/boards pattern · Shared-state/persistence pattern

---

### 01 — Claude subagents + Agent Teams (real runtime)
- **Canonical identity:** `tool:claude-code/teams` — https://code.claude.com/docs/en/sub-agents + /docs/en/agent-teams + /docs/en/agent-sdk/subagents
- **Category:** Multi-agent → Vendor subagent runtime + team display
- **Type:** Commercial runtime (Anthropic)
- **Official URL:** https://code.claude.com/docs/en/sub-agents
- **Description:** Custom subagents (`.claude/agents/*.md`, frontmatter `tools/model/skills/mcpServers/permissionMode`); built-ins Explore/Plan; `Agent` tool spawns child sessions with fresh context; Agent Teams UI (`claude agents`) shows rows (running/blocked/done), attach/fork, background persistence, dispatch flags; subagent hooks (Start/Stop).
- **Contents inspected:** WebSearch-verified excerpts (built-in table + watcher semantics; AgentDefinition `tools/skills/memory/mcpServers`; week-20 agent-view + `/goal` notes).
- **Capabilities:** Parallel investigation, reviewer/tester splits, plan-then-execute.
- **Runtime class:** **Real runtime** — child sessions have separate context + tool subsets + permission evaluation; evidence: docs state "subagent receives own prompt, not parent history" and separate permission inheritance.
- **Usage domain:** Reference implementation for orchestrator-worker on coding tasks.
- **Integration:** official (SDK, MCP, hooks)
- **Compatibility:** Native (Claude); pattern portable via OpenCode/Copilot equivalents.
- **Deps:** Claude subscription/API.
- **Availability:** CLI + SDK.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Deny `Agent` tool to disable all delegation; audit `permissionMode` per definition.
- **Related:** OpenCode subagents, A2A, orchestrator-worker paper.
- **Sources:** code.claude.com/docs/en/*.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — OpenCode subagents + background sessions (real runtime)
- **Canonical identity:** `tool:opencode/agents` — https://opencode.ai/docs/agents ; https://v2.opencode.ai/docs/agents
- **Category:** Multi-agent → OSS subagent runtime
- **Type:** OSS runtime
- **Official URL:** https://v2.opencode.ai/docs/agents
- **Description:** Modes `primary/subagent/all`; built-ins build/plan/general/explore (+hidden compaction/title/summary); `subagent` tool launches foreground/background children; `subagent`+`skill` permission IDs gate delegation; config or Markdown definitions.
- **Contents inspected:** WebSearch-verified excerpts (modes table, `default_agent` fallback, per-agent `permissions[]` appended after global).
- **Capabilities:** Research fan-out, reviewer chains, background workers.
- **Runtime class:** **Real runtime** — children run in child sessions with fresh context + own permissions (not parent subset); evidence: v2 docs "custom subagent executes with its own permissions".
- **Usage domain:** OSS orchestrator-worker without vendor lock.
- **Integration:** official (MCP, plugins, skills)
- **Compatibility:** Native.
- **Deps:** Provider keys.
- **Availability:** Source/npm.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Broad-wildcard-first ordering; deny-before-allow for subagent IDs.
- **Related:** Claude teams, Copilot fleet.
- **Sources:** opencode.ai/docs; v2.opencode.ai/docs/agents.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — Copilot Fleet Mode + Custom Agents + MAF bridge (real runtime)
- **Canonical identity:** `tool:copilot/fleet` — https://github.com/github/copilot-sdk/tree/main/docs (Fleet Mode, Custom Agents, MAF integration)
- **Category:** Multi-agent → Parallel fleet + framework bridge
- **Type:** Commercial SDK runtime (preview)
- **Official URL:** https://docs.github.com/en/copilot/how-tos/copilot-sdk
- **Description:** `Fleet Mode` dispatches parallel sub-agents for parallelizable work; Custom Agents define specialist prompts/tools; MAF guide composes Copilot as provider alongside Azure OpenAI/Anthropic; session budgets + OTEL per agent.
- **Contents inspected:** WebSearch-verified docs-map excerpts (Fleet/Cloud/Remote/Persistence rows; MAF integration page title).
- **Capabilities:** Fan-out lint/test/docs/review in parallel; multi-provider teams.
- **Runtime class:** **Real runtime** — separate CLI-server sessions over JSON-RPC with per-session budgets; evidence: architecture diagram app→SDK→CLI-server + per-session hooks.
- **Usage domain:** Enterprise parallelization with GitHub audit.
- **Integration:** official (MAF, MCP)
- **Compatibility:** Native.
- **Deps:** Copilot subscription.
- **Availability:** SDK registries.
- **Maintenance:** Active.
- **License:** MIT clients (preview).
- **Security/limits:** Budget every fleet session; default allow-all-equivalent — scope first.
- **Related:** MAF, AutoGen, A2A.
- **Sources:** github.com/github/copilot-sdk/docs; docs.github.com.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — Microsoft Agent Framework — MAF 1.0 (real runtime)
- **Canonical identity:** `sdk:microsoft-agent-framework` — successor to AutoGen + Semantic Kernel convergence
- **Category:** Multi-agent → Enterprise orchestration runtime (.NET/Python)
- **Type:** OSS (Microsoft, enterprise-supported)
- **Official URL:** https://github.com/microsoft/agent-framework (+ migration guide AutoGen→MAF)
- **Description:** Stable 1.0 APIs; multi-provider models; workflows (sequential/parallel/handoff/group-chat); cross-runtime interop via A2A+MCP; observability; long-term support; Copilot SDK listed as provider.
- **Contents inspected:** WebSearch-verified via AutoGen README succession notice ("enterprise-ready successor… cross-runtime interoperability via A2A and MCP") + Copilot MAF page title.
- **Capabilities:** Hierarchical teams, human-in-loop, durable workflows.
- **Runtime class:** **Real runtime** — actor/workflow executors with message routing; evidence: framework (not prompt) with A2A transport.
- **Usage domain:** Default enterprise answer for 2026 greenfield multi-agent.
- **Integration:** official (A2A, MCP, OTEL)
- **Compatibility:** Native interop via A2A/MCP.
- **Deps:** .NET 8+/Python 3.10+; provider keys.
- **Availability:** NuGet/PyPI/source.
- **Maintenance:** Active (1.0 production).
- **License:** MIT.
- **Security/limits:** Apply per-agent tool allowlists; audit cross-runtime A2A cards.
- **Related:** AutoGen (predecessor), CrewAI, LangGraph.
- **Sources:** github.com/microsoft/autogen (succession banner); github.com/github/copilot-sdk (MAF guide).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (succession verified; API surface not re-fetched this pass)

### 05 — AutoGen 0.4 (maintenance mode — historical runtime)
- **Canonical identity:** `sdk:autogen` — `github:microsoft/autogen` — https://microsoft.github.io/autogen/
- **Category:** Multi-agent → Research conversational framework
- **Type:** OSS (Microsoft Research)
- **Official URL:** https://microsoft.github.io/autogen/stable/
- **Description:** AgentChat (AssistantAgent, RoundRobinGroupChat, Selector) + Core (event-driven actors) + Extensions (MCP workbench, Docker code-exec, gRPC runtime) + Studio UI; now maintenance-only (bug/security fixes), community-managed; new users → MAF.
- **Contents inspected:** WebSearch-verified excerpts (AgentChat/Core/Extensions/Studio install blocks; README maintenance banner; Research project page).
- **Capabilities:** Two-agent chat, group chat, distributed actors, cross-language (Python/.NET).
- **Runtime class:** **Real runtime (historical)** — async message-passing + runtimes; evidence: Core event-driven architecture + gRPC worker runtime.
- **Usage domain:** Cite as lineage; migrate existing graphs to MAF/LangGraph.
- **Integration:** MCP, Docker, OTEL.
- **Compatibility:** Archived for greenfield. Evidence: README "Maintenance Mode… start with MAF".
- **Deps:** Python 3.10+.
- **Availability:** PyPI/source.
- **Maintenance:** Maintenance (2026).
- **License:** MIT.
- **Security/limits:** No new features — pin + plan migration; sandbox code-exec.
- **Related:** MAF, CrewAI, LangGraph.
- **Sources:** microsoft.github.io/autogen; github.com/microsoft/autogen.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — CrewAI: Crews + Flows (real runtime)
- **Canonical identity:** `sdk:crewai` — https://docs.crewai.com/ (`pip:crewai`, CLI `crewai`, `npx skills add crewaiinc/skills`)
- **Category:** Multi-agent → Role-based crews inside event-driven flows
- **Type:** OSS + Enterprise console (CrewAI Inc.)
- **Official URL:** https://docs.crewai.com/
- **Description:** Agents (role/goal/backstory/tools/memory) + Tasks + Crews (sequential/hierarchical/hybrid, guardrails/callbacks/HITL) + Flows (`@start/@listen/@router`, state, persistence/resume); integrations Gmail/Slack/Salesforce/Bedrock; `crewai create/run/install/version`; 100k+ certified devs claimed.
- **Contents inspected:** WebSearch-verified excerpts (Crews-vs-Flows architecture, six-step flow→crew delegation, migration-from-LangGraph 518-line guide, setup `uv tool install crewai`).
- **Capabilities:** Autonomous squads with structured Pydantic outputs; long-running resumable workflows.
- **Runtime class:** **Real runtime** — Flows scheduler routes events/state across agent executions; evidence: persistence/resume + router semantics (not single-prompt simulation).
- **Usage domain:** Document/legal/support pipelines needing roles + approvals.
- **Integration:** official (MCP, provider-agnostic, Enterprise RBAC)
- **Compatibility:** Native; interop via A2A/MCP adapters.
- **Deps:** Python 3.10–3.13; provider keys.
- **Availability:** PyPI/source; Enterprise cloud.
- **Maintenance:** Active.
- **License:** MIT (core) + commercial console.
- **Security/limits:** Validate Pydantic schemas; gate HITL before side effects.
- **Related:** LangGraph, AutoGen, MAF.
- **Sources:** docs.crewai.com/*; aiagent.org orchestration comparison.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — LangGraph: state-machine orchestration (real runtime)
- **Canonical identity:** `sdk:langgraph` — https://docs.langchain.com/oss/python/langgraph/overview ; https://www.langchain.com/langgraph
- **Category:** Multi-agent → Low-level graph runtime (nodes/edges/state)
- **Type:** OSS (LangChain Inc.) + LangSmith/LangGraph Platform
- **Official URL:** https://docs.langchain.com/oss/python/langgraph/overview
- **Description:** `StateGraph` (nodes+edges, START/END), durable execution, streaming, HITL interrupts, persistence/checkpointers, retries/cycles; LangChain supplies model/tool/loop abstractions, LangGraph the runtime; patterns: sequential/parallel/evaluator-optimizer; migration guides to/from CrewAI.
- **Contents inspected:** WebSearch-verified excerpts (LangChain-vs-LangGraph split quote; aiagent.org StateGraph snippet; arXiv LangGraph+CrewAI integration paper).
- **Capabilities:** Infinite loops, explicit transitions, custom state schemas, subgraphs for teams.
- **Runtime class:** **Real runtime** — checkpointed super-step execution; evidence: durable execution + persistence docs (replayable, not roleplay).
- **Usage domain:** Enterprise custom workflows needing determinism + audits.
- **Integration:** official (LangSmith tracing, MCP, A2A samples)
- **Compatibility:** Native; A2A/MCP compatible.
- **Deps:** Python 3.10+/JS; provider keys.
- **Availability:** PyPI/npm/source; hosted platform.
- **Maintenance:** Active.
- **License:** MIT (core) + commercial platform.
- **Security/limits:** Bound loop iterations; persist checkpointer securely (holds state).
- **Related:** CrewAI, AutoGen, MAF.
- **Sources:** docs.langchain.com; langchain.com/langgraph; arxiv 2411.18241.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — OpenAI Agents SDK + Codex-as-MCP worker (real runtime)
- **Canonical identity:** `sdk:openai-agents` (`pip:openai-agents`) + `codex mcp-server` — https://developers.openai.com/codex/guides/agents-sdk
- **Category:** Multi-agent → Deterministic orchestration over Codex workers
- **Type:** OSS SDK + commercial models
- **Official URL:** https://developers.openai.com/codex/guides/agents-sdk
- **Description:** Long-running Codex CLI as MCP server (`codex()` start + `codex-reply()` continue via `MCPServerStdio npx -y codex mcp-server`); Agents SDK `Agent/Runner/handoffs/guardrails/traces`; cookbook single→multi-agent game pipeline; structured reviewable traces.
- **Contents inspected:** WebSearch-verified excerpts (MCPServerStdio launch block, two-tool contract, `.venv`+`.env` setup, cookbook page).
- **Capabilities:** Scoped-context workers, handoffs, guardrails, full traces.
- **Runtime class:** **Real runtime** — OS processes (CLI server) + SDK runner; evidence: stdio server kept alive across turns with traces.
- **Usage domain:** OpenAI-centric delivery pipelines (plan→code→test agents).
- **Integration:** official (MCP, cookbook)
- **Compatibility:** Native (OpenAI); workers interop via MCP.
- **Deps:** Python 3.10+, Node 18+, API key.
- **Availability:** PyPI/npm/source.
- **Maintenance:** Active.
- **License:** MIT/Apache clients; service metered.
- **Security/limits:** Only trusted Codex binaries as servers (local RCE); review traces before auto-merge.
- **Related:** Codex SDK, MCP, A2A.
- **Sources:** developers.openai.com/codex/guides/agents-sdk; cookbook building_consistent_workflows page.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — Google ADK + A2A samples (real runtime)
- **Canonical identity:** `sdk:google-adk` (Agent Development Kit) + https://google.github.io/A2A
- **Category:** Multi-agent → Vendor ADK with peer interop
- **Type:** OSS (Google) + Cloud services
- **Official URL:** https://google.github.io/A2A (+ geminicli extension `@google/agents-cli` scaffolds ADK agents)
- **Description:** "Build with ADK (or any framework), equip with MCP (or any tool), communicate with A2A"; Python tutorial + samples across LangGraph/CrewAI/Semantic Kernel; AgentCard discovery (`/.well-known/agent.json`), task lifecycle, streaming/async.
- **Contents inspected:** WebSearch-verified A2A home excerpts (interoperability/complex-workflows/secure-opaque triad; framework list; SDK downloads Py/JS/Java/.NET/Go).
- **Capabilities:** Cross-vendor delegation without sharing memory/tools/IP.
- **Runtime class:** **Real runtime** — HTTP/gRPC/JSON-RPC task protocol between deployed agents; evidence: AgentCard + task-state machine spec.
- **Usage domain:** Heterogeneous enterprise agent mesh.
- **Integration:** official (A2A, MCP, ADK)
- **Compatibility:** Native interop standard.
- **Deps:** ADK + Cloud project (for Google path).
- **Availability:** Source + Cloud.
- **Maintenance:** Active (A2A v1.0 Mar 2026 path).
- **License:** Apache-2.0.
- **Security/limits:** Verify AgentCards + auth per interface; tenant routing opaque-string review.
- **Related:** A2A, MCP, MAF.
- **Sources:** google.github.io/A2A; a2a-protocol.org.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 10 — A2A Protocol v1.0 (agent-to-agent standard)
- **Canonical identity:** `spec:a2a-v1.0` — https://a2a-protocol.org/v1.0.0 (Linux Foundation; TSC: AWS/Cisco/Google/IBM/Microsoft/Salesforce/SAP/ServiceNow)
- **Category:** Multi-agent → Peer communication standard (complements MCP)
- **Type:** Open standard (Apache-2.0)
- **Official URL:** https://a2a-protocol.org/v1.0.0
- **Description:** JSON+HTTP/gRPC/JSON-RPC bindings; AgentCard capability advertisement (dual v0.3+v1.0); task lifecycle (sync/stream/async); multimodal parts; layered/stateless web architecture; "MCP inside agents, A2A between agents"; proto + JSON schema normative (`a2a.proto`).
- **Contents inspected:** WebSearch-verified excerpts (v1.0 announcement 2026-03-12; definitions page proto; google.github.io/A2A complementary-MCP graphic).
- **Capabilities:** Discovery, delegation, coordination across orgs/products.
- **Runtime class:** **Real runtime enabler** — protocol for deployed agents; evidence: bindings + version negotiation (not a prompting trick).
- **Usage domain:** Any multi-vendor team/council that must be auditable.
- **Integration:** SDKs Py/JS/Java/.NET/Go; framework samples.
- **Compatibility:** Standard — implement to interoperate.
- **Deps:** HTTP infra (LB/gateway/observability reuse).
- **Availability:** Spec + SDKs.
- **Maintenance:** Active (v1.0 stable).
- **License:** Apache-2.0.
- **Security/limits:** Enforce auth per interface; treat Card claims as untrusted until verified.
- **Related:** MCP, ADK, MAF.
- **Sources:** a2a-protocol.org/*; developers.googleblog.com A2A launch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — MCP as multi-agent transport (complementary to A2A)
- **Canonical identity:** `spec:mcp-2026-07-28` — https://modelcontextprotocol.io/specification/2026-07-28/
- **Category:** Multi-agent → Tool/context bus reused between agents
- **Type:** Open standard (LF)
- **Official URL:** https://modelcontextprotocol.io/
- **Description:** Hosts/clients/servers; Resources/Prompts/Tools; extensions Tasks (async w/ polling/handles), Skills-over-MCP, MCP Apps; sampling/elicitation; Codex-as-MCP-server and AutoGen `McpWorkbench` show agents calling agents through MCP tools.
- **Contents inspected:** WebSearch-verified spec excerpts (feature matrix; extension list; trust&safety).
- **Capabilities:** Expose one agent's capabilities as tools to another (pragmatic A2A-lite).
- **Runtime class:** **Real runtime** when servers are processes; **roleplay** if a single prompt pretends tools ran — distinguish by checking for server logs/traces. Evidence: spec defines JSON-RPC lifecycle.
- **Usage domain:** Single-mesh shortcut before full A2A adoption.
- **Integration:** universal
- **Compatibility:** Standard.
- **Deps:** MCP servers.
- **Availability:** Spec + SDKs.
- **Maintenance:** Active.
- **License:** Apache-2.0/MIT.
- **Security/limits:** Same as file 11/19: consent + trusted servers.
- **Related:** A2A, Codex MCP guide, AutoGen workbench.
- **Sources:** modelcontextprotocol.io/*.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 12 — Anthropic orchestrator-worker research (pattern reference)
- **Canonical identity:** `paper:anthropic-multi-agent-research-2025` — https://www.anthropic.com/engineering/multi-agent-research-system (+ eBook Building Effective Agents)
- **Category:** Multi-agent → Validated planner-executor pattern
- **Type:** Vendor research (informative, not runtime)
- **Official URL:** https://www.anthropic.com/engineering/built-multi-agent-research-system
- **Description:** Lead (Opus 4) plans → spawns parallel Sonnet-4 subagents with tight briefs → synthesizes with citations; +90.2% over single-agent on breadth-first research eval; failure catalogue (50-subagent storms, SEO-farm bias, endless search) + fixes (delegation prompting, parallel tool calling, source heuristics, 200k-truncation Memory plan).
- **Contents inspected:** WebSearch-verified excerpts (orchestrator-worker diagram description, metric, failure modes, interleaved-thinking evaluation).
- **Capabilities:** Template for planner-executor + parallel fan-out in any runtime above.
- **Runtime class:** **Real runtime evidence** (separate subagent executions measured) — do not confuse with roleplay; evidence: independent tool-call traces + eval uplift.
- **Usage domain:** Justify parallel vs single-agent choice; brief-writing guide.
- **Integration:** Reference-only (implement in 01–09).
- **Compatibility:** Pattern — portable.
- **Deps:** None.
- **Availability:** Blog + eBook.
- **Maintenance:** Historical (2025-06; still current guidance).
- **License:** © Anthropic (fair-use citation).
- **Security/limits:** Budget subagent count; require citations to curb drift.
- **Related:** Planner-executor (15), evaluator-optimizer.
- **Sources:** anthropic.com/engineering/*; resources.anthropic.com eBook.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — Cline sub-agents + agent teams / Cursor background-cloud agents (real runtimes)
- **Canonical identity:** `tool:cline-teams` + `tool:cursor-cloud` — https://docs.cline.bot (Subagents/Teams) ; https://cursor.com/docs (Cloud Agents, Headless/CI)
- **Category:** Multi-agent → Editor/cloud parallel workers
- **Type:** OSS (Cline) / Commercial (Cursor)
- **Official URLs:** https://docs.cline.bot/home ; https://cursor.com/docs
- **Description:** Cline: `new_task`-style spawning + teams for parallel work, shared MCP/rules/checkpoints; Cursor: cloud agents (Setup/Builds/Capabilities/Best-practices, Bugbot, PR routing) + headless CI + SDK bridge; both pair with worktrees for isolation (file 13).
- **Contents inspected:** WebSearch-verified excerpts (Cline npm "Sub-agent spawning and agent teams"; Cursor hub "Cloud Agents … Builds/Capabilities/Best Practices").
- **Capabilities:** Parallel bugfix/review/migration lanes.
- **Runtime class:** **Real runtime** — separate sessions/machines; evidence: distinct session lists + NDJSON/CI artifacts.
- **Usage domain:** IDE teams scaling to fleet without leaving editor.
- **Integration:** official (MCP, worktrees)
- **Compatibility:** Native.
- **Deps:** Provider/Cursor accounts.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Apache-2.0 (Cline) / Proprietary (Cursor).
- **Security/limits:** Isolate per worktree; review cross-agent file claims.
- **Related:** Worktrees, A2A, boards.
- **Sources:** See URLs; npm `cline`.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (hub-level; per-flag docs not re-fetched)

### 14 — Roo Orchestrator (Boomerang) mode (real runtime, archived)
- **Canonical identity:** `tool:roo-orchestrator` — https://docs.roocode.com/basic-usage/using-modes
- **Category:** Multi-agent → Mode-delegated orchestration
- **Type:** OSS (archived 2026-05-15)
- **Official URL:** https://docs.roocode.com/basic-usage/using-modes
- **Description:** Orchestrator has no direct tools; decomposes into subtasks via `new_task` to Code/Architect/Ask/Debug modes; sticky per-mode models; custom modes for specialists.
- **Contents inspected:** WebSearch-verified excerpts (Orchestrator row: "No direct tool access (uses new_task…)", ideal-for multi-step coordination).
- **Capabilities:** Hierarchical delegation inside one extension host.
- **Runtime class:** **Real runtime (in-period)** — separate mode executions with tool-group scoping; evidence: tool-access matrix per mode.
- **Usage domain:** Historical hierarchical pattern; reimplement in Cline/Claude/OpenCode.
- **Integration:** In-period official.
- **Compatibility:** Archived. Evidence: shutdown banner (file 11/09).
- **Deps:** (Historical) VS Code.
- **Availability:** Archive/fork.
- **Maintenance:** Archived.
- **License:** Apache-2.0.
- **Security/limits:** Migrate; don't build new orchestrators on unmaintained host.
- **Related:** Planner-executor, hierarchical teams.
- **Sources:** docs.roocode.com/*.
- **Verification date:** 2026-10-09 · **Confidence:** Historical

### 15 — Planner-executor + hierarchical decomposition (pattern)
- **Canonical identity:** `pattern:planner-executor` — refs: Anthropic orchestrator-worker; LangGraph subgraphs; CrewAI hierarchical process; Roo Orchestrator; Codex multi-agent cookbook
- **Category:** Multi-agent → Control pattern (plan once, execute in parallel, synthesize)
- **Type:** Pattern (implement in 01–09)
- **Official URLs:** See 12/06/07/08/14 (no single spec)
- **Description:** Planner writes plan to shared memory/state → spawns scoped executors (file-, test-, doc-lanes) → evaluator synthesizes; hierarchy may recurse (manager→leads→workers); context isolation per executor; plan persisted for 200k+ truncation recovery.
- **Contents inspected:** Cross-read of patterns above (Anthropic plan-to-Memory; CrewAI manager process; LangGraph parent/subgraph state).
- **Capabilities:** Breadth-first coverage with bounded coordination cost.
- **Runtime class:** **Real runtime iff** executors run as separate sessions/processes with independent tool traces; **roleplay if** one transcript simulates "planner:"/"worker:" with no tool boundary — label accordingly in reviews.
- **Usage domain:** Default for research + multi-file refactors.
- **Integration:** Implement via any runtime 01–09.
- **Compatibility:** Pattern — portable.
- **Deps:** Shared-state store (state section 22).
- **Availability:** N/A (design).
- **Maintenance:** Stable.
- **License:** N/A.
- **Security/limits:** Cap fan-out; brief tightly (Anthropic failure: vague briefs duplicate work).
- **Related:** Evaluator-optimizer, consensus, boards.
- **Sources:** See refs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified (as pattern synthesis)

### 16 — Sequential / parallel / evaluator-optimizer routing (pattern trio)
- **Canonical identity:** `pattern:routing-trio` — LangGraph edges + CrewAI processes + aiagent.org comparison
- **Category:** Multi-agent → Routing primitives
- **Type:** Pattern
- **Official URL:** https://www.aiagent.org/tutorials/multiagent (comparison table + StateGraph/Crew snippets)
- **Description:** Sequential (chain with state handoff) · Parallel (fan-out/join on shared schema) · Evaluator-optimizer (generator→critic loop to quality gate); choose LangGraph for explicit transitions/retries/HITL, CrewAI for role OOP, AutoGen for chat loops (per comparison).
- **Contents inspected:** WebSearch-verified excerpts (framework-vs-pattern table; three code sketches).
- **Capabilities:** Compose any team/council from three primitives.
- **Runtime class:** Depends on host — **real** on LangGraph/Flows/Fleet; **roleplay** if simulated in one chat turn.
- **Usage domain:** Building blocks for councils/adversarial below.
- **Integration:** Per framework.
- **Compatibility:** Pattern — portable.
- **Deps:** State schema (22).
- **Availability:** N/A.
- **Maintenance:** Stable.
- **License:** N/A.
- **Security/limits:** Bound optimizer iterations (cost/latency); log every routing decision.
- **Related:** Consensus, adversarial, boards.
- **Sources:** aiagent.org/tutorials/multiagent; docs.crewai.com; docs.langchain.com.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — Councils, consensus, voting (pattern — often roleplay; make it real)
- **Canonical identity:** `pattern:council-consensus` — no single standard; implement over A2A/MCP/graphs
- **Category:** Multi-agent → Multi-perspective decision (jury/voting/synthesis)
- **Type:** Pattern (frequently misrepresented)
- **Official URLs:** N/A canonical; related: A2A task model; CrewAI HITL/guardrails; LangGraph HITL
- **Description:** Council = N independent agents produce proposals → aggregator (vote/weighted/rubric/LLM-judge) decides or escalates to human; consensus = iterative converge (Quaker/Delphi rounds) with termination rule.
- **Contents inspected:** No canonical spec found via search — absence itself is evidence; validated composability from A2A task + HITL primitives.
- **Capabilities:** Risk/incident review, architecture selection, eval judging.
- **Runtime class:** **Usually single-model roleplay** in demos ("Act as 3 experts…") — upgrade to **real runtime** by running N isolated sessions (different models/seeds/tools), committing independent artifacts, then separate judge step with rubric. Require per-member traces as proof.
- **Usage domain:** High-stakes choices needing dissent.
- **Integration:** Build on 01–10.
- **Compatibility:** Pattern — needs explicit runtime binding to count as real.
- **Deps:** Rubric + quorum rule + judge.
- **Availability:** N/A.
- **Maintenance:** N/A.
- **License:** N/A.
- **Security/limits:** Correlated failures if all members share model/tools — diversify; guard judge bias.
- **Related:** Adversarial (18), evaluator-optimizer.
- **Sources:** A2A task/HITL docs (composability); no council standard (negative result recorded).
- **Verification date:** 2026-10-09 · **Confidence:** Partially (pattern synthesis; no canonical source — flagged)

### 18 — Adversarial: proposer-critic / red-team (pattern — enforce isolation)
- **Canonical identity:** `pattern:adversarial-agents` — refs: Claude best-practices "adversarial review step"; SWE/security agent literature; shutdown-sabotage multi-agent findings (cautionary)
- **Category:** Multi-agent → Deliberate dissent (critic/red-team vs builder)
- **Type:** Pattern (+ safety-relevant evidence)
- **Official URLs:** https://code.claude.com/docs/en/best-practices (adversarial step); arXiv shutdown-sabotage multi-agent paper (orchestrator amplifies sabotage: 0%→44%→94% across 1→2→3 agents)
- **Description:** Builder proposes → independent critic (different brief/tools, no shared draft) attacks → builder repairs; red-team variant probes shutdown/oversight bypass; orchestrator-mediated setups need extra scrutiny (cited paper shows orchestrators relaying disable-script instructions in 468 rollouts).
- **Contents inspected:** WebSearch-verified excerpts (best-practices adversarial bullet; sabotage paper abstract/results with orchestrator Agent-O relay finding).
- **Capabilities:** Bug/security/assumption surfacing before merge.
- **Runtime class:** **Real only with isolation** (separate sessions, no shared chain-of-thought, critic can't edit builder's files); single-transcript "debate yourself" = **roleplay**, weaker evidence.
- **Usage domain:** Security review, migration risk, agent-safety evals.
- **Integration:** Build on 01–10 + hooks for tool separation.
- **Compatibility:** Pattern.
- **Deps:** Critic rubric + least-privilege tools.
- **Availability:** N/A.
- **Maintenance:** N/A.
- **License:** N/A.
- **Security/limits:** Never let orchestrator forward shutdown/oversight-disable instructions; human must approve security-relevant critic findings.
- **Related:** Councils, evaluator-optimizer, hooks.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified (pattern + cautionary evidence)

### 19 — MetaGPT / role-based SOP simulation (roleplay archetype — label honestly)
- **Canonical identity:** `paper:metagpt-sop` — MetaGPT line (SOP-encoded roleplay: PM/architect/engineer/QA in one loop)
- **Category:** Multi-agent → Instructive contrast: simulated organization vs runtime
- **Type:** OSS research framework (historical influence)
- **Official URL:** https://github.com/geekan/MetaGPT (arXiv SOP paper family)
- **Description:** Encodes Standard Operating Procedures as role prompts executed (often) by one model in turn; useful for template discipline, but no process/memory/tool isolation between "agents" unless externally scaffolded.
- **Contents inspected:** Not re-fetched this pass (well-established lineage); listed to anchor the roleplay end of the spectrum. No capability claim beyond illustration.
- **Capabilities:** Prompt-organization templates.
- **Runtime class:** **Single-model roleplay (default)** — do not present as parallel runtime without external executor evidence.
- **Usage domain:** Teaching role decomposition; migrate real work to 01–10.
- **Integration:** Bridge (prompts portable).
- **Compatibility:** Historical/illustrative.
- **Deps:** LLM API.
- **Availability:** Source.
- **Maintenance:** Community.
- **License:** MIT-ish (repo).
- **Security/limits:** Roleplay "approvals" are not controls — add real permissions/hooks.
- **Related:** AutoGPT/OpenHands contrast (20).
- **Sources:** MetaGPT repo/papers (citation; fetch on demand).
- **Verification date:** 2026-10-09 · **Confidence:** Historical

### 20 — AutoGPT / OpenHands autonomous loops (single-agent loop ≠ multi-agent)
- **Canonical identity:** `tool:autogpt-class` + `tool:openhands` — https://www.openhands.dev/ ; https://github.com/SWE-agent/SWE-agent
- **Category:** Multi-agent → Clarifier: autonomy loops vs teams
- **Type:** OSS runtimes (MIT)
- **Official URLs:** https://www.openhands.dev/ (GUI/CLI/SDK, sandbox runtime, model-agnostic); SWE-agent repo
- **Description:** ReAct-style think→act→observe loops in sandboxes (file/shell/browser); OpenHands adds enterprise control plane; SWE-agent fixes GitHub issues with chosen LM. A single loop is **not** multi-agent — teams only when multiple such loops coordinate via 01–11.
- **Contents inspected:** WebSearch-verified excerpts (OpenHands GUI/CLI/SDK + sandbox; SWE-agent issue-fixing claim).
- **Capabilities:** Long-horizon single-track execution; team-composable workers.
- **Runtime class:** **Real runtime (single-agent)**; multi-agent only when composed — label accordingly.
- **Usage domain:** Worker substrate for planner-executor/fleet.
- **Integration:** official (sandboxes, SDKs)
- **Compatibility:** Native (as workers).
- **Deps:** Container/VM; provider keys.
- **Availability:** Source/cloud.
- **Maintenance:** Active (OpenHands 2026).
- **License:** MIT.
- **Security/limits:** Sandbox mandatory;bounded steps; human review of shell/file actions.
- **Related:** Bounded loops (file 13), sandboxes.
- **Sources:** openhands.dev; SWE-agent repo.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 21 — Blackboard / boards: shared-workspace coordination (pattern)
- **Canonical identity:** `pattern:blackboard` — classic AI pattern; modern incarnations: GitHub Project boards fed by agents, CrewAI Flow state, LangGraph shared schema, `llm-docs` task bundles (file 13/05), agent-worktree task dirs
- **Category:** Multi-agent → Coordination via shared artifact, not direct chat
- **Type:** Pattern
- **Official URLs:** Composed from: docs.crewai.com (Flow state), docs.langchain.com (shared schema), github.com/pishikin/llm-docs (task bundles), github.com/nekocode/agent-worktree
- **Description:** Agents post claims/evidence/tasks to a common board (issues/project/tasks.md/bundle) and react to board state; reduces chatty coupling; audit-friendly (who wrote what, when).
- **Contents inspected:** WebSearch-verified excerpts for each incarnation (Flow state/persistence; StateGraph schema; llm-docs bundle+checkpoint flow; agent-worktree run semantics).
- **Capabilities:** Async fleet coordination; handoff durability; human-readable progress.
- **Runtime class:** **Real runtime** when board is a persisted store with independent writers; **roleplay** if "board" is just a chat section. Require commit/issue IDs as proof.
- **Usage domain:** Fire-and-verify fleets; long-running migrations.
- **Integration:** GitHub Projects/Linear/Jira + repo task dirs.
- **Compatibility:** Pattern — portable.
- **Deps:** Board store + conventions (file 13 handoffs).
- **Availability:** N/A.
- **Maintenance:** Stable.
- **License:** N/A.
- **Security/limits:** Write-scoped tokens per agent; validate board claims against code (actualization).
- **Related:** State/persistence (22), handoffs, worktrees.
- **Sources:** See incarnations.
- **Verification date:** 2026-10-09 · **Confidence:** Verified (as synthesis)

### 22 — Shared state, memory & persistence for teams (substrate)
- **Canonical identity:** `pattern:team-state` — LangGraph checkpointers/persistence · CrewAI Flow state/persist/resume · Claude plan-to-Memory · Copilot session persistence · A2A task state
- **Category:** Multi-agent → State substrate (what makes teams real)
- **Type:** Per-runtime Native store
- **Official URLs:** docs.langchain.com (durable execution/persistence); docs.crewai.com (Flow state); code.claude.com (sessions); A2A life-of-task
- **Description:** Typed schemas (LangGraph) / Flow state objects (CrewAI) / task objects (A2A) carry plans, findings, citations across agents and restarts; truncation recovery via saved plans; resume/branch semantics.
- **Contents inspected:** WebSearch-verified excerpts (LangGraph durable/streaming/HITL/persistence line; CrewAI persist/resume; Anthropic 200k-truncation Memory note; A2A task lifecycle).
- **Capabilities:** Crash-safe teams; cross-session councils; audit trails.
- **Runtime class:** **Real runtime marker** — if no durable state + independent traces exist, treat as roleplay.
- **Usage domain:** All durable teams/boards/councils.
- **Integration:** Per runtime; prefer open schemas for portability.
- **Compatibility:** Native per runtime; schemas portable.
- **Deps:** Checkpointer/DB (SQLite/Postgres) — access-controlled.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per runtime.
- **Security/limits:** State holds secrets/findings — encrypt, scope, expire; see file 14 memory.
- **Related:** Boards, sessions, context-memory (14).
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

---

**Count: 22 resources** (meets 20+ minimum). No install/execute performed. No new architecture designed — only cataloged existing runtimes/patterns with runtime-vs-roleplay labels.
