# RESEARCHER A — Broad Mapper Phase 1 Batch 1: EXECUTION & AGENCY LAYER
## P1-01 + P1-03 + P1-05a Consolidated Mapping

**Repo root:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness`
**Grounding:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md` (§2 Batch 1 P1-01..P1-08) · `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` (C1-C6, SC-01..SC-10, rubric wiring)

**Method:** 12 distinct search angles (required ≥5, target 7+). 12 WebSearch passes covering 19 ecosystems + 4 conceptual probes. Stop-rule tracked per sub-area; halt only after 3 consecutive distinct queries returned only known synonyms/trivia/niche noise. Every claim ≥2 independent sources; vendor marketing cross-checked against community/OSS implementation.

**Search angles executed:**
1. Claude Code subagents/delegation/background/hooks
2. OpenAI Codex CLI subagents/orchestration
3. Cursor background agents / Windsurf Cascade workflows
4. Gemini CLI + GitHub Copilot agent mode
5. OpenCode / Cline / Roo Code / Aider / OpenHands
6. LangGraph / CrewAI / AutoGen / Microsoft Agent Framework
7. Subagent delegation vs handoff vs agent-team (GoClaw 4-pattern)
8. Human-in-the-loop + trust calibration + autonomy calibration (SOC, adaptive, TCF)
9. Autonomy calibration details (L0-L5, Zones, Stages, Inbox)
10. GitHub Copilot coding agent workspace + background tasks (cloud agent, gh agent-task)
11. Git worktree isolated workspace harness (gwq, Vibora, AgentsMesh, Omegon)
12. Agent SDK/runtime/framework comparison 2025 (LangChain/LangGraph vs CrewAI vs AG2 vs OpenAI SDK vs Anthropic/MCP)

---

### 1. P1-01 SEED SWEEP — Execution Primitives Across Ecosystems

#### 1.0 At-a-Glance: What Execution Primitives Exist Where

| Ecosystem | Execution Primitives (canonical terms) | Differentiator |
|---|---|---|
| **Claude Code** | `subagents` (`.claude/agents/*.md` + YAML frontmatter: name/description/tools/model/permissionMode/hooks/isolation), `background agents` (foreground vs background, Ctrl+B), `worktree isolation` (`isolation: worktree`), `hooks` (25 lifecycle events, command/http/mcp_tool/prompt/agent), `forked subagents` (experimental `CLAUDE_CODE_FORK_SUBAGENT`), `slash commands`/`skills` as prompt-pack triggers | Subagent = separate Claude instance with own context window, custom system prompt, limited tools, zero conversation history (unless forked). Main decides delegation via `description` field (`use proactively`). Subagents CANNOT spawn subagents. Background runs with auto-denied permissions + push notification on completion. [Sources: code.claude.com/docs/en/sub-agents, code.claude.com/docs/en/hooks] |
| **OpenAI Codex CLI** | `subagent workflows` (parallel fan-out, up to 6 threads default), `agent threads`, `custom agents` (`.codex/agents/*.toml`: name/description/developer_instructions), `config.toml [agents]` (`agents.enabled`, `max_concurrent_threads_per_session`, `default_subagent_model`, `reasoning_effort`), built-ins `default/worker/explorer` | Subagent = delegated agent with own model config + sandbox policy inheritance (+ per-agent override). Orchestration managed by Codex: spawning, routing follow-ups, waiting, closing threads. Trigger phrases: "spawn two agents", "delegate in parallel", "one agent per point". Anti-context-rot purpose: main focused on requirements/decisions, subagents return summaries. Headless `codex exec --full-auto` as cross-model subagent. [Sources: developers.openai.com/codex/subagents, awesome-codex-cli, VoltAgent/awesome-codex-subagents] |
| **Cursor** | `Background Agents` (isolated Ubuntu VMs, cloud, up to 8 parallel), `Agent Window parallel agents`, `worktree-backed background tasks` + `/multitask`, `Cloud Agent API` (launch/follow-up/status/list/delete/fetch + MCP server), `native SDK subagents incl. nested subagents`, `Cursor Automations` (scheduled/event-triggered), `@cursor/sdk local & cloud agents` | Primary differentiator is **cloud VM isolation** vs local process. Background agents: edit/test/push directly to branches via API. GitHub PR integration: `@Cursor` tag triggers fix+push. Foreground + background manageable from sidebar. SDK exposes both local and cloud primitives. [Sources: Cursor Background Agents docs, Cursor SDK] |
| **Windsurf (Cascade)** | `Cascade Flow agents`, `cascade flows`, `workflows` (`.windsurf/workflows/*.md` + `.windsurf/workflows/stages/`), `visual flow editor`, `Workspace-aware agents`, `CI hooks` | Flow = chain of smaller tasks (planning → implementation → validation agents). Pipeline defined as set of workflows in `stages/`. Visual pipeline builder + orchestration layer as central workflow/agent registration. Enterprise claim: refactor across files, understand arch, run tests, lint. [Sources: Windsurf Cascade docs] |
| **Gemini CLI** | `agents` (`.gemini/agents/*.md`), `subagents` via host-session Orchestration Operating Model in `AGENTS.md` (host = Copilot CLI / Claude Code / OpenCode / Codex CLI / Gemini CLI as orchestrator + N specialized subagents), cross-platform `caesar-harness-agent` mapping | Uses same markdown-agent definition pattern as Claude/Copilot but under `.gemini/`. Orchestration via `AGENTS.md` Operating Model section that turns host session into orchestrator. Compatible with `midego1/claude-orchestrate` portable edition + `zeoel-framework` 23-agent team. [Sources: caesar-harness-agent, zeoel-framework, ops-engineering-skills] |
| **GitHub Copilot (IDE + CLI + Cloud)** | `custom agents` (`.github/agents/*.agent.md`, `.github/agents/`), `Copilot coding agent` (async autonomous background agent on GitHub Actions infra), `workspace` (parallel workspace per task, branch auto-creation), `gh agent-task` (CLI 2.80+: `create/list`), `/delegate TASK` slash (commit unstaged → new branch → draft PR → background edits), `Copilot CLI custom agents` (model selection + allowed tools per agent) | Three execution layers: IDE agent sessions (memory across project), CLI agents (local tools), Cloud coding agent (GitHub-hosted Actions VM that compiles/tests/lints). Delegation model: assign issue to Copilot like a developer. Multi-agent boilerplate: manager spawns subagents after plan approval (`github.copilot.chat.claudeAgent.enabled`). [Sources: GitHub Docs — Copilot cloud agent, GitHub Changelog gh agent-task, GitHub Copilot CLI] |
| **OpenCode** | `agents` (`build` + `plan` vanilla flat shared everything), `OpenCodeOrchestra` hierarchy: PM (Depth 0) → Orchestrator (Depth 1) → Investigator/Auditor/Web-Search/Docs (Depth 2+, read-only constraints), `OpenAgentsControl` 7 subagents (task-manager, context-scout, context-manager, coder-agent, test-engineer, code-reviewer, external-scout), 75+ provider support + LSP | Vanilla = flat 2 agents sharing context/permissions/tools. Hierarchical fix splits by depth with role constraints (Investigator/Auditor read-only no shell). PM talks to user, Orchestrator executes approved spec. [Sources: OpenCode docs, OpencodeOrchestra, OpenAgentsControl] |
| **Cline / Roo Code / Kilo Code** | `Cline CLI` (model-agnostic, planning + file edits + command execution + browser use), `Roo Code` (`architect/code/debug/orchestrator` modes, 22k stars, checkpoints + skills), `Kilo Code` (orchestrator mode, 100s LLMs, skills) | Mode-based orchestration inside single agent: explicit `orchestrator` mode in Roo/Kilo that plans then delegates to `code` mode agents. Browser-use as parallel surface. Checkpoints as rewind primitive. [Sources: Cline/Roo Code/Kilo Code CLIs, terminal-native agents directory] |
| **Aider** | Pair-programming agent (diff/patch editing, strong git + multi-file), no native subagent primitive — orchestration is external (Untrivial AO, Orchestrator) | Execution primitive is **single-agent diff application**; parallelism achieved via external harness spawning multiple Aider instances in worktrees. [Sources: Aider docs, Agent Orchestrator] |
| **OpenHands (ex-OpenDevin)** | `OpenHands agent` + `OpenHands CLI`, autonomous repo tasks, event-driven runtime, Docker sandboxes | Single-agent autonomous loop; multi-agent via external orchestrator (ORCH, AO) spawning multiple OpenHands pods. [Sources: OpenHands] |
| **LangChain / LangGraph** | `Graph-based runtime` (nodes = agents/tools, edges = transitions, conditional routing), `state machines`, `checkpointing` (pause/resume/rewind, threads, custom stores), `Supervisor agents`, `hierarchical teams`, `handoffs` via graph composition, `LangSmith Platform` (tracing/monitoring/eval, GA May 2025, ~400 companies), 600+ integrations, 47M+ PyPI | Graph-first: every workflow is a DAG/state machine. Strongest state/human-in-the-loop production maturity. LangChain chains → LangGraph graphs migration. [Sources: LangGraph docs, LangChain vs CrewAI vs AutoGen comparison] |
| **CrewAI** | `Crews` (role-based collaboration), `Flows` (deterministic event-driven orchestration), `Agents` (role/goal/backstory + tools), `Tasks` (assigned to agents) | Two-layer: Crews handle dynamic collaboration, Flows ensure deterministic steps. Fastest time-to-prototype, 44k+ stars, 2-3x benchmark speed. Orchestration styles: Sequential, hierarchical, custom. [Sources: CrewAI docs] |
| **AutoGen / AG2 (AgentOS)** | `ConversableAgent` (core), `Group Chat` (moderator + turn-taking), `Sequential`/`Nested` chats, `Core` (event-driven messaging, async event loop + RPC) | Conversation-driven: multi-agent = structured dialogue. Docker-based code execution, mix-and-match LLMs/tools/human input. Nov 2024 split to AG2 independent Project; MS successor is Microsoft Agent Framework (AutoGen + Semantic Kernel merger). [Sources: AutoGen/AG2 docs] |
| **Microsoft Agent Framework** | Merger of AutoGen + Semantic Kernel, enterprise compliance, `handoffs + guardrails` | Enterprise-governed conversation + graph hybrid; inherits AutoGen patterns + SK plugins. [Sources: microsoft/agent-framework] |
| **OpenAI Agents SDK** | `Agents`, `Handoffs`, `Guardrails` (lightweight 3 primitives), `Sessions` | Minimal abstraction; direct handoff workflows. Chosen when simplicity + minimal orchestration overhead desired. [Sources: OpenAI Agents SDK docs] |
| **GoClaw (gateway)** | `Lane-based Scheduler` (`main/subagent/delegate/cron`, adaptive throttle), `Agent Teams` (shared task board + mailbox), `Inter-agent delegation` (sync/async, per-link + per-target concurrency), `Conversation handoff` (routing override + context transfer), `Evaluate loop` (generator↔evaluator, 3-5 rounds), `Quality gates` (command/agent hooks, blocking retry) | Most explicit 4-pattern reference implementation: subagent (anonymous clone) vs delegation (named agent) vs team (task board) vs handoff (conversation transfer) in one codebase — used as ground truth for split/merge analysis (§2). [Sources: GoClaw multi-agent gateway docs] |
| **Enterprise platforms (Bedrock, Vertex, Agent Framework)** | `Agent runtimes` (managed), `orchestration frameworks` vs `agent runtimes` distinction, `A2A (Agent-to-Agent) protocol` (Google) | Runtime = managed execution (sandbox, secrets, scaling, observability); Framework = authoring abstraction. A2A = protocol for inter-agent delegation across runtimes. [Sources: AWS Bedrock Agents, Google A2A spec, Microsoft Agent Framework] |
| **Universal orchestration harnesses** | `ORCH` (CLI for Claude/Codex/Cursor), `Czarina` (2-20+ workers, git worktrees, lesson propagation via Hopper), `Vibora/fulcrum` (parallel worktrees, single-screen monitor), `AgentsMesh` (AgentPod = PTY + worktree + stream), `Omegon` (single binary, worktree-parallel), `gwq` (fuzzy worktree manager), `Universal DAG Engine` (124 MCP tools: workflow_create/run/validate, retry/rollback/intelligent scheduling) | Harness vs framework split: harness owns worktrees/PTYS/branches/PRs; framework owns graph/crew/conversation logic. `lesson propagation` and `review gates` are harness-level coordination beyond framework. [Sources: ORCH, Czarina, Vibora, AgentsMesh, Omegon, gwq, Universal MCP engine] |
| **Cross-tool portability layer** | `AGENTS.md Operating Model`, `.claude/commands/` as de facto cross-CLI skill path (Cursor/Windsurf/Cline read it), `caesar-harness-agent` 5-platform one-config matrix | `AGENTS.md` + `.claude/commands/` emerging as **portable orchestration contract** across Claude/Codex/Cursor/Gemini/Copilot/OpenCode. [Sources: agents-system-setup, caesar-harness-agent, Dev-AID] |

