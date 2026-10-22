# Deliverable F — Compatibility and Integration Index
**The Omniscient Resource Atlas · Built 2026-10-10**

Verified compatibility of resources with coding agents, protocols, frameworks, and environments. Classification per record; **no claim is upgraded beyond its evidence**. Generic protocol support (e.g., "speaks MCP") is not presented as proof that a particular integration was tested.

## Classification legend

| Class | Meaning |
|---|---|
| Native | Built for the host; first-party or host-documented support |
| Official integration | Vendor-maintained integration, documented by the vendor |
| Documented adapter / port | Third-party or community port with explicit install/usage docs |
| Open standard / protocol | Works via a shared open standard (Agent Skills SKILL.md, MCP, AGENTS.md, OpenAPI) — host-independent |
| Custom integration required | No ready-made path; wiring needed |
| Reference-only | Documentation/reference value; not consumed as a tool |
| Unverified | Claimed but not confirmed in this research |
| Incompatible / unavailable | Evidence of non-support |

## F1. Open standards — the shared protocol layer

These standards are the compatibility backbone; anything built on them works across hosts without per-host ports.

| Standard | What it is | Hosts with evidenced support |
|---|---|---|
| Agent Skills (SKILL.md, agentskills.io) | Open format: SKILL.md with name/description frontmatter; progressive disclosure (discover → activate → execute) | Claude Code, GitHub Copilot (CLI/VS Code/agents), OpenAI Codex, Cursor, Gemini CLI, OpenCode, OpenClaw, Windsurf, Antigravity — per agentskills.io client showcase and vendor skill repos (Verified) |
| MCP (Model Context Protocol) | Open JSON-RPC 2.0 protocol: hosts, clients, servers; tools/resources/prompts | Any MCP client (Claude Code, OpenCode, Cursor, Cline, Windsurf, VS Code, Zed, Amazon Q…) consumes any MCP server via standard config (Verified — protocol property, not per-integration testing) |
| AGENTS.md | Repo-level instruction file convention | OpenCode (native), Codex, and other agents read it natively; plain-markdown fallback elsewhere (Partially verified per host) |
| OpenAPI → MCP | OpenAPI specs converted to MCP servers (openapi-mcp-codegen, awslabs/openapi-mcp-server) | Any MCP client (Documented adapter pattern; DIY per-spec — Verified as a pattern) |
| DESIGN.md (`@google/design.md`) | Visual-identity file + lint/diff/export CLI | Any agent via shell-out / file read (Verified) |

## F2. Coding agents — extension surface and verified integrations

| Agent | Extension surface (evidenced) | Notable verified integrations |
|---|---|---|
| OpenCode (`sst/opencode`) | Plugins (JS/TS lifecycle hooks), Agent Skills (`~/.config/opencode/skills/`, `.agents/skills/`), subagents, slash commands, MCP (`opencode.json`), themes, headless (`run`/`serve`/`web`) | context7 (MCP), github/github-mcp-server (official OpenCode install guide), microsoft/playwright-mcp (opencode section in README), michaljach/opencode-browser (native plugin), 163-resource prior catalog (native/documented-adapter/open-standard) — Verified |
| Claude Code | Plugins, skills, subagents, hooks, slash commands, MCP, rules, marketplace | affaan-m/ECC via plugin `ecc@ecc`; ruvnet/ruflo via plugin + MCP server; anthropics/skills via marketplace; Leonxlnx/taste-skill via marketplace; Scrapling via MCP; stefandsl/notebooklm-skill (skill) — Verified |
| Cursor | Rules, subagents, skills, commands, hooks, plugins/marketplace, MCP, AGENTS.md | Leonxlnx/taste-skill (Agent Skill); Scrapling (MCP) — Verified |
| OpenAI Codex CLI | Skills, plugins, subagents, hooks, MCP, agents | Leonxlnx/taste-skill (Agent Skill); ruvnet/ruflo (native integration claimed) — Verified (skill), Partially (ruflo/Codex depth) |
| Antigravity CLI (`agy`, Google) | Plugins, skills, rules, hooks, custom agents, MCP | Successor to Gemini CLI (consumer Gemini CLI sunset 2026-06-18; Historical). Firecrawl agent skill lists Antigravity — Partially verified |
| GitHub Copilot (CLI + VS Code) | Custom agents, skills, hooks, plugins, MCP, instructions | Agent Skills client per agentskills.io (Verified) |
| Windsurf / Cascade → Devin Desktop | (Rebranded; `.devin/rules/` preferred) | Historical rename — verify current extension docs before use |
| Cline / Roo Code / Kilo Code / Crush / Aider / Amp / Goose / Continue.dev / Kimi Code CLI / Factory Droid / Pi / Qwen Code | Per-agent extension hosts (rules, modes, MCP, skills, checkpoints — see B3) | MCP-based integrations generally applicable via open standard; per-tool native support varies — see source catalog `03b-agents.md` |

