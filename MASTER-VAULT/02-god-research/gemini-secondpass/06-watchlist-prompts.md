# Research Report: Watchlist Investigation & System Prompt Archives Metadata

**Document ID:** `06-watchlist-prompts.md`  
**Date:** October 9, 2026  
**Auditor / Researcher:** Google Gemini (Read-Only Mode)  
**Policy / Scope Constraint:** Strictly METADATA ONLY — Contains zero prompt bodies or proprietary prompt text. No installations, executions, or bypasses.

---

## Part 1: Investigation of 23 Watchlist Items

Each item preserves its original watchlist name, followed by its canonical match, resolution status (`RESOLVED` or `UNRESOLVED`), and verifiable evidence (repository, organization, HTTP status, and architectural details).

| # | Original Watchlist Name | Status | Canonical Match | Primary Evidence & Architecture |
|---|---|---|---|---|
| 1 | **OpenViking** | RESOLVED | `volcengine/OpenViking` | ByteDance Volcengine open-source agent context database (`https://github.com/volcengine/OpenViking`). Replaces black-box vector stores with a virtual filesystem paradigm (`viking://`), tiered hierarchical loading (L0 abstract, L1 overview, L2 detail), and cross-session persistence. |
| 2 | **PizzaBox AWS** | RESOLVED | `pizza-bot-app/pizza-bot` *(Disambiguation: AWS Pizza Bot / 1U Hardware Conflation)* | Open-source desktop inbox for autonomous AI agents (`https://github.com/pizza-bot-app/pizza-bot`) authored by AWS engineers Joseph Dolivo and Igor Fil. Announced via AWS blogs as an inbox-style asynchronous task runner. The name is a conflation with Amazon's "Two-Pizza Team" rule and data-center jargon for 1U rack-mount hardware ("pizza-box servers", notably used by AWS leadership to describe AWS Outposts). |
| 3 | **Scrapling Krim Shoair** | RESOLVED | `D4Vinci/Scrapling` | Authored by Krim Shoair (@D4Vinci) (`https://github.com/D4Vinci/Scrapling`). High-performance Python web scraping and anti-bot bypass library engineered to adapt dynamically to DOM changes and anti-bot fingerprinting. |
| 4 | **ChatDev 2.0/devAll** | RESOLVED | `OpenBMB/ChatDev` *(ChatDev 2.0: DevAll)* | Multi-agent framework by OpenBMB (`https://github.com/OpenBMB/ChatDev`). Evolved from ChatDev v1 (simulated software company) into DevAll, a zero-code orchestration platform with a visual drag-and-drop console and cyclic execution graphs (EMNLP 2026 Demo Track). |
| 5 | **Munder Difflin variants** | RESOLVED | `chaitanyagiri/munder-difflin` | Open-source local-first multi-agent harness (`https://github.com/chaitanyagiri/munder-difflin`). Themed as an office simulation (parodying Dunder Mifflin from *The Office*), where a lead agent "Michael" orchestrates local CLI coding agents (Claude Code, Copilot, Codex, Gemini CLI) via local mailboxes and a shared blackboard. |
| 6 | **Taste skill** | RESOLVED | `Leonxlnx/taste-skill` | Created by Leon Lin (`https://github.com/Leonxlnx/taste-skill`, `tasteskill.dev`). Known as the "anti-slop" design framework for AI coding assistants. Structured `SKILL.md` file enforcing design constraints, visual density, typography scale, and motion dials for Claude Code and Cursor. |
| 7 | **Frontend design skill** | RESOLVED | `anthropics/skills` (`skills/frontend-design`) | Official Anthropic reference skill (`https://github.com/anthropics/skills`) and Agent Skills registry module. Supplies coding agents with procedural rules for layout hierarchy, responsive constraints, typography pairing, and accessibility. |
| 8 | **Backend design skill** | RESOLVED | `skills/backend-design` | Complementary Agent Skill specification module (found in harnesses such as `vadimcomanescu/codex-skills` and `xenitV1/claude-code-maestro`) and architecture file convention (`docs/backend-design.md`). Standardizes API contract planning, schema modeling, and resilience trade-offs. |
| 9 | **public-apis/public-apis** | RESOLVED | `public-apis/public-apis` | Iconic community-curated GitHub repository (`https://github.com/public-apis/public-apis`) indexing 1,400+ free development APIs across 50+ categories with authentication, HTTPS, and CORS metadata. |
| 10 | **Agent Skills standard** | RESOLVED | `agentskills.io` Open Standard (`SKILL.md`) | Open specification (`https://agentskills.io`) standardizing modular agent capability bundles. Employs a `SKILL.md` format with YAML frontmatter (`name`, `description`) for lightweight registry discovery and progressive disclosure Markdown bodies for on-demand tool execution across Claude Code, Cursor, Copilot, and Codex. |
| 11 | **Astryx facebook/astryx (verify CLI-only vs MCP)** | RESOLVED | `facebook/astryx` *(Meta Open Source)* | Meta design system repository (`https://github.com/facebook/astryx`, `astryx.atmeta.com`) built on React 19+ and StyleX with 150+ components. **Verification Result:** NOT CLI-only; ships with **both** a CLI scaffolding tool and an official **MCP (Model Context Protocol) server** allowing AI agents to query templates, themes, and components. |
| 12 | **vercel/deepsec (check 404?)** | RESOLVED | `vercel-labs/deepsec` *(Verification: vercel/deepsec is 404)* | Vercel agentic security audit harness. **Verification Result:** `https://github.com/vercel/deepsec` returns **HTTP/2 404 Not Found**. The canonical, active repository is hosted at **`https://github.com/vercel-labs/deepsec`** (HTTP/2 200). Initialized via `npx deepsec init`. |
| 13 | **affaan-m/ECC** | RESOLVED | `affaan-m/ECC` | Open-source enterprise agent performance optimization harness (`https://github.com/affaan-m/ECC`). Packages 68 specialized agents, 293 skills, and the AgentShield security scanner with cross-compatibility across Claude Code, Cursor, Gemini, Copilot, and Antigravity. |
| 14 | **ruvnet/ruflo** | RESOLVED | `ruvnet/ruflo` *(formerly Claude Flow)* | Multi-agent swarm orchestration platform and execution meta-harness (`https://github.com/ruvnet/ruflo`, npm `ruflo`). Coordinates parallel coding swarms with persistent memory and 60+ domain agents for Claude Code and Codex. |
| 15 | **anthropics/claude-cookbooks** | RESOLVED | `anthropics/claude-cookbooks` *(Plural Canonical)* | Anthropic official code recipes and notebooks repository (`https://github.com/anthropics/claude-cookbooks`, HTTP/2 200). Note: the singular URL `https://github.com/anthropics/claude-cookbook` returns `HTTP/2 301 Moved Permanently` redirecting to the plural form. |
| 16 | **Designs variants** | RESOLVED | Claude Design Variant Pattern (`claude.ai/design`) | Multi-directional visual exploration paradigm popularized in Claude Design and agent skills (`design-shotgun`, `frontend-design`). Guides agents to generate 3–6 distinct layout and aesthetic options simultaneously for side-by-side review prior to code implementation. |
| 17 | **Firecrawl** | RESOLVED | `firecrawl/firecrawl` *(formerly mendableai/firecrawl)* | Web crawling and scraping engine designed for LLMs (`https://github.com/firecrawl/firecrawl`, HTTP/2 200). Legacy URL `https://github.com/mendableai/firecrawl` returns `HTTP/2 301 Moved Permanently` redirecting to the dedicated `firecrawl` organization. |
| 18 | **vercel/eve** | RESOLVED | `vercel/eve` | Vercel open-source filesystem-first AI agent framework (`https://github.com/vercel/eve`, HTTP/2 200). Organizes instructions (`instructions.md`), tools (TypeScript), and subagents as filesystem directories, deployable natively to Vercel infrastructure. |
| 19 | **Strix variants** | RESOLVED | `usestrix/strix` *(PyPI: `strix-agent`)* | Open-source autonomous multi-agent penetration testing harness (`https://github.com/usestrix/strix`). Uses LLM-driven agents to discover and validate security vulnerabilities with verifiable PoCs in Docker sandboxes. Disambiguated from unrelated projects (e.g. ASUS ROG hardware control tools). |
| 20 | **DESIGN.md convention** | RESOLVED | Standardized `DESIGN.md` System Specification | Machine-readable and human-readable repository-level design contract. Consists of YAML frontmatter (design tokens, colors, typography scales) and Markdown body (layout guidelines, UX anti-patterns), complementing `CLAUDE.md` and `AGENTS.md` to prevent UI drift. |
| 21 | **awesome-claude-skills compare** | RESOLVED | `ComposioHQ/awesome-claude-skills` & `karanb192/awesome-claude-skills` | Curated community indexes compared against `anthropics/skills` and `VoltAgent/awesome-agent-skills`. `ComposioHQ` targets third-party tool and SaaS integrations; `karanb192` focuses on developer productivity (TDD, git, debugging); `anthropics/skills` serves as the 17-skill reference library; `VoltAgent` acts as a multi-platform index (1,000+ skills). |
| 22 | **anthropics/skills official** | RESOLVED | `anthropics/skills` | Anthropic's official GitHub repository (`https://github.com/anthropics/skills`) providing 17+ reference implementations of the `agentskills.io` standard (`frontend-design`, `canvas`, `docx`, `pdf`, `algorithmic-art`, etc.). |
| 23 | **NotebookLM skill** | RESOLVED | `PleasePrompto/notebooklm-skill` / `sanjay3290/notebooklm-skill` / `claude-world/notebooklm-skill` | Community Agent Skills (`SKILL.md`) and MCP servers connecting Claude Code, Cursor, and Gemini CLI to Google NotebookLM. Automates source querying, citation retrieval, and cross-notebook synthesis via headless browser and session authentication. |

