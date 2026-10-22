# Phase 0 — Verification Report

**Session date:** 2026-08-09  
**Method:** Live web search + direct URL fetch for each item. No guesses presented as confirmed facts.  
**Key:** ✅ Confirmed exactly as given | ⚠️ Corrected (real name differs) | ❌ Not found / unverifiable | 🔶 Found but with important caveats

---

## Section A — "Already Confirmed Real" (existence re-checked, not re-researched in depth)

| Name As Given | Real Name / URL Found | Status |
|---|---|---|
| facebook/astryx | `facebook/astryx` — confirmed as Meta's open-source agent-ready React design system, released June 18 2026, 150+ components, MIT licensed, CLI confirmed (`@astryxdesign/cli`). The `--features agents` flag and auto-generated `AGENTS.md` are confirmed. **CORRECTION (Phase 8, 2026-08-11):** "ships MCP server" was WRONG — direct fetch of facebook/astryx found NO MCP package (packages/mcp-server and packages/mcp both 404; CLI README has zero MCP references). Astryx integration is bash calls only: `npx @astryxdesign/cli <command> --dense`. | ⚠️ Partially correct — MCP server claim was wrong |
| karpathy/llm-council | `github.com/karpathy/llm-council` — confirmed real, by Andrej Karpathy, intentionally unmaintained ("weekend hack"), OpenRouter-native. | ✅ Confirmed exactly as given |
| okjpg/llm-council (fork) | **Could not be verified.** No prominent public repository under `okjpg/llm-council` surfaced in multiple searches. The llm-council fork ecosystem is large but this specific handle did not appear. May be a voice-to-text distortion of a different username. | ❌ Not found — repo handle unverifiable |
| ngmeyer/council-review (fork) | `ngmeyer/council-review` — confirmed real **but now archived.** Standalone skill has been migrated into monorepo: `ngmeyer/skills`. The devil's-advocate pass and theatrical-consensus detector features are described in multiple sources. Active install path: `npx skills@latest add ngmeyer/skills`. | ⚠️ Real but archived — live version is now `ngmeyer/skills` |
| Graphify-Labs/graphify | `github.com/Graphify-Labs/graphify` — confirmed. Star count at research time: **104,000+** (you were given 76,000 — number has grown). OpenCode support explicitly documented. `/graphify` command confirmed. | ✅ Confirmed (star count higher than given) |

---

## Section B — "Now Verify These" (names given as-is, may be distorted)

| Name As Given | Real Name / URL Found | Status |
|---|---|---|
| "ruflo" | `ruvnet/ruflo` — confirmed real. **Formerly known as Claude Flow.** Open-source AI agent meta-harness by the `ruvnet` org. 60+ agent types, 300+ MCP tools, "AIDefence" security features, self-learning vector memory. Install: `npx ruflo@latest init wizard`. MCP server add: `claude mcp add ruflo -- npx ruflo@latest mcp start`. | ⚠️ Corrected: real repo is `ruvnet/ruflo`, formerly "Claude Flow" |
| "enilkowaski apple designs skill" | `emilkowalski/skills` — confirmed real. Maintainer is **Emil Kowalski** (voice-to-text garbled the name). Contains an `apple-design` skill distilling Apple WWDC design principles (Designing Fluid Interfaces, spring animations, physical motion). Install: `npx skills@latest add emilkowalski/skills`. Works with Claude Code, Cursor, Windsurf, Cline, and others. | ⚠️ Corrected: "enilkowaski" → **emilkowalski** (`emilkowalski/skills`) |
| "notebooklm py" | `teng-lin/notebooklm-py` — confirmed real. Unofficial Python async API client for Google's Gemini Notebook (formerly NotebookLM). Reverse-engineers internal RPCs. Supports bulk import of PDFs, URLs, YouTube videos, Google Drive files; triggers podcast/video/quiz/mind-map generation; extracts artifacts locally; includes a Skill for Claude Code. **Unofficial / uses undocumented APIs — breakage risk if Google updates backend.** | ⚠️ Corrected: full repo is `teng-lin/notebooklm-py`; unofficial, not an official Google package |
| "eve" by Vercel | `vercel/eve` — confirmed real. Released June 2026. Filesystem-first framework for building durable AI agents (Next.js conventions applied to agents). Defines agents via directory structure (`agent/instructions.md`, `agent/tools/`, etc.). Durable execution, human-in-the-loop, OpenTelemetry. Part of Vercel's "Agent Stack." Init: `npx eve@latest init my-agent`. | ✅ Confirmed exactly as given |
| "deepsec" by Vercel | `vercel/deepsec` — confirmed real. Released May 2026. AI-powered agentic security scanner (not a SaaS — self-hosted only). Stage-based pipeline: Scan (regex, free) → Process (LLM agents, paid) → Revalidate → Export. **Cost warning:** Scanning large repos with Opus-class models can cost hundreds to thousands of dollars. Static analysis only — not a runtime security tool. | ✅ Confirmed exactly as given |
| "claude-mem" | `thedotmack/claude-mem` — confirmed real. Persistent memory plugin: captures session activities, compresses to semantic summaries, injects into future sessions. Explicitly supports **OpenCode** (install: `npx claude-mem install --ide opencode`). Also works with Claude Code and others. | ✅ Confirmed exactly as given (maintainer: thedotmack) |
| "mvanhorn/last30days-skill" | `mvanhorn/last30days-skill` — **confirmed real, exact repo path correct.** Searches Reddit, X, YouTube, HN, TikTok, Polymarket, Bluesky, and open web; filters to last 30 days; scores by engagement; returns citation-backed synthesis. Install: `npx skills add mvanhorn/last30days-skill -g`. Compatible with Claude Code and OpenCode. | ✅ Confirmed exactly as given |

