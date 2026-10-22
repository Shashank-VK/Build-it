# Part 8 — Coding Agents, Plugins & Developer Environments (03b-agents)

> Research workstream #7 | Verification date: 2026-10-10
> READ-ONLY research: discover, inspect, identify, verify, categorize, explain usage, record sources.
> No installing, executing, building, configuring, ranking, or recommending.

## 1. Research method

### Sources searched (primary-first)
For each agent: official documentation site, official GitHub repository (README, docs/, package.json/extension manifests, CHANGELOG/releases), official extension marketplace listings, official blog/changelog announcements. Secondary: high-quality technical write-ups only where primary docs are unavailable. All compatibility claims are grounded in documentation inspected; unverifiable claims are marked as such.

### Search themes used
1. Exact agent name + "extensions / plugins / skills / hooks / slash commands / MCP"
2. Agent name + "AGENTS.md / CLAUDE.md / rules / instruction files"
3. Agent name + "marketplace / extension registry"
4. "agent CLI 2026" / "new coding agent CLI 2026" (emerging tools)
5. Cross-tool standards: Agent Skills spec (SKILL.md), MCP, AGENTS.md
6. "headless / non-interactive / CI" + agent name (background execution / headless operation)

### Deduplication (already catalogued — cross-referenced, not re-researched)
Per the workstream brief, the following are cross-referenced only:
- **OpenCode's own ecosystem** (prior catalog: 163 usable resources across 26 elements): oh-my-openagent, opencode-market, opencode-marketplace, ocx, awesome-opencode, opencode plugin system, opencode-workspace, opencode-primer, @opencode-ai/sdk, anomalyco/opencode issues (#7467 marketplace gap, #5199 output-styles gap, #8619/#30295 statusLine hook gap, #4031 Python SDK gap).
- **Claude Code hooks / plugin marketplace** and Claude-Code-only resources from the prior OpenCode catalog (excluded items: garrytan/gstack et al. — Claude-Code-only, no OpenCode path).

### Verification labels (used exactly as specified)
**Verified** / **Partially verified** / **Unverified** / **Corrected** / **Archived** / **Inaccessible** / **Historical** / **Unresolved**

### Compatibility classification (used exactly as specified)
**Native** / **Official integration** / **Documented adapter or port** / **Shared standard or protocol** / **Custom integration required** / **Reference-only** / **Unverified** / **Incompatible or unavailable**

---

## 2. OpenCode (cross-reference — deduped)

