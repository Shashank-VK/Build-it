# OpenCode Ecosystem Research — Master Index

> Full sweep of 26 elements completed: 2026-08-07/08
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

| # | Element | Usable | Excluded | File |
|---|---------|--------|----------|------|
| 1 | Skills (SKILL.md repos/collections) | 14 | 28 | [01-skills.md](01-skills.md) |
| 2 | Permission modes (configs/presets) | 4 | 1 | [02-permission-modes.md](02-permission-modes.md) |
| 3 | Checkpoints / rewind tools | 3 | 3 | [03-checkpoints-rewind.md](03-checkpoints-rewind.md) |
| 4 | Context management tools | 15 | 2 | [04-context-management.md](04-context-management.md) |
| 5 | Hooks (collections/frameworks) | 6 | 2 | [05-hooks.md](05-hooks.md) |
| 6 | MCP servers | 9 | 2 | [06-mcp-servers.md](06-mcp-servers.md) |
| 7 | Sandboxing tools | 3 | 1 | [07-sandboxing-tools.md](07-sandboxing-tools.md) |
| 8 | Subagents (collections) | 15 | 2 | [08-subagents.md](08-subagents.md) |
| 9 | Plugins / plugin marketplaces | 6 | 2 | [09-plugins-marketplaces.md](09-plugins-marketplaces.md) |
| 10 | Output styles | 8 | 1 | [10-output-styles.md](10-output-styles.md) |
| 11 | Background task tools | 7 | 1 | [11-background-tasks.md](11-background-tasks.md) |
| 12 | Security-review tools | 6 | 2 | [12-security-review-tools.md](12-security-review-tools.md) |
| 13 | Headless / CI setups | 6 | 1 | [13-headless-ci.md](13-headless-ci.md) |
| 14 | Usage / cost tracking tools | 11 | 2 | [14-usage-cost-tracking.md](14-usage-cost-tracking.md) |
| 15 | Agent-team frameworks | 17 | 4 | [15-agent-team-frameworks.md](15-agent-team-frameworks.md) |
| 16 | Workflow orchestration tools | 12 | 3 | [16-workflow-orchestration.md](16-workflow-orchestration.md) |
| 17 | Agent SDKs | 3 | 2 | [17-agent-sdks.md](17-agent-sdks.md) |
| 18 | Discipline/skill packs | 4 | 1 | [18-discipline-skill-packs.md](18-discipline-skill-packs.md) |
| 19 | Docs-context MCP servers | 3 | 1 | [19-docs-context-mcp.md](19-docs-context-mcp.md) |
| 20 | Statusline tools | 3 | 1 | [20-statusline-tools.md](20-statusline-tools.md) |
| 21 | Git-worktree helpers | 3 | 1 | [21-git-worktree-helpers.md](21-git-worktree-helpers.md) |
| 22 | Awesome-lists (cross-tool) | 5 | 5 | [22-awesome-lists.md](22-awesome-lists.md) |
| 23 | Security scanners for agent configs | 3 | 2 | [23-security-scanners.md](23-security-scanners.md) |
| 24 | Safety-net / guardrail tools | 5 | 2 | [24-safety-net-guardrails.md](24-safety-net-guardrails.md) |
| 25 | Hook management CLIs | 2 | 2 | [25-hook-management-clis.md](25-hook-management-clis.md) |
| 26 | Self-improving / instinct-mining tools | 3 | 2 | [26-self-improving-instinct-mining.md](26-self-improving-instinct-mining.md) |

---

**Grand totals:** 163 usable resources | 43 excluded (Claude-Code-only)


---

# Element 1: Skills (SKILL.md repos / collections)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard (Agent Skills spec, AGENTS.md, .agents/skills/)

---

## Well-known / high-star