---

## Section C — walkinglabs/learn-harness-engineering (special URL verification)

| Claim | Finding | Status |
|---|---|---|
| Repo exists: `walkinglabs/learn-harness-engineering` | Confirmed real. Repo resolves and is publicly accessible. | ✅ Confirmed |
| URL `https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/resources/templates/index.md` resolves | Confirmed. URL was fetched directly via HTTP. The file exists and returns content. | ✅ URL confirmed live |
| File contains the "five layers" framework (task not clearly defined / insufficient context / misconfigured environment / missing verification / loss of state between sessions) | **DOES NOT MATCH.** The file at that exact URL is a **Template Guide** — it documents how to use AGENTS.md, init.sh, claude-progress.md, and feature_list.json templates. It does NOT contain the five-layer diagnostic framework as described to you. The five-layer framework **does exist elsewhere in the repo** (web searches confirm it), but the **layer names differ from what you were given.** The canonical layers in the repo are: **Instructions, State, Verification, Scope Boundaries, Lifecycle Handoff** — not the phrasing "task not clearly defined / insufficient context / misconfigured environment / missing verification / loss of state between sessions." That phrasing appears to be an imprecise paraphrase, not a direct quote. The specific URL given does not contain this framework at all. | ⚠️ URL exists and is live, but does NOT contain the five-layer content at that path. Framework is real but layer names differ from what you were given. |

---

## Section D — Loop-Engineering Related Repos (five repos, one-line differentiator each)

| Name As Given | Real Name / URL Found | Status | One-Line Differentiator |
|---|---|---|---|
| cobusgreyling/loop-engineering | `github.com/cobusgreyling/loop-engineering` | ✅ Confirmed | **The canonical patterns-and-CLI repo:** provides `loop-init`, `loop-audit`, `loop-doctor`, `loop-cost` CLI tools plus production patterns (daily-triage, PR monitor, dependency checker) for scaffolding autonomous agent loops across Grok, Claude Code, Codex, OpenCode, and GitHub Actions. |
| KanakMalpani/Loop-Engineering | Repo found is `KanakMalpani/LoopBench` — not "Loop-Engineering." MLPerf-style benchmark suite for evaluating loop engineering agents, not a framework or pattern library. | ⚠️ Corrected: real repo is `KanakMalpani/LoopBench` | **The benchmark/evaluation tool:** measures loop agent performance like MLPerf measures ML systems — for assessing and comparing loop quality, not for building loops. |
| Forward-Future/loopy | `github.com/Forward-Future/loopy` | ✅ Confirmed | **The loop-as-playbook skill:** installs as an agent skill, gives agents a live catalog of pre-designed feedback loops for iterative tasks (refactoring, test coverage, debugging), and runs them in bounded passes with receipts of actions and outcomes. |
| huangruiteng/loopx | `github.com/huangruiteng/loopx` | ✅ Confirmed | **The state kernel / local control plane:** a lightweight, agent-agnostic layer for long-running agent teams — manages durable goals, quota-aware auto-wake, executable todos, and evidence logs; focused on state persistence and handoff across turns and tools, not pattern libraries. |
| baidu-baige/LoongFlow | `github.com/baidu-baige/LoongFlow` | ✅ Confirmed | **The evolutionary algorithm framework:** implements a Plan-Execute-Summary (PES) cognitive loop with Evolutionary Algorithms (MAP-Elites, Boltzmann selection) so agents self-optimize prompts and logic across generations — purpose-built for math and ML tasks; has an arXiv paper (2512.24077). The most technically distinct of the five. |

---

## Section E — "Confirm Current State" Items