### Resource record: OpenCode
- **Resource name:** OpenCode
- **Canonical identity:** `sst/opencode` — open-source terminal coding agent by SST (formerly built as a Claude Code open alternative). Command: `opencode`.
- **Category:** Ready-made coding agent (terminal TUI)
- **Type:** AGENT + extension host (plugins, skills, hooks, subagents, MCP, commands, themes)
- **Official URL:** https://opencode.ai (repo: https://github.com/sst/opencode)
- **Description:** Terminal-based AI coding agent with a plugin architecture: JS/TS plugins with lifecycle hooks, Agent Skills (SKILL.md via `.agents/skills/` and `~/.config/opencode/skills/`), subagents, slash commands, background tasks, headless/CI operation, shareable themes, and a provider-agnostic model layer (including "Models.dev" routing).
- **Contents inspected:** This workstream does NOT re-inspect OpenCode's ecosystem per the dedup brief — it is already covered by the prior catalog (163 usable resources across 26 elements in `~/workspace/user/files/catalog.md`, plus `05-remaining-resources.md`). Cross-reference only.
- **Actual capabilities:** (per prior catalog) Plugin system (`opencode.json` plugin config), skill directories, hook events, agent definitions, command files, background task tools, checkpoint tools, statusline hooks, usage tracking.
- **Usage domain:** General-purpose terminal coding agent; extension-host for third-party skills/plugins.
- **Integration method:** AGENTS.md instruction files; SKILL.md skills; MCP; plugin packages via `opencode plugin` CLI.
- **Compatibility:** Native (OpenCode's own ecosystem) — see prior catalog. Cross-tool: **Shared standard or protocol** for Agent Skills (agentskills.io) and MCP.
- **Dependencies:** Node.js; model provider credentials (Anthropic, OpenAI, others; or OpenCode Zen managed service).
- **Availability:** Open source, actively maintained (prior catalog: verified 2026-08).
- **Maintenance:** Active.
- **License:** MIT (per repo; cross-referenced, not re-verified this pass).
- **Limitations:** Prior catalog records known gaps (no native marketplace — issue #7467; no output-styles — #5199; statusLine hook gap — #8619/#30295; no official Python SDK — #4031).
- **Related resources:** oh-my-openagent, opencode-market, opencode-marketplace, ocx, awesome-opencode, @opencode-ai/sdk (prior catalog).
- **Sources:** Prior workstream catalog (`~/workspace/user/files/catalog.md`, 2026-08-07/08).
- **Verification date:** 2026-10-10 (cross-reference of prior verification).
- **Confidence:** High for "already catalogued" status; **Unverified** in this pass (deduped by design).

---

## 3. Claude Code

### Resource record: Claude Code
- **Resource name:** Claude Code
- **Canonical identity:** Anthropic's official agentic coding tool. Command: `claude`. Surfaces: terminal, VS Code extension, desktop app (local sessions), cloud sessions (claude.ai/code), and Agent SDK.
- **Category:** Ready-made coding agent (first-party, single-vendor model)
- **Type:** AGENT + full extension host (plugins, skills, subagents, hooks, slash commands, MCP, LSP, output styles)
- **Official URL:** https://code.claude.com (docs: https://code.claude.com/docs/en/plugins)
- **Description:** Anthropic's flagship coding agent with the deepest first-party extensibility stack of any single-vendor agent: composable extension primitives (skills, subagents, hooks, slash commands, MCP servers) that work standalone in `~/.claude/` / `.claude/` and can be packaged into versioned, shareable **plugins** distributed through **marketplaces**.
- **Contents inspected:** Official docs page "Plugins overview" (fetched 2026-10-10, full page): plugin definition, marketplace model, install scopes, component model. Secondary corroboration: dev.to SkillGild plugin guides; `michaeldimmitt/claude-skills` sources index (docs map). Did not re-inspect hooks/plugin-marketplace internals per dedup brief.
- **Actual capabilities:**
  - **Skills:** SKILL.md (progressive disclosure; name/description in context, body loaded on use); user `~/.claude/skills/`, project `.claude/skills/`.
  - **Slash commands:** `.claude/commands/<name>.md` (being folded into the skills model; plugin commands namespaced `/plugin-name:command`).
  - **Subagents (custom agents):** `.claude/agents/<name>.md` with tool restrictions, model selection, delegation.
  - **Hooks:** lifecycle event handlers (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, etc.) via `settings.json` or plugin `hooks.json`; plus JS "hooks modules" (a plugin containing one is called a "mod").
  - **Plugins:** directory with `.claude-plugin/plugin.json` manifest (name/description/version/author) + `skills/`, `commands/`, `agents/`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`, `settings.json`, `output-styles/`; loaded as one unit.
  - **Marketplaces:** git-repo or directory catalogs with `.claude-plugin/marketplace.json`; official (`anthropics/claude-plugins-official`, auto-added), community, and third-party tiers; `/plugin` UI with Discover/Installed/Marketplaces tabs; team pinning of marketplace + plugin list via committed settings; install scopes (user/project/local).
  - **Instruction files:** CLAUDE.md (project root, nested, global `~/.claude/CLAUDE.md`, CLAUDE.local.md untracked variant).
  - **Permissions:** settings.json allow/deny lists; permission modes; plugin trust/security review guidance.
  - **External integrations:** MCP servers (`.mcp.json`, `claude mcp add`), LSP servers (`.lsp.json`), background execution, headless/non-interactive operation, scheduling, Slack integration (per secondary comparison).
  - **API/SDK access:** Claude Agent SDK (TypeScript/Python) supports loading local plugins programmatically.
- **Usage domain:** Professional software engineering; agent customization and team distribution.
- **Integration method:** Marketplace install (`/plugin marketplace add <owner/repo>` + `/plugin install <name>@<marketplace>`); direct folder load (`--plugin-dir`); settings files.
- **Compatibility:** Native (own ecosystem). **Shared standard or protocol** for SKILL.md agent skills and MCP. Claude-Code-only plugins have **Incompatible or unavailable** status for OpenCode (per prior catalog exclusions, e.g. garrytan/gstack — listed there as Claude-Code-primary).
- **Dependencies:** Anthropic account/subscription or API key; Node.js.
- **Availability:** Commercial (Anthropic plans); CLI + IDE + web.
- **Maintenance:** Very active (official marketplace, SkillGild listings, weekly-scale ecosystem churn).
- **License:** Proprietary.
- **Limitations:** Plugins run with user privileges (trust review required); enabled plugins add per-turn context cost (official marketplace shows context-cost estimates); Claude-only models (no model routing).
- **Related resources:** anthropics/skills (official skills repo); `anthropics/claude-plugins-official` marketplace; Agent Skills open standard (agentskills.io); OpenCode (open alternative).
- **Sources:**
  - https://code.claude.com/docs/en/plugins (official, fetched 2026-10-10)
  - https://dev.to/skillgild/claude-code-plugins-install-build-and-publish-372f (secondary, 2026-10)
  - https://dev.to/skillgild/claude-code-skills-vs-agents-vs-commands-vs-plugins-vs-mcp-30co (secondary, 2026-10)
  - https://github.com/michaeldimmitt/claude-skills/blob/HEAD/plugins/tools/claude-code/skills/sources.md (secondary index)
- **Verification date:** 2026-10-10
- **Confidence:** High. Plugin/marketplace architecture **Verified** against official docs. Hook/plugin-marketplace internals intentionally cross-referenced per dedup brief.

---

## 4. Cursor

### Resource record: Cursor
- **Resource name:** Cursor
- **Canonical identity:** AI-first code editor by Anysphere. Editor + `cursor-agent` CLI (a.k.a. Cursor CLI) + Cloud Agents. VS Code fork.
- **Category:** Ready-made coding agent (IDE) + CLI agent
- **Type:** AGENT + extension host (rules, subagents, skills, commands, hooks, plugins/marketplace, MCP, VS Code extensions)
- **Official URL:** https://cursor.com (docs: https://cursor.com/docs)
- **Description:** The most widely adopted AI IDE. Its Agent (chat) is steered by a layered customization stack — Project Rules (`.cursor/rules/*.mdc`), User/Team Rules, AGENTS.md, and (since v2.4–v2.5, 2026) custom **subagents** and a **plugin/marketplace** system packaging skills, subagents, MCP servers, hooks, and rules. Inherits the full VS Code extension marketplace.
- **Contents inspected:** Official docs page "Rules" (https://cursor.com/docs/context/rules, fetched 2026-10-10, full page): four rule types (Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually), frontmatter (`description`, `globs`, `alwaysApply`), AGENTS.md support (root + nested), Team Rules, plugin-based rule import (`.cursor-plugin/marketplace.json`), Customize UI. Secondary: Cursor subagents/platform specs (`.cursor/agents/*.md`, hooks at `.cursor/hooks.json`, Marketplace at cursor.com/marketplace), CLI docs (cursor.com/en/cli), changelog notes (Agents Window v3.0).
- **Actual capabilities:**
  - **Rules files:** `.cursor/rules/*.mdc` (frontmatter `description`/`globs`/`alwaysApply`); User Rules (global); Team Rules (dashboard-enforced, Enterprise).
  - **Instruction files:** `AGENTS.md` at project root AND nested subdirectories (combined, more specific wins); legacy `.cursorrules`.
  - **Slash commands:** project `.cursor/commands/` (user-level `~/.cursor/commands` reported by community, **Unverified** officially); built-ins (`/create-rule`, `/plan`, `/ask`, `/worktree`, `/best-of-n`, `/in-cloud`).
  - **Custom agents / subagents:** Markdown + YAML frontmatter (`name`, `description`, `model` [inherit|fast|specific id], `readonly`, `is_background`) in `.cursor/agents/` (project) or `~/.cursor/agents/` (user); also natively reads `.claude/agents/` and `.codex/agents/`; built-ins Explore/Bash/Browser; nesting since 2.5; async background subagents writing to `~/.cursor/subagents/`.
  - **Skills:** Agent Skills support (`cursor.com/docs/skills`); `.cursor/skills/` discovery (secondary evidence).
  - **Hooks:** `hooks.json` (repo `.cursor/` root; `_hook_md` companion fields → `.cursor/hooks/`), events incl. sessionStart/End, preToolUse/postToolUse, beforeShellExecution, beforeMCPExecution, beforeFileEdit, subagentStart/Stop (secondary evidence; exact schema **Partially verified**).
  - **Plugins & marketplace:** plugin = directory with plugin manifest bundling skills/commands/rules/hooks/MCP; published via marketplace with `.cursor-plugin/marketplace.json`; install via Customize → From GitHub Repository or team marketplace (official docs page confirms the mechanism; marketplace URL https://cursor.com/marketplace per secondary).
  - **MCP:** `.cursor/mcp.json` / Settings → MCP; MCP Apps host (Cursor 2.6+) for inline UI.
  - **Model routing:** built-in model picker + per-subagent `model` selection; Custom Modes via skills.
  - **Permission systems:** per-tool approval; auto-execution levels (editor agent).
  - **Session state:** local sessions + Cloud Agents (remote VMs, `/in-cloud`).
  - **Background execution:** background subagents; Agents Window (v3.0) for parallel agents across repos/worktrees/cloud.
  - **Headless operation:** `cursor-agent` CLI (non-interactive), Cloud Agents API.
  - **API/SDK access:** ACP support (`agent acp` per hapi docs); Cloud Agents.
  - **External tool integrations:** full VS Code extension marketplace; MCP; GitHub (`@cursor` on issues/PRs updates rules).
- **Usage domain:** Daily-driver IDE for professional developers; team-standardized agent workflows.
- **Integration method:** Customize UI; `npx <plugin> install` CLIs (community convention); git-clone of rule repos; marketplace one-click (secondary).
- **Compatibility:** Native (own ecosystem). **Official integration** with VS Code extension marketplace (VS Code fork). **Shared standard or protocol** for AGENTS.md, SKILL.md, MCP. **Documented adapter or port**: reads `.claude/agents/` and `.codex/agents/` natively (secondary evidence, Partially verified).
- **Dependencies:** Cursor account/subscription; VS Code-compatible OS.
- **Availability:** Commercial (free tier; Pro from ~$20/mo, credit-based).
- **Maintenance:** Very active (changelog through v3.x in 2026).
- **License:** Proprietary.
- **Limitations:** Rules don't affect Cursor Tab/inline edit; `~/.cursor/commands` user path not officially documented; hooks surface less documented than Claude Code's.
- **Related resources:** VS Code (upstream); Windsurf/Devin Desktop (competitor); Cline/Roo Code (also run inside Cursor per Cline docs).
- **Sources:**
  - https://cursor.com/docs/context/rules (official, fetched 2026-10-10)
  - https://cursor.com/docs (official docs root, cited)
  - https://cursor.com/en/cli (official, cited via secondary)
  - https://github.com/thixpin/pitway/blob/HEAD/docs/evidence/M022/cursor.md (secondary evidence file, 2026-09)
  - https://github.com/factoryengineering/factoryengineering/blob/HEAD/src/content/docs/ides/cursor.md (secondary)
  - https://github.com/yhlooo/dsh-bridges/blob/HEAD/docs/reference/cursor/subagents.md (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** High on rules/AGENTS.md/plugin mechanism (official docs). Medium (Partially verified) on hooks schema, marketplace details, and cross-tool agent reads (secondary evidence only).

---
## 5. OpenAI Codex CLI

### Resource record: OpenAI Codex CLI
- **Resource name:** Codex CLI
- **Canonical identity:** `openai/codex` — OpenAI's open-source coding agent. Rust codebase (`codex-rs/`; older Node wrapper in `codex-cli/` retained). Command: `codex`.
- **Category:** Ready-made coding agent (open agent platform; TUI + non-interactive + app-server)
- **Type:** AGENT + extension host (skills, plugins, subagents, hooks, MCP, agents, exec-policy rules) + SDK surfaces
- **Official URL:** https://developers.openai.com/codex (docs); https://github.com/openai/codex (repo)
- **Description:** OpenAI's terminal coding agent, architecturally an open agent platform: `codex-core` is shared by the TUI, a non-interactive runner, an MCP server mode, a VS Code-facing **app-server** (JSON-RPC 2.0 over stdio, powering the Codex VS Code extension `openai.chatgpt`), a remote exec-server, and hosted/mobile control surfaces. Deep customization via layered TOML config, Agent Skills, TOML-defined subagents, Starlark exec-policy rules, and a ChatGPT-shared plugin directory.
- **Contents inspected:** Official docs "Build skills" (https://developers.openai.com/codex/skills, fetched 2026-10-10, full page): skill scopes/locations, progressive disclosure (2% context budget), `SKILL.md` + `agents/openai.yaml` metadata, `$skill-installer`, `[[skills.config]]` disable. Secondary corroboration: pitway evidence file (skills/commands/agents/rules/tools/permissions matrix with doc links); Codex CLI development SKILL.md (config schema, hook config, plugin manifest paths); config reference (https://developers.openai.com/codex/config-reference/, cited in an upstream issue). Repo facts: `openai/codex` Apache-2.0, ~127,889 stars (Aug 2026), `codex-rs/app-server/README.md` (mirrored).
- **Actual capabilities:**
  - **Skills:** `SKILL.md` directories scanned at scopes REPO (`$CWD/.agents/skills`, `$CWD/../.agents/skills`, `$REPO_ROOT/.agents/skills`), USER (`$HOME/.agents/skills`), ADMIN (`/etc/codex/skills`), SYSTEM (bundled, cached at `$CODEX_HOME/skills/.system`); required frontmatter `name` + `description`; symlinked folders followed; invocation explicit (`$skill-name`) or implicit; `agents/openai.yaml` for UI metadata/invocation policy/tool deps; `[[skills.config]]` disable entries; `$skill-installer` curated installer.
  - **Plugins:** universal plugin directory **shared by ChatGPT and Codex** — plugins distribute reusable skills and connectors; bundle skills + registered MCP servers + bundled MCP config + presentation assets; work in ChatGPT (web/desktop/mobile), ChatGPT desktop's Codex, Codex IDE extension, and Codex CLI. (Official skills page; manifest shape in `codex-rs/plugin/src/manifest.rs` per secondary source.)
  - **Slash commands / custom prompts:** `~/.codex/prompts/*.md` surfaced as `/prompts:<name>` — **deprecated in favor of skills** (official); `$1`–`$9`/`$ARGUMENTS` placeholders (legacy).
  - **Custom agents (subagents):** TOML agent roles in `~/.codex/agents/` and `.codex/agents/` (`name`, `description`, `developer_instructions`, model/sandbox/MCP/skill overrides); `[agents]` global settings; prompt-driven spawning with isolated context.
  - **Instruction files:** layered `AGENTS.md` (root→CWD concatenation, `AGENTS.override.md` first, 32 KiB default cap via `project_doc_max_bytes`); global `~/.codex/AGENTS(.override).md`; `model_instructions_file`, `instructions`, `developer_instructions` config keys.
  - **Hooks:** `hooks.json` (user `~/.codex/hooks.json`, project `.codex/hooks.json`); lifecycle events; admin `requirements.toml` can set `allow_managed_hooks_only`.
  - **Permission systems:** `sandbox_mode` (read-only / workspace-write / danger-full-access) × `approval_policy` (untrusted/on-request/never/granular); Starlark `prefix_rule` `.rules` files per config layer; network proxy domain allow/deny; protected paths; named `[permissions.*]` profiles; trust-gated project config.
  - **MCP / tool registry:** `[mcp_servers.<name>]` tables (stdio + streamable HTTP), tool filtering, per-tool approval modes; built-in `web_search`.
  - **Model routing:** `model` key; provider config; (OpenAI-centered model plane).
  - **Session state:** append-only canonical history; cross-session memory pipeline (two-phase, per secondary architecture review); `/resume`-style session continuation.
  - **Background execution:** non-interactive runner; remote exec-server; `codex app-server` for IDE embedding.
  - **Headless operation:** Verified — non-interactive mode for CI (`codex exec`-style one-shot; exact flags in CLI reference).
  - **API/SDK access:** app-server JSON-RPC protocol (documented in-repo); SDKs referenced in repo (`sdk/` directory).
  - **External tool integrations:** MCP; VS Code extension via app-server; ChatGPT surfaces via shared plugins.
- **Usage domain:** Software engineering agent for OpenAI-model users; embeddable agent core (app-server) for IDE vendors.
- **Integration method:** `~/.codex/config.toml` (+ `.codex/config.toml` project overlay, `/etc/codex/config.toml` admin, `-c key=value` CLI overrides; JSON schema in `codex-rs/core/config.schema.json`); plugin directory install; `$skill-installer`.
- **Compatibility:** Native (own ecosystem). **Shared standard or protocol** for Agent Skills (agentskills.io) and MCP; shares plugin directory with ChatGPT (**Official integration** within OpenAI surfaces). **Documented adapter or port**: Cursor natively reads `.codex/agents/` (secondary evidence). `~/.agents/skills` shared bucket with Claude Code.
- **Dependencies:** OpenAI account/API access or ChatGPT subscription (some features, e.g. plugins/marketplace, require ChatGPT account auth per secondary).
- **Availability:** Open source (repo public); CLI via npm/cargo; VS Code extension on marketplace.
- **Maintenance:** Very active (127k+ stars; weekly-scale commits through 2026-08).
- **License:** Apache-2.0.
- **Limitations:** Project-local config cannot override network/provider settings (security boundary); skill discovery has no `~/.codex/skills` authoring location (uses `~/.agents/skills`); API surface evolves rapidly (field names should be re-verified per release).
- **Related resources:** ChatGPT (shared plugins/skills); Codex VS Code extension (`openai.chatgpt`); Cursor (reads `.codex/agents/`); open-gsd/gsd-core (integrates Codex runtime).
- **Sources:**
  - https://developers.openai.com/codex/skills (official, fetched 2026-10-10)
  - https://developers.openai.com/codex/config-reference/ (official, cited via upstream issue)
  - https://github.com/openai/codex (official repo; commit/issue pages crawled 2026-10)
  - https://github.com/thixpin/pitway/blob/HEAD/docs/evidence/M022/codex.md (secondary evidence, 2026-09)
  - https://github.com/tomdale/skills/blob/HEAD/.agents/skills/codex-cli-development/SKILL.md (secondary, repo-source-anchored)
  - https://github.com/s2p2/dsh-lab/blob/HEAD/docs/research/harness-map/codex.md (secondary architecture review, 2026-08)
- **Verification date:** 2026-10-10
- **Confidence:** High on skills/plugin/config model (official docs). Medium on subagent TOML schema and hook event names (secondary evidence only — **Partially verified**).

---

## 6. Antigravity CLI (Google) — successor to Gemini CLI

### Resource record: Antigravity CLI (`agy`)
- **Resource name:** Antigravity CLI
- **Canonical identity:** Google's terminal coding agent, part of the Google Antigravity agent-first development platform (Antigravity 2.0 desktop + CLI + SDK). Command: `agy`. Go binary.
- **Category:** Ready-made coding agent (first-party platform CLI)
- **Type:** AGENT + extension host (plugins, skills, rules, hooks, custom agents, MCP)
- **Official URL:** https://antigravity.google (docs: https://antigravity.google/docs, https://antigravity.google/docs/cli/plugins — cited via secondary; primary blog: Google Developers Blog 2026-05-19)
- **Description:** Announced at Google I/O 2026 (May 19, 2026) as the replacement for Gemini CLI: a Go-based terminal agent sharing one unified agent harness with the Antigravity 2.0 desktop app. Supports async background subagents, lifecycle hooks, workspace skills/rules/plugins, custom agents, and MCP — with first-launch migration from Gemini CLI (`agy plugin import gemini`).
- **Contents inspected:** Not fetched directly (official docs are JS-heavy; no verbatim-fetchable primary page obtained this pass). Evidence: Google Developers Blog announcement (primary, verified via blog search index, 2026-05-19: "Transitioning Gemini CLI to Antigravity CLI"); gsd-core issue #1928 quoting the blog ("Antigravity CLI keeps the most critical features of Gemini CLI: Agent Skills, Hooks, Subagents, and Extensions (now as Antigravity plugins)"); Lisa PRD #720 (Antigravity docs summary: `.agents/skills`, `.agents/rules`, `.agents/mcp_config.json`, `hooks.json` events PreToolUse/PostToolUse/PreInvocation/PostInvocation/Stop, `GEMINI.md`/`AGENTS.md` context); three independent cheatsheets/research docs (cantrips, cortex-forge, jqueryscript) agreeing on plugin layout and CLI surface.
- **Actual capabilities (Partially verified — secondary-sourced, mutually corroborated):**
  - **Plugins:** `plugin.json` at plugin root (only `name` required; `$schema: https://antigravity.google/schemas/v1/plugin.json`) + optional `skills/<name>/SKILL.md`, `rules/*.md` (+ `rules.json`), `agents/`, `hooks.json`, `mcp_config.json`; `agy plugin list|install|enable|disable|uninstall`; install paths: workspace `.agents/plugins/` (IDE scans), global `~/.gemini/config/plugins/`; CLI stages to `~/.gemini/antigravity-cli/plugins/<name>/`; **no marketplace/marketplace.json** (explicitly noted by cantrips research).
  - **Skills:** workspace `.agents/skills/` or global `~/.gemini/antigravity-cli/skills/`; surfaced as slash commands (e.g. `/format-tests`); progressive disclosure.
  - **Rules:** `.agents/rules/*.md`, `AGENTS.md`/`GEMINI.md` auto-parsed; user+workspace rules share ~20k token budget (cheatsheet).
  - **Custom agents:** Markdown + YAML frontmatter; workspace `.agents/agents/<name>.md` (or `<name>/agent.md`), global `~/.gemini/config/agents/`; `--agent <name>` launch; `@<subagent>` messaging; nested/background subagents; browser subagent.
  - **Hooks:** `hooks.json` pre/post tool interceptors (events incl. PreToolUse, PostToolUse, PreInvocation, PostInvocation, Stop); `/hooks` viewer.
  - **MCP:** `agy mcp add/list/enable/disable/remove` (stdio + http); workspace `.agents/mcp_config.json`, user `~/.gemini/config/mcp_config.json`.
  - **Slash commands:** built-ins (`/resume`, `/rewind`, `/fork`, `/mcp`, `/hooks`, `/add-dir`); skills auto-convert to commands.
  - **Session state:** SQLite-backed conversations; `/resume`; session export to Antigravity 2.0 GUI.
  - **Background execution:** async background subagents; background sidecars with cron scheduling; `agy --print` non-interactive mode (text/JSON/stream-JSON) for scripts and CI.
  - **Model routing:** `agy --model`; multi-model (Gemini 3.5 Flash noted; Ultra-plan multi-agent teamwork).
  - **Permission systems:** `allowNonWorkspaceAccess` gate; terminal sandbox (`enableTerminalSandbox`); plan/accept-edits/default modes.
- **Usage domain:** Terminal-first agentic development on Google's stack; Gemini CLI migration target.
- **Integration method:** `agy plugin install <path|git-url>`; `.agents/` workspace directory conventions; Google account auth.
- **Compatibility:** **Official integration** with Antigravity 2.0 desktop (shared harness/settings). Migration path from Gemini CLI (**Documented adapter or port**: `agy plugin import gemini`, `.gemini/` config reuse). **Shared standard or protocol** for SKILL.md and MCP. **Custom integration required** for Claude-Code-style `marketplace.json` catalogs (none exists; cohabitation with Codex `.agents/plugins/marketplace.json` untested).
- **Dependencies:** Google account; non-enterprise users (enterprise Gemini CLI access continues separately).
- **Availability:** GA (announced 2026-05-19); consumer/free/Pro/Ultra migration completed 2026-06-18.
- **Maintenance:** Active (Google I/O 2026 platform bet).
- **License:** Proprietary (Go binary distribution).
- **Limitations:** No plugin marketplace; hook event schema not fully enumerated in public docs (PostToolUse equivalent **Unverified** per cantrips); enterprise vs consumer surface split.
- **Related resources:** Gemini CLI (predecessor — see Historical record below); Antigravity 2.0 desktop; Antigravity SDK (custom agents, Managed Agents in Gemini API).
- **Sources:**
  - Google Developers Blog, "An important update: Transitioning Gemini CLI to Antigravity CLI" (2026-05-19) — verified via https://developers.googleblog.com index (primary)
  - https://github.com/open-gsd/gsd-core/issues/1928 (quotes primary announcement)
  - https://github.com/codyswanngt/lisa/issues/720 (secondary, docs-anchored)
  - https://github.com/toverux/cantrips/blob/HEAD/docs/research/multi-harness-plugins.md (secondary research)
  - https://github.com/jqueryscript/antigravity-cli-cheatsheet/blob/HEAD/readme.md (secondary)
  - https://github.com/fderuiter/agy-skills/blob/HEAD/wiki/Antigravity-Customizations.md (secondary)
  - https://www.scriptbyai.com/antigravity-cli/ (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** High on existence/successor status and announcement facts (primary). Medium (**Partially verified**) on extension-system details (secondary, multi-source corroboration; official docs not directly fetched).

### Resource record: Gemini CLI (Historical)
- **Resource name:** Gemini CLI
- **Canonical identity:** `google-gemini/gemini-cli` — Google's former open-source terminal AI agent (TypeScript). Command: `gemini`.
- **Category:** Ready-made coding agent (HISTORICAL — superseded)
- **Type:** AGENT + extension host (historical: extensions, skills, hooks, MCP, custom commands)
- **Official URL:** https://github.com/google-gemini/gemini-cli (archived/sunset for consumers)
- **Description:** Google's community terminal agent (reached 100k+ GitHub stars, millions of users per Google). Extension system: `gemini-extension.json` manifests (mcpServers, contextFileName, excludeTools, settings, themes), `commands/*.toml` custom commands, `hooks/hooks.json` (v0.26.0+), SKILL.md skills (`~/.gemini/skills/`, `.gemini/skills/`, `~/.agents/skills/`), GEMINI.md instruction files, `settings.json` (user/project/system), `@google/gemini-cli-sdk` (`GeminiCliAgent`), ACP mode, extension gallery (50+ at launch, hosted in public GitHub repos).
- **Contents inspected:** Secondary research docs only (elevenpowers host profile; gemini-cli-pro extension guide; philschmid/gemini-cli-extension README). Not fetched from primary (JS-heavy docs; product sunset).
- **Actual capabilities (Historical):** As above; all extension surfaces now live on as "Antigravity plugins" per Google's announcement.
- **Usage domain:** (Historical) terminal agentic coding for Gemini models.
- **Integration method:** `gemini extensions install|uninstall|enable|disable|update|link|new`; `gemini skills install|list|uninstall`.
- **Compatibility:** **Historical** — consumer/free/Pro/Ultra request serving ended 2026-06-18; enterprise access continues under relevant licenses/API keys. Qwen Code is a fork of Gemini CLI v0.8.2 (**Documented adapter or port** lineage).
- **Dependencies:** (Historical) Google account / Gemini API key.
- **Availability:** Sunset for non-enterprise users (2026-06-18).
- **Maintenance:** Superseded by Antigravity CLI.
- **License:** Apache-2.0 (open source; repo remains).
- **Limitations:** Dead product path for consumers — new work should target Antigravity CLI.
- **Related resources:** Antigravity CLI (successor); Qwen Code (fork); `@google/gemini-cli-sdk`.
- **Sources:**
  - Google Developers Blog announcement (2026-05-19) via developers.googleblog.com index (primary)
  - https://github.com/satyamsingh-git/elevenpowers/blob/HEAD/docs/research/hosts/gemini-cli.md (secondary)
  - https://github.com/juberuu/gemini-cli-pro/blob/HEAD/docs/extension.md (secondary)
  - https://github.com/philschmid/gemini-cli-extension (secondary)
  - https://www.neowin.net/news/google-brings-extensions-feature-to-gemini-cli/ (secondary, 2025-10)
- **Verification date:** 2026-10-10
- **Confidence:** High on sunset facts (primary). Medium on extension-system details (secondary). Label: **Historical**.

---
## 7. GitHub Copilot CLI (+ VS Code Copilot extensions)

### Resource record: GitHub Copilot CLI
- **Resource name:** GitHub Copilot CLI
- **Canonical identity:** GitHub's terminal-native agentic coding CLI. Command: `copilot` (standalone; distinct from the legacy `gh copilot suggest` shell helper). npm: `@github/copilot`.
- **Category:** Ready-made coding agent (multi-model terminal agent)
- **Type:** AGENT + extension host (custom agents, skills, hooks, plugins, MCP, instructions) + SDK
- **Official URL:** https://docs.github.com/en/copilot (CLI: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)
- **Description:** Fully agentic terminal Copilot: edits files, runs commands, creates PRs, iterates toward goals. Multi-model (Claude Sonnet/Opus, GPT-5.x, Gemini switchable mid-session via `/model`; BYOK `providers.json`), plan + autopilot modes, GitHub-native integration, LSP support, and a customization stack (instructions, agents, skills, hooks, plugins) that mirrors Claude Code's primitives with `.github/`-rooted paths.
- **Contents inspected:** Official docs "GitHub Copilot CLI" (fetched 2026-10-10, 409-line page): interactive vs programmatic (`-p/--prompt`) UIs, plan mode, approval options (`--allow-tool`, `--allow-all-tools`), trusted directories, local sandbox (`/sandbox enable`), cloud sandboxes (`copilot --cloud`), auto-compaction (`/compact`, `/context`), and the customization list (custom instructions, MCP, custom agents, hooks, skills, Copilot Memory). Secondary: docs.github.com customization cheat-sheet paths (via repokan/docs mirror + Lisa PRD #719: `~/.copilot/{agents,skills,hooks,providers.json}`, `.github/{agents,skills,hooks,prompts,instructions}`); custom-agents SDK doc (docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents); copilot-cli-for-beginners tutorial repo (github.com/github/copilot-cli-for-beginners).
- **Actual capabilities:**
  - **Custom agents:** `.agent.md` files — repo `.github/agents/`, user `~/.copilot/agents/` (repo wins on name clash); YAML frontmatter (`name`, `description`, `tools`, `model`, `disable-model-invocation`, `user-invocable`, `mcp-servers`); `/agent` picker; `--agent <name>` programmatic; SDK `customAgents` with sub-agent orchestration + Fleet mode (parallel subagents).
  - **Skills:** Agent Skills (SKILL.md) in `.github/skills/`, `~/.copilot/skills/`, plus cross-reads of `.claude/skills/` and `.agents/skills/` (secondary; Partially verified); `/skills` management commands.
  - **Hooks:** `.github/hooks/*.json` + inline `hooks` key in settings + user `~/.copilot/hooks/`; lifecycle events (sessionStart/userPromptSubmitted/preToolUse/postToolUse/sessionEnd/errorOccurred); preToolUse deny blocks; CLI GA / VS Code preview (secondary).
  - **Plugins:** `copilot plugin install <path|owner/repo|plugin@marketplace>`; `/plugin` management; legacy manifest accepts `.claude-plugin/plugin.json`; "Agent Plugins 1.0" wants root `plugin.json` + `skills/` + `com.github.copilot/{agents,hooks,commands,rules}` (secondary; Partially verified); enterprise-managed plugins (public preview 2026-05-06 per cantrips).
  - **Instruction files:** `.github/copilot-instructions.md` (always-on) + `.github/instructions/*.instructions.md` (`applyTo:` globs) + user `~/.copilot/instructions/`; reads `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` (secondary; Partially verified); Agentic Memory.
  - **Slash commands:** built-ins (`/agent`, `/skills`, `/mcp`, `/plugin`, `/instructions`, `/env`, `/model`, `/diff`, `/pr`, `/review`, `/plan`, `/research`, `/compact`, `/context`, `/usage`, `/resume`); prompt-file commands `.github/prompts/*.prompt.md` are VS Code-only, NOT CLI (secondary).
  - **MCP:** user `~/.copilot/mcp-config.json`, repo `.github/mcp.json`, workspace `.mcp.json`; `/mcp add`; agent-scoped `mcp-servers` frontmatter; built-in GitHub/Playwright/fetch/time servers (secondary).
  - **Permission systems:** per-tool approval prompts; `--allow-tool='shell(git)'`; trusted directories; local sandboxing; cloud sandboxes; content-exclusion policies (Business/Enterprise).
  - **Session state:** auto-compaction at 95%; `/resume`; cloud sandbox session persistence across machines.
  - **Background execution:** cloud sandboxes run tasks in parallel; multi-subagent Fleet mode.
  - **Headless operation:** `-p/--prompt` programmatic mode; pipe input; `copilot --cloud`.
  - **API/SDK access:** `@github/copilot-sdk` (`CopilotClient`, `defineTool`, `customAgents`, `AsAIAgent` for Microsoft Agent Framework); ACP support (`copilot --acp --stdio` per hapi docs).
  - **External tool integrations:** GitHub (issues/PRs/Actions/workflows via natural language + GitHub MCP server); LSP servers (`add-lsp-servers` doc); computer use (macOS/Windows desktop automation, preview).
- **Usage domain:** Terminal-centric GitHub workflows; enterprise teams on Copilot plans.
- **Integration method:** `~/.copilot/` user config dir; `.github/` repo conventions; `copilot plugin install`; npm `@github/copilot`.
- **Compatibility:** Native (own ecosystem). **Shared standard or protocol** for SKILL.md and MCP. **Documented adapter or port**: accepts Claude-Code-style `.claude-plugin/plugin.json` manifests and reads `.claude/skills/`, `.agents/skills/`, `.claude/agents/` (secondary evidence — **Partially verified**). VS Code Copilot Chat shares the customization model (**Official integration** across GitHub surfaces: CLI / VS Code / JetBrains / cloud agent).
- **Dependencies:** GitHub Copilot subscription (Free through Enterprise; usage-based AI Credits since 2026-06 per secondary).
- **Availability:** GA (CLI GA 2026-02-25 per github.blog changelog, secondary). Linux/macOS/Windows (PowerShell/WSL).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Prompt-file slash commands are VS Code-only; Opus models restricted to Pro+ tiers (secondary); enterprise Copilot CLI policy must be enabled by org.
- **Related resources:** VS Code Copilot Chat extensions (below); `@github/copilot-sdk`; Microsoft Agent Framework integration.
- **Sources:**
  - https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli (official, fetched 2026-10-10)
  - https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents (official, search-verified)
  - https://github.com/github/copilot-cli-for-beginners (official tutorial repo)
  - https://github.com/repokan/docs/blob/HEAD/content/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md (docs mirror, secondary)
  - https://github.com/ejtx16/claude-code-copilot-cli-agentic-coding-skill/blob/HEAD/skills/agent-scaffold/references/copilot-cli-formats.md (secondary, docs-verified 2026-09)
  - https://www.devleader.ca/2026/07/23/github-copilot-cli-custom-agents-and-skills (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** High on CLI core + customization categories (official docs). Medium (Partially verified) on exact config paths and cross-tool reads (secondary evidence only).

### Resource record: VS Code marketplace extensions (Copilot / Cursor / Windsurf host surface)
- **Resource name:** VS Code Extension Marketplace (as agent-extension host)
- **Canonical identity:** Visual Studio Marketplace — extension host shared by VS Code, Cursor, Windsurf/Devin Desktop (VS Code forks), and VS Code-compatible editors.
- **Category:** Extension host / marketplace (not an agent itself)
- **Type:** EXTENSION HOST
- **Official URL:** https://marketplace.visualstudio.com
- **Description:** The distribution channel through which agent-adjacent capabilities reach Cursor, Windsurf, Copilot, Cline, and Roo Code users: language servers, themes, tool integrations — and agent extensions themselves (Cline `saoudrizwan.claude-dev`, Roo Code `RooVeterinaryInc.roo-cline`/`rooveterinaryinc.roo-cline`, Codex `openai.chatgpt`, Kimi Code `moonshot-ai.kimi-code`). Agents are also distributed as `.vsix`.
- **Contents inspected:** Referenced via agent docs (Cline install instructions; Roo Code install; Codex app-server README naming `openai.chatgpt`). No direct marketplace crawl this pass.
- **Actual capabilities:** Extension install/enable/disable; `windsurf --install-extension <id>` CLI parity (secondary evidence in a Windsurf skill); Open VSX as alternative registry (Cline publishes there too).
- **Usage domain:** Editor extension distribution for all VS Code-family agent IDEs.
- **Integration method:** Marketplace UI / `code --install-extension` / fork CLIs.
- **Compatibility:** **Official integration** for Cursor and Windsurf (VS Code forks with gallery access); **Native** for Cline/Roo Code (distributed as extensions).
- **Dependencies:** VS Code-compatible editor.
- **Availability:** Available.
- **Maintenance:** Active (Microsoft).
- **License:** Proprietary marketplace; extensions carry their own licenses.
- **Limitations:** Some forks (e.g., VSCodium-likes) re-point the gallery; marketplace access is a Microsoft service dependency.
- **Related resources:** Open VSX; Cline; Roo Code; Cursor; Windsurf.
- **Sources:** https://docs.cline.bot/ (Cline install); https://github.com/ibm/ibmi-mcp-server/blob/HEAD/docs/clients/cline.mdx (marketplace install steps); agent docs cross-references.
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified** — role as shared host is well-evidenced; no direct marketplace fetch).

---

## 8. Windsurf (Cascade) — now Devin Desktop

### Resource record: Windsurf / Cascade
- **Resource name:** Windsurf (agentic IDE; agent: Cascade)
- **Canonical identity:** AI IDE by Windsurf (Codeium). Agent surface: **Cascade**. **Major 2026 change:** docs now brand the product **"Devin Desktop"** — Cognition's Devin product line subsumes Windsurf (Devin Desktop + CLI on the same plan as Windsurf, per techstackups; docs.windsurf.com pages reference "Devin Desktop" throughout).
- **Category:** Ready-made coding agent (IDE)
- **Type:** AGENT + extension host (rules, workflows, skills, memories, MCP, hooks, VS Code extensions)
- **Official URL:** https://windsurf.com (docs: https://docs.windsurf.com)
- **Description:** Agentic IDE whose Cascade agent is customized through Memories (auto-generated), Rules (user-defined, multi-level), Workflows (slash-command prompt templates), Skills (model-invoked procedures with reference files), and MCP. VS Code fork: full VS Code extension marketplace access plus `windsurf --install-extension` CLI parity.
- **Contents inspected:** Official docs "Cascade Memories" (https://docs.windsurf.com/windsurf/cascade/memories, fetched 2026-10-10, full page): Memories vs Rules vs Workflows vs Skills table; rule scopes (Global `~/.codeium/windsurf/memories/global_rules.md`; Workspace `.devin/rules/*.md` preferred / `.windsurf/rules/*.md` fallback / legacy `.windsurfrules`; AGENTS.md; System/Enterprise); activation modes (`always_on`, `glob`, `model_decision`, `manual` via `trigger:` frontmatter); character limits (6k global, 12k workspace). Secondary: openclaw windsurf-cascade skill (Cascade Hooks, terminal auto-execution levels incl. Turbo Mode, MCP config `~/.codeium/windsurf/mcp_config.json`).
- **Actual capabilities:**
  - **Rules files:** `.devin/rules/*.md` (preferred) / `.windsurf/rules/*.md` (fallback) / legacy `.windsurfrules`; global `global_rules.md`; system-level (Enterprise, OS-specific dirs); activation via `trigger:` frontmatter (always_on/glob/model_decision/manual with `globs:`); AGENTS.md processed by the same rules engine (root = always-on, subdirectory = auto-glob).
  - **Instruction files:** AGENTS.md (zero-config location-scoped rules).
  - **Slash commands:** **Workflows** — prompt templates for repeatable multi-step tasks, manual-only via `/[workflow-name]`.
  - **Skills:** `.windsurf/skills/` (secondary matrix); model dynamically invokes or `@mention`; bundled scripts/templates; docs advise "invest here" for complex tasks.
  - **Custom agents:** Cascade itself is the agent; no user-authored subagent files documented (secondary matrix: no hooks/session-start for Windsurf) — **Unverified** for standalone custom-agent definitions.
  - **Hooks:** "Cascade Hooks" — execute custom shell commands at key points in Cascade's workflow (openclaw skill, secondary; **Partially verified**).
  - **MCP:** `~/.codeium/windsurf/mcp_config.json` (user), project-level configs; Settings → Cascade → Manage MCPs.
  - **Memories:** auto-generated, workspace-scoped, stored `~/.codeium/windsurf/memories/`, retrieved when relevant.
  - **Permission systems:** terminal auto-execution levels (Manual / Semi-auto / Turbo Mode / Custom allow-deny lists).
  - **Session state:** per-workspace memories; conversation persistence in IDE.
  - **Background execution:** not documented as a first-class surface (secondary matrix marks hooks/session-start absent) — **Unverified**.
  - **Headless operation:** not documented — IDE requires GUI context (openclaw skill notes headless automation should use Workflows/MCP instead) — **Unverified/Incompatible or unavailable** for headless.
  - **API/SDK access:** none documented — **Unverified**.
  - **External tool integrations:** VS Code extension marketplace (official integration as VS Code fork); MCP; `.codeiumignore`.
- **Usage domain:** IDE-centric agentic development; enterprise rule enforcement.
- **Integration method:** Cascade Customizations UI; rules directories; `windsurf --install-extension <vscode-id>`.
- **Compatibility:** Native (own ecosystem). **Official integration** with VS Code extension marketplace. **Shared standard or protocol** for AGENTS.md and MCP; SKILL.md discovery via `.windsurf/skills/` (secondary). **Incompatible or unavailable**: headless operation (GUI required).
- **Dependencies:** Windsurf/Devin account; subscription.
- **Availability:** Available; docs rebrand to "Devin Desktop" in progress (2026).
- **Maintenance:** Active (Cognition).
- **License:** Proprietary.
- **Limitations:** No documented plugin marketplace (git-clone distribution only, per secondary matrix); no hook events documented to the depth of Claude Code; headless/CI operation not supported.
- **Related resources:** Devin (Cognition; same plan); Cursor (competitor); Cline (runs inside Windsurf per Cline docs).
- **Sources:**
  - https://docs.windsurf.com/windsurf/cascade/memories (official, fetched 2026-10-10)
  - https://github.com/dvcrn/openclaw-skills-marketplace/blob/HEAD/plugins/lucaslcarrijo--windsurf-cascade/skills/windsurf-cascade/SKILL.md (secondary)
  - https://techstackups.com/comparisons/coding-agent-harness-comparison-2026/ (secondary, Devin/Windsurf plan note)
- **Verification date:** 2026-10-10
- **Confidence:** High on rules/memories/workflows/skills taxonomy (official docs). **Corrected** this pass: product is being rebranded Devin Desktop; `.devin/` paths now preferred over `.windsurf/`. Medium on hooks/MCP details (secondary).

---

## 9. Cline

### Resource record: Cline
- **Resource name:** Cline
- **Canonical identity:** `cline/cline` — open-source AI coding agent. Surfaces: VS Code Extension (`saoudrizwan.claude-dev`), JetBrains Plugin, CLI (`npm i -g cline`), Desktop App, SDK (`@cline/sdk`), Kanban (`npx kanban`).
- **Category:** Ready-made coding agent (multi-surface; model-agnostic)
- **Type:** AGENT + extension host (rules, custom modes, MCP marketplace, skills, plugins, hooks, checkpoints)
- **Official URL:** https://cline.bot (docs: https://docs.cline.bot)
- **Description:** Autonomous coding agent that began as a VS Code extension and grew into a multi-surface platform on a shared agent core ("Cline's agent core" per docs). Plan/Act mode loop with human-in-the-loop approvals; model-agnostic (ClinePass subscription, BYOK, provider profiles).
- **Contents inspected:** Official docs home (https://docs.cline.bot/, fetched 2026-10-10): surfaces, model access (ClinePass $9.99/mo, BYOK), editor support list (VS Code, Cursor, Windsurf, JetBrains, Antigravity, Zed, Neovim via ACP). Official CHANGELOG (cline/cline repo, via search): **4.0.0** adds SDK-backed extension runtime + **Customize marketplace** (Skills, MCP servers, Plugins; installed/marketplace tabs; plugin-bundled skills). Secondary: jexp/agentic-engineering cline profile; edwardathomson/agent-reviews cline review (docs inventory, security model); clemens865 cline-roo-code research (custom modes, MCP self-creation).
- **Actual capabilities:**
  - **Rules files:** `.clinerules` file or `.clinerules/` directory (conditional/glob scoping); AGENTS.md recognized (secondary, **Partially verified**).
  - **Custom modes:** user-defined modes (role definition, tool groups, custom instructions) — the mechanism Roo Code forked and expanded; mode toggle Plan/Act via Tab; auto-approve toggles; YOLO mode.
  - **Slash commands:** MCP prompts surfaced as `/mcp:<server>:<prompt>` (secondary); deep planning via slash commands (review).
  - **Skills:** Customize marketplace distributes Skills (4.0.0+); plugin-bundled skills supported.
  - **Plugins:** **Cline Plugins** (4.0.0+): extend Cline with custom tools, workflows, skills, MCP-powered capabilities; installed from the Customize marketplace.
  - **Marketplace:** in-extension **Customize marketplace** for Skills, MCP servers, Plugins (installed/marketplace tabs, search/filter, enable/disable) — official changelog.
  - **Hooks:** customization docs list hooks (review); exact event schema not captured — **Partially verified**.
  - **MCP:** first-class; `cline_mcp_settings.json`; in-extension MCP Marketplace; stdio + SSE/HTTP; Cline can scaffold and install new MCP servers from chat.
  - **Permission systems:** human-in-the-loop by default (every file change/command needs approval); granular AutoApprovalSettings; `CommandPermissionController` (allow/deny globs); `.clineignore`.
  - **Session state:** checkpoints (rollback); task history; compaction.
  - **Background execution:** parallel sessions (Desktop App); queued prompts; Kanban web board runs many agents in parallel with per-card worktrees.
  - **Headless operation:** CLI supports fully headless automation for CI/CD (`npm i -g cline`) — official docs.
  - **API/SDK access:** `@cline/sdk` (agent core for building agents/automations); ACP mode; standalone build; URI handler deep-linking.
  - **External tool integrations:** MCP; browser tool (real Chromium via Puppeteer); LSP-ish code intelligence; enterprise SSO/audit/observability (OpenTelemetry/Datadog/Grafana/Splunk).
  - **Model routing:** provider profiles; Cline Provider gateway; dynamic model IDs.
- **Usage domain:** Editor-embedded autonomous coding; CI automation; agent-platform building on the SDK.
- **Integration method:** VS Code/JetBrains marketplace install; `npm i -g cline`; Customize marketplace in-extension.
- **Compatibility:** Native (own ecosystem incl. plugins/marketplace). **Official integration** with VS Code + JetBrains marketplaces. Runs inside Cursor/Windsurf/Antigravity/Zed/Neovim (per official docs). **Shared standard or protocol** for MCP and SKILL.md. **Documented adapter or port**: Roo Code is a fork (modes/rules formats shared: `.clinerules`/`.roorules`, `.roo/rules-*`).
- **Dependencies:** Model access (ClinePass, BYOK, or provider keys); VS Code 1.84.0+ for the extension.
- **Availability:** Open source; extension + CLI + desktop + SDK.
- **Maintenance:** Very active (4.0.0 changelog 2026-09/10 window).
- **License:** Apache-2.0 (repo; cross-referenced).
- **Maintenance note:** ClinePass subscription + enterprise tier (SSO, audit trails, remote config, Bugcrowd).
- **Limitations:** No formal sub-agent file system (delegation via Plan-mode tasks/new_task); parallel agents require multiple windows/worktrees or Kanban.
- **Related resources:** Roo Code (fork); Kilo Code (related lineage); Cline SDK; Open VSX.
- **Sources:**
  - https://docs.cline.bot/ (official, fetched 2026-10-10)
  - https://github.com/cline/cline/blob/HEAD/CHANGELOG.md (official, via search 2026-10)
  - https://github.com/jexp/agentic-engineering/blob/HEAD/research/coding-agents/cline.md (secondary)
  - https://github.com/edwardathomson/agent-reviews/blob/HEAD/reviews/coding/cline.md (secondary)
  - https://github.com/clemens865/lazy-fetch/blob/HEAD/research/frameworks/cline-roo-code.md (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** High on surfaces/marketplace/plugins (official docs + changelog). Medium on hooks/rules specifics (secondary).

---
## 10. Roo Code

### Resource record: Roo Code
- **Resource name:** Roo Code
- **Canonical identity:** `RooCodeInc/Roo-Code` — VS Code extension (fork lineage from Cline/Roo-Cline). Publisher IDs seen: `RooVeterinaryInc.roo-cline` / `rooveterinaryinc.roo-cline` / `roocode.roocode` (marketplace naming has shifted; canonical repo is RooCodeInc/Roo-Code). Also ships **Roo Code CLI** and **Roomote** (cloud agent).
- **Category:** Ready-made coding agent (multi-mode IDE agent)
- **Type:** AGENT + extension host (custom modes, rules, MCP, checkpoints, marketplace)
- **Official URL:** https://roo.dev (docs: https://roo.dev/docs; legacy docs site: https://roocodeinc.github.io/Roo-Code/)
- **Description:** Autonomous coding agent distinguishing itself through **modes as the primary extension primitive**: built-in modes (Code, Architect, Ask, Debug, Orchestrator) plus user-authored **custom modes** with role definitions, tool-group permissions, file-regex restrictions, and mode-scoped rules. Orchestrator mode delegates to sub-modes via `new_task` with parent-child task hierarchies.
- **Contents inspected:** Official docs "Customizing Modes" (https://roocodeinc.github.io/Roo-Code/features/custom-modes/, fetched 2026-10-10, 1117-line page): mode properties (slug/name/description/roleDefinition/whenToUse/groups/customInstructions), YAML (`custom_modes.yaml`/`.roomodes`) and JSON formats, import/export with rules packaging, **Roo Code Marketplace** for one-click mode installs, sticky models per mode, Orchestrator. Secondary: Roo Code CLI/Roomote (agentlist); `.roo/` conventions (codyswanngt ROO_CODE_OFFICIAL_DOCS: `.roo/mcp.json`, `.roorules`/`.clinerules`/`.cursorrules`/`.windsurfrules` compat, `.roo/rules-{mode-slug}/`).
- **Actual capabilities:**
  - **Custom modes:** global (`custom_modes.yaml`) or project (`.roomodes`); `groups` tool allowlists with `fileRegex` restrictions; `whenToUse` for orchestrated selection; import/export as single YAML incl. rules; marketplace distribution.
  - **Rules files:** `.roorules` (primary), `.clinerules` fallback, `.cursorrules`/`.windsurfrules` read for compatibility; mode-scoped `.roo/rules-{mode-slug}/` directories; `.rooignore`.
  - **Instruction files:** custom instructions (global/workspace/mode-specific) — no dedicated ROO.md; AGENTS.md honored via compat reads (secondary).
  - **Slash commands:** `/code`, `/architect`, `/ask` mode switches (secondary).
  - **Subagents:** Orchestrator → `new_task(mode, message)` delegation; hierarchical tasks (rootTaskId/parentTaskId/childTaskId); each subtask own context window.
  - **MCP:** `.roo/mcp.json` (project), user-level settings; stdio + SSE; `alwaysAllow` per-server tool lists.
  - **Marketplace:** Roo Code Marketplace for modes (official docs); (extensions distributed via VS Code marketplace).
  - **Permission systems:** per-mode tool groups; file-regex edit restrictions; human-in-the-loop approvals.
  - **Session state:** checkpoints; task history.
  - **Background execution:** not documented as first-class — **Unverified**.
  - **Headless operation:** Roo Code CLI exists (multi-mode CLI agent per awesome list) — **Partially verified**.
  - **API/SDK access:** Roomote (single-tenant cloud coding agent, self-hosted or hosted) — **Partially verified** (secondary).
  - **Model routing:** sticky models per mode; multi-model via provider settings.
- **Usage domain:** IDE agent workflows with strict role separation (architect vs implementer vs reviewer).
- **Integration method:** VS Code marketplace install; `.roomodes`/`.roo/` repo conventions; mode YAML import/export.
- **Compatibility:** Native (own modes/rules system). **Documented adapter or port** from Cline (fork lineage; `.clinerules` compat). **Shared standard or protocol** for MCP. Reads `.cursorrules`/`.windsurfrules` (compat).
- **Dependencies:** VS Code; model provider keys.
- **Availability:** Open source (repo public); VS Code marketplace.
- **Maintenance:** Active.
- **License:** Apache-2.0 (cross-referenced; not re-verified this pass).
- **Limitations:** Mode system is Roo-specific (no portable subagent-file standard); marketplace limited to modes (vs Claude Code's full plugin bundles).
- **Related resources:** Cline (upstream fork lineage); Kilo Code (related); Roomote; Roo Code CLI.
- **Sources:**
  - https://roocodeinc.github.io/Roo-Code/features/custom-modes/ (official docs, fetched 2026-10-10)
  - https://roo.dev/docs (official docs root, cited)
  - https://github.com/codyswanngt/saasstarter/blob/HEAD/docs/ROO_CODE_OFFICIAL_DOCS.md (secondary, 2025)
  - https://github.com/clemens865/lazy-fetch/blob/HEAD/research/frameworks/cline-roo-code.md (secondary)
  - https://github.com/agentlistio/awesome-agent-list (secondary, Roomote/Roo CLI)
- **Verification date:** 2026-10-10
- **Confidence:** High on custom modes/marketplace/rules (official docs). Medium on CLI/Roomote (secondary).

---

## 11. Aider

### Resource record: Aider
- **Resource name:** Aider
- **Canonical identity:** `Aider-AI/aider` — open-source AI pair-programming agent for the terminal. Command: `aider`.
- **Category:** Ready-made coding agent (pair-programmer; diff/commit-centric — not a fully autonomous agent)
- **Type:** AGENT (lightweight extension surface: conventions files, config, watch mode)
- **Official URL:** https://aider.chat
- **Description:** The leading open-source AI pair programmer: lives in the terminal, edits files directly, treats git as source of truth (every AI change is a clean attributed commit). Chat modes: code, ask, architect (two-model plan/edit split), help. Works with Anthropic/OpenAI/Gemini/DeepSeek or local models (Ollama).
- **Contents inspected:** Secondary only this pass (aider.chat docs referenced via qwickapps/ai-sdlc-workflows: https://aider.chat/docs/usage/conventions.html; the-focus-ai interoperability report §2.8; mindcockpit aider-guide). No primary fetch (docs site not verbatim-available; aider.chat referenced consistently).
- **Actual capabilities:**
  - **Instruction/convention files:** `CONVENTIONS.md` loaded via `--read` flag; `.aider.conf.yml` (`read:` directive for always-loaded files); repo-map for context.
  - **Config standard:** `.aider.conf.yml` (model selection, conventions, settings).
  - **Permissions:** git-centric review (diffs shown; commits attributed); `.aiderignore` to block sensitive files.
  - **Session state:** git history as state; chat history; cost tracking.
  - **Background execution:** watch-files mode (drive Aider from comments in any IDE); scripting for batch/CI use — **Partially verified** (secondary).
  - **Headless operation:** scriptable batch/CI use — **Partially verified**.
  - **Model routing:** `--model` flag; architect mode splits reasoning vs editor models.
  - **Skills/plugins/hooks/MCP/subagents/marketplace:** none native. Community wrappers (`aider-mcp-server`, `mcpm-aider`) expose Aider *as* an MCP server (experimental). No plugin/marketplace/hook system.
  - **External tool integrations:** git; linters (auto-lint loop); test loops (auto-test until pass); voice/image input (secondary).
- **Usage domain:** Pair-programming edits with tight git discipline; local-model coding.
- **Integration method:** CLI flags + YAML config; convention markdown files.
- **Compatibility:** **Reference-only** for SKILL.md-style skills (consumes them only as inlined convention text via adapters, per agent-jump-start: generates `CONVENTIONS.md` with inline skill summaries for Aider). **Shared standard or protocol**: AGENTS.md-style instruction files via `--read`. **Custom integration required** for MCP (community wrappers only).
- **Dependencies:** Python (pip install); model API keys or local models.
- **Availability:** Open source.
- **Maintenance:** Active (~47.7k stars per awesome list, 2026).
- **License:** Apache-2.0 (cross-referenced).
- **Limitations:** No native skills/hooks/plugins/subagents/marketplace; no native MCP client; safety is advisory (model-read conventions), not programmatic enforcement.
- **Related resources:** OpenCode/Claude Code/Codex (full agents users graduate to); agent-jump-start (renders Aider conventions from canonical spec).
- **Sources:**
  - https://aider.chat (official, cited; docs page https://aider.chat/docs/usage/conventions.html via secondary)
  - https://github.com/the-focus-ai/claude-marketplace/blob/HEAD/reports/2026-02-13-portable-ai-coding-skills-cross-tool-interoperability.md (secondary)
  - https://github.com/cortesimone/agent-jump-start (secondary)
  - https://github.com/qwickapps/ai-sdlc-workflows (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified** — consistent secondary evidence; no primary fetch this pass).

---

## 12. Amp

### Resource record: Amp
- **Resource name:** Amp (Amp Code)
- **Canonical identity:** Coding agent by **Amp Inc.** — spun out of Sourcegraph on 2026-12-02 (secondary: techstackups). Surfaces per current official manual: **Web (ampcode.com), macOS & iOS apps, Terminal CLI** (`amp`); concepts: **Threads** (persistent shareable conversations), **Orbs** (per-thread cloud machines), **Runners** (headless `amp --no-tui --runner-id`), **Puck** (agent launcher/coordinator).
- **Category:** Ready-made coding agent (multi-model, cloud-threaded)
- **Type:** AGENT + extension host (skills, commands, hooks, MCP, plugins, subagents[partial])
- **Official URL:** https://ampcode.com (manual: https://ampcode.com/manual; company: https://sourcegraph.com/amp)
- **Description:** Sourcegraph's former agentic product, rebuilt and spun out as an independent company. Differentiators: **model routing by mode, not model picker** (Smart/Deep/Oracle modes route across GPT/Claude/Gemini-class models; user can't directly swap arbitrary models), pass-through (at-cost) pricing, and cloud threads/orbs that keep working with the laptop closed. Rebuilt May 2026 per secondary.
- **Contents inspected:** Official manual intro (https://ampcode.com/manual, fetched 2026-10-10): multi-model claim, Orbs, web/macOS/iOS/CLI surfaces, Threads, Puck. Secondary: gald3r Amp PLATFORM_SPEC (verified 2026-06-02 against the manual: commands/rules/skills/hooks/MCP/plugins native; subagents partial); jaiskills amp-harness deep dive (threads/orbs/runners/subagents/inter-agent messaging; AGENTS.md instruction-file conventions with glob frontmatter); ai-harness-deepdive amp profile (`.agents/skills/` project, `~/.config/agents/skills/` XDG shared bucket with Kimi CLI/Replit).
- **Actual capabilities (Partially verified — secondary-anchored, manual-confirmed on surfaces):**
  - **Instruction files:** `AGENTS.md` primary (also `AGENT.md`, legacy `CLAUDE.md`); locations: cwd + parents to `$HOME`, subtree AGENTS.md, `~/.config/amp/AGENTS.md`, `~/.config/AGENTS.md`, system `/etc/ampcode/AGENTS.md` (Linux); glob-scoped instructions via YAML frontmatter (`globs:`); `@path` mentions; auto-generation from `.cursorrules`/`.windsurfrules`/etc.
  - **Skills:** native SKILL.md — project `.agents/skills/`, also discovers `.claude/skills/` as fallback, global `~/.config/agents/skills/` (shared bucket); `allowed-tools` honored.
  - **Slash commands:** custom slash commands native (CLI).
  - **Subagents:** main agent **auto-spawns** subagents (up to 7 parallel; inter-agent messaging); users **cannot** author standalone subagent definition files (partial); plugins can simulate custom agents/modes via experimental API.
  - **Hooks:** lifecycle hooks native (two surfaces per PLATFORM_SPEC; exact events **Unverified** here).
  - **MCP:** full MCP server support (VS Code `settings.json` `amp.mcpServers` for editor; CLI config).
  - **Plugins:** plugin system present (experimental API for agent/mode simulation).
  - **Threads/sessions:** persistent, shareable threads (`@T-<id>` refs); orbs = remote execution machines; runners = headless execution.
  - **Background execution:** orbs (close laptop, resume anywhere); runners headless; cron-style scheduling (secondary).
  - **Headless operation:** `amp --no-tui` runner mode (secondary).
  - **Model routing:** mode-based routing across providers (no BYOK arbitrary model swap); "Oracle" second-opinion reasoning model.
  - **API/SDK access:** not documented in inspected material — **Unverified**.
- **Usage domain:** Professional teams wanting multi-model routing without model management; async/cloud agent workflows.
- **Integration method:** `curl -fsSL https://ampcode.com/install.sh | bash` or `npm install -g @ampcode/cli`; AGENTS.md + `.agents/` conventions.
- **Compatibility:** **Shared standard or protocol** for AGENTS.md, SKILL.md, MCP (`~/.config/agents/skills/` shared bucket with Kimi CLI). Editor-surface status **Unresolved**: Feb 2026 "The Coding Agent Is Dead" post announced VS Code/Cursor extension shutdown (self-destruct 2026-03-05) and CLI-only pivot (techstackups, secondary), but the current manual (primary, 2026-10-10) presents web + macOS/iOS apps + CLI as first-class — later evolution not reconciled.
- **Dependencies:** Amp account; subscription (free tier $10/day per secondary; Enterprise markup).
- **Availability:** Available (web/CLI/apps).
- **Maintenance:** Active (weekly-scale changes per secondary).
- **License:** Proprietary.
- **Limitations:** No user-authored subagent files; model choice is mode-mediated (no arbitrary model picker); threads live on vendor servers (no local-only mode per secondary).
- **Related resources:** Sourcegraph Cody (predecessor product); Kimi CLI (shares skills bucket); OpenCode (alternative).
- **Sources:**
  - https://ampcode.com/manual (official, fetched 2026-10-10)
  - https://github.com/gald3r-labs/gald3r_platform_cursor/blob/HEAD/platforms/amp/PLATFORM_SPEC.md (secondary, manual-verified 2026-06-02)
  - https://github.com/jairotorregrosa/jaiskills/blob/HEAD/skills/prompting/metaprompt/references/amp-harness.md (secondary)
  - https://github.com/imarash/ai-harness-deepdive/blob/HEAD/docs/agents/amp.md (secondary)
  - https://techstackups.com/comparisons/coding-agent-harness-comparison-2026/ (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** High on identity/surfaces/thread model (official manual). Medium (**Partially verified**) on extension primitives (secondary). **Unresolved**: current editor-integration status vs the Feb–Mar 2026 CLI-only pivot reports.

---
## 13. Factory Droid (Factory AI)

### Resource record: Factory Droid
- **Resource name:** Factory Droid ("Droid")
- **Canonical identity:** Flagship agent of **Factory AI** (factory.ai) — enterprise agent-fleet platform. Command: `droid`.
- **Category:** Ready-made coding agent (enterprise fleet; terminal/IDE/web/cloud)
- **Type:** AGENT + extension host (skills, hooks, MCP, custom droids/subagents, missions)
- **Official URL:** https://factory.ai (docs: https://docs.factory.ai)
- **Description:** Enterprise-oriented agentic platform: configurable **Droids** (coding, review, incident, release roles) run in the terminal (Droid CLI), IDEs (VS Code, JetBrains), web, Slack, and cloud **Missions** (multi-agent planning/delegation/validation). Model-flexible (Claude, GPT, Gemini). Organizational context via knowledge-graph indexing (GitHub/Jira/Slack/Drive/wiki/CI).
- **Contents inspected:** Secondary only this pass: hindsight installer docs (hook/MCP/skill paths: `~/.factory/hooks.json`, `~/.factory/mcp.json`, `~/.factory/skills`; hook protocol matches Claude Code's); RealPython Droid tool page (missions, custom droids, skills, `droid exec` headless, model routing, integrations); agentscamp factory.md (Droid CLI/IDE/web surfaces, AGENTS.md grounding); awesome-vibe-coding factory-droid.md (configurable droids, CLI+CI-native, SSO/SAML/SCIM, on-prem).
- **Actual capabilities (Partially verified — secondary, multi-source):**
  - **Instruction files:** `AGENTS.md` at repo root as the Droid instruction manual (style rules, framework prefs, architecture constraints); autonomy levels 1–5 selectable in AGENTS.md.
  - **Skills:** reusable procedures packaged as **Skills** (user `~/.factory/skills`).
  - **Custom agents:** **Custom Droids** — specialized subagents; multiple named droids per org workflow.
  - **Hooks:** `~/.factory/hooks.json` (user scope) — 4 hook registrations in the hindsight installer incl. cancellation-safe `Notification` write-back; hook protocol matches Claude Code (`session_id`/`transcript_path`/`cwd` in, `hookSpecificOutput.additionalContext` out); Droid does not emit `Stop` after a cancelled turn.
  - **MCP:** `~/.factory/mcp.json` (`mcpServers.hindsight` pattern); open MCP standard.
  - **Subagents/multi-agent:** **Missions** (multi-agent planning, delegation, validation).
  - **Session state:** cloud missions + local sessions (details **Unverified**).
  - **Background execution:** Missions run async in cloud; "Droid executable" runner for automation pipelines.
  - **Headless operation:** `droid exec` for scripts, CI jobs, PR checks (RealPython).
  - **Model routing:** routes tasks to Anthropic/OpenAI/Google models; Droid Core free pool of open-weight models.
  - **Permission systems:** autonomy levels (Suggest → Write → PR → Deploy → full lifecycle); enterprise SSO/SAML/SCIM, on-prem/air-gapped options.
  - **API/SDK access:** not captured — **Unverified**.
  - **External tool integrations:** GitHub/GitLab, Jira/Linear, Slack, PagerDuty; VS Code/Cursor/Windsurf/JetBrains/Zed alongside.
- **Usage domain:** Engineering organizations standardizing agentic workflows; enterprise governance.
- **Integration method:** Factory account login; `droid` CLI; docs.factory.ai.
- **Compatibility:** **Shared standard or protocol** for AGENTS.md, SKILL.md, MCP; hook protocol wire-compatible with Claude Code (**Documented adapter or port** per hindsight installer). No evidence of a public plugin marketplace — **Unverified**.
- **Dependencies:** Factory account; paid plans (Pro $20/mo, Plus $100/mo, Max $200/mo; Teams/Business/Enterprise custom — per secondary, Sep 2026).
- **Availability:** Commercial, no free tier (Droid Core free open-weight pool excepted).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Proprietary/paid; extension-system details (skills format, custom-droid schema) not verified against primary docs this pass.
- **Related resources:** Devin (competitor); GitHub Copilot (competitor); hindsight (integration example).
- **Sources:**
  - https://docs.factory.ai (official, cited; not fetched — JS)
  - https://github.com/mabaty/hindsight/blob/HEAD/hindsight-docs/docs-integrations/coding-agents.md (secondary)
  - https://REALPYTHON.COM/ref/ai-coding-tools/droid/ (secondary)
  - https://github.com/imtiazrayhan/agentscamp/blob/HEAD/src/content/tools/factory.md (secondary)
  - https://github.com/awesome-vibe-coding/awesome-vibe-coding/blob/HEAD/content/tools/factory-droid.md (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified** — consistent secondary evidence; primary docs not fetched).

---

## 14. Kimi Code (Moonshot AI)

### Resource record: Kimi Code CLI
- **Resource name:** Kimi Code CLI
- **Canonical identity:** `MoonshotAI/kimi-code` — Moonshot AI's terminal coding agent. Executable: `kimi`. **Correction:** the older `MoonshotAI/kimi-cli` ("Kimi CLI", Apache-2.0) is now a **legacy alias being wound down** — its README states it is "evolving into Kimi Code CLI" with automatic config/session migration. The live product is **Kimi Code CLI** (MIT).
- **Category:** Ready-made coding agent (terminal TUI; multi-provider)
- **Type:** AGENT + extension host (skills, plugins, custom agents, hooks, MCP, subagents, themes)
- **Official URL:** https://www.kimi.com/code/ (repo: https://github.com/MoonshotAI/kimi-code; docs: https://moonshotai.github.io/kimi-code/en/)
- **Description:** MIT-licensed terminal coding agent: reads/edits code, runs shell commands, searches files, fetches web pages, chooses next steps from feedback. Works out-of-box with Kimi models; configurable to other providers. Ships as desktop + CLI + IDE plugins under one subscription. Shell-command mode (Ctrl-X), agent swarm (subagents), ACP/MCP.
- **Contents inspected:** Official README (https://github.com/MoonshotAI/kimi-code, via search-verified content, 2026-10): install (`curl -fsSL https://code.kimi.com/kimi-code/install.sh`), `/login` (Kimi Code OAuth or Moonshot Open Platform key), quick start. Legacy repo notice (https://github.com/moonshotai/kimi-cli/blob/HEAD/README.md): "A legacy alias of kimi-cli, not the new Kimi Code CLI" / evolution notice. Secondary: scriptbyai Kimi CLI guide (skill paths, plugin manifest, built-in skills); rueclaw review (monorepo: CLI/TUI, web UI, VS Code extension, server, ACP adapter, SDK, plugin manifests); openspec SKILL.md (validated against `kimi 0.34.0`: permission modes, MCP timeout config).
- **Actual capabilities (Partially verified — README primary; extension details secondary):**
  - **Skills:** Agent Skills from SKILL.md — user `$KIMI_CODE_HOME/skills/`, `~/.agents/skills/`; project `.kimi-code/skills/`, `.agents/skills/`; built-in skill-commands: `/mcp-config`, `/custom-theme`, `/update-config`, `/check-kimi-code-docs`, `/import-from-cc-codex` (imports Claude Code/Codex instructions, skills, MCP settings), `/sub-skill`.
  - **Plugins:** `kimi.plugin.json` manifest (also `.kimi-plugin/plugin.json` seen in review); package Agent Skills, custom agents, MCP server definitions, lifecycle hooks, system instructions, slash commands; `/plugins` manager (installed/official/curated/custom); `/reload` to activate.
  - **Custom agents:** custom agents supported (plugin-packaged); agent profiles selectable; built-in subagent types (coder, explore, plan per one skill doc).
  - **Subagents:** agent swarm (up to 300 sub-agents per one secondary — treat as **Unverified** magnitude); `context: fork` not supported (ai-harness-deepdive).
  - **Hooks:** lifecycle hooks in plugins (secondary).
  - **MCP:** MCP client (OAuth + bearer); `/mcp-config` built-in.
  - **Slash commands:** built-ins listed above; custom commands via plugins.
  - **Instruction files:** not captured as a dedicated file — `/import-from-cc-codex` suggests cross-tool instruction import — **Partially verified**.
  - **Permission systems:** `default_permission_mode` (auto et al.); sensitive-file detection; per-turn approvals.
  - **Session state:** session management (continue/resume by ID); session storage; replay; goals; checkpoints (per review).
  - **Background execution:** swarm/subagents; background mode via wrapper skills — **Partially verified**.
  - **Headless operation:** `--print`/`-p` non-interactive (auto-approves; exit codes 0/1/75), `--quiet`, JSONL streaming output — **Partially verified** (secondary skill docs).
  - **Model routing:** multi-provider (Kimi default; OpenAI/Anthropic/Gemini/Vertex configurable); `/login` OAuth.
  - **API/SDK access:** client/SDK packages in monorepo; ACP adapter; server package (Fastify REST/WebSocket `/api/v1`).
  - **External tool integrations:** VS Code extension (`moonshot-ai.kimi-code`); JetBrains/Zed via ACP; MCP ecosystem.
- **Usage domain:** Cost-effective terminal coding with Moonshot models; multi-provider terminal agent.
- **Integration method:** install script / npm `@moonshot-ai/kimi-code` / Homebrew `kimi-code`; `/plugins` in-TUI.
- **Compatibility:** Native (own plugin/skill system). **Shared standard or protocol** for SKILL.md and MCP; `~/.agents/skills` shared bucket. **Documented adapter or port**: `/import-from-cc-codex` imports Claude Code/Codex assets (**Partially verified**). Shares `~/.config/agents/skills/` XDG bucket with Amp (secondary).
- **Dependencies:** Kimi Code OAuth or Moonshot API key (or configured provider); Node 22.19+ for npm path (or dependency-free install script).
- **Availability:** Open source (MIT), actively developed.
- **Maintenance:** Active (releases ~0.28–0.34 in 2026 window).
- **License:** MIT (Kimi Code CLI). Legacy Kimi CLI: Apache-2.0.
- **Limitations:** Legacy `kimi-cli` → `kimi-code` migration in progress (naming confusion in third-party docs); swarm-scale claims unverified.
- **Related resources:** MoonshotAI/kimi-cli (legacy alias — Historical); Kimi Code desktop/IDE plugins.
- **Sources:**
  - https://github.com/MoonshotAI/kimi-code (official README, search-verified 2026-10)
  - https://github.com/moonshotai/kimi-cli/blob/HEAD/README.md (official legacy notice)
  - https://moonshotai.github.io/kimi-code/en/ (official docs, cited)
  - https://www.scriptbyai.com/kimi-cli/ (secondary)
  - https://github.com/rueclaw/public-data/blob/HEAD/reviews/kimi-code.md (secondary review)
  - https://github.com/vicle1908/openspec-store/blob/HEAD/./.hermes/skills/autonomous-ai-agents/kimi-code/SKILL.md (secondary, binary-validated)
- **Verification date:** 2026-10-10
- **Confidence:** High on identity/install/legacy-alias correction (official READMEs). Medium (**Partially verified**) on plugin/skill/hook internals (secondary).

---

## 15. Pi (Earendil Works)

### Resource record: Pi coding agent
- **Resource name:** Pi
- **Canonical identity:** `earendil-works/pi` — open-source minimal extensible agent harness by Mario Zechner / Earendil Works. npm: `@earendil-works/pi-coding-agent`. Site/docs: https://pi.dev.
- **Category:** Ready-made coding agent + framework for building agents (harness)
- **Type:** AGENT + extension host (TypeScript extensions, skills, prompt templates, themes, packages) + SDK/RPC
- **Official URL:** https://pi.dev (repo: https://github.com/earendil-works/pi)
- **Description:** "A minimal, extensible agent harness that you can make your own." TypeScript monorepo (pi-ai, pi-agent-core, pi-coding-agent, pi-tui). Customization = TypeScript **extensions** + **skills** + **prompt templates** + **themes**, bundled as **Pi packages** shared via npm or git. Ships with strong defaults but deliberately *no* built-in subagents or plan mode ("ask Pi to build what you want, or install a package").
- **Contents inspected:** Official README (via search-verified content): install (`curl -fsSL https://pi.dev/install.sh | sh`, `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`, Node 22.19+), modes, extension model. Official packages doc (https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md, via search): package manifest, resource selection (extensions/skills/prompts filters), `pi config` scopes. Secondary: harness-knowledge-base pi usage reference (modes table, tools, providers, AGENTS.md/CLAUDE.md discovery, `~/.pi/agent` config); bacnh85/pi-extensions (community package ecosystem: router, checkpoint, cron, selfskills); Wikipedia Pi (AI agent) article (identity/history: badlogic → Earendil Works, MIT, pi.dev).
- **Actual capabilities:**
  - **Extensions:** TypeScript extensions (first-class; host supplies `@earendil-works/pi-*` packages + typebox); add tools, skills, integrations.
  - **Skills:** SKILL.md skills as package resources.
  - **Prompt templates:** prompt-template resources in packages.
  - **Themes:** theme resources.
  - **Packages:** Pi package manifest; install from npm (`npm:@example/pi-tools`) or git; per-resource include/exclude filters (`extensions`, `skills`, `prompts`); `pi config` to enable/disable (personal vs project `--local` scopes).
  - **Instruction files:** `AGENTS.md` and `CLAUDE.md` context discovery (secondary).
  - **Slash commands:** built-in (`/login`, `/update`, `/reload`, `/router-config`, etc. per community packages).
  - **Subagents:** none built-in (by design) — **Verified** (official README).
  - **Hooks:** not documented as a primitive — **Unverified**.
  - **MCP:** community packages add MCP support (oh-my-pi fork `omp` adds MCP; bacnh85 ecosystem) — core status **Partially verified**.
  - **Session state:** append-only JSONL sessions; context-safe `/reload`; session replay.
  - **Background execution:** not a built-in primitive — **Unverified**.
  - **Headless operation:** print mode (`pi -p`), JSON mode (`pi --mode json`), long-lived RPC (`pi --mode rpc`, JSON-line RPC over stdio) — **Partially verified** (secondary).
  - **Model routing:** provider/model selection; community router packages (OpenAI-compatible routers).
  - **API/SDK access:** Pi TypeScript SDK (in-process Node.js integration); RPC mode; OpenClaw integration cited as real-world embedding.
  - **External tool integrations:** Slack bot (in toolkit scope); community bridges (e.g., pi-agy → Antigravity CLI delegation).
- **Usage domain:** Hackable minimal harness for developers who want to own the agent loop; embedding via SDK/RPC.
- **Integration method:** `pi.dev/install.sh` or npm; `pi config`; package install from npm/git.
- **Compatibility:** Native (TypeScript extension API). **Shared standard or protocol** for SKILL.md and AGENTS.md/CLAUDE.md discovery. **Unresolved**: relationship to the Rust rewrite (`noeljackson/pi` — "native Rust CLI coding agent" claiming cutover from the TS monorepo; could be a fork — not reconciled against earendil-works/pi this pass).
- **Dependencies:** Node.js 22.19+; provider keys or `/login` subscription.
- **Availability:** Open source; installer + npm.
- **Maintenance:** Active (docs at pi.dev/docs/latest; community package ecosystem).
- **License:** MIT (per Wikipedia; cross-referenced).
- **Limitations:** No built-in subagents/plan mode; TypeScript-only extension authoring; smaller ecosystem than Claude Code/Cursor.
- **Related resources:** oh-my-pi / OH-MY-PI (can1357 — enhanced fork/standalone, TS/Rust monorepo); OpenClaw (integration); noeljackson/pi (possible Rust rewrite — Unresolved).
- **Sources:**
  - https://github.com/earendil-works/pi (official repo; README + packages/coding-agent/docs/packages.md, search-verified 2026-10)
  - https://pi.dev (official site/docs, cited)
  - https://en.wikipedia.org/wiki/Pi_(AI_agent) (identity/history)
  - https://github.com/minfengyuan/harness-knowledge-base/blob/HEAD/skills/pi-coding-agent/references/core/usage.md (secondary)
  - https://github.com/bacnh85/pi-extensions (secondary, community ecosystem)
  - https://github.com/krippergaulana-dot/hapi/blob/HEAD/docs/guide/agents.md (secondary, `pi --mode rpc`)
- **Verification date:** 2026-10-10
- **Confidence:** High on identity/extension model/modes (official docs). Medium on headless/RPC/AGENTS.md specifics (secondary). **Unresolved**: Rust-rewrite relationship.

---
## 16. Emerging / other coding agents (uncovered in this sweep)

### Resource record: Qwen Code (Alibaba)
- **Resource name:** Qwen Code
- **Canonical identity:** `QwenLM/qwen-code` — Alibaba's official CLI coding agent. Command: `qwen`. npm: `@qwen-code/qwen-code`. Site: https://qwen.ai/qwencode.
- **Category:** Ready-made coding agent (open-source, multi-protocol)
- **Type:** AGENT + extension host (skills, hooks, subagents, MCP, IDE plugins, SDKs)
- **Official URL:** https://github.com/QwenLM/qwen-code (docs: https://qwenlm.github.io/qwen-code-docs/)
- **Description:** Standalone multi-provider terminal coding agent. **Lineage:** fork of Google's Gemini CLI v0.8.2; from v0.1 diverged into independent multi-protocol development ("If you know Claude Code, you already know Qwen Code" per its README). Chases Claude Code feature parity with differentiators: open model+framework, multi-protocol providers, Agent Arena, daemon mode, IM channels.
- **Contents inspected:** Secondary only (ai-tooling evaluation with README-grounded claims; josvaal research with README + docs citations; ai-harness-deepdive profile). No primary README fetch this pass.
- **Actual capabilities (Partially verified):** interactive TUI (`qwen`); headless one-shot (`qwen -p`) for CI/CD; daemon/ACP server (`qwen serve`, multi-client over HTTP+SSE, experimental); IM-bot channels (`qwen channel` → Telegram/DingTalk/WeChat/Feishu); SubAgents; **Agent Teams**; Auto-Memory; Auto-Skills; **Hooks** (native `~/.qwen/settings.json` hooks per hindsight installer); MCP client; Plan Mode; LSP integration; sandbox; git-worktree; computer-use/desktop automation; IDE plugins (VS Code, JetBrains, Zed); desktop GUI; SDKs (TypeScript, Python, Java); skills in `.qwen/skills/` (user `~/.qwen/skills/`; built-ins incl. `bugfix`, `codegraph`, `create-issue`); multi-protocol (OpenAI/Anthropic/Gemini/Qwen APIs; Ollama/vLLM local; runtime switch via `/auth`).
- **Usage domain:** Open-source Claude-Code-parity agent; Qwen-model optimization.
- **Integration method:** npm `@qwen-code/qwen-code`; install script.
- **Compatibility:** **Documented adapter or port** from Gemini CLI (fork lineage). **Shared standard or protocol** for AGENTS.md, SKILL.md, MCP.
- **Dependencies:** Alibaba Cloud Coding Plan / Qwen API or any configured provider.
- **Availability:** Open source (~27.7k stars per awesome list).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Limitations:** Young fork; some capabilities (daemon/IM channels) experimental.
- **Related resources:** Gemini CLI (upstream fork base); ZCode (zai-org, GLM's harness — mentioned in research).
- **Sources:**
  - https://github.com/QwenLM/qwen-code (official, cited; README claims via secondary)
  - https://github.com/mattbutlerengineering/ai-tooling/blob/HEAD/evaluations/qwen-code.md (secondary, README-grounded)
  - https://github.com/josvaal/opencode-droxon-harness/blob/HEAD/features/qwen-model-family-support/research/qwen-code-findings.md (secondary)
  - https://github.com/imarash/ai-harness-deepdive/blob/HEAD/docs/agents/qwen-code.md (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified** — README-grounded secondary claims; primary not fetched).

### Resource record: Crush (Charm)
- **Resource name:** Crush
- **Canonical identity:** `charmbracelet/crush` — Charm (Charmbracelet) terminal coding agent. Go single binary.
- **Category:** Ready-made coding agent (TUI-first, multi-provider BYOK)
- **Type:** AGENT + extension host (MCP, LSP, Agent Skills)
- **Official URL:** https://github.com/charmbracelet/crush
- **Description:** "The glamorous AI coding agent for your terminal." Single Go binary hosting Bubble Tea TUI + agent loop; fully BYOK (no vendor account); provider/model catalog (Catwalk) auto-updates. First-class **LSP integration** (spawns language servers per project for type-aware navigation). Local SQLite sessions.
- **Contents inspected:** Secondary (jexp/agentic-engineering crush profile; multica feature request with capability list; crush skill cards citing upstream README + raw README extract showing `crush.json` LSP/MCP config schema).
- **Actual capabilities (Partially verified):** MCP (stdio/http/sse; env expansion); LSP config in `crush.json`/`$HOME/.config/crush/crush.json` (`$schema: https://charm.land/crush.json`); Agent Skills (open standard); multi-model mid-session switching; sessions/contexts per project; `--yolo` auto-accept; desktop notifications on permission prompts.
- **Usage domain:** Terminal-native multi-provider coding; LSP-rich code intelligence.
- **Integration method:** `brew install charmbracelet/tap/crush`, `npm i -g @charmland/crush`, `go install`, release binaries.
- **Compatibility:** **Shared standard or protocol** for MCP and Agent Skills. Runs anywhere Go runs (macOS/Linux/Windows/Android/BSDs).
- **Dependencies:** Provider API keys (BYOK).
- **Availability:** Open source (~22–28k stars across trackers).
- **Maintenance:** Active (fast release cadence; v0.64 Apr 2026 per secondary).
- **License:** **Unresolved** — sources disagree (MIT per jexp profile; FSL-1.1-MIT per multica issue). Not verified against repo LICENSE this pass.
- **Limitations:** No plugin marketplace/hook system documented; config is JSON-file only.
- **Related resources:** OpenCode (similar TUI-agent space); Catwalk (model catalog).
- **Sources:**
  - https://github.com/charmbracelet/crush (official, cited)
  - https://github.com/jexp/agentic-engineering/blob/HEAD/research/coding-agents/crush.md (secondary)
  - https://github.com/multica-ai/multica/issues/4642 (secondary)
  - https://github.com/agentskillexchange/skills/blob/HEAD/skills/crush-agentic-ai-coding-cli-charmbracelet/SKILL.md (secondary)
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified**). License **Unresolved**.

### Resource record: Kilo Code
- **Resource name:** Kilo Code
- **Canonical identity:** `Kilo-Org/kilocode` — agentic engineering platform (VS Code extension lineage; now with CLI). Command (CLI): per awesome lists, Kilo Code CLI.
- **Category:** Ready-made coding agent (IDE + CLI)
- **Type:** AGENT + extension host (modes, skills, MCP, checkpoints)
- **Official URL:** https://github.com/Kilo-Org/kilocode
- **Description:** Agentic engineering platform with orchestrator mode, 100+ LLMs, skills, and checkpointing; ships a CLI in addition to the IDE extension.
- **Contents inspected:** Awesome-list entries only (nilline/dinkaass). No docs fetched.
- **Actual capabilities:** Orchestrator mode; skills; checkpointing; multi-model — **Unverified** beyond list blurbs.
- **Usage domain:** IDE + CLI agentic engineering.
- **Integration method:** VS Code marketplace; CLI binary — **Unverified**.
- **Compatibility:** **Unverified**.
- **Dependencies:** Model provider access — **Unverified**.
- **Availability:** Open source (~26–27k stars per lists).
- **Maintenance:** Active per lists.
- **License:** Not verified.
- **Limitations:** Not researched in depth this pass.
- **Related resources:** Roo Code; Cline (lineage-adjacent).
- **Sources:** https://github.com/nilline/awesome-cli-coding-agents; https://github.com/dinkaass/awesome-cli-coding-agents (secondary lists).
- **Verification date:** 2026-10-10
- **Confidence:** Low (**Unverified** — list-level evidence only). More work warranted.

### Resource record: Goose (Block)
- **Resource name:** Goose
- **Canonical identity:** `block/goose` (listed as `aaif-goose/goose` in one list — canonical owner **Unverified**; Block's open-source agent). 
- **Category:** Ready-made coding agent (local-first, extensible)
- **Type:** AGENT + extension host (MCP-centric)
- **Official URL:** https://github.com/block/goose (to verify)
- **Description:** Local, extensible agent that can execute, edit, and test; designed to run on-device and integrate with MCP (~51.8k stars per awesome list).
- **Contents inspected:** Awesome-list entries only.
- **Actual capabilities:** On-device execution; MCP integration — **Unverified** beyond blurbs.
- **Usage domain:** Local-first agentic coding.
- **Integration method:** Not verified.
- **Compatibility:** **Unverified**.
- **Dependencies:** Not verified.
- **Availability:** Open source.
- **Maintenance:** Active per lists.
- **License:** Apache-2.0 (commonly cited; not verified).
- **Limitations:** Not researched in depth this pass.
- **Related resources:** —
- **Sources:** https://github.com/nilline/awesome-cli-coding-agents (secondary list).
- **Verification date:** 2026-10-10
- **Confidence:** Low (**Unverified**). More work warranted.

### Resource record: Continue.dev (Continue CLI + Continue Hub)
- **Resource name:** Continue.dev
- **Canonical identity:** `continuedev/continue` — open-source AI code assistant (IDE extensions + CLI).
- **Category:** Ready-made coding agent / assistant platform
- **Type:** AGENT + extension host (Hub marketplace, MCP, skills, slash commands)
- **Official URL:** https://github.com/continuedev/continue (docs: https://docs.continue.dev)
- **Description:** Open-source terminal + IDE extension for multi-model coding with local/privacy focus. **Continue Hub** = marketplace for sharing custom-built assistants and building blocks (launched with Continue 1.0). Full MCP integration (Docker partnership for containerized MCP blocks). Recent agent-skills support.
- **Contents inspected:** Secondary (the-focus-ai interoperability report §2.7; awesome lists). Docs URLs cited but not fetched.
- **Actual capabilities (Partially verified):** Continue Hub marketplace (assistants/building blocks); `~/.continue/config.json` (`mcpServers`); `.continuerules`; custom slash commands + prompt templates (MCP prompts exposed as slash commands); agent skills; multi-model providers; local-model focus.
- **Usage domain:** Privacy-conscious local/multi-model coding assistance.
- **Integration method:** VS Code/JetBrains marketplace; Hub; CLI.
- **Compatibility:** **Shared standard or protocol** for MCP and skills. Hub is a proprietary marketplace (**Native**).
- **Dependencies:** Model providers or local models.
- **Availability:** Open source (~35.8k stars).
- **Maintenance:** Active.
- **License:** Apache-2.0 (commonly cited; not re-verified).
- **Limitations:** Hub is Continue-specific; smaller agent-depth than Claude Code.
- **Related resources:** —
- **Sources:** https://github.com/the-focus-ai/claude-marketplace/blob/HEAD/reports/2026-02-13-portable-ai-coding-skills-cross-tool-interoperability.md (secondary); https://github.com/nilline/awesome-cli-coding-agents (secondary).
- **Verification date:** 2026-10-10
- **Confidence:** Medium (**Partially verified**).

### Other uncovered agents (brief mentions — not researched in depth)
- **Grok Build** (`xai-org/grok-build`) — xAI's official coding agent harness/TUI; fullscreen, mouse-interactive, extensible; Apache-2.0; ~26.5k stars. **Unverified** beyond list blurbs.
- **Reasonix** (`esengine/DeepSeek-Reasonix`) — single Go binary coding agent for long unattended runs; terminal/desktop/browser/editor-over-ACP; `reasonix.toml` config; MCP + Extension Protocol sidecar; plan mode; workspace sandbox; per-turn checkpoints; MIT; ~35.4k stars. **Unverified** beyond list blurbs.
- **Deep Agents Code** (`langchain-ai/deepagents`) — LangChain's official terminal coding agent on the Deep Agents SDK; TUI, subagents, headless mode, HITL approvals; PyPI `deepagents-code`; ~29.1k stars. **Unverified** beyond list blurbs.
- **Codebuff** (CodebuffAI) — coding CLI; native binary; open-source fork "Freebuff". **Unverified**.
- **MiniMax CLI** (`mmx-cli`) — MiniMax's coding CLI via npm. **Unverified**.
- **Mistral Vibe** — Mistral's Python-based coding CLI via pip. **Unverified**.
- **MiMo Code** (Xiaomi) — Xiaomi's coding CLI. **Unverified**.
- **Open Interpreter** (`OpenInterpreter/open-interpreter`) — terminal agent executing code/actions; ~67.3k stars. **Unverified**.
- **SWE-agent** (`SWE-agent/SWE-agent`) — agent for resolving repo issues/PR tasks; SWE-bench workflows; ~20.3k stars. **Unverified**.
- **Roomote** (`RooCodeInc/Roomote`) — Roo Code team's single-tenant cloud coding agent (hosted/self-hosted). **Unverified** beyond agentlist blurb.
- **ZCode** (zai-org) — Zhipu/GLM's official harness; no GLM-specific harness behavior publicly documented (per josvaal research). **Unverified**.
- **OH-MY-PI** (`can1357/oh-my-pi`) — enhanced standalone Pi ("omp") with Rust addons: session management, MCP support, AST tools; ~20–30k stars. **Unverified** beyond lists.
- **Cline CLI / Roo Code CLI** — covered under Cline (§9) and Roo Code (§10) records.
- **Sources (all secondary lists):** https://github.com/nilline/awesome-cli-coding-agents; https://github.com/dinkaass/awesome-cli-coding-agents; https://github.com/agentlistio/awesome-agent-list
- **Verification date:** 2026-10-10
- **Confidence:** Low (**Unverified**). These warrant a follow-up sweep if the Atlas needs depth here.

---
## 17. Compatibility matrix — agents × extension mechanisms

Legend: ✅ Native | 🔗 Official integration | 🔌 Documented adapter/port | 🌐 Shared standard/protocol | 🛠 Custom integration required | 📖 Reference-only | ❓ Unverified | ⛔ Incompatible/unavailable | 🕰 Historical

| Agent | Plugins / marketplace | Skills (SKILL.md) | Slash commands | Custom agents / subagents | Instruction files | Rules files | Hooks | MCP / tool registry | Permission system | Session / background / headless | API / SDK |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude Code | ✅ plugin + marketplace (`.claude-plugin/`) | ✅ | ✅ | ✅ (`.claude/agents/`) | ✅ CLAUDE.md | ✅ (via skills/settings) | ✅ | ✅ MCP+LSP | ✅ | ✅ / ✅ / ✅ | ✅ Agent SDK |
| OpenCode | ✅ plugin system (marketplace: ⛔ gap #7467) | ✅ 🌐 | ✅ | ✅ | ✅ AGENTS.md | ✅ | ✅ | ✅ MCP | ✅ | ✅ / ✅ / ✅ | ✅ SDK |
| Cursor | ✅ plugin + marketplace (`.cursor-plugin/`) | ✅ | ✅ (`.cursor/commands/`) | ✅ (`.cursor/agents/`, 🔌 reads `.claude/`, `.codex/`) | ✅ AGENTS.md (+ nested) | ✅ `.mdc` | ✅ (`.cursor/hooks.json`) | ✅ | ✅ | ✅ / ✅ / ✅ (CLI+Cloud) | ✅ ACP/Cloud |
| Codex CLI | ✅ shared ChatGPT/Codex plugin dir | ✅ (4 scopes) | ✅ legacy (deprecated→skills) | ✅ (TOML agents) | ✅ AGENTS.md (layered) | ✅ Starlark `.rules` | ✅ (`hooks.json`) | ✅ | ✅ (sandbox×approval) | ✅ / ✅ / ✅ | ✅ app-server/SDK |
| Antigravity CLI | ✅ plugin.json (no marketplace) | ✅ | ✅ (skills→commands) | ✅ (`.agents/agents/`) | ✅ AGENTS.md/GEMINI.md | ✅ `.agents/rules/` | ✅ (`hooks.json`) | ✅ | ✅ | ✅ / ✅ / ✅ (`-p`) | ✅ Antigravity SDK |
| Gemini CLI | 🕰 extensions (`gemini-extension.json`) | 🕰 | 🕰 (TOML) | 🕰 | 🕰 GEMINI.md | 🕰 | 🕰 (`hooks/hooks.json`) | 🕰 | 🕰 | 🕰 | 🕰 SDK/ACP |
| Copilot CLI | ✅ (`copilot plugin`; Agent Plugins 1.0) | ✅ (`.github/skills/` + 🔌 cross-reads) | ✅ (built-ins; prompt-files VS Code-only) | ✅ (`.agent.md` + Fleet) | ✅ `.github/copilot-instructions.md` (+ AGENTS.md read) | ✅ `.instructions.md` | ✅ (`.github/hooks/`) | ✅ | ✅ (allow-lists/sandbox) | ✅ / ✅ / ✅ (`-p`, `--cloud`) | ✅ SDK/ACP |
| Windsurf/Cascade | ⛔ (none; git-clone only) | ✅ (`.windsurf/skills/`) | ✅ Workflows | ❓ (no user-authored files found) | ✅ AGENTS.md | ✅ `.devin/rules/` ⬅ `.windsurf/rules/` | ✅ Cascade Hooks | ✅ | ✅ (Turbo levels) | ✅ / ❓ / ⛔ (GUI req.) | ❓ |
| Cline | ✅ Customize marketplace + Cline Plugins | ✅ | ✅ (`/mcp:` prompts) | ✅ custom modes (+ Plan delegation) | ✅ `.clinerules` (+ AGENTS.md) | ✅ `.clinerules/` | ✅ | ✅ (marketplace) | ✅ (approvals/controller) | ✅ / ✅ / ✅ (CLI) | ✅ SDK/ACP |
| Roo Code | ✅ modes marketplace (+ VS Code mkt) | ❓ | ✅ (mode switches) | ✅ custom modes + Orchestrator | ✅ (custom instr.; compat reads) | ✅ `.roo/rules-*` | ❓ | ✅ | ✅ (mode tool groups) | ✅ / ❓ / ✅ (CLI) | ✅ Roomote |
| Aider | ⛔ | 📖 (as inlined conventions) | ⛔ | ⛔ | ✅ CONVENTIONS.md (`--read`) | 📖 | ⛔ | 🛠 (community wrappers) | ✅ (git review) | ✅ / ✅ (watch) / ✅ (scripted) | ⛔ |
| Amp | ✅ (experimental API) | ✅ (`.agents/skills/`, 🌐 shared bucket) | ✅ | 🛠 (auto-spawn only; no user files) | ✅ AGENTS.md (glob frontmatter) | ✅ | ✅ | ✅ | ✅ (modes) | ✅ / ✅ (orbs/runners) / ✅ | ❓ |
| Factory Droid | ❓ | ✅ (`~/.factory/skills`) | ❓ | ✅ Custom Droids + Missions | ✅ AGENTS.md (autonomy levels) | ✅ | ✅ (`~/.factory/hooks.json`, Claude-compatible) | ✅ | ✅ (L1–L5) | ✅ / ✅ / ✅ (`droid exec`) | ❓ |
| Kimi Code | ✅ (`kimi.plugin.json`, `/plugins`) | ✅ (4 paths) | ✅ (built-ins + plugin) | ✅ (plugin-packaged; swarm) | 📖 (`/import-from-cc-codex`) | ❓ | ✅ (plugin) | ✅ | ✅ | ✅ / ✅ / ✅ (`--print`) | ✅ SDK/ACP/server |
| Kimi CLI (legacy) | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 | 🕰 |
| Pi | ✅ Pi Packages (npm/git) | ✅ (package resource) | ✅ | ⛔ (by design) | ✅ AGENTS.md/CLAUDE.md | ❓ | ❓ | 🛠 (community pkgs) | ✅ (user perms) | ✅ / ❓ / ✅ (`-p`, rpc) | ✅ SDK/RPC |
| Qwen Code | ❓ | ✅ (`.qwen/skills/`) | ❓ | ✅ (SubAgents, Agent Teams) | ✅ AGENTS.md | ❓ | ✅ (`~/.qwen/settings.json`) | ✅ | ✅ | ✅ / ✅ / ✅ (`-p`, `serve`) | ✅ SDKs |
| Crush | ⛔ | ✅ 🌐 | ❓ | ❓ | ❓ | ❓ (`crush.json`) | ⛔ | ✅ | ✅ (approvals) | ✅ / ❓ / ❓ | ❓ |
| Kilo/Goose/Continue/Grok/others | ❓/✅(Hub) | ❓/✅ | ❓ | ❓ | ❓ | ❓ | ❓ | ❓/✅ | ❓ | ❓ | ❓ |

### Cross-tool standards observed (shared protocol layer)
- **Agent Skills (SKILL.md, agentskills.io):** native in Claude Code, Codex, Antigravity, Copilot CLI, Cursor, Amp, Kimi Code, Qwen Code, Crush, Pi (as package resource); shared discovery buckets `~/.agents/skills/` and `~/.config/agents/skills/` (XDG) span Amp/Kimi/Replit.
- **MCP (modelcontextprotocol.io):** universal tool-registry standard — every agent except Aider (community wrappers only) has native MCP client support.
- **AGENTS.md:** read natively by Codex, Cursor (root+nested), Antigravity, Amp (primary), Copilot CLI, Aider (via `--read`), Qwen Code, Pi; Windsurf processes it through its rules engine.
- **Claude-Code-compat shims:** Copilot CLI accepts `.claude-plugin/plugin.json` manifests; Cursor reads `.claude/agents/`; Kimi Code imports Claude Code/Codex assets; Factory's hook protocol is wire-compatible with Claude Code's; Cline/Roo share `.clinerules` lineage.
- **ACP (Agent Client Protocol):** supported by Cline, Kimi Code, Cursor (`agent acp`), Copilot CLI (`--acp`), Qwen Code (`serve`), Reasonix — emerging as the cross-editor embedding standard.

---

## 18. Coverage note

### Counts
- **Full records:** 15 (Claude Code, Cursor, Codex CLI, Antigravity CLI, Gemini CLI [Historical], Copilot CLI, Windsurf/Devin Desktop, Cline, Roo Code, Aider, Amp, Factory Droid, Kimi Code, Pi, OpenCode [cross-ref]) + 1 host-surface record (VS Code marketplace) + 1 legacy-alias note (Kimi CLI) = **17 records**.
- **Emerging records (medium depth):** Qwen Code, Crush, Kilo Code, Goose, Continue.dev = **5**.
- **Brief mentions:** Grok Build, Reasonix, Deep Agents Code, Codebuff, MiniMax CLI, Mistral Vibe, MiMo Code, Open Interpreter, SWE-agent, Roomote, ZCode, OH-MY-PI = **12**.
- **Verification spread:** High/Verified: 8 · Partially verified: 9 · Historical: 2 (Gemini CLI, Kimi CLI legacy) · Unverified: 17 (mostly brief mentions) · Unresolved items: 4 (see below).

### Key findings
1. **Gemini CLI is dead for consumers** — Google I/O 2026 (May 19) moved it into **Antigravity CLI** (`agy`, Go binary, shared harness with Antigravity 2.0 desktop); consumer serving ended **2026-06-18** (primary: Google Developers Blog). Antigravity keeps Skills/Hooks/Subagents/Extensions as "Antigravity plugins" (`plugin.json`, no marketplace).
2. **Windsurf is becoming Devin Desktop** — docs.windsurf.com now brands Cascade's host as "Devin Desktop"; `.devin/rules/` preferred over `.windsurf/rules/` (primary docs, fetched 2026-10-10). Cognition consolidation.
3. **Kimi CLI → Kimi Code CLI** — `MoonshotAI/kimi-cli` is a legacy alias being wound down; the live product is `MoonshotAI/kimi-code` (MIT) with `kimi.plugin.json` plugins, skills, hooks, subagent swarm (official READMEs).
4. **Amp's surface is in flux** — spun out of Sourcegraph (Dec 2025); Feb 2026 "Coding Agent Is Dead" post + VS Code/Cursor extension shutdown (Mar 2026) per secondary; but the current official manual presents web + macOS/iOS + CLI as first-class. Unresolved.
5. **Extension-primitive convergence** — skills (SKILL.md), hooks, MCP, and AGENTS.md are now near-universal; the differentiators are **distribution** (marketplace vs git-clone vs none) and **subagent authoring** (declarative files vs auto-spawn vs modes).
6. **Claude-Code-compat is the de-facto interop layer** — Copilot CLI, Cursor, Kimi Code, Factory Droid, and Cline/Roo all read or accept Claude-Code-shaped assets.

### Limitations of this pass
- Primary docs not directly fetched for: Antigravity (JS docs), Factory Droid (JS docs), Aider (secondary only), Qwen Code (secondary only), Pi extension internals beyond packages doc. Their records are **Partially verified** via multi-source secondary corroboration.
- Cursor hooks schema, Copilot CLI cross-tool reads, and Kimi Code plugin internals rely on secondary evidence.
- 12 emerging agents are mention-level only.

### More work warranted?
- **Yes, targeted:** (a) Antigravity official docs deep-read (plugin schema, hook events); (b) Factory Droid primary docs (skills/custom-droid schema); (c) Kilo Code, Goose, Grok Build, Reasonix, Deep Agents Code full records; (d) resolve the 4 Unresolved items below; (e) OpenCode cross-check pass (out of scope here by dedup design).

### Unresolved items
1. Amp editor-integration status (CLI-only pivot vs current apps-first manual).
2. Pi Rust rewrite (`noeljackson/pi`) relationship to `earendil-works/pi`.
3. Crush license (MIT vs FSL-1.1-MIT across sources).
4. `~/.cursor/commands` user-level path (community-reported; no official doc captured).

---
*Catalog 03b-agents.md completed 2026-10-10 by workstream researcher #7.*
