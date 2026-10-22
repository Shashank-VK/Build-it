# Phase 0 — Source Inventory (Read-Only)

**Role:** Librarian-Phase0 — read-only research, no installs/executions.
**Source folder:** `/mnt/c/Users/Shashank Karamudi/Desktop/projects/opencode-research`
**Date inventoried:** 2026-10-09
**Files read:** 23 / 23 (5 root + 13 research/ + 5 harness-templates/)
**Large-file pagination:** catalog.md 2994 lines, BUILD-PROMPT-FINAL.md 2261 lines, BUILD-PROMPT-UNIVERSAL.md 2072 lines — all read to EOF via offset pagination.

## Source file map (all 23)

| # | File | Lines | Role |
|---|---|---|---|
| 1 | README.md | 162 | Phase tracker, directory map, key corrections table, architecture decisions |
| 2 | catalog.md | 2994 | Master index: 26 elements, 163 usable + 43 excluded; Elements 1–26 full text + appended discovery sweep (Elements 2–26 second pass + Element 1 tail) |
| 3 | verification.md | 75 | Final verification checklist: 26 elements → build prompt mapping, selected toolkit table, harness templates table |
| 4 | BUILD-PROMPT-FINAL.md | 2261 | Phases 1–5 (OpenCode-specific build): foundation, loops, council/Astryx/testing, context/commands/security, mass-install TOOL_CATALOG |
| 5 | BUILD-PROMPT-UNIVERSAL.md | 2072 | Phases 1–5 (tool-agnostic build): Tool Discovery Protocol, same stack, two-tier library + promote-skill, full TOOL_CATALOG |
| 6 | research/00-verification.md | 83 | Phase 0 verification report, session 2026-08-09, Sections A–E |
| 7 | research/00-gaps-and-unknowns.md | 67 | Phase 0 gaps log |
| 8 | research/01-existing-summary.md | 224 | All 26 elements summarized, 163 usable / 43 excluded |
| 9 | research/02-ui-ux.md | 250 | Astryx, design resources, backend gap, 3D templates |
| 10 | research/03-multi-agent-council.md | 192 | Council forks, n8n verdict, ensemble research, Two-Judge config |
| 11 | research/04-harness-environment.md | 173 | Antigravity bridge, slash commands, proxy verdict, DoD template, harness evolution, context anxiety |
| 12 | research/05-remaining-resources.md | 214 | 20 verified named resources, 5-point breakdowns each |
| 13 | research/06-unfound-and-gaps.md | 60 | Corrections log (both-live fixes) + 7 ecosystem gaps |
| 14 | research/07-autonomous-agent-architecture.md | 342 | FINAL architecture, Q1–Q5 decisions locked 2026-08-10, Phase 8 corrections 2026-08-11 |
| 15 | research/08-astryx-mcp.md | 169 | Phase 8 Task 4: Astryx has NO MCP server (2026-08-11) |
| 16 | research/08-loopy-verification.md | 175 | Phase 8 Task 2: loopy deep-verify, receipt gap (2026-08-11) |
| 17 | research/08-pre-commit-hook.md | 204 | Phase 8 Task 3: git hook (hard) + plugin hook (soft) (2026-08-11) |
| 18 | research/08-testing-qa.md | 198 | Phase 8 Task 1: opencode-browser + Playwright agents (2026-08-11) |
| 19 | harness-templates/AGENTS.md | 56 | walkinglabs startup workflow + working rules + DoD (verbatim) |
| 20 | harness-templates/feature_list.json | 65 | Scope lock schema (single_active_feature, verification[], evidence[]) |
| 21 | harness-templates/claude-progress.md | 49 | Per-session progress log template |
| 22 | harness-templates/init.sh | 30 | INSTALL_CMD / VERIFY_CMD / START_CMD baseline script |
| 23 | harness-templates/README.md | 30 | Provenance: walkinglabs/learn-harness-engineering docs/en/resources/templates/, pulled 2026-08-09 |

---

## A. Named resources — canonical inventory

Prior category = Phase 0 section or Phase 5 slot / catalog element. Prior status/date = status as recorded in source + research date.