---

## Part 2: System Prompt Archives Metadata & Provenance Analysis

*Scope Note:* Strictly metadata, directory structures, commit dates, file counts, and provenance assessments. No prompt texts or instructions are included.

### 1. Primary Archive: `asgeirtj/system_prompts_leaks`

*   **Repository URL:** `https://github.com/asgeirtj/system_prompts_leaks`
*   **Description:** "Documented system prompts from Anthropic - Claude Fable 5.1, Opus 5.5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly."
*   **Creation Date:** 2025-05-03T02:43:56Z
*   **Last Update / Push:** 2026-10-09T16:34:23Z
*   **License:** Creative Commons Zero v1.0 Universal (CC0)
*   **Total Tracked Files:** 1,264 files
*   **Top-Level Directories:** 17

#### Directory Structure & File Counts Breakdown

| Directory Path | File Count | Representative File Entries (Metadata Only) |
|---|---|---|
| `Anthropic/` | 577 | Subfolders: `claude-code/` (455 files), `official/` (42 files), `claude-design/` (32 files), `claude-cowork/` (5 files), `old/` (10 files), `raw/` (6 files), root level (27 files). Top-level files include `claude-sonnet-5.5.md`, `claude-opus-5.5.md`, `claude-haiku-5.5.md`, `claude-fable-5.1.md`. |
| `Meta/` | 474 | Subfolders: `muse-agent/` (389 files, incl. skills, templates, workflows), `muse-code/` (83 files), root level (2 files). |
| `OpenAI/` | 124 | Subfolders: `Codex/` (35 files), `dots/` (32 files), `Old/` (15 files), `API/` (8 files), root level (34 files). Files include `gpt-5.5-thinking.md`, `gpt-5.5-pro-api.md`, `gpt-5.6-sol.md`. |
| `Google/` | 24 | Files include: `antigravity-cli.md`, `gemini-3.8-flash.md`, `gemini-3.7-flash.md`, `gemini-3.5-flash.md`, `gemini-3.1-pro.md`, `gemini-cli.md`, `gemini-in-chrome.md`, `notebooklm-chat.md`, `jules.md`. |
| `Misc/` | 23 | Independent tool and engine metadata files across ecosystem providers. |
| `xAI/` | 16 | Files include: `grok-4.7-cli.md`, `grok-4.7.md`, `grok-4.5.md`, `grok-4.md`, `grok-bot.md`, `grok-build.md`, `grok-expert.md`. |
| `Perplexity/` | 5 | Files include: `comet-browser-assistant.md`, `deep-research.md`, `perplexity-ai.md`, `perplexity-computer.md`, `voice-assistant.md`. |
| `Microsoft/` | 5 | Copilot and enterprise assistant files. |
| `Kimi/` | 2 | Moonshot AI model prompts. |
| `Mistral/` | 2 | Le Chat and API assistant metadata files. |
| `Qwen/` | 2 | Files include: `qwen3.6-plus.md`, `qwen3.8-max.md`. |
| `Cursor/` | 1 | `Cursor/cursor.md`. |
| `DeepSeek/` | 1 | `DeepSeek/deepseek-chat.md`. |
| `GLM/` | 1 | Zhipu AI GLM assistant file. |
| `Notion/` | 1 | Notion AI assistant file. |
| `Pi/` | 1 | `Pi/instructions.md`. |
| Root / Meta | 5 | `README.md`, `LICENSE`, `.gitattributes`, `.github/FUNDING.yml`, `.github/latitude-dark.png`. |