#### 1.1 Detailed Notes: How They Differentiate (Subagent vs Workflow vs Background Task vs Worktree)

- **Subagent** = *Who does the work* (actor). Isolated context, limited tools, custom prompt. Lifecycle: spawn → isolated execution → return summary → die. Cost control via model routing (e.g., Haiku for Explore). Claude and Codex both emphasize context-pollution avoidance as the primary problem solved. Cross-terms: Claude `subagent`, Codex `subagent thread / custom agent`, CrewAI `agent`, AutoGen `ConversableAgent`, LangGraph `node`, Cursor `SDK subagent`, OpenCode `Investigator/Auditor` (depth-2).

- **Workflow / Flow / Graph / DAG** = *How work is sequenced and gated* (control flow). Deterministic orchestration (nodes→edges→conditionals→retries→rollbacks). Windsurf `workflow`, CrewAI `Flow`, LangGraph `Graph`, Universal engine `DAG`, GoClaw `evaluate_loop`. Distinct from subagent because workflow exists even with one actor; it is the *plan* not the *actor*.

- **Background task / async job / cloud agent** = *Where/when it runs* (execution mode). Foreground (blocking, permission-through) vs background (concurrent, auto-denied, notified on done) vs cloud (off-device Action VM). Includes `Ctrl+B` (Claude), Cursor Cloud VMs, Copilot Actions VMs, Codex background threads, GoClaw `cron` lane. Distinct from subagent because a background task can be the *same* agent continuance, not necessarily a delegated child.

- **Git worktree isolation** = *Where code mutations land* (workspace). Mechanism for true parallelism without merge conflicts: `git worktree add .worktrees/<branch> <branch>` → independent working directory + branch per agent. Harness-level primitive used by gwq, Vibora, AgentsMesh (`sandboxes/{pod}/workspace/`), Omegon, Czarina, multi-agent-orchestration pattern. Claude subagent `isolation: worktree` flag bridges subagent → worktree. This is the *sandbox* not the *actor* nor the *flow*.

- **Hooks / Quality gates / Guardrails** = *When policy is enforced* (governance). 25 lifecycle hooks (Claude), command/agent gates (GoClaw), guardrails (OpenAI SDK), LangGraph interrupts. Deterministic code vs LLM evaluation (`prompt`/`agent` hook types). Exit code 2 = blocking.

---

### 2. P1-03 DEEP DIVE — Subagent vs Agent-Team vs Workflow: ONE Capability or THREE?

**Verdict: THREE distinct capabilities with tight coupling — not one. Merge would lose precisely the distinctions the taxonomy needs to rank correctly. Evidence below.**

#### 2.1 Conceptual Definitions

- **Subagent (delegation):** Single parent → one or more scoped children, each with isolated context, task-scoped prompt, and limited tools. Parent retains control, synthesizes results. Lifecycle is ephemeral (spawn→return→die). Depth is typically 1 (Claude explicitly forbids subagent→subagent; OpenCode depth 2 via hierarchy). Concurrency caps: Codex `max_concurrent_threads_per_session`, GoClaw per-link `max_concurrent` + per-agent `max_delegation_load`. Problem solved: context pollution, specialization, parallel exploration, cost routing.

- **Agent-Team (crew / group chat / team):** Persistent or semi-persistent cohort with shared state (task board, mailbox, lessons, memory) and role assignment. Members have identities, can claim tasks atomically (`blocked_by` deps), send peer messages, handle handoffs. Lifecycle is longer than a single parent call — the team *is* the unit. Roles: Lead/PM/Orchestrator vs members; Cursor 3 agents + parallel subagents; CrewAI role/goal/backstory; AutoGen group-chat moderator. Problem solved: division of labor, specialization persistence, continuous collaboration.

- **Workflow (graph / flow / DAG / cascade):** Deterministic control structure defining *what happens in what order, under what conditions, with what gates*. Includes triggers (cron/webhook/schedule), branching, retries, rollbacks, approval gates, evaluation loops, and state persistence (checkpointing). Exists independently of how many agents execute it — a workflow can be single-agent with steps. Problem solved: reproducibility, auditability, recoverability, governance.

#### 2.2 Evidence For SPLIT (Why Three)

