# Phase 0 — Inventory of Existing Research

**Built:** 2026-10-10 (coordinator) from all files in `~/workspace/user/files/`
**Source dates:** catalog sweep 2026-08-07/08; Phase 0 verification 2026-08-09; architecture decisions 2026-08-10; Phase 8 corrections 2026-08-11.
**Filter of the original research:** OpenCode-supporting resources only (natively, via documented adapter/port, or via open cross-tool standard). The Atlas widens scope to the whole web-dev/agent ecosystem; items below are the known base to dedupe against.

---

## 1. Grand totals from prior research

| Metric | Value |
|---|---|
| Catalog sweep elements | 26 |
| Usable resources | 163 |
| Excluded (Claude-Code-only) | 43 |
| Phase-5 named resources (5-point breakdowns) | 20 |

---

## 2. Phase-5 named resources (20) — name, canonical URL, status

| # | Name | Canonical URL | Status (2026-08) |
|---|---|---|---|
| 1 | Graphify-Labs/graphify | https://github.com/Graphify-Labs/graphify | Verified (104k+ stars; `/graphify` command; OpenCode native) |
| 2 | ruvnet/ruflo (formerly "Claude Flow") | https://github.com/ruvnet/ruflo | Verified; Corrected from "ruflo" (61k–67k stars; swarm meta-harness) |
| 3 | emilkowalski/skills | https://github.com/emilkowalski/skills | Verified; Corrected from "enilkowaski" (apple-design skill, WWDC principles) |
| 4 | teng-lin/notebooklm-py | https://github.com/teng-lin/notebooklm-py | Verified but UNOFFICIAL — reverse-engineers undocumented Google RPCs; breakage risk |
| 5 | vercel/eve | https://github.com/vercel/eve | Verified (filesystem-first durable agent framework, June 2026) |
| 6 | vercel/deepsec | https://github.com/vercel/deepsec | Verified (self-hosted agentic security scanner; high API-cost warning) — watchstream 14 later re-verified org as **vercel-labs/deepsec** |
| 7 | thedotmack/claude-mem | https://github.com/thedotmack/claude-mem | Verified (persistent memory plugin; `npx claude-mem install --ide opencode`) |
| 8 | mvanhorn/last30days-skill | https://github.com/mvanhorn/last30days-skill | Verified (last-30-days web research skill) |
| 9 | cobusgreyling/loop-engineering | https://github.com/cobusgreyling/loop-engineering | Verified (`loop-init`, `loop-audit`, `loop-doctor`, `loop-cost`) |
| 10 | KanakMalpani/LoopBench | https://github.com/KanakMalpani/LoopBench | Verified; Corrected (benchmark suite, not framework) |
| 11 | Forward-Future/loopy | https://github.com/Forward-Future/loopy | Verified (SKILL — Loop Library companion; 9 paths: Discover/Find/Audit/Adapt/Craft/Run/Debrief/Save/Publish; writes LOOPS.md; no opencode.json entry needed) |
| 12 | huangruiteng/loopx | https://github.com/huangruiteng/loopx | Verified (state kernel; EXCLUDED from final architecture — dual-source-of-truth problem) |
| 13 | baidu-baige/LoongFlow | https://github.com/baidu-baige/LoongFlow | Verified (evolutionary PES loop; arXiv 2512.24077; math/ML specialist) |
| 14 | gsd-build/get-shit-done | https://github.com/gsd-build/get-shit-done | **ARCHIVED June 2026 — SECURITY WARNING** (deep shell permissions; do NOT use) |
| 14b | open-gsd/gsd-core | https://github.com/open-gsd/gsd-core | Verified — safe community fork ("Git. Ship. Done - Core") |
| 15 | mattpocock/skills | https://github.com/mattpocock/skills | Verified (SDLC skills) |
| 16 | obra/superpowers | https://github.com/obra/superpowers | Verified (14-skill dev methodology; OpenCode native install) |
| 17 | garrytan/gstack | https://github.com/garrytan/gstack | Verified (startup-role skills + headless Chromium `/qa`) — note: also listed as Claude-Code-primary in catalog sweep; mixed evidence |
| 18 | public-apis/public-apis | https://github.com/public-apis/public-apis | Verified (free public API reference index; reference-only) |
| 19 | asgeirtj/system_prompts_leaks | https://github.com/asgeirtj/system_prompts_leaks | Verified; Corrected path — `Anthropic/claude-fable-5.md` is in `Anthropic/` subfolder, not root; unofficial extracted prompts |
| 20 | anthropics/claude-cookbooks | https://github.com/anthropics/claude-cookbooks | Verified (official; org is "anthropics" with s) |

