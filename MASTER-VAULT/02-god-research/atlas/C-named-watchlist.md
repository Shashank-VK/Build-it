# Deliverable C — Named-Resource Investigation Register
**The Omniscient Resource Atlas · Part 19 / Built 2026-10-10**

For every entry in the Part-19 watchlist: original name supplied, exact matched project, canonical URL, repository files inspected, what it contains, what it does, where it can be used, compatibility/integration type, limitations, verification status, sources.

**Totals: 18 Verified · 1 Corrected · 2 Partially verified · 2 Unresolved** (of 23 items)

**Preserved corrections (do not silently alter):** ruvnet/ruflo (ex-Claude Flow) · emilkowalski/skills · teng-lin/notebooklm-py (unofficial) · ngmeyer/council-review LIVE · KanakMalpani/Loop-Engineering vs LoopBench (separate) · open-gsd/gsd-core (safe fork; gsd-build archived June 2026) · okjpg/llm-council (not found) · Karim Shoair (not "Krim") · vercel-labs/deepsec (not vercel/deepsec) · Pizza Bot (not "PizzaBox") · affaan-m/ECC (name retired) · Astryx has NO MCP server.

---
## 1. OpenViking

- **Original name supplied:** OpenViking
- **Exact matched project:** OpenViking — "Self-evolving Context Database for AI Agents" by ByteDance's Volcano Engine Viking team
- **Canonical URL:** https://github.com/volcengine/OpenViking (website: https://openviking.ai, docs: https://docs.openviking.ai)
- **Repository files inspected:** README.md (root file list: `openviking/`, `openviking_cli/`, `openviking_gateway/`, `crates/` (Rust CLI), `bot/`, `web-studio/`, `sdk/`, `docs/`, `examples/`, `deploy/`, `benchmark/`, `Dockerfile`, `docker-compose.yml`, `pyproject.toml`, `Cargo.toml`, `SECURITY.md`); README sections on architecture, tiers, CLI, integrations, VikingBot, commercial editions
- **What it actually contains:** Python server + Rust CLI (`ov_cli`), gateway, SDKs (Python, Go, TypeScript), HTTP API, MCP server, Web Studio (browser console), desktop app beta (macOS/Windows), VikingBot agent framework, agent-plugin installers, benchmarks (LoCoMo, tau2-bench), Docker deployment
- **What it actually does:** Open-source (AGPL-3.0) "context database" that unifies agent memory, knowledge RAG, and skills as one browsable virtual filesystem under the `viking://` protocol. Content is loaded in tiers: L0 abstract (one-sentence), L1 overview, L2 full detail. Agents use file-like ops (`ov ls`, `ov tree`, `ov find`, `ov grep`); retrieval is hierarchical/directory-scoped rather than a flat vector index
- **Where it can be used:** Self-hosted via pip (`pip install openviking`), `uv tool install openviking`, Docker, or standalone HTTP service; requires an embedding provider and a VLM (Volcengine, OpenAI, Codex OAuth, Kimi, GLM, local Ollama). Managed SaaS/self-managed commercial editions via Volcengine
- **Compatibility and integration type:** Hooks + MCP integrations for Claude Code, Codex, Cursor, TRAE, OpenCode, OpenClaw; context engine for Hermes; plugin + MCP for DSH; native extension for pi; tools + store for LangChain; Agent Plugins 1.0 and MCP client support generally
- **Relevant limitations:** Open-source edition described by maintainers as still early-stage; AGPL-3.0 (copyleft — commercial/hosting implications); needs embedding + VLM API keys; token cost of indexing; commercial tiers exist for enterprise features
- **Verification status:** Verified
- **Sources:** https://github.com/volcengine/OpenViking (README inspected 2026-10-10); https://openviking.ai; https://docs.openviking.ai

---

## 2. PizzaBox by AWS