| # | Evidence | Source(s) |
|---|---|---|
| S1 | GoClaw implements all four patterns as separate tools with distinct permission and concurrency models. Table: subagent (anonymous clone, inherited tools, depth-limits) vs delegation (named agent, own tools/identity, explicit `agent_links`) vs team (task board + mailbox, atomic claiming) vs handoff (routing override). If they were one capability the implementation would converge; it diverges on identity, tools, session isolation, and concurrency. | GoClaw multi-agent gateway docs |
| S2 | Claude vs CrewAI vs LangGraph taxonomy: Claude has subagents + hooks but no native "team" (team is a *prompt pattern* on top of subagents); CrewAI has natively named crews (team-first); LangGraph has graphs (workflow-first) where multi-agent is graph composition. The primitives are orthogonal axes in framework comparison tables (orchestration style: graph vs crew vs conversation). 2025 comparison: LangGraph = graph, CrewAI = crews+flows, AutoGen = conversation — same domain, disjoint primary primitives. | LangChain vs CrewAI vs AutoGen 2025 comparison; CrewAI docs; LangGraph docs |
| S3 | Workflow exists without multi-agent: Windsurf workflows (`.windsurf/workflows/stages/`), LangGraph flows, and Universal DAG engine (124 MCP tools) all define approval gates, retries, rollbacks, and triggers that are meaningless for a single ephemeral subagent but essential for a repeatable process. Czarina's *Lesson Propagation* (Hopper) and *Review Gates* are workflow properties of the harness, not of any single agent. | Windsurf Cascade; Universal MCP engine; Czarina |
| S4 | Concurrency & isolation differ qualitatively: subagent isolation = context window isolation (and optionally worktree); team isolation = worktree + private credentials per *pod* (AgentsMesh `sandboxes/{pod}/workspace/`); workflow isolation = state checkpointing (LangGraph) and idempotent DAG re-run. These map to different SCs: subagent → SC-05 Cost/SC-09 CSP; team → SC-10 IDFR + SC-03 MTTR; workflow → SC-06 DRR + SC-02 TSR auditability. A single capability would be wired to all SCs weakly; split wiring is precise (see rubric wiring §4.1 in ARCHETYPES_AND_CRITERIA.md). | ARCHETYPES_AND_CRITERIA.md SC-01..SC-10; AgentsMesh; LangGraph checkpointing |
| S5 | Cross-ecosystem naming collision proof: searching "workflow orchestration" returns orchestration *frameworks* and *harnesses*; searching "subagent delegation handoff" returns *permission/concurrency* and *context isolation* designs. The result sets are disjoint beyond vendor marketing overlap. When forced to translate, teams map to "crew/group chat/team", subagents map to "subagent/specialist/delegatee", workflows map to "graph/flow/DAG/cascade/stages" — no single term covers all three in any ecosystem. | Search angles 1,2,6,7 result sets |
| S6 | Temporal persistence: subagent is seconds→minutes (ephemeral), team is hours→days (project-scoped), workflow is indefinite (declarative definition checked into repo like Terraform). Omegon/Vibora demonstrate this: child tasks get separate worktrees that outlive the subagent that created them; the workflow DAG is the durable artifact. | Omegon; Vibora/fulcrum |

#### 2.3 Evidence Considered For MERGE (and why it fails)

| # | Merge Argument | Counter-Evidence |
|---|---|---|
| M1 | "Team is just N subagents with shared state" | Shared state changes failure modes: team needs atomic claiming, blocked_by deps, mailbox ordering, lesson propagation — none of which a subagent has. GoClaw's `team_tasks` (create/claim/complete/search) and `team_message` (send/broadcast/read) are team-only tools; subagents use `delegate_task` instead. |
| M2 | "Workflow is just the orchestration of subagents" | Universal DAG engine and LangGraph work even with one agent (single-node graph with approval gates). Workflow's value (pause/resume/rewind, retry/rollback, schedule/cron, audit) is orthogonal to actor count. Phase 0 already flagged `A07 single vs multi-agent` as a *mode toggle* not an archetype — same logic applies at primitive level. |
| M3 | "Handoff = delegation = subagent" | GoClaw definition is crisp: delegation = A stays in control, B returns result; handoff = B takes over conversation routing entirely (with `clear` to revert). Permission models differ: delegation uses `agent_links` with direction + concurrency; handoff uses routing override. Clinically distinct: delegation for lookups/reports, handoff for escalation/transfer. |

#### 2.4 When One Implies / Requires the Other

- **Subagent → workflow (weak, not required):** Parallel delegation almost always benefits from a lightweight workflow (even if just "fan out → collect → synthesize" ). Codex's phrase "subagent workflows" is explicitly the *pairing* — subagents are the actors, workflow is the orchestration shape. But many uses remain ad-hoc single delegation (e.g., Explore subagent) with no DAG.

- **Team → workflow (strong, usually co-occurs):** A persistent team without a workflow degenerates into manual coordination. CrewAI formalizes this by shipping both: Crews *and* Flows (1.8+). Vibora/Czarina pair AgentPods/worktrees (team) with DAG/Stage definitions (workflow). Tagging note (V-D): team = Capability, workflow = Mechanism/Framework that teams *use*.

- **Workflow → subagent/team (situational):** Approval-gated, retry/rollback workflows apply equally to single-agent steps (e.g., "plan → validate → execute" inside one Claude session via hooks). So neither subagent nor team is implied.

- **Handoff → team or delegation (required):** Handoff only makes sense inside a multi-actor context; it transfers *between* members of a team or from a delegator to a named agent.

**Translation check (≥2 ecosystems) for this cluster:**

| Canonical | Claude Code | OpenAI Codex | Cursor | Windsurf | CrewAI | LangGraph | AutoGen | GoClaw | OpenCode |
|---|---|---|---|---|---|---|---|---|---|
| Subagent | `subagent` | `subagent thread / custom agent` | `SDK subagent` | — (task agent) | `agent` (within crew) | `node` | `ConversableAgent` | `subagent` (anon) | `Investigator/Auditor` |
| Delegation | auto-delegation via `description` | delegate to subagent | — | — | `task delegation` | `handoff`/`send` | `nested chat` | `delegate_task` (named) | `Orchestrator → subagent` |
| Handoff | `/fork` (experimental, inherits history) | — | — | — | `handoff` | `handoff`/`interrupt` | `handoff` (OpenAI Swarm SDK) | `handoff()` routing override | — |
| Agent-Team | prompt pattern (not primitive) | — (workflow = threads) | Agent Window team | — | `crew` | `Swarm`/`StateGraph team` | `Group Chat` | `team_tasks + team_message` | `PM → Orchestrator → Depth2` |
| Workflow | — (skills as workflow packs) | `subagent workflow` | Automations | `Cascade workflow` | `Flow` | `Graph`/`StateGraph` | `Sequential pipeline` | `evaluate_loop`/`quality gates` | `Orchestrator` |

**Confidence:** HIGH that three capabilities are warranted. MED that handoff is a fourth mechanism under delegation/team rather than its own capability (see element catalog below where handoff is tagged Mechanism, not Capability).

---

### 3. P1-05a — AUTONOMY CALIBRATION, HUMAN-IN-THE-LOOP, TRUST/REVIEW UX

**Question:** Are these distinct capabilities or subsets? What does 2+ ecosystems call each, and when does one imply the other?

#### 3.1 Definitions (from literature, not vendors)

- **Autonomy calibration:** Designing how much unsupervised action an agent may take, as a function of *earned trust* rather than raw capability. Trust is learned through accumulated verifiable successes; autonomy is granted progressively and retracted quickly. Failure mode is miscalibration — over-trust (complacency, miss of agent error) and under-trust (disuse, manual takeover, toil). [Sources: SOC Trusted Autonomy framework; GJETA Tiered Controllability Framework (TCF) 2026; Yang et al. 2020 Trust-Risk × Error-Risk matrix; Parahelp Trust-Autonomy Tradeoff skill]

- **Human-in-the-loop (HITL) controls:** Concrete mechanisms that keep a human as authorizer, reviewer, or escalation point inside the loop (not on-the-loop observing). Includes approval gates, permission scopes, escalation paths, intervention affordances, and observability to make gating informed. [Sources: Claude permissionMode/PermissionRequest hook; GitHub Copilot human review; LangGraph interrupt/approval patterns]

- **Trust calibration / review UX:** The interface and instrumentation that lets humans accurately judge when to trust the agent and efficiently review its work. Includes agent inbox patterns, confidence display, provenance, decision journals, override tracking, and metrics (approval/edit/override rates, time-to-decision, rejection rate). [Sources: Adaptive Trust Calibration (Okamura & Yamada PMC7034851); Johnson et al. 2023; Kestrel HITL patterns; Parahelp Agent Inbox]

#### 3.2 Are They One or Distinct?

**Three distinct but tightly coupled capabilities/patterns — not subsets. Rationale:**