### A1. Phase 0 Section A — "Already Confirmed Real" (2026-08-09, corrected 2026-08-11)

| Resource name | Canonical URL | Prior category | Prior verification status / date | Known correction |
|---|---|---|---|---|
| facebook/astryx | https://github.com/facebook/astryx | Section A; Phase 2 TOP PICK #1; catalog-adjacent frontend | ⚠️ Partially correct 2026-08-09; corrected Phase 8 2026-08-11 | **Astryx CLI-only, NO MCP.** packages/mcp-server + packages/mcp both 404; CLI README zero MCP refs; no `mcp` subcommand. Integration = bash `npx @astryxdesign/cli <cmd> --dense` only |
| karpathy/llm-council | https://github.com/karpathy/llm-council | Section A; Phase 3 council | ✅ Confirmed 2026-08-09 (unmaintained weekend hack, OpenRouter-native) | None — usable but DIY (Python sidecar, not SKILL.md) |
| okjpg/llm-council (fork) | (no URL — not found) | Section A; Phase 3 | ❌ Not found 2026-08-09, re-confirmed Phase 3 | **Not found.** No public repo under okjpg handle. Skip until exact URL provided |
| ngmeyer/council-review | https://github.com/ngmeyer/council-review | Section A → Phase 3 council skill | ⚠️ "Archived" 2026-08-09 → ✅ **Corrected LIVE 2026-08-09 (Phase 3 + Phase 6)** | **Both live in parallel.** Standalone skill, page title verified. NOT archived; NOT replaced |
| ngmeyer/skills | https://github.com/ngmeyer/skills (monorepo) | Section A correction target; Phase 3 | ✅ Live (parallel monorepo) | **Both live.** Consolidated version adds devil's-advocate, theatrical-consensus detector, sycophancy guardrail |
| Graphify-Labs/graphify | https://github.com/Graphify-Labs/graphify | Section A; Phase 5 #1 | ✅ Confirmed 2026-08-09 (104k+ stars, `/graphify` native) | Star count grew (was given 76k). Verdict: MUST-HAVE |

### A2. Phase 0 Section B — "Now Verify These" (2026-08-09)

| Resource name | Canonical URL | Prior category | Prior status / date | Note |
|---|---|---|---|---|
| ruvnet/ruflo (fka Claude Flow) | https://github.com/ruvnet/ruflo | Section B ("ruflo"); Phase 5 #2 | ⚠️ Corrected 2026-08-09 (real repo ruvnet/ruflo) | 60+ agents, 300+ MCP tools. Verdict: POWER-USER, too heavy for solo |
| emilkowalski/skills | https://github.com/emilkowalski/skills | Section B ("enilkowaski"); Phase 5 #3 | ⚠️ Corrected 2026-08-09 (voice-to-text garble) | apple-design skill. TOP PICK for frontend animation |
| teng-lin/notebooklm-py | https://github.com/teng-lin/notebooklm-py | Section B ("notebooklm py"); Phase 5 #4 | ⚠️ Corrected, 🔶 unofficial 2026-08-09 | Reverse-engineers undocumented Google RPCs — breakage risk. USE WITH CAUTION |
| vercel/eve | https://github.com/vercel/eve | Section B; Phase 5 #5 | ✅ Confirmed 2026-08-09 (June 2026, filesystem-first agents) | WRONG LAYER for OpenCode — agent-building framework, not a plugin |
| vercel/deepsec | https://github.com/vercel/deepsec | Section B; Phase 5 #6 | ✅ Confirmed 2026-08-09 (May 2026 scanner) | SPECIALIZED AUDIT only — Opus-class scan costs $100s–$1000s |
| thedotmack/claude-mem | https://github.com/thedotmack/claude-mem | Section B ("claude-mem"); Phase 5 #7 | ✅ Confirmed 2026-08-09 (`npx claude-mem install --ide opencode`) | TOP MEMORY PICK |
| mvanhorn/last30days-skill | https://github.com/mvanhorn/last30days-skill | Section B; Phase 5 #8 | ✅ Confirmed exact path 2026-08-09 | HIGH VALUE research skill (last-30-days synthesis) |

### A3. Phase 0 Section C — walkinglabs URL (2026-08-09)

