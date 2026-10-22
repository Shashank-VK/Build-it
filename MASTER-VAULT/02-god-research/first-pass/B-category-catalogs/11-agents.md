# 11 — Agents (Coding Agents · Plugins/Marketplaces · Skills/Commands · Hooks · Permissions · Subagents · Sessions/Background/Headless · SDKs)

> Part 3 · B-category catalog · Agents-Harness researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> Compatibility classes: Native (first-party feature) · Compatible (works via standard path, e.g. MCP/AGENTS.md) · Bridge (needs adapter/plugin) · N/A

## Index (25 resources)

Core agents: OpenCode · Claude Code · Cursor · OpenAI Codex · Gemini CLI (+Antigravity note) · GitHub Copilot · Windsurf/Cascade · Cline · Roo Code · Aider
Extension systems: OpenCode commands/skills/MCP/permissions · Claude skills/commands/hooks/subagents · Cursor rules/skills/subagents/hooks · Codex skills/plugins/hooks · Gemini extensions · Copilot extensions/SDK · Cline modes/MCP/skills/hooks · Roo modes/marketplace
Cross-cutting: MCP specification · Agent Skills format (SKILL.md) · AGENTS.md convention · Headless/Background sessions · Checkpointing · Agent SDKs (Claude/Codex/Copilot/Cursor)

---