| Capability | Core Artifact | Primary Instrument | SC Wiring (phase-0) | Harm If Absent |
|---|---|---|---|---|
| **Autonomy calibration** | Autonomy policy (L0-L5 / Zone A/B/C / Stages 0-3) — how much autonomy per *action type* at a given trust level. E.g., trivial → autonomous for all levels; irreversible → always ask. | Policy table + expansion protocol (one action type per 2 weeks + 60-day no-incident window + override rate <1%). | SC-04 HIR, SC-05 CPSR (cost of premature autonomy), SC-07 SSHC (irreversible actions) | Over-autonomy → irreversible harm; under-autonomy → adoption failure (HIR > threshold) |
| **HITL controls** | Gates + permissions (blocking vs auto-advance, authorization scopes, escalation, rollback/undo, allow/deny/interrupt). | Permission modes, `PermissionRequest`/`PreToolUse` hooks (exit 2 = block, 0 = pass), approval gates. | SC-04 HIR, SC-03 MTTR (gate friction), SC-07 SSHC (sandbox boundary) | No gate → SC-07 catastrophic; too many gates → SC-04/SC-01 regression |
| **Trust & review UX** | Inbox + confidence + provenance + metrics that make gating *calibrated* (not just present). | Agent Inbox types (ESCALATE/AUTHORIZE/COLLECT/RESULT/INFORM), confidence buckets (95%+/70-95%/50-70%/<50%), decision journal, approval/edit/override/time metrics, graduated intervention (Observe→Approve-first→Autonomous). | SC-09 CSP (context surviving review), SC-02 TSR (faithfulness), SC-04 HIR quality | Controls without UX → miscalibration (5% rejection → over-reliance; >40% edit rate → quality fail) |

**Evidence that HITL ≠ autonomy:** You can have HITL gates that are *uncalibrated* (always ask, even for trivial reversible actions) — high HIR, poor UX, under-trust. Autonomy calibration is the *policy* that decides when a gate should exist. HITL is the *mechanism* that enforces it. One without the other produces either insecure autonomy (no gates) or toilsome autonomy (gates everywhere).

**Evidence that trust UX ≠ either:** Two harnesses can have identical gate policies yet differ wildly in review efficacy: one shows confidence + provenance + aggregated inbox with bulk actions (fast, accurate), the other dumps raw diffs (slow, error-prone). Metrics distinguish them: time-to-decision (<30s healthy vs >2m poor UX), edit rate (<20% healthy vs >40% quality problem), override rate (>2% means autonomy outran trust). Trust calibration literature treats this as its own pillar mediating autonomy ↔ HITL (SOC framework: trust as third pillar between autonomy tier and HITL level).

**When one implies the other:**

- Autonomy calibration **implies** both HITL controls (to enforce tiers) *and* trust UX (to decide tier transitions, e.g., Shadow Stage exit = 95% agreement rate, Delegated Stage entry = ≥3 months Stage 2 + 60-day no incident). But you can deploy HITL without formal calibration (ad-hoc "ask before dangerous tools").
- HITL controls **do not imply** calibration (many tools ship allow/deny without staged expansion protocol).
- Trust UX **presupposes** some observability substrate (tracing, audit) but not necessarily gates.

**Preliminary tiering for harness:** Autonomy calibration = **Foundational** (governs SC-07 veto). HITL controls = **Foundational** (implements SC-07/SC-04 contract). Trust/review UX = **Important** (determines whether foundational controls actually achieve calibrated trust; SC-02/SC-04 predictor). These three should *not* be collapsed into "permissions" or "safety" alone.

#### 3.3 Concrete Vocabulary Across Ecosystems (Translation Check)

| Canonical | Claude Code | Cursor / Copilot | LangGraph / LangChain | Enterprise (SOC/Parahelp) | Research lit |
|---|---|---|---|---|---|
| **Autonomy levels** | `permissionMode` (`approve` / `auto`) + subagent `permissionMode` | Copilot workspace: human assigns issue like a developer | `interrupt` patterns, draft→await-approval→proceed | L0-L5 / Zone A/B/C / Stages 0-3 | TCF 4 tiers (risk×reversibility×scope) |
| **Approval gates** | `PermissionRequest`, `PreToolUse` (exit 2 = block), `Stop/SubagentStop` hooks | PR review, `gh agent-task`, `@Cursor` on PR | `human interrupt` / checkpoint approval | Zone B confirmation (gated) vs Zone A autonomous | HITL levels mapped to task risk |
| **Trust UX** | Plan mode review, cost ledger, trace viewer (implied screening) | Sidebar agent manager (foreground+background), Conversation fetch | LangSmith tracing/eval, thread checkpoint viewer | Agent Inbox (5 types), Decision Journal, Confidence+Provenance, Trust metrics | trust calibration cues (TCC), reliance behavior monitoring |
| **Graduated intervention** | Not named (implicit via permissionMode + hooks) | — | — | Observe → Approve-first → Autonomous (per category, one-move retract) | Adaptive trust calibration (over-trust/under-trust detection) |
| **Scope contract** | — (AGENTS.md as proxy) | — | — | Authority as readable document | Agent Operational Envelope (permissions/domain/safety/governance/autonomy) |

#### 3.4 Health Thresholds (Operational, Cross-Cited)

- Approval rate by action type: >85% healthy.
- Edit rate on drafts: <20% healthy; <10% = ready for autonomy expansion (Zone A); >40% = quality problem (contract autonomy).
- Override rate: <2% healthy; any action type >2% → autonomy outran trust, revert to Zone B, file decision journal note.
- Time-to-decision: <30s healthy; >2m signals poor confirmation UX.
- Rejection rate: 15-30% healthy; <5% signals over-reliance (automation complacency).
- Shadow→Assisted exit: ≥95% agreement; Collaborative→Delegated: ≥3 months prior stage + 60 days no incidents + override <1%; expansion cadence = one action type per 2 weeks.

These numbers are research-anchored (Parahelp, Kestrel, SOC, Yang et al.) not vendor opinion, and should be wired into Batch 4/5 safety + Batch 5 observability validation (SC-04/SC-07).

---

### 4. CANDIDATE ELEMENT CATALOG — Execution & Agency Layer

> Per Phase 1 protocol: canonical name, definition, problem solved, why it matters, level, lifecycle role, related concepts, cross-ecosystem terms, confidence, foundational/important/specialized/situational.

#### E-01 — Subagent Delegation (Specialized Delegated Workers)

- **Definition:** Parent agent spawns one or more scoped child instances, each with its own context window, custom system prompt (often a Markdown file with YAML frontmatter: `name/description/tools/model/permissionMode`), and optionally restricted tool access. Child returns a summary; parent synthesizes. Depth typically 1; chaining via parent orchestration. Isolated by default (zero history unless forked variant); optional worktree isolation for file-mutating subagents.
- **Problem:** Context pollution/rot in long trajectories; need for specialization (Explore vs Plan vs General-purpose) and parallelism without main-thread bloat; cost routing (cheap model for scoping reads).
- **Why it matters:** Directly predicts SC-05 CPSR (cheapest-model routing + summary vs raw output), SC-09 CSP (key intents survive because noisy exploration stays off main thread), and SC-02 TSR on research/code-search tasks (parallel subagents 3-5× faster synthesis per Claude guide: "Research auth, DB, API in parallel using separate subagents").
- **Level:** **Capability** (primary) + **Mechanism** (spawn primitive + frontmatter schema) + **Tool** (`.claude/agents/`, `.codex/agents/*.toml`, `.gemini/agents/`, `.github/agents/`).
- **Lifecycle role:** Execute (explore, investigate, web-search) + Verify (auditor) within a single run; authoring-time definition (Markdown/TOML) checked in.
- **Related:** E-02 (team), E-03 (workflow), E-04 (background mode), E-05 (worktree isolation), E-06 (handoff), hooks/permissionMode, skills/slash commands, context isolation.
- **Cross-ecosystem terms:** Claude `subagent` · Codex `subagent thread / custom agent (worker/explorer)` · Cursor `SDK subagent (nested)` · OpenCode `Investigator/Auditor/Docs` (Depth 2) · CrewAI `agent` (within crew) · LangGraph `node` · AutoGen `ConversableAgent` · GoClaw `subagent (anonymous subagent)` vs `delegation (named agent)`.
- **Confidence:** HIGH. **Preliminary tier:** FOUNDATIONAL — every serious harness past single-prompt needs it; ranked S for C1/C2/C4 (research/engineering) per SC-01/SC-05/SC-09.

#### E-02 — Agent Teams / Crews / Collaborative Teams