| Resource name | Canonical URL | Prior category | Prior status / date |
|---|---|---|---|
| walkinglabs/learn-harness-engineering | https://github.com/walkinglabs/learn-harness-engineering | Section C; harness-templates source; Phase 4 DoD | ✅ Repo live + template URL live, ⚠️ content mismatch 2026-08-09 |
| walkinglabs templates index (claimed 5-layer URL) | https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/resources/templates/index.md | Section C | ⚠️ URL live but contains Template Guide (AGENTS.md/init.sh/progress/feature_list), NOT five-layer framework. Real layers elsewhere: Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff |

### A4. Phase 0 Section D — Loop-engineering repos (2026-08-09)

| Resource name | Canonical URL | Prior category | Prior status / date | Differentiator |
|---|---|---|---|---|
| cobusgreyling/loop-engineering | https://github.com/cobusgreyling/loop-engineering | Section D; Phase 5 #9; arch Layer: scaffold/audit/governance | ✅ Confirmed LIVE (loop-init/loop-audit/loop-doctor/loop-cost) | Canonical patterns-and-CLI repo — INCLUDED |
| KanakMalpani/Loop-Engineering | https://github.com/KanakMalpani/Loop-Engineering | Section D (was mis-corrected to LoopBench only) | ✅ **Confirmed LIVE — corrected Phase 6 2026-08-09** | **Both live, separate.** Loop-Engineering = framework |
| KanakMalpani/LoopBench | https://github.com/KanakMalpani/LoopBench | Section D correction target; Phase 5 #10 | ✅ Confirmed LIVE | **Both live, separate.** LoopBench = MLPerf-style benchmark, reference-only |
| Forward-Future/loopy | https://github.com/Forward-Future/loopy | Section D; Phase 5 #11; arch Layer: bounded loops | ✅ Confirmed LIVE | Loop-as-playbook SKILL.md — INCLUDED. **Receipt gap:** run receipts NOT auto-propagated to feature_list.json evidence[] (needs explicit AGENTS.md instruction). Pure SKILL.md, no opencode.json entry; OpenCode via interactive installer only (not named target); 9 paths (Find/Craft/Run/Debrief/Save = correct subset); CONTRIBUTING.md 404 |
| huangruiteng/loopx | https://github.com/huangruiteng/loopx | Section D; Phase 5 #12; arch Q1 | ✅ Confirmed LIVE, ❌ EXCLUDED by architecture Q1 2026-08-10 | State kernel — EXCLUDED (dual-source-of-truth with walkinglabs; needs external Turn Loop Controller; built for 200h+ runs) |
| baidu-baige/LoongFlow | https://github.com/baidu-baige/LoongFlow | Section D; Phase 5 #13 | ✅ Confirmed LIVE (arXiv 2512.24077) | Evolutionary PES framework — specialized research, low web-dev relevance |
| cobusgreyling/goal-engineering | https://github.com/cobusgreyling/goal-engineering (per arch Q5) | Arch Q5 | ✅ Real, ❌ NOT adopted | GOAL.md = second state file (dual-source problem); /goal name collides with Grok/Codex natives. Entry = /idea |

### A5. Phase 0 Section E — "Confirm Current State" (2026-08-09)