## F3. Selected resources — integration type and verified hosts

| Resource | Integration type | Verified hosts / notes | Status |
|---|---|---|---|
| facebook/astryx | CLI bash calls only (`npx @astryxdesign/cli … --dense`); **no MCP server** | Any agent with shell access (bash tool). No MCP, no native plugin — Corrected per Phase-8 direct fetch | Verified |
| upstash/context7 | MCP server (remote `https://mcp.context7.com/mcp` or local `npx`) | OpenCode (explicit install docs); any MCP client via open standard | Verified |
| anthropics/skills | Claude Code plugin marketplace; portable SKILL.md | Claude Code (native); other Agent-Skills hosts via open standard | Verified |
| ComposioHQ/awesome-claude-skills | SKILL.md folders; `npx skills add` | Claude Code, Cursor, Copilot, Codex, Gemini CLI, OpenCode (per repo topics) | Verified |
| Leonxlnx/taste-skill | Agent Skills (`npx skills add`); Claude Code plugin marketplace | Claude Code, Codex, Cursor, Copilot; framework-agnostic (React/Vue/Svelte) | Verified |
| vercel-labs/agent-skills (+ `vercel-labs/skills` CLI) | Skill collection; `skills.sh` / `npx skills add` | Agent-Skills-compatible hosts | Verified |
| microsoft/skills, supabase/agent-skills, stripe/ai, expo/skills, angular/skills, cloudflare/skills, hashicorp/agent-skills, getsentry/skills, huggingface/skills, neondatabase/agent-skills, netlify/context-and-tools | Official vendor skill collections (SKILL.md) | Vendor-named hosts per repo; cross-host via open standard | Verified (existence + vendor claim) |
| ruvnet/ruflo (ex-Claude Flow) | CLI (`npx ruflo init`); MCP server (314 tools); Claude Code plugin | Claude Code (plugin + MCP); Codex (native per project); OpenCode via MCP bridge (open standard) | Verified |
| affaan-m/ECC | Claude Code plugin (`ecc@ecc`); npm `ecc-universal` | Claude Code (native); Cursor, OpenCode, Codex, Gemini, Antigravity (compatible harnesses per project) | Verified |
| firecrawl/firecrawl | REST API (`api.firecrawl.dev/v2`); SDKs (Python/Node/Go/Java/Elixir/Rust/Ruby/.NET/PHP); MCP server (`npx -y firecrawl-mcp`); Agent Skill; CLI | Hosted or self-hosted (Docker); skill lists Claude Code, Antigravity, OpenCode | Verified |
| volcengine/OpenViking | Hooks + MCP; SDKs (Python/Go/TS); Rust CLI | Claude Code, Codex, Cursor, TRAE, OpenCode, OpenClaw (per README) | Verified |
| D4Vinci/Scrapling | MCP server; bundled agent skill; pip/Docker | Claude/Cursor/etc. via MCP (per README) | Verified |
| vercel/eve | TypeScript framework (`npx eve@latest init`); deploy to Vercel | Model-agnostic via Vercel AI Gateway; Slack/Discord/web channels | Verified |
| vercel-labs/deepsec | TypeScript CLI (`npx deepsec init`); uses user's Claude/Codex CLIs | Bring-your-own Claude/Codex subscriptions; Vercel Sandbox fanout optional | Verified |
| stefandsl/notebooklm-skill | Agent Skill; depends on teng-lin/notebooklm-py | Claude (claude.ai/code); unofficial RPC dependency (breakage risk) | Verified (unofficial dependency preserved) |
| google-labs-code/design.md | CLI (`npx @google/design.md lint`) | Any agent via shell-out | Verified |
| shadcn MCP | Official remote MCP; community `@jpisnice/shadcn-ui-mcp-server` | Any MCP client | Verified |
| microsoft/playwright-mcp | MCP server | Official README documents OpenCode usage | Verified |
| michaljach/opencode-browser | OpenCode plugin wrapping browsermcp.io | OpenCode (native) | Verified |
| public-apis/public-apis | None (documentation resource) | Reference-only for any developer/agent workflow | Verified |
| anthropics/claude-cookbooks | Notebooks + scripts (reference repo) | Reference-only; needs Claude API key | Verified |
| OpenBMB/ChatDev (2.0 = DevAll) | Self-hosted web app (React + Python) | GPT-4o/4o-mini and other models | Verified |
| jeffreycayao/munder-difflin | Desktop harness wrapping CLIs | Claude Code, Antigravity, Codex, Grok, Kimi Code, Gemini CLI, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, Cursor | Verified |
| obra/superpowers | SKILL.md methodology (14 skills) | OpenCode (dedicated install docs); Agent-Skills hosts via open standard | Verified |
| mattpocock/skills | SKILL.md via `npx skills add` | `.agents/skills/` hosts (open standard) | Verified |
| thedotmack/claude-mem | Native plugin (`npx claude-mem install --ide opencode`) | OpenCode (explicit flag) | Verified |
| mvanhorn/last30days-skill | SKILL.md via `npx skills add` | Open-standard hosts | Verified |
| Forward-Future/loopy | SKILL.md (no opencode.json entry needed) | Agent-Skills hosts; writes LOOPS.md | Verified |
| cobusgreyling/loop-engineering | CLI (`loop-init`, `loop-audit`, `loop-doctor`, `loop-cost`) | GitHub Actions, OpenCode, Claude Code (per project) | Verified |
| Graphify-Labs/graphify | Native OpenCode skill + `/graphify` command | OpenCode (explicit) | Verified |
| keysjoao/laws-of-ux-skills | SKILL.md drop-in | `.opencode/skills/` / `~/.config/opencode/skills/` | Verified |
| remorses/opencode-injection-guard | OpenCode plugin (`tool.execute.after` hook) | OpenCode (native) | Verified |
| boxpositron/envsitter-guard | OpenCode plugin (tool interception on `.env*`) | OpenCode (native) | Verified |
| ngmeyer/council-review | Claude Code skill (standalone) | Claude Code; parallel to ngmeyer/skills monorepo | Verified (LIVE — not archived) |
| KanakMalpani/Loop-Engineering | Framework repo (CLI/patterns) | Separate from LoopBench (benchmark suite) | Verified |
| open-gsd/gsd-core | Community fork (audited) | Safe replacement for archived gsd-build/get-shit-done | Verified |