### 01 — OpenCode (terminal/desktop/IDE agent)
- **Canonical identity:** `npm:opencode-ai` — `github:anomalyco/opencode` (formerly sst/opencode)
- **Category:** Agents → Terminal-first open-source coding agent
- **Type:** OSS (OpenCode.ai)
- **Official URL:** https://opencode.ai/docs (agents: https://opencode.ai/docs/agents ; v2: https://v2.opencode.ai/docs/agents)
- **Description:** Terminal TUI + desktop + IDE extension; 75+ LLM providers; built-in `build` (primary, full tools) / `plan` (primary, no edits) / `general`+`explore` (subagents); custom agents via `~/.config/opencode/agents/*.md` or `opencode.json`.
- **Contents inspected:** WebSearch-verified official agents docs excerpts (build/plan/general/compaction roles, `opencode agent create`, permission frontmatter) + install docs (`curl …/install | bash`, npm/Homebrew/Choco/Scoop/Docker).
- **Capabilities:** Primary/subagent modes, custom agents, per-agent model/permissions, background subagents, plan mode.
- **Usage domain:** Terminal-first alternative to Claude Code/Cursor for any repo.
- **Integration:** official (TUI `/init`, `/connect`; IDE extensions; MCP servers)
- **Compatibility:** Native — agents/subagents/permissions are first-party. Evidence: official agents page lists build/plan/general/explore + config schema.
- **Deps:** Node.js or native binary; provider API keys.
- **Availability:** npm/binary/source.
- **Maintenance:** Active (v2 docs live 2026).
- **License:** MIT (core OSS).
- **Security/limits:** Permissive defaults (most allow; `.env` deny, external-dir ask); configure deny for secrets.
- **Related:** Claude Code, Codex CLI, skills, MCP.
- **Sources:** opencode.ai/docs; v2.opencode.ai/docs/agents.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Claude Code (Anthropic reference agent)
- **Canonical identity:** `tool:claude-code` — Anthropic
- **Category:** Agents → Reference terminal/IDE coding agent
- **Type:** Commercial (Anthropic; subscription/API)
- **Official URL:** https://code.claude.com/docs/en/ (commands: /docs/en/commands; sub-agents: /docs/en/sub-agents; hooks: /docs/en/hooks)
- **Description:** Agentic coding CLI + IDE extension; built-in Explore/Plan subagents, skills (`/code-review`), slash commands (`/init /agents /permissions /hooks /batch /goal`), hooks (PreToolUse/PermissionRequest/PostToolUse/SubagentStart/Stop…), permission modes incl. plan/bypass, background sessions (`claude agents` view), headless `claude -p`.
- **Contents inspected:** WebSearch-verified docs excerpts (subagent frontmatter `tools/model/skills/mcpServers`, hooks lifecycle table, commands reference, checkpointing, agent-view/`/goal` week-20 notes).
- **Capabilities:** Subagents, skills-as-commands, hooks, checkpoints/rewind, plan mode, `Agent` SDK definitions.
- **Usage domain:** Baseline other harnesses copy (permissions/skills/hooks vocabulary).
- **Integration:** official (VS Code/JetBrains extensions; MCP; Agent SDK TS/Python; `/import codex|gemini|cursor`)
- **Compatibility:** Native — all listed mechanisms are first-party. Evidence: code.claude.com publishes each surface under its own page.
- **Deps:** Anthropic account/API; Node 18+.
- **Availability:** npm (`@anthropic-ai/claude-code`) + native binaries.
- **Maintenance:** Active (weekly releases, v2.1.x 2026).
- **License:** Proprietary CLI (docs CC-ish; SDK Apache-2.0 parts).
- **Security/limits:** `bypassPermissions` never inherited blindly by subagents; critical-path `rm` always gated; deny rules win.
- **Related:** OpenCode, Codex, Agent SDK, MCP.
- **Sources:** code.claude.com/docs/en/*; Anthropic engineering blog (multi-agent).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — Cursor (AI editor + agents)
- **Canonical identity:** `tool:cursor` — Anysphere
- **Category:** Agents → AI-native IDE + cloud/CLI agents
- **Type:** Commercial (freemium Teams/Enterprise)
- **Official URL:** https://cursor.com/docs (rules: /docs/rules; agent overview: /docs/agent/overview)
- **Description:** Fork-based editor with Agent (Chat) + Cloud Agents + CLI (`cursor-agent`) + SDK (TS/Python); customization via Project/User/Team Rules (`.cursor/rules/*.mdc`), `AGENTS.md`, Skills (`.cursor/skills/` + compat `.claude/skills .codex/skills`), Subagents (`/docs/agent/subagents`), Hooks (`/docs/hooks`), Plugins/marketplace (`/docs/plugins`), MCP, headless/CI (`Headless / CI` page).
- **Contents inspected:** WebSearch-verified docs hub excerpts (models table incl. Claude/Sonnet/GPT/Gemini/Grok, rules `.mdc` anatomy, skills/subagents/hooks/MCP nav, CLI+SDK pages).
- **Capabilities:** Plan mode, checkpoints, review, Bugbot, background/cloud agents, ACP shell mode.
- **Usage domain:** IDE-first teams wanting editor + agents + review in one surface.
- **Integration:** official (GitHub/GitLab/Linear/Slack/JetBrains connectors; MCP)
- **Compatibility:** Native — rules/skills/subagents/hooks/MCP/headless are first-party docs pages. Evidence: docs nav lists each under Customize/CLI/SDK.
- **Deps:** Cursor account; project repo.
- **Availability:** Download (Win/macOS/Linux) + web agents.
- **Maintenance:** Active (2026 model pool incl. Composer/Grok).
- **License:** Proprietary.
- **Security/limits:** Team rules + Enterprise controls; review AI diffs before merge (review inbox).
- **Related:** Copilot, Windsurf, Cline, MCP.
- **Sources:** cursor.com/docs; docs.cursor.com/*.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — OpenAI Codex (CLI + IDE + Cloud + SDK)
- **Canonical identity:** `tool:codex-cli` — `github:openai/codex` — `npm:@openai/codex-sdk` / `pip:openai-codex`
- **Category:** Agents → Vendor CLI/cloud coding agent
- **Type:** Commercial OSS-client (OpenAI; CLI Apache/MIT, service metered)
- **Official URL:** https://developers.openai.com/codex/ (CLI: /codex/cli; SDK: /codex/sdk; skills: Build skills; plugins: Build plugins; hooks)
- **Description:** Rust CLI (`codex`, `codex exec`, `codex mcp-server`, `codex cloud`); IDE extension; cloud environments; sandbox + permissions (`/permissions`); subagents; MCP; skills (`.codex/skills/`); plugins; hooks; App Server (replaces `codex mcp-server` binary); TS+Python SDKs (start/continue/resume threads); Agents-SDK orchestration via MCP server.
- **Contents inspected:** WebSearch-verified developer-docs excerpts (SDK install `npm i @openai/codex-sdk` / `pip install openai-codex`, `codex mcp-server` + Agents SDK guide, CLI quickstart `curl …/codex/install.sh | sh`).
- **Capabilities:** Interactive TUI, non-interactive exec, cloud delegation, code review, image gen, skills/plugins/site-tools (WebMCP).
- **Usage domain:** OpenAI-model shops; CI pipelines via `exec`; multi-agent via Agents SDK.
- **Integration:** official (GitHub/GitLab/Slack/Linear; MCP Inspector)
- **Compatibility:** Native — skills/plugins/hooks/MCP/SDK are first-party docs sections. Evidence: developers.openai.com/codex nav lists each.
- **Deps:** OpenAI account/ChatGPT plan or API key; Node 18+/Python 3.10+ for SDKs.
- **Availability:** installer/npm/source; cloud hosted.
- **Maintenance:** Active (2026 SDK stable TS / beta→stable Python).
- **License:** CLI OSS; service ToS metered.
- **Security/limits:** Sandboxes + writable-roots; approvals for edits/commands; pin SDK runtime intentionally.
- **Related:** Agents SDK, MCP, Claude Code, Gemini CLI.
- **Sources:** developers.openai.com/codex/*; github.com/openai/codex (sdk/typescript/README).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 05 — Gemini CLI (Google, open-source)
- **Canonical identity:** `tool:gemini-cli` — `github:google-gemini/gemini-cli`
- **Category:** Agents → Open-source terminal agent (Gemini)
- **Type:** OSS (Apache-2.0, Google) + Google cloud quota
- **Official URL:** https://geminicli.com/docs/ (extensions: /docs/extensions/; headless: /docs/cli/headless/)
- **Description:** Terminal agent; extensions bundle prompts+MCP+commands+themes+hooks+sub-agents+skills (`gemini extensions install <gh-url>`; manifest `gemini-extension.json`); gallery ~2046 extensions; headless `-p/--prompt` + `--output-format json|jsonl-stream`; MCP OAuth/SSE/HTTP; note: unpaid/Google-One tier migrated to Antigravity CLI 2026-06-18.
- **Contents inspected:** WebSearch-verified docs excerpts (extension format/manifest fields, headless JSON schema + exit codes 0/1/42/53, extension gallery counts).
- **Capabilities:** Custom commands, sub-agents, skills, hooks, themes, plans dir, MCP servers.
- **Usage domain:** Gemini-centric terminal automation + extension sharing.
- **Integration:** official (Google Workspace extension, MCP servers, VS Code companion)
- **Compatibility:** Native — extensions/headless/MCP are first-party. Evidence: geminicli.com/docs/* each with reference pages.
- **Deps:** Google account/API key; Node 20+.
- **Availability:** npm (`@google/gemini-cli`) + source.
- **Maintenance:** Active (gallery growing; Antigravity fork for consumer tier).
- **License:** Apache-2.0.
- **Security/limits:** Inspect extensions before install (arbitrary MCP/tools); OAuth browser flow unavailable headless.
- **Related:** Antigravity, Codex, Claude Code, MCP.
- **Sources:** geminicli.com/docs/*; github.com/google-gemini/gemini-cli/docs/*.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — GitHub Copilot (CLI + coding agent + SDK)
- **Canonical identity:** `tool:copilot-cli` + `npm:@github/copilot-sdk` / `pip:github-copilot-sdk` — `github:github/copilot-sdk`
- **Category:** Agents → Platform coding agent (editor/CLI/cloud/SDK)
- **Type:** Commercial (Copilot subscription; SDK technical preview)
- **Official URL:** https://docs.github.com/en/copilot (CLI extensions: /concepts/agents/copilot-cli/about-cli-extensions; SDK: /how-tos/copilot-sdk; SDK docs map: github.com/github/copilot-sdk/tree/main/docs)
- **Description:** CLI with tools+slash-commands, extensions (JS module: tools+commands; Load&Augment/Load-Only/Disabled), hooks (Pre/Post-Tool-Use, prompt, lifecycle), skills, MCP, LSP servers, image input, session persistence/resume, remote/cloud sessions, fleet mode (parallel sub-agents), plugin directories (bundle skills+hooks+MCP+agents), OTEL observability, MAF multi-agent integration; SDKs TS/Python/Go/.NET over JSON-RPC to CLI server.
- **Contents inspected:** WebSearch-verified docs excerpts (SDK docs index incl. hooks/custom-agents/MCP/skills/plugins/fleet/cloud/remote; CLI extensions locations `.github/extensions/`, `~/.copilot/extensions/`; Go module README architecture).
- **Capabilities:** Agent mode in VS Code, coding agent (PR-assigned), CLI automation, embeddable runtime.
- **Usage domain:** GitHub-native orgs standardizing on Copilot everywhere.
- **Integration:** official (VS Code/JetBrains/CLI; MCP; Microsoft Agent Framework)
- **Compatibility:** Native — extensions/hooks/skills/plugins/MCP/SDK are first-party. Evidence: copilot-sdk docs map lists each guide.
- **Deps:** Copilot subscription; CLI in PATH (or bundled).
- **Availability:** Bundled with VS Code/GitHub; SDK via npm/PyPI/Go/NuGet.
- **Maintenance:** Active (SDK v0.1.x early 2026, rapid).
- **License:** SDK MIT (preview); service commercial.
- **Security/limits:** Default `--allow-all`-equivalent in SDK — scope tools/permissions explicitly; BYOK available.
- **Related:** MAF, MCP, Cursor, Codex.
- **Sources:** docs.github.com/en/copilot/*; github.com/github/copilot-sdk/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — Windsurf + Cascade (agentic IDE)
- **Canonical identity:** `tool:windsurf` (Cascade agent; ex-Codeium) — Windsurf/Cognition
- **Category:** Agents → Agentic IDE
- **Type:** Commercial (Windsurf; free+pill tiers)
- **Official URL:** https://docs.windsurf.com/windsurf/cascade/cascade (MCP: …/cascade/mcp; AGENTS.md: …/cascade/agents-md)
- **Description:** Cascade with Code/Chat (Write/Chat in JetBrains) modes, 20–25 tool calls/prompt, voice, checkpoints/revert, real-time awareness, linter integration; Memories+Rules (`.windsurf/rules/*.md`, global + repo); `AGENTS.md` auto-discovered into Rules engine (root=always-on, subdir=glob); MCP (`~/.codeium/windsurf/mcp_config.json`, Marketplace one-click, stdio/HTTP/SSE+OAuth, 100-tool cap); JetBrains + Devin Desktop surfaces.
- **Contents inspected:** WebSearch-verified docs excerpts (Cascade modes/tool limits, AGENTS.md scoping table, MCP config examples + tool-cap guidance).
- **Capabilities:** Plan/build, explain/fix Problems panel, auto-execution levels (Off/Auto/Turbo), checkpoints.
- **Usage domain:** IDE-loyal teams wanting Cascade awareness without terminal-first flow.
- **Integration:** official (MCP Marketplace; JetBrains plugin; Devin Desktop)
- **Compatibility:** Native — rules/AGENTS.md/MCP/checkpoints are first-party. Evidence: docs.windsurf.com pages per surface.
- **Deps:** Windsurf account/IDE install.
- **Availability:** IDE download; Teams/Enterprise registries.
- **Maintenance:** Active (Devin-era docs 2026).
- **License:** Proprietary.
- **Security/limits:** 100-tool MCP cap — disable unused servers; `.codeiumignore` for sensitive paths.
- **Related:** Cursor, Copilot, Cline, MCP.
- **Sources:** docs.windsurf.com/*; MCPBundles setup guide (cap corroboration).
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — Cline (open-source editor+CLI agent)
- **Canonical identity:** `tool:cline` — `npm:cline` — `github:cline/cline` (Cline Bot Inc.)
- **Category:** Agents → OSS Plan/Act editor agent + CLI
- **Type:** OSS (Apache-2.0) + provider keys (or Cline sign-in / ChatGPT sub via openai-codex)
- **Official URL:** https://docs.cline.bot/home (CLI: apps/cli; MCP: /mcp/mcp-overview; marketplace: cline.bot/mcp-marketplace)
- **Description:** VS Code/Cursor/Windsurf/JetBrains/Antigravity + CLI sharing one agent core (plan/act, MCP, checkpoints `/undo`, rules, skills, provider config); CLI shapes: interactive TUI (`cline`/`-i`), one-shot, `--json` NDJSON, `--yolo`, `--zen` background hub daemon; `cline mcp [install]` wizard; sub-agent spawning + agent teams; hooks (8 events, Unix-only); workflows; `.clineignore`; checkpoints; cron/event schedules; Telegram/GChat/WhatsApp connectors; ACP mode.
- **Contents inspected:** WebSearch-verified docs + npm/GitHub excerpts (CLI mode table, MCP config `~/.cline/mcp.json` stdio/streamableHttp/sse, docs index, CHANGELOG SDK-migration note).
- **Capabilities:** @-mentions, visual diffs, browser automation, auto-approve, Memory Bank/Focus Chain, checkpoints.
- **Usage domain:** OSS-first teams needing same agent in editor and CI/headless.
- **Integration:** official (MCP Marketplace one-click; provider-agnostic incl. local)
- **Compatibility:** Native — modes/MCP/marketplace/hooks/headless are first-party. Evidence: docs.cline.bot nav + npm CLI reference.
- **Deps:** Editor or Node; provider key or Cline account.
- **Availability:** Marketplace/OpenVSX/npm/source.
- **Maintenance:** Active (11M+ devs claimed; SDK-backed runtime 2026).
- **License:** Apache-2.0.
- **Security/limits:** Auto-approve now off by default; approval-gate risky commands; Unix-only hooks.
- **Related:** Roo Code, Kilo, Cursor, MCP.
- **Sources:** docs.cline.bot/*; npm `cline`; github.com/cline/cline.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 09 — Roo Code (modes-first agent; community fork ZooCode)
- **Canonical identity:** `tool:roo-code` — `github:RooCodeInc/Roo-Code` (+ Docs repo)
- **Category:** Agents → Modes-first VS Code agent
- **Type:** OSS (Apache-2.0) — NOTE: official extension shut down 2026-05-15; community fork ZooCode + Cline paths documented
- **Official URL:** https://docs.roocode.com/ (modes: /basic-usage/using-modes; marketplace: /features/marketplace; MCP: /features/mcp/overview)
- **Description:** Built-in modes Code/Ask/Architect/Debug/Orchestrator(Boomerang via `new_task` delegation) + custom modes (tool groups read/edit/command/browser/mcp); sticky per-mode models; Marketplace for MCPs+Modes (project `.roo/mcp.json`+`.roomodes` vs global settings); MCP stdio/HTTP/SSE.
- **Contents inspected:** WebSearch-verified docs excerpts (mode tool-access table, marketplace project-vs-global table, MCP transport pages) + GitHub README shutdown notice.
- **Capabilities:** Mode switching (`⌘/.`, `/architect`…), delegation, per-mode guardrails.
- **Usage domain:** Historical reference for modes/marketplace pattern; migrate to ZooCode/Cline.
- **Integration:** official-in-period (VS Code Marketplace/OpenVSX; MCP)
- **Compatibility:** Native-in-period; now **Archived** for greenfield. Evidence: README "Extension was shut down on May 15th".
- **Deps:** VS Code; provider keys.
- **Availability:** Source/archive; fork ZooCode.
- **Maintenance:** Archived (2026-05).
- **License:** Apache-2.0.
- **Security/limits:** Do not adopt for new work without fork review; audit custom-mode tool grants.
- **Related:** Cline, Kilo Code, ZooCode.
- **Sources:** docs.roocode.com/*; github.com/RooCodeInc/Roo-Code.
- **Verification date:** 2026-10-09 · **Confidence:** Archived

### 10 — Aider (terminal pair-programmer)
- **Canonical identity:** `pip:aider-chat` — `github:Aider-AI/aider`
- **Category:** Agents → Terminal pair-programming harness
- **Type:** OSS (Apache-2.0)
- **Official URL:** https://aider.chat/docs (repo map: /2023/10/22/repomap.html)
- **Description:** Git-native pair loop (`aider <files>`; `/add /model /ask /run /test /read /clear /drop`); repo map via tree-sitter (classes/functions+signatures); auto-commit with sensible messages; lint/test auto-fix loop; voice-to-code; images/URLs; IDE watch-comments; model-agnostic (Claude/DeepSeek/GPT/Ollama…); headless-friendly (`--message`, `--yes`, piped context; benchmarked SWE-bench).
- **Contents inspected:** WebSearch-verified README/docs excerpts (44.9k★, repo-map method, chat modes code/architect/ask/help, provider matrix).
- **Capabilities:** Multi-file edits, read-only/ask flows, conventions files, copy/paste web-chat bridge.
- **Usage domain:** Git-purist terminal pairing; low-ceremony harness reference.
- **Integration:** Compatible (git + editor-agnostic; MCP via wrappers, not native core)
- **Compatibility:** Compatible — git/conventions/headless are native; MCP/skills are Bridge. Evidence: aider.chat docs list no native MCP page.
- **Deps:** Python 3.9+; git; provider keys.
- **Availability:** PyPI/source/Docker.
- **Maintenance:** Active (13k+ commits; 6.8M installs claimed).
- **License:** Apache-2.0.
- **Security/limits:** Auto-commit + auto-lint can run arbitrary repo hooks — review staged diffs.
- **Related:** Repo maps (14), pre-commit (13), worktrees.
- **Sources:** aider.chat/*; github.com/Aider-AI/aider.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — Continue (OSS IDE agent; acquired by Cursor/Anysphere 2026-06)
- **Canonical identity:** `tool:continue` — `github:continuedev/continue` (read-only post-acquisition)
- **Category:** Agents → OSS IDE agent (historical)
- **Type:** OSS (Apache-2.0) → now under Anysphere
- **Official URL:** https://docs.continue.dev/ (repo: github.com/continuedev/continue)
- **Description:** VS Code/JetBrains chat+autocomplete+edit agent with `config.yaml` (models/tools/rules), docs-context (@Docs), MCP-adjacent tooling; acquisition note per agent-manual: "Continue was acquired by Cursor/Anysphere in June 2026; repo now read-only".
- **Contents inspected:** WebSearch-verified secondary attestation only (agent-manual hooks/MCP matrix row); no fresh official fetch this pass.
- **Capabilities:** Chat/edit/apply, codebase context, local-model friendly.
- **Usage domain:** Historical OSS IDE-agent reference; prefer Cline/OpenCode/Cursor going forward.
- **Integration:** Bridge (community MCP adapters in-period)
- **Compatibility:** Archived — do not greenfield. Evidence: acquisition + read-only attestation.
- **Deps:** Editor + provider keys (in-period).
- **Availability:** Archive/source.
- **Maintenance:** Archived (2026-06).
- **License:** Apache-2.0.
- **Security/limits:** Unmaintained — pin last release; audit model endpoints.
- **Related:** Cursor, Cline, Roo.
- **Sources:** agent-manual matrix (Ar9av/agent-manual); continuedev/continue.
- **Verification date:** 2026-10-09 · **Confidence:** Historical

### 12 — Agent Skills format (SKILL.md) — cross-harness standard
- **Canonical identity:** `spec:agent-skills` — https://agentskills.io (Anthropic proposal; embraced by OpenCode/Cline/Codex/Copilot/Gemini/Cursor)
- **Category:** Agents → Portable capability packaging (skills/commands)
- **Type:** Open spec (vendor-neutral)
- **Official URL:** https://agentskills.io/ ; Claude: https://code.claude.com/docs/en/skills ; Codex: https://developers.openai.com/codex (Build skills)
- **Description:** Directory with `SKILL.md` (YAML frontmatter `name/description/...` + markdown body); progressive disclosure (metadata → body → bundled resources); discovered under `.agents/skills/ .claude/skills/ .codex/skills/ .cursor/skills/ ~/.config/opencode/skills/`; invocable as `/skill` slash commands or via `Skill` tool; converters exist (Claude↔Codex).
- **Contents inspected:** WebSearch-verified docs excerpts (Claude Agent SDK skills/subagents mapping; Codex `.codex/skills/` + 345-skill converter guide; Copilot SDK Skills; Cursor `.agents/skills` discovery).
- **Capabilities:** Reusable prompts+scripts+MCP wiring shared across harnesses.
- **Usage domain:** Single authoring target for all 9 agents in this file.
- **Integration:** Compatible — every listed agent consumes it (paths differ; frontmatter extensions vary)
- **Compatibility:** Compatible — evidence: per-agent docs each document a skills directory; converters attest format parity.
- **Deps:** None (markdown + optional scripts).
- **Availability:** Spec + per-agent loaders.
- **Maintenance:** Active (2026 Skills-over-MCP extension in MCP spec).
- **License:** Spec open; skills vary.
- **Security/limits:** Skills execute with agent authority — review bundled scripts/MCP before install.
- **Related:** MCP, slash commands, hooks.
- **Sources:** agentskills.io; code.claude.com/docs/en/skills; developers.openai.com/codex; github.com/github/copilot-sdk/docs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 13 — Slash commands + custom commands (per-agent)
- **Canonical identity:** `pattern:slash-commands` (OpenCode `.opencode/commands/` · Claude `.claude/commands/` · Codex prompts · Cursor chat commands · Copilot slash · Gemini custom-commands · Cline `.cline/workflows`)
- **Category:** Agents → Repeatable prompt shortcuts
- **Type:** Per-agent convention (all Native in own harness)
- **Official URLs:** OpenCode: https://opencode-tutorial.com/en/docs/commands ; Claude: https://code.claude.com/docs/en/commands ; Cursor: https://cursor.com/docs/agent/chat/commands ; Copilot CLI: docs.github.com (extensions add commands)
- **Description:** `$ARGUMENTS/$1…` templates + `!`backtick`` shell interpolation; built-ins (`/init /undo /redo /share /compact /review`); stacking (`/write-tests /fix-issue 123`); Agent-SDK dispatch via prompt string; `context:fork` variants run as subagent.
- **Contents inspected:** WebSearch-verified excerpts (OpenCode `$ARGUMENTS/$1` + override rule; Claude stacked-skill expansion + forked `/code-review`; agent-manual coverage note).
- **Capabilities:** One-key workflows (plan→implement→verify); team-shared prompt library.
- **Usage domain:** Standardize harness UX across repos (paired with skills).
- **Integration:** official per agent; portable via Skills (12)
- **Compatibility:** Native (per harness) · Compatible (cross-harness via SKILL.md). Evidence: each agent docs a commands page.
- **Deps:** Agent config dirs.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Commands inherit session permissions; `!cmd` interpolation runs shell — gate with hooks.
- **Related:** Skills, subagents, hooks.
- **Sources:** See URLs above.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 14 — Hooks (event-gated guardrails) — cross-harness matrix
- **Canonical identity:** `pattern:agent-hooks` — matrix: https://github.com/Ar9av/agent-manual
- **Category:** Agents → Deterministic control points (PreToolUse/PostToolUse/PermissionRequest/SessionStart/Stop/PreCompact/SubagentStart…)
- **Type:** Per-agent Native; matrix OSS reference
- **Official URLs:** Claude: https://code.claude.com/docs/en/hooks ; Codex: developers.openai.com/codex (Hooks) ; Cursor: cursor.com/docs/hooks ; Copilot: SDK Hooks + `Using hooks with Copilot CLI` ; Cline: docs.cline.bot (Hooks, 8 events Unix-only) ; OpenCode: via plugins (`plugin` hooks)
- **Description:** Counts attested: Claude 31 events · Cursor 23 · Codex 10 · Cline 8 · Copilot full-hook set (Pre/Post-Tool-Use, prompt, lifecycle, error) · OpenCode via plugin SDK. Matchers (`Edit|Write`, `Bash(git *)`), exit-code/JSON decisions, timeouts.
- **Contents inspected:** WebSearch-verified excerpts (Claude lifecycle table + `if`-filter + exec-form; Copilot hooks reference; Cline hooks index; OpenCode Godot-Studio hooks.json example with SessionStart/PreToolUse/PostToolUse/PreCompact/Stop/SubagentStart/Stop).
- **Capabilities:** Block risky tools, inject context, run style/tests post-edit, audit subagents, notify.
- **Usage domain:** Runaway protection + evidence + policy (feeds file 13).
- **Integration:** official per agent
- **Compatibility:** Native (per harness). Evidence: each official hooks page + matrix counts.
- **Deps:** Shell scripts in repo (version them).
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent; matrix MIT-ish.
- **Security/limits:** Hooks run with user authority — keep handlers small, versioned, timeout-bounded; prefer `exec` form to avoid shell-quoting bugs.
- **Related:** Permissions, pre-commit, checkpoints.
- **Sources:** See URLs; agent-manual matrix.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 15 — Permissions / approval policies
- **Canonical identity:** `pattern:agent-permissions` (OpenCode `permission:{*/bash/edit…}`/v2 `permissions[]` · Claude `permissions.allow/deny` + modes · Codex sandbox+approvals · Copilot allowlists · Cursor team rules)
- **Category:** Agents → Least-privilege tool gating
- **Type:** Per-agent Native
- **Official URLs:** OpenCode: https://opencode.ai/en/docs/permissions + https://v2.opencode.ai/docs/permissions ; Claude: code.claude.com permission-modes + Agent SDK permissions ; Codex: developers.openai.com (sandbox/permissions)
- **Description:** allow/ask/deny + glob/regex matching, last-match-wins; tool-keyed (`read/edit/bash/task/skill/lsp/webfetch`, MCP `server_tool`); agent overrides; `.env` deny-by-default (OpenCode); critical-path `rm` never allow-listed (Claude); `plan` vs `bypassPermissions` inheritance rules for subagents.
- **Contents inspected:** WebSearch-verified excerpts (OpenCode defaults + frontmatter `permission: edit: deny…`; v2 rule schema `action/resource/effect`; Claude deny→ask→allow evaluation order + subagent inheritance).
- **Capabilities:** Per-command rules (`git *` ask, `grep *` allow), per-agent scoping, durable saved approvals.
- **Usage domain:** Required companion to every autonomous loop (13).
- **Integration:** official
- **Compatibility:** Native. Evidence: dedicated permissions pages in OpenCode/Claude/Codex/Copilot/Cursor docs.
- **Deps:** Config files (`opencode.json`, `settings.json`, `.codex/config.toml`).
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Saved `always` patterns can broaden scope — prefer narrow globs; deny beats allow everywhere.
- **Related:** Hooks, subagents, sessions.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 16 — Subagents / custom agents (delegation primitive)
- **Canonical identity:** `pattern:subagents` (OpenCode `mode:subagent/all` · Claude `.claude/agents/*.md` + `AgentDefinition` · Codex subagents · Cursor subagents · Copilot custom agents/fleet · Cline sub-agent+teams · Gemini sub-agents in extensions)
- **Category:** Agents → Scoped delegation with fresh context
- **Type:** Per-agent Native
- **Official URLs:** OpenCode: opencode.ai/docs/agents (+`task` permission) ; Claude: code.claude.com/docs/en/sub-agents + /agent-sdk/subagents ; Cursor: cursor.com/docs/agent/subagents ; Copilot: SDK Custom Agents + Fleet Mode
- **Description:** Frontmatter (`description/tools|model/skills/mcpServers/permissionMode/hooks`); built-ins (OpenCode general/explore; Claude Explore/Plan; Copilot fleet workers); foreground vs background; plugin-subagent restrictions (no hooks/mcpServers/permissionMode in Claude plugins); `subagent` permission gates child IDs.
- **Contents inspected:** WebSearch-verified excerpts (OpenCode modes table + `subagent` tool; Claude AgentDefinition `tools/skills/memory/mcpServers` + invocation/permission inheritance; Copilot fleet/custom-agent docs).
- **Capabilities:** Parallel investigation, reviewer/tester splits, orchestrator-worker fan-out (feeds file 12).
- **Usage domain:** All multi-agent patterns in file 12 build on this primitive.
- **Integration:** official
- **Compatibility:** Native. Evidence: per-agent subagent pages + SDK types.
- **Deps:** Agent definition dirs.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Children get own permissions (OpenCode) or inherit parent mode (Claude) — never assume containment; pass least tools.
- **Related:** Sessions, hooks (SubagentStart/Stop), A2A.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 17 — Sessions: persistence, resume, share, compaction
- **Canonical identity:** `pattern:agent-sessions` (OpenCode SQLite `~/.local/share/opencode/opencode.db` + `/sessions /resume /export` · Claude `--resume/--continue/fork-session /branch` + snapshots · Copilot persistence/remote · Cline task history · Cursor checkpoints)
- **Category:** Agents → Continuity across turns/machines
- **Type:** Per-agent Native
- **Official URLs:** OpenCode sessions skill (gideonfip/opencode-skills SKILL.md) ; Claude sessions/checkpointing docs ; Copilot Session Persistence/Remote Sessions
- **Description:** Full-transcript resume, fork/branch for experiments, export to markdown, snapshot dirs, remote-share to web/mobile (Copilot Remote, Claude Remote Control), compaction/summary agents preserve plan across 200k+ truncation.
- **Contents inspected:** WebSearch-verified excerpts (OpenCode db paths + log/snapshot/tool-output dirs; Claude 100-checkpoint retention + 30-day sweep + `/branch --fork-session`; Copilot persistence/remote guides).
- **Capabilities:** Long-horizon work without losing decisions; handoff bundles (feeds 13).
- **Usage domain:** Multi-session features, audits, mobile steering.
- **Integration:** official
- **Compatibility:** Native. Evidence: dedicated session/persistence pages per agent.
- **Deps:** Local disk (SQLite/snapshots); auth for remote.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Session DBs hold secrets/tool output (1–2 GB typical) — exclude from git, set `cleanupPeriodDays`.
- **Related:** Checkpoints, memory (14), handoffs (13).
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 18 — Background / cloud / headless execution
- **Canonical identity:** `pattern:background-headless` (`opencode run --attach` · `claude -p/--print [--output-format json|stream-json] [--allowedTools] [--max-turns]` + `claude agents` view · `codex exec` + cloud chats · `gemini -p` · `copilot` server mode + cloud sessions · `cline --json/--yolo/--zen` · Cursor Cloud Agents/Headless-CI)
- **Category:** Agents → Unattended + parallel execution
- **Type:** Per-agent Native
- **Official URLs:** Claude headless + agent-view (week-20) ; Codex non-interactive mode ; Gemini headless reference ; Copilot Backend/Cloud sessions ; Cursor Headless/CI ; Cline headless
- **Description:** Non-TTY execution with structured output (JSON/NDJSON/stream-json), tool allowlists, turn caps, exit codes (Gemini 0/1/42/53), stdin piping (`git diff | claude -p …`), cron/`/loop`, `timeout 600 …`; background rows keep running detached; cloud variants on hosted compute.
- **Contents inspected:** WebSearch-verified excerpts (Claude `-p` + `--allowedTools/--max-turns/--output-format` + bare mode; Gemini headless schema; Codex exec; Copilot headless-over-TCP; Cline NDJSON/zen).
- **Capabilities:** CI triage/review, batch migrations, issue→label, fleet fan-out (with worktrees).
- **Usage domain:** File 13 autonomous/bounded loops run on this substrate.
- **Integration:** official
- **Compatibility:** Native. Evidence: each agent ships a headless/CI page.
- **Deps:** CI runner; least-privilege tokens.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Per-agent.
- **Security/limits:** Cap turns+tools; read-only first pass for reviews; never `--dangerously-skip-permissions` in shared CI without sandbox.
- **Related:** Worktrees, cost tracking, evidence logs.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 19 — MCP (Model Context Protocol) — agent tool bus
- **Canonical identity:** `spec:mcp` — `github:modelcontextprotocol/*` — spec 2026-07-28
- **Category:** Agents → Standard tool/context wiring
- **Type:** Open standard (Linux Foundation; Apache-2.0)
- **Official URL:** https://modelcontextprotocol.io/ (spec: /specification/2026-07-28/ ; docs: /docs/2026-07-28)
- **Description:** JSON-RPC 2.0 hosts/clients/servers; servers expose Resources/Prompts/Tools (+ Sampling/Elicitation; extensions Tasks, Skills-over-MCP, MCP Apps); transports stdio/Streamable-HTTP/SSE(+OAuth); `codex mcp-server`, `gemini mcp`, `cline mcp install`, Copilot MCP Servers, Cursor MCP, Windsurf `mcp_config.json` all speak it; registry + inspector.
- **Contents inspected:** WebSearch-verified spec excerpts (hosts/clients/servers, features, trust&safety consent rules, extension list).
- **Capabilities:** One integration reused in every agent (DBs, browsers, SaaS, code search).
- **Usage domain:** Default answer for "connect agent to X".
- **Integration:** universal
- **Compatibility:** Native in all 9 agents (config keys differ). Evidence: per-agent MCP pages reference same spec version.
- **Deps:** Server processes (npx/docker/URLs).
- **Availability:** Spec + SDKs (TS/Python/Go/…).
- **Maintenance:** Active (2026-07-28 latest).
- **License:** Apache-2.0 / MIT SDKs.
- **Security/limits:** Treat tool descriptions as untrusted; user consent before invoke; only trusted servers (local RCE risk).
- **Related:** Skills-over-MCP, A2A, plugins.
- **Sources:** modelcontextprotocol.io/*; Anthropic MCP page.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 20 — Plugin & marketplace systems
- **Canonical identity:** `pattern:agent-marketplaces` (OpenCode `plugin[]`+skill-MCP · Claude plugins/marketplaces · Cursor Plugins · Codex plugins · Gemini gallery 2046 · Copilot plugin directories+marketplace · Cline MCP Marketplace · Roo Marketplace MCPs+Modes)
- **Category:** Agents → Shareable capability bundles
- **Type:** Per-agent Native
- **Official URLs:** Gemini: geminicli.com/extensions/ ; Cline: cline.bot/mcp-marketplace ; Roo: docs.roocode.com/features/marketplace ; Cursor: cursor.com/docs/plugins ; Copilot: Plugin directories ; Codex: Build plugins
- **Description:** Bundle skills+hooks+MCP+agents+commands as installable units (local path / GitHub URL / registry); conflict resolution by name; enterprise allowlists/custom registries (Windsurf/Cline-enterprise); `gemini extensions install …`, `opencode mcp add`, `cline mcp install …`.
- **Contents inspected:** WebSearch-verified excerpts (Gemini 2046-extension gallery sample; Cline marketplace categories; Roo project-vs-global install table; Copilot plugin-directory manifest; Codex plugin guide nav).
- **Capabilities:** One-click team standardization; versioned capability packs.
- **Usage domain:** Distribute org conventions + tool wiring.
- **Integration:** official per agent
- **Compatibility:** Native (per harness); cross-harness via SKILL.md+MCP. Evidence: each marketplace page live 2026.
- **Deps:** Registry/manifest trust review.
- **Availability:** Built-in.
- **Maintenance:** Active (except Roo archived).
- **License:** Per-item.
- **Security/limits:** Inspect source + permissions before install (marketplace code runs locally).
- **Related:** Skills, MCP, rules.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 21 — Claude Agent SDK (build on Claude Code runtime)
- **Canonical identity:** `npm:@anthropic-ai/claude-agent-sdk` / `pip:claude-agent-sdk` — docs: code.claude.com/docs/en/agent-sdk/*
- **Category:** Agents → SDK: embed agent loop in apps
- **Type:** Commercial SDK (Anthropic)
- **Official URL:** https://code.claude.com/docs/en/agent-sdk/ (subagents, skills/slash-commands, permissions, hooks)
- **Description:** Same tools/loop/context as Claude Code; programmatic queries, `AgentDefinition` (prompt/tools/skills/memory/mcpServers/permissionMode), `canUseTool` approvals, streaming, session resume; CLI for scripts/CI too.
- **Contents inspected:** WebSearch-verified excerpts (AgentDefinition fields table; skills dispatch via `/name`; permission evaluation order; subagent prompt/context isolation notes).
- **Capabilities:** Custom harnesses without rebuilding orchestration (feeds file 12 runtimes).
- **Usage domain:** Product teams embedding Claude execution.
- **Integration:** official
- **Compatibility:** Native to Claude Code runtime. Evidence: agent-sdk docs subtree.
- **Deps:** Node 18+/Python 3.10+; Anthropic key.
- **Availability:** npm/PyPI.
- **Maintenance:** Active.
- **License:** Proprietary/Apache parts.
- **Security/limits:** Re-implement approval UI via `canUseTool`; never hardcode keys.
- **Related:** Codex SDK, Copilot SDK, MCP.
- **Sources:** code.claude.com/docs/en/agent-sdk/*.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 22 — Codex SDK + App Server (TS + Python)
- **Canonical identity:** `npm:@openai/codex-sdk` + `pip:openai-codex` — `github:openai/codex/tree/main/sdk`
- **Category:** Agents → SDK: programmatic Codex threads
- **Type:** OSS client (OpenAI service metered)
- **Official URL:** https://developers.openai.com/codex/sdk (repos: sdk/typescript README)
- **Description:** `new Codex()` → `startThread()/resumeThread()` → `run(prompt|[{text|local_image}])` with JSON-schema responses; env isolation, `--config` TOML overrides; Python controls local app-server over JSON-RPC (pinned CLI runtime); app-server for custom clients (auth/history/approvals/streaming); Security TS SDK (beta) for scans.
- **Contents inspected:** WebSearch-verified excerpts (TS+Python install/usage snippets; env/config override semantics; `codex mcp-server` removal → app-server note).
- **Capabilities:** CI/CD embedding, custom agents calling Codex, internal tools.
- **Usage domain:** OpenAI-centric automation + multi-agent worker (via Agents SDK).
- **Integration:** official
- **Compatibility:** Native. Evidence: developers.openai.com/codex/sdk + sdk/typescript/README lines quoted.
- **Deps:** Node 18+/Python 3.10+; Codex CLI runtime.
- **Availability:** npm/PyPI/source.
- **Maintenance:** Active (stable TS; Python stable/prerelease tracks).
- **License:** OSS client; service ToS.
- **Security/limits:** Server-side only; control `env` for sandboxed hosts (Electron); audit `--config` overrides.
- **Related:** Agents SDK, MCP, App Server.
- **Sources:** developers.openai.com/codex/*; github.com/openai/codex/sdk/typescript/README.md.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 23 — Copilot SDK (TS/Python/Go/.NET + MAF bridge)
- **Canonical identity:** `npm:@github/copilot-sdk` / `pip:github-copilot-sdk` / `go:github.com/github/copilot-sdk/go` / `nuget:GitHub.Copilot.SDK` — `github:github/copilot-sdk`
- **Category:** Agents → SDK: Copilot runtime for any app
- **Type:** Commercial-tech-preview SDK (MIT client; subscription required)
- **Official URL:** https://docs.github.com/en/copilot/how-tos/copilot-sdk + https://github.com/github/copilot-sdk/tree/main/docs
- **Description:** Same engine as CLI over JSON-RPC (bundled/local/headless-over-TCP CLI lifecycle); hooks, custom agents, MCP, skills, plugin dirs, image input, streaming events, steering/queueing, persistence/resume, remote+cloud sessions, fleet mode, session budgets, OTEL; MAF integration for multi-agent; BYOK/OAuth/Azure-MI; multi-tenancy/scaling guides.
- **Contents inspected:** WebSearch-verified excerpts (docs map: setup/auth/features/hooks-reference/observability/integrations; Go README architecture + bundler/embed; BYOK/billing FAQ).
- **Capabilities:** Embed Copilot planning/tools/edits in products; parallel fleets.
- **Usage domain:** GitHub-ecosystem ISVs + enterprise backends.
- **Integration:** official (MAF, MCP)
- **Compatibility:** Native. Evidence: SDK docs map + package registries (npm/PyPI/Go/NuGet).
- **Deps:** Copilot subscription/CLI; language runtimes.
- **Availability:** Registries + source.
- **Maintenance:** Active (v0.1.16–19 Jan 2026 window).
- **License:** MIT (clients, preview).
- **Security/limits:** Subscription-gated; headless TCP needs network policy; scope session budgets.
- **Related:** MAF, MCP, Codex/Claude SDKs.
- **Sources:** docs.github.com/en/copilot/how-tos/copilot-sdk; github.com/github/copilot-sdk.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 24 — Cursor CLI + SDK (headless/CI + programmatic)
- **Canonical identity:** `tool:cursor-cli` (`cursor-agent`) + Cursor SDK (TS/Python) — docs: cursor.com/docs/cli/* + /docs/sdk
- **Category:** Agents → CLI/SDK companion to IDE agent
- **Type:** Commercial (plan-metered)
- **Official URL:** https://cursor.com/docs/cli/overview + https://cursor.com/docs/sdk (reference: CLI Capabilities/Changelog/Shell/ACP/Headless-CI)
- **Description:** Shell mode, ACP (Agent Client Protocol), headless/CI (`--print`-style non-interactive + JSON), Bridge; SDK mirrors agent tools for embedding; Teams/Enterprise controls carry over.
- **Contents inspected:** WebSearch-verified docs-hub excerpts (CLI section list: Installation/Capabilities/Changelog/Shell/ACP/Headless-CI/Reference; SDK TS/Python/Bridge/Changelog).
- **Capabilities:** Scripted edits/reviews in CI; editor↔CLI handoff.
- **Usage domain:** Cursor shops automating checks + bulk refactors.
- **Integration:** official
- **Compatibility:** Native. Evidence: docs nav exposes CLI + SDK subtrees.
- **Deps:** Cursor account; CI token.
- **Availability:** Bundled with Cursor install.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** CI least-privilege; gate auto-apply with review inbox.
- **Related:** Cloud Agents, MCP, review (13).
- **Sources:** cursor.com/docs/cli/*; cursor.com/docs/sdk.
- **Verification date:** 2026-10-09 · **Confidence:** Partially (hub nav verified; per-flag semantics not re-fetched this pass)

### 25 — AGENTS.md / rules conventions (portable repo instructions)
- **Canonical identity:** `pattern:agents-md` (OpenCode `/init` generates `AGENTS.md` · Claude `CLAUDE.md`+`.claude/rules/` · Cursor `.cursor/rules/*.mdc`+`AGENTS.md` · Windsurf `.windsurf/rules/`+`AGENTS.md` · Cline Rules · Codex `AGENTS.md`)
- **Category:** Agents → Portable instruction layer consumed by all harnesses
- **Type:** Open convention (+ per-agent rules engines)
- **Official URLs:** OpenCode init docs (opencode.ai/docs) ; Cursor: cursor.com/docs/rules ; Windsurf: docs.windsurf.com/windsurf/cascade/agents-md ; Cline: docs.cline.bot (Rules)
- **Description:** Markdown instructions auto-loaded by agent (root always-on; subdir glob-scoped in Windsurf); frontmatter controls (`description/globs/alwaysApply`, `Apply Intelligently/Manually`); commit to git for team consistency; `/init` bootstraps from repo analysis.
- **Contents inspected:** WebSearch-verified excerpts (OpenCode `/init`→AGENTS.md tip; Cursor `.mdc` anatomy + `AGENTS.md` alternative; Windsurf AGENTS.md→Rules-engine mapping).
- **Capabilities:** Single file steering every agent in this catalog.
- **Usage domain:** Baseline for spec-driven + harness runs (files 13–14).
- **Integration:** universal (all 9 agents read it)
- **Compatibility:** Compatible — evidence: three independent docs attest the same filename.
- **Deps:** None.
- **Availability:** Convention.
- **Maintenance:** Active.
- **License:** N/A (your content).
- **Security/limits:** Instructions are prompt, not policy — pair with permissions/hooks; don't paste secrets.
- **Related:** Rules, skills, MCP.
- **Sources:** See URLs.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

---

**Count: 25 resources** (meets 20+ minimum). No install/execute performed.