---

## 3. Other individually verified resources (Phases 0–8)

| Name | URL | Status/notes |
|---|---|---|
| facebook/astryx | https://github.com/facebook/astryx | Verified live; Meta agent-ready React design system (June 2026, MIT); **NO MCP server** (Phase 8, 2026-08-11: `packages/mcp-server` and `packages/mcp` 404; CLI README has zero MCP refs). Integration = bash calls: `npx @astryxdesign/cli <cmd> --dense` |
| @astryxdesign/cli | npm | Verified; commands: blog, build, component, discover, docs, doctor, hook, init, layout, search, swizzle, template, theme, upgrade, validate-integration — NO "mcp" subcommand |
| karpathy/llm-council | https://github.com/karpathy/llm-council | Verified (weekend hack, OpenRouter-native, unmaintained by design) |
| ngmeyer/council-review | https://github.com/ngmeyer/council-review | **Corrected: LIVE and active** (not archived); standalone council skill |
| ngmeyer/skills | https://github.com/ngmeyer/skills | Verified; monorepo parallel to council-review (devil's advocate, theatrical-consensus detector, sycophancy guardrail) |
| walkinglabs/learn-harness-engineering | https://github.com/walkinglabs/learn-harness-engineering | Verified; harness templates: AGENTS.md, feature_list.json, claude-progress.md, init.sh. Five subsystems: Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff |
| KanakMalpani/Loop-Engineering | https://github.com/KanakMalpani/Loop-Engineering | **Corrected: LIVE** (framework repo; separate from LoopBench) |
| upstash/context7 | https://github.com/upstash/context7 | Verified (docs MCP: resolve-library-id, get-library-docs) |
| shadcn MCP | https://www.shadcn.io/api/mcp | Verified (official remote MCP) + community `@jpisnice/shadcn-ui-mcp-server` |
| keysjoao/laws-of-ux-skills | https://github.com/keysjoao/laws-of-ux-skills | Verified (Advisor/Audit/Pre-ship Checklist skills) |
| VoltAgent/awesome-design-md | https://github.com/VoltAgent/awesome-design-md | Verified (brand DESIGN.md collection; Google format; `npx @google/design.md lint`) |
| microsoft/playwright-mcp | https://github.com/microsoft/playwright-mcp | Verified (official; opencode section in README) |
| michaljach/opencode-browser | https://github.com/michaljach/opencode-browser | Verified (OpenCode plugin wrapping browsermcp.io; v0.1.3 pinned) |
| remorses/opencode-injection-guard | https://github.com/remorses/opencode-injection-guard | Verified (tool.execute.after judge-model injection guard) |
| boxpositron/envsitter-guard | https://github.com/boxpositron/envsitter-guard | Verified (.env* protection plugin) |
| tickernelz/opencode-mem | https://github.com/tickernelz/opencode-mem | Verified (vector memory; web UI 127.0.0.1:4747) |
| Opencode-DCP/opencode-dynamic-context-pruning | https://github.com/Opencode-DCP/opencode-dynamic-context-pruning | Verified (now maintenance mode; successor "Sleev" per README) |
| anthropics/skills | https://github.com/anthropics/skills | Verified (official Agent Skills repo + spec) |
| agentskills/agentskills | https://github.com/agentskills/agentskills | Verified (official Agent Skills spec) |
| lawsofux.com | https://lawsofux.com | Verified (reference-only) |
| alexpate/awesome-design-systems | https://github.com/alexpate/awesome-design-systems | Verified (~25k stars; reference list) |
| gztchan/awesome-design | https://github.com/gztchan/awesome-design | Verified (~17.4k stars; reference list) |
| pmndrs/react-three-start | https://github.com/pmndrs/react-three-start | Verified (file-based R3F meta-framework) |
| pmndrs/react-three-next | https://github.com/pmndrs/react-three-next | Verified (R3F + Next.js template) |
| cnoe-io/openapi-mcp-codegen | https://github.com/cnoe-io/openapi-mcp-codegen | Verified (OpenAPI→MCP codegen) |
| awslabs/openapi-mcp-server | https://github.com/awslabs/openapi-mcp-server | Verified (OpenAPI proxy MCP server) |
| cobusgreyling/goal-engineering | (same author as loop-engineering) | Verified real; NOT adopted (GOAL.md = second state file) |