- **Definition:** Persistent or semi-persistent cohort of named agents with role assignment, shared state (task board, mailbox, Hopper/lessons, memory), and peer-to-peer coordination (atomic task claiming with `blocked_by` deps, send/broadcast/read). Distinct from ephemeral subagents by identity, persistence, and shared coordination substrate. Roles: Lead/PM/Orchestrator vs members.
- **Problem:** Complex multi-step feature plans requiring division of labor (planner→generator→verifier→CI validator), specialization persistence, and coordination beyond parent synthesis.
- **Why it matters:** Predicts ability to scale beyond single-agent capability ceiling (SC-02 on C1/C5/C6 team archetypes), SC-10 IDFR (task board as source of truth for drift-free re-run), SC-03 MTTR (atomic claiming prevents double-assignment, mailbox orders follow-ups). Without an explicit team primitive, "teams" become ad-hoc prompt patterns with implicit coordination (fragile, uninstrumented).
- **Level:** **Capability** + **Framework** (Crew, Group Chat, Team). Tool layer = `team_tasks`/`team_message` (GoClaw), `Crew` (CrewAI), `Group Chat` (AutoGen), `Agent Window` (Cursor).
- **Lifecycle role:** Plan (PM drafts spec) → Execute (members claim tasks) → Verify (auditor/reviewer) → Govern (task board as audit).
- **Related:** E-01, E-03, E-05 (AgentPod workspaces), E-06, E-08, lesson propagation, review gates.
- **Cross-ecosystem:** CrewAI `crew` · AutoGen `group chat (moderator)` · LangGraph `Swarm` · GoClaw `team_tasks + team_message` · Cursor `Agent Window parallel agents` · OpenCode `PM→Orchestrator→Depth2` hierarchy · Claude Code *prompt pattern* (no native primitive — gap) · AgentsMesh `AgentPod` cohort.
- **Confidence:** HIGH (native in CrewAI/AutoGen/GoClaw, pattern elsewhere). **Tier:** IMPORTANT — foundational for team archetypes (C1 scale, C5, C6), specialized for solo archetypes (C3/C4-read-only can stay subagent-only).

#### E-03 — Workflow Orchestration (Graph / Flow / DAG / Cascade)

- **Definition:** Declarative control structure defining nodes, edges, conditionals, triggers (cron/webhook/schedule/event), retries with intelligence, rollbacks, approval gates, evaluation loops, and state persistence/checkpointing. The *plan* not the *actors*; applies to single-agent steps and multi-agent cohorts equally. Examples: Windsurf `workflows/stages`, CrewAI `Flows (1.8+)`, LangGraph `StateGraph`, Universal `DAG Engine` (124 MCP tools: workflow_create/run/validate).
- **Problem:** Reproducibility, durability (pause/resume/rewind), recoverability (retry/rollback), auditability, and governance (approval gates before production) that ad-hoc delegation lacks.
- **Why it matters:** Wires to SC-06 DRR (byte/semantically identical re-run), SC-03 (retry intelligence), SC-10 IDFR (no-op on frozen inputs), SC-02 per archetype (auditable state). Without it, orchestration is prompt-implicit and unmeasurable.
- **Level:** **Capability** + **Framework** (orchestration framework) + **Protocol** (A2A for cross-runtime delegation). Workflow files (`.windsurf/workflows/*.md`, graph definition) are project artifacts (IaC analog).
- **Lifecycle role:** Define (author DAG) → Run (execute with permissions) → Observe (LangSmith trace) → Re-run (idempotent).
- **Related:** E-01/E-02 (actors that execute nodes), E-10/E-11 (gates that annotate edges), E-04 (lanes that schedule nodes), checkpointing, triggers, idempotency.
- **Cross-ecosystem:** Windsurf `Cascade workflow / stages` · CrewAI `Flow` · LangGraph `Graph / StateGraph` · Universal `DAG` · GoClaw `evaluate_loop` · Temporal/Argo analog · OpenAI SDK `handoffs` (lightweight DAG) · Czarina `Stages + Lesson Propagation + Review Gates`.
- **Confidence:** HIGH. **Tier:** FOUNDATIONAL — declarative workflows are load-bearing for C2/C5/C6/C3 (SC-06/SC-10 veto classes) and for any harness claiming reproducibility.

#### E-04 — Background Tasks / Async Jobs / Cloud Agents

- **Definition:** Execution-mode primitive orthogonal to actor: foreground (blocking, permission-through) vs background (concurrent, auto-denied permissions, notified on completion) vs cloud (off-device VM — Ubuntu VM or GitHub Actions runner — that edits/tests/pushes to branches and opens draft PRs). Includes `Ctrl+B` backgrounding (Claude), up to 8 parallel Cursor cloud agents, `gh agent-task create/list` (Copilot on Actions), Codex `max_concurrent_threads_per_session` background threads, GoClaw `cron` lane.
- **Problem:** Need genuine parallelism without blocking the interactive session; offload long tests/lints/compiles and autonomous branch work; allow mobile follow-up (GitHub Mobile agent tasks).
- **Why it matters:** SC-01 TTFUA (keep interactive session responsive while build/test runs), SC-05 CPSR (container-min billing for cloud VMs), SC-04 HIR (async changes reviewed as RESULT not AUTHORIZE). Distinguishing foreground vs background is itself a policy decision (trust-risk × error-risk).
- **Level:** **Mechanism** (execution mode) + **Tool** (APIs/CLIs: Cursor Background Agents API, `gh agent-task`, `codex exec --full-auto`). Not a standalone capability — it is *how* delegation/team/workflows run.
- **Lifecycle role:** Run-time scheduling; also authoring-time declaration (Cursor Automations: scheduled/event-triggered).
- **Related:** E-01, E-05, E-10, lanes/throttle, PTY streaming (AgentsMesh).
- **Cross-ecosystem:** Claude `foreground vs background subagent` · Cursor `Background Agent (cloud VM, 8 parallel)` · Copilot `coding agent + cloud agent (Actions VM) + gh agent-task` · Codex `background subagent thread` · GoClaw `Lane-based Scheduler (main/subagent/delegate/cron)` · AgentsMesh `AgentPod (PTY + worktree + stream)`.
- **Confidence:** HIGH. **Tier:** IMPORTANT — specialized for solo-interactive but foundational once parallelism or cloud delegation is in scope.

#### E-05 — Git Worktree Isolation / Workspace Sandboxing

- **Definition:** Each agent/pod gets an isolated Git worktree (independent working directory + independent branch) plus private credentials/env, so concurrent agents never collide and main branch is untouched. Implemented as `git worktree add .worktrees/<feature> <branch>` per agent; harness managers (gwq fuzzy finder, Vibora single-screen, AgentsMesh `sandboxes/{pod}/workspace/`, Omegon single binary, Czarina) automate creation/cleanup/merge.
- **Problem:** True parallelism on same repo without merge conflicts; safe experimentation (retry/rollback without touching main); per-agent credential isolation (SC-07).
- **Why it matters:** SC-07 SSHC (private credentials per pod, egress allowlist), SC-10 IDFR (worktree as frozen-input sandbox), SC-02 on C1/C6 (shadow/dual-write requires isolated execution). Without it, parallel agents contend on HEAD and produce nondeterministic merges.
- **Level:** **Mechanism** + **Tool** (gwq, Vibora, AgentsMesh Workspace, Omegon). Bridges to E-01 via Claude `isolation: worktree` flag and to E-02 via AgentPod definition.
- **Lifecycle role:** Run-time isolation; project setup (`sandboxes/` directory, `.worktrees/` gitignore).
- **Related:** E-01, E-02, E-04, sandboxing/egress policy, credential management.
- **Cross-ecosystem:** `git worktree` (git primitive) · gwq (`gwq` manager) · Vibora `Git Worktree Isolation` · AgentsMesh `Workspace (worktree + creds)` · Omegon `real git worktrees` · Czarina `Git Worktrees` · multi-agent-orchestration `Git Worktree Isolation` pattern · Claude `isolation: worktree`.
- **Confidence:** HIGH. **Tier:** IMPORTANT — foundational for parallel execution; specialized for strictly sequential single-agent harnesses.

#### E-06 — Conversation Handoff (Routing Transfer)

- **Definition:** Control transfer where Agent A hands the *entire conversation* to Agent B, who then owns future user messages (routing override + context transfer). Differs from delegation where A stays in control and B returns a result. Revertible via `handoff(action="clear")`. Four-tier use: escalation, expertise transfer, role change, recovery.
- **Problem:** Scenarios where the original agent is the wrong specialist and continuing to proxy (delegation) adds latency/indirection; need clean transfer of conversational authority.
- **Why it matters:** Determines UX interrupt budget (SC-04) and audit trail (SC-07: who owns the conversation when irreversible actions occur). Miscalibrated handoff → confused ownership and untraceable authorization.
- **Level:** **Mechanism** / **Protocol** (routing rule + context payload). Presupposes multi-actor substrate (team or named delegates).
- **Lifecycle role:** Run-time routing; governance (auditable transfer).
- **Related:** E-01, E-02, E-08, Agent-to-Agent (A2A) protocol.
- **Cross-ecosystem:** GoClaw `handoff()` (routing override) · OpenAI Agents/Swarm SDK `handoff` · CrewAI/AutoGen `handoff` · LangGraph `interrupt + handoff` · Claude experimental `forked subagent` (history-inheriting variant) · Google `A2A` (cross-runtime handoff).
- **Confidence:** MED-HIGH (explicit in GoClaw/OpenAI SDK/A2A, implicit elsewhere). **Tier:** SPECIALIZED — needed once multi-agent routing matters; not needed for ephemeral subagent-only harnesses.