- **Original name supplied:** PizzaBox by AWS
- **Exact matched project:** None under that name. Nearest evidence-backed AWS match is **Pizza Bot** — the name "PizzaBox" appears to be a name variant/mishearing of "Pizza Bot"
- **Canonical URL:** https://aws.amazon.com/blogs/opensource/introducing-pizza-bot-an-open-source-inbox-for-ai-agents-that-work-in-the-background/ (announcement, 2026-09-10); repo https://github.com/pizza-bot-app/pizza-bot (via secondary sources)
- **Repository files inspected:** Not inspected directly (repo URL obtained from secondary sources: The Register, Aicybr, hongsw/clawfit research note). AWS Open Source Blog announcement read for purpose/architecture
- **What it actually contains (Pizza Bot, the match):** Local-first inbox app for background AI agents: Hono API server owning runs/state/persistence (SQLite + files), Electron desktop shell, browser and terminal clients over HTTP/SSE; DeepAgents + LangGraph runtime engine; bundled plugins, built-in Agent Skills, optional `skills/`, tests for LangGraph compatibility
- **What it actually does:** Runs AI agents in the background and surfaces their work in an email-style inbox (All / Unread / Action views); supports manual, scheduled (cron), and webhook-triggered tasks; per-tool approval policies; MCP integrations (Claude Code `.mcp.json` compatible); multi-model providers (Anthropic, Bedrock, Gemini, OpenAI, OpenRouter, Ollama)
- **Where it can be used:** Self-hosted local infrastructure (macOS, Windows, Linux desktop builds; standalone/containerized backend for always-on scheduled work). Not an AWS-supported service (community project)
- **Compatibility and integration type:** MCP client; Claude Code-compatible MCP config; skill/plugin API; browser automation + guide skills bundled
- **Relevant limitations:** Amazon-specific skills/MCP connections excluded from public release; community must build integrations; not AWS-supported (no SLA)
- **Verification status:** Corrected (supplied name "PizzaBox by AWS" does not exist as a project; evidence points to AWS's "Pizza Bot" as the intended lead — same org, same pizza naming, same agent-ecosystem topic, announced 2026-09-10)
- **Sources:** https://aws.amazon.com/blogs/opensource/introducing-pizza-bot-an-open-source-inbox-for-ai-agents-that-work-in-the-background/ (2026-10-10); https://www.theregister.com/ai-and-ml/2026/09/15/your-ai-agents-reports-and-questions-have-a-new-inbox-courtesy-of-aws/5296661 (2026-10-10); https://aicybr.com/blog/aws-pizza-bot-background-ai-agents-guide (2026-10-10); https://github.com/hongsw/clawfit/blob/HEAD/docs/research-watch/2026-09-15-aws-pizza-bot-background-agent-inbox.md (2026-10-10)

---

## 3. Scrapling by Krim Shoair

- **Original name supplied:** Scrapling by Krim Shoair
- **Exact matched project:** Scrapling by **Karim Shoair** (GitHub: D4Vinci) — author name corrected (Krim → Karim); project "Scrapling" itself matches exactly
- **Canonical URL:** https://github.com/D4Vinci/Scrapling (docs: https://scrapling.readthedocs.io)
- **Repository files inspected:** README.md (root file list: `scrapling/` package, `agent-skill/` directory, `docs/`, `tests/`, `server.json`, `Dockerfile`, `pyproject.toml`, `AI_POLICY.md`, `ROADMAP.md`, `CHANGELOG.md`); Key Features sections: Spiders, Advanced Fetching, Adaptive Scraping, AI Features
- **What it actually contains:** Python adaptive web-scraping framework: `Fetcher`/`AsyncFetcher`/`StealthyFetcher`/`DynamicFetcher` classes, Scrapy-like `Spider` API (start_urls, parse, streaming, pause/resume checkpoints, AutoThrottle, robots.txt), selector engine (CSS/XPath/text/regex), adaptive element tracking, proxy rotation, Playwright/Chromium automation, MCP server, interactive scraping shell + `extract` command, CLI, agent skill (`agent-skill/`), Docker image
- **What it actually does:** Handles everything from a single request to a full-scale crawl: fetches sites incl. JS-heavy/anti-bot pages (Cloudflare Turnstile bypass), scrapes with selectors that survive site-structure changes (adaptive similarity), and scales to concurrent multi-session crawls; AI features let chatbots/agents scrape via MCP
- **Where it can be used:** Python library (`pip install scrapling`; extras `scrapling[ai]`, `scrapling[shell]`, `scrapling[all]`; browser deps via `scrapling install`); Docker image `pyd4vinci/scrapling` / ghcr.io/d4vinci/scrapling; agent integration via MCP server
- **Compatibility and integration type:** MCP server for Claude/Cursor/etc.; agent skill bundled; Discord community; sponsors from proxy providers
- **Relevant limitations:** BSD-3-Clause; authorship: educational/research disclaimer about scraping laws, ToS, robots.txt; anti-bot bypass exists in legal gray areas
- **Verification status:** Verified (project identity; author spelling corrected: Karim Shoair, D4Vinci)
- **Sources:** https://github.com/D4Vinci/Scrapling (README inspected 2026-10-10); https://scrapling.readthedocs.io

---

## 4. ChatDev 2.0 / devAll

- **Original name supplied:** ChatDev 2.0 / devAll
- **Exact matched project:** ChatDev 2.0, a.k.a. DevAll — one project, versioned successor (not multiple projects)
- **Canonical URL:** https://github.com/OpenBMB/ChatDev (releases: https://github.com/OpenBMB/ChatDev/releases/tag/v2.0.0)
- **Repository files inspected:** Releases page (v2.0.0 + v2.1.0 notes inspected via search-result text); README.md (mirrored in forks darshan-paapani06/chatdev1, samulli/chatdev) — news banner, architecture overview, quick-start, requirements
- **What it actually contains:** ChatDev 2.0 (released 2026-01-07) introduces **DevAll**, "a Zero-Code Multi-Agent Platform for 'Developing Everything'" — no-code construction/config/execution of multi-agent workflows; frontend (React) + backend; ChatDev 1.0 (virtual software company: CEO/CTO/Programmer agents) preserved on `chatdev1.0` branch for maintenance; `main` branch switched to 2.0
- **What it actually does:** Lets users build, configure, and run customized multi-agent systems without writing code (data viz, 3D generation, deep research, game dev use cases); conceptual generalization of ChatDev 1.0 from software-focused to general orchestration
- **Where it can be used:** Self-hosted; Python 3.12+, Node 18+, uv package manager; macOS/Linux/Windows/WSL
- **Compatibility and integration type:** Supports GPT-4o/GPT-4o-mini and other models; web frontend
- **Relevant limitations:** 2.0 is an architectural break from 1.0; 1.x users must migrate or stay on legacy branch
- **Verification status:** Verified (one project, DevAll = ChatDev 2.0 codename)
- **Sources:** https://github.com/OpenBMB/ChatDev/releases/tag/v2.0.0 (2026-10-10); https://github.com/OpenBMB/ChatDev/releases (2026-10-10)

---

## 5. Munder Difflin

- **Original name supplied:** Munder Difflin
- **Exact matched project:** Munder Difflin — "Agent harness to run an office of your clones" (name is an intentional play on the fictional Dunder Mifflin paper company; no "Dunder Mifflin"-named coding resource found)
- **Canonical URL:** https://github.com/jeffreycayao/munder-difflin
- **Repository files inspected:** README.md (search-result text: description, wrapped CLIs, stack, features); docs/media assets noted. Secondary: gulum/munder-difflin blog post "why-we-built-munder-difflin.md" (references chaitanyagiri/munder-difflin fork line — author blog); cartychris/munder-difflin fork (README v0.4.5, MIT, CHANGELOG.md, CONTRIBUTING.md, Discord)
- **What it actually contains:** Free, open-source, local-first multi-agent harness; Electron + React + TypeScript + Pixi.js + xterm.js + node-pty desktop app that visualizes agents as avatars at desks on a shared office floor; coordinator "your clone" (Michael); agents that message, route, and remember
- **What it actually does:** Turns the terminal coding CLI you already run into persistent clones that keep working while you're away, coordinated as an office of agents on your own machine; works with existing subscriptions "on their hourly limits"
- **Where it can be used:** Local machine, macOS / Windows / Linux
- **Compatibility and integration type:** Wraps Claude Code, Antigravity (Gemini), OpenAI Codex, xAI Grok, Kimi Code, Gemini CLI, Qwen, OpenCode, Crush, pi.dev, GitHub Copilot CLI, and Cursor; bring-your-own keys and local LLMs supported
- **Relevant limitations:** Self-described "working prototype"; GitHub Trending #1 repo of the day and Product Hunt #5 (attention spike); fork network exists (cartychris/munder-difflin, chaitanyagiri/munder-difflin)
- **Verification status:** Verified
- **Sources:** https://github.com/jeffreycayao/munder-difflin (README, inspected via search 2026-10-10); https://github.com/gulum/munder-difflin/blob/HEAD/blog/src/posts/why-we-built-munder-difflin.md (2026-10-10)

---

## 6. Taste skill

- **Original name supplied:** Taste skill
- **Exact matched project:** **Taste Skill** — "Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop" by Leonxlnx
- **Canonical URL:** https://github.com/Leonxlnx/taste-skill (site: https://tasteskill.dev)
- **Repository files inspected:** README.md (root file list: `.claude-plugin/`, `skills/`, `scripts/`, `examples/`, `research/`, `assets/`, `CHANGELOG.md`, `skill.sh`, `LICENSE`); full skills table (install names); settings/dials; FAQ. Note: folder names ≠ install names (install name is the `name:` frontmatter, e.g. `design-taste-frontend`)
- **What it actually contains:** Portable Agent Skills library (MIT): implementation skills — `taste-skill` (install name `design-taste-frontend`, v2 experimental), `taste-skill-v1` (`design-taste-frontend-v1`), `gpt-tasteskill` (`gpt-taste`), `image-to-code-skill` (`image-to-code`), `redesign-skill` (`redesign-existing-projects`), `soft-skill` (`high-end-visual-design`), `output-skill` (`full-output-enforcement`), `minimalist-skill` (`minimalist-ui`), `brutalist-skill` (`industrial-brutalist-ui`), `stitch-skill` (`stitch-design-taste`, includes optional DESIGN.md export); image-generation skills (`imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`); `research/` background writing; `scripts/`; Claude Code plugin wrapper (`.claude-plugin/`)
- **What it actually does:** Enforces design taste in AI-generated frontends: anti-slop rules (bans on generic patterns), three tunable dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY), canonical GSAP code skeletons, redesign-audit protocol; image-first workflow (generate references → implement)
- **Where it can be used:** Any Agent-Skills-compatible agent — Claude Code, Codex, Cursor, Copilot, etc.; framework-agnostic (React, Vue, Svelte)
- **Compatibility and integration type:** Agent Skills (`npx skills add https://github.com/Leonxlnx/taste-skill` or `--skill "<install-name>"`); Claude Code plugin marketplace; SKILL.md files copyable into repos/conversations
- **Relevant limitations:** Default `design-taste-frontend` is v2 experimental (active iteration); framework targets design intent, not a single framework API; companion product **TasteCode** (tastecode.dev) — local desktop workspace with a design agent, separate repo
- **Verification status:** Verified (Leonxlnx/taste-skill as the canonical "Taste skill"; ~94k stars)
- **Sources:** https://github.com/Leonxlnx/taste-skill (README inspected 2026-10-10); https://tasteskill.dev
- **Variants noted (different skills, similar names):** sprungundlandung/taste-skill and lamwon/taste-skill — a *different* "taste-skill" (reverse-engineers any website's design taste into tokens + trade-offs; `/taste <url>` workflow; exports to Cursor/Windsurf/CLAUDE.md/Copilot/Bolt/Antigravity/v0/Figma Make/Lovable); ntoledo319/helldeck `.claude/skills/taste-engineering/` (taste audit/facelift crew)

---

## 7. Frontend design skill

- **Original name supplied:** Frontend design skill
- **Exact matched project:** "frontend-design" is a *generic skill name* used by many authors — no single canonical repo is established by the supplied name alone. Strongest canonical candidate: the `frontend-design` skill in **anthropics/skills** (mirrored copies of Anthropic's official skill circulate widely; see Variants)
- **Canonical URL:** https://github.com/anthropics/skills (canonical home of Anthropic's frontend-design skill; skill path `skills/frontend-design/SKILL.md` per mirrors — not directly inspected on the canonical tree)
- **Repository files inspected:** Mirrors/copies of the skill: idwong/dev-skills `dev-impl/skills/frontend-design/SKILL.md` (full SKILL.md: name/description frontmatter, Design Thinking section, anti-AI-slop guidance); evolving-machines-lab/evolve `skills/frontend-design/SKILL.md`; chaitanyame/test-harness_ralph `.github/skills/frontend-design/SKILL.md`; limaon/dotfiles `.config/opencode/skills/frontend-design/SKILL.md`; tobihagemann/turbo `skills/frontend-design/SKILL.md`; tomevault-io/skills-registry `yukiteruamano--skills--frontend-design/SKILL.md` (yukiteruamano variant: React+Tailwind generation with a11y requirements)
- **What it actually contains (the widely-copied Anthropic-style skill):** SKILL.md guiding agents to create distinctive, production-grade frontend interfaces: bold aesthetic direction (purpose/tone/constraints/differentiation), anti-generic-"AI slop" rules, production-grade implementation in HTML/CSS/JS or React/Vue
- **What it actually does:** Steers coding agents to implement real working frontend code with a deliberate aesthetic point-of-view rather than generic template output
- **Where it can be used:** Claude Code, Codex, Cursor, OpenCode, Copilot, and other Agent-Skills-compatible agents (`.claude/skills/`, `.agents/skills/`, `.github/skills/`, `.config/opencode/skills/` placements observed)
- **Compatibility and integration type:** Agent Skills (SKILL.md, drop-in folder)
- **Relevant limitations:** Name collision across many authors means the "Frontend design skill" lead is inherently ambiguous; content of copies varies (Anthropic-style anti-slop variant vs. yukiteruamano React+Tailwind variant); licensing varies (Apache-2.0 vs. LICENSE.txt terms)
- **Verification status:** Partially verified (canonical candidate = anthropics/skills `frontend-design`; the exact canonical file was not inspected on the canonical tree, only on mirrors/copies)
- **Sources:** https://github.com/anthropics/skills (2026-10-10); https://github.com/idwong/dev-skills (SKILL.md inspected via search 2026-10-10); https://github.com/tomevault-io/skills-registry/blob/HEAD/yukiteruamano--skills--frontend-design/SKILL.md (2026-10-10)

---

## 8. Backend design skill

- **Original name supplied:** Backend design skill
- **Exact matched project:** Not established — "backend-design" is a generic skill name with multiple independent implementations by different authors; no single canonical match emerged (notably, Anthropic's anthropics/skills does not appear to ship a backend-design skill)
- **Canonical URL:** None established
- **Repository files inspected:** ainnaziha/claude-atelier `plugins/atelier/skills/backend-design/SKILL.md` (backend design brief via interview; server-side counterpart to `design-brief`); keyvaluesoftwaresystems/kv-skills `skills/backend-design/SKILL.md` (backend LLD artifact writer, file:line-grounded); firdausmntp/techneuma `backend-design/SKILL.md` (Apache-2.0, API/services/jobs design quality bar, `reference/api-contracts.md`); majiayu000/claude-skill-registry `skills/design/backend-design/SKILL.md` (backend for Design OS frontend components); xsefirosus/sefi-agents `plugins/sefi-core/skills/backend-design/SKILL.md` (contract-first API design, anti-hallucination rules)
- **What it actually contains:** Author-dependent: interview-driven backend briefs, low-level-design artifact writers, API-contract design guides, operational quality bars
- **What it actually does:** Guides agents through backend/API/data-model/scale/observability design before implementation
- **Where it can be used:** Agent-Skills-compatible agents (Claude Code, Cursor, Codex, etc.)
- **Compatibility and integration type:** Agent Skills (SKILL.md drop-in)
- **Relevant limitations:** Genuinely ambiguous lead; the five candidates above are distinct projects, not forks of one canonical skill
- **Verification status:** Unresolved (candidates recorded; no canonical match)
- **Sources:** https://github.com/ainnaziha/claude-atelier (2026-10-10); https://github.com/keyvaluesoftwaresystems/kv-skills (2026-10-10); https://github.com/firdausmntp/techneuma (2026-10-10); https://github.com/majiayu000/claude-skill-registry (2026-10-10); https://github.com/xsefirosus/sefi-agents (2026-10-10)

---

## 9. public-apis/public-apis

- **Original name supplied:** public-apis/public-apis
- **Exact matched project:** Public APIs — "A collective list of free APIs" (org account `public-apis`)
- **Canonical URL:** https://github.com/public-apis/public-apis
- **Repository files inspected:** README.md (structure via README outline: APILayer suite sections, MCP Servers section, Index of ~51 categories: Animals → Weather; each category table with API / Description / Auth / HTTPS / CORS columns); root files: `.github/`, `scripts/`, `CONTRIBUTING.md`, `LICENSE`, `README.md`
- **What it actually contains:** Curated markdown catalog of 1,400+ free public APIs across 51 categories; contribution guide; CI scripts for list validation; APILayer-sponsored sections; MCP Servers section (newer addition)
- **What it actually does:** Serves as the unofficial starting point for finding free APIs for projects and portfolios; Auth/HTTPS/CORS columns answer the three key integration questions per API
- **Where it can be used:** Any developer/agentic workflow needing API discovery; consumed as a reference page, forks, and by scrapers/wrappers
- **Compatibility and integration type:** None directly (documentation resource); API-backed access via a community "API for this project"
- **Relevant limitations:** MIT; community-curated (listings can go stale); APILayer commercial sponsorship influences top-of-README placement
- **Verification status:** Verified
- **Sources:** https://github.com/public-apis/public-apis (repo metadata + README outline inspected 2026-10-10)

---

## 10. Agent Skills

- **Original name supplied:** Agent Skills
- **Exact matched project:** Agent Skills — the open standard for agent skills (SKILL.md format), originally developed by Anthropic and released as an open standard
- **Canonical URL:** https://agentskills.io (spec: https://agentskills.io/specification); spec repo: https://github.com/agentskills/agentskills
- **Repository files inspected:** Not a single repo: spec repo `agentskills/agentskills` (README: progressive disclosure — Discovery/Activation/Execution; client showcase; Apache-2.0 code / CC-BY-4.0 docs); MicrosoftDocs/Agent-Skills README (skill frontmatter structure; platform docs table); supabase/agent-skills README (`.well-known/agent-skills/` discovery spec, dist/index.json); NativeScript/skills README (official product skills per open standard)
- **What it actually contains:** The format spec (SKILL.md with `name`/`description` frontmatter + Markdown instructions, optional scripts/references/assets), documentation site, example skills, a `.well-known` discovery URI spec (schema v0.2.0), client showcase
- **What it actually does:** Defines how agents discover (name+description only), activate (load full SKILL.md), and execute skills with a small context footprint; enables write-once/run-anywhere reusable instruction packages across agents
- **Where it can be used:** Claude Code, GitHub Copilot (CLI/VS Code/agents), OpenAI Codex, Cursor, Gemini CLI, OpenCode, OpenClaw, Windsurf, and other compatible clients
- **Compatibility and integration type:** SKILL.md folders installed to `~/.claude/skills/`, `~/.codex/skills/`, `.github/skills/`, `.cursor/skills/`, etc.; `npx skills add` CLI; `gh skill` (GitHub CLI); `.well-known/agent-skills/` HTTP discovery
- **Relevant limitations:** Standard is young and ecosystem-fragmented (many competing "awesome" lists and registries); frontmatter conventions vary slightly between hosts
- **Verification status:** Verified
- **Sources:** https://agentskills.io (2026-10-10); https://github.com/agentskills/agentskills (via erfnzdeh/awesome-agent-skills-1 list, 2026-10-10); https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (via kaiykk/skillnudge research note, 2026-10-10); https://github.com/supabase/agent-skills (2026-10-10); https://github.com/NativeScript/skills (2026-10-10)
- **Related/companion resources:** anthropics/skills (official Anthropic skills), openai/skills, github/awesome-copilot, MicrosoftDocs/Agent-Skills, microsoft/agent-skills, microsoft/azure-skills, vercel-labs/add-skill (official skills CLI), registries: skill.md, skills.sh, agent-skills.md

---

## 11. Astryx / facebook/astryx

- **Original name supplied:** Astryx / facebook/astryx
- **Exact matched project:** Astryx — Meta's open-source design system, "fully customizable and agent ready" (canonical org: facebook)
- **Canonical URL:** https://github.com/facebook/astryx (docs: https://astryx.atmeta.com; Storybook and Sandbox on facebook.github.io/astryx)
- **Repository files inspected:** README.md (root file list: `apps/`, `packages/`, `internal/`, `docs/`, `AGENTS.md`, `CLAUDE.md`, `IME_GUARD_DESIGN.md`, `SECURITY.md`, `package.json` (pnpm workspace), `playwright.config.ts`); README sections: Getting Started, Packages table, Principles, Architecture (Foundations/Components/Patterns), Project Structure
- **What it actually contains:** 150+ accessible typed React components (React 19+), styles authored in StyleX but invisible to consumers (className overrides with Tailwind/CSS modules/plain CSS work); brand-level theming via CSS custom properties; dark mode; 7 ready-made themes (neutral, butter, chocolate, matcha, stone, gothic, y2k); ready-to-ship templates; `@astryxdesign/lab` (experimental), `@astryxdesign/vega`/`@astryxdesign/charts` (canary); docs site, Storybook, Sandbox; `swizzle` for ejecting component source
- **What it actually does:** A cohesive design system for people and AI assistants to build from the same reference; packages: `@astryxdesign/core` (components/themes/utils), `@astryxdesign/cli` (component docs, templates, scaffolding, themes, codemods), `@astryxdesign/build` (StyleX build plugins), `@astryxdesign/theme-*`
- **Where it can be used:** React 19+ projects (Next.js, Tailwind, Vite, CDN); Meta-internal system of 8 years powering 13,000+ apps, open-sourced Jan 2026 (beta)
- **Compatibility and integration type:** Agent integration is **CLI bash calls** — e.g. `npm run astryx -- component --list` via `node node_modules/@astryxdesign/cli/clients/cli/bin/astryx.mjs`; prior correction upheld: **NO MCP server** (none found in README or packages; CLI is the documented agent surface; the `--dense` output flag is carried over from prior verified research, not re-verified in this pass)
- **Relevant limitations:** Beta; MIT; requires React 19+ peer deps (`react`, `react-dom`, `@stylexjs/stylex`)
- **Verification status:** Verified (repo, design-system components, CLI, docs/templates; prior no-MCP-server correction re-confirmed)
- **Sources:** https://github.com/facebook/astryx (README + root file list inspected 2026-10-10)

---

## 12. DeepSec by Vercel / vercel/deepsec

- **Original name supplied:** DeepSec by Vercel / vercel/deepsec
- **Exact matched project:** deepsec — Vercel Labs' open-source agent-powered vulnerability scanner. Org corrected: actual repo is **vercel-labs/deepsec**, not vercel/deepsec
- **Canonical URL:** https://github.com/vercel-labs/deepsec (site: https://deepsec.sh; Vercel OSS page: https://vercel.com/oss/deepsec; launch post: https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base)
- **Repository files inspected:** README.md (via search-result text: workflow, cost warning, resume behavior, npm/Labs badges); vercel.com/oss/deepsec page (scan → matchers → agents → revalidate flow, `npx deepsec init`); Vercel launch blog (architecture: scan/investigate/revalidate/enrich/export; optional Vercel Sandbox fanout)
- **What it actually contains:** TypeScript CLI distributed via npm (`deepsec` package); plugin system for auth models/data layers/team conventions; docs (incl. `docs/models.md` for `--thinking-level`); static-analysis matcher stage; agent investigation + revalidation loops; git-metadata enrichment; ticket export formatter
- **What it actually does:** Scans large codebases for hard-to-find vulnerabilities: regex/static pre-scan selects security-sensitive files → coding agents (claude/codex CLIs at max reasoning: Claude Opus 4.7, GPT 5.5) investigate each candidate tracing data flows → second agent run revalidates (cuts the stated 10–20% false-positive rate) → git metadata identifies owners → export formats actionable tickets
- **Where it can be used:** Own infrastructure (laptop or worker fleet); large repos fan out across parallel workers, incl. optional Vercel Sandboxes (1,000+ concurrent in Vercel's own use); resumable runs
- **Compatibility and integration type:** Uses the user's existing Claude/Codex subscriptions for inference; CLI entry `npx deepsec init`
- **Relevant limitations:** Apache-2.0; **cost warning**: scans can cost thousands to tens of thousands of dollars on large repos (best models at max thinking); not deterministic SAST — best paired with deterministic scanners; intended for governed review workflows with human approval
- **Verification status:** Verified (org corrected to vercel-labs/deepsec)
- **Sources:** https://github.com/vercel-labs/deepsec (2026-10-10); https://vercel.com/oss/deepsec (2026-10-10); https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base (2026-10-10); https://deepsec.sh

---

## 13. Everything Claude Code / affaan-m/ECC

- **Original name supplied:** Everything Claude Code / affaan-m/ECC
- **Exact matched project:** ECC (formerly "Everything Claude Code") by affaan-m — an open-source performance harness / "operating system" for AI coding agents. Note: the expanded name has been retired; repo renamed `affaan-m/everything-claude-code` → `affaan-m/ECC` (Oct 2026)
- **Canonical URL:** https://github.com/affaan-m/ECC
- **Repository files inspected:** Commit "chore: retire the Everything Claude Code name, ECC only (#3330)" (file list: `.adal/`, `.agents/skills/ecc-conventions/`, `.claude/commands/`, `.claude/ecc-tools.json`, `.claude/enterprise/controls.md`, `.claude/homunculus/instincts/`, `.claude/research/`); migration doc `docs/MIGRATION-1X-TO-2.0.md` (via krishnakanthb13 fork); README (via sheeeng fork: naming note, install commands, settings.json snippet)
- **What it actually contains:** Component types: specialized subagents (`agents/*.md`), skills (`skills/*/SKILL.md` — ~182), legacy slash-command shims (`commands/` — ~68), hierarchical rules (`rules/` common + language-specific, 12+ ecosystems), hooks (`hooks/hooks.json` + `scripts/hooks/*.js`), MCP server configs (`mcp-configs/`, `.mcp.json`), "instincts" (project-scoped learned patterns), continuous-learning pipeline mining session activity
- **What it actually does:** Coordinates an engineering lifecycle (plan → test → implement → review → verify → remember → improve) inside terminal coding agents via runtime hooks, prompt profiles, and memory; enforces development lifecycles and cross-session memory
- **Where it can be used:** Claude Code (via plugin marketplace `ecc@ecc`), plus compatible harnesses (Cursor, OpenCode, Codex, Gemini, Antigravity); npm package `ecc-universal`
- **Compatibility and integration type:** Claude Code plugin (`/plugin marketplace add https://github.com/affaan-m/ECC`, `/plugin install ecc@ecc`); install.sh profiles; rules copied into `~/.claude/rules/`; MCP configs
- **Relevant limitations:** Three non-interchangeable identifiers (repo `affaan-m/ECC`, plugin `ecc@ecc`, npm `ecc-universal`); 1.x → 2.0 migration requires removing old plugin to avoid duplicate skills/hooks
- **Verification status:** Verified
- **Sources:** https://github.com/affaan-m/ECC (2026-10-10); https://github.com/affaan-m/ecc/commit/c05b2d6614f62f6db0047669aa4eefb223d478f9 (2026-10-10); https://github.com/krishnakanthb13/everything-claude-code/blob/HEAD/docs/MIGRATION-1X-TO-2.0.md (2026-10-10); https://coderlegion.com/26762/ecc-an-open-source-performance-harness-and-operating-system-for-ai-coding-agents (2026-10-10)

---

## 14. Ruflo / ruvnet/ruflo

- **Original name supplied:** Ruflo / ruvnet/ruflo
- **Exact matched project:** Ruflo by ruvnet — confirmed as the successor name of **Claude Flow** ("Claude Flow is now Ruflo — named by rUv"; powered by Cognitum.One agentic architecture)
- **Canonical URL:** https://github.com/ruvnet/ruflo
- **Repository files inspected:** README.md (search-result text: architecture diagram, quick-start, two install paths, background/name origin, plugin table); `.claude-plugin/docs/INSTALLATION.md` (install methods, 150+ commands/74+ agents inventory); releases v3.50.0 and v3.51.0 notes (Claude Code "mods", /ruflo console)
- **What it actually contains:** Agent harness: 100+ specialized agents, coordinated swarms, self-learning memory, federation across machines, enterprise security guardrails, MCP server (314 tools), hooks system, daemon, Claude Code plugins (`.claude-plugin/`), `/ruflo` console mod (swarm topology, federation map, plugin health, learning pipeline, cost gauge, approvals queue)
- **What it actually does:** Execution layer around Claude Code and Codex: agents self-organize into swarms, learn from tasks, remember across sessions, and federate securely across machines; conceptual learning loop User → CLI/MCP → Router → Swarm → Agents → Memory → LLM providers
- **Where it can be used:** Local dev machines; `npx ruflo init` (full loop) or Claude Code plugin install (lightweight: slash commands + skills + agent defs, zero workspace files)
- **Compatibility and integration type:** CLI (`ruflo`, `npx ruflo init`), MCP server, Claude Code plugin marketplace (`ruvnet/ruflo`), hooks; npm packages `@claude-flow/cli`, `claude-flow`, `ruflo`; native Claude Code / Codex / Hermes integrations
- **Relevant limitations:** "Underneath, powered by Cognitum.One" — the Rust-based engine claim is the project's own description; license of the core package should be checked before reuse; two install paths have very different surface areas
- **Verification status:** Verified (prior correction confirmed: ruvnet/ruflo = Claude Flow's successor; duplicate mentions are one resource)
- **Sources:** https://github.com/ruvnet/ruflo (2026-10-10); https://github.com/ruvnet/ruflo/releases/tag/v3.50.0 (2026-10-10); https://github.com/ruvnet/ruflo/releases/tag/v3.51.0 (2026-10-10); https://github.com/ruvnet/ruflo/blob/HEAD/.claude-plugin/docs/INSTALLATION.md (2026-10-10)

---

## 15. Claude Cookbooks / anthropics/claude-cookbooks

- **Original name supplied:** Claude Cookbooks / anthropics/claude-cookbooks
- **Exact matched project:** Claude Cookbooks by Anthropic — org is **anthropics** (with an s), as previously established
- **Canonical URL:** https://github.com/anthropics/claude-cookbooks
- **Repository files inspected:** Root file list (`capabilities/`, `tool_use/`, `third_party/`, `multimodal/`, `patterns/agents`, `skills/`, `claude_agent_sdk/`, `evals/agentic_search`, `cost_optimization/`, `finetuning/`, `managed_agents/`, `observability/`, `anthropic_cookbook/` legacy dir, `scripts/`, `tests/`, `registry.yaml`, `authors.yaml`, `CLAUDE.md`, `CONTRIBUTING.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `tox.ini`, `.pre-commit-config.yaml`); commit "Add content moderation cookbook" (files: policies.md, schema.json, rules.golden.json, samples.jsonl, build_creatives.py, labeled image data, standalone eval script)
- **What it actually contains:** Collection of Jupyter notebooks/recipes: core capabilities (classification, RAG, summarization), tool use (customer service agent, calculator, SQL), third-party integrations (Pinecone, Wikipedia, VoyageAI embeddings), multimodal (images, charts, forms), advanced (sub-agents, PDF upload, automated evals, JSON mode), skills, Claude Agent SDK examples, agentic evals, cost optimization, finetuning, managed agents, observability
- **What it actually does:** Provides copy-able code and guides for building with Claude — real-world Claude API integration patterns beyond simple prompt calls (e.g., Haiku+Opus sub-agent orchestration balancing cost and complexity)
- **Where it can be used:** Python notebooks run locally with a Claude API key; concepts portable to other languages
- **Compatibility and integration type:** Notebooks + scripts; no package install (reference repo); links to Claude API Fundamentals course
- **Relevant limitations:** MIT; mostly Python — adaptation needed for other languages; requires Claude API key (cost); assumes familiarity with AI concepts
- **Verification status:** Verified
- **Sources:** https://github.com/anthropics/claude-cookbooks (repo metadata + commit inspected 2026-10-10); https://github.com/anthropics/claude-cookbooks/commit/5a2576e211ba6bb6a2698cd14989d4091398f441 (2026-10-10)

---

## 16. Designs

- **Original name supplied:** Designs
- **Exact matched project:** Not established — the bare name "Designs" matches no specific project in exact search; too generic to resolve without more context
- **Canonical URL:** None established
- **Repository files inspected:** None (no canonical candidate)
- **What it actually contains:** Unknown
- **What it actually does:** Unknown
- **Where it can be used:** Unknown
- **Compatibility and integration type:** Unknown
- **Relevant limitations:** Plausible leads (not confirmed as intended): anthropics/skills `canvas-design` skill; Leonxlnx/taste-skill variants; podo/design-agent-skills; bergside/awesome-design-skills; VoltAgent/awesome-design-md; mollyrrose/super_claude `hermes-design-md` skill. None can be tied to the bare name "Designs" with evidence
- **Verification status:** Unresolved
- **Sources:** No primary source established (2026-10-10)

---

## 17. Firecrawl

- **Original name supplied:** Firecrawl
- **Exact matched project:** Firecrawl — web data/context API for AI agents (by Firecrawl Inc.)
- **Canonical URL:** https://github.com/firecrawl/firecrawl (site: https://firecrawl.dev; docs: https://docs.firecrawl.dev)
- **Repository files inspected:** README.md (root file list: `apps/`, `examples/`, `firecrawl-cli/`, `firecrawl-cli-skills/`, `firecrawl-skills/`, `firecrawl-workflows/`, `skills/`, `AGENTS.md`, `CLAUDE.md`, `SELF_HOST.md`, `docker-compose.yaml`, `CONTRIBUTING.md`, `LICENSE`); README sections: Feature Overview, Quick Start (Search/Scrape/Interact), Power Your Agent (Skill/MCP/Agent Onboarding), More Endpoints (Agent/Crawl/Map/Batch Scrape), SDKs, Integrations
- **What it actually contains:** Core endpoints: Search (web search + full page content), Scrape (URL → markdown/HTML/screenshots/structured JSON), Interact (AI-prompt or code-driven page interaction), Agent (`/v2/agent` — autonomous data gathering with effort levels and structured output), Crawl, Map, Batch Scrape; SDKs: Python, Node.js, Go, Java, Elixir, Rust, Ruby, .NET, PHP; CLI (`firecrawl-cli`); skill dirs (`firecrawl-cli-skills/`, `firecrawl-skills/`); MCP server (`firecrawl-mcp`); agent onboarding skill; self-host via Docker; actions (click/scroll/write/wait); media parsing (PDF/DOCX); rotating proxies, rate-limit handling
- **What it actually does:** Turns websites into LLM-ready data: finds sources, extracts content, converts to clean markdown/structured JSON for agents and apps; "Agent" endpoint gathers data from a natural-language description without URLs
- **Where it can be used:** Hosted service (firecrawl.dev, API key) or self-hosted (docker-compose, SELF_HOST.md); AGPL-3.0
- **Compatibility and integration type:** REST API (api.firecrawl.dev/v2), language SDKs, MCP server (`npx -y firecrawl-mcp`), Agent Skill (`npx -y firecrawl-cli@latest init --all --browser`; works with Claude Code, Antigravity, OpenCode, etc.), agent onboarding skill at https://firecrawl.dev/agent-onboarding/SKILL.md, CLI
- **Relevant limitations:** AGPL-3.0 (copyleft); hosted service requires API key and is usage-priced; self-hosted needs proxy/browser infrastructure for hard targets
- **Verification status:** Verified
- **Sources:** https://github.com/firecrawl/firecrawl (README + root file list inspected 2026-10-10); https://firecrawl.dev; https://docs.firecrawl.dev

---

## 18. Eve by Vercel / vercel/eve

- **Original name supplied:** Eve by Vercel / vercel/eve
- **Exact matched project:** eve — "The Open Framework for Building Agents" by Vercel (lowercase name, as used upstream)
- **Canonical URL:** https://github.com/vercel/eve (site: https://eve.dev; product page: https://vercel.com/eve)
- **Repository files inspected:** README.md (root file list: `.agents/skills/`, `skills/eve/`, `apps/`, `packages/`, `docs/`, `e2e/`, `research/`, `AGENTS.md`, `CLAUDE.md`, `package.json` pnpm/turbo monorepo, `CONTRIBUTING.md`, `SECURITY.md`); README sections: filesystem authoring interface, quick start, minimal example, Add Web Chat, beta terms
- **What it actually contains:** TypeScript framework where an agent is a directory: `agent/agent.ts` (model/runtime config), `agent/instructions.md` (system prompt), `agent/tools/` (typed `defineTool` functions), `agent/skills/` (on-demand playbooks), `agent/subagents/`, `agent/channels/` (HTTP/Slack/Discord/web), `agent/schedules/` (cron-style jobs); npm `eve` package (bundles docs in `node_modules/eve/docs`); terminal UI; deployment to Vercel Functions
- **What it actually does:** Filesystem-first durable agent framework ("Next.js for web apps, but for agents"): durable execution (session state checkpointed/replayed via Vercel Workflow SDK — survives restarts/deployments), sandboxed compute (Vercel Sandbox; local Docker/microsandbox/bash backends), human-in-the-loop approval gates, subagents, built-in eval hooks, OpenTelemetry observability, model-agnostic routing via Vercel AI Gateway. Used internally for v0 and Vercel's agent fleet; launched 2026-06-17, public beta
- **Where it can be used:** `npx eve@latest init my-agent`; local dev without Vercel account; production deploy via `npx eve deploy` to Vercel platform (Workflow/Sandbox/AI Gateway managed services are usage-priced)
- **Compatibility and integration type:** TypeScript-first; AI Gateway model routing (any provider); channels for Slack/Discord/web chat; web dev relation: deploys as a Vercel Functions service, `npx eve add channel/web` for web chat
- **Relevant limitations:** Apache-2.0 framework, but production infrastructure (Workflow, Sandbox, AI Gateway) runs on Vercel's platform (account + standard pricing); beta — APIs may change before GA
- **Verification status:** Verified (prior finding — filesystem-first durable agent framework, June 2026 — confirmed against the live README)
- **Sources:** https://github.com/vercel/eve (README + root file list inspected 2026-10-10); https://eve.dev; https://openorchestrators.org/news/vercel-eve-filesystem-first-agent-framework/ (2026-10-10)

---

## 19. Strix

- **Original name supplied:** Strix
- **Exact matched project:** Not conclusively established — four distinct candidates share the name. Primary candidate by evidence weight: **usestrix/strix** (open-source AI penetration testing tool; the only "Strix" with a Wikipedia article and dominant adoption). Recorded as candidate, not claimed as intended
- **Canonical URL (primary candidate):** https://github.com/usestrix/strix (site: https://strix.ai)
- **Repository files inspected (primary candidate):** Root file list (`strix/` package with `agents/`, `core/`, `tools/`, `skills/`, `runtime/`, `interface/`, `report/`, `viewer/`; `containers/`, `docs/`, `tests/`, `benchmarks/`, `scripts/`, `AGENTS.md`, `CONTRIBUTING.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `strix.spec`); README outline (Strix Overview, Use Cases, Quick Start, Ways to Run, Strix Cloud, Enterprise, Use from Coding Agent, Features incl. Graph of Agents, CI/CD, MCP servers); via mohamed-amine-slama/vulnscan-ai integration README (layout table, run instructions)
- **What it actually contains (primary candidate):** Autonomous AI pentesting CLI/TUI: multi-agent orchestration (Graph of Agents), offensive-security tools + agent skills, Docker-sandboxed runtime, agentic pentesting tools, vulnerability scanner, reports + local web viewer, CI/CD GitHub Actions support, headless mode, nine bundled agent skills (`penetration-testing-with-strix`, `fix-security-vulnerabilities-with-strix`, `ci-security-scanning-with-strix`, etc.), PyPI package `strix-agent`
- **What it actually does (primary candidate):** Runs autonomous AI agents to find (and help fix) app vulnerabilities against owned targets — reconnaissance, exploitation, real PoC validation; "autonomous AI hackers" framing
- **Where it can be used:** Python 3.12+, uv, Docker (running), LLM API key (`STRIX_LLM`, `LLM_API_KEY`); targets: source dirs, live apps, OpenAPI/Swagger/Postman specs; `pipx install strix-agent` or `curl https://strix.ai/install`
- **Compatibility and integration type:** CLI; agent skills via `npx skills add usestrix/strix`; connect-your-own MCP servers; coding-agent integration docs
- **Relevant limitations:** Apache-2.0; offensive-security tooling — only run against apps you own or have written authorization to test; requires Docker + LLM provider
- **Verification status:** Partially verified (primary candidate identified with strong evidence: 67k stars, Wikipedia "Strix (security)" article, security topic fit; alternatives recorded — not claimed as the intended resource)
- **Sources:** https://github.com/usestrix/strix (repo metadata + README outline inspected 2026-10-10); https://en.wikipedia.org/wiki/Strix_(security) (2026-10-10); https://github.com/biswadipgoj/biswodip-engineering-skills/blob/HEAD/integrations/strix/README.md (2026-10-10)
- **Alternative candidates:** strixgov/strix (agent execution-control trust primitives: verifier, tool-gateway, capability packs; MIT + Elastic License MCP adapter; mirror of closed monorepo — https://github.com/strixgov/strix); strixproject/Strix (CLI pentesting assistant with system-prompt presets); mythicalsign/strix (fork with StrixDB knowledge-repo feature)

---

## 20. DESIGN.md / design.md

- **Original name supplied:** DESIGN.md / design.md
- **Exact matched project:** DESIGN.md — Google Labs' open format specification for describing a visual identity to coding agents (repo: google-labs-code/design.md)
- **Canonical URL:** https://github.com/google-labs-code/design.md (npm: `@google/design.md`)
- **Repository files inspected:** README.md (root file list: `docs/spec.md`, `examples/`, `packages/cli/`, `.agents/skills/`, `PHILOSOPHY.md`, `CONTRIBUTING.md`, `skills-lock.json`); sections: The Format, File Structure, Token Schema, Token Types, Section Order, Component Tokens, Consumer Behavior, CLI Reference (lint/diff/export/spec), Linting Rules (11 rules), Design Token Interoperability, Status
- **What it actually contains:** Spec + CLI + examples. A DESIGN.md file = YAML front matter (machine-readable tokens: `name`, `colors`, `typography`, `rounded`, `spacing`, `components` with `{path.to.token}` references; `version: alpha`; optional `omitted`) + Markdown body (human rationale in canonical section order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts)
- **What it actually does:** Gives agents a persistent, structured understanding of a design system — the design counterpart to CLAUDE.md/AGENTS.md. CLI validates (`lint`: structure + WCAG contrast, JSON findings), diffs versions for regressions, exports to Tailwind (v3/v4) or W3C DTCG JSON, and prints the spec itself for prompt injection
- **Where it can be used:** Any coding agent workflow; `npx @google/design.md lint DESIGN.md` (with `designmd` alias for Windows); Apache-2.0
- **Compatibility and integration type:** CLI shell-out from agents/skills (pi-ux orchestrates it via shell-out, zero-dep); consumer skills: `hermes-design-md` (mollyrrose/super_claude, loggger101/hermes_skills), `design-md-author` (guowushi/agentskills), `design-md-visual-system` (lizliz404/agent-skills), anthropics `design-system` skill (knowledge-work-plugins)
- **Relevant limitations:** Spec status "alpha", actively evolving; schema gaps noted by third parties (no motion/dark-mode/breakpoint tokens as of Aug 2026)
- **Verification status:** Verified
- **Sources:** https://github.com/google-labs-code/design.md (README + root file list inspected 2026-10-10)
- **Collections/generators:** https://github.com/VoltAgent/awesome-design-md (73+ brand DESIGN.md files collected; prior finding confirmed via mimukit/skills plan doc 2026-10-10); https://getdesign.md (300+ reverse-engineered brand files, per same source)

---

## 21. awesome-claude-skills

- **Original name supplied:** awesome-claude-skills
- **Exact matched project:** ComposioHQ/awesome-claude-skills — "A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows" (dominant match: ~76k stars; contains actual skill folders, not just links)
- **Canonical URL:** https://github.com/ComposioHQ/awesome-claude-skills
- **Repository files inspected:** Root file list (skill directories: `artifacts-builder`, `brand-guidelines`, `canvas-design`, `changelog-generator`, `competitive-ads-extractor`, `composio-skills`, `connect-apps`, `content-research-writer`, `document-skills`, `internal-comms`, `invoice-organizer`, `mcp-builder`, `meeting-insights-analyzer`, `skill-creator`, `skill-share`, `slack-gif-creator`, `theme-factory`, `twitter-algorithm-optimizer`, `video-downloader`, `webapp-testing`, `template-skill`; `CONTRIBUTING.md`, `README.md`); topics: agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, cursor, gemini-cli, mcp
- **What it actually contains:** Curated collection of installable Claude skills (each a folder with SKILL.md + optional scripts) plus resources/tools for customizing Claude AI workflows; covers codex/cursor/gemini-cli/antigravity in addition to Claude
- **What it actually does:** Discovery + distribution point for ready-made agent skills (clone the skill folder into your skills dir; no configuration)
- **Where it can be used:** Claude Code, Cursor, Copilot, Codex, Gemini CLI, OpenCode, and other Agent-Skills-compatible tools
- **Compatibility and integration type:** SKILL.md folders; `npx skills add` compatible
- **Relevant limitations:** Created 2025-10-17; skill quality/maintenance varies per entry; Composio commercial association
- **Verification status:** Verified (ComposioHQ/awesome-claude-skills as the dominant identity)
- **Sources:** https://github.com/ComposioHQ/awesome-claude-skills (repo metadata + root file list inspected 2026-10-10)
- **Similar repositories (distinct):** jculberson/awesome-claude-skills ("Open-source collection of Agent Skills for Claude Code: documentation tooling, automation"; clone/copy install pattern; MIT); arturayupov/awesome-claude-skills (referenced as install source); travisvn/awesome-claude-skills (~5.7k stars); BehiSecc/awesome-claude-skills (~4.2k stars); mingrath/awesome-claude-skills (list-style fork; PR workflow documented in TerminallyLazy/tree-ring-memory marketing docs); regional mirrors: ammosu/awesome-claude-skills-zh-TW, bbylw/awesome-claude-skills-cn

---

## 22. Anthropic's official skills repository / anthropics/skills

- **Original name supplied:** Anthropic's official skills repository / anthropics/skills
- **Exact matched project:** anthropics/skills — "Public repository for Agent Skills" (Anthropic)
- **Canonical URL:** https://github.com/anthropics/skills
- **Repository files inspected:** Root file list (`.claude-plugin/`, `skills/` directory, `spec/` directory (Agent Skills spec), `template/`, `THIRD_PARTY_NOTICES.md`, `README.md`); README outline (Skill Sets; Try in Claude Code / Claude.ai / API; Creating a Basic Skill; Partner Skills). Skill-set contents established via secondary descriptions: frontend-design, claude-api, docx, pdf, pptx, xlsx, canvas-design, mcp-builder, algorithmic-art, brand-guidelines, skill-creator, document skills (source-available)
- **What it actually contains:** Anthropic's official example/reference skills incl. production document skills (docx/pdf/pptx/xlsx — source-available, not open source), the Agent Skills `spec/`, a skill `template/`, a `skill-creator` skill; also functions as a Claude Code plugin marketplace (`.claude-plugin/`)
- **What it actually does:** Reference implementation and exemplars for the Agent Skills standard; the gold standard for skill structure (SKILL.md anatomy)
- **Where it can be used:** Claude Code (plugin marketplace), Claude.ai, Claude API; skills are portable to other Agent-Skills-compatible hosts
- **Compatibility and integration type:** Claude Code plugin marketplace; SKILL.md folders; spec for cross-host use
- **Relevant limitations:** Some skills are source-available rather than open source — check each directory's license before reuse; repo notes point to agentskills.io for the standard itself
- **Verification status:** Verified
- **Sources:** https://github.com/anthropics/skills (repo metadata + root file list + README outline inspected 2026-10-10); https://github.com/rohithpariki/firm-os/blob/HEAD/docs/anthropic-alignment.md (2026-10-10); https://github.com/devilking7x/awesome-claude-code (2026-10-10)
- **Related official repos:** anthropics/knowledge-work-plugins (11 plugins for Claude Cowork/knowledge workers: Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 connectors); anthropics/claude-plugins-official (Anthropic-managed plugin directory); anthropics/claude-code-action; anthropics/defending-code-reference-harness

---

## 23. NotebookLM skill

- **Original name supplied:** NotebookLM skill
- **Exact matched project:** **notebooklm-skill** — "NotebookLM Skill for Claude" by RoboNuggets (repo: stefandsl/notebooklm-skill). This is a **distinct skill repository beyond teng-lin/notebooklm-py** (the unofficial Python library), though it is built on top of it
- **Canonical URL:** https://github.com/stefandsl/notebooklm-skill
- **Repository files inspected:** README.md (files: `SKILL.md`, `scripts/nlm.py`, `scripts/refresh_auth.py`, `INSTALL_PROMPT.md`, `README.md`); "What This Does" section (query notebooks, add sources, generate slide decks, auto-refresh auth); Requirements (Python 3.9+, Google account with NotebookLM access, Claude); Quick Start (install notebooklm-py via pip, install skill via INSTALL_PROMPT.md, `python scripts/nlm.py login`, `python scripts/nlm.py list`)
- **What it actually contains:** `SKILL.md` (the skill file the agent reads), `scripts/nlm.py` (CLI wrapper for notebooklm-py), `scripts/refresh_auth.py` (headless cookie refresh), `INSTALL_PROMPT.md` (copy-paste setup prompt for Claude)
- **What it actually does:** Connects a Claude agent to Google NotebookLM: query notebooks from inside Claude, add sources automatically (URLs, PDFs, files, raw text), generate branded slide decks, keep auth alive without manual re-login
- **Where it can be used:** Claude (claude.ai/code) or any Claude agent setup; Python 3.9+; Google account with NotebookLM access
- **Compatibility and integration type:** Agent Skill; depends on teng-lin/notebooklm-py (pip install `notebooklm-py[browser]` + `playwright install chromium`) — the unofficial library that reverse-engineers NotebookLM's undocumented RPCs (prior finding upheld: unofficial)
- **Relevant limitations:** Depends on undocumented NotebookLM RPCs via notebooklm-py — can break when Google changes internals; requires Google login/cookies; community project (RoboNuggets), not Google-supported
- **Verification status:** Verified (distinct "NotebookLM skill" exists beyond teng-lin/notebooklm-py)
- **Sources:** https://github.com/stefandsl/notebooklm-skill (README inspected 2026-10-10); fork: https://github.com/takachaa/notebooklm-skill (2026-10-10)

---

## Summary

| # | Original name | Matched project | Status |
|---|---|---|---|
| 1 | OpenViking | volcengine/OpenViking | Verified |
| 2 | PizzaBox by AWS | Pizza Bot (pizza-bot-app/pizza-bot; AWS Open Source Blog) | Corrected |
| 3 | Scrapling by Krim Shoair | D4Vinci/Scrapling by Karim Shoair | Verified |
| 4 | ChatDev 2.0 / devAll | OpenBMB/ChatDev (2.0 = DevAll, one project) | Verified |
| 5 | Munder Difflin | jeffreycayao/munder-difflin | Verified |
| 6 | Taste skill | Leonxlnx/taste-skill | Verified |
| 7 | Frontend design skill | anthropics/skills `frontend-design` (canonical candidate) | Partially verified |
| 8 | Backend design skill | none (5 author-specific candidates) | Unresolved |
| 9 | public-apis/public-apis | public-apis/public-apis | Verified |
| 10 | Agent Skills | agentskills.io + agentskills/agentskills | Verified |
| 11 | Astryx / facebook/astryx | facebook/astryx | Verified |
| 12 | DeepSec by Vercel / vercel/deepsec | vercel-labs/deepsec (org corrected) | Verified |
| 13 | Everything Claude Code / affaan-m/ECC | affaan-m/ECC (name retired → ECC) | Verified |
| 14 | Ruflo / ruvnet/ruflo | ruvnet/ruflo (ex-Claude Flow) | Verified |
| 15 | Claude Cookbooks / anthropics/claude-cookbooks | anthropics/claude-cookbooks (org = "anthropics") | Verified |
| 16 | Designs | none identified | Unresolved |
| 17 | Firecrawl | firecrawl/firecrawl | Verified |
| 18 | Eve by Vercel / vercel/eve | vercel/eve | Verified |
| 19 | Strix | usestrix/strix (primary candidate) + alternatives | Partially verified |
| 20 | DESIGN.md / design.md | google-labs-code/design.md | Verified |
| 21 | awesome-claude-skills | ComposioHQ/awesome-claude-skills | Verified |
| 22 | Anthropic's official skills repository / anthropics/skills | anthropics/skills | Verified |
| 23 | NotebookLM skill | stefandsl/notebooklm-skill (on teng-lin/notebooklm-py) | Verified |

**Totals: 18 Verified · 1 Corrected · 2 Partially verified · 2 Unresolved · 0 Not found**

**Key corrections vs prior research:**
- PizzaBox by AWS: no such project exists; the lead almost certainly refers to AWS's **Pizza Bot** (Sept 2026, AWS Open Source Blog) — name recorded as variant, identification Corrected rather than claimed.
- Scrapling author: "Krim Shoair" → **Karim Shoair** (GitHub D4Vinci).
- DeepSec org: vercel/deepsec → **vercel-labs/deepsec** (Vercel Labs).
- Ruflo: ruvnet/ruflo confirmed as Claude Flow's renamed successor (one resource, per prior correction).
- ECC: "Everything Claude Code" name officially retired; canonical identifier is **affaan-m/ECC** with plugin id `ecc@ecc` and npm package `ecc-universal`.
- Astryx: re-confirmed **NO MCP server**; agent integration is CLI bash calls (`npx @astryxdesign/cli` / `npm run astryx -- <cmd>`); prior correction upheld.
- NotebookLM skill: a distinct skill (**stefandsl/notebooklm-skill** by RoboNuggets) exists on top of teng-lin/notebooklm-py — not just the unofficial library.

**New leads discovered:**
- TasteCode (tastecode.dev) — local desktop workspace with a built-in design agent, from the Taste Skill team.
- getdesign.md — 300+ reverse-engineered brand DESIGN.md files (companion to VoltAgent/awesome-design-md).
- anthropics/knowledge-work-plugins — Anthropic's 11-plugin repo for Claude Cowork (Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365).
- vercel-labs/add-skill — Vercel's official skills CLI.
- agentskills/agentskills — the official spec/documentation repo behind agentskills.io.
- Microsoft's official skills repos (MicrosoftDocs/Agent-Skills, microsoft/agent-skills, microsoft/azure-skills).
- Firecrawl agent-onboarding skill (https://firecrawl.dev/agent-onboarding/SKILL.md) and `firecrawl-cli-skills/` / `skills/` dirs.
- Alternative "taste-skill" implementations (sprungundlandung, lamwon) — reverse-engineer-any-website design-taste skill, a different project from Leonxlnx's.
- Alternative Strix candidates (strixgov/strix, strixproject/Strix, mythicalsign/strix) if the security-tool identification proves wrong.