| Name As Given | Real Name / URL Found | Status | Notes |
|---|---|---|---|
| getshitdone / GSD | `gsd-build/get-shit-done` | ⚠️ Real but **SECURITY WARNING** | Confirmed real: spec-driven, multi-agent development framework addressing "context rot." **However: original repo was archived June 2026 after reports the creator "rug-pulled" with security concerns about deep shell permissions.** Community migrated to `open-gsd` governance and audited forks (e.g., `get-shit-done-redux`). Do not use the original package. |
| mattpocock/skills | `github.com/mattpocock/skills` | ✅ Confirmed, active | 200,000+ GitHub stars. Covers full SDLC: `/grill-with-docs`, `/tdd`, `/to-spec`, `/to-tickets`, `/design-an-interface`, `/improve-codebase-architecture`. Install: `npx skills@latest add mattpocock/skills`. Agent-agnostic; works with Claude Code, Cursor, OpenCode, and others. |
| obra/superpowers | `github.com/obra/superpowers` | ✅ Confirmed, active | Jesse Vincent's agentic skills framework. Model-agnostic, plain-Markdown skills. Explicitly confirmed OpenCode support (via `.opencode/skills/` directory). Also available via Claude plugin marketplace. Skills auto-trigger by context, no manual invocation required. |
| garrytan/gstack | `github.com/garrytan/gstack` | ✅ Confirmed, active | By Y Combinator president Garry Tan. ~23 startup-role skills (CEO, EM, Designer, QA, etc.). Think→Plan→Build→Review→Test→Ship→Reflect workflow. Notable: maintains a persistent headless Chromium daemon for real browser QA testing via `/qa`. Built for Claude Code primarily but compatible with other SKILL.md-supporting agents. |
| public-apis/public-apis | `github.com/public-apis/public-apis` | ✅ Confirmed — yes, the well-known free public API reference list | Community-curated list of free public APIs organized by category (hundreds of thousands of stars). Not an installable skill — agents use it as a reference document to discover available APIs when building features. In this setup it would most likely be referenced via a graphify-indexed local clone or via an MCP web-fetch. |
| asgeirtj/system_prompts_leaks | `github.com/asgeirtj/system_prompts_leaks` | ✅ Confirmed | Repo confirmed live. **`claude-fable-5.md` EXISTS** — it is at path `Anthropic/claude-fable-5.md` (inside an `Anthropic/` subfolder, not at repo root). Note: the folder appears in sources as uppercase `Anthropic`. Prompts are extracted not hacked; unofficial. |
| Anthropic's official Claude Cookbooks | `github.com/anthropics/claude-cookbooks` | ✅ Confirmed | Exact org name is `anthropics` (with an "s"). Also browsable at `platform.claude.com/cookbook`. Notebooks and recipes for building Claude applications. |
| n8n | n8n (workflow automation tool, n8n.io) | ✅ Confirmed active | n8n is confirmed active and expanding in 2026 (AI Agent node focus). **Re: OpenCode integration specifically:** No native, documented integration path between n8n and OpenCode was found. Community nodes exist but are unofficial. The two tools are **essentially separate ecosystems** for now — n8n handles workflow orchestration, OpenCode handles code agent tasks, and connecting them requires custom wiring with no official template support. For a solo developer/student workflow, adding n8n adds substantial overhead with unclear payoff. |

---

## Summary of Key Corrections and Flags (10 items)

1. **`okjpg/llm-council`** — could not be verified. Likely a voice-to-text error. **Skip** until you can provide the exact URL.
2. **`ngmeyer/council-review`** — real but **archived**. The maintained version is now `ngmeyer/skills`.
3. **"ruflo"** → actual repo is `ruvnet/ruflo` (formerly Claude Flow, by ruvnet org).
4. **"enilkowaski"** → actual maintainer is **emilkowalski** (`emilkowalski/skills`).
5. **`teng-lin/notebooklm-py`** — unofficial tool using undocumented Google APIs; breakage risk on Google backend updates.
6. **walkinglabs five-layers URL** — URL resolves and is real, but the **specific file at that URL does not contain the five-layer framework**. Framework exists elsewhere in repo with different layer names (Instructions / State / Verification / Scope Boundaries / Lifecycle Handoff, not the phrasing you were given).
7. **`KanakMalpani/Loop-Engineering`** → actual repo is `KanakMalpani/LoopBench` (a benchmark tool, not a framework).
8. **GSD / getshitdone** — real but original repo **archived with security concerns**; use only audited community forks.
9. **`asgeirtj/system_prompts_leaks` — `claude-fable-5.md`** file exists, but it is in the `Anthropic/` subfolder, not at repo root. Your description ("at anthropic/claude-fable-5.md") is directionally correct, path case may vary.
10. **n8n ↔ OpenCode** — essentially **unconnected ecosystems**; no official integration path exists as of this research.