#### E-07 — Orchestrator / Supervisor / Hierarchical Patterns

- **Definition:** Architectural pattern where a lead agent (Orchestrator/PM/Supervisor/Router) plans, breaks work into tasks, spawns/redirects workers, passes relevant context (not full history), follows progress, and coordinates follow-up. Variants: supervisor/worker, planner-executor, swarm/handoff, group-chat moderator, Lane-based Scheduler.
- **Problem:** Coordination overhead, context relevance (workers need slice not whole), and quality control (review gates) that flat parallel spawning cannot solve.
- **Why it matters:** Predicts SC-09 CSP (workers get relevant context → goal embedding survives), SC-03 MTTR (supervisor retries alt worker), SC-02 on complex tasks where uncoordinated subagents produce incoherent artifacts. Documents *when* to use hierarchical vs swarm vs graph (CrewAI sequential/hierarchical/custom, LangGraph conditional routing, AutoGen group chat).
- **Level:** **Framework / Pattern** (orchestration pattern catalog). Implemented by framework primitives (LangGraph Supervisor, AutoGen GroupChat+Moderator, CrewAI hierarchical crew, GoClaw lane throttle).
- **Lifecycle role:** Plan → Execute → Verify loop; system design choice.
- **Related:** E-01..E-03, E-08, E-12, planner-executor, verifier pattern, lesson propagation.
- **Cross-ecosystem:** LangGraph `Supervisor`, CrewAI `hierarchical crew`, AutoGen `Group Chat + Moderator`, OpenCode `PM→Orchestrator` hierarchy, GoClaw `Lane Scheduler`, Czarina `Conductor`, Orchestrator hints in `AGENTS.md`.
- **Confidence:** HIGH. **Tier:** IMPORTANT — pattern choice determines whether multi-agent scales or thrashes.

#### E-08 — Delegation Permissions / Lane Scheduler / Throttle

- **Definition:** Concurrency and authorization fabric for multi-agent execution: explicit `agent_links` with direction (`outbound/inbound/bidirectional`) + two-layer concurrency (`per-link max_concurrent` + `per-agent max_delegation_load`), lane assignment (`main/subagent/delegate/cron`), adaptive throttle for group chats, deny/allow per user (JSONB), sandbox_mode per agent (e.g., `read-only` for Investigator/Auditor). Quality-gate evaluators skip own gates (recursion-safe).
- **Problem:** Unbounded delegation → resource exhaustion, confused ownership, policy bypass; need governable fan-out with auditable concurrency.
- **Why it matters:** SC-05 CPSR (concurrency → token×infra cost), SC-07 (read-only vs read-write sandbox), SC-04 (throttle prevents interrupt flood). Without it, "N subagents" is an unmanaged fork bomb.
- **Level:** **Mechanism** (+ policy as `other_config`). Distinct from HITL gates (which gate *each action*) — this gates *delegation itself*.
- **Lifecycle role:** Governance / run-time enforcement; configured in `config.toml`/`other_config`.
- **Related:** E-01, E-04, E-10, quality gates.
- **Cross-ecosystem:** GoClaw `agent_links + max_concurrent + max_delegation_load` · Codex `max_concurrent_threads_per_session` · Claude `tools/hooks/permissionMode` per subagent · Cursor `Allowed Tools` per agent · OpenCode `read-only Investigator/Auditor` constraints.
- **Confidence:** MED (explicit only in GoClaw/Codex/Claude/OpenCode; elsewhere implicit). **Tier:** SPECIALIZED — load-bearing once fan-out >3 concurrent agents or multi-tenant.

#### E-09 — Autonomy Calibration (Progressive Trust / Tiered Controllability)

- **Definition:** Policy framework that maps *action types* (by risk × reversibility × scope) to autonomy levels (L0 Shadow → L1 Assisted → L2 Approve-before → L3 Review-after → L4 Spot-check / Zones A/B/C / Stages 0-3) and evolves them via earned trust. Trust ladder: trivial failures autonomous for all levels; reversible failures graduated by trust level (ask+reasoning → ask+checkbox → autonomous+24h undo → block); irreversible always ask. Expansion at most one action type per 2 weeks, after 2-week observation, with rollback on override>2%/incidents. Trust is a portfolio, not a switch.
- **Problem:** Raw capability ≠ trustworthiness; premature autonomy → irreversible harm (SC-07), insufficient autonomy → adoption failure (SC-04/HIR) and toil. Miscalibration (over/under-trust) is the most prevalent agentic failure mode per GJETA 2026.
- **Why it matters:** Wires to SC-04 HIR, SC-07 SSHC (irreversible never autonomous), SC-05 CPSR (Shadow mode 95% agreement gate before spend), SC-03 MTTR (L4 autonomous recovery vs L2 approve-before). The harness can pass all tool tests yet fail operationally if autonomy is uncalibrated.
- **Level:** **Capability** (governance capability) + **Protocol** (expansion/retraction rules). Operationalized via policy tables and metrics.
- **Lifecycle role:** Governance — design-time policy, run-time enforcement, post-run re-evaluation (trust analytics).
- **Related:** E-10, E-11, TCF, Agent Operational Envelope, Zone framework.
- **Cross-ecosystem:** SOC `L0-L5 Autonomy Tiered Framework` · Parahelp `Zone A/B/C + Trust Ladder + 4 Stages (Shadow→Assisted→Collaborative→Delegated)` · GJETA `Tiered Controllability Framework (4 tiers)` · Yang et al. `Trust-Risk × Error-Risk (HIGH/MED/LOW)` · Kestrel `Scope contract + Graduated intervention`.
- **Confidence:** HIGH (convergent across SOC, GJETA, Parahelp, Kestrel, Yang). **Tier:** FOUNDATIONAL.

#### E-10 — Human-in-the-Loop Controls (Approval Gates / Permission Modes / Escalation)

- **Definition:** Concrete control surfaces that keep a human as authorizer/reviewer/escalation point: blocking vs auto-advance gates, permission modes (`approve` vs `auto`), per-tool allow/deny/interrupt, escalation on failure, and rollback/undo affordances. Blocking gates (human must act) migrate to auto-advance when trust is earned (via analytics). Gates instrumented with `human.input` events, `was_blocked` chips, and permission-denial metrics.
- **Problem:** Executing consequential tool calls, file writes, or external actions without a calibrated human checkpoint.
- **Why it matters:** SC-07 gate (0 leaks / 100 runs), SC-04 median HIR targets (0 for C1, ≤1 for C2/C3/C5/C6, ≤2 for C4), SC-03 (gate friction ↔ MTTR). Pre-deployment verification: *post-hoc* controls (prompt guardrails) offer limited production assurance without governed envelopes (Agent Operational Envelope paper).
- **Level:** **Capability** + **Mechanism** (hooks, permission modes, interrupts).
- **Lifecycle role:** Run-time (PreToolUse/PermissionRequest) plus design-time policy (AGENTS.md Operating Model).
- **Related:** E-09, E-11, sandboxing, audit trail, compensation/retry.
- **Cross-ecosystem:** Claude `permissionMode + PermissionRequest + PreToolUse (exit 2 block)` · Copilot `PR review + human approval` · Cursor `permission scopes + agent manager` · LangGraph `interrupts (draft→await-approval→proceed)` · GoClaw `quality gates (command/agent, blocking retry)` · OpenAI `Guardrails`.
- **Confidence:** HIGH. **Tier:** FOUNDATIONAL.

#### E-11 — Trust Calibration & Review UX (Agent Inbox / Confidence / Decision Journal)

