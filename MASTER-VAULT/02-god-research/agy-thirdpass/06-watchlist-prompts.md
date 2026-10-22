model-used: gemini-3.8-flash-high (sonnet-quota-fallback)

# 06 — Watchlist Investigation & System Prompt Archives (Metadata Only)

> **Document ID:** `06-watchlist-prompts.md`  
> **Verification Date:** 2026-10-09  
> **Auditor / Mode:** Read-Only Researcher (Antigravity)  
> **Mandate:** Strictly METADATA ONLY — Zero prompt bodies reproduced. No installs, no command execution beyond read-only queries, no bypass attempts, no credentials.

---

## Table of Contents

1. [Investigation of 23 Watchlist Items](#1-investigation-of-23-watchlist-items)
   - [Summary Comparison Matrix](#summary-comparison-matrix)
   - [Detailed Item Dossiers (1–23)](#detailed-item-dossiers-123)
2. [System Prompt Archives Metadata & Provenance](#2-system-prompt-archives-metadata--provenance)
   - [Primary Archive: asgeirtj/system_prompts_leaks](#21-primary-archive-asgeirtjsystem_prompts_leaks)
   - [Comparative Archive: LouisShark/chatgpt_system_prompt](#22-comparative-archive-louissharkchatgpt_system_prompt)
   - [Comparative Archive: Piebald-AI/claude-code-system-prompts](#23-comparative-archive-piebald-aiclaude-code-system-prompts)
   - [Official References & Verified In-Repo Instructions](#24-official-references--verified-in-repo-instructions)
3. [Methodology & Authenticity Boundaries](#3-methodology--authenticity-boundaries)
4. [Summary Counts & Disposition](#4-summary-counts--disposition)

---

## 1. Investigation of 23 Watchlist Items

### Summary Comparison Matrix

| # | Original Watchlist Name | Status | Canonical Match / Disambiguation | Key Architecture & Verification Evidence |
|---|---|---|---|---|
| 1 | `OpenViking` | **RESOLVED** | [`volcengine/OpenViking`](https://github.com/volcengine/OpenViking) | ByteDance Volcengine context database for AI agents (`viking://` virtual filesystem, L0/L1/L2 tiered loading, `ov` CLI, AGPLv3). |
| 2 | `PizzaBox AWS` | **UNRESOLVED (Provisional)** | [`pizza-bot-app/pizza-bot`](https://github.com/pizza-bot-app/pizza-bot) *(Candidate)* | Conflation of Amazon "Two-Pizza Team" rule + 1U rack-mount ("pizza-box") hardware. Closest agent candidate is `pizza-bot-app/pizza-bot` by AWS engineers Joseph Dolivo & Igor Fil. |
| 3 | `Scrapling Krim Shoair` | **RESOLVED** | [`D4Vinci/Scrapling`](https://github.com/D4Vinci/Scrapling) | Authored by Krim Shoair (@D4Vinci). High-performance Python adaptive web scraping and anti-bot bypass library. |
| 4 | `ChatDev 2.0/devAll` | **RESOLVED** | [`OpenBMB/ChatDev`](https://github.com/OpenBMB/ChatDev) | OpenBMB multi-agent framework. `v2.0.0` (DevAll) switched `main` to a zero-code orchestration platform with cyclic CADET graphs and Vue3 console. |
| 5 | `Munder Difflin variants` | **RESOLVED** | [`HarnessMD/munder-difflin`](https://github.com/HarnessMD/munder-difflin) | Formerly `chaitanyagiri/munder-difflin` (HTTP 301). Local-first multi-agent harness parodying *The Office*, orchestrating local CLI agents via "Michael" lead agent. |
| 6 | `Taste skill` | **RESOLVED** | [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) | Created by Leon Lin (`tasteskill.dev`). Anti-slop design framework for AI coding assistants via modular `SKILL.md`. |
| 7 | `Frontend design skill` | **RESOLVED** | [`anthropics/skills`](https://github.com/anthropics/skills) (`skills/frontend-design`) | Official Anthropic reference skill bundle in the `anthropics/skills` repository establishing frontend aesthetic rules and responsive layouts. |
| 8 | `Backend design skill` | **RESOLVED (Convention)** | `skills/backend-design` / `docs/backend-design.md` | Absent from official `anthropics/skills` tree. Exists as a community skill module (`vadimcomanescu/codex-skills`, `xenitV1/claude-code-maestro`) and architecture file convention. |
| 9 | `public-apis/public-apis` | **RESOLVED** | [`public-apis/public-apis`](https://github.com/public-apis/public-apis) | Canonical community directory of 1,400+ free public developer APIs categorized by Auth, HTTPS, and CORS. |
| 10 | `Agent Skills standard` | **RESOLVED** | [`agentskills/agentskills`](https://github.com/agentskills/agentskills) / [`agentskills.io`](https://agentskills.io) | Open standard originating from Anthropic specifying `SKILL.md` YAML frontmatter (`name`, `description`) and progressive disclosure directories (`scripts/`, `references/`, `assets/`). |
| 11 | `Astryx facebook/astryx (CLI vs MCP nuance)` | **RESOLVED** | [`facebook/astryx`](https://github.com/facebook/astryx) | Meta design system (React 19, StyleX). **Nuance:** Local toolchain is strictly CLI-only (`@astryxdesign/cli`); MCP server exists exclusively as remote hosted Streamable HTTP endpoint (`/mcp` on docsite). |
| 12 | `vercel/deepsec (check 404 vs vercel-labs/deepsec)` | **RESOLVED** | [`vercel-labs/deepsec`](https://github.com/vercel-labs/deepsec) | `vercel/deepsec` returns **HTTP 404**. Active repository is verified at `vercel-labs/deepsec` (**HTTP 200**), an agentic security auditing harness (`npx deepsec init`). |
| 13 | `affaan-m/ECC` | **RESOLVED** | [`affaan-m/ECC`](https://github.com/affaan-m/ECC) | Enterprise Agent Harness Performance Optimization System. Packages 68 agents, 293 skills, AgentShield scanner for Claude Code, Cursor, Codex. |
| 14 | `ruvnet/ruflo` | **RESOLVED** | [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) | Formerly Claude Flow. Meta-harness for Claude Code and Codex with swarm coordination, persistent memory, and MCP server integration (npm `ruflo`). |
| 15 | `anthropics/claude-cookbooks` | **RESOLVED** | [`anthropics/claude-cookbooks`](https://github.com/anthropics/claude-cookbooks) | Anthropic official recipe repository. Note: `anthropics/claude-cookbook` returns HTTP 301 redirecting to plural `claude-cookbooks`. |
| 16 | `Designs variants` | **RESOLVED (Pattern)** | Claude Design Variant Exploration (`claude.ai/design`) | Visual exploration pattern (`design-shotgun`) prompting agents to render 3–6 distinct aesthetic/layout variations side-by-side prior to implementation. |
| 17 | `Firecrawl` | **RESOLVED** | [`firecrawl/firecrawl`](https://github.com/firecrawl/firecrawl) | Web crawling engine for LLMs (markdown/screenshot scraping). Legacy `mendableai/firecrawl` returns HTTP 301 redirecting to dedicated org. |
| 18 | `vercel/eve` | **RESOLVED** | [`vercel/eve`](https://github.com/vercel/eve) | Vercel filesystem-first durable agent framework (`agent/instructions.md`, tools, skills, channels, `npx eve init`). |
| 19 | `Strix variants` | **RESOLVED** | [`usestrix/strix`](https://github.com/usestrix/strix) | Autonomous AI penetration testing tool (PyPI `strix-agent`, Docker PoC sandbox). Disambiguated from ASUS ROG hardware tools. |
| 20 | `DESIGN.md convention` | **RESOLVED** | Standardized `DESIGN.md` Specification | Machine- and human-readable design token specification (`google-labs-code/design.md`) pairing YAML frontmatter tokens with Markdown rationale. |
| 21 | `awesome-claude-skills compare` | **PARTIAL (Multi-org)** | [`ComposioHQ`](https://github.com/ComposioHQ/awesome-claude-skills) & [`travisvn`](https://github.com/travisvn/awesome-claude-skills) | Multiple community registries. `travisvn` is earliest; `ComposioHQ` is largest commercial list; `karanb192` focuses on dev workflows; `VoltAgent` is multi-agent. |
| 22 | `anthropics/skills official` | **RESOLVED** | [`anthropics/skills`](https://github.com/anthropics/skills) | Anthropic public repository implementing the Agent Skills standard with 19 reference skill folders (`frontend-design`, `docx`, `pdf`, `xlsx`, `canvas-design`). |
| 23 | `NotebookLM skill` | **RESOLVED** | [`PleasePrompto/notebooklm-skill`](https://github.com/PleasePrompto/notebooklm-skill) | Community skill and MCP implementations enabling coding agents (Claude Code, Cursor) to query Google NotebookLM via automated sessions. |

---

### Detailed Item Dossiers (1–23)

#### 1. OpenViking
- **Original String:** `OpenViking`
- **Canonical Match:** `https://github.com/volcengine/OpenViking`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Repository hosted under ByteDance Volcengine org (`volcengine/OpenViking`).
  - Architecture: Designed as a "Context Database for AI Agents" implementing an agent-native virtual filesystem (`viking://`).
  - Key Components: Tiered hierarchical context loading (L0 abstract summary, L1 operational overview, L2 complete source detail), session-level persistence, and the `ov` CLI (`ov status`, `ov add-resource`, `ov ls`, `ov find`, `ov grep`).
  - Licensing: AGPL-3.0. Official site: `https://openviking.ai`.

#### 2. PizzaBox AWS
- **Original String:** `PizzaBox AWS`
- **Canonical Match:** `UNRESOLVED (Provisional Candidate: https://github.com/pizza-bot-app/pizza-bot)`
- **Status:** `UNRESOLVED (Provisional)`
- **Evidence & Disambiguation Nuance:**
  - No repository named `PizzaBox` or `pizzabox` exists under the official `aws` or `aws-samples` GitHub organizations.
  - Two distinct conflation vectors identified:
    1. **Agent Tool Candidate:** `pizza-bot-app/pizza-bot` — A local-first desktop inbox for long-running autonomous AI agents authored by AWS engineers Joseph Dolivo and Igor Fil, published on the AWS Open Source Blog (2026-09-10). It supports Amazon Bedrock, LangGraph, and DeepAgents. The project name derives from Jeff Bezos's "Two-Pizza Team" rule.
    2. **Hardware Conflation:** "Pizza-box" is standard data-center industry slang for 1U rack-mount server chassis, frequently used by AWS infrastructure teams to describe single-server edge devices such as the 1U AWS Outposts server.
  - Verdict: Original string preserved verbatim. Neither entity is officially titled `PizzaBox AWS`.

#### 3. Scrapling Krim Shoair
- **Original String:** `Scrapling Krim Shoair`
- **Canonical Match:** `https://github.com/D4Vinci/Scrapling`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Repository: `D4Vinci/Scrapling` (HTTP 200).
  - Author Linkage: Authored and maintained by Karim Shoair (GitHub username `@D4Vinci`, confirmed via profile title "D4Vinci (Karim shoair)").
  - Architecture: An adaptive Python web scraping framework engineered to withstand DOM structure changes and anti-bot fingerprinting. Unifies single HTTP fetches, dynamic browser rendering, and full crawler pipelines with automated selector re-mapping.

#### 4. ChatDev 2.0 / devAll
- **Original String:** `ChatDev 2.0/devAll`
- **Canonical Match:** `https://github.com/OpenBMB/ChatDev`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Maintained by OpenBMB (`OpenBMB/ChatDev`).
  - Version 2.0 Evolution: In release `v2.0.0`, the repository's default `main` branch transitioned from the legacy ChatDev 1.0 waterfall roleplay model (CEO, CTO, Programmer) to **DevAll** ("Dev All through LLM-powered Multi-Agent Collaboration").
  - Architecture: A zero-code multi-agent orchestration platform driven by the declarative CADET cycle-aware execution graph, offering a Vue 3 interactive visual canvas and Python SDK. Legacy ChatDev 1.x moved to branch `chatdev1.0`.

#### 5. Munder Difflin variants
- **Original String:** `Munder Difflin variants`
- **Canonical Match:** `https://github.com/HarnessMD/munder-difflin`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Formerly `chaitanyagiri/munder-difflin` (verified HTTP 301 Permanent Redirect to `HarnessMD/munder-difflin`).
  - Architecture: An open-source, local-first multi-agent development harness. Parodies the Dunder Mifflin paper company from *The Office*.
  - Execution Model: A lead agent named "Michael" manages a team of local CLI coding agents (Claude Code, Copilot, Codex, Gemini CLI) operating within local mailboxes, terminal sandboxes, and a shared blackboard memory layer.

#### 6. Taste skill
- **Original String:** `Taste skill`
- **Canonical Match:** `https://github.com/Leonxlnx/taste-skill`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Authored by Leon Lin (`Leonxlnx/taste-skill`, homepage `https://tasteskill.dev`). Verified HTTP 200.
  - Purpose: Known as the "anti-slop" design framework for AI coding assistants.
  - Implementation: Modular `SKILL.md` compliant with the Agent Skills standard. Injects strict visual constraints, typographic hierarchy, responsive spacing ratios, and motion curves into Claude Code and Cursor prompts to prevent boilerplate, generic UI generation.

#### 7. Frontend design skill
- **Original String:** `Frontend design skill`
- **Canonical Match:** `https://github.com/anthropics/skills/tree/main/skills/frontend-design`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Official first-party skill bundle maintained within Anthropic's reference repository (`anthropics/skills`).
  - Structure: Directory contains `SKILL.md` along with guidelines covering visual weight, responsive layouts, color contrast standards, and accessibility primitives. Used by Claude Code and Claude.ai web environments.

#### 8. Backend design skill
- **Original String:** `Backend design skill`
- **Canonical Match:** `Convention / Ecosystem Module (e.g., vadimcomanescu/codex-skills, xenitV1/claude-code-maestro)`
- **Status:** `RESOLVED (Convention)`
- **Evidence & Architecture:**
  - Not present in Anthropic's official `anthropics/skills` directory (which focuses on frontend, canvas, documents, and testing).
  - Ecosystem Presence: Exists as a widely recognized community skill specification module (`skills/backend-design/SKILL.md`) and architectural contract file convention (`docs/backend-design.md`). Standardizes API contract planning (OpenAPI/gRPC), schema data modeling, idempotent state handling, and error boundaries for coding agents.

#### 9. public-apis/public-apis
- **Original String:** `public-apis/public-apis`
- **Canonical Match:** `https://github.com/public-apis/public-apis`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Canonical repository created in March 2016, maintained under the `public-apis` organization.
  - Characteristics: Over 486k GitHub stars; indexes 1,400+ free public developer APIs across 50+ categories with strict metadata schemas: API Name, Description, Authentication Type (API Key, OAuth, None), HTTPS support, and CORS availability.

#### 10. Agent Skills standard
- **Original String:** `Agent Skills standard`
- **Canonical Match:** `https://github.com/agentskills/agentskills` / `https://agentskills.io`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Open specification originally designed by Anthropic and released as an open community standard (`agentskills.io/specification`).
  - Standard Specification: Defines a modular directory standard centered on `SKILL.md`. Requires YAML frontmatter (`name`, `description`) for minimal context token overhead during initial tool matching, followed by Markdown instructions and progressive disclosure asset folders (`scripts/`, `references/`, `assets/`). Supported across Claude Code, Codex CLI, Cursor, and Gemini CLI.

#### 11. Astryx facebook/astryx (CLI vs MCP nuance)
- **Original String:** `Astryx facebook/astryx (CLI vs MCP nuance)`
- **Canonical Match:** `https://github.com/facebook/astryx`
- **Status:** `RESOLVED`
- **Evidence & The CLI vs. MCP Nuance:**
  - Repository: Meta Open Source design system (`facebook/astryx`, `astryx.atmeta.com`) built on React 19 and StyleX with 150+ components.
  - **The Architectural Nuance Disambiguated:**
    1. **Local Distributable Surface (CLI-Only):** The locally installed npm package `@astryxdesign/cli` and the root `packages/cli` tree are **strictly CLI-only**. There is no local `@astryxdesign/mcp` package, no `astryx mcp` command in the binary, and no local stdio daemon. Local agent interaction is conducted via `npx @astryxdesign/cli <command> --dense` or `manifest --json`.
    2. **Remote Hosted Endpoint Surface (MCP Server):** An official Model Context Protocol server exists **exclusively as a remote Streamable HTTP web service** hosted within the docsite web application (`apps/docsite/src/app/mcp/route.ts` using `mcp-handler` and `zod`) at `https://astryx.atmeta.com/mcp`. It exposes two tools to remote agents: `search(query, type?, limit?)` and `get(name, type)`.
  - Conclusion: Both claims in prior audits were correct at their respective scopes: locally it is CLI-only; hosted remotely it offers an MCP HTTP endpoint.

#### 12. vercel/deepsec (check 404 vs vercel-labs/deepsec)
- **Original String:** `vercel/deepsec (check 404 vs vercel-labs/deepsec)`
- **Canonical Match:** `https://github.com/vercel-labs/deepsec`
- **Status:** `RESOLVED`
- **Evidence & HTTP Status Verification:**
  - `https://github.com/vercel/deepsec` returns **HTTP/2 404 Not Found** (tested live 2026-10-09).
  - `https://github.com/vercel-labs/deepsec` returns **HTTP/2 200 OK** (tested live 2026-10-09).
  - Metadata: Description: *"Deepsec is a security harness for finding vulnerabilities in your codebase powered by coding agents"*. Initialized and executed via `npx deepsec init`.
  - Resolution: The canonical repository resides under experimental lab organization `vercel-labs`, not the primary `vercel` production org.

#### 13. affaan-m/ECC
- **Original String:** `affaan-m/ECC`
- **Canonical Match:** `https://github.com/affaan-m/ECC`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Repository: `affaan-m/ECC` (Enterprise Code / Agent Harness Performance Optimization System).
  - Architecture: Provides 68 specialized agent roles, 293 modular skills, 94 command shims, and the AgentShield security auditing harness. Compatible with Claude Code (`/plugin install ecc@ecc`), Codex, Cursor, Opencode, and Antigravity.

#### 14. ruvnet/ruflo
- **Original String:** `ruvnet/ruflo`
- **Canonical Match:** `https://github.com/ruvnet/ruflo`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Repository: `ruvnet/ruflo` (formerly known as Claude Flow; README: "Claude Flow is now Ruflo").
  - Architecture: Multi-agent meta-harness for Claude Code and Codex ("Agent = Model + Harness"). Implements parallel worker swarms, shared persistent memory, 35 modular plugins, and an extensive MCP server architecture exposing 320+ tools alongside a 45-command CLI (npm package `ruflo`).

#### 15. anthropics/claude-cookbooks
- **Original String:** `anthropics/claude-cookbooks`
- **Canonical Match:** `https://github.com/anthropics/claude-cookbooks`
- **Status:** `RESOLVED`
- **Evidence & Redirect Nuance:**
  - Canonical URL is the **plural form**: `https://github.com/anthropics/claude-cookbooks` (HTTP/2 200).
  - The legacy singular URL `https://github.com/anthropics/claude-cookbook` returns **HTTP/2 301 Moved Permanently**, redirecting to the plural repo.
  - Subfolder `skills/`: Hosts the official Claude Skills Cookbook (`skills/notebooks/03_skills_custom_development.ipynb`, custom skill templates, and built-in skill documentation for `docx`, `pdf`, `pptx`, `xlsx`).

#### 16. Designs variants
- **Original String:** `Designs variants`
- **Canonical Match:** `Claude Design Exploration Pattern (claude.ai/design)`
- **Status:** `RESOLVED (Pattern)`
- **Evidence & Architecture:**
  - Not a distinct standalone Git repository; refers to the **Multi-Variant Visual Exploration Pattern** codified within Claude Design (`claude.ai/design`) and related community skills (`design-shotgun`).
  - Methodology: Instructs generative coding agents to formulate 3 to 6 distinct layout, typographic, and palette options in parallel, allowing users to compare contrasting UI directions prior to selecting an implementation branch.

#### 17. Firecrawl
- **Original String:** `Firecrawl`
- **Canonical Match:** `https://github.com/firecrawl/firecrawl`
- **Status:** `RESOLVED`
- **Evidence & Redirect Nuance:**
  - Canonical URL: `https://github.com/firecrawl/firecrawl` (HTTP/2 200).
  - Legacy URL `https://github.com/mendableai/firecrawl` returns **HTTP/2 301 Moved Permanently** redirecting to the dedicated `firecrawl` organization.
  - Architecture: Open-source web scraping and crawling engine built specifically for LLM context ingestion (converts complex JS-rendered web pages into clean Markdown, structured JSON, or screenshots via `/v2/scrape` and `/v2/crawl`).

#### 18. vercel/eve
- **Original String:** `vercel/eve`
- **Canonical Match:** `https://github.com/vercel/eve`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Hosted at `vercel/eve` (HTTP/2 200). Homepage: `https://eve.dev`.
  - Architecture: An open-source, filesystem-first durable AI agent framework. Structure maps agent behavior directly to directory trees: `agent/instructions.md` (normative guidelines), `agent/tools/` (TypeScript function schemas), `agent/skills/`, `agent/channels/` (GitHub webhook/mention bindings), and `agent/schedules/`. Designed for long-running execution on Vercel serverless/edge infrastructure.

#### 19. Strix variants
- **Original String:** `Strix variants`
- **Canonical Match:** `https://github.com/usestrix/strix`
- **Status:** `RESOLVED`
- **Evidence & Disambiguation:**
  - Canonical Repository: `usestrix/strix` (HTTP/2 200), distributed via PyPI as `strix-agent`.
  - Architecture: An open-source autonomous multi-agent penetration testing harness. Coordinates LLM reasoning agents to identify, probe, and validate security vulnerabilities, verifying exploits with reproducible Proof-of-Concepts (PoCs) inside isolated Docker sandboxes.
  - Disambiguation: Explicitly distinguished from ASUS ROG Strix motherboard/GPU lighting and fan control utilities.

#### 20. DESIGN.md convention
- **Original String:** `DESIGN.md convention`
- **Canonical Match:** `Standardized DESIGN.md Specification (google-labs-code/design.md)`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Specification repository: `google-labs-code/design.md` (`docs/spec.md`).
  - Architecture: A repository-level design contract pairing machine-readable YAML frontmatter (design tokens for colors, typography scales, border radii, spacing) with human-readable Markdown body sections (layout hierarchy, elevation, component guidelines, UX anti-patterns). Complements `AGENTS.md` and `CLAUDE.md` to prevent visual styling drift across AI agent coding sessions.

#### 21. awesome-claude-skills compare
- **Original String:** `awesome-claude-skills compare`
- **Canonical Match:** `Multi-Registry Comparison: ComposioHQ vs. travisvn vs. karanb192 vs. VoltAgent`
- **Status:** `PARTIAL (Multi-org)`
- **Comparative Taxonomy:**
  1. [`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills): Earliest chronological list (created 2025-10-16, ~15.3k stars); focused on Claude Code workflows and official Anthropic cookbook links.
  2. [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills): Largest commercial directory (created 2025-10-17, ~64k–74k stars); indexes 1,000+ SaaS tool integrations and automated action connectors across Claude, Codex, Cursor, and Antigravity.
  3. [`karanb192/awesome-claude-skills`](https://github.com/karanb192/awesome-claude-skills): Developer productivity focus (50+ verified skills; TDD, Git workflows, debugging) with clear installation documentation.
  4. [`BehiSecc/awesome-claude-skills`](https://github.com/BehiSecc/awesome-claude-skills): Categorized taxonomy spanning documents, security testing, data analysis, and media.
  5. [`VoltAgent/awesome-agent-skills`](https://github.com/VoltAgent/awesome-agent-skills): Cross-platform multi-agent meta-registry (1,000+ skills).
  - Conclusion: No single canonical exists under the bare name; org qualification (`ComposioHQ`, `travisvn`, etc.) is required.

#### 22. anthropics/skills official
- **Original String:** `anthropics/skills official`
- **Canonical Match:** `https://github.com/anthropics/skills`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Anthropic's official open-source repository implementing the `agentskills.io` standard.
  - Directory Structure: Contains 19 reference skill packages including `frontend-design`, `canvas-design`, `theme-factory`, `web-artifacts-builder`, `webapp-testing`, `claude-api`, `algorithmic-art`, `skill-creator`, and proprietary enterprise document processing skills (`docx`, `pdf`, `pptx`, `xlsx`). Installed via the Anthropic Skills API or Claude Code plugin marketplace (`claude plugin marketplace add anthropics/skills`).

#### 23. NotebookLM skill
- **Original String:** `NotebookLM skill`
- **Canonical Match:** `https://github.com/PleasePrompto/notebooklm-skill`
- **Status:** `RESOLVED`
- **Evidence & Architecture:**
  - Canonical Repository: `PleasePrompto/notebooklm-skill` (HTTP/2 200). Adjacent community variants: `sanjay3290/notebooklm-skill`, `claude-world/notebooklm-skill`.
  - Architecture: Bridges AI coding assistants (Claude Code, Cursor, Gemini CLI) directly to Google NotebookLM notebooks. Operates through headless browser automation and persistent session tokens, enabling agents to query private source notebooks and retrieve grounded, citation-backed context from Gemini models without hallucination.

---

## 2. System Prompt Archives Metadata & Provenance

> [!IMPORTANT]
> **Strict Metadata Policy:** In accordance with research security guidelines, this section contains exclusively file lists, directory paths, commit timestamps, file counts, and provenance classifications. **Zero prompt text, instructions, or system prompt bodies are reproduced.**

### 2.1 Primary Archive: `asgeirtj/system_prompts_leaks`

- **Repository URL:** `https://github.com/asgeirtj/system_prompts_leaks`
- **Description:** *"Documented system prompts from Anthropic - Claude Fable 5.1, Opus 5.5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly."*
- **Creation Date:** 2025-05-03T02:43:56Z
- **Last Push / Update:** 2026-10-09T16:34:23Z
- **License:** Creative Commons Zero v1.0 Universal (CC0-1.0)
- **Repository Volume:** 1,264 tracked files across 17 top-level directories
- **Metrics:** ~69.2k stars | ~11.3k forks | 851+ commits

#### Directory Structure & File Counts Census

| Directory Path | File Count | Representative Filenames (Metadata Only) |
|---|---|---|
| `Anthropic/` | 577 | `claude-sonnet-5.5.md`, `claude-opus-5.5.md`, `claude-haiku-5.5.md`, `claude-fable-5.1.md`<br>Subdirectories: `claude-code/` (455 files), `official/` (42 files), `claude-design/` (32 files), `claude-cowork/` (5 files), `old/` (10 files), `raw/` (6 files), root level (27 files). |
| `Meta/` | 474 | `muse-spark-1.3-muse-code.md`<br>Subdirectories: `muse-agent/` (389 files: skills, workflows, system), `muse-code/` (83 files), root level (2 files). |
| `OpenAI/` | 124 | `gpt-5.5-thinking.md`, `gpt-5.5-pro-api.md`, `gpt-5.6-sol.md`<br>Subdirectories: `Codex/` (35 files), `dots/` (32 files: dreamer, voice, tools), `Old/` (15 files), `API/` (8 files), root level (34 files). |
| `Google/` | 24 | `antigravity-cli.md`, `gemini-3.8-flash.md`, `gemini-3.7-flash.md`, `gemini-3.5-flash.md`, `gemini-3.1-pro.md`, `gemini-cli.md`, `gemini-in-chrome.md`, `notebooklm-chat.md`, `jules.md`. |
| `Misc/` | 23 | Independent engine and third-party agent wrapper files. |
| `xAI/` | 16 | `grok-4.7-cli.md`, `grok-4.7.md`, `grok-4.5.md`, `grok-4.md`, `grok-bot.md`, `grok-build.md`, `grok-expert.md`. |
| `Perplexity/` | 5 | `comet-browser-assistant.md`, `deep-research.md`, `perplexity-ai.md`, `perplexity-computer.md`, `voice-assistant.md`. |
| `Microsoft/` | 5 | Copilot, Copilot Studio, and enterprise assistant files. |
| `Kimi/` | 2 | Moonshot AI chat and reasoning models. |
| `Mistral/` | 2 | Le Chat and Mistral Large assistant files. |
| `Qwen/` | 2 | `qwen3.6-plus.md`, `qwen3.8-max.md`. |
| `Cursor/` | 1 | `Cursor/cursor.md`. |
| `DeepSeek/` | 1 | `DeepSeek/deepseek-chat.md`. |
| `GLM/` | 1 | Zhipu AI GLM assistant file. |
| `Notion/` | 1 | Notion AI assistant file. |
| `Pi/` | 1 | `Pi/instructions.md`. |
| Root / Meta | 5 | `README.md`, `LICENSE`, `.gitattributes`, `.github/FUNDING.yml`, `.github/latitude-dark.png`. |

#### Chronological Commit Activity Sample (October 2026)

- `2d9b8f2` (2026-10-09): Update Claude Code system prompts (2.1.295)
- `e31ec21` (2026-10-08): Update claude-code skills
- `dd45aa5` (2026-10-07): Update claude-code skills
- `a7b30ef` (2026-10-07): Add Claude Haiku 5.5 system prompt (claude.ai)
- `84dc028` (2026-10-07): Update Claude Code system prompts (2.1.293)
- `9991a25` (2026-10-07): Add Haiku 5.5 system prompt (Claude Code)
- `209ea2b` (2026-10-07): Add official Claude Haiku 5.5 system prompt (October 7, 2026)
- `db3b2ac` (2026-10-07): Add Claude Code plan mode system message
- `11f19dd` (2026-10-07): Update Claude Design system prompt and starter components
- `f015440` (2026-10-06): Update claude-sonnet-5.5.md

#### Provenance & Dual Classification

- **Overall Provenance:** `alleged-leak / unverified` (Dual Provenance Structure):
  1. **Alleged-Leak / Community-Extracted (Vast Majority):** Entries across `OpenAI/`, `Google/`, `xAI/`, `Meta/`, and `Anthropic/claude-code/` are third-party extractions derived from jailbreak prompts, prompt injection probes, memory dumps, or binary unpacking. They lack cryptographic vendor signatures and may represent reconstructed, partial, or hallucinated representations.
  2. **Official Mirror Sub-Archive (`Anthropic/official/`):** The 42 files within `Anthropic/official/` mirror Anthropic's publicly published system prompt changelogs (spanning releases from 2024-07-12 to 2026-10-07) and model constitutions (v1 2023-05-09, v2 2026-01-20).
- **Press & Industry Mentions:**
  - *The Washington Post* (2026-05-11): "See the hidden rules behind AI. Then use them to rewrite this article."
  - *CEPS AI World* (2026-07-10): "System prompts and what they tell us about the chat before the chat."
  - *Simon Willison* (2026-08-20): Noted as the most comprehensive community archive of extracted agent instructions.

---

### 2.2 Comparative Archive: `LouisShark/chatgpt_system_prompt`

- **Repository URL:** `https://github.com/LouisShark/chatgpt_system_prompt`
- **Description:** *"A collection of GPT system prompts and various prompt injection/leaking knowledge."*
- **Creation Date:** 2023-11-01T12:35:05Z
- **Last Push / Update:** 2026-10-08T11:26:51Z
- **Metrics:** 10,800+ stars | Size: ~30.5 MB
- **Directory Structure:**
  - `prompts/official-product/` (Extracted prompts from consumer AI web applications)
  - `prompts/gpts/` (Custom GPT instruction extractions)
  - `prompts/opensource-prj/` (Prompts from open-source agent projects)
  - Documentation: `GETTING_STARTED.md`, `RESOURCES.md`, `SECURITY.md`, `TOC.md`
- **Provenance Classification:** `alleged-leak / unverified` (Crowdsourced prompt injections and reverse engineering).

---

### 2.3 Comparative Archive: `Piebald-AI/claude-code-system-prompts`

- **Repository URL:** `https://github.com/Piebald-AI/claude-code-system-prompts`
- **Description:** *"All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version."*
- **Creation Date:** 2025-11-18T21:26:33Z
- **Last Push / Update:** 2026-10-08T21:58:06Z
- **Metrics:** 12,800+ stars | Size: ~6.5 MB
- **Directory Structure:**
  - `system-prompts/` (900+ files detailing discrete sub-agent states, lifecycle hooks, and tool wrappers across version increments)
  - `tools/` (Built-in tool metadata definitions and schemas)
- **Provenance Classification:** `alleged-leak / unverified` (Derived from binary analysis and runtime extraction without vendor endorsement).

---

### 2.4 Official References & Verified In-Repo Instructions

For authoritative, verified agent design patterns, the following official sources serve as ground truth (metadata cataloged):

1. **Official Vendor Pedagogical Guides & Cookbooks:**
   - Anthropic: `anthropics/claude-cookbooks` (`skills/notebooks/03_skills_custom_development.ipynb`)
   - Anthropic Prompt Engineering Interactive Tutorial: `https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview`
   - OpenAI Prompt Engineering Guide: `https://platform.openai.com/docs/guides/prompt-engineering`
   - Google Gemini Prompting Strategies: `https://ai.google.dev/gemini-api/docs/prompting-strategies`
2. **Official Specification & Reference Repositories:**
   - Agent Skills Standard: `https://github.com/agentskills/agentskills` (`spec/agent-skills-spec.md`)
   - Anthropic Reference Skills: `https://github.com/anthropics/skills` (`template/SKILL.md`)
3. **In-Repo Project Instructions (Official Developer Artifacts):**
   - Astryx: `https://github.com/facebook/astryx` (`AGENTS.md`, `CLAUDE.md`)
   - Eve: `https://github.com/vercel/eve` (`agent/instructions.md`, `agent/tools/`, `agent/skills/`)
   - ECC: `https://github.com/affaan-m/ECC` (`AGENTS.md`, `CLAUDE.md`, `rules/`, `skills/`)
   - Ruflo: `https://github.com/ruvnet/ruflo` (`USERGUIDE.md`, `docs/STATUS.md`)

---

## 3. Methodology & Authenticity Boundaries

1. **Strict Metadata Compliance:** No system prompts, secret tokens, prompt injection payloads, or proprietary agent instructions are reproduced in this document. All references are restricted to paths, repository metadata, commit timestamps, and architectural roles.
2. **Read-Only Verification:** All checks conducted via read-only HTTP headers, public Git metadata, and repository file trees. No packages were installed, no untrusted code was executed, and no authentication bypasses were attempted.
3. **Authenticity Disclaimer for Alleged-Leak Archives:** Community prompt leak repositories (`asgeirtj`, `LouisShark`, `Piebald-AI`) must be treated as **unverified third-party claims**. Model architectures, prompt prefixes, and agent rules contained within them may be outdated, injected, synthetically generated, or altered. Developers must rely on official vendor documentation for production agent constraints.

---

## 4. Summary Counts & Disposition

- **Watchlist Items Investigated:** 23
  - **Resolved (Canonical Match Verified):** 20 (OpenViking, Scrapling Krim Shoair, ChatDev 2.0/devAll, Munder Difflin variants, Taste skill, Frontend design skill, Backend design skill [convention], public-apis/public-apis, Agent Skills standard, Astryx facebook/astryx [CLI vs MCP nuance], vercel/deepsec [404 confirmed; vercel-labs 200], affaan-m/ECC, ruvnet/ruflo, anthropics/claude-cookbooks, Designs variants [pattern], Firecrawl, vercel/eve, Strix variants, DESIGN.md convention, anthropics/skills official, NotebookLM skill)
  - **Partially Resolved (Multi-Registry Org Qualifier Required):** 1 (awesome-claude-skills compare)
  - **Unresolved / Provisional Candidate:** 1 (PizzaBox AWS — conflation preserved verbatim)
  - **Total Watchlist Addressed:** 23 / 23
- **System Prompt Archives Cataloged (Metadata Only):** 3 primary comparative archives (`asgeirtj/system_prompts_leaks`, `LouisShark/chatgpt_system_prompt`, `Piebald-AI/claude-code-system-prompts`) + 4 official vendor in-repo sources.
- **Files Tracked in Primary Archive (`asgeirtj`):** 1,264 files across 17 vendor directories.
- **Prompt Bodies Reproduced:** 0 (100% Policy Compliant).

---

DONE + counts: 23 watchlist items investigated (21 resolved/pattern/convention, 1 multi-org partial, 1 provisional unresolved), 3 prompt archives cataloged, 1,264 files surveyed in primary archive, 0 prompt bodies reproduced.
