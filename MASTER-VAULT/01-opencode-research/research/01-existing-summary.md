# Phase 1 — Existing Research Summary

**Source:** 26-element OpenCode Ecosystem Research Catalog (sweep completed 2026-08-07/08)  
**Grand totals from catalog:** 163 usable resources | 43 excluded (Claude-Code-only)  
**Filter applied throughout:** Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard  
**Status:** ✅ All 26 elements summarized in full.

---

> **How to use this file:** Each element is one paragraph — enough to know what it covers without reloading the full catalog. For full detail on any element, refer to the original catalog files in `research/discovery/`.

---

## Element 1 — Skills (SKILL.md repos / collections)
**14 usable | 28 excluded (Claude-Code-only)**

The richest and most cross-tool category. The Agent Skills open standard (`agentskills.io`) has achieved broad adoption, with OpenCode natively discovering skills in `.agents/skills/` and `~/.config/opencode/skills/`. Top picks by stars: **obra/superpowers** (211k stars, 14 composable skills, dedicated OpenCode install docs), **anthropics/skills** (151k stars, Anthropic's official skills repo implementing the open spec), **mattpocock/skills** (130k stars, 17 dev-workflow skills), **addyosmani/agent-skills** (60k stars, 24 SDLC skills with explicit OpenCode setup docs), **[REDACTED-caveman]** (~92k stars, 65% token compression skill with OpenCode installer). Smaller but notable: **hardikpandya/stop-slop** (removes AI writing tells), **Gentleman-Programming/Gentleman-Skills** (Angular/React/Next.js/TypeScript stacks), **VoltAgent/awesome-agent-skills** (curated index of 1000+ skills from official dev teams), **cloudflare/skills** (Cloudflare Workers/Agents/Durable Objects), **waybarrios/opencode-power-pack** (55 skills ported to OpenCode with dedicated plugin), **hqhq1025/skill-optimizer** (skill mining/personalizing/generalizing lifecycle toolkit), **glebis/claude-skills** (~100 skills across meetings/research/writing/TDD). 28 repos excluded as Claude-Code-only plugin-marketplace exclusives with no documented OpenCode path (including garrytan/gstack, various SEO/IoT/Solana skills).

---

## Element 2 — Permission Modes (configs / presets)
**4 usable | 1 excluded**

OpenCode's native permission system is mature: granular `allow`/`ask`/`deny` rules per tool (bash, edit, write, webfetch, etc.), wildcard patterns, per-agent overrides, and `--auto` CLI flag. The ecosystem adds config examples and guard plugins rather than a centralized preset marketplace. **joelhooks/opencode-config** demonstrates production permission patterns (global `webfetch: deny`, per-agent boundaries). **kdcokenny/opencode-workspace** (555 stars) ships a full OCX profile with pre-configured role-based boundaries (plan=read-only, build=full, researcher=MCP-only, coder=full, scribe=write-only-no-bash, reviewer=read-only+git). **boxpositron/envsitter-guard** is a native OpenCode plugin that intercepts any agent attempt to read/edit `.env*` files and routes through a safe alternative. Excluded: Claude Code's Shift+Tab permission cycling (OpenCode has a feature request but not yet implemented).

---

## Element 3 — Checkpoints / Rewind Tools
**3 usable | 3 excluded**

OpenCode ships native `/undo` (git-based session rewind, restores file state and conversation, survives restarts). Two plugins extend this: **@arkfactory/opencode-checkpoint** adds automatic shadow-git checkpoints (5s debounce on edits, session-end and error checkpoints, interactive `/checkpoint-review` TUI for per-file accept/reject diffs). **witlox/opencode-checkpoint** adds named SQLite-backed checkpoints with explicit `checkpoint_create`/`checkpoint_list`/`checkpoint_restore`/`checkpoint_delete` tools, fork-based restore using OpenCode's `session.fork()` API, 100% test coverage. Excluded: pi-rewind (Pi-agent only), Claude Code `/rewind`, Cline Checkpoints.

---

## Element 4 — Context Management Tools
**15 usable | 2 excluded**

The richest category overall. Organized by scale: **Opencode-DCP/opencode-dynamic-context-pruning** (3.9k stars) does intelligent compression — replaces stale content with summaries before LLM requests, deduplicates repeated tool calls, purges errored inputs. **tickernelz/opencode-mem** (1.3k stars) provides persistent vector memory with auto-capture on idle, web UI at `127.0.0.1:4747`, and `memory` tool for add/search/list/forget. **0xranx/OpenContext** (715 stars) is a personal knowledge store with MCP server, desktop GUI, and web UI. **upstash/context7** (7k stars) is the standout docs MCP — fetches version-specific library documentation from source on demand. Large harnesses that bundle context management: **code-yeongyu/oh-my-openagent** (67.2k stars, auto-injects AGENTS.md/README.md, hash-anchored edits, session recovery, background agents) and **alvinunreal/oh-my-opencode-slim** (7.8k stars, 7 specialist agents with preset switching). **kdcokenny/opencode-background-agents** handles async delegation with results persisted to markdown surviving context compaction. Smaller plugins: opencode-conductor (Context→Spec→Plan→Implement lifecycle), IgorWarzocha context analysis (token visualization), oc-mnemoria (Rust hive-mind memory engine with BM25+semantic), supamem (Qdrant hybrid retrieval MCP), Hipocampo (PostgreSQL+pgvector+Gemini embeddings), opencode-short-term-memory (auto-summaries injected every few turns), MrDoe/OpenCodeRAG (local-first RAG with tree-sitter chunking+LanceDB), opencode-skillful (lazy-load skills on demand to reduce upfront context size).

---

## Element 5 — Hooks (collections / frameworks)
**6 usable | 2 excluded**

OpenCode hooks are primarily implemented as plugin event callbacks rather than standalone hook collections. Largest: **oh-my-openagent** (67.2k stars) with 54+ lifecycle hooks across session, tool calls, agent transitions, and background tasks. **oh-my-opencode-slim** (7.8k stars) integrates hooks with tmux/Zellij/kitty for live agent visibility. **smartfrog/opencode-froggy** (102 stars) is a focused hooks+agents+tools plugin providing Claude Code-style hooks bridged to OpenCode events. **Opencode Hooks Plugin** (from awesome-opencode) is an explicit adapter from Claude Code hooks format to OpenCode's plugin event system. **hcom** enables cross-agent hooks across terminals — OpenCode, Claude Code, Gemini CLI, and Codex agents can message each other, detect file edit collisions, read transcripts, and subscribe to activity. **FlowDeck** bundles 25 specialist agents with deep hooks for context monitoring, session idle summaries, and shell environment injection. Excluded: Claude Code native hooks and various Claude-Code-specific hook collections.

---

## Element 6 — MCP Servers
**9 usable | 2 excluded**

MCP is the great equalizer: any MCP server works with OpenCode natively via `opencode.json` config. Standout: **upstash/context7** (7k stars) — version-specific library docs from source on demand, the de facto docs MCP for all agents. **AlaeddineMessadi/opencode-mcp** uniquely exposes OpenCode itself as an MCP server, letting Claude/Cursor/VS Code/Cline delegate coding work to OpenCode (80 tools, 10 resources, 6 prompts, auto-starts OpenCode HTTP server). **ajhcs/Better-OpenCodeMCP** is an enhanced async version with process pooling, crash recovery, and 293 tests. From awesome-opencode: **Ejentum** provides reasoning/code/anti-deception/memory tools that agents call on-demand and receive structured prompts in return. **SwarmVault** bundles RAG knowledge-base compilation with MCP server. **supamem** is a Qdrant-backed dual-memory MCP. **OpenCode Chromium Browser Plugin** provides browser automation (screenshots, CDP, DOM actions, console/network). **Dodo Payments MCP** is an official payments plugin with two embedded MCP servers. **OpenCode Claude Memory** bridges memory between OpenCode and Claude Code using shared Markdown format. Excluded: Claude Code-specific MCP implementations with hardcoded config paths.

---

## Element 7 — Sandboxing Tools
**3 usable | 1 excluded**

OpenCode explicitly does NOT implement built-in sandboxing — official security docs state the permission system is a UX feature, not security isolation, and recommend Docker/VM for true isolation. **fabianlema/opencode-sandbox** (21 stars) is a Docker sandbox purpose-built for OpenCode with multi-arch support (AMD64 + ARM64/Apple Silicon), pre-installed dev tools (git, gh, python3, jq, node), non-root user, GHCR-hosted, and `opencode_here.sh` helper alias. **athal7/opencode-devcontainers** is a native OpenCode plugin for isolated branch workspaces via devcontainers (full container isolation) or git worktrees (lightweight filesystem isolation), with auto-port assignment and secret copying. **jailoc** (from awesome-opencode) provides containerized execution contexts as an OpenCode plugin. Excluded: Claude Code's built-in sandbox.

---

## Element 8 — Subagents (collections)
**15 usable | 2 excluded**

OpenCode's native subagent system (built-in `general`, `explore`, `scout` plus custom agents in `.opencode/agents/` or `~/.config/opencode/agents/`) has attracted the largest ecosystem after skills. **ankitmundada/awesome-opencode-subagents** is the definitive discovery hub with an interactive installer. Large bundles: **oh-my-openagent** (67.2k, 10+ specialist subagents, Team Mode for parallel execution), **oh-my-opencode-slim** (7.8k, 7 agents with Council for parallel model consensus), **kdcokenny/opencode-workspace** (555 stars, 4 role-based agents with pre-configured permissions). Innovative paradigms: **NERV** (SDD pipeline + A2A delegation hub + MAGI semantic memory + 9 specialist agents, scaffolds 45+ files via `nerv init`), **hiai-opencode** (canonical 12-agent model with skills/MCPs/LSP/ralph-loop), **Open Conclave** (multi-agent debates moderated by captain until consensus), **CrewBee** (task-specific reusable agent teams), **OpenCode Ensemble** (parallel agents with shared task board and git worktree isolation), **Pocket Universe** (closed-loop async subagents blocking main thread), **Gem Team** (self-learning multi-agent for spec-driven dev), **deliberation** (asks GPT/Gemini/Grok/OpenRouter as expert subagents via MCP — 7 experts, `ask-all` and `consensus` modes). Also: Python Expert Agent, OpenCode Agents, and Agentic (modular commands for structured dev). Excluded: Claude Code native subagents and Claude-Code-labeled collections without OpenCode ports.

---

## Element 9 — Plugins / Plugin Marketplaces
**6 usable | 2 excluded**

OpenCode has no official centralized marketplace yet (feature request #7467 is open). The ecosystem has self-organized around three discovery/installation tools: **awesome-opencode/awesome-opencode** is the de facto curated discovery hub (organized into plugins, themes, agents, projects). **CKGrafico/opencode-market** is a CLI that discovers and installs plugins from GitHub marketplaces (searches `marketplace.json` in `.github/plugin/` etc., supports `npx opencode-market install <plugin>@<marketplace>`). **NikiforovAll/opencode-marketplace** is a zero-config CLI with content-hash change detection, convention-based discovery (`.opencode/`, `.claude/`, `./commands/`), supporting commands, agents, and skills. **kdcokenny/ocx** is a registry-based package manager bundling plugins, skills, agents, and MCP servers into profiles. **OpenCode Manager** adds a mobile-first web UI for graphical plugin management. **opencode-agent-for-cowork** bridges Claude Desktop (Cowork) to OpenCode with 8 orchestration skills and per-project memory. Excluded: Claude Code Plugin Marketplace (individual plugins may be portable but the marketplace itself is Claude Code-only).

---

## Element 10 — Output Styles (themes)
**8 usable | 1 excluded**

OpenCode supports a JSON-based theme system (`~/.config/opencode/themes/`) with `opencode.json` theme key. **ajaxdude/opencode-ai-poimandres-theme** is the standout — minimal frameless dark theme with three variants including a WCAG AA accessible version (100% contrast ratio pass for all 24 critical color pairs). From awesome-opencode: **VS Code Themes for OpenCode** ports all built-in VS Code theme defaults (vscode-modern, vscode-plus, vscode-vs, vscode-hc) with automatic dark/light variant selection. **OpenCode Light Themes** is the largest collection — 21 carefully crafted light themes converted from popular VS Code themes (Solarized Light, GitHub Light, Quiet Light, Bluloco Light, and more). Smaller themes: **Ayu Dark** (golden yellow accent port), **Charcoal** (near-black grayscale, all 56 color keys in shades of gray), **Lavi** (soft dark purple tones, Nix flake support), **Moonlight** (cool-toned dark palette), **@franlol/opencode-md-table-formatter** (markdown table formatter plugin). Excluded: Claude Code native themes.

---

## Element 11 — Background Task Tools
**7 usable | 1 excluded**

Background task support in OpenCode is plugin-driven. **kdcokenny/opencode-background-agents** is the flagship — adds Claude Code-style async delegation: fire off tasks, continue working, retrieve results later; results persist to markdown surviving compaction and crashes; 15-minute timeout; read-only subagents only. **zenobi-us/opencode-background** handles raw process management (`createBackgroundProcess`, `listBackgroundProcesses`, `killProcesses`), captures last 100 lines of output, all processes killed on OpenCode close. **server-manager** (from awesome-opencode) specializes in dev server lifecycle (Node.js, Python, Go, .NET, Java, Rust, PHP) with JSON state persistence, HTTP health checks, and log grep. **opencode-scheduler** adds cron-style recurring jobs via launchd (Mac) or systemd (Linux). **opencode-notify** bridges background task events to OS native notifications (dbus on Linux, osascript on macOS) — shows project name, elapsed time, message preview. **Pilot** is an automation daemon polling GitHub issues and Linear tickets and dispatching tasks to OpenCode agents. Excluded: Claude Code native background tasks (kdcokenny's plugin explicitly mirrors this behavior).

---

## Element 12 — Security-Review Tools
**6 usable | 2 excluded**

Security review in OpenCode spans multiple layers. **alibaba/open-code-review** is a battle-tested hybrid tool (deterministic pipelines + LLM agent, precise line-level comments, multi-language ruleset) with an explicit OpenCode integration mode and a Delegation Mode where OpenCode runs the review. **waybarrios/opencode-power-pack** bundles `/security-review` as a first-class slash command (adapted from Anthropic's security-review skill). **opencode-review** (from awesome-opencode) automatically reviews staged changes on session idle with configurable cooldown, multi-dimension analysis (code quality, security, performance, testing, docs), severity levels, and auto-fix chain. **OpenCode Swarm** provides a multi-agent security verification pipeline (architect + independent review + test engineer + security checker + resumable evidence). **boxpositron/envsitter-guard** adds runtime `.env*` protection at the tool layer. **OpenAgentsControl** (4.6k stars) is a plan-first development framework with a built-in `CodeReviewer` security subagent and approval gates. Excluded: Anthropic's upstream claude-code-security-review skill (Claude Code native), Claude Code native security features.

---

## Element 13 — Headless / CI Setups
**6 usable | 1 excluded**

OpenCode's headless capabilities are first-class and native: `opencode run "<prompt>"` (one-shot with `--auto`, `--format json`, `--continue`, `--session`, `--fork`, `--mini` flags), `opencode serve --port 4096` (headless HTTP API), `opencode web --port 4096` (web UI), and `opencode github install` (GitHub agent). **wesammustafa/opencode-primer** is the definitive community guide covering `opencode run` for CI jobs, `opencode serve` for headless API, GitHub Actions workflows, GitLab CI recipes, and `--mini` lightweight mode. **OpenCode Manager** is a mobile-first web interface (Bun/Hono backend + React/Vite frontend, PWA support) wrapping OpenCode's headless server in a graphical UI. **AlaeddineMessadi/opencode-mcp** bridges any MCP client to OpenCode's headless API, enabling CI systems to delegate coding work to OpenCode via MCP. **Subagent Reporter** (from awesome-opencode) pipes subagent actions to stdout during `opencode run` sessions for CI visibility. **opencode-plugin-otel** exports session metrics/logs/traces via OTLP/gRPC to Datadog, Honeycomb, Grafana Cloud, etc. Excluded: Claude Code GitHub Actions templates (OpenCode has its own `opencode github install`).

---

## Element 14 — Usage / Cost Tracking Tools
**11 usable | 2 excluded**

This category is unusually dense. **eserete/opencode-token-tracker** (3 stars) displays real-time token usage, cost, and latency in the TUI sidebar footer updating every 2 seconds. **opgginc/opencode-bar** is a macOS menu-bar tracker reading `auth.json` directly, with color-coded progress (green→yellow→orange→red), daily tracking, EOM prediction, and add-on cost tracking. **ramtinJ95/opencode-tokenscope** turns session telemetry into readable reports via `/tokenscope` slash command. From awesome-opencode: **Token Monitor** tracks input/output/reasoning/cache tokens with daily ASCII charts, budget alerts, and per-agent/model cross-analysis. **OpenCode Throughput** monitors TTFT, TPS, latency, and cost per model in real-time. **Opencode Quota** adds toasts and quota tracking across providers. **Opencode Usage Monitor** shows API usage quotas for OpenAI and Z.AI providers. **Opencode Telemetry** is the most comprehensive — passive cross-session logging to local SQLite, turn-by-turn forensic inspection, aggregates costs across orchestration chains, zero cloud/network, `octm` CLI for reports without spending tokens. **opencode-mystatus** checks all AI subscription quotas in one command (OpenAI, Zhipu AI, Google Antigravity, and more). **Langfuse OpenCode Observability** traces user turns, assistant generations, tool calls, retries, reasoning output, compaction, and failed steps for team monitoring and debugging. **pai4451/opencode-telemetry-plugin** exports session telemetry via OTLP/gRPC. Excluded: Claude Code native cost tracking and usage dashboard.

---

## Element 15 — Agent-Team Frameworks
**17 usable | 4 excluded**

The largest category by far. **oh-my-openagent** (67.2k stars) is the mega-harness: 10+ specialist subagents, 54+ lifecycle hooks, LSP/AST tools, built-in MCPs, Team Mode for parallel execution with consensus. **oh-my-opencode-slim** (7.8k stars) is the lean version: 7 agents, tmux integration, Council for multi-model consensus, preset switching. **OpenAgentsControl** (4.6k stars) is a plan-first framework with approval-based execution, 3 main agents + 8+ specialized subagents, MVI context system (80% token reduction), multi-language support. **kdcokenny/opencode-workspace** (555 stars) bundles 4 role-based agents with pre-configured permission boundaries. **agnusdei1207/opencode-orchestrator** handles parallel sessions (up to 50) with Commander→Planner→Workers→Reviewer distribution. From awesome-opencode: **NERV** (SDD pipeline + A2A hub + MAGI memory + 9 subagents), **hiai-opencode** (12-agent canonical model), **CrewBee** (reusable task-specific agent teams), **OpenCode Ensemble** (parallel agents with shared task board + git worktree isolation), **Open Conclave** (multi-agent debates to consensus), **OpenCode Swarm** (verification-gated multi-agent pipeline), **FlowDeck** (25 specialist agents + 15 pre-built orchestration flows + AI Safety layer), **Open Dynamic Workflows** (dynamic local daemon for concurrent agents + adversarial verification + crash-resume), **Gem Team** (self-learning harness for spec-driven dev), **Pocket Universe** (closed-loop async subagents), **deliberation** (multi-model second opinions via MCP). Also: Claude Squad (TUI for parallel agents across tools, lists OpenCode in `-p` flag). Excluded: Claude Squad default mode, Vibe Kanban, Microsoft Conductor, Code Conductor (all Claude-Code-primary).

---

## Element 16 — Workflow Orchestration Tools
**12 usable | 3 excluded**

OpenCode's workflow orchestration ecosystem is mature and diverse. **mark-hingston/opencode-workflows** (Mastra engine) is the most structured — deterministic, auditable, resumable, composable workflows with five patterns (Sequential Chain, Parallel Experts, Tool-Augmented, Human-in-the-Loop, Conditional Routing), each step's output captured and reviewable, workflows persist to disk and survive restarts. **derekbar90/opencode-conductor** (121 stars) provides a clean protocol-driven lifecycle (Context→Spec→Plan→Implement) with named track commands. From awesome-opencode: **FlowDeck** is the richest (four-phase cycle: discuss→plan→execute→review, 25 agents, 24 skills, 15 flows, SDD, wave-based parallel execution, AI Safety layer with patch trust scoring and edit gates). **Open Dynamic Workflows** adds a local daemon generating orchestration scripts with adversarial verification and crash-resume. **opencode-bmad-workflow** implements the BMAD agile methodology (product management, architecture, development, QA agents). **GoopSpec** provides 5-phase spec-driven workflow (Plan→Research→Specify→Execute→Accept) with contract gates and 12 specialist subagents. **NERV** scaffolds complete SDD pipelines. **OpenCode Swarm** adds verification-gated quality gates. **Subtask2** extends `/commands` into a granular orchestration system. **ForLoop Planner** is an autopilot development platform covering the entire lifecycle. Smaller: **open-plan-annotator** (browser-based plan annotation UI with strikethrough/replace/comment) and **Opencode Roadmap** (strategic planning plugin). Excluded: Microsoft Conductor, conductor.build (Melty), Code Conductor (all Claude-Code-primary or closed-source).

---

## Element 17 — Agent SDKs
**3 usable | 2 excluded**

OpenCode's SDK ecosystem is intentionally lean. **anomalyco/opencode-sdk-js** (87 stars) is the official JS/TS SDK — handles sessions, file operations, streaming, plugin development, and programmatic agent control with type-safe hooks and context APIs. **anomalyco/opencode-sdk-go** is the official Go SDK — auto-generated via Fern for zero manual work per version bump. **Acksell/opencode-go-sdk** is a community Go SDK also generated with Fern. Note: there is no official Python SDK yet (issue #4031 tracks the request). Most OpenCode plugin development happens directly in JS/TS using `@opencode-ai/plugin` rather than through a standalone SDK. Excluded: Anthropic Agents SDK (Python, no OpenCode integration), Claude Code SDK (closed-source, no public SDK).

---

## Element 18 — Discipline / Skill Packs (methodology-level)
**4 usable | 1 excluded**

These are full development methodologies that agents follow, not just individual skills. **obra/superpowers** (211k stars) is the genre-defining example — 14 composable skills forming a complete software development methodology; auto-installs as OpenCode plugin via `plugin` config in `opencode.json`. **waybarrios/opencode-power-pack** (~460 stars) is the most thorough cross-tool port of Claude Code workflows: 55 skills in 7-phase feature development, security audit, frontend design, Hugging Face ML/training (13 skills), AWS/SageMaker cloud (5 skills). **meaningfy-ws/skillery** is a meta-collection bundling superpowers, stream-coding, and ponytail for OpenCode via standard SKILL.md directories. **DietrichGebert/ponytail** is a lighter-weight ruleset/discipline approach — loads as always-on context every session, registers `/ponytail` commands, ships skills activated when a task needs them; available as `opencode-ponytail` npm package. Excluded: Anthropic official Claude Code skills (upstream sources that the adapters above port from).

---

## Element 19 — Docs-Context MCP Servers
**3 usable | 1 excluded**

These solve the "stale training data" problem by injecting live documentation into context. **upstash/context7** (7k stars) is the undisputed leader — fetches version-specific library docs and code examples from source via `resolve-library-id` and `get-library-docs` tools; explicit OpenCode install docs for both remote (`https://mcp.context7.com/mcp`) and local (`npx -y @upstash/context7-mcp`) configurations. **sandbox-technologies/opencode-docs-mcp** gives agents direct access to OpenCode's own documentation (27 documents, 3 tools: SearchOpenCodeDocs, GetOpenCodeDocPage, BrowseOpenCodeDocs), self-hostable or remote at `https://tryinspector.com/api/opencode-docs/mcp`. **bgauryy/open-docs** is the deepest technical reference for OpenCode internals — 310+ pages, 520+ code examples, 100+ diagrams covering architecture, session management, tool system, LSP integration, ACP protocol, MCP integration, TUI/desktop/web implementations, and SDKs; a docs-context resource rather than a tool. Excluded: Claude Code native docs retrieval (built-in web search).

---

## Element 20 — Statusline Tools
**3 usable | 1 excluded**

OpenCode's statusline ecosystem is small but functional. The native status bar covers basics (active model, session state, tokens, agent mode). **Joaquinvesapa/sub-agent-statusline** adds critical multi-agent visibility — TUI sidebar plugin showing running/completed/failed subagents, elapsed time, and token/context usage; built with SolidJS for OpenTUI compatibility. **eserete/opencode-token-tracker** adds real-time cost awareness in the TUI sidebar footer updating every 2 seconds. Notable gap: Claude Code's customizable `statusLine` hook (pipes session state as JSON to a shell script after each message) is not yet available in OpenCode (feature requests #30295 and #8619 are open) — the above plugins partially fill this gap.

---

## Element 21 — Git-Worktree Helpers
**3 usable | 1 excluded**

Git worktree isolation is essential for AI-driven development to prevent agents from polluting the main branch. **kdcokenny/opencode-worktree** (701 stars, 35 forks) is the most popular — auto-spawns terminals, syncs files, runs post-create hooks (e.g., `pnpm install`), cleans up on exit; two tools (`worktree_create`, `worktree_delete`); supports Ghostty, Kitty, tmux; configurable via `.opencode/worktree.jsonc`. **felixAnhalt/opencode-worktree-session** takes an aggressive approach — every session automatically gets its own worktree, refuses to run on `main`, pivots the agent's cwd to the worktree, generates commit message via OpenCode API on exit, pushes to origin, removes worktree; available as `@tmegit/opencode-worktree-session` npm package. **athal7/opencode-devcontainers** offers the most flexibility, supporting both full container isolation and lightweight worktree isolation with auto-port assignment. Excluded: Claude Code native worktree support.

---

## Element 22 — Awesome-Lists (cross-tool, includes OpenCode)
**5 usable | 5 excluded (Claude-Code-only lists)**

Cross-tool awesome-lists that include OpenCode are scarce — most lists in this space are Claude Code-centric. **bradAGI/awesome-cli-coding-agents** (308 stars) is the best cross-tool discovery hub, listing 80+ terminal-native coding agents with OpenCode prominently featured (193k stars noted) alongside orchestrators like Claude Squad, hcom, and agent-of-empires. **ai-for-developers/awesome-ai-coding-tools** (1.7k stars) covers agents, MCP servers, skills, and harnesses with OpenCode in the Coding Agents section. **kyrolabs/awesome-agents** lists OpenCode under Software Development alongside Claude Engineer, Cline, Stakpak, ReviewCerberus, Dorothy, Greywall, Maestro. **awesome-opencode/awesome-opencode** is the canonical OpenCode-specific discovery hub (plugins, themes, agents, projects). **GetBindu/awesome-claude-code-and-skills** and **ai-boost/awesome-harness-engineering** (705 stars) provide supplementary cross-tool references. Excluded: hesreallyhim/awesome-claude-code (43k stars), VoltAgent/awesome-claude-code-subagents (19.6k), ComposioHQ/awesome-claude-skills (59k), travisvn/awesome-claude-skills (12k), rohitg00/awesome-claude-code-toolkit (1.6k) — all Claude-only.

---

## Element 23 — Security Scanners for Agent Configs
**3 usable | 2 excluded**

Security scanning for agent-driven development is an emerging category. **sandervandegeijn/code-security-scanner** is the most sophisticated — a thin Python wrapper around `opencode run` implementing a 6-phase methodology (Discovery → Dependency audit with osv-scanner → Per-file review → Confirmation pass → Semantic dedup → Business summary) with a dedicated read-only jail agent defined in `opencode.json` (denies bash, edit, write, patch, task, skill, webfetch, websearch). **zm2231/z-audit** provides a lighter 7-phase skill-based security audit (Stack Detection → Secrets & Credentials → Authentication & Authorization → API Security → Infrastructure-Specific → Security Headers & CORS → Dependencies → Data Exposure), explicitly labeled for Claude Code / OpenCode. **remorses/opencode-injection-guard** (15 stars) fills a critical niche — real-time prompt injection detection at the tool-output layer, intercepting bash/webfetch outputs via `tool.execute.after` hook and running them through a separate judge model before the main agent sees them. Gap identified: no generic "agent config linter" that audits opencode.json for overly permissive settings or dangerous tool combinations. Excluded: AgentLint (Claude Code plugin), SecureCodeWarrior/ai-security-rules (not a scanner).

---

## Element 24 — Safety-Net / Guardrail Tools
**5 usable | 2 excluded**

Safety in OpenCode is layered: **remorses/opencode-injection-guard** blocks prompt injection at the output layer (intercepts tool outputs via `tool.execute.after`, sends to judge model, replaces compromised output with warning). **boxpositron/envsitter-guard** prevents secret exfiltration at the tool level (intercepts any read/edit/write/patch on `.env*` paths). **Greywall** (from kyrolabs/awesome-agents list) provides deny-by-default command sandboxing with filesystem isolation, network control via transparent proxy, built-in OpenCode-specific profiles, and learning mode for auto-generating configs. **Daytona Sandbox Plugin** (official OpenCode plugin from Daytona) runs each session inside an isolated remote Daytona sandbox with complete kernel/filesystem/network isolation. **FlowDeck** embeds safety intelligence into workflow orchestration — patch trust scoring, edit gates, phase gating, arch constraint enforcement, failure replay, and regression prediction. Together these provide defense-in-depth: injection detection → secret protection → command sandboxing → full kernel isolation → workflow-level safety gates. Excluded: Claude Code native guardrails, claudebox (Claude Code-only sandbox).

---

## Element 25 — Hook Management CLIs
**2 usable | 2 excluded**

This category is essentially empty by design. OpenCode's hooks are managed as code (JS/TS plugins) rather than via a separate CLI — the plugin system auto-discovers hooks from `~/.config/opencode/plugins/` and `.opencode/plugins/`, so there's no need for a "hook install/enable/disable" CLI. **Opencode Hooks Plugin** (from awesome-opencode) bridges Claude Code hooks format to OpenCode's plugin event system. **OpenCode Native Plugin System** itself IS the hook management system — plugins are JS/TS modules returning hook objects (`tool.execute.before`, `tool.execute.after`, `session.idle`, `file.edited`, etc.). If you're looking for hook management, you're looking for plugin management (see Element 9). Excluded: Claude Code native hooks, various Claude Code hook collections.

---

## Element 26 — Self-Improving / Instinct-Mining Tools
**3 usable | 2 excluded**

A nascent but important category forming a complete skill lifecycle. **okdk7788/opencode-self-improving-skills** is the standout — a native OpenCode plugin running an autonomous loop: `distill_skill` captures reusable techniques as SKILL.md from session evidence; `optimize_skill` runs GEPA-style measured improvement (collect evidence → generate candidates → judge → Pareto-select → human-gated apply) grounded in failure traces; `curator_status` and `evolution_status` provide on-demand visibility; installs to `~/.config/opencode/plugins/self-improving-skills/` and auto-loads at startup. **hqhq1025/skill-optimizer** (~125 stars) provides the complementary mining and publication layer: `skill-miner` scans coding-agent history and repeated work to surface workflow-worthy patterns (covers Codex, Claude Code, Gemini, Antigravity, exported transcripts); `skill-personalizer` audits installed skills for undertriggering/overtriggering; `skill-generalizer` strips private paths/credentials to make skills publishable. **thousandflowers/skillreaper** (47 stars) approaches from the opposite direction — evidence-based pruning: reads real session transcripts to find skills/MCP servers/agents loaded but never fired, then safely quarantines dead weight; explicitly lists OpenCode in supported platforms alongside Claude Code, Codex, Cursor. Excluded: jo-inc/pi-reflect (Pi-only), sentient-agi/EvoSkill (Claude Code primary).

---

## Final Totals (confirmed from catalog)

| Metric | Count |
|---|---|
| Elements covered | 26 of 26 |
| Total usable resources | 163 |
| Total excluded (Claude-Code-only) | 43 |

---

## Cross-Cutting Observations (full picture)

1. **MCP and SKILL.md are the two universal standards.** Anything built on either works with OpenCode natively. The ecosystem has broadly converged on these two formats as the lingua franca for cross-tool compatibility.

2. **oh-my-openagent (67.2k stars) appears in 5+ categories** (context management, hooks, subagents, background tasks, agent-team frameworks) — it is the single most comprehensive OpenCode harness in the catalog, functioning as an everything-bundle for power users.

3. **OpenCode has no built-in sandboxing** — an explicit design choice documented in official security docs. Docker/devcontainers are the recommended path. The small ecosystem around this reflects the "use Docker" recommendation being sufficient for most users.

4. **The "permission boundary + specialist subagent" pattern** (kdcokenny/opencode-workspace, oh-my-opencode-slim, NERV, OpenAgentsControl) is the dominant architecture for multi-agent OpenCode setups — every major multi-agent framework independently converged on this design.

5. **Context7 (7k stars) is the standout docs MCP** — should be in any serious OpenCode setup regardless of other choices. It solves the stale training data problem cleanly and non-intrusively.

6. **Self-improvement is a real category now** — okdk7788's opencode-self-improving-skills + skill-optimizer + skillreaper form a complete lifecycle (mine → distill → optimize → prune) that didn't exist in previous generations of coding agents.

7. **Cost/usage tracking is overdeveloped relative to its importance** — 11 distinct tools for cost tracking vs. 3 for sandboxing, despite sandboxing being the more critical safety gap. Reflects community priorities (cost visibility is visible; security gaps are not).

8. **Biggest real ecosystem gap: no official OpenCode marketplace.** Feature request #7467 is open. The community has built 4 different workarounds (awesome-opencode, opencode-market, opencode-marketplace, OCX) reflecting real demand.

9. **The customizable statusLine hook** (Claude Code feature requests #30295 and #8619) is the most cited missing feature in the catalog — it would let users pipe session state to arbitrary shell scripts for custom displays, notifications, and CI integration.