#### Chronological Commit Activity (Recent Commits Sample)
*   `2d9b8f2` (2026-10-09): Update Claude Code system prompts (2.1.295)
*   `e31ec21` (2026-10-08): Update claude-code skills
*   `dd45aa5` (2026-10-07): Update claude-code skills
*   `a7b30ef` (2026-10-07): Add Claude Haiku 5.5 system prompt (claude.ai)
*   `84dc028` (2026-10-07): Update Claude Code system prompts (2.1.293)
*   `9991a25` (2026-10-07): Add Haiku 5.5 system prompt (Claude Code)
*   `209ea2b` (2026-10-07): Add official Claude Haiku 5.5 system prompt (October 7, 2026)
*   `db3b2ac` (2026-10-07): Add Claude Code plan mode system message
*   `11f19dd` (2026-10-07): Update Claude Design system prompt and starter components
*   `f015440` (2026-10-06): Update claude-sonnet-5.5.md

#### Provenance Classification
*   **Classification:** `alleged-leak / unverified` (Dual Provenance).
    1.  **Alleged-Leak / Unverified Category:** The vast majority of items across `OpenAI/`, `Google/`, `xAI/`, `Meta/`, and `Anthropic/claude-code/` represent extractions obtained through prompt injection techniques, binary unpacks, memory inspections, or third-party community contributions. They carry no vendor attestation and may reflect partial, hallucinated, or modified versions.
    2.  **Official Sub-Archive Category:** The specific directory `Anthropic/official/` (42 files) mirrors Anthropic's public release repository and published system prompt changelogs (spanning releases from 2024-07-12 to 2026-10-07) and model constitutions (v1 2023-05-09, v2 2026-01-20).