## F4. Explicitly non-integrations (do not assume)

- Astryx ↔ MCP: **no MCP server exists** (Phase-8 direct fetch; re-confirmed 2026-10-10).
- vercel/eve ↔ OpenCode: **reference-only / parallel ecosystem** — Eve is an agent-*building* framework, not an OpenCode extension.
- n8n ↔ OpenCode: **no official pipeline import path** (ecosystem gap; community nodes unofficial).
- Antigravity IDE DOM ↔ OpenCode terminal: **no native zero-config link** (gap; Puppeteer/Playwright MCP bridge is the workaround).
- Generic protocol support ≠ tested integration: e.g., "any MCP server works with OpenCode" is a protocol property; per-server behavior still needs its own verification.

## F5. Compatibility claims requiring more evidence (do not rely on yet)

- garrytan/gstack with OpenCode: mixed evidence (Phase-5 says compatible; Element-1 sweep excluded as Claude-Code-only) — Unresolved.
- Windsurf Cascade's current extension surface post-rebrand to Devin Desktop — verify current docs.
- Antigravity CLI (`agy`) plugin/skill details — primary JS docs not fetched in this pass.
- Factory Droid, Qwen Code, Pi agent extension internals — secondary evidence only.
- Xata managed-database status (shutdown rumors vs 2026 listings) — Unresolved.