| Resource name | Canonical URL | Prior category | Prior status / date |
|---|---|---|---|
| gsd-build/get-shit-done (GSD original) | https://github.com/gsd-build/get-shit-done | Section E; Phase 5 #14 | ⚠️ Real but ARCHIVED June 2026 + security warning (deep shell perms, rug-pull reports). DO NOT USE original |
| open-gsd/gsd-core (maintained fork) | https://github.com/open-gsd/gsd-core | Section E correction; Phase 5 #14 | ✅ Confirmed LIVE 2026-08-09 ("Git. Ship. Done - Core"). USE FORK ONLY |
| mattpocock/skills | https://github.com/mattpocock/skills | Section E; Phase 5 #15 | ✅ Confirmed active 2026-08-09 (200k+ stars) — ESSENTIAL |
| obra/superpowers | https://github.com/obra/superpowers | Section E; Phase 5 #16 | ✅ Confirmed active (211k+ stars, OpenCode `.opencode/skills/` support) — FOUNDATIONAL. Layer-1/manual-only caveat in build (conversational Q&A violates Layer 2 autonomy) |
| garrytan/gstack | https://github.com/garrytan/gstack | Section E; Phase 5 #17 | ✅ Confirmed active (~23 role skills, `/qa` headless Chromium) |
| public-apis/public-apis | https://github.com/public-apis/public-apis | Section E; Phase 5 #18 | ✅ Confirmed (reference list, not installable; index via graphify clone) |
| asgeirtj/system_prompts_leaks | https://github.com/asgeirtj/system_prompts_leaks | Section E; Phase 5 #19 | ✅ Confirmed; `Anthropic/claude-fable-5.md` EXISTS (subfolder, uppercase Anthropic) — study material |
| anthropics/claude-cookbooks | https://github.com/anthropics/claude-cookbooks | Section E; Phase 5 #20 | ✅ Confirmed (org `anthropics` with s; also platform.claude.com/cookbook) — official reference |
| n8n | https://github.com/n8n-io/n8n / https://n8n.io | Section E; Phase 3 §B | ✅ Active, ❌ SKIPPED for this setup (no official OpenCode import path; n8n-nodes-opencode inverts control; MCP bridge is manual) |

### A6. Council / testing / context / guard selections (verification.md + Phases 3/4/7/8)

| Resource name | Canonical URL | Prior category | Prior status |
|---|---|---|---|
| deliberation (plugin + MCP) | via awesome-opencode (Element 8/15) | Council turnkey pick; Two-Judge vehicle | ✅ Native OpenCode plugin, 7 experts, ask-all/consensus |
| Open Conclave | via awesome-opencode (Element 8) | Council analog (debate-to-consensus) | ✅ Native plugin |
| michaljach/opencode-browser | https://github.com/michaljach/opencode-browser | Phase 8 Task 1; verification.md Phase 3C | ✅ LIVE (plugin over browsermcp.io; `npx opencode-browser init`; MCP `@browsermcp/mcp@0.1.3` pinned; needs Chrome/Edge ext; interactive smoke only, no CI) |
| microsoft/playwright-mcp | https://github.com/microsoft/playwright-mcp | Phase 8 Task 1; verification.md Phase 3C | ✅ LIVE (opencode.json `playwright` entry; `npx playwright init-agents --loop=opencode`; Planner/Generator/Healer; `npx playwright test` = DoD hard gate) |
| upstash/context7 | https://github.com/upstash/context7 | verification.md Phase 4A Priority 1 | ✅ ALWAYS install (remote https://mcp.context7.com/mcp or local `npx -y @upstash/context7-mcp`) |
| tickernelz/opencode-mem | https://github.com/tickernelz/opencode-mem | verification.md Phase 4A P2 Option A | ✅ Optional (vector recall, UI 127.0.0.1:4747) — either/or with claude-mem |
| Opencode-DCP/opencode-dynamic-context-pruning | https://github.com/Opencode-DCP/opencode-dynamic-context-pruning | verification.md Phase 4A P3 | ✅ Optional (3.9k stars, intelligent compression) |
| remorses/opencode-injection-guard | https://github.com/remorses/opencode-injection-guard | verification.md Phase 4C | ✅ Recommended if external data (tool.execute.after judge model) |
| boxpositron/envsitter-guard | https://github.com/boxpositron/envsitter-guard | verification.md Phase 4C | ✅ Recommended if .env secrets |
| sandervandegeijn/code-security-scanner | https://github.com/sandervandegeijn/code-security-scanner | verification.md Phase 4C | ✅ Optional formal audits (6-phase, read-only jail agent) |
| hqhq1025/skill-optimizer | https://github.com/hqhq1025/skill-optimizer | Phase 4 §5 harness evolution (Mine) | ✅ skill-miner/personalizer/generalizer |
| okdk7788/opencode-self-improving-skills | https://github.com/okdk7788/opencode-self-improving-skills | Phase 4 §5 (Distill/GEPA-optimize) | ✅ distill_skill/optimize_skill/curator |
| thousandflowers/skillreaper | https://github.com/thousandflowers/skillreaper | Phase 4 §5 (Prune) | ✅ evidence-based dead-weight quarantine |
| Graphify-Labs/graphify | (see A1) | verification.md Phase 4A P4 optional | ✅ Optional for large codebases |
| mvanhorn/last30days-skill | (see A2) | verification.md / Phase 4A P5 optional | ✅ Optional for bleeding-edge research |