**[obra/superpowers](https://github.com/obra/superpowers)** — 211,860 stars, actively maintained — Complete agentic skills framework & software development methodology built on 14 composable skills (brainstorming, TDD, systematic-debugging, code review, git-worktrees, subagent-driven-development, etc.). — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/INSTALL.md` and `docs/README.opencode.md`; explicit install command provided.

**[anthropics/skills](https://github.com/anthropics/skills)** — 151,088 stars, actively maintained — Anthropic's official public agent skills repository. Contains the Agent Skills specification, skill template, and 15+ example skills (docx, pdf, pptx, xlsx, algorithmic art, canvas design, MCP builder, webapp testing, brand guidelines, etc.). — OpenCode support: **Open standard** — Agent Skills spec (agentskills.io) is the open standard OpenCode natively implements; OpenCode discovers `.agents/skills/` and `SKILL.md` files directly.

**[mattpocock/skills](https://github.com/mattpocock/skills)** — 130,016 stars, actively maintained — "Skills for Real Engineers." 17+ dev workflow skills including `/grill-me`, `/tdd`, `/diagnosing-bugs`, `/code-review`, `/triage`, `/wayfinder`, `/improve-codebase-architecture`. Installable via `npx skills` or Claude Code plugin. — OpenCode support: **Open standard** — pure SKILL.md format installable via `npx skills add mattpocock/skills` which writes to `.agents/skills/`; no proprietary lock-in.

**[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** — 60,265 stars, actively maintained — Production-grade engineering skills covering the full SDLC: 24 skills across DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP. Includes anti-rationalization tables, verification gates, and Google engineering culture patterns. — OpenCode support: **Documented port/adapter exists** — explicit `docs/opencode-setup.md` describes AGENTS.md + `skill` tool integration.

**[[REDACTED-caveman]](https://github.com/[REDACTED-caveman])** — ~92,000 stars, actively maintained — Token-compression skill that cuts 65% of output tokens by making agents talk in terse [REDACTED]-speak. Six compression levels, [REDACTED]-commit, [REDACTED]-review, [REDACTED]-stats. Supports 30+ agents. — OpenCode support: **Documented port/adapter exists** — explicit OpenCode install instructions in README; curl/pipe installer detects OpenCode and drops skill into `~/.config/opencode/skills/`.

**[hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)** — 13,400 stars, maintained — Skill for removing AI tells and "slop" from prose. Banned phrases, structural clichés, sentence-level rules, and 1-10 scoring rubric. — OpenCode support: **Open standard** — plain SKILL.md + references/ directory; copy to `.agents/skills/` or `~/.config/opencode/skills/`.

**[Gentleman-Programming/Gentleman-Skills](https://github.com/Gentleman-Programming/Gentleman-Skills)** — actively maintained, community-driven — Curated + community skills for Angular, React 19, Next.js 15, TypeScript, Tailwind, Zod, Zustand, AI SDK, Django, Playwright, pytest, Jira, and more. Democratic voting for community contributions. — OpenCode support: **Native** — explicitly documents OpenCode's native skill directory (`~/.config/opencode/skills/`) in README.

**[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** — actively maintained — Curated awesome-list of 1000+ agent skills from official dev teams (Anthropic, Google, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, etc.) and community. Hand-picked, not AI-generated. — OpenCode support: **Open standard** — catalog of SKILL.md repos; explicitly lists OpenCode in compatibility matrix and provides `~/.config/opencode/skills/` path.

**[cloudflare/skills](https://github.com/cloudflare/skills)** — actively maintained, official — Skills for teaching agents how to build on Cloudflare: Workers, Agents SDK, Durable Objects, Wrangler, web-perf, MCP servers (cloudflare-api, cloudflare-docs, cloudflare-bindings). — OpenCode support: **Native** — explicitly documents OpenCode install path (`~/.config/opencode/skills/`) and `npx skills add` support.

**[composiohq/skills](https://github.com/composiohq/skills)** (composio-community/skills) — actively maintained — Distributable agent skills for Composio developers. Tool Router best practices, Triggers & Events, production patterns. Uses AGENTS.md + SKILL.md dual format. — OpenCode support: **Open standard** — AGENTS.md consolidated file format that OpenCode natively reads; also standard SKILL.md directories.

**[waybarrios/opencode-power-pack](https://github.com/waybarrios/opencode-power-pack)** — ~460 stars, actively maintained — 55 rigorous skills ported from Claude Code workflows to Codex, OpenCode, and Pi. Code review, security audit, feature development, frontend design, MCP tools, Hugging Face ML/training. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit `opencode plugin --global` install docs; registers skills as slash commands automatically.

**[hqhq1025/skill-optimizer](https://github.com/hqhq1025/skill-optimizer)** — ~125 stars, actively maintained — Agent Skills lifecycle toolkit: `skill-miner` (mine repeated workflows from session history), `skill-personalizer` (audit and tune skills to your habits), `skill-generalizer` (turn personal skills into publishable ones). — OpenCode support: **Native** — explicitly documents OpenCode path (`~/.config/opencode/skills/`) and `npx skills add` compatibility.

**[glebis/claude-skills](https://github.com/glebis/claude-skills)** — actively maintained — ~100 skills for Claude Code covering meetings & transcripts, research & knowledge, writing & publishing, image/audio generation, TDD, app release, personal analytics, and Claude Code ops. — OpenCode support: **Open standard** — installable via `npx skills add glebis/claude-skills` which writes standard SKILL.md files to `.agents/skills/`.

**[agentskills/agentskills](https://github.com/agentskills/agentskills)** — actively maintained — The official Agent Skills specification repository. Defines the open SKILL.md format, progressive disclosure model, and directory structure. — OpenCode support: **Open standard** — this IS the specification that OpenCode natively implements.

---

## Actively maintained but smaller

**[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** — maintained — Multi-category skill pack: system architecture (Clean Architecture, SOLID, ADR), automated code review, iOS dev, Go with LLM subagents, strategic decision-making, brand voice, SEO. — OpenCode support: **Open standard** — plain SKILL.md format; copy to `.agents/skills/`.

**[steipete/agent-rules](https://github.com/steipete/agent-rules)** — maintained — Rules and knowledge to work better with agents. Archived Cursor rules adapted for cross-agent use. Static prompt templates with no runtime code. — OpenCode support: **Open standard** — static markdown; install script writes to `~/.claude/CLAUDE.md` but content is portable to OpenCode's AGENTS.md.

**[FrancyJGLisboa/agent-skill-creator](https://github.com/FrancyJGLisboa/agent-skill-creator)** — maintained — Meta-skill that teaches agents to create complete agents autonomously. Cross-platform generator for 14+ AI tools. Writes to `~/.agents/skills/` and `~/.claude/skills/`. — OpenCode support: **Open standard** — writes to `.agents/skills/` which OpenCode discovers natively.

**[tripleyak/SkillForge](https://github.com/tripleyak/SkillForge)** — maintained — Ultimate meta-skill for generating best-in-class Claude Code skills. 4-phase architecture with Python validation scripts. — OpenCode support: **Open standard** — SKILL.md output format.

**[alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory)** — maintained — Toolkit for building production-ready skills, agents, and slash commands at scale. 10 slash commands and 5 agents for generating skills. — OpenCode support: **Open standard** — writes output to `~/.claude/skills/` in portable SKILL.md format.

**[NeoLabHQ skills](https://github.com/NeoLabHQ)** (code-review, reflexion, sdd, ddd, sadd, kaizen) — maintained — Engineering methodology skills: spec-driven dev, domain-driven dev, self-refinement loops, continuous improvement. — OpenCode support: **Open standard** — SKILL.md format.

**[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** — maintained — Comprehensive best practices guide covering agents, commands, skills, hooks, workflows, and orchestration patterns. — OpenCode support: **Claimed but unverified** — repo exists and discusses cross-tool patterns but no explicit OpenCode install docs found.

---

## Old or possibly abandoned

*(None identified in this sweep — all listed repos show recent 2026 activity or are official team repos with ongoing maintenance.)*

---

## Claude-Code-only, excluded

The following resources are Claude-Code-only with no documented OpenCode path. Listed here so nothing gets silently lost:

- **garrytan/gstack** — 110,407 stars. 28 skills turning Claude Code into a virtual engineering team. No OpenCode port found.
- **Donchitos/Claude-Code-Game-Studios** — 48 AI agents and 36 workflows for Claude Code.
- **Lum1104/Understand-Anything** — Turns codebase into interactive knowledge base via Claude Code.
- **UfoMiao/zcf** — Zero-config code flow for Claude Code and Codex only.
- **zilliztech/claude-context** — Code search MCP for Claude Code only.
- **wanshuiyin/Auto-claude-code-research-in-sleep** — Autonomous ML research skill for Claude Code.
- **PeonPing/peon-ping** — Warcraft III voice notifications for Claude Code/Codex/Gemini CLI.
- **zubair-trabzada/geo-seo-claude** — GEO-first SEO skill, Claude-specific install.
- **mukul975/Anthropic-Cybersecurity-Skills** — 753 cybersecurity skills, Claude-branded.
- **OthmanAdi/planning-with-files** — Manus-style planning for Claude Code.
- **conorluddy/ios-simulator-skill** — iOS simulator automation for Claude Code.
- **michalparkola/tapestry-skills** — Productivity skills for Claude Code.
- **axiaoge2/Apple-Hig-Designer** — Apple HIG skill for Claude Code.
- **BrownFineSecurity/iothackbot** — IoT pentesting skill for Claude Code.
- **forayconsulting/gemini_cli_skill** — Teaches Claude Code to invoke Gemini CLI.
- **rokpiy/auto-commenter** — Reddit comment bot skill for Claude Code.
- **solana-foundation/solana-dev-skill** — Solana dev skill for Claude Code.
- **aaron-he-zhu/seo-geo-claude-skills** — SEO/GEO skills for Claude Code.
- **Ceeon/videocut-skills** — AI video editing skill for Claude Code.
- **huangserva/skill-prompt-generator** — AI image prompt generation skill for Claude Code.
- **nidhinjs/prompt-master** — Universal SEO skill with 19 sub-skills for Claude Code.
- **blader/humanizer** — Remove AI writing patterns skill for Claude Code.
- **muratcankoylan/ralph-wiggum-marketer** — Autonomous copywriter plugin for Claude Code.
- **zscole/adversarial-spec** — Multi-model debate system, Claude Code plugin.
- **slavingia/skills** — Business advice skills based on The Minimalist Entrepreneur, Claude Code plugin marketplace.
- **sanjay3290/claude-skills** (imagen, etc.) — Claude-specific skills.
- **jeffallan/claude-skills** — 65 full-stack dev skills, Claude-branded.
- **AgriciDaniel/claude-seo** — Universal SEO skill for Claude Code.
- **makenotion/claude-code-notion-plugin** — Notion integration plugin, Claude Code only.

---

## Summary

- **Element:** Skills (SKILL.md repos / collections)
- **Total found:** 14 usable + 28 excluded (Claude-Code-only)
- **Key insight:** The Agent Skills open standard (agentskills.io) has achieved broad cross-tool adoption. Almost every major skill collection now supports OpenCode either natively (via `.agents/skills/` or `~/.config/opencode/skills/`) or via documented adapters. The highest-star repos (Superpowers, Anthropic skills, Matt Pocock skills, Addy Osmani agent-skills, [REDACTED]) all explicitly document OpenCode installation. The main gap is Claude Code plugin-marketplace exclusives that haven't been ported.
- **File path:** `research/discovery/01-skills.md`


---

# Element 2: Permission Modes (configs / presets)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[OpenCode Built-in Permission System](https://opencode.ai/docs/permissions/)** — Core feature of OpenCode, actively maintained — Granular permission framework with `allow` / `ask` / `deny` rules per tool (bash, edit, write, webfetch, etc.). Supports wildcard `*` patterns, per-agent overrides, and `--auto` CLI flag for auto-approve mode. — OpenCode support: **Native**

**[joelhooks/opencode-config](https://github.com/joelhooks/opencode-config)** — actively maintained — Personal OpenCode configuration repository demonstrating production permission patterns: global `webfetch: deny`, per-agent permission boundaries (plan=read-only, build=full, explore=filesystem-only), and `.env` read protections. — OpenCode support: **Native** — pure `opencode.json` config.

**[kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace)** — 555 stars, actively maintained — Bundled multi-agent orchestration harness with pre-configured permission boundaries: global `webfetch: deny`, plan/build agents as read-only orchestrators delegating via `task` tool, researcher with MCP-only access, coder with full file+bash, scribe with write-only no-bash, reviewer with read-only+git. — OpenCode support: **Native** — ships as OCX profile with permission presets.

---

## Actively maintained but smaller

**[boxpositron/envsitter-guard](https://github.com/boxpositron/envsitter-guard)** — actively maintained — OpenCode plugin that blocks agents/tools from reading or editing sensitive `.env*` files while providing safe EnvSitter-backed alternatives (keys, fingerprints, scans, mutations without exposing values). Hooks into OpenCode's tool system to intercept `read`/`edit`/`write`/`patch` on `.env*` paths. — OpenCode support: **Native** — OpenCode plugin using tool hooks.

---

## Old or possibly abandoned

*(None identified — permission mode tooling is either built into OpenCode core or actively maintained as plugins.)*

---

## Claude-Code-only, excluded

- **Claude Code Shift+Tab permission cycling** — Claude Code's native runtime permission mode toggle (Normal/Plan/Auto). OpenCode has a feature request for this but it's not yet implemented.

---

## Summary

- **Element:** Permission Modes (configs/presets)
- **Total found:** 4 usable + 1 excluded
- **Key insight:** OpenCode's permission system is mature and native. The ecosystem around it consists of config examples (joelhooks, kdcokenny workspace) and guard plugins (envsitter-guard) rather than standalone "permission mode" tools. There is no centralized "preset marketplace" for permissions yet — users share configs as GitHub repos.
- **File path:** `research/discovery/02-permission-modes.md`


---

# Element 3: Checkpoints / Rewind Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[OpenCode Native /undo](https://opencode.ai/docs/)** — Core feature, actively maintained — Built-in session rewind via `/undo` command. Restores file state and conversation to previous turn. Git-based snapshotting under the hood. Survives restarts. — OpenCode support: **Native**

**[@arkfactory/opencode-checkpoint](https://www.npmjs.com/package/@arkfactory/opencode-checkpoint)** — actively maintained — Automatic checkpoint plugin for OpenCode. Creates shadow git repository in `.opencode/checkpoints/`, auto-checkpoints on file edits (5s debounce), session end, and errors. Interactive TUI (`/checkpoint-review`) for visual diff review with accept/reject per file. — OpenCode support: **Native** — OpenCode plugin.

**[witlox/opencode-checkpoint](https://github.com/witlox/opencode-checkpoint)** — actively maintained — Named checkpoint plugin for OpenCode with SQLite storage. `checkpoint_create`, `checkpoint_list`, `checkpoint_restore`, `checkpoint_delete` tools. Fork-based restore using OpenCode's `session.fork()` API. Optional git commit tracking. 100% test coverage. — OpenCode support: **Native** — OpenCode plugin using official session APIs.

---

## Actively maintained but smaller

*(No additional smaller repos found in this sweep.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **pi-rewind** (arpagon/pi-rewind) — Excellent checkpoint/rewind extension for the Pi coding agent. Researched 11 coding agents including OpenCode, but is Pi-only. No OpenCode port.
- **Claude Code /rewind** — Native to Claude Code only.
- **Cline Checkpoints** — Cline-editor native feature.

---

## Summary

- **Element:** Checkpoints / Rewind Tools
- **Total found:** 3 usable + 3 excluded
- **Key insight:** OpenCode has solid native `/undo` support. The plugin ecosystem adds two complementary approaches: @arkfactory's automatic shadow-git checkpoints with TUI review, and witlox's named SQLite-backed checkpoints with explicit tool APIs. Both leverage OpenCode's native plugin architecture and session APIs. No major gap exists here.
- **File path:** `research/discovery/03-checkpoints-rewind.md`


---

# Element 4: Context Management Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[Opencode-DCP/opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)** — 3,894 stars, actively maintained — Intelligent context compression plugin for OpenCode. Replaces stale conversation content with high-fidelity summaries before LLM requests. Two modes: `range` (contiguous spans) and `message` (individual messages). Deduplication of repeated tool calls, purge of errored tool inputs after N turns. Session history never modified — only pruned content sent to LLM. — OpenCode support: **Native** — OpenCode plugin.

**[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** — 1,300+ stars, actively maintained — Persistent memory plugin for OpenCode using local vector database. Auto-capture extracts technical context on idle, injects relevant memories into chat. Manual `memory` tool for add/search/list/forget. Web UI at `127.0.0.1:4747`. Public subpath exports for third-party plugins. — OpenCode support: **Native** — OpenCode plugin with auto-capture and web UI.

**[0xranx/OpenContext](https://github.com/0xranx/OpenContext)** — 715 stars, actively maintained — Personal context/knowledge store for AI agents. Reuses existing coding agent CLI (Codex/Claude/OpenCode). `oc` CLI for global `contexts/` library, MCP server for agent integration, desktop GUI, web UI. Skills + slash commands for Cursor/Claude Code/Codex. — OpenCode support: **Native** — explicit OpenCode config path (`~/.config/opencode/`) documented; MCP server works with OpenCode.

**[upstash/context7](https://github.com/upstash/context7)** — 7,072 stars, actively maintained — Context7 MCP server: up-to-date code documentation for LLMs. Fetches version-specific docs and code examples straight from source. `resolve-library-id` and `get-library-docs` tools. Supports OpenCode via MCP config. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers MCP servers.

**[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** — 67.2k stars, actively maintained — Multi-model agent orchestration harness for OpenCode. Context injection (auto-inject AGENTS.md, README.md, conditional rules), hash-anchored edit tool, session recovery, LSP/AST tools, built-in MCPs (Exa websearch, Context7 docs, Grep.app). 54+ lifecycle hooks, background agents, Team Mode with parallel agents. — OpenCode support: **Native** — OpenCode plugin with deep context management.

**[alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)** — 7.8k stars, actively maintained — Lightweight multi-agent orchestration for OpenCode. Seven specialized agents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background orchestration, bundled skills, Council for parallel model consensus, preset switching (`/preset`), LSP/AST tools, built-in MCPs. — OpenCode support: **Native** — OpenCode plugin.

**[kdcokenny/opencode-background-agents](https://github.com/kdcokenny/opencode-background-agents)** — actively maintained — Async background delegation for OpenCode. Delegate research tasks, continue working, retrieve results later. Results persisted to `~/.local/share/opencode/delegations/` as markdown. Survives context compaction. Three tools: `delegate`, `delegation_read`, `delegation_list`. — OpenCode support: **Native** — OpenCode plugin.

**[derekbar90/opencode-conductor](https://github.com/derekbar90/opencode-conductor)** — 121 stars, actively maintained — Protocol-driven workflow plugin for OpenCode. Context → Spec → Plan → Implement lifecycle. `/conductor:setup`, `/conductor:newTrack`, `/conductor:implement`, `/conductor:status`, `/conductor:revert` commands. Persistent planning state. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[IgorWarzocha/Opencode-Context-Analysis-Plugin](https://github.com/IgorWarzocha/Opencode-Context-Analysis-Plugin)** — maintained — Token usage analysis plugin for OpenCode. Visual breakdown of token distribution across tools (read, bash, webfetch, etc.). Bar charts showing percentages and counts. `/context` command. — OpenCode support: **Native** — OpenCode plugin.

**[oc-mnemoria](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Persistent shared memory (hive mind) for OpenCode agents across sessions. Rust engine with hybrid BM25 + semantic search, CRC32 checksum chains, append-only binary format. 7 tools and `/mn-*` slash commands. — OpenCode support: **Native** — OpenCode plugin.

**[supamem](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Project-agnostic dual-memory MCP CLI for OpenCode. Semantic memory (Qdrant tuned hybrid retrieval: dense MiniLM + sparse BM25) and structural memory hooks. Installer wires `qdrant-find` / `qdrant-store` tools. — OpenCode support: **Native** — MCP server + OpenCode plugin installer.

**[Hipocampo](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Dual memory system (PostgreSQL + pgvector + Gemini Embeddings) for AI coding agents. BIRE algorithm (unified semantic + lexical search, auto-tagging, hybrid scoring, GIN trigram indexes). Ships as opencode skill with SKILL.md. — OpenCode support: **Native** — OpenCode skill.

**[opencode-short-term-memory](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Automatically summarizes conversation context into structured session memory and injects it back into the system prompt every few turns. Preserves user instructions, project context, decisions, active references across long chats and compactions. — OpenCode support: **Native** — OpenCode plugin.

**[MrDoe/OpenCodeRAG](https://github.com/MrDoe/OpenCodeRAG)** — maintained — Local-first RAG plugin for OpenCode. Semantic code search with tree-sitter chunking (19 languages), LanceDB, incremental indexing, file-change detection, watch mode. Ollama or OpenAI embeddings. CLI + OpenCode plugin with chunk retrieval tool. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-skillful](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Allow OpenCode agents to lazy-load prompts on demand with skill discovery and injection. Reduces upfront context size by only loading skills when needed. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified in this sweep.)*

---

## Claude-Code-only, excluded

- **Claude Code native context compaction** — Built into Claude Code only; OpenCode has its own compaction system.
- **Claude Code memory system** — Claude Code's persistent memory; OpenCode has opencode-mem as the cross-tool equivalent.

---

## Summary

- **Element:** Context Management Tools
- **Total found:** 15 usable + 2 excluded
- **Key insight:** This is the richest category so far. OpenCode has a thriving ecosystem of context management plugins: DCP (3.9k stars) for intelligent pruning, opencode-mem (1.3k stars) for persistent vector memory, OpenContext (715 stars) as a personal knowledge store, and massive harnesses like oh-my-openagent (67.2k stars) and oh-my-opencode-slim (7.8k stars) that bundle context injection, session recovery, and background agents. The MCP standard enables cross-tool docs servers like Context7 (7k+ stars) to work natively with OpenCode.
- **File path:** `research/discovery/04-context-management.md`


---

# Element 5: Hooks (collections / frameworks)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** — 67.2k stars, actively maintained — Multi-model agent orchestration harness with 54+ lifecycle hooks (61 with Team Mode), all configurable via `disabled_hooks`. Hooks cover session lifecycle, tool calls, agent transitions, background task events, and more. Full Claude Code compatibility layer with hook parity. — OpenCode support: **Native** — OpenCode plugin with extensive hook system.

**[alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)** — 7.8k stars, actively maintained — Lightweight multi-agent orchestration plugin with deep system hooks for agent lifecycle, task delegation, and context monitoring. Hooks integrate with tmux/Zellij/kitty multiplexers for live agent visibility. — OpenCode support: **Native** — OpenCode plugin.

**[smartfrog/opencode-froggy](https://github.com/smartfrog/opencode-froggy)** — 102 stars, maintained — OpenCode plugin providing Claude Code-style hooks, specialized agents, and tools like gitingest. Hooks for session events, file operations, and agent transitions. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[Opencode Hooks Plugin](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Use Claude Code hooks definition and hook them to opencode hooks. Bridges Claude Code's hook format to OpenCode's plugin event system. — OpenCode support: **Documented port/adapter exists** — explicit adapter from Claude Code hooks to OpenCode hooks.

**[hcom](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Let AI agents message, watch, and spawn each other across terminals. Claude Code, Gemini CLI, Codex CLI, and OpenCode agents in separate terminals can message each other, detect file edit collisions, read transcripts, view terminal screens, subscribe to activity, and spawn/fork/resume agents. First-class OpenCode support with native plugin. TUI dashboard, cross-device relay, Python API. — OpenCode support: **Native** — OpenCode plugin with cross-agent hook integration.

**[FlowDeck](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — AI-powered multi-agent workflow orchestration with deep system hooks: context monitoring, session idle summaries, shell environment injection. 25 specialist agents, 24 workflow skills, 17 workflow commands, persistent state via `.planning/STATE.md`. — OpenCode support: **Native** — OpenCode plugin with deep hooks.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native hooks** (`pre-tool`, `post-tool`, `session-start`, etc.) — Built into Claude Code only. The Opencode Hooks Plugin provides an adapter for some of these.
- **claude-code-hooks** community collections — Various Claude Code-specific hook collections with no OpenCode port.

---

## Summary

- **Element:** Hooks (collections/frameworks)
- **Total found:** 6 usable + 2 excluded
- **Key insight:** OpenCode's hook ecosystem is dominated by large orchestration harnesses (oh-my-openagent with 54+ hooks, oh-my-opencode-slim) rather than standalone "hook collections." The Froggy plugin (102 stars) provides a focused hooks+agents toolkit. The Opencode Hooks Plugin explicitly bridges Claude Code hook definitions to OpenCode. hcom enables cross-agent hooks across different CLI tools. Hooks in OpenCode are primarily plugin-event-driven rather than traditional git-style hooks.
- **File path:** `research/discovery/05-hooks.md`


---

# Element 6: MCP Servers

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[upstash/context7](https://github.com/upstash/context7)** — 7,072 stars, actively maintained — Context7 MCP server: up-to-date code documentation for LLMs. `resolve-library-id` and `get-library-docs` tools fetch version-specific docs and code examples. Community-contributed library index. Works with any MCP client including OpenCode. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers and connects MCP servers via `opencode.json`.

**[AlaeddineMessadi/opencode-mcp](https://github.com/AlaeddineMessadi/opencode-mcp)** — actively maintained — MCP server that bridges any MCP client (Claude, Cursor, Windsurf, VS Code, Cline, Zed, Amazon Q) to OpenCode's headless API. 80 tools, 10 resources, 6 prompts. Auto-starts OpenCode HTTP server in-process. Multi-project support. — OpenCode support: **Open standard** — MCP server exposing OpenCode's capabilities to any MCP client; OpenCode itself can also consume MCP servers.

**[ajhcs/Better-OpenCodeMCP](https://github.com/ajhcs/Better-OpenCodeMCP)** — actively maintained — Enhanced MCP server for OpenCode CLI. Async task execution, process pooling, crash recovery, 293 tests. Bridges Claude to Gemini, DeepSeek, and other models via OpenCode's multi-model capabilities. Interactive setup wizard. — OpenCode support: **Open standard** — MCP server.

---

## Actively maintained but smaller

**[Ejentum](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — MCP server with four tools (`harness_reasoning`, `harness_code`, `harness_anti_deception`, `harness_memory`) that AI agents call on demand. Each returns a structured prompt the calling agent ingests before generating. — OpenCode support: **Open standard** — MCP server.

**[SwarmVault](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Local-first RAG knowledge base compiler with bundled skill and MCP server. Turns raw docs, research, and code into persistent markdown wiki, knowledge graph, and hybrid SQLite FTS + embeddings search. Works with OpenCode, Claude Code, and Codex. — OpenCode support: **Open standard** — MCP server + OpenCode skill.

**[supamem](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Project-agnostic dual-memory MCP CLI for OpenCode. Semantic memory (Qdrant hybrid retrieval: dense MiniLM + sparse BM25) and structural memory hooks. Installer wires `qdrant-find` / `qdrant-store` tools. — OpenCode support: **Open standard** — MCP server.

**[OpenCode Chromium Browser Plugin](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Browser automation MCP for Chromium-based browsers (Chrome, Edge, Brave). Manifest V3 extension + Node.js native messaging host. Screenshots, CDP commands, DOM actions, downloads, console/network inspection. — OpenCode support: **Native** — OpenCode plugin with MCP-style browser tools.

**[Dodo Payments MCP](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Official Dodo Payments plugin bundles two MCP servers: live API server with browser OAuth, and documentation search server. Checkout, subscriptions, webhooks, usage-based billing, credits, license keys. — OpenCode support: **Native** — OpenCode plugin with embedded MCP servers.

**[OpenCode Claude Memory](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Share persistent Markdown memory between OpenCode and Claude Code using Claude Code-compatible paths and file formats. Cross-tool memory bridge. — OpenCode support: **Open standard** — uses shared file format readable by both tools.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native MCP client** — Claude Code can consume MCP servers but its MCP implementation is proprietary. OpenCode can consume the same MCP servers via standard MCP protocol.
- **Various Claude Desktop-only MCP servers** — Any MCP server that hardcodes Claude Desktop config paths without supporting generic MCP clients.

---

## Summary

- **Element:** MCP Servers
- **Total found:** 9 usable + 2 excluded
- **Key insight:** MCP is the great equalizer — any MCP server works with OpenCode natively via the open Model Context Protocol standard. Context7 (7k+ stars) is the standout docs MCP server. The opencode-mcp project is unique: it exposes OpenCode itself as an MCP server, letting other tools delegate coding work to OpenCode. The ecosystem is rich with memory MCPs (supamem, SwarmVault), browser automation, payments, and reasoning harnesses (Ejentum). OpenCode's native MCP client support means the entire MCP registry (thousands of servers) is available.
- **File path:** `research/discovery/06-mcp-servers.md`


---

# Element 7: Sandboxing Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[fabianlema/opencode-sandbox](https://github.com/fabianlema/opencode-sandbox)** — 21 stars, actively maintained — Docker sandbox environment for running OpenCode AI agents with all necessary dev tools pre-installed (git, gh, python3, jq, node). Multi-architecture (AMD64 + ARM64/Apple Silicon). Runs as non-root user (`node`). GHCR-hosted with `opencode_here.sh` helper alias (`oh`). Config persisted to `~/.config/opencode-sandbox/`. — OpenCode support: **Native** — Docker container purpose-built for OpenCode; official OpenCode docs recommend Docker/VM for true isolation.

**[athal7/opencode-devcontainers](https://github.com/athal7/opencode-devcontainers)** — actively maintained — OpenCode plugin for isolated branch workspaces using devcontainers or git worktrees. Auto-assigned ports (13000–13099), session state management, automatic copying of gitignored secrets (.env, credentials), unified workspace cleanup. Supports both full container isolation (devcontainers) and lightweight filesystem isolation (worktrees). — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[jailoc](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Sandboxed Docker environments for OpenCode agents. Provides containerized execution contexts for agent operations. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native sandbox** — Claude Code runs in a sandboxed environment by default. OpenCode does not; it relies on external sandboxing (Docker, devcontainers) as documented in its security model.

---

## Summary

- **Element:** Sandboxing Tools
- **Total found:** 3 usable + 1 excluded
- **Key insight:** OpenCode explicitly does NOT implement built-in sandboxing — its security docs state the permission system is a UX feature, not security isolation, and recommend Docker/VM for true isolation. The ecosystem fills this gap with fabianlema's Docker sandbox (21 stars) and athal7's devcontainer/worktree plugin. This is a smaller category because the official recommendation is "use Docker," which many users do without a dedicated tool.
- **File path:** `research/discovery/07-sandboxing-tools.md`


---

# Element 8: Subagents (collections)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[ankitmundada/awesome-opencode-subagents](https://github.com/ankitmundada/awesome-opencode-subagents)** — actively maintained — Definitive curated collection of specialized AI assistants for OpenCode CLI. Categories cover full-stack development tasks. Interactive installer script (`install-agents.sh`) with browse/select/install/uninstall flow. Agents install to `~/.config/opencode/agents/` (global) or `.opencode/agents/` (project). — OpenCode support: **Native** — drops into OpenCode's native agent discovery paths.

**[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** — 67.2k stars, actively maintained — Multi-model orchestration harness bundling 10+ specialized subagents (Explorer, Oracle, Librarian, Designer, Fixer, etc.) with background task management, LSP/AST tools, MCP servers, and 54+ lifecycle hooks. Team Mode with parallel agent execution. — OpenCode support: **Native** — OpenCode plugin.

**[alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)** — 7.8k stars, actively maintained — Lightweight multi-agent orchestration with 7 specialized subagents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background task management, LSP/AST tools, tmux integration for live agent visibility, MCP servers. — OpenCode support: **Native** — OpenCode plugin.

**[kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace)** — 555 stars, actively maintained — Bundled multi-agent harness with 4 specialist subagents: researcher (MCP-only, read-only), coder (full file+bash), scribe (write-only, no bash), reviewer (read-only+git). Pre-configured permission boundaries and planning protocols. — OpenCode support: **Native** — OpenCode plugin + OCX profile.

**[NERV](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure for AI agents. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI), and 9 specialized subagents for OpenCode. Scaffolds 45+ files via `nerv init` including SDD skills, slash commands, MCP servers, and lifecycle plugins. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

**[hiai-opencode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Canonical 12-agent model with bundled skills, MCP servers, LSP integration, and ralph-loop. 10 visible agents (Bob, Coder, Strategist, Critic, Guard, Researcher, Designer, Manager, Brainstormer, Vision) plus hidden Sub and Agent Skills. — OpenCode support: **Native** — OpenCode plugin.

**[Open Conclave](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Multi-agent debates moderated by a captain agent until consensus. Each agent has a different system prompt (logical, creative, research-focused). Configurable provider/model per agent. — OpenCode support: **Native** — OpenCode plugin.

**[CrewBee](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Task-specific Agent Teams for OpenCode. Define reusable task/project-specific agent teams, project them into OpenCode agents, switch between single-agent and multi-agent collaboration. Built-in Coding Team template with review flow and completion criteria. — OpenCode support: **Native** — OpenCode plugin.

**[OpenCode Ensemble](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Parallel agent teams for OpenCode. Coordinate parallel agents with peer messaging, shared task board, git worktree isolation, and live dashboard. — OpenCode support: **Native** — OpenCode plugin.

**[Pocket Universe](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Subagent-driven pocket universe for primary agent. Extends native OpenCode subagent paradigm to provide closed-loop, resilient, async agents that block main thread execution. Three tools for parallel subagent communication and coordination. — OpenCode support: **Native** — OpenCode plugin.

**[Gem Team](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Self-learning multi-agent orchestration harness for spec-driven development and automated verification. — OpenCode support: **Native** — OpenCode plugin.

**[deliberation](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Ask GPT, Gemini, Grok, or OpenRouter for a second opinion or fix as expert subagents over MCP. Seven expert subagents (Architect, Plan Reviewer, Scope Analyst, Code Reviewer, Security Analyst, Researcher, Debugger). `ask-all` asks every model at once; `consensus` runs an arbiter loop. — OpenCode support: **Open standard** — MCP server + OpenCode plugin.

**[Python Expert Agent for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Custom configurable agent toolkit with 1 primary custom agent (`python-expert`) plus predefined specialized subagents for code generation, review, testing, and exploration. On-demand skills and context files for standards/patterns/security. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[OpenCode Agents](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — A set of opencode configurations, prompts, agents, and plugins for enhanced development workflows. — OpenCode support: **Native** — OpenCode plugin/configs.

**[Agentic](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Modular AI agents and commands for structured software development with OpenCode. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native subagents** (`/task`, `/review`, etc.) — Built into Claude Code only; OpenCode has its own `task` tool and subagent system.
- **Various "Claude Code subagents" collections** — Many repos labeled "Claude Code subagents" with no OpenCode port or documented adapter.

---

## Summary

- **Element:** Subagents (collections)
- **Total found:** 15 usable + 2 excluded
- **Key insight:** This is a massive category. OpenCode's native subagent system (general, explore, scout built-ins + custom agents in `.opencode/agents/`) has attracted a rich ecosystem. The ankitmundada awesome-list is the definitive discovery hub. Large orchestration harnesses (oh-my-openagent 67.2k stars, oh-my-opencode-slim 7.8k stars, kdcokenny workspace 555 stars) bundle multiple specialist subagents with permission boundaries. NERV, hiai-opencode, and Pocket Universe provide innovative subagent paradigms (SDD pipeline, 12-agent model, closed-loop async). The deliberation plugin uniquely uses MCP to bring multi-model consensus into OpenCode.
- **File path:** `research/discovery/08-subagents.md`


---

# Element 9: Plugins / Plugin Marketplaces

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode)** — actively maintained, community-driven — The de facto curated marketplace/discovery hub for the OpenCode ecosystem. Organized into plugins, themes, agents, and projects. Each entry links to its repository with description and install instructions. The closest thing to an "app store" for OpenCode. — OpenCode support: **Native** — discovery list of native OpenCode plugins.

**[CKGrafico/opencode-market](https://github.com/CKGrafico/opencode-market)** — actively maintained — CLI to discover, install, and manage OpenCode agent plugins from GitHub marketplaces. Registers marketplaces from GitHub repos (searches `marketplace.json` in `.github/plugin/`, `.claude-plugin/`, or root). `npx opencode-market install <plugin>@<marketplace> [--local|--opencode]`. Supports both OpenCode and Claude Code marketplace formats. — OpenCode support: **Native** — CLI tool purpose-built for OpenCode plugin discovery/installation.

**[NikiforovAll/opencode-marketplace](https://github.com/NikiforovAll/opencode-marketplace)** — actively maintained — CLI marketplace for OpenCode plugins. Install from local directories or GitHub URLs. Zero-config convention-based discovery (`.opencode/`, `.claude/`, `./command/`, `./commands/`). Content-hash based change detection. Supports commands, agents, and skills. User-global or project-local scope. `bunx opencode-marketplace install <url>`. — OpenCode support: **Native** — CLI tool purpose-built for OpenCode.

**[kdcokenny/ocx](https://github.com/kdcokenny/ocx)** (OCX Ecosystem) — actively maintained — Registry-based plugin manager for OpenCode. `ocx add kdco/workspace --from https://registry.kdco.dev`. Bundles plugins, skills, agents, and MCP servers into profiles. Dependency management and automatic updates. — OpenCode support: **Native** — purpose-built registry and package manager for OpenCode.

---

## Actively maintained but smaller

**[OpenCode Manager](https://github.com/chriswritescode-dev/opencode-manager)** — actively maintained — Mobile-first web interface for OpenCode AI agents. Repository management, chat/session control, Git/file tools, schedules, AI configuration, MCP server management, plugin management, push notifications, PWA support. Runs as Bun/Hono backend + React/Vite frontend with supervised OpenCode server. — OpenCode support: **Native** — web UI that manages OpenCode plugins and MCP servers.

**[opencode-agent-for-cowork](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Cowork (Claude desktop) plugin that bridges natural language conversations with OpenCode. Handles agent routing, stall detection, result validation, per-project operational memory, provider fallback chain, MCP composability. Ships 8 orchestration skills, 3 scheduled-task recipes, 1 custom agent template. — OpenCode support: **Native** — bridges Cowork to OpenCode.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code Plugin Marketplace** — Official Claude Code marketplace (Claude Code Switch, etc.). No OpenCode compatibility layer found for the marketplace itself, though individual plugins may be portable via opencode-market or opencode-marketplace.
- **Claude Desktop plugins** — Various Claude Desktop-only plugins with no OpenCode path.

---

## Summary

- **Element:** Plugins / Plugin Marketplaces
- **Total found:** 6 usable + 2 excluded
- **Key insight:** OpenCode has no official centralized marketplace yet (feature request #7467 is open). The ecosystem has self-organized around three discovery/installation tools: (1) awesome-opencode as the curated discovery hub, (2) CKGrafico's opencode-market for GitHub-marketplace-style installs, (3) NikiforovAll's opencode-marketplace for zero-config local/GitHub installs, and (4) kdcokenny's OCX as a registry-based package manager. These four tools together provide a robust decentralized marketplace experience. The OpenCode Manager web UI adds a graphical layer for plugin management.
- **File path:** `research/discovery/09-plugins-marketplaces.md`


---

# Element 10: Output Styles

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[ajaxdude/opencode-ai-poimandres-theme](https://github.com/ajaxdude/opencode-ai-poimandres-theme)** — actively maintained — Minimal, frameless dark theme for OpenCode inspired by the poimandres VS Code theme. Semantic color coding, optimized for truecolor terminals. Three variants: original (100% aesthetic), turquoise-expanded, and accessible (WCAG AA compliant — 100% contrast ratio pass for all 24 critical color pairs). Install via `/theme` command or `opencode.json`. — OpenCode support: **Native** — OpenCode theme format (`~/.config/opencode/themes/`).

**[VS Code Themes for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Ports of all built-in VS Code themes from the vscode.theme-defaults extension: vscode-modern, vscode-plus, vscode-vs, vscode-hc. Automatic dark/light variant selection. One-line install script. — OpenCode support: **Native** — OpenCode theme format.

**[OpenCode Light Themes](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Largest collection of light themes for OpenCode. 21 carefully crafted light themes converted from popular VS Code themes: scaefy-light, Solarized Light, Vivid Light, Coffee Cream, GitHub Light, Quiet Light, Bluloco Light, Brackets Light Pro, NetBeans Light, Ysgrifennwr, Hop Light, GitHub Plus, Classic Light, HC Flurry, all Milkshake variants. Bilingual EN/TR docs, one-command install. — OpenCode support: **Native** — OpenCode theme format.

---

## Actively maintained but smaller

**[Ayu Dark Theme for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Port of the popular Ayu Dark color scheme with golden yellow accent. — OpenCode support: **Native** — OpenCode theme format.

**[Charcoal Theme for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Deep-black grayscale theme for OpenCode — no hues, all shades of gray. Near-black (#0d0d0d) background. All 56 theme color keys use shades of gray. Also available for bat and Ghostty. — OpenCode support: **Native** — OpenCode theme format.

**[Lavi Theme for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Soft, sweet dark theme with rich purple tones. Part of the Lavi colorscheme family (Neovim, Alacritty, Ghostty, Kitty, Wezterm, Zellij, etc.). Nix flake and home-manager support. — OpenCode support: **Native** — OpenCode theme format.

**[Moonlight Theme for OpenCode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Moonlight color theme based on the popular moonlight-vscode-theme by atomiks. Dark, cool-toned palette inspired by moonlight aesthetics. — OpenCode support: **Native** — OpenCode theme format.

**[@franlol/opencode-md-table-formatter](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode / kdcokenny workspace) — maintained — Markdown table formatting plugin for OpenCode. Part of the OCX workspace bundle. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native themes** — Built into Claude Code only; no theme system equivalent found for OpenCode beyond the JSON theme format.

---

## Summary

- **Element:** Output Styles
- **Total found:** 8 usable + 1 excluded
- **Key insight:** OpenCode supports a JSON-based theme system (themes in `~/.config/opencode/themes/`). The standout is ajaxdude's poimandres theme with its WCAG AA accessible variant. The awesome-opencode list catalogs 25+ themes including a massive 21-theme light collection and ports of popular VS Code themes. This is a smaller but well-curated category — themes are easy to create (JSON format) so the barrier to entry is low.
- **File path:** `research/discovery/10-output-styles.md`


---

# Element 11: Background Task Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[kdcokenny/opencode-background-agents](https://github.com/kdcokenny/opencode-background-agents)** — actively maintained — Claude Code-style async background delegation for OpenCode. Fire off research tasks, continue working, retrieve results later. Three tools: `delegate(prompt, agent)`, `delegation_read(id)`, `delegation_list()`. Results persisted to `~/.local/share/opencode/delegations/` as markdown — survive context compaction, session restarts, and crashes. Read-only subagents only (write-capable agents must use native `task` tool). 15-minute timeout. Lifecycle parity with Claude Code background agents. — OpenCode support: **Native** — OpenCode plugin.

**[zenobi-us/opencode-background](https://github.com/zenobi-us/opencode-background)** — actively maintained — Background process management plugin for OpenCode. `createBackgroundProcess` (shell command, name, tags, global/session scope), `listBackgroundProcesses` (filter by session/status/tags), `killProcesses` (by ID/session/status/tags). Tracks in-memory with singleton manager. Captures last 100 lines of output. States: pending, running, completed, failed, cancelled. ALL processes killed when OpenCode closes. — OpenCode support: **Native** — OpenCode plugin.

**[server-manager](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Non-blocking background server management for OpenCode. Start, track, and stop local dev servers without blocking the AI session. Supports Node.js, Python, Go, .NET, Java, Rust, PHP, and any framework with a dev server. JSON state persistence, per-project log files, HTTP health checks, log tail/grep for debugging. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-scheduler](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list / docs ecosystem) — actively maintained — Schedule recurring jobs using launchd (Mac) or systemd (Linux) with cron syntax. Integrates with OpenCode's task system. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-notify](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list / docs ecosystem) — actively maintained — Native OS notifications for OpenCode. Know when background tasks complete, error, need approval, or wait for input. dbus (Linux) and osascript (macOS). Shows project name, elapsed time, message preview. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[Pilot](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Automation daemon that polls for work from GitHub issues and Linear tickets. Runs as a background process, dispatches tasks to OpenCode agents. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-background-agents](https://opencode.ai/docs/ecosystem/)** (from official docs ecosystem list) — actively maintained — Same as kdcokenny's background agents — listed in official OpenCode ecosystem documentation. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native background tasks** — Built into Claude Code only. OpenCode's kdcokenny background-agents plugin explicitly mirrors this behavior.

---

## Summary

- **Element:** Background Task Tools
- **Total found:** 7 usable + 1 excluded
- **Key insight:** Background task support in OpenCode is plugin-driven. kdcokenny's background-agents is the flagship — it adds Claude Code-style async delegation with persistence that survives compaction and crashes. zenobi-us's opencode-background handles raw process management (create/list/kill). server-manager specializes in dev server lifecycle. opencode-scheduler adds cron-style recurring jobs, and opencode-notify bridges background task events to the OS notification system. Together these provide comprehensive background task capabilities comparable to Claude Code's native system.
- **File path:** `research/discovery/11-background-tasks.md`


---

# Element 12: Security-Review Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** — actively maintained, official Alibaba project — Fast, efficient, battle-tested code review tool with hybrid architecture: deterministic pipelines + LLM Agent. Precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection). OpenAI & Anthropic compatible. Delegation mode lets coding agents run the review. — OpenCode support: **Documented port/adapter exists** — explicit "OpenCode" integration in docs: install native review tools and slash commands; also supports Delegation Mode where OpenCode runs the review.

**[waybarrios/opencode-power-pack](https://github.com/waybarrios/opencode-power-pack)** — ~460 stars, actively maintained — Bundles `/security-review` as a first-class slash command. 45 rigorous skills including security audit, code review, feature development. Security-review skill is a licensed adaptation from Anthropic's `claude-code-security-review`. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit OpenCode install docs.

**[opencode-review](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Automatic structured code review plugin for OpenCode CLI. Reviews staged changes when session goes idle, with configurable cooldown, multi-dimension analysis (code quality, security, performance, testing, documentation), severity levels, and auto-fix chain support. — OpenCode support: **Native** — OpenCode plugin.

**[OpenCode Swarm](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, and resumable evidence. Multi-agent security review pipeline. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[boxpositron/envsitter-guard](https://github.com/boxpositron/envsitter-guard)** — actively maintained — Prevents agents/tools from reading or editing sensitive `.env*` files, while allowing safe inspection via EnvSitter (keys + deterministic fingerprints; never values). Hooks into OpenCode's tool system. — OpenCode support: **Native** — OpenCode plugin.

**[OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** — 4.6k stars, actively maintained — Plan-first development framework with built-in security analysis subagent (`CodeReviewer`). Approval gates, pattern-based security validation, context-aware security standards. — OpenCode support: **Native** — OpenCode agent framework with security subagent.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Anthropic claude-code-security-review** — The upstream security review skill that waybarrios/power-pack adapted. Claude Code native.
- **Claude Code native security features** — Built-in security analysis in Claude Code only.

---

## Summary

- **Element:** Security-Review Tools
- **Total found:** 6 usable + 2 excluded
- **Key insight:** Security review in OpenCode spans three layers: (1) Alibaba's open-code-review as a standalone tool with explicit OpenCode integration, (2) waybarrios' power-pack bundling security-review as a slash command, (3) opencode-review as an automatic idle-time code review plugin, and (4) OpenCode Swarm for multi-agent security verification. The envsitter-guard plugin adds runtime .env protection. OpenAgentsControl provides a framework-level security subagent with approval gates.
- **File path:** `research/discovery/12-security-review-tools.md`


---

# Element 13: Headless / CI Setups

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[OpenCode Native Headless Mode](https://opencode.ai/docs/)** — Core feature, actively maintained — Three headless interfaces built into OpenCode: (1) `opencode run "<prompt>"` for one-shot prompts with `--auto`, `--format json`, `--continue`, `--session`, `--fork`, `--mini` flags; (2) `opencode serve --port 4096` for headless HTTP API; (3) `opencode web --port 4096` for web UI. GitHub agent via `opencode github install`. Session export/import, stats tracking. — OpenCode support: **Native**

**[wesammustafa/opencode-primer](https://github.com/wesammustafa/opencode-primer)** — actively maintained — Comprehensive community guide covering headless CI setup: `opencode run` for scripts/CI jobs, `opencode serve` for headless API, GitHub Actions workflows, GitLab CI recipes. `--auto` flag for CI-only auto-approve. `--mini` lightweight mode (v1.17.10+). — OpenCode support: **Native** — documentation/guide for native OpenCode headless features.

**[OpenCode Manager](https://github.com/chriswritescode-dev/opencode-manager)** — actively maintained — Mobile-first web interface for OpenCode AI agents. Runs as supervised OpenCode server with Bun/Hono backend + React/Vite frontend. Repository management, chat/session control, Git/file tools, schedules, AI configuration, MCP server management. PWA support. — OpenCode support: **Native** — wraps OpenCode's headless server in a web UI.

**[AlaeddineMessadi/opencode-mcp](https://github.com/AlaeddineMessadi/opencode-mcp)** — actively maintained — MCP server bridging any MCP client to OpenCode's headless API. 80 tools, 10 resources, 6 prompts. Auto-starts OpenCode HTTP server in-process. Multi-project support. Enables CI systems to delegate coding work to OpenCode via MCP. — OpenCode support: **Open standard** — MCP server exposing OpenCode headless API.

---

## Actively maintained but smaller

**[Subagent Reporter](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Pipes subagent actions/events directly to stdout during `opencode run` sessions, prefixes them with subagent names, enumerates parallel subagents. Essential for CI visibility when subagents are involved. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-plugin-otel](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — OpenTelemetry telemetry exporter for OpenCode sessions. Exports metrics, logs, traces via OTLP/gRPC to any OTel backend (Datadog, Honeycomb, Grafana Cloud). Instruments session lifecycle, token usage, cost, tool durations, git commits. CI observability. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code GitHub Actions** — Claude Code's native GitHub integration workflows. No OpenCode equivalent for the specific GitHub Actions templates, though OpenCode has its own `opencode github install`.

---

## Summary

- **Element:** Headless / CI Setups
- **Total found:** 6 usable + 1 excluded
- **Key insight:** OpenCode's headless capabilities are first-class: `opencode run`, `opencode serve`, and `opencode web` are all native. The ecosystem adds the opencode-mcp bridge (enabling any MCP client to use OpenCode in CI), the OpenCode Manager web UI, and the Subagent Reporter for CI visibility. OpenTelemetry plugin adds observability for production CI deployments. The wesammustafa primer is the definitive community guide for CI setup.
- **File path:** `research/discovery/13-headless-ci.md`


---

# Element 14: Usage / Cost Tracking Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[eserete/opencode-token-tracker](https://github.com/eserete/opencode-token-tracker)** — 3 stars, actively maintained — Real-time token usage, cost, and latency tracking for every AI request in OpenCode. TUI sidebar footer display: `⏳ last: in: 70.0k · out: 1.2k · 1 req · $0.04` / `📊 total: in: 1.2m · out: 0.3m · 42 reqs · $1.23`. Updates every 2 seconds during execution. Install via curl to `~/.config/opencode/plugins/token-tracker.tsx` + `tui.json` registration. — OpenCode support: **Native** — OpenCode TUI plugin.

**[opgginc/opencode-bar](https://github.com/opgginc/opencode-bar)** — actively maintained — macOS menu-bar token usage tracker for OpenCode. Auto-detects providers from `auth.json`. Multi-path support. Color-coded progress (green→yellow→orange→red). Daily tracking, EOM prediction, add-on cost tracking. Per-provider subscription settings. Launch at login. Sparkle auto-updates. — OpenCode support: **Native** — reads OpenCode's `auth.json` directly.

**[ramtinJ95/opencode-tokenscope](https://github.com/ramtinJ95/opencode-tokenscope)** — actively maintained — Comprehensive token usage analysis and cost tracking for OpenCode sessions. Turns telemetry into readable reports. npm installable (`@ramtinj95/opencode-tokenscope`). `/tokenscope` slash command. Session-scoped analysis. — OpenCode support: **Native** — OpenCode plugin.

**[Token Monitor](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Token analysis & cost tracking with budgets, trends, and per-project analytics. Tracks input/output/reasoning/cache tokens, estimates costs, daily trends with ASCII charts, budget alerts, export data. Per-agent breakdown, agent×model cross-analysis, project-scoped analytics. — OpenCode support: **Native** — OpenCode plugin.

**[OpenCode Throughput](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Real-time LLM performance monitoring. Tracks TTFT, TPS, latency, token usage, and cost per model. Toast notifications + TUI sidebar display. — OpenCode support: **Native** — OpenCode plugin.

**[Opencode Quota](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Quota toasts and token tracking across providers. Automatic toasts and slash commands. — OpenCode support: **Native** — OpenCode plugin.

**[Opencode Usage Monitor](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — OpenCode sidebar plugin displaying API usage quotas for OpenAI and Z.AI providers. Per-model breakdown, spend tracking, configurable refresh controls. — OpenCode support: **Native** — OpenCode plugin.

**[Opencode Telemetry](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Passive cross-session telemetry to local SQLite. Logs every session automatically — tokens, tool calls, skills, per-turn cost. Aggregates costs across orchestration chains (conductor + child sessions). Turn-by-turn forensic inspection. `octm` CLI for reports without spending model tokens. Zero cloud, zero network. — OpenCode support: **Native** — OpenCode plugin.

**[opencode-mystatus](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Check all AI subscription quotas in one command. Supports OpenAI (Plus/Pro/Codex), Zhipu AI, Google Antigravity, and more. — OpenCode support: **Native** — OpenCode plugin/slash command.

**[Langfuse OpenCode Observability](https://langfuse.com/integrations/developer-tools/opencode)** — actively maintained — OpenTelemetry-based observability for OpenCode. Traces user turns, assistant generations, tool calls, retries, reasoning output, compaction, failed steps. Sent to Langfuse for monitoring, debugging, cost analysis. — OpenCode support: **Native** — OpenCode plugin (`@langfuse/opencode-observability-plugin`).

**[pai4451/opencode-telemetry-plugin](https://github.com/pai4451/opencode-telemetry-plugin)** — actively maintained — OpenTelemetry metrics exporter for OpenCode. Exports session telemetry via OTLP/gRPC. Built with `@opentelemetry/sdk-metrics` and `@opencode-ai/plugin`. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

*(All major tools are listed above.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native cost tracking** — Built into Claude Code only.
- **Claude Code usage dashboard** — Claude Code's web-based usage analytics.

---

## Summary

- **Element:** Usage / Cost Tracking Tools
- **Total found:** 11 usable + 2 excluded
- **Key insight:** This is a densely populated category. OpenCode has ~11 distinct tools for cost/usage tracking, ranging from TUI sidebar plugins (token-tracker, Throughput, Usage Monitor) to macOS menu-bar apps (opencode-bar) to SQLite telemetry databases (Opencode Telemetry) to OTel exporters (Langfuse, pai4451). The diversity is notable: real-time in-session tracking, cross-session aggregation, provider quota monitoring, and third-party observability platforms are all covered. No single tool dominates; users typically combine 2-3 (e.g., token-tracker for real-time + Opencode Telemetry for historical + Langfuse for team observability).
- **File path:** `research/discovery/14-usage-cost-tracking.md`


---

# Element 15: Agent-Team Frameworks

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** — 67.2k stars, actively maintained — Multi-model agent orchestration harness for OpenCode. 10+ specialized subagents (Explorer, Oracle, Librarian, Designer, Fixer, etc.), background task management, LSP/AST tools, MCP servers, 54+ lifecycle hooks. Team Mode with parallel agent execution and consensus. — OpenCode support: **Native** — OpenCode plugin.

**[alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)** — 7.8k stars, actively maintained — Lightweight multi-agent orchestration. 7 specialized subagents (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer). Background tasks, LSP/AST tools, tmux integration for live agent visibility, MCP servers. — OpenCode support: **Native** — OpenCode plugin.

**[kdcokenny/opencode-workspace](https://github.com/kdcokenny/opencode-workspace)** — 555 stars, actively maintained — Bundled multi-agent orchestration harness with 16 components. 4 specialist subagents (researcher, coder, scribe, reviewer) with pre-configured permission boundaries. OCX profile system. — OpenCode support: **Native** — OpenCode plugin + OCX profile.

**[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** — 4.6k stars, actively maintained — Plan-first development framework with approval-based execution. 3 main agents (OpenAgent, OpenCoder, SystemBuilder) + 8+ specialized subagents (ContextScout, TaskManager, CoderAgent, TestEngineer, CodeReviewer, BuildAgent, DocWriter, ExternalScout). MVI context system (80% token reduction). Multi-language support (TypeScript, Python, Go, Rust, C#/.NET). — OpenCode support: **Native** — OpenCode agent framework.

**[agnusdei1207/opencode-orchestrator](https://github.com/agnusdei1207/opencode-orchestrator)** — actively maintained — Multi-agent orchestrator plugin for OpenCode. Parallel sessions (up to 50), agent distribution (Commander → Planner → Workers → Reviewer), background tasks, auto-retry, loop-until-done. Shared state coordination. — OpenCode support: **Native** — OpenCode plugin.

**[NERV](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI), 9 specialized subagents. Scaffolds 45+ files via `nerv init`. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

**[hiai-opencode](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Canonical 12-agent model. 10 visible agents (Bob, Coder, Strategist, Critic, Guard, Researcher, Designer, Manager, Brainstormer, Vision) + hidden Sub and Agent Skills. Bundled skills, MCP servers, LSP integration, ralph-loop. — OpenCode support: **Native** — OpenCode plugin.

**[CrewBee](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Task-specific Agent Teams for OpenCode. Define reusable task/project-specific agent teams, project them into OpenCode agents, switch between single-agent and multi-agent collaboration. Built-in Coding Team template with review flow and completion criteria. — OpenCode support: **Native** — OpenCode plugin.

**[OpenCode Ensemble](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Parallel agent teams for OpenCode. Coordinate parallel agents with peer messaging, shared task board, git worktree isolation, live dashboard. — OpenCode support: **Native** — OpenCode plugin.

**[Open Conclave](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Multi-agent debates moderated by captain agent until consensus. Each agent has different system prompt (logical, creative, research-focused). Configurable provider/model per agent. — OpenCode support: **Native** — OpenCode plugin.

**[OpenCode Swarm](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, resumable evidence. Multi-agent team with quality gates. — OpenCode support: **Native** — OpenCode plugin.

**[FlowDeck](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — AI-powered multi-agent workflow orchestration. 25 specialist agents (architect, planner, coder, reviewer, tester, debugger, risk-analyst, policy-enforcer, etc.). 24 workflow skills, 17 workflow commands, 15 pre-built orchestration flows. Persistent state via `.planning/STATE.md`. Wave-based parallel execution. AI Safety layer. — OpenCode support: **Native** — OpenCode plugin.

**[Open Dynamic Workflows](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Dynamic multi-agent workflows for OpenCode. Local daemon runs generated orchestration script with concurrent agents, adversarial verification, crash-resume. OpenCode plugin adds workflow triggers and planning UI. Bring your own model. — OpenCode support: **Native** — OpenCode plugin + local daemon.

**[Gem Team](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Self-learning multi-agent orchestration harness for spec-driven development and automated verification. — OpenCode support: **Native** — OpenCode plugin.

**[Pocket Universe](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Subagent-driven pocket universe for primary agent. Closed-loop, resilient, async agents that block main thread. Three tools for parallel subagent communication. — OpenCode support: **Native** — OpenCode plugin.

**[deliberation](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Ask GPT, Gemini, Grok, or OpenRouter for second opinion as expert subagents over MCP. 7 expert subagents (Architect, Plan Reviewer, Scope Analyst, Code Reviewer, Security Analyst, Researcher, Debugger). `ask-all` and `consensus` modes. — OpenCode support: **Open standard** — MCP server + OpenCode plugin.

---

## Actively maintained but smaller

**[Claude Squad](https://github.com/smtg-ai/claude-squad)** — actively maintained — TUI for parallel agents with git worktree isolation. Supports OpenCode via `-p "opencode"`. tmux sessions, vim-style navigation. AGPL-3.0. — OpenCode support: **Documented port/adapter exists** — explicitly lists OpenCode in agent support; launches OpenCode in tmux worktree sessions.

**[Baton (mraza007)](https://github.com/topics/agent-orchestration)** — maintained — Poll-dispatch-reconcile orchestration for git worktrees. Supports Claude Code, Codex, Gemini, OpenCode. — OpenCode support: **Claimed but unverified** — listed in orchestration roundups as supporting OpenCode but no explicit docs found.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Squad default mode** — Defaults to Claude Code; OpenCode support exists but is secondary.
- **Vibe Kanban** — Lists OpenCode in agent support but is community-maintained after Bloop shutdown; primary focus unclear.
- **Microsoft Conductor** — YAML workflow orchestration with Copilot SDK and Anthropic Agents SDK; no explicit OpenCode support found.
- **Code Conductor (ryanmac)** — GitHub-native CLI, Claude Code only.

---

## Summary

- **Element:** Agent-Team Frameworks
- **Total found:** 17 usable + 4 excluded
- **Key insight:** This is the largest category by far. OpenCode's native multi-session support and subagent system have spawned a rich ecosystem of team frameworks. The big three are oh-my-openagent (67.2k stars), oh-my-opencode-slim (7.8k stars), and OpenAgentsControl (4.6k stars). NERV, hiai-opencode, FlowDeck, and Open Dynamic Workflows provide innovative orchestration paradigms (SDD pipelines, 12-agent models, 25-agent safety-gated teams, dynamic workflow daemons). The deliberation plugin uniquely uses MCP for multi-model consensus. Claude Squad provides cross-tool worktree-based parallel sessions.
- **File path:** `research/discovery/15-agent-team-frameworks.md`


---

# Element 16: Workflow Orchestration Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[mark-hingston/opencode-workflows](https://github.com/mark-hingston/opencode-workflows)** — actively maintained — Workflow automation plugin for OpenCode using the Mastra engine. Deterministic, auditable, resumable, composable agent orchestration. Patterns: Sequential Chain, Parallel Experts, Tool-Augmented, Human-in-the-Loop (`suspend` steps), Conditional Routing. Each step's output captured and reviewable. Workflows persist to disk and survive restarts. — OpenCode support: **Native** — OpenCode plugin.

**[derekbar90/opencode-conductor](https://github.com/derekbar90/opencode-conductor)** — 121 stars, actively maintained — Protocol-driven workflow plugin for OpenCode. Context → Spec → Plan → Implement lifecycle. `/conductor:setup`, `/conductor:newTrack`, `/conductor:implement`, `/conductor:status`, `/conductor:revert` commands. Persistent planning state. — OpenCode support: **Native** — OpenCode plugin.

**[FlowDeck](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — AI-powered multi-agent workflow orchestration. Four-phase cycle: discuss → plan → execute → review. 25 specialist agents, 24 reusable workflow skills (TDD, security scan, deploy check, code review), 17 workflow commands, 15 pre-built orchestration flows including Spec-Driven Development (SDD). Persistent state via `.planning/STATE.md`. Wave-based parallel execution. AI Safety layer with patch trust scoring, edit gates, phase gating. — OpenCode support: **Native** — OpenCode plugin.

**[Open Dynamic Workflows](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Dynamic multi-agent workflows for OpenCode. Local daemon runs generated orchestration script with concurrent agents, adversarial verification, crash-resume. OpenCode plugin adds workflow/ultracode triggers and planning UI. Bring your own model. — OpenCode support: **Native** — OpenCode plugin + local daemon.

**[opencode-bmad-workflow](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — BMAD (Breakthrough Method of Agile AI-Driven Development) workflow plugin. Specialized agents for product management, architecture, development, QA. Automates epic planning, feature breakdown, sprint workflows, code reviews through structured multi-agent pipeline. — OpenCode support: **Native** — OpenCode plugin.

**[GoopSpec](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Spec-driven development workflow. 5-phase workflow: Plan → Research → Specify → Execute → Accept. Contract gates for user confirmation, 12 specialized subagents, persistent memory system, wave-based execution with atomic commits, deviation rules. — OpenCode support: **Native** — OpenCode plugin.

**[NERV](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Invisible engineering infrastructure. Spec-Driven Development pipeline, A2A task delegation hub, persistent semantic memory (MAGI). Scaffolds 45+ files via `nerv init` including SDD skills, slash commands, MCP servers, lifecycle plugins. — OpenCode support: **Native** — OpenCode plugin + scaffolding CLI.

**[OpenCode Swarm](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Verification-gated swarm with architect planning, independent review, test engineering, security checks, resumable evidence. Multi-agent workflow with quality gates. — OpenCode support: **Native** — OpenCode plugin.

**[Subtask2](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Extend opencode `/commands` into a powerful orchestration system with granular flow control. Task decomposition and dependency management. — OpenCode support: **Native** — OpenCode plugin.

**[ForLoop Planner](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — Autopilot development platform. Plan with ForLoop agent, then Build, Test, Deploy on cloud in one go. Covers entire development lifecycle. — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

**[open-plan-annotator](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Fully local agentic coding plugin that intercepts plan mode and opens an annotation UI in browser. Select text to strikethrough, replace, insert, or comment — then approve plan or request changes. — OpenCode support: **Native** — OpenCode plugin.

**[Opencode Roadmap](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Strategic roadmap planning and multi-agent coordination plugin. Project-wide planning capabilities. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Microsoft Conductor** — YAML-defined workflows with GitHub Copilot SDK and Anthropic Agents SDK. No explicit OpenCode support.
- **conductor.build (Melty)** — Closed-source macOS desktop app.
- **Code Conductor (ryanmac)** — GitHub-native CLI, Claude Code only.

---

## Summary

- **Element:** Workflow Orchestration Tools
- **Total found:** 12 usable + 3 excluded
- **Key insight:** OpenCode's workflow orchestration ecosystem is mature and diverse. mark-hingston's opencode-workflows (Mastra engine) provides the most structured approach with deterministic, auditable, resumable workflows and five orchestration patterns. FlowDeck offers the richest feature set (25 agents, 24 skills, 15 flows, safety layer). Conductor provides a clean protocol-driven lifecycle. NERV, GoopSpec, and opencode-bmad-workflow each bring spec-driven development methodologies. The open-plan-annotator adds a unique human-in-the-loop planning UI. Together these tools cover everything from simple task decomposition to complex multi-phase development pipelines.
- **File path:** `research/discovery/16-workflow-orchestration.md`


---

# Element 17: Agent SDKs

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[anomalyco/opencode-sdk-js](https://github.com/anomalyco/opencode-sdk-js)** — 87 stars, actively maintained — Official JavaScript/TypeScript SDK for OpenCode. Handles sessions, file operations, streaming responses, plugin development, and programmatic agent control. Type-safe hooks and context APIs. Auto-generated types from OpenCode's internal type system. — OpenCode support: **Native** — official SDK from the OpenCode team.

**[anomalyco/opencode-sdk-go](https://github.com/anomalyco/opencode-sdk-go)** — actively maintained — Official Go SDK for OpenCode. Generated with Fern to track OpenCode versions with no manual work per version bump. Core client, field types, and session management primitives. — OpenCode support: **Native** — official SDK from the OpenCode team.

**[Acksell/opencode-go-sdk](https://github.com/Acksell/opencode-go-sdk)** — 1 star, maintained — Community Go SDK for OpenCode, generated with Fern. Tracks OpenCode with no manual work per version bump. — OpenCode support: **Native** — community SDK wrapping OpenCode APIs.

---

## Actively maintained but smaller

*(No additional smaller SDKs found in this sweep.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Anthropic Agents SDK** — Python SDK for building agentic systems with Claude. No OpenCode integration.
- **Claude Code SDK** — No public SDK for Claude Code; it's a closed-source tool.

---

## Summary

- **Element:** Agent SDKs
- **Total found:** 3 usable + 2 excluded
- **Key insight:** OpenCode's SDK ecosystem is intentionally lean — the official JS/TS and Go SDKs cover the primary use cases. The JS SDK (87 stars) is the most mature, handling sessions, file ops, streaming, and plugin development. The Go SDK is auto-generated via Fern for version parity. A community Go SDK exists but has minimal adoption. Notably, there is no official Python SDK yet (issue #4031 tracks this request). Most OpenCode plugin development happens directly in JS/TS using the `@opencode-ai/plugin` package rather than through a standalone SDK.
- **File path:** `research/discovery/17-agent-sdks.md`


---

# Element 18: Discipline / Skill Packs (Superpowers / ponytail-style)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[obra/superpowers](https://github.com/obra/superpowers)** — 211,860 stars, actively maintained — Complete agentic skills framework & software development methodology. 14 composable skills: brainstorming, TDD, systematic-debugging, code review, git-worktrees, subagent-driven-development, etc. Auto-installs as OpenCode plugin via `plugin: ["superpowers@git+https://github.com/obra/superpowers.git"]`. — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/INSTALL.md` and `docs/README.opencode.md`; auto-installs on OpenCode restart.

**[waybarrios/opencode-power-pack](https://github.com/waybarrios/opencode-power-pack)** — ~460 stars, actively maintained — 55 rigorous skills ported from Claude Code workflows to Codex, OpenCode, and Pi. Feature development (7-phase), code review, security audit, frontend design, MCP builder, skill creator, Hugging Face ML/training (13 skills), AWS/SageMaker cloud (5 skills). — OpenCode support: **Documented port/adapter exists** — dedicated `.opencode/plugins/opencode-power-pack.js` plugin; explicit OpenCode install docs.

**[meaningfy-ws/skillery](https://github.com/meaningfy-ws/skillery)** — actively maintained — Collection of agent skills. On OpenCode: skill-packs (superpowers, stream-coding, ponytail) load from `.claude/` natively; OpenSpec, commit-commands, and gitnexus also supported. Cross-tool skill pack distribution. — OpenCode support: **Open standard** — loads standard SKILL.md packs into OpenCode's native skill directories.

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** — actively maintained — Ponytail discipline/ruleset for AI agents. Loads as always-on context every session. Registers `/ponytail` commands and ships skills activated when a task needs them. Available as `opencode-ponytail` npm package. — OpenCode support: **Documented port/adapter exists** — `opencode-ponytail` package; loads ruleset and skills into OpenCode.

---

## Actively maintained but smaller

*(No additional smaller discipline packs found beyond those already listed in Element 1.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Anthropic official Claude Code skills** — Many upstream skills that power-pack and superpowers adapt from; excluded because they are Claude Code-native without direct OpenCode paths (the adapters above handle the porting).

---

## Summary

- **Element:** Discipline / Skill Packs (Superpowers / ponytail-style)
- **Total found:** 4 usable + 1 excluded
- **Key insight:** The "discipline pack" concept — comprehensive, opinionated skill frameworks that reshape how agents work — is led by obra/superpowers (212k stars) as the genre-defining example. waybarrios' power-pack (460 stars) is the most thorough cross-tool adaptation of Claude Code workflows. meaningfy-ws/skillery provides a meta-collection that bundles superpowers, stream-coding, and ponytail for OpenCode. DietrichGebert's ponytail offers a lighter-weight ruleset approach. These are not just "skills" — they are full methodologies that agents follow, comparable to software development frameworks.
- **File path:** `research/discovery/18-discipline-skill-packs.md`


---

# Element 19: Docs-Context MCP Servers (Context7-style)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[upstash/context7](https://github.com/upstash/context7)** — 7,072 stars, actively maintained — The definitive docs-context MCP server. Fetches up-to-date, version-specific documentation and code examples straight from source. `resolve-library-id` and `get-library-docs` tools. Community-contributed library index. Explicit OpenCode install docs for both remote (`https://mcp.context7.com/mcp`) and local (`npx -y @upstash/context7-mcp`) configurations. — OpenCode support: **Open standard** — MCP server; OpenCode natively discovers MCP servers.

**[sandbox-technologies/opencode-docs-mcp](https://github.com/sandbox-technologies/opencode-docs-mcp)** — actively maintained — OpenCode Docs MCP Server. Self-hostable or remote-hosted at `https://tryinspector.com/api/opencode-docs/mcp`. Three tools: `SearchOpenCodeDocs` (query search), `GetOpenCodeDocPage` (full page content), `BrowseOpenCodeDocs` (table of contents). Covers 27 documents across Getting Started, Usage, Configure, Develop, Providers, Protocols, Security, Server, UI, and Developer Resources. — OpenCode support: **Open standard** — MCP server with explicit OpenCode config example.

**[bgauryy/open-docs](https://github.com/bgauryy/open-docs)** — actively maintained — Comprehensive technical documentation suite for OpenCode (27 documents, 310+ pages, 520+ code examples, 100+ diagrams). Deep technical insights into architecture, implementation, and development. Complements official user docs. Covers architecture, session management, tool system, LSP integration, provider system, ACP protocol, MCP integration, server architecture, TUI/desktop/web implementations, and SDKs. — OpenCode support: **Native** — documentation resource consumed by OpenCode users and agents; not a tool per se but essential docs-context infrastructure.

---

## Actively maintained but smaller

*(No additional smaller docs-context MCPs found.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native docs retrieval** — Claude Code has built-in web search and docs access; no separate MCP server needed.

---

## Summary

- **Element:** Docs-Context MCP Servers (Context7-style)
- **Total found:** 3 usable + 1 excluded
- **Key insight:** Context7 (7k+ stars) is the undisputed leader in this space — it solves the "outdated training data" problem by pulling live docs into LLM context. The OpenCode-specific docs MCP (sandbox-technologies) is a nice complement, giving agents direct access to OpenCode's own documentation. bgauryy's open-docs provides the deepest technical reference (310+ pages) for OpenCode internals. Together these ensure agents never hallucinate APIs or work from stale documentation.
- **File path:** `research/discovery/19-docs-context-mcp.md`


---

# Element 20: Statusline Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[Joaquinvesapa/sub-agent-statusline](https://github.com/Joaquinvesapa/sub-agent-statusline)** — actively maintained — Subagent Monitor for OpenCode. TUI sidebar plugin showing running/completed/failed subagents, elapsed time, and token/context usage. Compact home/footer summary when active subagent activity exists. Built with SolidJS in universal mode for OpenTUI compatibility. — OpenCode support: **Native** — OpenCode TUI sidebar plugin.

**[eserete/opencode-token-tracker](https://github.com/eserete/opencode-token-tracker)** — 3 stars, actively maintained — Real-time token usage, cost, and latency tracking displayed in the TUI sidebar footer. Updates every 2 seconds during execution. Shows last request and session totals with cost estimates. — OpenCode support: **Native** — OpenCode TUI plugin.

**[OpenCode Native Status Bar](https://opencode.ai/docs/)** — Core feature, actively maintained — Built-in status bar showing active model, session state, token usage, and agent mode (Plan vs. Build). Configurable via `tui.json`. — OpenCode support: **Native**

---

## Actively maintained but smaller

*(No additional smaller statusline tools found.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code customizable statusLine** — Claude Code supports a customizable `statusLine` that pipes session state as JSON to a shell script after each assistant message. OpenCode has feature requests (#30295, #8619) for this but it is not yet implemented. The sub-agent-statusline and token-tracker plugins fill part of this gap.

---

## Summary

- **Element:** Statusline Tools
- **Total found:** 3 usable + 1 excluded
- **Key insight:** OpenCode's statusline ecosystem is small but functional. The native status bar covers basics (model, session state, tokens). Joaquinvesapa's sub-agent-statusline adds critical visibility for multi-agent workflows — showing which subagents are running, done, or failed. eserete's token-tracker adds real-time cost awareness. The gap is a Claude Code-style customizable statusLine hook (feature requests #30295 and #8619 are open), which would let users pipe session state to arbitrary shell scripts for custom status displays.
- **File path:** `research/discovery/20-statusline-tools.md`


---

# Element 21: Git-Worktree Helpers

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[kdcokenny/opencode-worktree](https://github.com/kdcokenny/opencode-worktree)** — 701 stars, 35 forks, actively maintained — Zero-friction git worktrees for OpenCode. Auto-spawns terminals, syncs files, cleans up on exit. Two tools: `worktree_create(branch, baseBranch?)` and `worktree_delete(reason)`. Creates worktree at `~/.local/share/opencode/worktree/<project-id>/<branch>`, runs post-create hooks (e.g., `pnpm install`), opens new terminal with OpenCode running. On delete: runs pre-delete hooks, commits all changes, removes worktree with `--force`. Config via `.opencode/worktree.jsonc`. Supports Ghostty, Kitty, tmux. Part of OCX ecosystem. — OpenCode support: **Native** — OpenCode plugin.

**[felixAnhalt/opencode-worktree-session](https://github.com/felixAnhalt/opencode-worktree-session)** — actively maintained — OpenCode plugin that automatically manages Git worktrees for every AI session. Creates worktree in `.opencode/worktrees/`, refuses to run on `main` branch, pivots AI's cwd to worktree automatically. On session exit: stages all changes, generates commit message via OpenCode API, pushes to origin, removes worktree. Install via `@tmegit/opencode-worktree-session` npm package. — OpenCode support: **Native** — OpenCode plugin.

**[athal7/opencode-devcontainers](https://github.com/athal7/opencode-devcontainers)** — actively maintained — OpenCode plugin for isolated branch workspaces using devcontainers OR git worktrees. Auto-assigned ports (13000–13099), session state management, automatic copying of gitignored secrets (.env, credentials), unified workspace cleanup. Supports both full container isolation (devcontainers) and lightweight filesystem isolation (worktrees). — OpenCode support: **Native** — OpenCode plugin.

---

## Actively maintained but smaller

*(No additional smaller worktree helpers found.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native worktree support** — Claude Code has built-in worktree integration; OpenCode relies on plugins for equivalent functionality.

---

## Summary

- **Element:** Git-Worktree Helpers
- **Total found:** 3 usable + 1 excluded
- **Key insight:** Git worktree isolation is essential for AI-driven development to prevent agents from polluting the main branch. kdcokenny's opencode-worktree (701 stars) is the most popular solution — it auto-spawns terminals, runs hooks, and cleans up on exit. felixAnhalt's worktree-session takes a more aggressive approach: every session gets its own worktree, auto-commits on exit, and refuses to touch `main`. athal7's devcontainers plugin offers the most flexibility, supporting both full container isolation and lightweight worktree isolation. These three plugins together cover every worktree workflow need.
- **File path:** `research/discovery/21-git-worktree-helpers.md`


---

# Element 22: Awesome-Lists (AI coding agents, cross-tool ones only)

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard. Cross-tool awesome-lists that include OpenCode.

---

## Well-known / high-star

**[bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents)** — 308 stars, actively maintained — Comprehensive directory of 80+ terminal-native AI coding agents (open-source and proprietary) plus harnesses that orchestrate them. Sorted by GitHub stars within sections. OpenCode is listed prominently in the "Open Source" section with 193k stars noted. Also catalogs orchestrators (Claude Squad, Superset, herdr, cmux, agent-of-empires, hcom, etc.) many of which support OpenCode. — OpenCode support: **Open standard** — cross-tool discovery list; OpenCode is a first-class entry.

**[ai-for-developers/awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools)** — 1.7k stars, actively maintained — Curated awesome-list of AI coding tools including agents, MCP servers, skills, and harnesses. OpenCode listed under "Coding Agents" section. Cross-tool coverage (Cursor, Claude Code, Codex, OpenCode, Aider, Cline, etc.). — OpenCode support: **Open standard** — cross-tool discovery list.

**[kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents)** — actively maintained — Awesome list of AI Agents across categories (Software Development, Research, Productivity, etc.). OpenCode listed under Software Development alongside Claude Engineer, Cline, Stakpak, ReviewCerberus, Dorothy, Greywall, Maestro Orchestrate, amux, AgentsMesh, Bernstein. — OpenCode support: **Open standard** — cross-tool discovery list.

**[awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode)** — actively maintained, community-driven — The definitive curated list of plugins, themes, agents, projects, and resources specifically for OpenCode. While not "cross-tool" in the broad sense, it is the canonical discovery hub for the OpenCode ecosystem and references many cross-tool compatible resources. — OpenCode support: **Native** — OpenCode-specific awesome-list.

---

## Actively maintained but smaller

**[GetBindu/awesome-claude-code-and-skills](https://github.com/GetBindu/awesome-claude-code-and-skills)** — maintained — Awesome list focused on Claude Code but cross-references OpenCode-compatible resources (skills, MCP servers) where applicable. Includes skillreaper, pi-reflect, and other cross-tool utilities. — OpenCode support: **Open standard** — lists cross-tool resources usable with OpenCode.

**[ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)** — 705 stars, maintained — Awesome list for harness engineering. References bradAGI/awesome-cli-coding-agents and cross-tool agent infrastructure. — OpenCode support: **Open standard** — cross-tool discovery list referencing OpenCode ecosystem.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **hesreallyhim/awesome-claude-code** — 43K stars. Claude Code focused; no OpenCode cross-references found.
- **VoltAgent/awesome-claude-code-subagents** — 19.6K stars. Claude Code subagents only.
- **ComposioHQ/awesome-claude-skills** — 59K stars. Claude skills only.
- **travisvn/awesome-claude-skills** — 12K stars. Claude skills only.
- **rohitg00/awesome-claude-code-toolkit** — 1.6K stars. Claude Code toolkit only.

---

## Summary

- **Element:** Awesome-Lists (AI coding agents, cross-tool ones only)
- **Total found:** 5 usable + 5 excluded
- **Key insight:** Cross-tool awesome-lists that include OpenCode are surprisingly scarce — most awesome-lists in this space are Claude Code-centric. bradAGI's awesome-cli-coding-agents (308 stars) is the best cross-tool discovery hub, with OpenCode prominently featured. ai-for-developers/awesome-ai-coding-tools (1.7k stars) and kyrolabs/awesome-agents provide broader tool coverage. The awesome-opencode list is the canonical OpenCode-specific discovery hub. The dominance of Claude-specific lists reflects the market reality, but OpenCode's inclusion in the cross-tool lists that do exist is consistently strong.
- **File path:** `research/discovery/22-awesome-lists.md`


---

# Element 23: Security Scanners for Agent Configs

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[sandervandegeijn/code-security-scanner](https://github.com/sandervandegeijn/code-security-scanner)** — actively maintained — Comprehensive security scanner built as a thin Python wrapper around `opencode run`. Six-phase methodology: Discovery → Dependency audit (with osv-scanner) → Per-file review → Confirmation pass → Semantic dedup → Business summary. Defines a custom `scanner` agent in `opencode.json` as a read-only jail (denies bash, edit, write, patch, task, skill, webfetch, websearch). Supports any opencode-supported provider (default: azure/gpt-5.5). `SECURITY_SCAN.md` for project context and whitelisting. — OpenCode support: **Native** — purpose-built around OpenCode's CLI and agent system.

**[zm2231/z-audit](https://github.com/zm2231/z-audit)** — actively maintained — Security audit skill for Claude Code / OpenCode. 7-phase methodology: Stack Detection → Secrets & Credentials → Authentication & Authorization → API Security → Infrastructure-Specific → Security Headers & CORS → Dependencies → Data Exposure. Auto-detects tech stack and runs targeted vulnerability checks. — OpenCode support: **Documented port/adapter exists** — explicitly labeled for Claude Code / OpenCode; manual install works for both.

---

## Actively maintained but smaller

**[remorses/opencode-injection-guard](https://github.com/remorses/opencode-injection-guard)** — 15 stars, actively maintained — Open-source prompt injection detection for OpenCode. Works with any model — not locked to OpenAI. Intercepts tool outputs via `tool.execute.after` hook and sends them to a separate judge model. If injection detected, original output is replaced with a warning before the main agent sees it. Opt-in via `.opencode/injection-guard.json` config. — OpenCode support: **Native** — OpenCode plugin.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **AgentLint** — 48 stars. 33 evidence-backed checks for AI-friendly repos. Claude Code plugin with auto-fix. No OpenCode port found.
- **SecureCodeWarrior/ai-security-rules** — Security rule files for AI-assisted developer tools. Generic ruleset, not a scanner tool per se.

---

## Summary

- **Element:** Security Scanners for Agent Configs
- **Total found:** 3 usable + 2 excluded
- **Key insight:** Security scanning for agent-driven development is an emerging category. sandervandegeijn's code-security-scanner is the most sophisticated — it's essentially a security audit framework built natively on OpenCode's agent architecture, with a proper read-only jail agent and six-phase methodology. zm2231's z-audit provides a lighter 7-phase skill-based approach. remorses' opencode-injection-guard fills a critical niche: real-time prompt injection detection at the tool-output layer. The gap is a generic "agent config linter" that audits opencode.json for overly permissive settings, exposed credentials, or dangerous tool combinations.
- **File path:** `research/discovery/23-security-scanners.md`


---

# Element 24: Safety-Net / Guardrail Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[remorses/opencode-injection-guard](https://github.com/remorses/opencode-injection-guard)** — 15 stars, actively maintained — Prompt injection detection plugin for OpenCode. Intercepts tool outputs (bash, webfetch) via `tool.execute.after` hook, sends to a judge model for injection analysis. Replaces compromised output with a warning before the main agent sees it. Configurable scan patterns. — OpenCode support: **Native** — OpenCode plugin.

**[boxpositron/envsitter-guard](https://github.com/boxpositron/envsitter-guard)** — actively maintained — Prevents agents/tools from reading or editing sensitive `.env*` files while allowing safe inspection via EnvSitter (keys + deterministic fingerprints; never values). Hooks into OpenCode's tool system to intercept read/edit/write/patch on `.env*` paths. — OpenCode support: **Native** — OpenCode plugin.

**[Greywall](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode/kyrolabs lists) — actively maintained — Deny-by-default command sandbox for AI coding agents with filesystem isolation, network control via transparent proxy, built-in profiles for agents like Claude Code or OpenCode, and learning mode for auto-generating configs. — OpenCode support: **Documented port/adapter exists** — explicit OpenCode profile support.

**[Daytona Sandbox Plugin](https://github.com/daytonaio/daytona/tree/main/libs/opencode-plugin)** — actively maintained (though Daytona repo is no longer maintained, the plugin remains functional) — Runs OpenCode sessions inside isolated Daytona sandboxes. Each session gets its own remote sandbox synced to a local git branch. Complete kernel/filesystem/network isolation. — OpenCode support: **Native** — official OpenCode plugin from Daytona.

---

## Actively maintained but smaller

**[FlowDeck](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — actively maintained — AI Safety layer built into its workflow orchestration: patch trust scoring, edit gates, phase gating, arch constraint enforcement, failure replay, regression prediction. — OpenCode support: **Native** — OpenCode plugin with embedded safety layer.

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native guardrails** — Built-in safety features of Claude Code only.
- **claudebox** — 53 stars. Sandboxed environment for Claude Code only.

---

## Summary

- **Element:** Safety-Net / Guardrail Tools
- **Total found:** 5 usable + 2 excluded
- **Key insight:** Safety in OpenCode is layered: (1) envsitter-guard prevents secret exfiltration at the tool level, (2) opencode-injection-guard blocks prompt injection attacks at the output layer, (3) Greywall provides deny-by-default sandboxing with OpenCode-specific profiles, (4) Daytona provides full kernel-level isolation via remote sandboxes, and (5) FlowDeck embeds safety intelligence into workflow orchestration (trust scoring, edit gates, regression prediction). These five tools together provide defense-in-depth for agent-driven development.
- **File path:** `research/discovery/24-safety-net-guardrails.md`


---

# Element 25: Hook Management CLIs

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

*(No standalone "hook management CLI" tools found for OpenCode. OpenCode's hook system is intrinsic to its plugin architecture — hooks are defined in JS/TS plugin files, not managed via a separate CLI.)*

---

## Actively maintained but smaller

**[Opencode Hooks Plugin](https://github.com/awesome-opencode/awesome-opencode)** (from awesome-opencode list) — maintained — Bridges Claude Code hooks definition to OpenCode hooks. Allows importing Claude Code-style hook definitions into OpenCode's plugin event system. — OpenCode support: **Documented port/adapter exists** — adapter from Claude Code hooks to OpenCode hooks.

**[OpenCode Native Plugin System](https://opencode.ai/docs/plugins/)** — Core feature, actively maintained — OpenCode's plugin system IS its hook system. Plugins are JS/TS modules that return hook objects (`tool.execute.before`, `tool.execute.after`, `session.idle`, `file.edited`, etc.). Hooks are automatically discovered from `~/.config/opencode/plugins/` and `.opencode/plugins/`. No separate CLI needed — hooks are managed as code. — OpenCode support: **Native**

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **Claude Code native hooks** (`pre-tool`, `post-tool`, `session-start`, etc.) — Built into Claude Code only. The Opencode Hooks Plugin provides partial bridging.
- **Various Claude Code hook collections** — Community hook collections with no OpenCode path.

---

## Summary

- **Element:** Hook Management CLIs
- **Total found:** 2 usable + 2 excluded
- **Key insight:** This category is essentially empty for OpenCode — and that's by design. OpenCode's hooks are managed as code (JS/TS plugins) rather than via a separate CLI. The plugin system auto-discovers hooks from the filesystem, so there's no need for a "hook install/enable/disable" CLI. The Opencode Hooks Plugin provides a bridge for importing Claude Code hook definitions. If you're looking for hook management, you're looking for plugin management (see Element 9: Plugins / Plugin Marketplaces).
- **File path:** `research/discovery/25-hook-management-clis.md`


---

# Element 26: Self-Improving / Instinct-Mining Tools

> Research sweep completed: 2026-08-07
> Filter: Only resources that ACTUALLY support OpenCode — natively, via documented adapter/port, or via open cross-tool standard

---

## Well-known / high-star

**[okdk7788/opencode-self-improving-skills](https://github.com/okdk7788/opencode-self-improving-skills)** — actively maintained — OpenCode plugin that implements a self-improvement loop for agent skills. Two companion skills + five custom tools:
- `distill_skill` (autonomous) — captures reusable techniques as SKILL.md from session evidence
- `curator_status` (on-demand) — shows learned skills, usage, idle/stale states
- `optimize_skill` (autonomous) — GEPA-style measured improvement grounded in failure traces (5-stage: collect evidence → generate candidates → judge → Pareto-select → human-gated apply)
- `evolution_status` (on-demand) — shows outcome stats + optimization ranking
- `mark_skill_optimized` (internal) — stamps `optimized_at` after applying a rewrite
Installs to `~/.config/opencode/plugins/self-improving-skills/` — auto-loaded at startup. — OpenCode support: **Native** — OpenCode plugin with autonomous skill distillation and evolution.

**[hqhq1025/skill-optimizer](https://github.com/hqhq1025/skill-optimizer)** — ~125 stars, actively maintained — Agent Skills lifecycle toolkit (covered in Element 1, but core to this category):
- `skill-miner` — scans coding-agent history, archives, memories, and repeated work to surface workflows worth encoding as skills. Deterministic scan script covers Codex, Claude Code, Gemini, Antigravity, and exported transcripts.
- `skill-personalizer` — audits installed skills for undertriggering/overtriggering, adapts to local phrasing and verification habits.
- `skill-generalizer` — turns local/private skills into publishable form, strips private paths/credentials.
— OpenCode support: **Native** — explicitly documents OpenCode path (`~/.config/opencode/skills/`).

**[thousandflowers/skillreaper](https://github.com/thousandflowers/skillreaper)** — 47 stars, actively maintained — Evidence-based pruning for AI agent configs. Reads real session transcripts to find skills, MCP servers, and agents loaded but never fired, then safely quarantines dead weight. Supports Claude Code, Codex CLI, Hermes, **OpenCode**, Cursor, and OpenClaw. Single static binary, zero telemetry. `reap` command shows exactly what costs you tokens. — OpenCode support: **Native** — explicitly lists OpenCode in supported platforms; reads OpenCode session transcripts.

---

## Actively maintained but smaller

*(All major tools listed above.)*

---

## Old or possibly abandoned

*(None identified.)*

---

## Claude-Code-only, excluded

- **jo-inc/pi-reflect** — 37 stars. Self-improving behavioral files for coding agents. Analyzes session transcripts for correction patterns and makes surgical edits to AGENTS.md. Pi-only extension; no OpenCode port.
- **sentient-agi/EvoSkill** — Automated skill discovery for coding agents. Uses git branches for program variants. Appears to target Claude Code primarily; no explicit OpenCode support found.

---

## Summary

- **Element:** Self-Improving / Instinct-Mining Tools
- **Total found:** 3 usable + 2 excluded
- **Key insight:** This is a nascent but fascinating category. okdk7788's opencode-self-improving-skills is the standout — it's a native OpenCode plugin that runs an autonomous loop: distill skills from evidence → curate them → optimize them via GEPA-style evolution. hqhq1025's skill-optimizer provides the complementary "mining" layer (scanning history for skill-worthy workflows) and "publication" layer (generalizing for distribution). skillreaper approaches the problem from the opposite direction: pruning dead weight from configs based on transcript evidence, which indirectly improves performance by reducing context bloat. Together these tools form a complete lifecycle: mine → distill → optimize → prune.
- **File path:** `research/discovery/26-self-improving-instinct-mining.md`
# OpenCode Resource Discovery Catalog

A systematic sweep of the OpenCode (AI coding agent) ecosystem, covering
26 categories of third-party and native resources — plugins, MCP servers,
frameworks, safety tooling, and more. Compiled one or two elements at a
time across a research session.

**Methodology:** Only resources that ACTUALLY support OpenCode are
included (native, adapter/port, open standard, or explicitly flagged as
claimed-but-unverified). Claude-Code-only or other-agent-only resources
are noted in footer sections per element for context, not included as
usable results. Every entry specifies HOW it supports OpenCode: **Native**
(built specifically for OpenCode), **Documented port/adapter** (built
elsewhere, explicit OpenCode integration confirmed), **Works via open
standard** (protocol-level compatibility, e.g. MCP), or **Claimed but
unverified** (stated support not independently confirmed in this sweep).

**Coverage note:** Element #1 (Skills) was completed in an earlier
session whose output file is not available in this compilation — it is
omitted here rather than reconstructed. Elements #2 and #3 (Permission
Modes and Checkpoints/Rewind Tools) were combined into a single file by
original design. All other elements (4 through 26) are included in full
below, unedited from their original sweep output.

---

## Table of Contents

- [Elements 2 & 3: Permission Modes + Checkpoints/Rewind Tools](#elements-2--3-permission-modes--checkpointsrewind-tools)
- [Element 4: Context Management Tools](#element-4-context-management-tools)
- [Element 5: Hooks (collections/frameworks)](#element-5-hooks-collectionsframeworks)
- [Element 6: MCP Servers](#element-6-mcp-servers)
- [Element 7: Sandboxing Tools](#element-7-sandboxing-tools)
- [Element 8: Subagents (collections)](#element-8-subagents-collections)
- [Element 9: Plugins / Plugin Marketplaces](#element-9-plugins--plugin-marketplaces)
- [Element 10: Output Styles](#element-10-output-styles)
- [Element 11: Background Task Tools](#element-11-background-task-tools)
- [Element 12: Security-Review Tools](#element-12-security-review-tools)
- [Element 13: Headless / CI Setups](#element-13-headless--ci-setups)
- [Element 14: Usage / Cost Tracking Tools](#element-14-usage--cost-tracking-tools)
- [Element 15: Agent-Team Frameworks](#element-15-agent-team-frameworks)
- [Element 16: Workflow Orchestration Tools](#element-16-workflow-orchestration-tools)
- [Element 17: Agent SDKs](#element-17-agent-sdks)
- [Element 18: Discipline/Skill Packs (Superpowers/ponytail-style)](#element-18-disciplineskill-packs-superpowersponytail-style)
- [Element 19: Docs-Context MCP Servers (Context7-style)](#element-19-docs-context-mcp-servers-context7-style)
- [Element 20: Statusline Tools](#element-20-statusline-tools)
- [Element 21: Git-Worktree Helpers](#element-21-git-worktree-helpers)
- [Element 22: Awesome-Lists (AI Coding Agents, Cross-Tool)](#element-22-awesome-lists-ai-coding-agents-cross-tool)
- [Element 23: Security Scanners for Agent Configs](#element-23-security-scanners-for-agent-configs)
- [Element 24: Safety-Net / Guardrail Tools](#element-24-safety-net--guardrail-tools)
- [Element 25: Hook Management CLIs](#element-25-hook-management-clis)
- [Element 26: Self-Improving / Instinct-Mining Tools](#element-26-self-improving--instinct-mining-tools)

---

# Elements 2 & 3: Permission Modes + Checkpoints/Rewind Tools

Combined sweep file per user request.

---

# Element 2: Permission Modes (configs/presets)

Scope: configs, presets, skills, or workarounds that control OpenCode's
allow/ask/deny permission system or add Claude-Code-style mode-switching
(plan/build/auto) on top of it.

Context: OpenCode ships a **native** built-in permission system
(`permission` block in `opencode.json`/`opencode.jsonc`, per-agent overrides,
`--auto` flag, TUI auto-approve toggle). Anything below is either (a) a
ready-made preset/config people share, or (b) a workaround/plugin trying to
add a mode-switch UX Claude Code has (Shift+Tab cycling) that OpenCode's core
doesn't natively offer yet.

---

## Well-known / high-star

**[opencode-config](https://github.com/joelhooks/opencode-config)** — 362 stars, active (recent commits per repo activity) — Joel Hooks' full personal OpenCode setup: commands, custom MCP tools, agents, and a `permission` block in `opencode.jsonc` covering allow/ask/deny per agent (planner/worker/explore/archaeologist/beads/refactorer/reviewer each get different permission profiles) — OpenCode support: **Native** (it's a real `opencode.jsonc` config, directly consumable/adaptable by OpenCode; no adapter needed).

## Actively maintained but smaller

**[opencode-permissions](https://github.com/NjengaFelix/opencode-permissions)** — 0 stars, 2 commits, recent — an OpenCode *Skill* (SKILL.md) packaging permission templates: "Production-Safe," "Developer-Friendly," and "Read-Only Exploration" presets, plus pattern-based bash allow/deny examples — OpenCode support: **Native** (ships as an OpenCode skill consumed directly via `~/.config/opencode/skills/`, and the JSON it generates is native `opencode.json` permission config).

**[Sandboxing opencode on macOS (Amin's blog + repo profile)](https://aminroosta.github.io/tools/llm/security/macos/2026/02/25/sandboxing-opencode-on-macos.html)** — blog post w/ linked repo, dated Feb 25 2026 — a recommended `~/.config/opencode/opencode.json` permission profile pairing OpenCode's native permission block with a macOS `sandbox-exec` "seatbelt" wrapper (denies-by-default, allowlists specific external dirs, restricts `agent.build.tools`) — OpenCode support: **Native** (it's literally OpenCode's own config schema; the sandbox layer is OS-level, not OpenCode-specific).

## Old or possibly abandoned

*(none found meeting the bar for this element — the space is very new; most permission-mode artifacts are <6 months old)*

---

## Related core feature (not third-party, for context)

- **OpenCode's own `permission` config + `--auto` flag + TUI auto-approve toggle** (opencode.ai/docs/permissions) is the native mechanism everything above builds on. Object-syntax rules (`allow`/`ask`/`deny`), per-agent overrides in Markdown frontmatter, and glob-pattern bash matching are all built in — no third-party tool is required for basic mode control.
- **Open GitHub issue [#7928](https://github.com/anomalyco/opencode/issues/7928)** requests a native Shift+Tab-style runtime mode toggle (Normal/Plan/Auto) matching Claude Code's UX — not yet implemented; current workaround is defining separate agents with different `permission` blocks and switching agents with Tab, which the issue itself notes is clunky (separate conversation contexts per agent).

---

## Claude-Code-only, excluded

- **Claude Code's Shift+Tab permission-mode cycling** — native keybind in Claude Code's own TUI; no OpenCode equivalent exists yet (tracked in the open feature request above).
- Various `.claude/settings.json` "permissions" preset gists/repos found in search that only target Claude Code's own JSON schema with no OpenCode-compatible output or stated port.

---

**Total found:** 3 usable (1 well-known, 2 smaller/active) + 2 Claude-Code-only excluded.

**Summary:** Permission "mode presets" for OpenCode are almost all native `opencode.json`/`opencode.jsonc` permission blocks (allow/ask/deny) shared as configs or skills — there's no separate ecosystem/format to port from Claude Code because OpenCode's permission system already covers the same ground. The one real gap is Claude Code's Shift+Tab quick-cycle UX, which is an open OpenCode feature request, not yet solved by any third-party tool.

-e 

---


# Element 3: Checkpoints / Rewind Tools

Scope: tools that snapshot working-tree/conversation state during an agent
session so you can roll back — either purpose-built for OpenCode or
cross-tool tools with a confirmed OpenCode integration.

Context: OpenCode has a **native** built-in `/undo` (and companion `/redo`)
backed by an internal Git object database (opencode.ai/v2/docs/snapshots) —
it restores file paths per completed assistant step without touching your
real Git index/branches. It's reported as somewhat unreliable in places
(see community feedback below), which is the gap the third-party tools
below are filling.

---

## Well-known / high-star

**[Entire CLI](https://github.com/entireio/cli)** — 4.3k stars, 332 forks, latest release v0.6.1 (May 7, 2026), 4,266 commits, very active — Git-native session/checkpoint capture tool: hooks into commits, stores full prompt/response transcripts + file diffs on a separate `entire/checkpoints/v1` branch, supports `entire checkpoint rewind` and `entire session resume` — OpenCode support: **Native** (ships a first-class OpenCode integration — `entire enable --agent opencode` installs a real `.opencode/plugins/entire.ts` TypeScript plugin using OpenCode's plugin/event system; docs confirm session-detection via OpenCode's own `session.created`/`session.idle` events and transcript export via `opencode export`. Docs flag this specific integration as "in preview," Bun-runtime-dependent).

## Actively maintained but smaller

**[opencode-rewind (opencode-checkpoint)](https://github.com/KyungJunAn/opencode-rewind)** — 0 stars, 3 commits — a small OpenCode plugin (`opencode-checkpoint.js`) that snapshots the working tree to a separate `opencode/checkpoints` branch on every `session.idle` event, with `restore_checkpoint` and `list_checkpoints` agent-callable tools, using `git commit-tree` so it never touches your real branch — OpenCode support: **Native** (it's an OpenCode plugin built directly against OpenCode's plugin API and event system — `.opencode/plugin/` install path).

## Old or possibly abandoned

*(none — every checkpoint/rewind tool found targeting OpenCode is from the last few months; nothing stale yet in this space)*

---

## Related core feature (not third-party, for context)

- **OpenCode's native `/undo` / `/redo`** (opencode.ai/v2/docs/snapshots) — internal Git object DB, restores only paths touched by cleanly-completed assistant steps after a chosen conversation point; doesn't create commits or move branches. Community reports (e.g. openai/codex discussion #9618) describe it as "still highly unreliable (and frequently broken)" as of recent months, and there's an **open feature request** ([issue #29980](https://github.com/anomalyco/opencode/issues/29980)) asking for a full Claude-Code-style `/rewind` that also rolls back *conversation* history, not just files — currently `/undo` only reverts file changes, not context.
- **SDK hooks in progress**: [issue #7553](https://github.com/anomalyco/opencode/issues/7553) proposes exposing `snapshot.track()` and `session.addPart()` so third-party plugins (like the two above) can register their own checkpoints into OpenCode's native undo history — not yet merged, worth watching since it would let plugin checkpoints interop with `/undo`.

---

## Claude-Code-only, excluded

- **pi-rewind** (arpagon/pi-rewind) — built for the "Pi" coding agent, not OpenCode; its own docs list OpenCode's `/undo` only as a competitor feature it was benchmarked against, not something it integrates with.
- **checkpoint-pi** / **pi-rewind-hook** — same Pi-agent ecosystem, no OpenCode path.
- Claude Code's own `/rewind` command and Esc+Esc checkpoint shortcut — native to Claude Code's TUI only.
- Various "Claude Code checkpoint-workflow plugin" results from `github.com/topics/checkpoint` (memory/doc-refresh + git-commit checkpoint plugins) — explicitly Claude-Code-plugin-tagged, no AGENTS.md/MCP/OpenCode path found.

---

**Total found:** 2 usable (1 well-known, 1 smaller) + 4 Claude-Code/other-agent-only excluded.

**Summary:** Entire CLI is the clear standout — high-star, actively maintained, and ships a real native OpenCode plugin integration (currently in preview). The smaller opencode-rewind plugin is a lightweight single-purpose alternative if you don't want Entire's full session/audit-trail overhead. OpenCode's own native `/undo` exists but is reported unreliable and file-only (no conversation rewind), which is exactly the gap both third-party tools target.

---

# Element 4: Context Management Tools

Scope: tools/plugins that manage, compact, prune, or extend the conversation
context window for OpenCode — either built for OpenCode natively or ported
from Claude Code with a confirmed OpenCode path.

Context: OpenCode has **native** built-in context management: storage/model-
context separation, auto-compaction (`compaction.auto`/`compaction.prune`),
pruning placeholders for heavy tool output, and a documented design
philosophy (see the "Context management opencode" gist referenced in
search) of curating a slice of stored history rather than deleting it. All
tools below either replace, extend, or add manual control on top of that
native system.

---

## Well-known / high-star

**[opencode-dynamic-context-pruning (DCP)](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)** — 3.9k stars, 216 forks, 1,365 commits, very active (npm: `@tarquinen/opencode-dcp`) — model-driven context pruning plugin: exposes a `compress` tool the model calls when it decides context is stale (not a static threshold trigger like native compaction), plus automatic deduplication of repeated tool calls and pruning of errored-tool inputs after N turns; protects `task`/`skill`/`todowrite`/etc. from pruning by default — OpenCode support: **Native** (published and installed as a first-class OpenCode plugin via `opencode plugin @tarquinen/opencode-dcp@latest --global`; config lives under `.opencode/dcp.json(c)`). Note: primary development has since shifted to a separate cross-harness tool called "Sleev" — DCP itself is now in maintenance mode per the repo's own README.

## Actively maintained but smaller

**[magic-context (CortexKit)](https://github.com/cortexkit/magic-context)** — recently updated (repo activity ~6 days old per search), part of "CortexKit" — background/automatic context manager: runs a separate "historian" model to compress older conversation while the main agent keeps working, persists cross-session project memory, and an "overnight dreamer" agent that consolidates and deduplicates memories — explicitly designed to disable itself if OpenCode's native compaction or DCP (above) is also active, to avoid double-compression — OpenCode support: **Native** (ships as an OpenCode plugin — see companion repo below — that directly detects and coordinates with OpenCode's own `compaction.auto`/`compaction.prune` settings).

**[opencode-magic-context](https://github.com/g1331/opencode-magic-context)** — the actual OpenCode plugin implementation of Magic Context (companion/fork of cortexkit/magic-context) — adds a TUI sidebar showing live context breakdown, token usage, and historian status directly in the OpenCode terminal, plus five agent-callable tools including `ctx_reduce` — OpenCode support: **Native** (built specifically as an OpenCode plugin, using OpenCode's plugin/TUI extension points).

**[magic-compact](https://github.com/aerovato/magic-compact)** — ~129 stars (per SkillsLLM security-scan listing) — "lossless" context compression: instead of collapsing history into one generic summary, it condenses each old assistant turn into its own summary while preserving user messages and tool calls verbatim; ships a `/magic-compact [N]` command (N = turns to preserve) and a separate `/magic-trim [N]` for tool I/O pruning only; creates a session backup before compacting — OpenCode support: **Native** (explicit dual-platform plugin — README states "Lossless context compression plugin for Claude Code & OpenCode," installed via `opencode plugin magic-compact --global`; author notes OpenCode support will deepen as OpenCode's plugin API exposes more hooks, i.e. currently a bit behind the Claude Code side but fully functional).

## Old or possibly abandoned

*(none found — this is an active, fast-moving space; even DCP, the most "settled" entry, is only recently in maintenance mode with an active successor)*

---

## Related core feature (not third-party, for context)

- **OpenCode's native context management**: storage/model-context separation, auto-compaction with configurable thresholds, pruning placeholders for heavy tool output, and plugin hooks for customizing prompts/injected context (opencode.ai docs + community design-reference gist). This is the baseline every tool above builds on or replaces.

---

## Claude-Code-only, excluded

- **Amp's context tools** (Handoff / Fork / Edit-Restore / Thread References) — referenced in the cross-tool "Context Compaction Research" gist as a different agent's (Amp's) manual-context-management approach; no OpenCode port found.
- Generic **Claude Code `/compact [instructions]`** custom-instruction compaction — native Claude Code feature; OpenCode's compaction doesn't yet support inline custom instructions the same way (per the same research gist).

---

**Total found:** 4 usable (1 well-known/high-star, 3 smaller-but-active) + 2 Claude-Code/other-agent-only excluded.

**Summary:** DCP is the dominant, high-star tool but is now in maintenance mode with development moving to a separate cross-harness successor ("Sleev"). Magic Context (CortexKit) is the newer, actively-developed alternative taking a "background historian" approach instead of DCP's model-triggered compression. Magic Compact targets a different failure mode (lossless per-turn summaries vs. native compaction's single blob) and explicitly supports both Claude Code and OpenCode as first-class targets, though the OpenCode side is currently the less mature of the two.

---

# Element 5: Hooks (collections/frameworks)

Scope: collections or frameworks of lifecycle hooks for OpenCode — either
native OpenCode hook systems/plugins, or Claude-Code-hooks compatibility
layers that port onto OpenCode's own event system.

Context: OpenCode has a **native** built-in plugin/hook system: plugins
subscribe to lifecycle events (`session.created`, `session.idle`,
`tool.execute.before`, `file.edited`, `permission.updated`, `message.part.updated`,
etc.) via a `Plugin` function that returns named hook handlers. This is
documented at opencode.ai and is the substrate every framework below is
built on.

---

## Well-known / high-star

**[oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** (formerly/also published as `oh-my-opencode`) — 67.3k stars, 5.5k forks, 11,932 commits, extremely active — the dominant OpenCode "batteries included" plugin: ships 54+ lifecycle hooks (61 with Team Mode enabled) across categories like rules-injection, todo-enforcement, comment-checking, auto-resume, and a **full Claude Code hooks-compatibility layer** (PreToolUse, PostToolUse, UserPromptSubmit, Stop events all supported) alongside its own agents/MCPs/tools — OpenCode support: **Native** (it *is* an OpenCode plugin, installed via `bunx oh-my-openagent install`, registered in `opencode.json`'s `plugin` array; the Claude Code hook compatibility is a bonus layer inside it, not the core mechanism). Note: repo/README states Anthropic has restricted OAuth access citing this project by name as a reason for blocking some OpenCode usage patterns (see the repo's own "Claude OAuth Access Notice" section) — relevant context if using it with a Claude subscription.

*(Note: `opensoft/oh-my-opencode`, 657 stars, is a fork/mirror of the above under the pre-rename name — same project, smaller star count because stars didn't migrate with the fork. Treat as the same tool; use the 67.3k-star canonical repo as the reference.)*

## Actively maintained but smaller

**[Opencode Hooks Plugin](https://github.com/awesome-opencode/awesome-opencode)** (listed entry, exact repo name not separately confirmed beyond the awesome-list description) — "Use Claude code hooks definition and hook them to opencode hooks" — a lightweight, single-purpose compatibility shim distinct from oh-my-openagent's bundled version, aimed at people who want *just* Claude Code hook-format support without the rest of oh-my-openagent's agent/MCP bundle — OpenCode support: **Documented port/adapter** (translates Claude Code's hooks JSON schema into OpenCode's native plugin hook calls; listed in the community awesome-opencode curated directory specifically under hook-compatibility tooling).

**[OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** — ~4.5–4.6k stars (star count fluctuates slightly across cached pages, consistently in this range), active — a plan-first, approval-gated agent framework with a `.opencode/plugin/` directory that auto-loads plugins on OpenCode startup, 7 specialized subagents, and a context/pattern-injection system (`/add-context`); its plugin layer implements hook-style lifecycle behavior (approval gates before write/edit/bash) — OpenCode support: **Native** (built directly on OpenCode's `.opencode/plugin/` and `.opencode/agent/` conventions; also separately distributed as a Claude Code plugin, but the OpenCode integration is first-class, not a port).

## Old or possibly abandoned

*(none identified — hooks/plugin frameworks for OpenCode are a very active area right now; nothing stale surfaced)*

---

## Related core feature (not third-party, for context)

- **OpenCode's native plugin/event system** (opencode.ai plugin docs) — `session.created`, `session.updated`, `session.deleted`, `session.error`, `session.idle`, `message.updated/removed/part.updated/part.removed`, `file.edited`, `file.watcher.updated`, `permission.updated/replied`, `server.connected`, `lsp.updated`. Every framework above is a layer on top of this native event list, not a separate mechanism.
- **V2 plugin API** (per opencode-primer changelog notes, v1.17.10+) adds namespaced plugin hooks and Effect/Promise-based plugin support — worth knowing since some hook frameworks may target the older vs. newer plugin API generation.

---

## Claude-Code-only, excluded

- **Claude Code's native hooks system** itself (PreToolUse, PostToolUse, Notification, SubagentStop, PreCompact, SessionStart, SessionEnd, etc., per Anthropic's own hooks-guide docs) — this is the *source* format that OpenCode-facing tools like "Opencode Hooks Plugin" and oh-my-openagent's compatibility layer translate from; the native system itself has no direct OpenCode execution path without going through one of those adapters.
- **rins_hooks** (maker95/rins_hooks) — auto-commit, code-formatter, and notification hooks, but built and documented specifically for Claude Code's hooks directory (`~/.claude/hooks/`); no OpenCode installation path found.
- **Claude Code Memory Awareness Hooks** (doobidoo/mcp-memory-service `claude-hooks/`) — installs into `~/.claude/hooks/` specifically; Windows/Node installer targets Claude Code's directory structure only, no OpenCode adapter found.

---

**Total found:** 3 usable (1 dominant/very-high-star, 2 smaller-but-active) + 3 Claude-Code-only excluded.

**Summary:** oh-my-openagent (67.3k★) is overwhelmingly the dominant hooks/plugin framework for OpenCode and already includes a full Claude Code hooks-compatibility layer as one of its many features — for most people it subsumes the need for a separate standalone hooks adapter. If you want *only* the Claude-Code-hooks-translation piece without the rest of oh-my-openagent's bundled agents/MCPs, the smaller "Opencode Hooks Plugin" is the lighter-weight alternative. OpenAgentsControl is a different category (a full plan-first agent framework) that happens to implement its approval-gate behavior via OpenCode's native plugin hooks.

---

# Element 6: MCP Servers

Scope: notable MCP (Model Context Protocol) servers, with confirmed
OpenCode support — either because MCP itself is the open standard
OpenCode implements natively, or because the server ships an OpenCode-
specific integration/adapter.

Context: **This element is structurally different from the others.** MCP is
an open, cross-tool standard (originated by Anthropic, now widely adopted).
OpenCode has **native, first-class MCP client support** — both local
(stdio) and remote (HTTP/SSE) servers are configured directly under the
`mcp` key in `opencode.json`/`opencode.jsonc`, with automatic OAuth via
Dynamic Client Registration (RFC 7591) for remote servers that require it.
This means **the overwhelming majority of published MCP servers work with
OpenCode "for free"** — no OpenCode-specific porting needed, because the
server just speaks the protocol OpenCode already implements. The main
caveat: OpenCode currently uses a `mcp` config key structurally different
from the `mcpServers` key used by Claude Code/Cursor/Gemini CLI, so copy-
pasting a config block requires a small reshape (tracked in an open
OpenCode feature request, noted below) — this is a config-format
difference, not a protocol-compatibility issue.

---

## Well-known / high-star (general-purpose MCP servers, OpenCode-native via the open standard)

**[Context7](https://github.com/upstash/context7)** — 39.3k+ stars — fetches current, version-specific library documentation and injects it into the agent's context on request (triggered via "use context7" in the prompt) — OpenCode support: **Works via open standard** (plain MCP server, added under `opencode.json`'s `mcp` key like any other; no Claude-Code-specific dependency).

**[GitHub MCP Server](https://github.com/github/github-mcp-server)** — 27.4k+ stars — official GitHub server: repo/PR/issue management, code search, Actions logs — OpenCode support: **Works via open standard**, and additionally has an **explicit official OpenCode install guide** (`docs/installation-guides/install-opencode.md`) with exact `opencode.json` config examples for both Docker and OAuth/PAT auth flows — closer to "Native/documented" than most, since GitHub itself publishes the OpenCode-specific config.

**[Playwright MCP](https://github.com/microsoft/playwright-mcp)** — 30.6k+ stars — official Microsoft server for browser automation via structured accessibility snapshots — OpenCode support: **Works via open standard** (plain stdio MCP server).

**Filesystem MCP** (reference server, part of the official MCP servers collection) and **Postgres/Supabase/Sentry/Stripe/Notion/Cloudflare MCP servers** — all widely-cited "top 10" servers per multiple 2026 roundups — OpenCode support: **Works via open standard** for all — none of these are Claude-Code-specific; they're added identically under OpenCode's `mcp` config.

## Actively maintained but smaller — OpenCode-specific MCP tooling

**[opencode-mcp (Traves-Theberge)](https://github.com/Traves-Theberge/opencode-mcp)** — exposes **OpenCode itself** as an MCP server/subagent, so other MCP clients (Claude Desktop, Cursor, Claude Code, etc.) can delegate coding tasks *to* OpenCode — OpenCode support: **Native** (this tool's entire purpose is bridging into OpenCode's own headless/server API; it's not something OpenCode consumes, but something that consumes OpenCode).

**[opencode-mcp (AlaeddineMessadi)](https://github.com/AlaeddineMessadi/opencode-mcp)** — similarly bridges any MCP client to OpenCode's headless API (80 tools, 10 resources, 6 prompts) so e.g. Claude can delegate "build me a REST API" work to an autonomous OpenCode session — OpenCode support: **Native** (built directly against OpenCode's headless server API).

**[opencode-docs-mcp](https://github.com/sandbox-technologies/opencode-docs-mcp)** — a Mintlify-style MCP server that serves OpenCode's own documentation (search, get-page, browse-toc) — usable *from* OpenCode via its own `mcp` config, and useful for agents needing to answer questions about OpenCode itself — OpenCode support: **Works via open standard** (also ships an `opencode.json` config snippet directly in its README).

## Old or possibly abandoned

*(not applicable in the usual sense — the general-purpose MCP servers above are all actively maintained by their vendors; no stale OpenCode-specific MCP tooling identified)*

---

## Related open item (not a resource, for context)

- **[Issue #27809](https://github.com/anomalyco/opencode/issues/27809)** — open feature request asking OpenCode to also accept the `mcpServers` key format (used by Claude Code, Gemini CLI, Cursor) directly in `opencode.json`, so configs can be copy-pasted without reshaping. Not yet merged — currently you must convert `mcpServers: {...}` to OpenCode's `mcp: {...}` structure by hand (usually a small key/shape change, not a protocol change).

---

## Claude-Code-only, excluded

*(none identified — because MCP is an open standard and OpenCode has full native client support, essentially nothing in the popular MCP server ecosystem is "Claude-Code-only." The only genuinely excludable category would be Claude-Code-specific *hook* or *skill* integrations bundled alongside an MCP server, which are covered in Elements 1 and 5, not here.)*

---

**Total found:** effectively the entire popular MCP server ecosystem (illustrative sample: Context7, GitHub MCP, Playwright MCP, Filesystem, Postgres/Supabase, Sentry, Stripe, Notion, Cloudflare — all Native-via-open-standard) + 3 OpenCode-specific bridging tools + 0 excluded.

**Summary:** Unlike every other element in this sweep, MCP servers don't need individual "does this support OpenCode" verification for the general population of servers — OpenCode's native MCP client (local + remote, with automatic OAuth) means virtually any published MCP server works out of the box via the open standard. The genuinely OpenCode-specific finds are the reverse-direction tools (opencode-mcp x2, opencode-docs-mcp) that expose OpenCode itself as, or to, other MCP clients. The one real friction point is a config-key-naming mismatch (`mcp` vs `mcpServers`) that's an open GitHub issue, not a compatibility gap.

---

# Element 7: Sandboxing Tools

Scope: tools that isolate OpenCode's execution (filesystem/network/process)
from the host — either OpenCode-native sandbox mechanisms, OpenCode-specific
plugins/wrappers, or cross-tool sandbox runtimes with confirmed OpenCode
support.

Context: OpenCode has **native, built-in OS-level sandboxing** as of recent
versions — a "restrictiveness lattice" implementation covering Bubblewrap
(Linux namespaces), gVisor, Firecracker, and Seatbelt (macOS), per source
references (`packages/opencode/src/sandbox/{index,bwrap,darwin,gvisor,
firecracker,linux}.ts`) cited in independent technical writeups. This is a
meaningfully different starting point from most other coding agents, which
rely entirely on third-party Docker wrappers for isolation.

---

## Well-known / high-star

*(No single third-party sandboxing tool for OpenCode has broken out to
high-star status yet — this space is fragmented across many small,
similarly-scoped Docker-wrapper repos, reflecting how recently OpenCode's
own native sandbox landed. The most notable "high visibility" entries are
vendor efforts rather than community stars — see below.)*

**[Docker Sandboxes](https://www.docker.com/blog/docker-sandboxes-a-new-approach-for-coding-agent-safety/)** — official Docker initiative (blog-announced, in active development) — purpose-built local sandboxes that wrap coding agents (explicitly including OpenCode, alongside Claude Code, Gemini CLI, Codex, Kiro) in containers mirroring the local workspace with enforced boundaries — OpenCode support: **Documented port/adapter** (Docker explicitly lists OpenCode as one of the supported agents this feature targets; not a community plugin but a vendor-backed adapter).

## Actively maintained but smaller

**[opencode-sandbox (npm package, via bubblewrap)](https://npmx.dev/package/opencode-sandbox)** — an OpenCode **plugin** (auto-installed from npm) that wraps every `bash` tool invocation using `@anthropic-ai/sandbox-runtime`, applying OS-level filesystem/network restrictions via Bubblewrap — no containers or VMs; intercepts via `tool.execute.before`/`tool.execute.after` hooks and gracefully falls back to unsandboxed execution if bubblewrap/init fails — OpenCode support: **Native** (built directly as an OpenCode plugin using OpenCode's own hook system; also directly builds on Anthropic's `sandbox-runtime` package, making it a genuine cross-tool bridge).

**[thisisryanswift/opencode-sandbox](https://github.com/thisisryanswift/opencode-sandbox)** — an OpenCode plugin that auto-provisions isolated sandboxes (Daytona, E2B, Sprites, or Docker fallback, auto-detected) per session; syncs project files in, respects `.gitignore` so secrets never enter the sandbox, translates paths transparently, and syncs changes back via git on idle — OpenCode support: **Native** (plugin architecture under `.opencode/plugin/`, directly using OpenCode's plugin/session lifecycle).

**[comsysto/opencode-sandbox](https://github.com/comsysto/opencode-sandbox)** — Docker + `mise`-based sandbox giving each project scoped filesystem access, independent per-project provider/API-key config, and persistent session state across container restarts; ships an interactive `ocs-init` setup wizard — OpenCode support: **Native** (purpose-built specifically to wrap OpenCode; generates `opencode.jsonc` as part of its own init flow).

**[mattolson/agent-sandbox (agentbox)](https://github.com/mattolson/agent-sandbox)** — general secure local dev environment for AI coding agents (not OpenCode-exclusive) with a policy-based network proxy restricting which provider endpoints are reachable — has a **documented OpenCode agent guide** (`docs/agents/opencode.md`) covering config-based permission setup and provider policy files specific to OpenCode — OpenCode support: **Documented port/adapter** (explicit first-party OpenCode documentation page, distinct from its Claude Code / Codex / Gemini docs).

**[rivet-dev/sandbox-agent](https://github.com/rivet-dev/sandbox-agent)** — Rust-based universal HTTP adapter for running coding agents (Claude Code, Codex, OpenCode, Amp, Pi) inside sandboxes and controlling them remotely; ships an **experimental OpenCode-compatible API** (`/opencode` endpoint) so OpenCode SDK/UI clients can connect through it — OpenCode support: **Documented port/adapter** (explicit "OpenCode Compatibility" doc page; flagged experimental by the maintainers, provider/model metadata "may differ from native OpenCode grouping").

**[arezi/opencode-sandbox](https://github.com/arezi/opencode-sandbox)** and **[fabianlema/opencode-sandbox](https://github.com/fabianlema/opencode-sandbox)** — both simple Docker-wrapper scripts (mapped home directory / pre-installed dev tools respectively) that run the OpenCode binary inside a container — OpenCode support: **Native** (purpose-built OpenCode wrappers, though very thin — essentially `docker run` scripts, not deep integrations).

**[JulScsl/opencode-sandbox](https://github.com/JulScsl/opencode-sandbox)** — Windows-specific variant using Podman/Docker, bundles Serena alongside OpenCode — OpenCode support: **Native** (purpose-built OpenCode wrapper for Windows).

**[zaid-marji/opencode-sandbox](https://github.com/zaid-marji/opencode-sandbox)** — minimal Docker wrapper mounting only the project directory plus a dedicated OpenCode-state directory, runs as non-root, documents optional hardening flags (`--read-only`, `--cap-drop=ALL`) — OpenCode support: **Native** (purpose-built OpenCode wrapper).

## Old or possibly abandoned

*(none confirmed stale — most of these repos are recent, reflecting how new both OpenCode's own sandbox and the third-party wrapper ecosystem are)*

---

## Related core feature (not third-party, for context)

- **OpenCode's native OS-level sandbox** (Bubblewrap/gVisor/Firecracker/Seatbelt via a restrictiveness-lattice design, per `packages/opencode/src/sandbox/`) and its companion **trust system** (`packages/opencode/src/trust/`, governing `opencode trust` for granting a repo/MCP server host access) — this is a materially different baseline from agents that rely solely on external Docker wrappers, and most of the third-party tools above either complement it (adding container-level isolation on top) or specifically target the gap it doesn't yet cover (per the DEV Community writeup: MCP servers themselves, which still run unsandboxed as a "zero-click supply-chain vector").

---

## Claude-Code-only, excluded

- **OpenClaw's Docker sandbox subsystem** (`src/agents/sandbox/docker.ts`) — referenced in an arXiv security analysis; this is a different agent framework (OpenClaw), not OpenCode, and the analysis is describing a *vulnerability* in OpenClaw's implementation, not an OpenCode-compatible tool.
- **NVIDIA OpenShell** sandbox images — lists OpenCode as having only "Partial Policy Coverage" ("Pre-installed. Add opencode.ai endpoint and OpenCode binary paths to the policy for full functionality") vs. Claude Code's "Full coverage" — included here as a caveat rather than excluded outright, since it does technically support OpenCode, just with more manual policy setup required than for Claude Code.

---

**Total found:** 9 usable (0 breakout-high-star, 1 notable vendor effort, 8 smaller/active) + 1 flagged-partial-coverage note + 1 excluded (different framework, not OpenCode).

**Summary:** OpenCode's own native OS-level sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt) means the baseline security posture here is already stronger than many competing agents that depend entirely on external wrappers — but the third-party ecosystem is still useful for container-level isolation (fully separating OpenCode's process from the host, not just restricting its syscalls) and for cloud/remote sandbox providers (Daytona, E2B, Sprites). No tool has yet become a clear community standard; the field is fragmented across many small, similarly-scoped `opencode-sandbox`-named repos plus one notable vendor effort (Docker Sandboxes) and one general-purpose cross-agent tool (agentbox) with dedicated OpenCode docs.

---

# Element 8: Subagents (collections)

Scope: collections of pre-built specialized subagent definitions for
OpenCode — either native OpenCode subagent-format collections, or
cross-tool collections with a documented OpenCode path.

Context: OpenCode has **native** built-in subagent support: three built-in
subagents (General, Explore, Scout) plus a documented format for custom
ones — Markdown files with YAML frontmatter (`mode: subagent`, `tools:`,
`permission:`, etc.) placed under `~/.config/opencode/agents/` (global) or
`.opencode/agents/` (project). This is structurally similar to Claude
Code's subagent format but lives in a different directory and has some
frontmatter differences, which is why "collections" need an actual
OpenCode-targeted release or install path to count here — a same-named
fork with unconverted install instructions does not.

---

## Well-known / high-star

**[awesome-opencode-subagents](https://github.com/ankitmundada/awesome-opencode-subagents)** — "100+ subagents for opencode" (star count not independently confirmed in search results, but positioned by the author as "the definitive collection of OpenCode CLI subagents") — organized into 10 categories (core development, language specialists, infrastructure, quality/security, data/AI, developer experience, specialized domains, business/product, meta-orchestration, research/analysis); ships an interactive `install-agents.sh` script that browses categories and installs/uninstalls agents individually, plus a curl-based installer that doesn't require cloning — OpenCode support: **Native** (each subagent is a Markdown file with YAML frontmatter written specifically for OpenCode's `~/.config/opencode/agents/` / `.opencode/agents/` convention; the companion `awesome-gemini-cli-subagents` repo by the same author confirms a deliberate per-tool-format release pattern, not a blind cross-post).

## Actively maintained but smaller

**[OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** — ~4.5–4.6k stars (see Element 5 for full detail) — ships 7 specialized subagents (task-manager, context-scout, context-manager, coder-agent, test-engineer, code-reviewer, external-scout) plus category specialists (frontend, devops, copywriter, technical-writer, data-analyst) as part of its broader plan-first framework — OpenCode support: **Native** (subagents defined directly in `.opencode/agent/` following OpenCode's own format; also separately distributed as a Claude Code plugin, but the OpenCode agents are first-class, not ported).

**[oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** — 67.3k stars (see Element 5) — ships a curated set of purpose-built agents (Sisyphus main orchestrator, Prometheus planner, Oracle for architecture/debugging, Librarian for docs/code search, Explore for fast grep, Hephaestus autonomous worker) with each tuned to a specific model — OpenCode support: **Native** (agents are core to the plugin's own OpenCode-specific architecture, not a separate "collection" bolted on).

## Old or possibly abandoned

*(none identified as stale — the space is active)*

---

## Related core feature (not third-party, for context)

- **OpenCode's native built-in subagents**: General, Explore, and Scout ship by default; `@mention` syntax lets you manually invoke any subagent, and primary agents can invoke subagents automatically per the docs at opencode.ai/docs/agents.

---

## Claude-Code-only, excluded

- **[jbeck018/agents-opencode](https://github.com/jbeck018/agents-opencode)** (and its sibling fork **delatorre-forks/agents-opencode**) — despite the repo name containing "opencode," this is a direct fork of **[wshobson/agents](https://github.com/wshobson/agents)**, titled "Claude Code Subagents Collection" in its own README, with installation instructions pointing at `~/.claude/agents/` (Claude Code's directory) and explicit dependency on "Claude Code v1.0.64" subagent model-selection syntax. No OpenCode-specific install path, directory convention, or format conversion is present — the "opencode" in the repo name appears to be a naming/labeling artifact, not an actual port. Excluded despite the misleading name.
- Generic **95-agent "Claude Code Subagents Collection"** style repos surfaced in the `subagents`/`subagent` GitHub topic pages (e.g. wshobson/agents itself, and various 75+/130+-agent collections) — these are Claude Code– or Codex-specific by their own documentation, with no OpenCode adapter found.

---

**Total found:** 3 usable (1 dedicated high-visibility collection + 2 framework-bundled subagent sets) + 2 excluded (misleadingly-named fork + generic Claude-Code-only collections).

**Summary:** awesome-opencode-subagents is the one dedicated, OpenCode-native subagent collection built specifically in OpenCode's Markdown+frontmatter format and installer convention. Beyond that dedicated collection, the most useful subagent sets come bundled inside the two big OpenCode frameworks already covered in Element 5 (OpenAgentsControl, oh-my-openagent) rather than as standalone "just subagents" repos. Watch out for repos with "opencode" in the name that are actually unconverted Claude Code forks — jbeck018/agents-opencode is a clear example: same content as wshobson/agents, install path still `~/.claude/agents/`.

---

# Element 9: Plugins / Plugin Marketplaces

Scope: marketplaces, registries, and installer CLIs for discovering and
installing OpenCode plugins — either OpenCode-native marketplace tooling
or cross-tool marketplaces with a confirmed OpenCode install path.

Context: OpenCode has a **native** plugin system (`.opencode/plugin/` or
`~/.config/opencode/plugin/`, loadable from npm via the `plugin` config
array) but, as of this sweep, **no official first-party marketplace** —
this is explicitly called out by one of the tools below ("Opencode has no
an official market"). This element is therefore almost entirely
community-built marketplace/registry tooling filling that gap, plus one
experimental official-adjacent `/plugin` command.

---

## Well-known / high-star

**[awesome-opencode](https://github.com/awesome-opencode/awesome-opencode)** — 8.5k stars, 605 forks, active (data-driven: entries are YAML files validated against a JSON schema, README auto-generated by CI) — the largest curated directory of OpenCode plugins, themes, agents, and resources, organized by category (plugins, themes, agents, MCP, resources) with live star-count badges per entry — OpenCode support: **Native** (this is *the* de facto community index for OpenCode-native resources specifically; not a cross-tool list with occasional OpenCode entries).

## Actively maintained but smaller

**[opencode-marketplace (NikiforovAll)](https://github.com/NikiforovAll/opencode-marketplace)** — CLI for installing OpenCode plugins from local directories or GitHub repos/subfolders; understands OpenCode's actual plugin directory layout (`command/`, `agent/`, `skill/` — recognizing both `.opencode/` and `.claude/` prefixed variants for cross-compat), supports install/update/list/scan(dry-run)/uninstall — OpenCode support: **Native** (built specifically around OpenCode's own plugin component layout, with explicit awareness of the `.opencode/` convention).

**[opencode-market (CKGrafico)](https://github.com/CKGrafico/opencode-market)** — CLI explicitly built to fill the "OpenCode has no official marketplace" gap (per the maintainer's own linked GitHub comment on an OpenCode issue); registers marketplaces from a repo's `marketplace.json`, installs plugins globally (`~/.agents/`) or to project-local `.opencode/` folders; notably also converts **Claude Code and GitHub Copilot** agents/skills into OpenCode-compatible form — OpenCode support: **Native**, plus **documented port/adapter** for its Claude Code / Copilot conversion feature specifically.

**[opencode-plugin-marketplace (Tommertom)](https://github.com/Tommertom/opencode-plugin-marketplace)** — community-driven marketplace exposing a `/plugin` slash command (`list`, `install <name>`, `create <name>`, `remove <name>`) directly inside the OpenCode TUI; explicitly flagged experimental by its author, and submissions must validate against a `schema/plugin.schema.json` — OpenCode support: **Native** (installs a real OpenCode command file at `~/.config/opencode/command/plugin.md`; built entirely around OpenCode's own command system).

**[n-skills (numman-ali)](https://github.com/numman-ali/n-skills)** — curated marketplace distributed via the "openskills" universal installer; explicitly lists OpenCode as one of the supported targets alongside Claude Code, Cursor, Windsurf, and Cline, and states it "works with... anything that reads AGENTS.md" — OpenCode support: **Works via open standard** (relies on OpenCode's AGENTS.md / skill-discovery conventions rather than a bespoke OpenCode-only integration, and is explicitly cross-tool by design rather than OpenCode-native).

## Old or possibly abandoned

*(none identified as stale — this tooling category is very new, matching how recently OpenCode's own plugin system and the "no official marketplace" gap became relevant)*

---

## Related core feature / gap (not third-party, for context)

- OpenCode's own plugin config (`plugin` array in `opencode.json`, loading from npm or local paths) is native, but there is **no first-party marketplace or `/plugin` browsing UI shipped by OpenCode itself** as of this sweep — every tool above exists specifically to fill that gap, which is a meaningfully different situation from Claude Code, which has an official `/plugin` command and marketplace support built in.

---

## Claude-Code-only, excluded

- **[dashed/claude-marketplace](https://github.com/dashed/claude-marketplace)** — titled "a local marketplace for personal Claude Code skills and plugins"; notably its own README explicitly documents how to *manually* wire it into OpenCode (since "opencode has no marketplace concept" and doesn't auto-discover the way Claude Code does) — worth knowing as a manual-integration example, but the marketplace itself is Claude-Code-native, with OpenCode support requiring hand-editing `opencode.json` to point at its skill/MCP paths rather than any built-in adapter.
- **Anthropic's official Claude Code plugin directory** (referenced via aitmpl.com's "Claude Code Plugins & Marketplaces" roundup) — Anthropic-managed, Claude-Code-only, no OpenCode path.
- Generic Claude Code "component marketplace" listings surfaced in the aitmpl.com roundup (context-usage statuslines, persistent-context plugins, etc., described as "for Claude Code") — no OpenCode installation path confirmed for these specific entries.

---

**Total found:** 5 usable (1 high-star directory + 4 smaller/active installer tools) + 3 excluded (Claude-Code-native, one with a documented manual OpenCode workaround).

**Summary:** Because OpenCode itself ships no official marketplace, this category is dominated by community-built gap-fillers: awesome-opencode is the dominant curated *directory* (8.5k★, browse-and-click-through model), while NikiforovAll's and CKGrafico's tools are actual *installer CLIs* that fetch and place plugin files for you — CKGrafico's tool additionally bridges in Claude Code/Copilot content, converting it into OpenCode-usable form. Tommertom's `/plugin` command is the closest thing to an in-TUI marketplace experience today, though explicitly experimental.

---

# Element 10: Output Styles

Scope: tools/configs that let you swap OpenCode's overall communication
style/personality/system-prompt wholesale (Claude Code's "output styles"
concept) — either native OpenCode equivalents or ported/workaround
mechanisms.

Context: **OpenCode has no native "output styles" feature.** There is an
open, unresolved feature request — [Issue #5199](https://github.com/anomalyco/opencode/issues/5199),
"Add output-style feature similar to Claude Code" — explicitly asking for
Claude-Code-style output-style swapping to be added to OpenCode. As of this
sweep it remains open with no shipped feature. This makes Element 10 the
sparsest category so far: there is no dedicated "output styles collection"
ecosystem for OpenCode the way there is for skills or hooks. What exists
instead are two categories of workaround, both built on OpenCode's real,
native customization primitives (agents + system prompts):

1. **Per-agent custom system prompts** — OpenCode's native `agent` config
   (Markdown or JSON) lets each agent define its own `prompt` file,
   effectively giving you a different "style" per agent, switchable via
   Tab or `@mention`. This is the closest native equivalent to output
   styles, but it changes *which agent* you're talking to, not the *same*
   agent's style on the fly — a structurally different UX from Claude
   Code's single-command style swap.
2. **Plugin-level system prompt transforms** — OpenCode exposes an
   `experimental.chat.system.transform` plugin hook that lets a plugin
   mutate the assembled system-prompt array at request time (per a
   detailed prompt-construction pipeline writeup). No public plugin found
   yet builds a full "output style switcher" on top of this hook, but it
   is the technical mechanism any future one would use.

---

## Well-known / high-star

*(None — no dedicated output-style-switching tool or collection was found
for OpenCode. This is a genuine ecosystem gap, not a search miss.)*

## Actively maintained but smaller

*(None found — searches for "OpenCode output style," "OpenCode persona
switcher," and "OpenCode communication style plugin" surfaced only the
open feature request and general agent-configuration docs, not a
standalone tool.)*

## Old or possibly abandoned

*(Not applicable — nothing exists yet to have gone stale.)*

---

## Related core feature / gap (not third-party, for context)

- **[Issue #5199](https://github.com/anomalyco/opencode/issues/5199)** — open feature request for Claude-Code-style output styles; unresolved.
- **OpenCode's native per-agent `prompt` config** (opencode.ai/docs/agents) — each primary agent or subagent can point at its own system-prompt file, switchable via Tab/`@mention` — the practical native workaround for "different communication styles," at the cost of it being agent-switching rather than in-place style-switching.
- **`experimental.chat.system.transform` plugin hook** (documented in a third-party prompt-construction-pipeline writeup, not official docs) — the mechanism a future output-style plugin would likely use; explicitly labeled experimental, with a safety fallback restoring the original system prompt if a plugin empties the array.

---

## Claude-Code-only, excluded

- **Claude Code's native Output Styles feature** itself (`/output-style` command, style files swapping the system prompt while keeping tools/context intact) — the feature this entire element is modeled on; no OpenCode port exists.
- Various Claude Code "output style pack" gists/repos (e.g. curated `.claude/output-styles/` collections) surfaced in general searches — all target Claude Code's specific style-file format with no OpenCode-compatible install path.

---

**Total found:** 0 usable + 2 Claude-Code-only excluded (feature itself + style-pack examples), plus 2 native/partial workarounds documented above (not "resources" in the collectible sense, but the honest answer to "what fills this gap today").

**Summary:** This is a real gap in the OpenCode ecosystem, not a search failure — Claude Code's output-styles feature has no OpenCode equivalent, tracked by an open, unresolved feature request. The practical workaround today is defining multiple custom agents with different system prompts and switching between them (native, but structurally different from in-place style swapping), or waiting for a plugin to build a switcher on top of the experimental `chat.system.transform` hook. Worth revisiting this file periodically — if #5199 ships, or if oh-my-openagent/awesome-opencode add a style-switcher, this file will need a real update.

---

# Element 11: Background Task Tools

Scope: tools/plugins that let OpenCode dispatch and manage async
background work (subagent tasks, long-running shell processes) without
blocking the main session — either native OpenCode mechanisms or
plugins/frameworks with confirmed OpenCode support.

Context: OpenCode does **not** natively support true non-blocking
background subagent dispatch or background bash execution (Claude Code's
Ctrl+B equivalent) — this is tracked by multiple open feature requests
(see below). The plugin ecosystem has stepped in to fill this specific
gap, and it's one of the more mature "gap-filling plugin" categories in
this sweep, with several independent, actively-maintained implementations.

---

## Well-known / high-star

**[oh-my-openagent's Background Task System](https://github.com/code-yeongyu/oh-my-openagent)** — 67.3k stars (see Elements 5 & 8) — built-in background task manager (`BackgroundManager` + `ConcurrencyManager`) that launches multiple AI agent tasks simultaneously, each in an independent session, with three-level concurrency control (model > provider > default), live status tracking (`bg_<id>`, running/pending/completed states), and automatic notification on completion so the main session doesn't need to poll — enabled automatically under "ultrawork" mode or configurable individually — OpenCode support: **Native** (core subsystem of this OpenCode-native plugin, not a bolt-on). Caveat: a filed bug ([issue #3452](https://github.com/code-yeongyu/oh-my-openagent/issues/3452)) notes `opencode run` (headless/CI mode) can exit prematurely while background tasks are still active if no todos exist — worth checking before relying on it in CI.

## Actively maintained but smaller

**[opencode-background-agents (kdcokenny)](https://github.com/kdcokenny/opencode-background-agents)** — part of the "KDCO" plugin registry/ecosystem, installed via `ocx add kdco/background-agents` — async delegation plugin specifically designed to survive context compaction: background research/task results are persisted to disk as Markdown rather than kept only in the live context window, so a compaction event doesn't erase in-flight work; uses a "fire and forget, notify when ready" (waiter-service) model — OpenCode support: **Native** (installs directly as an OpenCode plugin under `.opencode/plugin/`; source is copyable manually if you don't want the `ocx` package manager dependency).

**[opencode-background-task (zeigarnick)](https://github.com/zeigarnick/opencode-background-task)** — MIT-licensed, lightweight standalone plugin exposing three agent-callable tools: `background_task` (launch async), `background_output` (poll/retrieve results by `task_id`), `background_cancel` (cancel one or all) — supports configurable concurrency limits, including per-provider and per-model caps — OpenCode support: **Native** (built directly against OpenCode's plugin system, installed via `.opencode/plugins/` + `opencode.json`'s `plugin` array).

**[opencode-background (zenobi-us)](https://github.com/zenobi-us/opencode-background)** — a different flavor: manages long-running **shell processes** (build watchers, test runners, dev servers) rather than agent subtasks — supports tagging (`["build","critical"]`), listing/filtering by tag, killing individual processes, and persisting global-scoped processes across sessions — OpenCode support: **Native** (configured directly in OpenCode's `config.json`, built specifically for OpenCode's process-management needs — this is the tool to reach for if your "background task" need is dev-server/build-pipeline management rather than agent delegation).

## Old or possibly abandoned

*(none identified as stale — every background-task plugin found is recent and tied to an active open feature-request thread, suggesting this is a currently-hot gap rather than a settled/abandoned one)*

---

## Related core feature / gap (not third-party, for context)

- **[Issue #5887](https://github.com/anomalyco/opencode/issues/5887)** — "[feat] True Async/Background Sub-Agent Delegation" — open request tracking the core capability gap; explicitly links to and consolidates several related asks.
- **[Issue #1970](https://github.com/anomalyco/opencode/issues/1970)** — "Add Background Bash Execution (Like Claude Code's Ctrl+b)" — open request for native non-blocking bash, described as a foundational requirement for true non-blocking subagent work.
- **[Issue #15069](https://github.com/anomalyco/opencode/issues/15069)** — "Async Task Management - Non-blocking Subagent Dispatch" — open request proposing intermediate solutions (fire-and-forget mode, background monitoring, or the current manual-session-management workaround) if full async support is too complex to ship at once.
- **[Issue #5826](https://github.com/anomalyco/opencode/issues/5826)** — "Agent Session Tab Bar Navigation" — related open request for UI to manage concurrent agent sessions.

None of these are merged as of this sweep — all four plugins above exist specifically because the native gap hasn't closed yet.

---

## Claude-Code-only, excluded

- **Claude Code's native Ctrl+B background bash execution** — the feature this entire element (and the OpenCode issues above) is modeled on/benchmarked against; no OpenCode-native equivalent shipped yet, only the third-party plugins above.
- **Claude Code's native `Task` tool for subagents** — referenced in kdcokenny's README as the thing its persistence layer is specifically compensating for (Claude's native task tool loses results on compaction, motivating the Markdown-persistence design) — this is Claude-Code's own mechanism, not something ported to OpenCode; the *plugin* is the OpenCode-facing artifact, not this note.

---

**Total found:** 4 usable (1 dominant framework-bundled system + 3 standalone plugins covering agent-tasks and shell-process management respectively) + 2 conceptually-excluded Claude Code native features (context only, not standalone resources).

**Summary:** Background task management is a genuine current gap in OpenCode core (tracked across at least 4 open feature-request issues), and the plugin ecosystem has responded with multiple independent, actively-maintained solutions rather than converging on one. oh-my-openagent's bundled system is the most feature-complete (concurrency tiers, auto-notify) if you're already using that framework; zeigarnick's and kdcokenny's plugins are good standalone options depending on whether you want simple polling (zeigarnick) or compaction-survival via disk persistence (kdcokenny); zenobi-us's tool solves a genuinely different problem (long-running dev processes, not agent subtasks) and is worth having alongside either of the others rather than instead of them.

---

# Element 12: Security-Review Tools

Scope: tools that scan code, PRs, or agent behavior itself for security
issues — either purpose-built for OpenCode or cross-tool tools with a
confirmed OpenCode path. Includes both "review my code for vulnerabilities"
tools and the newer category of "protect the agent session itself from
malicious tool calls / prompt injection."

Context: OpenCode has **no native security-review or vulnerability-
scanning feature** — this entire category is third-party. Two distinct
sub-categories emerged in this sweep: (1) traditional code/PR security
scanners adapted to run via an agent, and (2) a newer, OpenCode-specific
category of tools that guard the *agent session itself* against
prompt-injection and malicious tool calls (motivated by real supply-chain
incidents like the Postmark MCP backdoor).

---

## Well-known / high-star

**[Open Code Review (OCR)](https://github.com/alibaba/open-code-review)** — Alibaba-maintained, "battle-tested at Alibaba's scale" (star count not directly confirmed in results, but backed by a major-vendor org account) — hybrid architecture combining deterministic pipelines with an LLM agent for precise line-level review comments; built-in multi-language ruleset covering NPE, thread-safety, XSS, SQL injection; benchmarked at higher precision/F1 than general-purpose agents like Claude Code while using ~1/9 the tokens; ships both a CLI (`ocr review`, `ocr scan`) and an MCP server (`ocr_scan`, `ocr_heal`, `ocr_explain`) — OpenCode support: **Works via open standard** (the MCP server follows standard MCP, consumable by OpenCode's native MCP client like any other server; the CLI itself is agent-agnostic and provider-configurable rather than Claude-Code-specific).

## Actively maintained but smaller

**[opencode-security-agent](https://github.com/red-orbita/opencode-security-agent)** — purpose-built for OpenCode specifically — v2 is a **real-time defense plugin** using OpenCode's native `tool.execute.before` hook to block credential exfiltration, known-bad domains (hardcodes the domain from the real Postmark MCP backdoor incident), reverse shells, `curl|bash` pipes, and prompt-injection attempts *before* they execute — not just after-the-fact scanning; v1's static scanner (vulnerability-database scanning, source-integrity verification, coherence analysis) is still bundled; also ships a GitHub Action producing SARIF output that appears in the GitHub Security tab alongside CodeQL — OpenCode support: **Native** (built directly on OpenCode's plugin/hook system — this is the most OpenCode-specific tool found in this category, not a port from anywhere else).

**[security-reviewer agent (Opencode-Workflows)](https://github.com/IgorWarzocha/Opencode-Workflows/blob/master/agents/security-reviewer/README.md)** — part of a broader "Opencode-Workflows" example repo — a specialized OpenCode subagent for auditing AI-integrated codebases specifically (exposed API keys, insecure configs, framework-specific issues), with a skill-auto-selection mechanism that loads the relevant scanning skills based on detected tech stack — OpenCode support: **Native** (delivered as an OpenCode agent definition, using OpenCode's native agent + skill-loading conventions).

## Old or possibly abandoned

*(none identified as stale — this is an active, recently-motivated category, particularly the real-time defense sub-category which is a direct response to 2025-2026 supply-chain incidents)*

---

## Related context (not a resource, but relevant)

- The opencode-security-agent README cites a stat worth flagging directly: **36% of public skills reportedly contain security flaws** (per Snyk's "ToxicSkills 2025" report) — the stated motivation for this entire sub-category of "protect the agent from itself" tooling, distinct from traditional "review my application code" scanners.

---

## Claude-Code-only, excluded

- **open-code-review (spencermarx)** — despite the confusingly similar name to Alibaba's tool above, this is a *different*, unrelated project: "open-code-review is an open-source AI agents skill for AI coding assistants such as Claude Code, Codex CLI, and ChatGPT" (324 stars per SkillsLLM) — its own install instructions point at the Claude Code skills directory specifically; no OpenCode path confirmed. Do not confuse with `alibaba/open-code-review` above, which is a different tool despite the near-identical name.
- Various generic **"code-review-assistant" / "security-review" GitHub-topic results** (e.g. a centralized GitHub-PR review platform "built on Claude," several `claude-code-plugin`-tagged multi-agent consensus/review tools) — explicitly Claude-Code-plugin-tagged with no OpenCode adapter found.

---

**Total found:** 3 usable (1 well-known vendor tool + 2 smaller OpenCode-native) + 2 excluded (1 confusingly-similarly-named Claude-Code-only tool + generic Claude-Code-tagged results).

**Summary:** This category splits into two genuinely different needs: traditional code-vulnerability scanning (Alibaba's OCR is the strongest, vendor-backed, MCP-compatible option) and a newer, more urgent OpenCode-specific need — defending the agent session itself from malicious tool calls and prompt injection, motivated directly by real supply-chain attacks. opencode-security-agent is the standout here precisely because it's real-time (blocks *before* execution via OpenCode's native hook system) rather than a post-hoc scanner. Watch the naming collision: `alibaba/open-code-review` and `spencermarx/open-code-review` are unrelated projects with nearly identical names — only the former has a confirmed OpenCode path.

---

# Element 13: Headless / CI Setups

Scope: tools, guides, and configs for running OpenCode non-interactively —
in CI pipelines, GitHub Actions, or as a headless server — either native
OpenCode mechanisms or third-party wrappers/guides with a confirmed
OpenCode path.

Context: OpenCode has **substantial native headless/CI support** — this is
one of the strongest "native-first" categories in the sweep. Built-in
primitives include `opencode run` (one-shot prompts, `--format json` for
machine-readable output, `--auto` to auto-approve everything not denied),
`opencode serve`/`opencode web` (headless HTTP API server, optional basic
auth via `OPENCODE_SERVER_PASSWORD`), an official **GitHub App +
GitHub Actions integration** (`opencode github install`, `/opencode` or
`/oc` PR/issue-comment triggers), and an ACP (Agent Client Protocol)
stdin/stdout server mode for tooling integrations. That said, headless
mode has known rough edges — see the open bug noted below — which is why
third-party guides and shims exist.

---

## Well-known / high-star

**[opencode-primer](https://github.com/wesammustafa/opencode-primer)** (repo slug: `wesammustafa/OpenCode-Everything-You-Need-to-Know`) — comprehensive reference/guide repo covering setup, agents, skills, plugins, MCP, and **headless CI** as a dedicated section — documents the full one-shot/headless command surface (`opencode run`, `--format json`, `--auto` "CI only" flag, `--mini` lightweight mode from v1.17.10+, `opencode stats`, `opencode export --sanitize`) and links out to CI recipes for both GitHub Actions and GitLab CI — OpenCode support: **Native** (this is a documentation/reference repo for OpenCode's own native headless commands, not a separate tool — included here because it's the most complete single write-up of the surface found in this sweep, useful as a map of what's already built in).

## Actively maintained but smaller

**[opencode-shell-strategy](https://github.com/anomalyco/opencode/pull/5995)** (linked via an ecosystem-page PR; standalone repo referenced but not directly resolved in search) — an **instructions file** (not a plugin) teaching the LLM to avoid interactive shell commands that hang in OpenCode's non-TTY headless environment — covers safe flags for package managers (`npm init -y`, `apt-get install -y`, `pip install --no-input`), Git operations (`git commit -m` instead of opening an editor, `--no-edit` on merges), and a banned-commands list (editors like `vim`/`nano`, pagers like `less`/`more`/`man`) that would otherwise hang a headless run waiting for interactive input — OpenCode support: **Native** (distributed as an OpenCode-consumable instructions/AGENTS.md-style file, specifically targeting OpenCode's non-TTY CI behavior; PR shows it being added to the official OpenCode ecosystem/plugins listing page).

## Old or possibly abandoned

*(none identified — headless/CI tooling for OpenCode is actively being refined, evidenced by the open bug below being reported recently)*

---

## Related core feature (not third-party, for context)

- **`opencode run`** — one-shot, non-interactive prompt execution; `--format json`, `--continue`/`--session <id>`, `--fork`, `--share`, `--file <path>`, `--replay` (v1.16+), `--auto` (CI-only auto-approve), `--mini` (v1.17.10+ lightweight mode).
- **`opencode serve`/`opencode web`** — headless HTTP API server with optional basic auth (`OPENCODE_SERVER_PASSWORD`), full Web UI variant.
- **Official GitHub integration** (`opencode github install`, `opencode.ai/docs/github`) — installs a GitHub App and workflow file; supports `/opencode`/`/oc` mentions on issues, PRs, and inline PR-code comments; runs securely inside the repo's own GitHub Actions runners; configurable `model`, `agent`, `share`, `prompt`, and `token` workflow inputs.
- **ACP server mode** — Agent Client Protocol over stdin/stdout (ND-JSON), for deeper tooling integrations beyond simple CLI calls.

---

## Related open bug (not a resource, worth flagging for anyone building CI on this)

- **[Issue #28407](https://github.com/anomalyco/opencode/issues/28407)** — "opencode run returns Session not found in headless mode" (OpenCode v1.15.5, reported on Windows) — `opencode run` requires an existing session and doesn't reliably auto-create one in some headless/stdin-piped scenarios, breaking third-party tools that spawn `opencode run` with piped stdin (cited example: the Open Design adapter). Worth checking your OpenCode version and testing stdin-piped invocations before relying on this pattern in production CI.

---

## Claude-Code-only, excluded

- **Codex Exec / `codex exec`** (OpenAI's Codex CLI headless mode) — a different agent entirely (OpenAI Codex, not OpenCode); referenced only because it appeared in comparative CI-guide search results discussing headless coding-agent patterns generally. No OpenCode relevance beyond the comparison.

---

**Total found:** 2 usable (1 comprehensive native-feature guide + 1 small but genuinely useful instructions-file tool) + 1 flagged open bug + 1 excluded (different agent, comparison-only).

**Summary:** Unlike several earlier elements, this category is dominated by OpenCode's own native capabilities — one-shot `run`, headless `serve`/`web`, and official first-party GitHub Actions integration cover most CI needs without third-party tooling. The genuinely useful third-party additions are narrow and practical: opencode-primer as a documentation map of the native surface, and opencode-shell-strategy as a small but sharp fix for a real headless-mode failure mode (commands that hang waiting for interactive input in a non-TTY environment). The one thing worth watching before depending on `opencode run` in production CI is the open session-handling bug in piped-stdin scenarios.

---

# Element 14: Usage / Cost Tracking Tools

Scope: tools that track token usage and dollar cost of OpenCode sessions —
dashboards, CLIs, plugins, menu-bar apps. All entries here are OpenCode-
specific by nature (they parse OpenCode's own local session data), so the
OpenCode-support classification is uniformly high, but they vary in
mechanism (plugin vs. external log-reader).

Context: OpenCode stores session/usage data locally (SQLite database
and/or JSON export via `opencode export`), and exposes a native
`opencode stats --days N --models` CLI command for basic token/cost
breakdown by model. Every tool below either wraps/extends that native
command's data, or reads the underlying local database directly for
richer analysis.

---

## Well-known / high-star

*(No single tool has broken out to clear high-star dominance yet — this is
a crowded, fragmented category with many independent, similarly-scoped
entries, all quite recent. Listed below by relative feature depth instead.)*

## Actively maintained but smaller

**[ocsight](https://github.com/heyhuynhgiabuu/ocsight)** — the most feature-complete entry found: install via Homebrew/npm/direct binary; `ocsight summary`, `ocsight budget set --monthly <N>` with spending alerts, `ocsight live` real-time dashboard, session drill-down/browsing, pricing browser across 500+ models, multi-format export for reporting — OpenCode support: **Native** (built specifically to read OpenCode's local usage data; not a generic multi-tool tracker).

**[opencode-token-monitor](https://github.com/Ainsley0917/opencode-token-monitor)** — real-time OpenCode plugin (not just a log-reader) tracking input/output/reasoning/cache tokens live; agent×model and tool×command cost attribution; trend analysis with week-over-week comparison and cost-spike detection; ASCII terminal charts; configurable daily/weekly/monthly budget thresholds with toast notifications; exposes three agent-callable tools (`token_stats`, `token_history`, `token_export`) — OpenCode support: **Native** (installed directly via the `plugin` array in `opencode.json`; deepest integration of the group since it hooks live rather than reading exported data after the fact).

**[opencode-tokenscope / opencode-tokenscope-plugin](https://github.com/ramtinJ95/opencode-tokenscope)** (also mirrored at `pantheon-org/opencode-tokenscope-plugin`) — the most analytically deep entry: per-provider-step telemetry (fresh input vs. cache read/write vs. output vs. reasoning), cache hit-rate and effective-rate analysis, **recursive subagent cost rollup** (child-session usage/cost from Task-tool-spawned subagents), context-budget breakdown by system override/skills/subagents/tool schemas, and explicit uncertainty warnings when pricing/metadata is incomplete — supports 41+ models with cache-aware pricing — OpenCode support: **Native** (built against `@opencode-ai/plugin >=1.1.48`, version-pinned and explicitly verified against OpenCode v1.17.18).

**[opencode-usage (gaboe)](https://github.com/gaboe/opencode-usage)** — simple CLI (`bunx opencode-usage`) with daily/monthly breakdowns, provider breakdown (Anthropic/OpenAI/Google/etc.), and an optional web dashboard (`--commander` flag) — OpenCode support: **Native**.

**[opencode-stats (Cateds)](https://github.com/Cateds/opencode-stats)** — terminal dashboard reading OpenCode's local SQLite DB or JSON exports; tokens, cost estimates, model/provider distribution, 365-day activity heatmap, image/text share-card export; explicitly "Inspired by Claude Code's `/stats` command" as an independent OpenCode-native reimplementation — OpenCode support: **Native**.

**[opencode-dashboard (touchkale)](https://github.com/touchkale/opencode-dashboard)** — single-file, zero-dependency Python HTTP dashboard; auto-refreshing, session history, per-day token/message charts, cost-by-model, tool usage, work-hour heatmap, click-to-filter by day/tool/agent/model; ships a macOS `.command` launcher for a standalone app-window experience — OpenCode support: **Native**.

**[opencode-token-tracker (tongsh6)](https://github.com/tongsh6/opencode-token-tracker)** — real-time tracking plugin with a clean CLI summary view (today's usage, by-model breakdown) and a `trend` subcommand for cost/token charts over configurable day ranges and widths — OpenCode support: **Native**.

**[opencode-bar (opgginc)](https://github.com/opgginc/opencode-bar)** — macOS **menu-bar** app (different form factor from the rest — always-visible, not a CLI/terminal dashboard); tracks usage across multiple providers simultaneously with color-coded progress indicators, EOM cost prediction via weighted averages, per-provider subscription-plan configuration, and auth-source labeling (detects whether a token came from OpenCode, VS Code, or system Keychain) — OpenCode support: **Native** (one of several sources it tracks, alongside other tools' auth stores — worth choosing this one specifically if you want a persistent menu-bar view rather than an on-demand CLI check).

## Old or possibly abandoned

*(none identified as stale — this entire category is very recent, consistent with OpenCode's own `stats` command and local usage-data storage being relatively new)*

---

## Related core feature (not third-party, for context)

- **`opencode stats --days N --models`** — native CLI command for basic token/cost-by-model breakdown, the baseline every tool above extends.
- **`opencode export <id> --sanitize`** — native JSON session export (with redaction), one of the two raw-data sources these tools read (the other being direct SQLite access).

---

## Claude-Code-only, excluded

*(none identified — every usage/cost tool found in this sweep was purpose-built specifically against OpenCode's own local data format; no Claude-Code-only tracker with a stated-but-unconfirmed OpenCode claim surfaced)*

---

**Total found:** 8 usable (0 clear high-star leader, 8 smaller/active — genuinely fragmented) + 0 excluded.

**Summary:** This is the most crowded category in the sweep relative to feature overlap — at least 8 independent, actively-maintained tools solve overlapping "track my OpenCode spend" needs, none yet dominant. Depth varies meaningfully: ocsight and opencode-token-monitor are the most full-featured for budget-alerting/live-dashboard use cases; opencode-tokenscope is the standout for deep analytical needs (cache economics, recursive subagent cost attribution); opencode-bar is the only one offering a persistent menu-bar form factor rather than CLI/terminal/web. If you only want one, ocsight (broadest feature set: budgets, live monitoring, session drill-down, multi-format export) or opencode-token-monitor (deepest real-time plugin integration) are the strongest general-purpose picks; add opencode-tokenscope specifically if subagent cost attribution matters to you.

---

# Element 15: Agent-Team Frameworks

Scope: frameworks that coordinate multiple AI agents as a "team" (commander/
specialist patterns, swarms, hub-and-spoke orchestration) with a confirmed
OpenCode path — either OpenCode-native plugins or cross-tool orchestrators
that explicitly list OpenCode as a supported/adapted agent.

Context: OpenCode has no native multi-agent-team orchestration beyond its
own subagent system (Element 8) — true "team" frameworks (parallel
dispatch, inter-agent messaging, kanban-style task boards, cross-CLI
coordination) are entirely third-party. This category splits into two
shapes: (1) OpenCode-native plugins implementing a team pattern *inside* a
single OpenCode session, and (2) external cross-tool orchestrators that
treat OpenCode as one of several "worker" CLIs they can dispatch to
alongside Claude Code, Codex, etc.

---

## Well-known / high-star

**[Orkas](https://github.com/Orkas-AI/Orkas)** — open-source multi-agent desktop client (macOS/Windows/Linux); a "Commander" LLM decomposes goals and dispatches specialist sub-agents in parallel or series, with self-evolving agents (reflection + "skill crystallization") retaining private skills/memory across tasks; local-first (all data/keys stay on disk, model calls go direct to provider, never proxied); explicitly lists **OpenCode as one of the external CLI coding agents it can plug in and orchestrate**, alongside Claude Code, Codex, and Cline — OpenCode support: **Documented port/adapter** (OpenCode is named as a supported external CLI agent target in the project's own description, not merely "cross-tool" in the abstract).

**[opencode-swarm](https://github.com/ZaxbyHub/opencode-swarm)** — architect-centric agentic swarm **plugin for OpenCode itself** (not an external orchestrator) — turns a single OpenCode session into a hub-and-spoke team: one agent writes code, a different agent reviews it, another writes/runs tests, another checks security, with required gates that must pass before anything ships; installer auto-registers as an OpenCode plugin and disables the conflicting native explore/general agents; live roster viewable via `/swarm agents` — OpenCode support: **Native** (this is the deepest, most purpose-built entry in the category — built specifically as an OpenCode plugin, not adapted from elsewhere).

## Actively maintained but smaller

**[opencode-orca](https://github.com/ex-machina-co/opencode-orca)** — a different, smaller "Orca" project (not to be confused with the Orca/orca IDE below) — an OpenCode plugin implementing a Planner + Specialists team (Coder, Tester, Reviewer, Researcher, Document Writer, Architect) under a central "Orca" orchestrator, with per-agent supervision toggles configurable in `opencode.json` — OpenCode support: **Native** (purpose-built OpenCode plugin).

**[Orca (stablyai)](https://github.com/stablyai/orca)** — "AI Orchestrator for 100x builders" — an ADE (agent development environment, not a plugin) running Codex, Claude Code, **OpenCode**, or Pi side-by-side, each in its own git worktree, with a "fan one prompt across five agents, compare and merge the winner" workflow; desktop + mobile + VPS availability — OpenCode support: **Documented port/adapter** (OpenCode explicitly named as one of the four supported coding-agent backends).

**[Vibe Kanban](https://github.com/BloopAI/vibe-kanban)** (referenced via the Agent-Analytics curated list) — Apache-2.0 kanban workspace for planning, running, reviewing, and shipping parallel coding-agent work "across Claude Code, Codex, Gemini CLI, **OpenCode**, and related agents" — OpenCode support: **Documented port/adapter** (explicitly named support).

**[Agent Orchestrator (AgentWrapper / mirrored at Untrivial-ai)](https://github.com/AgentWrapper/agent-orchestrator)** — agent IDE managing fleets of coding agents (Claude Code, Codex, Cursor, Kimi Code, **opencode**, and others) sharing one workspace, with automatic CI-failure/review-comment/merge-conflict routing back to the right agent — OpenCode support: **Documented port/adapter** (OpenCode explicitly listed among supported terminal-based agents).

## Old or possibly abandoned

*(none identified — this whole category (cross-CLI agent-team orchestrators) is a very recent, fast-moving trend as of this sweep; nothing stale surfaced)*

---

## Related awareness (curated lists, not standalone tools)

- **[andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators)** — a curated meta-list of agent orchestrators (updated within the last week per search results); explicitly names several more OpenCode-compatible team/orchestration tools worth tracking as this space matures: **shire** ("persistent team workspaces with inter-agent mailboxes and a shared drive" — Claude Code, OpenCode, Pi), **tutti** (config-driven workflows passing typed artifacts between agents, each in its own worktree), and **opengoat** (organizations of agents coordinating across Codex, Claude Code, Cursor, and OpenCode). None of these were independently verified beyond this list's description in this sweep — flag as "claimed, worth a dedicated follow-up search" rather than fully confirmed here.
- **[Agent-Analytics/awesome-multi-agent-orchestrators](https://github.com/Agent-Analytics/awesome-multi-agent-orchestrators)** — a second, overlapping curated list; corroborates Orca and Vibe Kanban's OpenCode support independently.

---

## Claude-Code-only, excluded

- **OpenAI's Swarm** (`openai/swarm`, now superseded by the OpenAI Agents SDK) — an educational, model-agnostic orchestration framework operating purely at the API/function-calling level; no CLI-coding-agent integration of any kind (Claude Code or OpenCode), so it's excluded as out-of-scope for "CLI coding agent team" rather than as Claude-Code-only specifically — included here only to flag that it is NOT what "Swarm" branded tools in this space are referring to.
- **VRSEN/OpenSwarm** ("Agency Swarm") — built on top of an OpenCode-based terminal experience per its own credits, but its focus and framing is general multi-agent business/task automation ("Claude code for everything except coding"), not a coding-agent-team tool; no clear OpenCode-coding-workflow integration confirmed beyond using OpenCode's terminal shell as a base.
- **kyegomez/swarms** — enterprise multi-agent orchestration framework (60+ swarm structures, MCP/x402/A2A protocol support) but framed entirely around general agent workflows (research, financial analysis, business processes), not coding-agent-CLI teaming; no OpenCode-specific integration found.

---

**Total found:** 5 usable (2 well-known/high-visibility + 3 smaller/active) + 3 flagged-for-follow-up (from curated lists, unverified independently) + 3 excluded (different scope/no clear OpenCode integration).

**Summary:** Two genuinely different patterns exist here: opencode-swarm and opencode-orca are "team-inside-a-single-OpenCode-session" plugins (deepest OpenCode integration, since they're built as OpenCode plugins directly), while Orkas, stablyai's Orca, Vibe Kanban, and AgentWrapper's Agent Orchestrator are external cross-CLI orchestrators that treat OpenCode as one of several dispatchable backend agents (broader scope, shallower per-agent integration — typically just shelling out to `opencode run` or similar). If you want a self-contained multi-role review/build/test pipeline within OpenCode itself, opencode-swarm is the standout; if you want to run OpenCode alongside Claude Code/Codex/Cursor as parallel workers on the same goal, Orkas or Orca (stablyai) fit better.

---

# Element 16: Workflow Orchestration Tools

Scope: tools that define and run deterministic, multi-step, multi-agent
workflows (as distinct from Element 15's "team" framing and Element 8's
subagent framing) — pipelines, DAGs, triggers, and phase-gated processes
— either OpenCode-native plugins or cross-tool orchestrators with a
confirmed OpenCode path.

Context: OpenCode has no native workflow-DAG/pipeline engine beyond its
own agent/subagent primitives — this entire category is third-party. It
splits into three recognizable shapes: (1) OpenCode-native plugins adding
a real workflow engine inside OpenCode, (2) external local daemons/runners
that treat OpenCode as one of several dispatchable CLI backends, and
(3) example/starter-kit repos packaging opinionated workflow patterns as
OpenCode agent+command bundles rather than a generic engine.

---

## Well-known / high-star

**[Superpowers](https://github.com/obra/superpowers)** — by Jesse Vincent (obra); reported star counts vary by source/date across the sweep's search results (89K+ per one March 2026 writeup, 129K+ by April 2026, 224K+ by June 2026 per another source — the discrepancy likely reflects genuinely explosive, ongoing growth rather than conflicting facts) — not a workflow-orchestration tool in the DAG sense but a **mandatory-workflow discipline framework**: composable Markdown skills enforcing brainstorm → design → plan → TDD implementation → two-stage review as an auto-triggering, non-optional pipeline; subagent-driven development with fresh context per task — OpenCode support: **Native** (explicitly listed as one of Superpowers' supported harnesses — Claude Code, Codex CLI/App, Factory Droid, Gemini CLI, **OpenCode**, Cursor, GitHub Copilot CLI — though installation is harness-specific: "OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness," per ClaudePluginHub's listing). Covered in more depth under Element 18 (discipline/skill packs), where it more precisely belongs; flagged here because multiple sources describe it using workflow/pipeline language.

## Actively maintained but smaller

**[opencode-workflows (mark-hingston)](https://github.com/mark-hingston/opencode-workflows)** — the most "traditional workflow engine" entry found: a real deterministic pipeline plugin built on the Mastra workflow engine — JSON or type-safe TypeScript workflow definitions, step dependencies (`after:`), shell-command steps, event-based triggers (e.g. `file.change` with glob patterns, debounced 300ms to avoid rapid re-fires), and explicit support for orchestrating multiple AI agents in a deterministic pipeline — OpenCode support: **Native** (built specifically as an OpenCode plugin, workflows live under `.opencode/workflows/`).

**[Open Dynamic Workflow](https://github.com/travisliu/open-dynamic-workflow)** — local-first workflow *runner* orchestrating **external** coding-agent CLIs, explicitly including OpenCode alongside Codex, Gemini, Copilot, Antigravity, Pi, Cursor, and a deterministic mock provider for dry runs — supports `parallel()` fan-out + `agent()` fan-in summarization patterns, tool execution, child workflows, and goal-oriented loops; has explicit per-provider permission-flag mapping documented for OpenCode specifically (`dangerously-full-access` → `--dangerously-skip-permissions`) — OpenCode support: **Documented port/adapter** (OpenCode is one of several named, individually-mapped backend targets, with OpenCode-specific flag translation documented in the README).

**[Open Dynamic Workflows (OpenCode plugin variant)](https://github.com/awesome-opencode/awesome-opencode)** (listed entry, distinct companion project to the above per the awesome-opencode directory's description) — "brings Claude-Code-style dynamic workflows and ultracode to OpenCode": a local daemon runs a generated orchestration script with concurrent agents, adversarial verification, and crash-resume; the OpenCode plugin half adds `/workflow`/`/ultracode` trigger commands plus a planning UI inside OpenCode — OpenCode support: **Native** (the plugin component is built specifically for OpenCode; MIT-licensed, model-agnostic — Anthropic, any OpenAI-compatible endpoint, or local Ollama).

**[NERV](https://github.com/awesome-opencode/awesome-opencode)** (listed entry) — "invisible engineering infrastructure for AI agents": Spec-Driven Development pipeline, an A2A (agent-to-agent) task-delegation hub, persistent semantic memory (MAGI), and 9 specialized subagents for OpenCode; `nerv init` scaffolds 45+ files including SDD skills, slash commands, MCP servers, and lifecycle plugins — OpenCode support: **Native** (purpose-built OpenCode scaffold/framework).

**[opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)** — a starter kit (not a generic engine) packaging product-development workflows as OpenCode agents/commands, with optional adapters for Open Design, Superpowers, Impeccable, Docker, and token-usage plugins; explicitly favors "local, inspectable configuration over hosted orchestration services" and documents who it's for vs. not for (small teams wanting repeatable workflows vs. those wanting a hosted multi-agent platform with billing/dashboards) — OpenCode support: **Native** (core kit built specifically around and requiring OpenCode).

**[Opencode-Workflows (IgorWarzocha)](https://github.com/IgorWarzocha/Opencode-Workflows)** — "an ever evolving repository of OpenCode workflow examples... I only left the stuff that actually works" — includes the "Ralph Wiggum Loop" (`/loop`, a deliberately simple while-loop pushing a task subagent through repeated implementation+verification cycles until 100% complete), a plugin-creation workflow bundle, model-specific focused-mode prompt injectors, and an `openspec-orchestrator` for strict spec formatting/validation — OpenCode support: **Native** (all examples are OpenCode agent/command/plugin files, not ported from elsewhere).

**[opencode-orch-mode](https://github.com/agents-to-go/opencode-orch-mode)** — an orchestration workflow specifically designed to keep smaller/faster/"dumber" models on-plan: a structured collaborative-planning-then-execution loop with continuous review/QA, using two named agents (e.g. `@grok` as executor, `@glm` as reviewer) cycling through numbered implementation/review files (`01-code.md`, `02-review.md`, etc.) until done — OpenCode support: **Native** (installs as a slash command in OpenCode's global config plus companion subagent Markdown files).

## Old or possibly abandoned

*(none identified as stale — every workflow tool found is recent, several explicitly dated within the last few months of this sweep)*

---

## Related awareness (curated list mentions, unverified independently — flag for follow-up)

- Per **awesome-agent-orchestrators**: **tutti** ("config-driven workflows passing typed artifacts between agents, each in its own worktree") and **Dex** ("human-gated planning, multi-reviewer code review, dead-end-aware research loops, shipped as cross-platform binaries for 7 CLI backends") were both named as supporting OpenCode among their backends, but neither was independently verified beyond the list description in this sweep.

---

## Claude-Code-only, excluded

- Generic "Claude-Code-style dynamic workflows" framing appears in several tool descriptions (e.g., Open Dynamic Workflows plugin) as the *inspiration*, not as a separate excluded resource — no standalone Claude-Code-only workflow tool without an OpenCode path was found in this specific search pass (contrast with other elements where this section is more populated).

---

**Total found:** 7 usable (1 flagged cross-listed with Element 18 + 6 OpenCode-native/adapter tools) + 2 flagged-for-follow-up (curated-list-only) + 0 clearly excluded this round.

**Summary:** This category is dense and somewhat overlapping with Elements 8, 15, and 18 — the honest distinction is that Element 16 tools focus on deterministic step/trigger/pipeline definition (Mastra-based opencode-workflows is the clearest example of a "real" workflow engine), while Open Dynamic Workflow and its plugin companion target dynamic, LLM-generated orchestration scripts with adversarial verification. The starter-kit and example-repo entries (opencode-agent-orchestration-kit, Opencode-Workflows, opencode-orch-mode) are less "tools" than curated patterns — useful as a starting point to adapt rather than install-and-go. Superpowers is included here only because it's frequently described in workflow/pipeline language; it more properly belongs in Element 18.

---

# Element 17: Agent SDKs

Scope: SDKs and programmatic-access libraries for building on top of or
integrating with OpenCode — either OpenCode's own native SDK or third-party
libraries with a confirmed OpenCode integration.

Context: OpenCode has a **native, official JS/TS SDK** (`@opencode-ai/sdk`)
— a type-safe client for the OpenCode server, letting developers build
integrations and control OpenCode programmatically. Historically there was
a documented gap here (an open, now largely superseded, feature request
asking for exactly this — [Issue #4028](https://github.com/anomalyco/opencode/issues/4028),
"Inquiry: Programmatic access or Node.js SDK for OpenCode," filed
November 2025), which the official SDK has since addressed.

---

## Well-known / high-star

*(The dominant "resource" here is OpenCode's own official SDK, which is
native rather than a third-party star-counted repo — see below. No
third-party wrapper library has reached comparable visibility yet.)*

**OpenCode's official SDK** (`@opencode-ai/sdk`, docs at opencode.ai/docs/sdk) — type-safe JS/TS client for the OpenCode server; can create a fresh instance (auto-picking up `opencode.json` config, with inline overrides) or connect to an already-running instance via `createOpencodeClient`; full TypeScript definitions for all API types — OpenCode support: **Native** (this is OpenCode's own first-party SDK, the foundation every tool below is either built on or exists to complement).

## Actively maintained but smaller

**[ai-sdk-provider-opencode-sdk](https://github.com/ben-vargas/ai-sdk-provider-opencode-sdk)** — a Vercel AI SDK community provider that wraps OpenCode's SDK, letting developers call `generateText()` (and the rest of the Vercel AI SDK surface) against any model configured in OpenCode, auto-starting an OpenCode server if needed — supports full provider/model addressing (`anthropic/claude-sonnet-4-5-...`, `openai/gpt-5.3-codex-spark`, etc.) and custom settings (hostname, port, default agent, session title) — OpenCode support: **Native** (built directly on top of `@opencode-ai/sdk`, not a port from another tool — this is the standout entry for developers who want OpenCode's configured-provider access inside standard Vercel AI SDK code rather than calling OpenCode's SDK directly).

**[opencode-mcp (Traves-Theberge)](https://github.com/Traves-Theberge/opencode-mcp)** and **[opencode-mcp (AlaeddineMessadi)](https://github.com/AlaeddineMessadi/opencode-mcp)** — covered in full under Element 6 (MCP servers); both bridge external MCP clients into OpenCode's headless/server API, functioning as an alternate, protocol-level "SDK" for driving OpenCode from outside — OpenCode support: **Native** (built directly against OpenCode's headless server API — cross-referenced here rather than duplicated in full).

**OpenAgentsControl / opencode-agent-orchestration-kit / NERV** and similar frameworks (see Elements 15 & 16) are *built on* OpenCode's native agent/plugin system rather than exposing a separate SDK surface — mentioned here only to clarify they are not "SDKs" in the programmatic-API sense this element targets, despite sometimes being described that way informally.

## Old or possibly abandoned

*(none identified — OpenCode's SDK is recent, and the one confirmed third-party wrapper found is actively maintained)*

---

## Related core feature / history (not third-party, for context)

- **[Issue #4028](https://github.com/anomalyco/opencode/issues/4028)** — the original community request for programmatic/Node.js access to OpenCode, filed November 2025; the official `@opencode-ai/sdk` release (referenced in current docs) is the resolution to this gap.
- **OpenCode's headless server mode** (`opencode serve`, `opencode web`) is the runtime surface the SDK talks to — see Element 13 (headless/CI) for the CLI-level detail; this element covers the *programmatic client* layer on top of that server.
- **ACP (Agent Client Protocol) server mode** — a stdin/stdout ND-JSON protocol server, an alternative lower-level integration surface to the JS/TS SDK, aimed at deeper tooling integrations (per OpenCode's CLI reference).

---

## Claude-Code-only, excluded

- **OpenAI Agents SDK** (successor to `openai/swarm`) — a general-purpose agent-building SDK for OpenAI's own models/API; no CLI-coding-agent integration (Claude Code or OpenCode) of any kind — excluded as out-of-scope rather than Claude-Code-specific, included here only to flag it's unrelated to this element's actual scope despite surface-level "agent SDK" name overlap.

---

**Total found:** 2 usable (1 native official SDK + 1 third-party wrapper) + 2 cross-referenced entries (already fully covered under Element 6) + 1 out-of-scope note.

**Summary:** This is a fairly settled, native-first category — OpenCode ships its own official, documented, type-safe JS/TS SDK, resolving what was an open community request as recently as November 2025. The one genuinely notable third-party addition is ben-vargas's Vercel AI SDK provider, useful specifically if your codebase already standardizes on the Vercel AI SDK interface and you want OpenCode's configured-provider access without learning OpenCode's own SDK surface directly. The MCP-bridge tools from Element 6 also function as an alternate "SDK-like" integration path and are worth considering alongside the JS/TS SDK depending on whether your integration language is JS/TS or something MCP-protocol-based instead.

---

# Element 18: Discipline/Skill Packs (Superpowers/ponytail-style)

Scope: comprehensive methodology/discipline frameworks — auto-triggering
skill collections that enforce a structured engineering process (TDD,
brainstorm→plan→execute→review, systematic debugging) rather than single
one-off skills — with confirmed OpenCode support.

Context: This is a genuine cross-tool phenomenon, not an OpenCode-specific
feature. The dominant framework, Superpowers, is explicitly designed to be
harness-agnostic (Markdown skill files any instruction-following model can
execute) and has been ported to/supports OpenCode as one of its
first-class harnesses, alongside Claude Code, Codex CLI/App, Cursor,
Gemini CLI, Factory Droid, and GitHub Copilot CLI.

---

## Well-known / high-star

**[Superpowers](https://github.com/obra/superpowers)** — by Jesse Vincent (obra) — star counts reported across sources in this sweep show explosive, ongoing growth (89K+ as of one March 2026 writeup, 129,443 by April 2026, 224,691 by June 2026 per a later source) — an agentic skills framework and software-development methodology enforcing a mandatory (non-optional, auto-triggering) pipeline: clarify → design → plan → red/green TDD implementation → two-stage review (spec compliance, then code quality), plus systematic-debugging (4-phase root-cause process) and subagent-driven-development with fresh context per task. Distributed through Anthropic's official Claude plugin marketplace and, separately, seven other harnesses. Skills are self-enforcing: the flagship `writing-skills` skill explicitly designs against agent rationalization under pressure ("agents are smart and will find loopholes... write skill before testing? Delete it. Start over.") — OpenCode support: **Native** (explicitly listed as one of Superpowers' supported harnesses; per ClaudePluginHub's own listing: "OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness" — meaning the OpenCode installation path is real and distinct, not a generic fallback).

## Actively maintained but smaller

**[opencode-power-pack](https://github.com/waybarrios/opencode-power-pack)** — 45 (README also cites 55 in places, likely reflecting recent additions) rigorous skills for Codex, OpenCode, and Pi: code review, security audit, feature development, frontend design, MCP tools, Hugging Face ML/training workflows, and more; explicitly positioned as **complementary to Superpowers** ("It complements obra/superpowers, which provides process skills such as brainstorming, TDD, debugging, and plan execution") rather than a competing discipline framework — ships immutable provenance tracking for every upstream-adapted skill, registers feature-development specialist roles as least-privilege, read-only OpenCode subagents, and lets Codex run the same phase assignments via its own native subagent workflow — OpenCode support: **Native** (adapted specifically for OpenCode as one of three named target harnesses, with OpenCode-specific subagent registration, not a blind cross-post).

**[science-superpowers](https://github.com/K-Dense-AI/science-superpowers)** — a domain reimplementation of Superpowers for computational science rather than software engineering: same auto-triggering-skill architecture, but the central discipline is **pre-registration** (turning a fuzzy research interest into a precise, falsifiable question before running any code) instead of TDD — includes `framing-research-questions` and `surveying-prior-work` skills — OpenCode support: **Claimed but unverified** (the repo's own install docs explicitly detail Pi and Antigravity installation paths in depth, but do not clearly confirm a dedicated OpenCode install path in the material surfaced by this search — flagged rather than assumed; worth a direct repo check before relying on it for OpenCode specifically).

## Old or possibly abandoned

*(none — this is one of the fastest-growing categories in the entire sweep, with Superpowers itself being among the most-starred agent-tooling repos found in this entire research project)*

---

## Related context (not a resource, for framing)

- Superpowers' own installation guidance underscores that "discipline pack" support across harnesses is **not automatically shared** — even a user already running Superpowers under Claude Code must separately install it for OpenCode, since OpenCode uses its own native plugin mechanism rather than a shared cross-harness install path. This matters operationally: don't assume "supports 8 harnesses" means one install covers all of them.

---

## Claude-Code-only, excluded

*(none clearly identified in this specific search pass — unlike several other elements, the flagship tool here (Superpowers) was explicitly designed multi-harness from a relatively early stage, so this search didn't surface a "same thing but Claude-Code-only" counterpart the way some other elements did. Worth a dedicated follow-up sweep if a more exhaustive list of Claude-Code-only discipline packs is wanted.)*

---

**Total found:** 3 usable (1 dominant/very-high-star + 1 smaller complementary pack + 1 claimed-unverified) + 0 excluded this pass.

**Summary:** Superpowers is the clear category leader by a wide margin — one of the most-starred agent-tooling projects surfaced anywhere in this entire sweep — and its OpenCode support is confirmed as a genuine, distinct native install path rather than an afterthought. opencode-power-pack is a strong complementary addition (not a competitor) covering domain-specific skills (security audit, frontend design, ML/Hugging Face workflows) that Superpowers' process-discipline focus doesn't include. science-superpowers is worth knowing about if your work is research/data-science rather than software engineering, but its OpenCode path specifically should be verified directly before relying on it, since this search couldn't confirm it as cleanly as Pi/Antigravity.

---

# Element 19: Docs-Context MCP Servers (Context7-style)

Scope: MCP servers that fetch current, version-specific library/API
documentation into an agent's context (solving the "training data is
stale" problem) — with confirmed OpenCode support.

Context: Same structural situation as Element 6 — this is an open MCP
standard category, and OpenCode's native MCP client (local + remote,
configured under `opencode.json`'s `mcp` key) means virtually every server
in this space works with OpenCode "for free," no porting needed. This
element exists as a focused sub-list of Element 6 specifically for the
"live docs lookup" use case, since it's common and frequently asked about
on its own.

---

## Well-known / high-star

**[Context7](https://github.com/upstash/context7)** — 39.3k+ stars (see Element 6) — the originator of this category: indexes community-contributed library documentation, served via MCP; triggered with "use context7" or an explicit library slash-ID (`/supabase/supabase`) in the prompt to skip library-matching — OpenCode support: **Works via open standard** (plain MCP server; add the hosted endpoint `https://mcp.context7.com/mcp` with an `Authorization: Bearer` API key, or self-host, under OpenCode's `mcp` config like any other server).

**[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** — explicitly positioned as an "Open-Source Alternative to Context7, Nia, and Ref.Tools" — builds a personal, always-current documentation index by fetching official docs from websites, GitHub, npm, PyPI, and local files; auto-probes for `llms.txt` at doc subpaths/site roots and prefers Markdown-native responses (via `Accept: text/markdown` content negotiation, including Cloudflare's Markdown-for-Agents support) over scraping HTML — OpenCode support: **Works via open standard** (long-running MCP endpoint, documented for Claude/Cline/Copilot/Gemini CLI/"other MCP clients" generically — OpenCode consumes it the same way any MCP client does).

## Actively maintained but smaller

**[DeepWiki](https://deepwiki.com)** (by Cognition/Devin team) — different shape than pure docs lookup: turns any public GitHub repo into an AI-enhanced wiki with automated documentation, architecture diagrams, and interactive Q&A; exposes three MCP tools querying any public repo's auto-generated wiki on the fly — free for public repos — OpenCode support: **Works via open standard** (plain MCP server; useful specifically for "how does this codebase work internally" rather than "what's the current API surface," complementing rather than replacing Context7-style tools).

**[Docfork](https://github.com/topics/mcp-server)** (per multiple comparison roundups) — MIT-licensed, open-source; claims 9,000+ libraries covered out of the box with automatic detection/download of docs, and a `dgrep init` flow that reads your `package.json` once and scopes documentation search to your actual dependencies ("Cabinets" for versioning) — OpenCode support: **Works via open standard** (plain MCP server per every comparison source found; widest claimed library coverage of the alternatives surveyed).

**[Ref Tools](https://ref.tools)** — closed-API, paid after a 200-credit free tier (~10 weeks average usage); differentiator is aggressive token efficiency — caps responses around 5K tokens using session-history awareness to stay lean under context pressure — OpenCode support: **Works via open standard** (MCP server; worth choosing specifically if context-window budget is the binding constraint, per its comparison-roundup positioning).

**[Rtfmbro](https://mcp.directory/collections/top-alternatives-to-context7-mcp)** — fetches version-aware documentation "just in time" directly from a package's GitHub repo, rather than Context7's pre-scan/index approach — OpenCode support: **Works via open standard** (plain MCP server per comparison sources).

**[GitMCP](https://gitmcp.io)** and **[grep.app-backed "Grep" MCP](https://mcp.directory/collections/top-alternatives-to-context7-mcp)** — GitMCP provides direct GitHub API access to code/docs for any project; Grep searches across millions of GitHub repos via the grep.app API with language/repo/path filtering — OpenCode support: **Works via open standard** for both.

**[Nia](https://trynia.ai)** — Y Combinator-backed (raised $6.2M), indexes docs and codebases together, claims a 27% coding-agent performance improvement via "intelligent indexing and context sharing" (self-reported, not independently verified in this sweep) — OpenCode support: **Works via open standard**.

**[Deepcon](https://mcp.directory/blog/top-context7-mcp-alternatives)** — differentiates on accuracy: cites a self-reported 90% score on a contextual benchmark vs. 65% for Context7 and 0% for unaugmented Claude Sonnet 4.5 (self-reported benchmark, not independently verified) — OpenCode support: **Works via open standard**.

## Old or possibly abandoned

*(none identified — this is an actively growing category with new entrants as recently as this sweep's search results)*

---

## Claude-Code-only, excluded

*(none identified — consistent with Element 6, this open-MCP-standard category has no genuinely Claude-Code-exclusive entries; every server surveyed across multiple independent comparison roundups is plain MCP, consumable by any MCP client including OpenCode)*

---

**Total found:** 8 usable (2 well-known/high-visibility + 6 smaller/differentiated) + 0 excluded.

**Summary:** As with Element 6, the "does this support OpenCode" question is largely moot for this entire category — every docs-context MCP server surveyed across five independent comparison articles is a standard MCP server, which OpenCode consumes natively. The genuinely useful differentiation is *not* OpenCode-compatibility but which server fits your specific need: Context7 for broad, established library coverage; docs-mcp-server or Docfork if you want the most current/widest indexing with strong open-source credentials; DeepWiki when you need to understand an unfamiliar codebase's architecture rather than just its public API; Ref Tools if context-window budget is your binding constraint. Several performance/coverage claims (Nia's 27%, Deepcon's 90% vs 65%) are self-reported by the vendors and were not independently verified in this sweep.

---

# Element 20: Statusline Tools

Scope: tools that add a customizable, persistent status display for
OpenCode (model, git branch, token usage, cost, session state) — either
native OpenCode mechanisms or workaround tools, since OpenCode currently
has no built-in customizable statusline.

Context: **OpenCode has no native customizable statusline** — this is a
confirmed, actively-tracked gap, not a search miss. Claude Code's
statusLine feature (pipe session-state JSON to a shell script after each
message; script's stdout becomes the status bar) has **no OpenCode
equivalent** as of this sweep. Multiple open feature requests exist
(below), and third-party tools have built workarounds ranging from TUI-
adjacent daemons to full external processes, since OpenCode's built-in
status bar is rendered in SolidJS with no plugin hook to modify it.

---

## Well-known / high-star

*(No single statusline tool has broken out to clear high-star dominance —
this is a workaround category filling a confirmed gap, populated by
several small, differently-scoped tools rather than one dominant winner.
Listed by approach/maturity instead.)*

## Actively maintained but smaller

**[ocstatusline](https://github.com/amirlehmam/ocstatusline)** — explicitly "the OpenCode counterpart of ccstatusline" (the popular Claude Code statusline tool) — since OpenCode has no status-line hook, external-command slot, or pluggable built-in bar, this tool **inverts the model**: runs as a separate live daemon (`ocstatusline start`) that repaints instantly as your session produces tokens, switches model, or changes cost, meant to run alongside OpenCode in a separate pane/split rather than being injected into OpenCode's own TUI — reuses ~70% of ccstatusline's widget engine/Powerline/color/flex-width/config-TUI concepts; rich widget set: model, provider, agent/mode, token totals, cost, context length/%, context bar, session timer, git branch/dirty/ahead-behind/changes/SHA, working dir, custom text — OpenCode support: **Native** (purpose-built specifically as OpenCode's counterpart to an existing Claude Code tool; not itself an OpenCode plugin, but a companion process designed around OpenCode's actual architecture and limitations — the README states this workaround exists precisely *because* "OpenCode has no equivalent" to Claude Code's statusLine hook).

**[opencode-status-line (markwilkening21)](https://github.com/markwilkening21/opencode-status-line)** — "inspired by cc-status-line" — a lightweight, fast standalone binary that connects to OpenCode's HTTP server (`--url`, required — "OpenCode does not expose an HTTP server by default, you need to start OpenCode with an explicit port"), themeable (built-in themes like Catppuccin or custom theme files), terminal-multiplexer-aware (tmux, zellij, wezterm), configurable refresh interval, PR status display (toggleable) — designed to run in a split pane (tmux/wezterm binding examples provided) — OpenCode support: **Native** (connects directly to OpenCode's own server API, purpose-built for OpenCode specifically, not adapted from elsewhere).

**[opencode-status-bar (aacassandra)](https://github.com/aacassandra/opencode-status-bar)** — a different form factor: a tiny **macOS menu bar app** (not a terminal pane) showing OpenCode's live status at a glance — "no windows, no dock icon, no analytics, just a pixel in your menu bar"; supports multiple concurrent OpenCode sessions with priority surfacing (a session awaiting permission jumps above one that's just thinking); architecture is stateless/event-driven: an OpenCode plugin (`plugin/statusbar.ts`) writes JSON state files on lifecycle events, and a separate Swift app polls and renders them (0.4s interval) — OpenCode support: **Native** (the plugin half is a real OpenCode plugin using OpenCode's lifecycle events; the Swift app is a companion renderer, together forming a complete native-to-OpenCode pipeline).

## Old or possibly abandoned

*(none identified as stale — all three tools found are recent, consistent with this being an actively-requested but still-unfilled native gap)*

---

## Related open feature requests / gap (not third-party, for context)

- **[Issue #30295](https://github.com/anomalyco/opencode/issues/30295)** — "Feature: Custom statusLine via shell script (like Claude Code)" — explicitly requests the Claude Code pattern (pipe session-state JSON to a script, script's stdout becomes the status bar); shows as **Closed** in search results with a "needs:compliance... auto-close after 2 hours" label — worth checking current status directly, as this may indicate process-closure rather than resolution.
- **[Issue #23539](https://github.com/anomalyco/opencode/issues/23539)** — "Plugin API for custom status bar widgets" — a broader, still-open consolidating request proposing plugins be allowed to register custom TUI status-bar widgets generally (use cases cited: terminal pets, pomodoro timers, build/test status indicators); explicitly references and consolidates two earlier related asks (#8619 `ui.statusLine` hook, #18969 `ui.footer` hook).
- **[Issue #8619](https://github.com/anomalyco/opencode/issues/8619)** — "Native StatusLine Hook for Plugins (Context-Free Display)" — the original ask; explicitly cites Claude Code's statusLine docs as the parity target and links a plugin (`opencode-breadcrumb`) demonstrating the current workaround limitation (must inject text into message parts, which is the wrong mechanism for persistent status).

---

## Claude-Code-only, excluded

- **ccstatusline** (`b-open-io/statusline`, 12.1k★ per SkillsLLM) — the Claude Code tool ocstatusline is explicitly modeled after; Claude-Code-specific (`CLAUDE_CONFIG_DIR` env var, receives Claude Code's JSON via stdin) with no OpenCode installation path — the *inspiration* for this element's OpenCode-native tools, not itself usable with OpenCode.

---

**Total found:** 3 usable (0 dominant high-star + 3 smaller/active, covering three distinct form factors) + 1 excluded (direct inspiration, Claude-Code-only).

**Summary:** This is a confirmed native gap (three open/recently-closed feature-request threads track it) rather than a search miss — OpenCode's TUI status bar is currently not customizable or pluggable. The three tools found solve it via three different form factors rather than converging on one approach: ocstatusline (separate live daemon in a terminal pane, closest in spirit to ccstatusline), opencode-status-line (standalone themed binary connecting via OpenCode's HTTP server), and opencode-status-bar (macOS menu-bar app driven by a real OpenCode plugin). Pick based on where you want the status visible — terminal split, standalone pane, or system menu bar — rather than by feature completeness, since none is a strict superset of the others.

---

# Element 21: Git-Worktree Helpers

Scope: tools that automate git-worktree-based parallel-agent workflows —
creating, syncing, and tearing down isolated worktrees for OpenCode
sessions — either OpenCode-native plugins or cross-tool helpers with a
confirmed OpenCode path.

Context: OpenCode has **no native worktree-automation feature** — git
worktrees work with OpenCode simply because OpenCode is a normal CLI tool
that runs fine inside any git worktree (no special integration needed for
the base case: `git worktree add ../feat-x -b feat/x && cd ../feat-x &&
opencode`). This entire element is therefore about *automation on top of*
that manual pattern — reducing the friction of create/navigate/launch/sync/
teardown across many parallel worktrees. There is one confirmed open
feature request asking OpenCode to build this in natively (below).

---

## Well-known / high-star

*(No single OpenCode-specific worktree helper has broken out to high-star
status yet — this is a fragmented space of small, focused tools, several
explicitly cross-tool rather than OpenCode-only. Listed by relevance/depth
instead.)*

## Actively maintained but smaller

**[opencode-worktree](https://skillsllm.com/skill/opencode-worktree)** — the most OpenCode-specific entry found: an OpenCode plugin that creates isolated git worktrees where **each worktree automatically opens its own terminal with OpenCode already running inside it** — exposes `worktree_create` (auto-spawns terminal, starts OpenCode, syncs files) and `worktree_delete` (auto-commits changes, cleans up the worktree) as agent-callable tools/lifecycle hooks; explicitly notes it works in OpenCode Desktop too, but loses automatic terminal-spawning there (GUI-locked); pairs with a separate tool called "cmux" for agentic workflows — OpenCode support: **Native** (purpose-built OpenCode plugin, not adapted from another tool; the standout entry specifically because it automates the full create→terminal→launch→sync→teardown lifecycle rather than just worktree creation).

**[git-worktree-runner (CodeRabbit)](https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents)** — cross-tool CLI (`git gtr new my-feature --ai`) explicitly supporting Claude, Cursor, **Opencode**, Copilot, and Gemini — OpenCode support: **Documented port/adapter** (OpenCode explicitly named among supported agents in the tool's own command surface, per the independent Upsun technical writeup).

**[agentree](https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents)** — quick worktree creation for AI workflows generally (`agentree -b fix-auth`) — agent-agnostic rather than OpenCode-specific; no explicit per-agent adapter confirmed, but nothing in its design prevents `cd`-ing into the created worktree and launching OpenCode manually — OpenCode support: **Claimed but unverified** (works via the general git-worktree pattern any CLI agent benefits from, but no OpenCode-specific integration point or documentation confirming special OpenCode awareness was found — flagged rather than assumed equivalent to git-worktree-runner's explicit support).

**[worktree-cli](https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents)** — targets AI workflows with MCP server integration, automatic setup hooks, and `.env` file copying, but per the source writeup is described as MCP-integrated **specifically for Claude Code** — OpenCode support: **Claimed but unverified** (no explicit OpenCode adapter found; MCP integration described is Claude-Code-specific per the source, so treat OpenCode compatibility as unconfirmed rather than assumed via the general MCP-openness argument used elsewhere in this sweep, since the *setup hooks* themselves may be Claude-Code-specific rather than protocol-level).

**[gwq](https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents)** — status-dashboard tool showing all active worktrees across repositories, with tmux integration for managing long-running agent processes — agent-agnostic (works with whatever CLI agent you point it at, OpenCode included, since it operates at the worktree/tmux layer rather than the agent layer) — OpenCode support: **Works via open standard** in the loose sense of "operates below the agent layer" — not a protocol-based claim like MCP, but genuinely agent-agnostic by design rather than requiring per-agent adapters.

## Old or possibly abandoned

*(none identified as stale — every tool found is from recent writeups/repos, consistent with git-worktree-for-parallel-agents being a 2025-2026-era pattern)*

---

## Related open feature request (not third-party, for context)

- **[Issue #12896](https://github.com/anomalyco/opencode/issues/12896)** — "[FEATURE] Parallel Workflow Support via Git Worktrees and Tabbed Sessions" — open request asking for exactly what opencode-worktree currently provides as a plugin: "a tool for opencode that automates the creation of a new session in a fresh Git worktree," ensuring isolated filesystem/git state per agent. Not yet natively shipped as of this sweep.

---

## Related context (not a resource, for framing)

- Git worktrees are widely documented as **the** dominant isolation pattern for running multiple coding-agent sessions (any agent, not just OpenCode) in parallel without file-level conflicts, since they share a single `.git` object store while giving each session its own working directory and index — this is general git functionality, not something requiring OpenCode-specific support to use at the basic level. OpenCode-specific *helpers* only add value on top of that baseline by automating the setup/teardown ceremony.

---

## Claude-Code-only, excluded

*(none clearly identified as Claude-Code-only-with-no-OpenCode-path in this search pass — most tools found are either explicitly cross-tool/agent-agnostic, or (in worktree-cli's case) flagged as claimed-but-unverified rather than confirmed excluded, since the underlying git-worktree pattern itself has no inherent Claude-Code dependency)*

---

**Total found:** 5 usable (1 OpenCode-native standout + 4 cross-tool, with confidence varying from "documented" to "claimed-unverified") + 1 open feature request (native gap tracker) + 0 clearly excluded.

**Summary:** The baseline capability — running OpenCode inside a manually-created git worktree — needs no special tooling at all and is well-documented as working cleanly (OpenCode is "just" a CLI that runs fine anywhere). The genuine value-add tools automate the ceremony around that: opencode-worktree is the clear standout for being purpose-built as a real OpenCode plugin with a full create→launch→sync→teardown lifecycle, while git-worktree-runner is the strongest cross-tool option with OpenCode explicitly named as supported. agentree, worktree-cli, and gwq are more general-purpose and their OpenCode-specific support level varies from "should just work via the general pattern" to "unconfirmed" — worth testing directly before relying on the Claude-Code-specific hook/setup features some of them advertise.

---

# Element 22: Awesome-Lists (AI Coding Agents, Cross-Tool)

Scope: curated meta-lists covering AI coding agent tooling across multiple
harnesses (not single-tool lists), with confirmed OpenCode coverage —
either as a dedicated section/tag or as a consistently-included harness
across entries.

Context: This element is about the *lists themselves* as resources (meta-
level), distinct from the individual tools they catalog (already covered
throughout Elements 1-21). Note also that awesome-opencode (Element 9,
8.5k★) is the dedicated single-tool OpenCode list, not a cross-tool one —
it belongs primarily there; this element covers lists spanning multiple
harnesses where OpenCode is one of several covered.

---

## Well-known / high-star

**[jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code)** — a Claude-Code-centric list, but many individual cataloged entries explicitly support/target OpenCode alongside Claude Code (e.g., claude-replay 720★ converts sessions from "Claude Code, Cursor, Codex, Gemini, OpenCode"; agentsys 878★ is an "automation toolkit... for Claude Code, OpenCode, Codex, Cursor, and Kiro"; medusa 643★ is a cross-agent security scanner) — OpenCode support: **Mixed per-entry** (the list itself is Claude-Code-branded, but functions as a de facto cross-tool discovery list since a meaningful fraction of entries explicitly support OpenCode — treat as "Documented port/adapter" for the specific entries that name OpenCode, not for the list as a whole).

**[hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins)** — explicitly framed as "for AI assistants including Claude Code, OpenAI Codex, Gemini, OpenCode and More" in its own title/description — genuinely cross-tool by design, not just by incidental entry overlap; catalogs plugins like Workflow Kit ("for Claude Code, Codex CLI, and OpenCode") and Claude Octopus (dispatches to 8 providers including OpenCode) — OpenCode support: **Works via open standard / documented per-entry** (the list's own framing includes OpenCode as a first-class target, not an afterthought).

**[gmh5225/awesome-skills](https://github.com/gmh5225/awesome-skills)** — cross-tool skills/resources list "for AI coding agents like Claude Code, Codex, Gemini CLI, GitHub Copilot, and more" — catalogs OpenCode-inclusive tools like skillreaper (session-transcript analysis for "Claude Code, Codex, Hermes, OpenCode, Cursor, and OpenClaw") and Skills宝 (a marketplace explicitly "across Claude Code, OpenCode, and more platforms") — OpenCode support: **Documented per-entry** (genuinely multi-harness list with OpenCode represented, though not as prominently as Claude Code).

## Actively maintained but smaller

**[bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents)** — explicitly scoped as "terminal-native AI coding agents and the harnesses that orchestrate them," listing OpenCode by name as one of the covered open-source tools alongside Pi, Aider, and Goose, plus platform agents (Claude Code, Codex, Gemini CLI); catalogs OpenCode-inclusive orchestration tools like Garcon (steers parallel sessions across "Claude Code, Codex, Cursor Agent, OpenCode, Amp, Droid, and Pi") and Agent AFK — OpenCode support: **Works via open standard / documented per-entry** (OpenCode named directly in the list's own scope description, not just in individual entries).

**[RoggeOhta/awesome-codex-cli](https://github.com/RoggeOhta/awesome-codex-cli)** — Codex-CLI-centric (150+ tools primarily for OpenAI Codex), but a meaningful minority of entries explicitly include OpenCode as a supported target — e.g., sync-agents-settings ("Sync MCP server configs from Claude Code to Gemini CLI, Codex CLI, OpenCode, Kiro, Cursor"), mco-org/mco ("Neutral orchestration layer for Claude Code, Codex CLI, Gemini CLI, OpenCode, Qwen Code") — OpenCode support: **Mixed per-entry** (same pattern as the Claude-Code-centric list above: the list itself isn't OpenCode-focused, but usefully surfaces OpenCode-compatible cross-tool entries you might otherwise miss by only searching OpenCode-specific lists).

## Old or possibly abandoned

*(none identified as stale — all lists found show recent update timestamps, consistent with this being an actively-curated space)*

---

## Related context (not a resource, for framing)

- This element inherently overlaps with material already covered by name throughout Elements 1-21 (medusa appears again in Element 23, cc-safety-net-style tools in Element 24, security-review tools in Element 12, etc.) — its distinct value is as a **discovery/maintenance mechanism**: these lists are where new OpenCode-compatible tools in any category will likely surface first, before a dedicated sweep like this one catches up. Worth bookmarking rather than treating as a one-time reference.

---

## Claude-Code-only, excluded

*(not applicable in the usual sense for this element — since these are curated meta-lists rather than individual tools, "excluding" a whole list would discard genuinely useful cross-references even where the list's primary branding is Claude-Code-centric; instead, treat every list here as a discovery source and apply the standard OpenCode-support filter to each individual entry as you encounter it, same as any other element)*

---

**Total found:** 5 usable curated lists (3 well-known/high-visibility + 2 smaller/actively-maintained), all functioning as legitimate OpenCode-tool-discovery sources despite varying primary branding.

**Summary:** No single "the" cross-tool awesome-list dominates the way awesome-opencode dominates the single-tool space (Element 9) — instead, several lists nominally branded around Claude Code or Codex CLI turn out to be genuinely useful OpenCode-discovery sources because so many modern agent tools are built cross-harness from the start. hashgraph-online/awesome-ai-plugins and bradAGI/awesome-cli-coding-agents are the two most explicitly OpenCode-inclusive by their own framing (not just incidental entry overlap); the Claude-Code-centric and Codex-CLI-centric lists (jqueryscript, RoggeOhta) are worth checking specifically for their OpenCode-tagged entries rather than dismissed as out-of-scope, since a real minority of their catalogued tools do explicitly support OpenCode.

---

# Element 23: Security Scanners for Agent Configs

Scope: tools that scan an agent's own configuration (skills, hooks,
plugins, permissions files) for malicious or vulnerable content before
installation/execution — distinct from Element 12 (code/PR security
review), this is specifically about vetting the *agent tooling supply
chain* itself.

Context: This is a rapidly growing category directly motivated by real
2025-2026 supply-chain incidents (the Postmark MCP backdoor, referenced
also in Element 12; Snyk's "ToxicSkills 2025" finding that a meaningful
percentage of published skills contain security flaws; Koi's ClawHavoc
investigation finding hundreds of malicious skills using stealer droppers,
password-protected archives, and reverse shells). OpenCode has no native
config-scanning feature — this entire category is third-party.

---

## Well-known / high-star

**[MEDUSA](https://github.com/Pantheon-Security/medusa)** — AI-first security scanner with 40,000+ detection patterns (star counts vary by mirror/fork found: 643★ per one listing, a separate fork "medusa1" cites 74+ analyzers/180+ AI-agent rules) — zero-setup, works out of the box; `medusa scan --git <URL>` vets any repo for AI supply-chain attacks (repo poisoning, prompt injection, MCP tool poisoning) before you clone; `medusa secrets scan` finds leaked API keys across "Claude / Cursor / Copilot / shell history" with 21 issuer types and interactive in-place redaction; v2026.7 added "Claude Code compromise detection" that explicitly vets **`.claude/` directory hooks, permissions, and skills** for injected instructions and backdoors — OpenCode support: **Claimed but unverified** (the specific "compromise detection" feature is documented as targeting the `.claude/` directory by name; no equivalent `.opencode/` directory scanning was confirmed in the material surfaced by this search, despite MEDUSA's broader scanning — general code/secrets/CVE scanning likely applies to any codebase including OpenCode projects, but the specific agent-config-directory vetting feature that makes this element distinct does not have confirmed OpenCode-directory coverage — flag for direct verification before relying on this specifically for `.opencode/` vetting).

## Actively maintained but smaller

**[secure-skills (alonw0)](https://github.com/alonw0/secure-skills)** — "The SECURE open agent skills tool," a fork/variant published as `npx skillsio` — explicitly states "Supports OpenCode, Claude Code, Codex, Cursor, and 37 more" in its own description; runs an automated local security scan **before** any skill install (`skillsio add` triggers the scan automatically) rather than after-the-fact; applies ~81 regex rules plus a correlation engine derived directly from the Snyk ToxicSkills and Koi ClawHavoc research, organized into 8 threat categories — OpenCode support: **Native** (OpenCode explicitly named first in its own supported-agents list, and the tool operates at the skill-installation layer generically rather than being tied to any one agent's specific config-directory format — this is the standout entry specifically because OpenCode support is stated outright, not inferred).

## Old or possibly abandoned

*(none identified as stale — every tool here is recent, directly tracking recent supply-chain incidents as they were disclosed)*

---

## Related context (not a resource, for framing)

- The motivating statistics cited across this category are worth carrying forward as context for why it matters: Snyk's "ToxicSkills 2025" analysis of 3,984 published skills found 13.4% had critical security issues and 76 were confirmed malicious; Koi's ClawHavoc investigation separately uncovered 341 malicious skills using techniques including AMOS stealer droppers, password-protected archives, base64-encoded payloads, macOS quarantine bypasses (`xattr -c`), and reverse shells.
- Compare with **opencode-security-agent** (Element 12) — that tool's *real-time defense* approach (blocking malicious tool calls at execution time via `tool.execute.before`) is complementary to this element's *pre-install scanning* approach; using both together (scan before install, guard during execution) is defense-in-depth rather than redundant.

---

## Claude-Code-only, excluded

*(none clearly identified as flatly Claude-Code-only-with-zero-OpenCode-path in this search pass — MEDUSA is flagged as claimed-but-unverified for its specific `.opencode/`-directory feature rather than excluded outright, since its broader scanning capabilities are agent-agnostic even if the flagship compromise-detection feature's directory targeting wasn't confirmed for OpenCode specifically)*

---

**Total found:** 2 usable (1 claimed-but-unverified for the specific agent-config feature + 1 confirmed-native) + 0 clearly excluded.

**Summary:** This category is thin but important, and the two entries found split cleanly: MEDUSA is the more comprehensive, higher-profile scanner (40,000+ patterns, CVE detection, secrets scanning) but its flagship agent-config-directory vetting feature is documented specifically for `.claude/` — worth a direct check with the maintainers or repo before assuming `.opencode/` gets the same treatment. secure-skills is narrower in scope (skill-installation-time scanning specifically) but explicitly and confidently states OpenCode support as one of its named target agents. If you want config-directory-specific vetting today with confirmed OpenCode support, secure-skills is the safer choice; if you want the broadest possible security-scanning coverage and are willing to verify OpenCode-specific claims yourself, MEDUSA's non-agent-specific features (git-repo vetting, secrets scanning, CVE detection) still apply regardless of which agent you use.

---

# Element 24: Safety-Net / Guardrail Tools

Scope: tools that intercept and block destructive or dangerous agent
actions (destructive git/filesystem commands, credential exposure) before
execution — distinct from Element 23 (pre-install config scanning) and
Element 12 (code security review), this is real-time action-level
protection during a live session.

Context: OpenCode has **native, partial** guardrail support via its
built-in permission system (allow/ask/deny rules — see Element 2) and a
`tool.execute.before` plugin hook that third-party tools use to build
deeper protection. However, native permission rules are pattern-based and
don't always distinguish *safe* from *destructive* variants of the same
command family (e.g., `git checkout -b feature` vs. `git checkout --
file`) — this is exactly the gap the tools below fill. There's also a
documented real-world incident motivating this category directly: **Issue
#17949** (OpenCode deleted a user's Downloads folder without confirmation)
led directly to **Issue #17953**, an open request for native destructive-
file-operation guardrails.

---

## Well-known / high-star

**[CC Safety Net (kenryu42/cc-safety-net)](https://github.com/kenryu42/cc-safety-net)** — the most comprehensive entry found: a coding-agent CLI hook catching destructive git/filesystem commands and secret-file access **before** they execute, working by *intent* rather than string-pattern matching — explicitly distinguishes `git checkout -b feature` (safe, allowed) from `git checkout -- file` (destructive, blocked); also catches `rm -rf` on destructive targets, `git reset --hard`, `git push --force`, `git stash clear`, `git clean -f`, `find -delete`, and `dd`/`mkfs`/`shred`; cross-platform (Windows/macOS/Linux) with OS-aware path/command handling — supports **ten** coding-agent CLIs: Claude Code, Codex, Gemini CLI, Copilot CLI, Antigravity CLI, Kimi Code, **OpenCode**, Pi, Cursor, and Amp Code — OpenCode support: **Native** (installs via `opencode plugin -g -f cc-safety-net@latest`, i.e. OpenCode's own native plugin command; the README documents a known OpenCode-specific caching quirk — stale cached plugin versions, tracked at [anomalyco/opencode#25293](https://github.com/anomalyco/opencode/issues/25293) — with a documented workaround of clearing `~/.cache/opencode/packages/`). Explicitly recommended as **defense-in-depth alongside sandboxing** (Element 7), not a replacement: "Sandboxing contains blast radius... Safety Net prevents footguns... catches git-specific mistakes that are technically 'safe' from the sandbox's perspective."

*(Note: an earlier/renamed version of this same tool appears at [kenryu42/claude-code-safety-net](https://github.com/kenryu42/claude-code-safety-net) — same author, overlapping description, listing five supported agents including OpenCode rather than the newer repo's ten. Treat as the same lineage; use `cc-safety-net` as the current canonical repo per its more complete, more recently-dated documentation.)*

## Actively maintained but smaller

**[Destructive Command Guard (dcg) — OpenCode integration](https://gist.github.com/AlexMikhalev/bc7cc0f237bdb2a6fade347aba203acb)** — a documented integration pattern (published as a gist/blog post, not a standalone repo) showing how to wire the `dcg` tool into OpenCode using its native `tool.execute.before`/`tool.execute.after` plugin hooks (available since OpenCode v1.4+) — intercepts commands before they run, catching the same class of AI-agent mistakes (a mistyped `rm -rf ./src`, an accidental `git reset --hard`, an unintended `git push --force`) — OpenCode support: **Native** (built directly against OpenCode's documented plugin `Hooks` interface; this is an integration guide rather than a packaged plugin, so implementation requires following the gist rather than a one-line install).

**[OpenGuardrails](https://openguardrails.com/)** — "the open standard & benchmark for AI agent safety & security" — a broader policy-based approach rather than a fixed destructive-command blocklist: the agent fetches and reads a skill (`openguardrails.com/skill/SKILL.md`), drafts a policy describing what it may/may not do, the operator approves it, and OGR then enforces that policy on every subsequent action including the agent's own — explicitly invocable by pasting an install prompt into "Claude Code, Codex, **opencode**, OpenClaw…" — OpenCode support: **Works via open standard** (delivered as a skill/instructions file the agent reads and self-applies, rather than a hook-based plugin — a fundamentally different, more agent-agnostic mechanism than CC Safety Net's hook interception, and explicitly OpenCode-inclusive in its own onboarding instructions).

## Old or possibly abandoned

*(none identified as stale — every tool here is recent and actively tracks or responds to recent real-world incidents)*

---

## Related core feature / gap (not third-party, for context)

- **OpenCode's native permission system** (`allow`/`ask`/`deny` rules, per-agent overrides — see Element 2 for full detail) — the baseline mechanism; `ask` rules pause and offer "Allow Once" / "Allow Always" / deny choices, and `deny` blocks outright. This is coarser-grained than the intent-aware distinction CC Safety Net makes (e.g., a blanket `git checkout` ask/deny rule can't distinguish the safe branch-creation form from the destructive file-discard form without a smarter guard on top).
- **[Issue #17949](https://github.com/anomalyco/opencode/issues/17949)** — the real-world incident: OpenCode deleted a user's Downloads folder without confirmation.
- **[Issue #17953](https://github.com/anomalyco/opencode/issues/17953)** — "[Security] Add destructive file operation guardrails with user confirmation" — open feature request filed directly in response to #17949, proposing native confirmation guardrails for destructive file operations. Not yet shipped as of this sweep — the third-party tools above exist specifically to fill this gap in the meantime.

---

## Claude-Code-only, excluded

- **[evil-opencode (winmin)](https://github.com/winmin/evil-opencode)** — the *inverse* of this element's scope: a fork of OpenCode with **safety guardrails deliberately removed** from the system prompts, telemetry stripped, framed as "Unleashed" with the model no longer refusing requests on ethics/safety grounds. Included here only as a flagged anti-pattern, explicitly **not** a resource to recommend — its existence is worth being aware of (e.g., if evaluating unfamiliar OpenCode forks) but it is the opposite of a safety-net/guardrail tool and should not be confused with the legitimate tools above.

---

**Total found:** 3 usable (1 comprehensive/well-known hook-based tool + 1 documented integration pattern + 1 policy-based agent-agnostic tool) + 1 flagged anti-pattern (not a real exclusion in the usual sense, but worth naming explicitly) + 2 related native-gap issues for context.

**Summary:** This category is well-served for OpenCode specifically, anchored by CC Safety Net — genuinely comprehensive (ten supported agent CLIs, intent-based rather than pattern-based detection, actively maintained with a documented OpenCode-specific caching quirk and workaround) and explicitly positioned as defense-in-depth alongside sandboxing (Element 7) rather than competing with it. The `dcg` integration and OpenGuardrails offer two different mechanisms worth knowing about: `dcg` via direct hook interception (more precise, requires manual wiring), OpenGuardrails via a self-drafted, operator-approved policy (more flexible, agent-agnostic by design). All three exist specifically because OpenCode's native permission system, while functional, doesn't yet make the safe/destructive distinction these tools do — tracked by an open feature request filed after a real data-loss incident.

---

# Element 25: Hook Management CLIs

Scope: tools that discover, install, enable/disable, and diagnose hooks
across coding-agent CLIs — distinct from Element 5 (hook *collections/
frameworks* themselves), this element is about the *management tooling*
layer on top of hooks.

Context: OpenCode's native plugin/hook system (Element 5) has **no native
enable/disable management surface** — this is a confirmed gap. There's an
open, unmerged feature request specifically for this ([Issue #11743](https://github.com/anomalyco/opencode/issues/11743)),
motivated by a real pain point: heavier plugins like oh-my-openagent can
meaningfully increase token consumption, and users currently have no quick
way to temporarily disable a plugin without manually editing config files
or fully uninstalling it. Separately, OpenCode does not natively support
Claude Code's specific hooks *format* (PreToolUse/PostToolUse/Stop) — see
the related issue below — which is a format-compatibility gap distinct
from the enable/disable-management gap this element centers on.

---

## Well-known / high-star

*(No dedicated, high-star, standalone hook-management CLI specifically for
OpenCode was found — this is a genuinely thin category, consistent with
the native gap it addresses being recent and still open.)*

## Actively maintained but smaller

**[hook-manager (bopen-tools)](https://www.claudepluginhub.com/skills/b-open-io-bopen-tools-2/hook-manager)** — the clearest fit found: "Discovers and installs automation hooks for Claude Code and Opencode, including security hooks, git reminders, and linting triggers"; manages hooks via natural-language commands — add, list, remove, update, validate — for lifecycle events like `PreToolUse`, `SessionStart`, `UserPromptSubmit`; ships a curated hook catalog (e.g., `protect-env-files` — blocks Write/Edit on `.env*` files, recommended universally as a zero-downside security safeguard; `auto-git-add`; `uncommitted-reminder`; `lint-on-save`/`lint-on-start`) — explicitly documents parallel install paths for both agents (`ls ~/.claude/hooks/` vs. `ls ~/.opencode/hooks/`), and its own instructions literally say "restart Claude Code (or Opencode) for the hook to take effect" — OpenCode support: **Native** (built with explicit, symmetric dual-agent support, not a Claude-Code tool with an incidental OpenCode mention — this is a skill/tool delivered via the bopen-tools collection specifically designed to manage hooks across both harnesses).

## Old or possibly abandoned

*(not applicable — too thin a category to assess for staleness; the one entry found is recent)*

---

## Related open gaps / feature requests (not third-party, for context)

- **[Issue #11743](https://github.com/anomalyco/opencode/issues/11743)** — "Feature Request: CLI Support for Plugin Enable/Disable" — the core native gap this element addresses; proposes a `disabled_plugins: string[]` config array so heavy plugins (cited example: oh-my-openagent's token overhead) can be temporarily toggled off without editing config files or fully uninstalling. Filed with a contributor volunteering to submit a PR; status as of this sweep shows it filed but not confirmed merged.
- **[Issue #12472](https://github.com/anomalyco/opencode/issues/12472)** — "Native Claude Code hooks compatibility (PreToolUse, PostToolUse, Stop)" — a related but distinct gap: OpenCode already has strong Claude Code compatibility for rules (`CLAUDE.md`) and skills (`~/.claude/skills/`), toggleable via `OPENCODE_DISABLE_CLAUDE_CODE_*` env vars, but Claude Code's specific **hooks format** (JSON-over-stdin, exit-code-2-blocks-with-stderr-feedback protocol) is not natively supported — the issue proposes a detailed mapping (`PreToolUse` → `tool.execute.before`, `PostToolUse` → `tool.execute.after`, `Stop` → `session.idle` with transcript re-injection on exit code 2) and a matching `OPENCODE_DISABLE_CLAUDE_CODE_HOOKS=1` toggle for consistency with the existing pattern. Not yet natively shipped as of this sweep — this is the underlying gap that Element 5's "Opencode Hooks Plugin" and oh-my-openagent's bundled compatibility layer currently fill via third-party translation.
- **[Issue #1473](https://github.com/anomalyco/opencode/issues/1473)** — the original "Hooks support?" request (filed July 2025, now closed) — historical context showing hooks support itself was, at one point, entirely absent before the current plugin/event-hook system existed.

---

## Claude-Code-only, excluded

*(none clearly identified as a standalone Claude-Code-only hook-management CLI in this specific search — general git-hook managers like `fivestars/git-hooks` and GitHub Copilot's own `hooks.json` system surfaced in adjacent searches but are unrelated tools for different products, not excluded OpenCode-adjacent candidates)*

---

**Total found:** 1 usable (hook-manager) + 0 clearly excluded + 3 related native-gap issues for context.

**Summary:** This is a genuinely thin category — the one dedicated hook-management tool found (hook-manager from bopen-tools) does explicitly and symmetrically support both Claude Code and OpenCode, which is good news given how few options exist. The more important finding is the *why*: OpenCode currently lacks native plugin/hook enable-disable management (tracked, unresolved, in issue #11743) and native support for Claude Code's specific hooks JSON/exit-code protocol (tracked, unresolved, in issue #12472) — the latter gap is what makes Element 5's translation-layer tools (Opencode Hooks Plugin, oh-my-openagent's bundled compatibility) necessary in the first place. If your actual need is "toggle a heavy plugin off temporarily to save tokens," there's currently no clean native or third-party solution beyond manually editing `opencode.json` — worth watching #11743 for resolution.

---

# Element 26: Self-Improving / Instinct-Mining Tools

Scope: tools that let a coding agent learn from its own past sessions —
mining errors, recoveries, and successful "golden paths" into reusable
skills/rules/prompts that improve future performance — with confirmed
OpenCode support.

Context: OpenCode has no native self-improvement or session-mining
mechanism — this entire category is third-party, and it splits into two
genuinely different technical approaches: (1) tools that harvest patterns
from a session's transcript/outcomes and write them into a durable
skill/rule file (the "AGENTS.md as repository memory" pattern), and
(2) more ambitious research-grade frameworks that treat skill/prompt
mutation as an optimization problem, evaluating variants against held-out
data across full benchmark suites.

---

## Well-known / high-star

**[EvoSkill](https://github.com/sentient-agi/EvoSkill)** — the most substantial, research-backed entry found: an open-source framework that automatically discovers and synthesizes reusable agent skills from **failed trajectories** to improve coding-agent performance; explicitly extends the feedback-driven idea from GEPA (a single-file prompt-optimization technique) to full agent evolution — proposes multiple skill *and* prompt mutations jointly, evaluates new variants against held-out data, and produces an entirely new agent program each iteration rather than revising one prompt in place; includes "Harbor," a containerized-benchmark component for evaluation — compatible with Claude Code, Codex CLI, **OpenCode**, OpenHands, Goose, and more; model-agnostic (OpenRouter, Anthropic, OpenAI, Fireworks, and others) — OpenCode support: **Native** (the installer explicitly offers `--agents claude,opencode`-style harness selection, `brew install opencode` is listed as a first-class supported install path alongside Claude Code/Codex/Goose, and its own config format shows `name = "opencode"` as a valid `[harness]` value alongside `openhands` — this is a confirmed, first-class, non-incidental integration, not a generic "should work" claim).

## Actively maintained but smaller

**[self-learning-skills (Kulaxyz)](https://github.com/Kulaxyz/self-learning-skills)** — a lighter-weight, more targeted tool: "recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time" — distributed via the community "skills CLI" (`npx skills add kulaxyz/self-learning-skills`), which **auto-detects installed agents** and installs accordingly, explicitly naming "Claude Code, Cursor, Codex, Cline, **OpenCode**, and more" as detectable targets; also installable via a Claude-Code-style plugin marketplace command as an alternative path — OpenCode support: **Native** (OpenCode explicitly named among the CLI's auto-detected target agents, not merely implied by "and more").

**[self-improving-agent (leohuang8688)](https://github.com/leohuang8688/self-improving-agent)** — a more full-featured learning system, but built specifically as an **OpenClaw skill** (a different agent, not OpenCode) — features error learning (learns from mistakes to avoid repetition), recovery learning (learns successful recovery patterns), session learning, performance-metrics learning, and an extensible hook system with a Python CLI (`learn-errors`, `learn-recoveries`, export-to-markdown) — genuinely feature-rich, but its install path is `~/.openclaw/workspace/skills`, an OpenClaw-specific directory — OpenCode support: **Claimed but unverified** (no OpenCode-specific install path, config, or documentation confirming OpenCode compatibility was found; flagged rather than assumed compatible despite the generically-named repo — this may be portable in principle given it's Python-CLI-based rather than deeply OpenClaw-hook-dependent, but that portability is not demonstrated in the material found).

## Old or possibly abandoned

*(none identified as stale — every tool found is recent, consistent with this being an emerging research-adjacent category)*

---

## Related context (not a resource, for framing)

- The broader academic/research space around this pattern is active and directly relevant even though the papers themselves aren't OpenCode tools: "Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation" (arXiv) frames structured mistake abstraction as "a critical lever for robust agent evolution... without the cost of parameter updates" — the same "training-free, context-based learning" philosophy EvoSkill and self-learning-skills operationalize as installable tools. Reflexion (Shinn et al., NeurIPS 2023) and "A self-improving coding agent" (Robeyns et al., 2025) are cited as foundational prior work in this space.
- A practical, non-tool version of this same idea — using `AGENTS.md` as durable repository memory so agents stop repeating the same corrections — is described in a January 2026 blog writeup ("How to build self-improving coding agents"), useful context for understanding the manual baseline these tools automate.
- The GitHub topic pages `self-improving` and `self-learning-agents` surfaced several more entries loosely relevant to this space (a Gemini-CLI+OpenCode local planner/reviewer/session-loop tool with "self learning architecture" was specifically OpenCode-tagged, but wasn't independently verified beyond the topic-page description in this sweep — flag for follow-up if deeper coverage of this specific niche is wanted).

---

## Claude-Code-only, excluded

*(none clearly identified as flatly Claude-Code-only-with-zero-OpenCode-path — the one entry with unclear OpenCode support, self-improving-agent, is built for a third agent (OpenClaw) rather than Claude Code specifically, so it's flagged as claimed-but-unverified rather than excluded as Claude-Code-only)*

---

**Total found:** 2 usable (1 substantial research-backed framework + 1 lighter targeted tool) + 1 flagged claimed-but-unverified (built for a different agent, OpenClaw) + 1 note on adjacent unverified topic-page result.

**Summary:** This is a small but genuinely interesting category, closing out the sweep on a research-forward note. EvoSkill is the standout — a real optimization framework (not just a heuristic pattern-harvester) with confirmed, first-class OpenCode support baked into its installer and config format. self-learning-skills is a good lighter-weight complement if you want the simpler "harvest one golden path per session" pattern without EvoSkill's full evaluation/mutation machinery. Watch for more entrants here — the underlying research (Mistake Notebook Learning, Reflexion-style approaches) is active, and "training-free agent adaptation via context/skill mutation" is clearly trending toward more installable tooling.

---

Element #1: Skills (SKILL.md repos/collections)
Filter applied: only resources that actually support OpenCode — native, documented adapter/port, or open cross-tool standard (SKILL.md / AGENTS.md / MCP) that OpenCode is known to read. Every entry below states exactly how.
Background fact that governs most of this list: OpenCode has native, first-party skill support. It discovers SKILL.md files from .opencode/skills/, ~/.config/opencode/skills/, and — critically — also natively walks and reads .claude/skills/*/SKILL.md and .agents/skills/*/SKILL.md (project and global). This means most "Claude Code skill" repos are already OpenCode-compatible out of the box, with zero adapter needed, as long as they're plain SKILL.md folders (no Claude-Code-only commands/hooks/agents bundled in). Source: https://opencode.ai/docs/skills/
Well-known / high-star
affaan-m/ECC ("Everything Claude Code") — 211.9k+ stars, 32.5k+ forks, 230+ contributors, actively maintained (2,300 commits, v2.0.0 shipped June 2026, weekly releases) — a full agent-harness operating system: 67 agents, 279 skills, hooks, rules, memory persistence, and the AgentShield security scanner, spanning 12+ language ecosystems — OpenCode support: Documented port/adapter exists — repo ships a dedicated .opencode/ directory described in the README as "Full plugin support in .opencode/," with its own OpenCode Support doc section, alongside similar first-class adapters for Cursor, Codex, Zed, and GitHub Copilot
obra/superpowers — 267.8k stars, forks 23.9k, actively maintained (680 commits, releases through May 2026, repo pushed same-day as of June 2026) — a full agentic-development methodology (brainstorming → plan → TDD → subagent-driven execution) built as composable skills — OpenCode support: Documented port/adapter exists — repo ships a dedicated .opencode/ directory with an INSTALL.md and its own OpenCode-specific plugin install flow (Fetch and follow instructions from .../obra/superpowers/refs/heads/main/.opencode/INSTALL.md), separate from the Claude Code plugin-marketplace install
anthropics/skills — 149k stars, forks 17.6k, active (recent commits, 41 total) — Anthropic's official public repo of demonstration Agent Skills (docx, pdf, pptx, xlsx, algorithmic-art, canvas-design, mcp-builder, webapp-testing, skill-creator, etc.) plus the Agent Skills spec/template — OpenCode support: Open standard (plain SKILL.md folders; OpenCode natively reads this exact layout via its .claude/skills-compatible discovery path; no Claude-Code-specific commands/hooks are required to use the skills themselves)
VoltAgent/awesome-agent-skills — 29.4k stars, forks 3.2k, active (424 commits, "Last Update" badge current) — hand-picked (non-AI-slop) collection of 1,497+ official Agent Skills from real engineering teams (Anthropic, Stripe, Cloudflare, Vercel, Sentry, Hugging Face, Microsoft, OpenAI, Figma, HashiCorp, and dozens more), each a real SKILL.md package, not just links — OpenCode support: Open standard — README explicitly states "Compatible with Claude Code, Codex, Antigravity, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf, and more"; skills are plain SKILL.md packages OpenCode discovers natively
alirezarezvani/claude-skills — 23.3k stars, forks 3.2k, active (1,286 commits) — 345+ skills/362 packaged skills across 18 domains (engineering, marketing, product, compliance, full C-suite advisory, academic research, finance) plus 102 agents and personas — OpenCode support: Documented port/adapter exists — ships a dedicated conversion script, ./scripts/install.sh --tool opencode --target ., that writes every skill into .opencode/skills/ in OpenCode's native format; FAQ explicitly confirms "Skills work natively with 13 tools ... OpenCode"
anthropics/knowledge-work-plugins — 21.3k stars, forks 2.5k, active — Anthropic's official open-source library of 11-15 role-based plugins (sales, legal, finance, product, HR, data, engineering, etc.) built as pure Markdown + JSON — OpenCode support: Open standard (partial) — each plugin's skills/ subfolder is a plain SKILL.md package OpenCode can discover if placed under .claude/skills or .opencode/skills; the plugin's commands/ slash-commands and .claude-plugin/plugin.json manifest are Claude-Code/Cowork-specific and do not carry over
Actively maintained but smaller
waybarrios/opencode-power-pack — 449 stars, forks 38, active (13 commits, recent) — ports 11 Claude-Code-only plugin workflows (code-review, security-review, feature-dev + 3 sub-agents, frontend-design, mcp-builder, skill-creator, agents-md-improver/revise) into pure OpenCode-native SKILL.md + slash-command form, specifically because the commands/agents parts of those Anthropic plugins are Claude-Code-only and don't translate on their own — OpenCode support: Native (built specifically for and tested against OpenCode; installs as an OpenCode plugin via opencode.json)
joshuadavidthomas/opencode-agent-skills — ~225 stars, forks 25, active (recent commits, changelog current) — an OpenCode plugin that adds dynamic skill discovery, context injection that survives compaction, and semantic skill-matching on top of skills; now in "maintenance mode" since OpenCode shipped native skill support — OpenCode support: Native (an OpenCode-specific plugin; explicitly built for and only runs in OpenCode)
farmage/opencode-skills — ~99 stars, forks 19, active — a fork/port of Jeffallan's Claude Skills collection (66 specialized skills + 9 workflow commands covering frameworks, DevOps, architecture, and specialized domains like Salesforce/Shopify/MCP dev), converted to OpenCode's native skill and command system — OpenCode support: Native (README: "Converted to work natively with OpenCode skill and command system"; installs via a one-line curl script, discovered through OpenCode's built-in skill tool)
joshuadavidthomas/agent-skills — star count not confirmed (smaller/newer companion repo), active (recent updates) — a standalone collection of actual skills (e.g. reducing-entropy for design-level code review, sub-agent coordination for codebase Q&A) meant to be symlinked into ~/.config/opencode/skills — OpenCode support: Native (README gives OpenCode-specific install commands and states OpenCode v1.0.190+ has native skill loading built in)
Old or possibly abandoned
None found in this pass — every OpenCode-relevant skills resource surfaced is currently maintained (commits within the last few months as of this sweep). No stale/abandoned OpenCode-compatible skill repos identified.
Claude-Code-only, excluded
anthropics/claude-code (the main Claude Code CLI repo itself — 140k+ stars, largest Anthropic repo) — bundles official plugins (code-review, feature-dev, frontend-design, PR-review agents, commit workflows) via .claude-plugin/marketplace.json; these mix skills/ with Claude-Code-only commands/ and agents/ formats and are installed through the Claude Code plugin system with no documented OpenCode path — noted here since it's "the" Claude Code repo, but excluded from the usable list as a whole.
jeremylongshore/claude-code-plugins-plus-skills ("Tons of Skills," 2.6k stars, 471 plugins / 3,179 skills / 347 agents) — README explicitly states "Built for Claude Code. Every plugin and skill in this catalog targets Anthropic's official CLI"; no OpenCode install path documented anywhere in the repo.
glebis/claude-skills — README states outright: "Skills require Claude Code to function; they are not standalone tools."
Notion Skills for Claude (linked from anthropics/skills "Partner Skills" section, hosted on notion.so) — delivered as a Claude/Claude.ai-specific workspace guide, no documented filesystem SKILL.md distribution or OpenCode install path found.
OpenSkills CLI (npx openskills install ..., referenced in community write-ups of anthropics/skills) — framed and documented specifically around Claude Code installs; an OpenCode path is not documented/confirmed, so excluded rather than listed as claimed-unverified in the main body.
Totals: 14 resources found (9 usable, 5 excluded as Claude-Code-only).
Summary: OpenCode's native SKILL.md discovery (including reading .claude/skills/ paths directly) means the largest official and community skill ecosystems — anthropics/skills (149k★) and VoltAgent's 1,497-skill collection (29.4k★) — are usable in OpenCode with zero porting. Beyond that, two of the very biggest "Claude Code" mega-repos in the whole ecosystem — affaan-m/ECC (211.9k★) and obra/superpowers (267.8k★) — both ship dedicated, documented .opencode/ install paths, and alirezarezvani/claude-skills (23.3k★) ships a scripted OpenCode converter. The main exclusion pattern: several huge "skills marketplace" repos (jeremylongshore's 3,179-skill catalog, glebis/claude-skills) are explicitly and only built for Claude Code's plugin system, with no OpenCode path at all — including, notably, the flagship anthropics/claude-code repo's own bundled plugins.