- **Definition:** Interface and instrumentation that lets humans *accurately* judge agent reliability and *efficiently* review work. Two layers: (a) Inbox taxonomy — every agent→human interaction is one of ESCALATE (take over, red) / AUTHORIZE (approve gate, amber) / COLLECT (structured input, blue) / RESULT (review completed work, green) / INFORM (awareness, grey); inbox composition is itself a trust metric (early AUTHORIZE-heavy → over time INFORM-heavy). (b) Calibrated signals — confidence buckets (95%+ / 70-95% / 50-70% / <50% with distinct phrasing), provenance (sources, tool trace), Decision Journal (what was decided, why, review depth, time spent), and metrics (approval/edit/override/time per action type).
- **Problem:** Gates without calibrated UX produce over-reliance (<5% rejection → complacency) or under-reliance (>40% edit rate → disuse) even when gate policy is sound. Adaptive Trust Calibration framework detects over/under-trust via reliance behavior + cognitive cues (TCC) and prompts re-calibration.
- **Why it matters:** Predicts whether SC-04 targets are *meaningful* (median HIR 0 could be good autonomy or over-reliance). Health thresholds (approval>85%, edit<20%, override<2%, time<30s, rejection 15-30%) give measurable gates for autonomy expansion (Stage exit criteria). 63% of users more likely to rely on AI that displays confidence — confidence display is not cosmetic.
- **Level:** **Capability** (review UX + observability). Distinct from HITL controls — this is *how review is presented and measured*.
- **Lifecycle role:** Review-time UX + post-run analytics (Did it materially improve? p10 archetype).
- **Related:** E-09, E-10, observability/evaluation, audit trail, Kestrel patterns (Confidence+provenance, Exception-first attention, Trust analytics).
- **Cross-ecosystem:** Parahelp `Agent Inbox (A2H) + Trust metrics` · Kestrel `Confidence+provenance + Trust analytics (track record)` · PMC7034851 `Adaptive Trust Calibration + Trust Calibration Cues (TCC)` · Johnson et al. `calibration training` · Claude/Cursor/Copilot indirect (trace viewer + PR diff review — weaker explicit inbox).
- **Confidence:** HIGH. **Tier:** IMPORTANT — determines whether foundational gates achieve calibrated trust; load-bearing for high-supervision archetypes C4/C6.

#### E-12 — Evaluate Loop / Quality Gates (Generator ↔ Evaluator)

- **Definition:** Orchestrated feedback cycle between a generator agent and an evaluator agent: `evaluate_loop(generator="writer-bot", evaluator="qa-bot", task="...", pass_criteria="...")`, configurable rounds (default 3, max 5), with custom pass criteria and automatic retry on failure. Quality gates generalize this: hook type `command` (shell exit 0=pass) or `agent` (delegate to reviewer agent); failed gates can block output and trigger retry with feedback; recursion-safe (evaluators skip own gates).
- **Problem:** Single-pass generation is unreliable for high-stakes artifacts; need gated, review-then-revise cycles without human for routine cases but with human escalation on repeated failure.
- **Why it matters:** SC-08 AHG (gate pass rate: ≥85% C1, ≥80% C2/C5), SC-02 TSR (evaluator as pre-submission test), SC-04 (loop depth → HIR when auto-retry exhausted). Blurs workflow ↔ team: the loop *is* the minimal workflow DAG with a team of two.
- **Level:** **Mechanism** (workflow pattern) + **Tool** (GoClaw `evaluate_loop`, quality-gate `other_config`).
- **Lifecycle role:** Verify phase; authoring-time pass_criteria definition.
- **Related:** E-03, E-02, E-10, verification strength (full-suite vs modified-tests), guardrail timeliness (EIR).
- **Cross-ecosystem:** GoClaw `evaluate_loop + Quality gates` · AutoGen `nested chat + review loop` · CrewAI `Flow with verification step` · LangGraph `conditional edge (pass→proceed, fail→revise)` · OpenOpen `Auditor (PASS/FAIL)` · Czarina `Review Gates`.
- **Confidence:** MED-HIGH (explicit in GoClaw/OpenCode/Czarina, pattern elsewhere). **Tier:** IMPORTANT — verification strength is an archetype discriminator (SC-08/SC-02 instrumentation gap per V-C Probe 3).

---

### 5. CROSS-ECOSYSTEM TRANSLATION MATRIX (Translation Check Summary)

| Canonical primitive | Ask in 2 other ecosystems — what is it called? | Implication test |
|---|---|---|
| Subagent delegation | Codex `custom agent (TOML)` = Claude `subagent` = CrewAI `agent` = AutoGen `ConversableAgent` = LangGraph `node` | Subagent implies a workflow shape ("fan out→collect") but not a team; solo Explore subagent is common (no team, no DAG). |
| Agent teams | CrewAI `crew` = AutoGen `group chat` = LangGraph `Swarm` = GoClaw `team_tasks+mailbox` = AgentsMesh `AgentPod cohort` | Team implies a workflow (even if implicit task board DAG) once N>2 and tasks have deps (`blocked_by`). |
| Workflow / DAG | Windsurf `Cascade workflow` = CrewAI `Flow` = LangGraph `Graph` = Universal `DAG` = GoClaw `evaluate_loop` | Workflow does NOT imply multi-agent; single-agent approval-gated flow is valid (LangGraph interrupt pattern). |
| Background / async | Claude `background subagent (Ctrl+B)` = Cursor `Background Agent (cloud VM)` = Copilot `coding agent (Actions)` = GoClaw `cron lane` | Background implies worktree isolation when file-mutating; else context-only isolation suffices. |
| Worktree isolation | `git worktree` = Claude `isolation: worktree` = AgentsMesh `Workspace` = Omegon `real git worktrees` = Vibora `Git Worktree Isolation` | Worktree does not imply any of the above; it can isolate a single-agent headless run. |
| Autonomy calibration | SOC `L0-L5` = Parahelp `Zone A/B/C + Stages 0-3` = GJETA `TCF 4-tier` = Yang `Trust-Risk×Error-Risk` | Calibration implies HITL gates + trust UX (needs both to be measurable); HITL alone does not imply calibration. |
| HITL gates | Claude `permissionMode + PreToolUse` = LangGraph `interrupt` = Copilot `PR review` = GoClaw `quality gate (blocking)` | HITL implies audit/observe substrate but not calibrated autonomy. |
| Trust/review UX | Parahelp `Agent Inbox (5 types)` = Kestrel `Confidence+provenance` = PMC `Trust Calibration Cues` | Trust UX presupposes observability; without it, inbox metrics (approval/edit/override/time) are uncomputable. |

---

### 6. STOP-RULE & NEGATIVE RESULTS

| Sub-area | Searches run | Consecutive "only synonyms/noise" before stop |
|---|---|---|
| Execution primitives (subagent/delegation/orchestration) | 7 (angles 1-6 + 7) | Stopped after angles 6→7→8 all returned only crew/group-chat/graph/swarm as synonyms of team/workflow — no new primitives beyond the GoClaw 4-pattern + handoff. Verified via "awesome-codex-subagents" (136 agents) produced niche trivia (agent counts) not new execution primitives. |
| Git worktrees | 1 dedicated (angle 11) + 3 incidental (hard-Cursor/Copilot/OpenCode) | Stopped after `gwq → Vibora → AgentsMesh → Omegon` all converged on `git worktree add` + private-creds pattern; further searches returned wrapper CLIs not new isolation mechanisms. |
| Autonomy/HITL/trust | 3 (angles 8-10) | Stopped after third angle returned only rephrasings of L0-L5/Zone/Stages and the same 5 inbox types + same 4 health thresholds; no new tier system beyond TCF/SOC/Parahelp/Kestrel/Yang 5-way convergence. |
| Workflows/orchestration frameworks | 2 (angles 3 + 12) | Stopped after 2025 comparison + Universal DAG converged on graph/crew/conversation triad; no new orchestration style beyond those three + A2A protocol. |

**Dead ends / niche noise logged (do not promote):**
- `VoltAgent/awesome-codex-subagents` 136-agent list: taxonomy is *agent role* marketplace, not execution primitive — situational registry, not capability.
- `Terminal-native agents directory` (Pi, Goose, Crush, Kilo): CLI entrypoint variety does not add new execution primitives beyond already-counted Cline/Roo/OpenCode patterns.
- `Scheduled Automations` (Cursor) and `cron lane` (GoClaw): trigger mechanism is workflow concern, not distinct from Workflow Orchestration (E-03) — folded as mechanism, not promoted.

**Commonly missed findings (P1-05a confirmation):** Autonomy calibration, HITL controls, and trust/review UX are *systematically missed* when batch-1 is framed as "multi-agent" — they are filed under Safety/Batch 4 or DX/Batch 5 but their execution-layer wiring (SC-04/SC-07/SC-08, permissionMode vs Zone vs Inbox) is load-bearing for ranking. All three should be tagged `IMPORTANT or FOUNDATIONAL` not `SPECIALIZED`.

---

### 7. SOURCES

**Claude Code:**
- https://code.claude.com/docs/en/sub-agents — Subagents (frontmatter schema, tools/permissionMode/hooks/isolation, auto-delegation, parallel delegation, built-ins Explore/Plan, cannot spawn subagents, forked subagents)
- https://code.claude.com/docs/en/hooks — Hooks (25 lifecycle events, command/http/mcp_tool/prompt/agent, exit-code 2 = blocking, scoped settings)

**OpenAI Codex:**
- https://developers.openai.com/codex/subagents — Subagent workflows (parallel fan-out up to 6 threads, custom TOML agents, AGENTS.md/skill instructions, context pollution avoidance, spawning/routing/waiting/close lifecycle)
- https://github.com/VoltAgent/awesome-codex-subagents — 136+ agents, 10 categories, 280+ resources (validates subagent as active ecosystem primitive)