### A7. Phase 2 design/backend/3D + Phase 4 ecosystem extras

| Resource name | Canonical URL | Prior category | Prior status |
|---|---|---|---|
| keysjoao/laws-of-ux-skills | https://github.com/keysjoao/laws-of-ux-skills | Phase 2 TOP PICK #2 | ✅ SKILL.md (Advisor/Audit/Pre-ship) → `.opencode/skills/` |
| VoltAgent/awesome-design-md | https://github.com/VoltAgent/awesome-design-md | Phase 2 TOP PICK #3 | ✅ DESIGN.md file drop + `npx @google/design.md lint` |
| shadcn-ui/ui | https://github.com/shadcn-ui/ui | Phase 2 TOP PICK #4 | ✅ Official shadcn MCP (remote w/ token) or `@jpisnice/shadcn-ui-mcp-server` |
| lawsofux.com | https://lawsofux.com | Phase 2 reference | ✅ Real site, reference-only (wrapper above is the actionable form) |
| alexpate/awesome-design-systems | https://github.com/alexpate/awesome-design-systems | Phase 2 reference | ✅ ~25k stars, bookmark only |
| gztchan/awesome-design | https://github.com/gztchan/awesome-design | Phase 2 reference | ✅ ~17.4k stars, bookmark only |
| kevindeasis/awesome-ui | https://github.com/kevindeasis/awesome-ui | Phase 2 reference | ✅ Exists, low priority (covered by laws-of-ux-skills) |
| batoreh/awesome-ux | https://github.com/batoreh/awesome-ux | Phase 2 reference | ✅ Exists, skip (research-methodology) |
| Google Material Design 3 | https://m3.material.io | Phase 2 reference | ✅ Real; agent-usable only via custom DESIGN.md or Context7 |
| Apple HIG | https://developer.apple.com/design/human-interface-guidelines | Phase 2 reference | ✅ Real; custom SKILL.md backlog for mobile |
| refactoringui.com | https://www.refactoringui.com | Phase 2 reference | ✅ Real (paid book), reference-only, no skill wrapper |
| cnoe-io/openapi-mcp-codegen | https://github.com/cnoe-io/openapi-mcp-codegen | Phase 2 backend workaround | ✅ Best available for specced backends (DIY: spec → MCP) |
| awslabs/openapi-mcp-server (+ ckanthony/openapi-mcp proxy) | https://github.com/awslabs/openapi-mcp-server | Phase 2 backend workaround | ✅ Dynamic OpenAPI→MCP proxy alternative |
| pmndrs/react-three-start | https://github.com/pmndrs/react-three-start | Phase 2 TOP 3D PICK | ✅ File-based scenes, most agent-friendly |
| pmndrs/react-three-fiber (+ Vite react-ts scaffold) | https://github.com/pmndrs/react-three-fiber | Phase 2 3D #2 | ✅ Standard 2026 stack (`three`, `@react-three/fiber`, `@react-three/drei`, `r3f-perf`) |
| pmndrs/react-three-next | https://github.com/pmndrs/react-three-next | Phase 2 3D #3 | ✅ Use only if Next.js/SSR needed |
| mdc-git/opencode-playwright-interactive | via Phase 8 §Other | Testing niche | ✅ Noted (Electron/REPL QA, niche) |
| upex-galaxy/agentic-qa-boilerplate | via Phase 8 §Other | Testing template | ✅ Noted (QA-heavy project template) |
| fugazi/test-automation-skills-agents | via Phase 8 §Other | Testing skills | ✅ Noted (lighter-weight, tool-agnostic) |

---

## B. Catalog — 26 elements (163 usable / 43 excluded)

Full raw text in catalog.md (Elements 1–26) + 01-existing-summary.md per-element paragraphs + verification.md build mapping. Condensed here to element + counts + standout URLs; full 163-name enumeration lives in catalog.md and BUILD-PROMPT TOOL_CATALOG tables.