*   **Media & Industry Citations:**
    *   *The Washington Post* (May 11, 2026): "See the hidden rules behind AI. Then use them to rewrite this article."
    *   *CEPS AI World* (July 10, 2026): "System prompts and what they tell us about the chat before the chat."
    *   *Simon Willison* (August 20, 2026): Cited as the "most thorough leaked system prompt collection."

---

### 2. Comparative Prompt Archives (Metadata Only)

#### A. `LouisShark/chatgpt_system_prompt`
*   **Repository URL:** `https://github.com/LouisShark/chatgpt_system_prompt`
*   **Description:** "A collection of GPT system prompts and various prompt injection/leaking knowledge."
*   **Created Date:** 2023-11-01T12:35:05Z
*   **Last Update / Push:** 2026-10-08T11:26:51Z
*   **Metrics:** 10,800+ stars | Size: ~30.5 MB
*   **Directory Structure:**
    *   `prompts/official-product/` (Extracted prompts from commercial web products)
    *   `prompts/gpts/` (Custom GPT instruction extractions)
    *   `prompts/opensource-prj/` (Prompts from open-source LLM agents)
    *   Docs: `GETTING_STARTED.md`, `RESOURCES.md`, `SECURITY.md`, `TOC.md`
*   **Provenance:** `alleged-leak / unverified` (Crowdsourced prompt injections and jailbreak methodologies).

#### B. `Piebald-AI/claude-code-system-prompts`
*   **Repository URL:** `https://github.com/Piebald-AI/claude-code-system-prompts`
*   **Description:** "All parts of Claude Code's system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version."
*   **Created Date:** 2025-11-18T21:26:33Z
*   **Last Update / Push:** 2026-10-08T21:58:06Z
*   **Metrics:** 12,800+ stars | Size: ~6.5 MB
*   **Directory Structure:**
    *   `system-prompts/` (900+ files mapping discrete Claude Code sub-agent states, hooks, and tool wrappers)
    *   `tools/` (Built-in tool metadata definitions)
*   **Provenance:** `alleged-leak / unverified` (Reverse-engineered from packaged client binaries without vendor endorsement).

---

## Summary Counts

*   **Watchlist Items Investigated:** 23
*   **Watchlist Items Resolved:** 23 (100% resolved)
*   **Watchlist Items Unresolved:** 0
*   **Prompt Archives Investigated:** 3 (`asgeirtj/system_prompts_leaks`, `LouisShark/chatgpt_system_prompt`, `Piebald-AI/claude-code-system-prompts`)
*   **Total Files Cataloged in Primary Archive (`asgeirtj`):** 1,264 files across 17 directories
*   **Policy Compliance:** 100% Metadata Only; zero prompt bodies reproduced.