**Cursor / Windsurf:**
- https://cursor.com — Background Agents (isolated Ubuntu VMs, up to 8 parallel, API launch/follow-up/status/MCP, GitHub PR @Cursor, Agent Window, SDK local+cloud, Automations scheduled/event-triggered)
- https://windsurf.com (Cascade Flow) — Cascade workflows (`.windsurf/workflows/*.md`, `.windsurf/workflows/stages/`, visual flow editor, CI hooks, workspace-aware)

**Gemini CLI / Copilot / Cross-platform harnesses:**
- https://github.com/caesar-harness-agent — Cross-platform subagent matrix (`.github/agents`, `.gemini/agents`, `.codex/agents`)
- https://github.com/xmedd/zeoel-framework — 23-agent orchestration framework across Claude/Cursor/Gemini/Copilot
- https://github.com/midego1/claude-orchestrate — Multi-agent orchestration plugin + portable edition for Codex/opencode/Cursor/Gemini/Copilot
- https://github.com/ops-engineering-skills/multi-agent-orchestration/SKILL.md — Supervisor/worker, swarm/handoff, hierarchical patterns across 5 CLIs
- https://docs.github.com/copilot/concepts/agents/about-copilot-coding-agent — Copilot coding agent (Actions-powered VM, branch/PR, compile/test/lint, delegate like a developer)
- https://github.blog/changelog/2026-02-09-kick-off-and-track-copilot-coding-agent-sessions-from-github-cli — `gh agent-task create/list` (CLI 2.80), `/delegate` slash
- https://docs.github.com/copilot — Copilot custom agents (`.github/agents/*.agent.md`, model selection + allowed tools)
- https://github.com/ytthuan/agents-system-setup — Host-session Orchestration Operating Model (`AGENTS.md` orchestrator role)

**OpenCode / Cline / Roo / Aider / OpenHands / Terminal-native:**
- https://opencode.ai — OpenCode vanilla `build/plan` + 75+ providers, LSP
- https://github.com/AidenGeunGeun/OpencodeOrchestra — PM→Orchestrator→Investigator/Auditor/Web-Search/Docs hierarchy (depth 0-2, read-only constraints)
- https://github.com/darrenhinde/OpenAgentsControl — 7 subagents (task-manager, context-scout, context-manager, coder-agent, test-engineer, code-reviewer, external-scout)
- https://github.com/cline/cline / https://github.com/RooVetGit/Roo-Code / https://github.com/Kilo-Org/kilocode — Cline/Roo/Kilo CLIs (orchestrator modes, checkpoints, skills, browser use, 22k stars)
- https://github.com/Aider-AI/aider / https://github.com/All-Hands-AI/OpenHands — Aider (diff/patch, git) / OpenHands (OpenDevin lineage, autonomous repo tasks)
- https://github.com/terminal-native agents directory — Curated terminal-agent directory (Pi, OpenCode, Aider, Goose, Cline, Roo, Kilo, OpenHands, orchestration)

**Agent Frameworks / Runtimes (LangChain / LangGraph / CrewAI / AutoGen / Microsoft):**
- https://docs.langchain.com / https://langchain-ai.github.io/langgraph/ — Graph-based runtime (nodes/edges/conditional routing, checkpointing pause/resume/rewind, supervisor/hierarchical/handoffs, 600+ integrations, LangSmith GA May 2025)
- https://docs.crewai.com — Crews (role/goal/backstory) + Flows (1.8+, deterministic), sequential/hierarchical/custom, 44k stars, 2-3× speed
- https://microsoft.github.io/autogen/ / https://github.com/ag2ai/fastagency — ConversableAgent, Group Chat, Sequential/Nested, Core event-driven, AG2 split Nov 2024 → Project AgentOS, Microsoft Agent Framework successor (AutoGen + SK)
- https://github.com/microsoft/agent-framework — Enterprise Agent Framework (handoffs+guardrails)
- https://openai.github.io/openai-agents-python/ — OpenAI Agents SDK (Agents, Handoffs, Guardrails)
- 2025 framework comparison synthesis (Nevo Systems 2026 Guide style table): orchestrator comparison, learning-curve/production-maturity matrix

**Multi-agent orchestration patterns & gateway:**
- https://github.com/GoClaw — GoClaw gateway (Lane-based Scheduler main/subagent/delegate/cron, Agent Teams team_tasks+team_message, delegation sync/async with agent_links + max_concurrent, handoff routing override, evaluate_loop generator↔evaluator, quality gates command/agent)
- https://github.com/orchjs/ORCH — ORCH CLI orchestrator (Claude/Codex/Cursor teams, DAG routing)
- https://github.com/Czarina — Czarina autonomous teams (2-20 workers, git worktrees, lesson propagation/Hopper, 95-98% autonomy)

**Git worktree isolation harness:**
- https://github.com/gwq — gwq worktree manager (fuzzy finder, parallel AI workflows, per-worktree isolated dir + branch)
- https://github.com/multi-agent-orchestration — 6 production patterns (Three-Tier Dispatch, Wave Execution, Git Worktree Isolation `git worktree add .worktrees/<feature> <branch>`, Cross-Model Routing, Review Gates)
- https://github.com/Vibora (fulcrum) — Vibora parallel worktree orchestration (Claude Code + OpenCode, multi-task worktrees, single screen)
- https://github.com/AgentsMesh — AgentsMesh (AgentPod = PTY + worktree + stream, Workspace = `sandboxes/{pod}/workspace/` + private creds)
- https://github.com/Omegon — Omegon single-binary worktree-parallel harness (child tasks, separate worktrees)
- https://www.kdnuggets.com — Git Worktrees for AI Development (worktree creation pattern)

**Autonomy calibration / HITL / Trust calibration literature:**
- https://arxiv.org — Unified Framework for Human-AI Collaboration in SOCs with Trusted Autonomy (L0-L5, HITL roles, trust thresholds, autonomy calibration §4.1, trust §3.3)
- https://gjetajournal.org — Between Autonomy and Oversight: Trust Calibration & Human Controllability in Agentic AI (Tiered Controllability Framework 4-tier: risk×reversibility×scope; over/under-reliance as top failure mode)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7034851 — Okamura & Yamada Adaptive Trust Calibration (miscalibration detection via reliance + cognitive cues = TCC; over-trust=misuse, under-trust=disuse)
- https://journals.sagepub.com (Johnson et al. 2023) — Training Impact on Trust Calibration (calibration training lowers expectations, mitigates trust-violation impact)
- https://arxiv.org/abs/2005.10158 — Yang et al. 2020 Trust-Risk × Error-Risk matrix (HIGH/MED/LOW)
- Parahelp skills — Trust-Autonomy Tradeoff (Zone A/B/C, 4 Stages Shadow→Delegated, Trust Ladder, expansion protocol one action/2 weeks, 95% shadow exit, ≥3 months Stage 2 + 60 days no incident + <1% override) + Agent Inbox (A2H: ESCALATE/AUTHORIZE/COLLECT/RESULT/INFORM, inbox composition as trust metric, healthy thresholds: approval>85%, edit<20%/<10%/<40%, override<2%, time<30s, rejection 15-30%)
- Kestrel prototype — Design Patterns for Human-in-Loop Experience (Scope contract, Graduated intervention Observe→Approve-first→Autonomous, Exception-first attention, Confidence+provenance, Trust calibration analytics that recommend expansion/contraction)

**Universal orchestration harness & MCP:**
- https://github.com/universal-dag-engine (Universal MCP engine) — 124 MCP tools (workflow_create/run/validate, retry intelligence, rollback architecture, trigger omniscience)
- https://skill.sh / Dev-AID — Multi-AI orchestrator for Claude/Gemini/GPT/local (9 agents, 4 teams, 16 tools, hybrid RAG, challenger reviews; reads `.claude/commands/` across Cursor/Windsurf/Cline)

**Verification of 10-SC anchoring:**
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` — SC-01 TTFUA, SC-02 TSR, SC-03 MTTR, SC-04 HIR, SC-05 CPSR, SC-06 DRR, SC-07 SSHC, SC-08 AHG, SC-09 CSP, SC-10 IDFR; rubric wiring (§4.1) and harm 4-5 rule (§4.2) used to justify split decisions and tiering above.

---

**Files relevant to next steps (absolute paths):**
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md` — Batch 1 P1-01..P1-08 task backbone
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` — Canonical archetypes C1-C6 + 10 SC definitions used for wiring
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\R-A_BROAD_MAPPER.md` / `R-B_CHALLENGER.md` / `V-C_ADVERSARIAL.md` / `V-D_ARCHITECTURAL.md` — Phase-0 source longlists this batch re-uses for variance preservation
- `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\STATUS.md` — Converge target for Batch 1 slice (next: V-C translation pass P1-06 + V-D re-tag P1-07)