---

## 4. 26-element catalog — key resources per element

Element 1 — Skills (14 usable): obra/superpowers, anthropics/skills, mattpocock/skills, addyosmani/agent-skills, [REDACTED-caveman], hardikpandya/stop-slop, Gentleman-Programming/Gentleman-Skills, VoltAgent/awesome-agent-skills, cloudflare/skills, composiohq/skills, waybarrios/opencode-power-pack, hqhq1025/skill-optimizer, glebis/claude-skills, agentskills/agentskills; smaller: alirezarezvani/claude-skills, steipete/agent-rules, FrancyJGLisboa/agent-skill-creator, tripleyak/SkillForge, NeoLabHQ skills, shanraisshan/claude-code-best-practice, alirezarezvani/claude-code-skill-factory.
Element 2 — Permission modes (4): OpenCode native permissions, joelhooks/opencode-config, kdcokenny/opencode-workspace, boxpositron/envsitter-guard; second sweep adds NjengaFelix/opencode-permissions, aminroosta macOS seatbelt guide, issue #7928 (Shift+Tab request).
Element 3 — Checkpoints/rewind (3): OpenCode /undo, @arkfactory/opencode-checkpoint, witlox/opencode-checkpoint; second sweep adds entireio/cli (4.3k★, native OpenCode plugin in preview), KyungJunAn/opencode-rewind, issues #29980 (/rewind request), #7553 (snapshot API proposal).
Element 4 — Context management (15): Opencode-DCP, tickernelz/opencode-mem, 0xranx/OpenContext, upstash/context7, code-yeongyu/oh-my-openagent, alvinunreal/oh-my-opencode-slim, kdcokenny/opencode-background-agents, derekbar90/opencode-conductor, IgorWarzocha/Opencode-Context-Analysis-Plugin, oc-mnemoria, supamem, Hipocampo, opencode-short-term-memory, MrDoe/OpenCodeRAG, opencode-skillful; second sweep adds cortexkit/magic-context, g1331/opencode-magic-context, aerovato/magic-compact.
Element 5 — Hooks (6): oh-my-openagent (54+ hooks), oh-my-opencode-slim, smartfrog/opencode-froggy, Opencode Hooks Plugin, hcom, FlowDeck; second sweep notes opensoft/oh-my-opencode is a fork/mirror, Anthropic OAuth restriction citing oh-my-openagent.
Element 6 — MCP servers (9 + whole ecosystem): upstash/context7, AlaeddineMessadi/opencode-mcp, ajhcs/Better-OpenCodeMCP, Ejentum, SwarmVault, supamem, OpenCode Chromium Browser Plugin, Dodo Payments MCP, OpenCode Claude Memory; second sweep adds github/github-mcp-server (official OpenCode install guide, 27.4k★), Traves-Theberge/opencode-mcp, sandbox-technologies/opencode-docs-mcp, issue #27809 (mcpServers key naming).
Element 7 — Sandboxing (3): fabianlema/opencode-sandbox, athal7/opencode-devcontainers, jailoc; second sweep adds OpenCode native OS-level sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt — CONTRADICTS first-pass "no built-in sandboxing" claim), Docker Sandboxes initiative, npm opencode-sandbox (bubblewrap plugin), thisisryanswift/opencode-sandbox, comsysto/opencode-sandbox, mattolson/agent-sandbox (agentbox, OpenCode docs), rivet-dev/sandbox-agent (/opencode endpoint), arezi/julscsl/zaid-marji opencode-sandbox variants, NVIDIA OpenShell (partial).
Element 8 — Subagents (15): ankitmundada/awesome-opencode-subagents, oh-my-openagent, oh-my-opencode-slim, kdcokenny/opencode-workspace, NERV, hiai-opencode, Open Conclave, CrewBee, OpenCode Ensemble, Pocket Universe, Gem Team, deliberation, Python Expert Agent, OpenCode Agents, Agentic; second sweep adds OpenAgentsControl subagents, excludes jbeck018/agents-opencode (misleading name — actually Claude Code fork).
Element 9 — Plugins/marketplaces (6): awesome-opencode/awesome-opencode, CKGrafico/opencode-market, NikiforovAll/opencode-marketplace, kdcokenny/ocx, OpenCode Manager (chriswritescode-dev), opencode-agent-for-cowork; second sweep adds Tommertom/opencode-plugin-marketplace, numman-ali/n-skills.
Element 10 — Output styles (8): ajaxdude/opencode-ai-poimandres-theme, VS Code Themes for OpenCode, OpenCode Light Themes (21), Ayu/Charcoal/Lavi/Moonlight themes, @franlol/opencode-md-table-formatter. CONTRADICTION: second sweep says genuine GAP — these are TUI themes, not Claude-Code-style output-style switching (issue #5199 open). Both facts preserved.
Element 11 — Background tasks (7): kdcokenny/opencode-background-agents, zenobi-us/opencode-background, server-manager, opencode-scheduler, opencode-notify, Pilot; second sweep adds zeigarnick/opencode-background-task, issues #5887/#1970/#15069/#5826 (native gap).
Element 12 — Security review (6): alibaba/open-code-review, waybarrios/opencode-power-pack (/security-review), opencode-review, OpenCode Swarm, boxpositron/envsitter-guard, darrenhinde/OpenAgentsControl; second sweep adds red-orbita/opencode-security-agent, IgorWarzocha security-reviewer agent; warns: spencermarx/open-code-review is a DIFFERENT Claude-Code-only project (name collision).
Element 13 — Headless/CI (6): OpenCode native run/serve/web/github, wesammustafa/opencode-primer, OpenCode Manager, AlaeddineMessadi/opencode-mcp, Subagent Reporter, opencode-plugin-otel; second sweep adds opencode-shell-strategy (PR #5995), issue #28407 (headless session bug).
Element 14 — Usage/cost tracking (11): eserete/opencode-token-tracker, opgginc/opencode-bar, ramtinJ95/opencode-tokenscope, Token Monitor, OpenCode Throughput, Opencode Quota, Opencode Usage Monitor, Opencode Telemetry, opencode-mystatus, Langfuse OpenCode Observability, pai4451/opencode-telemetry-plugin; second sweep adds heyhuynhgiabuu/ocsight, Ainsley0917/opencode-token-monitor, gaboe/opencode-usage, Cateds/opencode-stats, touchkale/opencode-dashboard, tongsh6/opencode-token-tracker.
Element 15 — Agent-team frameworks (17): oh-my-openagent, oh-my-opencode-slim, kdcokenny/opencode-workspace, OpenAgentsControl, agnusdei1207/opencode-orchestrator, NERV, hiai-opencode, CrewBee, OpenCode Ensemble, Open Conclave, OpenCode Swarm, FlowDeck, Open Dynamic Workflows, Gem Team, Pocket Universe, deliberation, smtg-ai/claude-squad, Baton (mraza007, claimed); second sweep adds Orkas-AI/Orkas, ZaxbyHub/opencode-swarm, ex-machina-co/opencode-orca, stablyai/orca, BloopAI/vibe-kanban, AgentWrapper/agent-orchestrator, shire/tutti/opengoat (claimed, unverified), Dex.
Element 16 — Workflow orchestration (12): mark-hingston/opencode-workflows, derekbar90/opencode-conductor, FlowDeck, Open Dynamic Workflows, opencode-bmad-workflow, GoopSpec, NERV, OpenCode Swarm, Subtask2, ForLoop Planner, open-plan-annotator, Opencode Roadmap; second sweep adds travisliu/open-dynamic-workflow, jcarlosrodicio/opencode-agent-orchestration-kit, IgorWarzocha/Opencode-Workflows (Ralph Wiggum loop), agents-to-go/opencode-orch-mode.
Element 17 — Agent SDKs (3): anomalyco/opencode-sdk-js, anomalyco/opencode-sdk-go, Acksell/opencode-go-sdk. DISCREPANCY: second sweep says official SDK is `@opencode-ai/sdk` (opencode.ai/docs/sdk); relationship to anomalyco repos unclear — flag as unresolved.
Element 18 — Discipline/skill packs (4): obra/superpowers, waybarrios/opencode-power-pack, meaningfy-ws/skillery, DietrichGebert/ponytail; second sweep adds K-Dense-AI/science-superpowers (claimed but unverified OpenCode path).
Element 19 — Docs-context MCP (3): upstash/context7, sandbox-technologies/opencode-docs-mcp, bgauryy/open-docs; second sweep adds arabold/docs-mcp-server, DeepWiki, Docfork, Ref Tools, Rtfmbro, GitMCP, Grep MCP, Nia, Deepcon.
Element 20 — Statusline (3): Joaquinvesapa/sub-agent-statusline, eserete/opencode-token-tracker, OpenCode native status bar; second sweep adds amirlehmam/ocstatusline, markwilkening21/opencode-status-line, aacassandra/opencode-status-bar; issues #30295 (Closed per search — check), #23539, #8619.
Element 21 — Git-worktree helpers (3): kdcokenny/opencode-worktree, felixAnhalt/opencode-worktree-session, athal7/opencode-devcontainers; second sweep adds git-worktree-runner (CodeRabbit, explicit Opencode support), agentree, worktree-cli, gwq, issue #12896.
Element 22 — Awesome-lists (5): bradAGI/awesome-cli-coding-agents, ai-for-developers/awesome-ai-coding-tools, kyrolabs/awesome-agents, awesome-opencode/awesome-opencode, GetBindu/awesome-claude-code-and-skills, ai-boost/awesome-harness-engineering; second sweep adds hashgraph-online/awesome-ai-plugins, gmh5225/awesome-skills, RoggeOhta/awesome-codex-cli, jqueryscript/awesome-claude-code.
Element 23 — Security scanners for configs (3): sandervandegeijn/code-security-scanner, zm2231/z-audit, remorses/opencode-injection-guard; second sweep adds Pantheon-Security/medusa (claimed but unverified .opencode/ coverage), alonw0/secure-skills (npx skillsio, OpenCode named).
Element 24 — Safety-net/guardrails (5): remorses/opencode-injection-guard, boxpositron/envsitter-guard, Greywall, daytonaio/daytona plugin (repo no longer maintained), FlowDeck safety layer; second sweep adds kenryu42/cc-safety-net (10 CLIs incl. OpenCode; `opencode plugin -g -f cc-safety-net@latest`), AlexMikhalev Destructive Command Guard gist, openguardrails.com.
Element 25 — Hook management CLIs (2): Opencode Hooks Plugin, OpenCode native plugin system; second sweep adds bopen-tools hook-manager (via claudepluginhub).
Element 26 — Self-improving/instinct-mining (3): okdk7788/opencode-self-improving-skills, hqhq1025/skill-optimizer, thousandflowers/skillreaper; second sweep adds Kulaxyz/self-learning-skills, leohuang8688/self-improving-agent (OpenClaw skill — claimed but unverified OpenCode path).

Excluded as Claude-Code-only (43 total; key ones): garrytan/gstack (mixed evidence — see discrepancy), hesreallyhim/awesome-claude-code, VoltAgent/awesome-claude-code-subagents, ComposioHQ/awesome-claude-skills, travisvn/awesome-claude-skills, Anthropic claude-code-security-review, AgentLint, pi-rewind, claudebox, Claude Code /rewind, native hooks, statusLine, output styles, Vibe Kanban (community-maintained), Microsoft Conductor, Code Conductor, Anthropic Agents SDK, Claude Code SDK.

---

## 5. Corrections and contradictions (preserve — do NOT silently resolve)

| # | Original claim | Corrected/current finding | Source/date |
|---|---|---|---|
| C1 | "Astryx ships MCP server" (02-ui-ux.md §A) | WRONG. Phase 8 direct fetch (2026-08-11): no `packages/mcp-server`, no `packages/mcp`, CLI README zero MCP refs, no "mcp" subcommand. Integration = bash calls. Watchstream 14 re-confirmed 2026-10-10. | 08-astryx-mcp.md |
| C2 | "ngmeyer/council-review archived" (00-verification.md) | WRONG. Corrected 2026-08-09: LIVE and active; parallel to ngmeyer/skills monorepo. | 06-unfound-and-gaps.md |
| C3 | "KanakMalpani/Loop-Engineering does not exist" (00-gaps) | WRONG. Corrected 2026-08-09: LIVE; framework repo, separate from LoopBench. | 06-unfound-and-gaps.md |
| C4 | okjpg/llm-council | Unverifiable handle; skip unless exact URL provided. | 00-verification.md |
| C5 | "OpenCode has no built-in sandboxing" (Element 7, first pass) | CONTRADICTED by second sweep: OpenCode has native OS-level sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt, `packages/opencode/src/sandbox/`). Both statements preserved; resolve in Atlas. | catalog.md Element 7 |
| C6 | Element 10 "Output Styles" (8 themes listed) | CONTRADICTED by second sweep: themes ≠ Claude-Code output-style switching; genuine gap (issue #5199 open). Both preserved; resolve in Atlas. | catalog.md Element 10 |
| C7 | Official OpenCode SDK identity | First pass: anomalyco/opencode-sdk-js (+go). Second sweep: official SDK is `@opencode-ai/sdk` (opencode.ai/docs/sdk). Relationship unclear — UNRESOLVED, flag for Atlas. | catalog.md Element 17 |
| C8 | garrytan/gstack | Listed as OpenCode-compatible (Phase 5) AND as Claude-Code-only excluded (Element 1) — mixed evidence; UNRESOLVED. | 05-remaining-resources.md vs catalog.md |
| C9 | Issue #30295 (custom statusLine) | First pass: open. Second sweep: shows "Closed" in search with auto-close label — may be process-closure not resolution; UNRESOLVED. | catalog.md Element 20 |
| C10 | Context7 star counts | 7,072 (Aug 2026 first pass) vs 39.3k+ (second sweep) — growth over time, not contradiction. | catalog.md |
| C11 | obra/superpowers star counts | 89K (Mar) → 129K (Apr) → 224K (Jun) → 211K (Aug) — growth; minor variance is source-date noise. | catalog.md |
| C12 | walkinglabs "five layers" URL | URL live but file = Template Guide, not the framework; canonical layer names differ (Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff). | 00-verification.md §C |
| C13 | "Krim Shoair" (Scrapling author) | Corrected to **Karim Shoair** (GitHub D4Vinci) by watchstream 14, 2026-10-10. | named-watchlist.md |
| C14 | vercel/deepsec org | Corrected to **vercel-labs/deepsec** by watchstream 14, 2026-10-10. | named-watchlist.md |
| C15 | "PizzaBox by AWS" | Corrected: no such project; evidence points to AWS **Pizza Bot** (Sept 2026) — watchstream 14, 2026-10-10. | named-watchlist.md |
| C16 | "Everything Claude Code" | Name officially retired; repo renamed **affaan-m/ECC** — watchstream 14, 2026-10-10. | named-watchlist.md |

---

## 6. Unverified names / unresolved identities

- okjpg/llm-council — not found (likely voice-to-text distortion).
- "Designs" (watchlist item 16) — UNRESOLVED 2026-10-10 (too generic, no match).
- Backend design skill — UNRESOLVED 2026-10-10 (5 distinct author implementations, no canonical match).
- Frontend design skill — PARTIALLY verified (candidate: anthropics/skills `frontend-design`, mirrors only).
- Strix — PARTIALLY verified (primary candidate usestrix/strix, 67k stars + Wikipedia; alternatives strixgov/strix, strixproject/Strix, mythicalsign/strix).
- jbeck018/agents-opencode — EXCLUDED (misleading name; actually Claude Code fork wshobson/agents).
- spencermarx/open-code-review — different Claude-Code-only project; do NOT confuse with alibaba/open-code-review.
- leohuang8688/self-improving-agent — OpenClaw-only; OpenCode path unverified.
- K-Dense-AI/science-superpowers — OpenCode path unverified.
- Baton (mraza007) — OpenCode support claimed but unverified.
- shire / tutti / opengoat — claimed from curated lists, unverified.
- Nia (27% perf claim), Deepcon (90% vs 65% claim) — self-reported, unverified.
- Issue #28407 (opencode run headless session bug) — flagged, not resolved.

## 7. Archived / inaccessible / unsafe items

- **gsd-build/get-shit-done** — ARCHIVED June 2026 + SECURITY WARNING (deep shell permissions, "rug-pull" trust reports). DO NOT USE. Safe fork: open-gsd/gsd-core.
- **okjpg/llm-council** — inaccessible/nonexistent.
- **daytonaio/daytona** — repo no longer maintained (plugin functional).
- **get-shit-done-redux** — community fork, status unverified.
- Opencode-DCP — maintenance mode (successor "Sleev" per README).

## 8. Missing categories / ecosystem gaps (honest, evidence-based)

1. No turnkey backend equivalent of Astryx (agent-readable, opinionated backend schema/design grounding).
2. No native zero-config OpenCode ↔ Antigravity terminal/DOM integration.
3. No official n8n ↔ OpenCode pipeline import path (wrong direction of control; community nodes unofficial).
4. No centralized official OpenCode plugin marketplace (issue #7467 open).
5. No customizable statusLine shell hook in OpenCode (#30295, #8619).
6. No official Python SDK for OpenCode (#4031 open).
7. No config linter for opencode.json security settings.
8. No output-styles feature in OpenCode (#5199 open).
9. No native true async/background subagent dispatch (#5887, #1970, #15069, #5826 open).
10. No native git-worktree automation (#12896 open).

## 9. Open research questions for the Atlas

- Q1: Resolve OpenCode sandbox contradiction (C5) — is the native sandbox widely enabled/relied upon, or is "no built-in sandboxing" still the practical truth?
- Q2: Resolve output-styles gap (C6) — has any plugin built a style switcher on experimental.chat.system.transform?
- Q3: Resolve SDK identity (C7) — @opencode-ai/sdk vs anomalyco repos.
- Q4: Resolve gstack status (C8) — OpenCode-compatible or Claude-Code-only?
- Q5: Resolve #30295 status (C9).
- Q6: Backend Astryx equivalent — still a gap, or new entrants in 2026-10?
- Q7: "Designs" and "Backend design skill" watchlist items — still unresolved.
- Q8: teng-lin/notebooklm-py — still live in Oct 2026? (Google RPC breakage risk).

---

## 10. Verification date index

- 2026-08-07/08 — catalog sweep (26 elements)
- 2026-08-09 — Phase 0 verification, 02-ui-ux, 03-multi-agent-council, 04-harness, 05-remaining-resources, 06-unfound-and-gaps
- 2026-08-10 — architecture decisions Q1–Q5
- 2026-08-11 — Phase 8 corrections (Astryx MCP, loopy, pre-commit, testing/QA)
- 2026-10-10 — watchstream 14 (named watchlist) completed; this inventory built