| # | Element | Usable / Excl. | Standout canonical URLs |
|---|---|---|---|
| 1 | Skills | 14 / 28 | https://github.com/obra/superpowers, https://github.com/anthropics/skills, https://github.com/mattpocock/skills, https://github.com/addyosmani/agent-skills, https://github.com/[REDACTED-caveman], https://github.com/waybarrios/opencode-power-pack, https://github.com/hqhq1025/skill-optimizer, https://github.com/cloudflare/skills |
| 2 | Permission modes | 4 / 1 | https://opencode.ai/docs/permissions/, https://github.com/joelhooks/opencode-config, https://github.com/kdcokenny/opencode-workspace, https://github.com/boxpositron/envsitter-guard |
| 3 | Checkpoints/rewind | 3 / 3 | OpenCode native /undo; https://www.npmjs.com/package/@arkfactory/opencode-checkpoint, https://github.com/witlox/opencode-checkpoint |
| 4 | Context mgmt | 15 / 2 | https://github.com/Opencode-DCP/opencode-dynamic-context-pruning, https://github.com/tickernelz/opencode-mem, https://github.com/0xranx/OpenContext, https://github.com/upstash/context7, https://github.com/code-yeongyu/oh-my-openagent, https://github.com/alvinunreal/oh-my-opencode-slim |
| 5 | Hooks | 6 / 2 | https://github.com/code-yeongyu/oh-my-openagent, https://github.com/alvinunreal/oh-my-opencode-slim, https://github.com/smartfrog/opencode-froggy, hcom + FlowDeck via https://github.com/awesome-opencode/awesome-opencode |
| 6 | MCP servers | 9 / 2 | https://github.com/upstash/context7, https://github.com/AlaeddineMessadi/opencode-mcp, https://github.com/ajhcs/Better-OpenCodeMCP, Ejentum/SwarmVault/supamem via awesome-opencode |
| 7 | Sandboxing | 3 / 1 | https://github.com/fabianlema/opencode-sandbox, https://github.com/athal7/opencode-devcontainers, jailoc via awesome-opencode (official docs: Docker/VM; no built-in sandbox) |
| 8 | Subagents | 15 / 2 | https://github.com/ankitmundada/awesome-opencode-subagents, oh-my-openagent, oh-my-opencode-slim, https://github.com/kdcokenny/opencode-workspace, NERV/hiai-opencode/CrewBee/Ensemble/Conclave/deliberation via awesome-opencode |
| 9 | Plugins/marketplaces | 6 / 2 | https://github.com/awesome-opencode/awesome-opencode, https://github.com/CKGrafico/opencode-market, https://github.com/NikiforovAll/opencode-marketplace, https://github.com/kdcokenny/ocx |
| 10 | Output styles | 8 / 1 | https://github.com/ajaxdude/opencode-ai-poimandres-theme (+ VS Code ports, 21 light themes, Ayu/Charcoal/Lavi/Moonlight via awesome-opencode) |
| 11 | Background tasks | 7 / 1 | https://github.com/kdcokenny/opencode-background-agents, https://github.com/zenobi-us/opencode-background, server-manager/scheduler/notify/Pilot via awesome-opencode |
| 12 | Security review | 6 / 2 | https://github.com/alibaba/open-code-review, https://github.com/waybarrios/opencode-power-pack, opencode-review + Swarm via awesome-opencode, https://github.com/darrenhinde/OpenAgentsControl |
| 13 | Headless/CI | 6 / 1 | `opencode run/serve/web`, https://github.com/wesammustafa/opencode-primer, https://github.com/chriswritescode-dev/opencode-manager, https://github.com/AlaeddineMessadi/opencode-mcp |
| 14 | Usage/cost tracking | 11 / 2 | https://github.com/eserete/opencode-token-tracker, https://github.com/opgginc/opencode-bar, https://github.com/ramtinJ95/opencode-tokenscope, Token Monitor/Throughput/Quota/Telemetry/mystatus/Langfuse via awesome-opencode |
| 15 | Agent-team frameworks | 17 / 4 | https://github.com/code-yeongyu/oh-my-openagent (67.2k), https://github.com/alvinunreal/oh-my-opencode-slim (7.8k), https://github.com/darrenhinde/OpenAgentsControl (4.6k), https://github.com/kdcokenny/opencode-workspace, https://github.com/agnusdei1207/opencode-orchestrator |
| 16 | Workflow orchestration | 12 / 3 | https://github.com/mark-hingston/opencode-workflows, https://github.com/derekbar90/opencode-conductor, FlowDeck/Open Dynamic Workflows/bmad/GoopSpec/NERV via awesome-opencode |
| 17 | Agent SDKs | 3 / 2 | https://github.com/anomalyco/opencode-sdk-js, https://github.com/anomalyco/opencode-sdk-go, https://github.com/Acksell/opencode-go-sdk (gap: no official Python SDK, issue #4031) |
| 18 | Discipline/skill packs | 4 / 1 | https://github.com/obra/superpowers, https://github.com/waybarrios/opencode-power-pack, https://github.com/meaningfy-ws/skillery, https://github.com/DietrichGebert/ponytail |
| 19 | Docs-context MCP | 3 / 1 | https://github.com/upstash/context7, https://github.com/sandbox-technologies/opencode-docs-mcp, https://github.com/bgauryy/open-docs |
| 20 | Statusline | 3 / 1 | https://github.com/Joaquinvesapa/sub-agent-statusline, https://github.com/eserete/opencode-token-tracker (gap: no customizable statusLine hook, #30295/#8619) |
| 21 | Git-worktree helpers | 3 / 1 | https://github.com/kdcokenny/opencode-worktree (701 stars), https://github.com/felixAnhalt/opencode-worktree-session, https://github.com/athal7/opencode-devcontainers |
| 22 | Awesome-lists | 5 / 5 | https://github.com/bradAGI/awesome-cli-coding-agents, https://github.com/ai-for-developers/awesome-ai-coding-tools, https://github.com/kyrolabs/awesome-agents, https://github.com/awesome-opencode/awesome-opencode |
| 23 | Security scanners | 3 / 2 | https://github.com/sandervandegeijn/code-security-scanner, https://github.com/zm2231/z-audit, https://github.com/remorses/opencode-injection-guard (gap: no opencode.json config linter) |
| 24 | Safety-net/guardrails | 5 / 2 | https://github.com/remorses/opencode-injection-guard, https://github.com/boxpositron/envsitter-guard, Greywall/Daytona/FlowDeck via lists |
| 25 | Hook mgmt CLIs | 2 / 2 | Opencode Hooks Plugin via awesome-opencode; OpenCode native plugin system = hook system (https://opencode.ai/docs/plugins/) |
| 26 | Self-improving | 3 / 2 | https://github.com/okdk7788/opencode-self-improving-skills, https://github.com/hqhq1025/skill-optimizer, https://github.com/thousandflowers/skillreaper |

Build-prompt disposition (verification.md): INCLUDED 1,2,4,5,6,8,9,10,12,14,16,18,19,20,23,24,26 (+custom dod-gate, two-judge, loop stack, context7, guards); EXCLUDED 3 (git over rewind), 7 (loop-gate denylist over VM), 11 (foreground /idea only), 13 (local loop, no CI), 15 (Two-Judge over mega-harness), 17 (no SDK wrapper), 21 (main-tree only), 22 (research only), 25 (native plugin scripts over CLI).

---

## C. Known corrections (required set + related)

1. **Astryx CLI-only, no MCP** — Phase 8 2026-08-11 direct fetch: no packages/mcp-server, no packages/mcp, CLI README zero MCP refs, no `mcp` subcommand; circulating `npx @astryxdesign/cli mcp` opencode.json snippet is speculative (would ERR_UNKNOWN_COMMAND). Use bash `--dense` calls; `astryx init` AGENTS.md merge. Architecture docs corrected (07 + build prompts).
2. **loopy receipt gap** — Phase 8 2026-08-11: loopy is a SKILL (not engine); LOOPS.md (recipe library) does not conflict with feature_list.json; but Run receipts stay in-session and do NOT auto-write to evidence[]. Agent MUST copy receipt → evidence[] (AGENTS.md Layer 2 rule). 5-path doc = correct subset of actual 9 paths; CONTRIBUTING.md 404.
3. **ngmeyer both live** — Phase 3 + Phase 6 2026-08-09 live fetch: `ngmeyer/council-review` LIVE (standalone, title verified), `ngmeyer/skills` LIVE (parallel monorepo with devil's-advocate/theatrical-consensus/sycophancy upgrades). Prior "archived/migrated" claim was wrong.
4. **KanakMalpani both live** — Phase 6 2026-08-09: `KanakMalpani/Loop-Engineering` LIVE (framework) AND `KanakMalpani/LoopBench` LIVE (benchmark). Prior "only LoopBench exists" claim was wrong.
5. **gsd-build archived → open-gsd** — Original `gsd-build/get-shit-done` archived June 2026 (security: deep shell perms). Maintained fork `open-gsd/gsd-core` verified live 2026-08-09. Use fork only.
6. **okjpg not found** — `okjpg/llm-council` unverifiable across Phase 0 + Phase 3 searches. Treat as voice-to-text distortion; skip unless exact URL supplied.
7. Related: ruvnet/ruflo (fka Claude Flow), emilkowalski (not enilkowaski), teng-lin/notebooklm-py unofficial, walkinglabs layer-name paraphrase + wrong-path URL, system_prompts_leaks subfolder path `Anthropic/claude-fable-5.md`, cookbooks org `anthropics` (with s).

## D. Unresolved items

- `okjpg/llm-council` — no public repo; needs exact URL from requester.
- walkinglabs five-layer canonical location — framework real (Instructions/State/Verification/Scope Boundaries/Lifecycle Handoff) but exact in-repo page for that wording not pinned; given URL holds Template Guide instead.
- MEDUSA `.opencode/` coverage, science-superpowers OpenCode path, Baton OpenCode docs, shanraisshan OpenCode docs — flagged claimed-but-unverified in catalog second pass.
- Superpowers star counts vary by date/source (89K→130K→211K→267K across 2026 writeups) — growth, not conflict; re-verify at verification time.
- No official Python SDK (issue #4031); statusLine hooks (#30295/#8619/#23539); marketplace #7467; plugin enable/disable #11743; Claude-hooks compat #12472 — all open at research time.

## E. Gaps (7 structural, per 06-unfound-and-gaps.md + Phase 2/4)

1. No turnkey backend Astryx — workaround: OpenAPI→MCP codegen or AGENTS.md schema tables.
2. No native OpenCode↔Antigravity DOM bridge — workaround: Puppeteer/Playwright MCP in opencode.json.
3. No official n8n↔OpenCode pipeline import — workaround: native plugins (FlowDeck/Open Dynamic Workflows/deliberation).
4. No official OpenCode plugin marketplace (#7467) — workarounds: awesome-opencode, opencode-market, opencode-marketplace, OCX, Tommertom /plugin.
5. No customizable statusLine shell hook — workarounds: ocstatusline daemon, opencode-status-line binary, opencode-status-bar menu app, sidebar plugins.
6. No official Python SDK (#4031) — workaround: `opencode run` subprocess or JS/TS SDK.
7. No opencode.json security config linter — workaround: manual permission audit or Docker sandbox.

## F. Harness templates + build prompts (provenance)

- harness-templates/AGENTS.md, feature_list.json, claude-progress.md, init.sh = verbatim walkinglabs/learn-harness-engineering docs/en/resources/templates/ (pulled 2026-08-09); README.md = provenance only, not a working file.
- BUILD-PROMPT-FINAL.md (OpenCode) and BUILD-PROMPT-UNIVERSAL.md (tool-agnostic + Phase 5 library/promote-skill) encode the locked architecture: walkinglabs sole state; loop-engineering scaffold/audit; loopy bounded loops; two-judge-verification SKILL.md; dual commit gate (git hard + plugin soft, transition-only on status→passing with empty evidence[]); Astryx CLI bash; Playwright + browsermcp + context7 MCP; /idea entry; no mega-harness.
- verification.md confirms all 26 elements deliberately included/excluded — none accidentally overlooked.
