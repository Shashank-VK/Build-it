# Phase 5 — Remaining Named Resources (Final Phase)

> Research completed: 2026-08-09  
> Scope: Full per-item analysis of all items confirmed real in Phase 0 using the standardized 5-point template.

---

## 1. Graphify-Labs/graphify

- **What it actually does:** Codebase-to-knowledge-graph tool/skill (104,000+ stars). Converts code, docs, SQL schemas, configs, images, and PDFs into an interactive, queryable local knowledge graph via AST parsing without requiring a vector database.
- **Exact OpenCode support type:** **Native** (ships an explicit `/graphify` command and native OpenCode skill integration).
- **When to use it:** At the start of onboarding a new or complex codebase to map dependency structures, visual relationships, and data flows.
- **When NOT to use it:** On small 1-3 file repos or simple isolated scripts where AST parsing overhead adds unnecessary complexity.
- **Final verdict:** **MUST-HAVE / TOP PICK.** Essential for codebase comprehension in OpenCode.

---

## 2. ruvnet/ruflo (formerly "Claude Flow")

- **What it actually does:** High-star (67k+ stars) AI agent meta-harness by ruvnet org. Orchestrates multi-agent swarms (hierarchical Queen/Worker topologies), includes 300+ MCP tools, adaptive HNSW vector memory, self-learning neural patterns (SONA), and multi-provider routing (Claude, GPT, Gemini, Ollama).
- **Exact OpenCode support type:** **Open standard** (operates via MCP server bridge: `claude mcp add ruflo -- npx ruflo@latest mcp start` or local MCP config in `opencode.json`).
- **When to use it:** Large-scale enterprise monorepo refactoring or complex multi-phase swarm tasks requiring strict agent governance and multi-agent coordination.
- **When NOT to use it:** Standard single-developer tasks, quick bug fixes, or lightweight feature additions where swarm coordination introduces extreme latency and complexity.
- **Final verdict:** **POWER-USER TOOL.** Extremely capable swarm engine, but too heavy for everyday solo developer/student workflows.

---

## 3. emilkowalski/skills (corrected from "enilkowaski")

- **What it actually does:** Collection of UI/animation skills created by Emil Kowalski. Distills Apple WWDC design principles, fluid interface mechanics, spring physics, and micro-interaction standards into machine-readable `SKILL.md` rules.
- **Exact OpenCode support type:** **Open standard** (installs via `npx skills@latest add emilkowalski/skills` into `.agents/skills/` or `.opencode/skills/`).
- **When to use it:** Frontend tasks involving animations, gesture handling, fluid UI layouts, and micro-interactions.
- **When NOT to use it:** Backend development, CLI tools, API design, or non-visual coding tasks.
- **Final verdict:** **TOP PICK FOR FRONTEND ANIMATION.** Excellent supplement to Astryx and shadcn/ui.

---

## 4. teng-lin/notebooklm-py (corrected from "notebooklm py")

- **What it actually does:** Unofficial Python async API client for Google NotebookLM (Gemini Notebook). Reverse-engineers internal RPCs to import PDFs, web URLs, YouTube videos, and Google Drive files; triggers audio podcast, video, and mind-map generations; extracts artifacts locally.
- **Exact OpenCode support type:** **Documented adapter/port** (ships a Claude Code / OpenCode skill wrapper for python invocation).
- **When to use it:** Deep research synthesis phase when gathering unstructured multi-format research assets (videos, PDFs, articles) before coding starts.
- **When NOT to use it:** Production codebases or critical CI/CD pipelines — it relies on private, undocumented Google RPCs that can break without notice.
- **Final verdict:** **USE WITH CAUTION.** Valuable for personal research gathering, but high breakage risk due to un-official RPC API dependency.

---

## 5. vercel/eve

- **What it actually does:** Open-source filesystem-first framework by Vercel (released June 2026) for building durable, resumable AI agents. Features filesystem-defined agents (`agent/instructions.md`, `agent/tools/`), human-in-the-loop pausing, Vercel MicroVM sandboxing, and OpenTelemetry tracing.
- **Exact OpenCode support type:** **Reference-only / Parallel ecosystem.** Eve is an agent *building* framework, whereas OpenCode is an agentic coding *assistant*.
- **When to use it:** When you are building a custom production AI agent service to host on Vercel or node infrastructure.
- **When NOT to use it:** As an extension or plugin inside OpenCode — Eve is an architecture for building agents, not a skill for OpenCode to consume.
- **Final verdict:** **WRONG LAYER FOR THIS SETUP.** Excellent framework for building SaaS agents, but irrelevant as a tool *inside* OpenCode.

---

## 6. vercel/deepsec

- **What it actually does:** Open-source agentic security scanner by Vercel (released May 2026). Multi-stage pipeline: Regex Scan $\rightarrow$ Agent Deep Investigation $\rightarrow$ Revalidation $\rightarrow$ Git Contributor Enrichment. Local CLI workspace tool (`.deepsec/`).
- **Exact OpenCode support type:** **Documented adapter/port** (can be invoked as a local CLI tool or via community `deepsec-skill`).
- **When to use it:** Pre-release security audits of critical authentication, payment, or data-handling code.
- **When NOT to use it:** Routine commits or small code edits — running Opus-class agentic security scans on large repos incurs massive API costs (hundreds to thousands of dollars).
- **Final verdict:** **SPECIALIZED AUDIT TOOL.** Highly effective for periodic security revalidation, but prohibitively expensive for continuous everyday use.

---

## 7. thedotmack/claude-mem

- **What it actually does:** Persistent cross-session semantic memory plugin. Automatically captures session actions, compresses key decisions into semantic summaries, and injects relevant historical context into future sessions.
- **Exact OpenCode support type:** **Native** (explicit installation flag: `npx claude-mem install --ide opencode`).
- **When to use it:** Long-running projects spanning multiple days or weeks where cross-session continuity is critical.
- **When NOT to use it:** One-off scratch scripts or isolated single-file tasks where long-term memory adds prompt overhead.
- **Final verdict:** **TOP MEMORY PICK.** Along with `opencode-mem`, it is the cleanest persistent memory solution for OpenCode.

---

## 8. mvanhorn/last30days-skill

- **What it actually does:** Agent skill that queries Reddit, X, YouTube, Hacker News, TikTok, Polymarket, Bluesky, and the open web, filtering specifically to the last 30 days of data and generating citation-backed synthesis.
- **Exact OpenCode support type:** **Open standard** (installs via `npx skills add mvanhorn/last30days-skill -g`).
- **When to use it:** Researching cutting-edge 2026 tech developments, fresh library releases, or breaking API changes that occurred after model knowledge cutoff dates.
- **When NOT to use it:** Looking up stable, long-established language documentation or internal project rules.
- **Final verdict:** **HIGH VALUE RESEARCH SKILL.** Crucial tool for avoiding stale assumptions on rapidly evolving 2026 web frameworks.

---

## 9. cobusgreyling/loop-engineering

- **What it actually does:** Canonical CLI toolset (`loop-init`, `loop-audit`, `loop-doctor`, `loop-cost`) and pattern library for scaffolding autonomous agent loops across GitHub Actions, OpenCode, and Claude Code.
- **Exact OpenCode support type:** **Open standard** (CLI tool + SKILL.md templates).
- **When to use it:** Setting up structured, repeatable background agent loops (e.g., daily dependency audits, PR triage).
- **When NOT to use it:** Interactive single-user pair programming sessions in the terminal.
- **Final verdict:** **GREAT FOR DEVOPS LOOPS.** Recommended if building automated background maintenance tasks.

---

## 10. KanakMalpani/LoopBench (corrected from "Loop-Engineering")

- **What it actually does:** MLPerf-style benchmark evaluation suite for measuring and comparing the performance of autonomous loop agents.
- **Exact OpenCode support type:** **Reference-only.** Benchmarking tool, not a developer workflow utility.
- **When to use it:** When researching or evaluating which agent harness performs best on standardized loop benchmarks.
- **When NOT to use it:** During active application development or coding workflows.
- **Final verdict:** **EVALUATION ONLY.** Useful research reference, not a development tool.

---

## 11. Forward-Future/loopy

- **What it actually does:** Agent skill that provides a live catalog of pre-designed feedback loops (refactoring loop, test coverage loop, debugging loop) that agents execute in bounded passes with action receipts.
- **Exact OpenCode support type:** **Open standard** (SKILL.md format).
- **When to use it:** Enforcing bounded iterative passes on tasks like getting test coverage to 90% or refactoring a module.
- **When NOT to use it:** Open-ended architectural design or creative exploratory coding.
- **Final verdict:** **RECOMMENDED SKILL.** Great for structured, bounded quality passes.

---

## 12. huangruiteng/loopx

- **What it actually does:** Lightweight, agent-agnostic local control plane / state kernel. Manages durable goals, quota-aware auto-wake, executable TODO lists, and evidence logs across long-running agent tasks.
- **Exact OpenCode support type:** **Open standard** (local daemon / CLI kernel).
- **When to use it:** Long-running multi-turn agent tasks where session state persistence and auto-resume across model crashes are needed.
- **When NOT to use it:** Simple short-lived terminal prompts.
- **Final verdict:** **SOLID INFRASTRUCTURE.** Great alternative to heavy frameworks for session resilience.

---

## 13. baidu-baige/LoongFlow

- **What it actually does:** Evolutionary algorithm framework implementing a Plan-Execute-Summary (PES) cognitive loop with MAP-Elites and Boltzmann selection to self-optimize agent prompts and logic across generations (arXiv 2512.24077).
- **Exact OpenCode support type:** **Reference-only / Specialized framework.**
- **When to use it:** Complex mathematical optimization, algorithmic research, or prompt-evolution experiments.
- **When NOT to use it:** General full-stack web development or standard software engineering tasks.
- **Final verdict:** **SPECIALIZED RESEARCH TOOL.** High academic interest, low relevance for web development setups.

---

## 14. gsd-build/get-shit-done (GSD) / `open-gsd`

- **What it actually does:** Spec-driven, multi-agent development framework designed to eliminate "context rot" via rigorous spec definition and task chunking.
- **Exact OpenCode support type:** **Documented adapter/port** (via `open-gsd` community audited forks).
- **CRITICAL SECURITY WARNING:** The original `gsd-build/get-shit-done` repository was archived in June 2026 due to critical security concerns regarding deep shell permissions. Do NOT install the original package. The active maintained fork is confirmed at **`open-gsd/gsd-core`** (`https://github.com/open-gsd/gsd-core`, page title: *"Git. Ship. Done - Core"*) — live URL verified 2026-08-09.
- **When to use it:** Spec-first multi-agent development on complex multi-file features.
- **When NOT to use it:** Quick one-line fixes; never use the original un-audited repository.
- **Final verdict:** **USE COMMUNITY AUDITED FORK ONLY (`open-gsd`).** Concept is strong, but original repo is unsafe.

---

## 15. mattpocock/skills

- **What it actually does:** 200,000+ star collection of SDLC skills by Matt Pocock (`/grill-with-docs`, `/tdd`, `/to-spec`, `/to-tickets`, `/design-an-interface`, `/improve-codebase-architecture`).
- **Exact OpenCode support type:** **Open standard** (installs via `npx skills@latest add mattpocock/skills`).
- **When to use it:** Core software engineering phases (TDD, spec extraction, interface design, architecture review).
- **When NOT to use it:** None — highly versatile across almost all coding workflows.
- **Final verdict:** **ESSENTIAL SKILL PACK / TOP PICK.** One of the highest-quality skill collections in the ecosystem.

---

## 16. obra/superpowers

- **What it actually does:** Jesse Vincent's flagship agentic skills framework (211,000+ stars). 14 composable skills forming a complete software development methodology (TDD, architectural verification, systematic debugging).
- **Exact OpenCode support type:** **Native** (explicit OpenCode install instructions via `.opencode/skills/`).
- **When to use it:** Always-on foundational discipline for any serious software development session.
- **When NOT to use it:** Quick exploratory scratchpad coding where strict methodology feels overly rigid.
- **Final verdict:** **FOUNDATIONAL MUST-HAVE.** The gold standard for agent discipline.

---

## 17. garrytan/gstack

- **What it actually does:** Y Combinator president Garry Tan's agent startup role skills (~23 roles: CEO, EM, Designer, QA, etc.). Features a persistent headless Chromium daemon for real browser QA testing via `/qa`.
- **Exact OpenCode support type:** **Open standard** (SKILL.md format + local browser daemon).
- **When to use it:** End-to-end feature development where automated browser testing and multi-role perspective reviews are needed.
- **When NOT to use it:** Lightweight backend logic edits where browser QA is irrelevant.
- **Final verdict:** **HIGH-QUALITY SUITE.** `/qa` browser testing skill alone makes it worth having.

---

## 18. public-apis/public-apis

- **What it actually does:** Massive community index of free public APIs organized by category.
- **Exact OpenCode support type:** **Reference-only.**
- **Concrete Usage in OpenCode Setup:** Clone locally into a reference directory and index it with `graphify` or query it via a web fetch MCP tool. When the agent is tasked with building a feature (e.g. "add weather data or currency conversion"), the agent queries the local public-apis index to find valid, keyless endpoints without hallucinating API URLs.
- **When to use it:** During ideation or feature design when selecting third-party data integrations.
- **When NOT to use it:** Building internal microservices or proprietary enterprise APIs.
- **Final verdict:** **EXCELLENT REFERENCE GROUNDING.** Grounding contract to prevent fake API endpoint hallucinations.

---

## 19. asgeirtj/system_prompts_leaks (specifically `Anthropic/claude-fable-5.md`)

- **What it actually does:** Repository archiving extracted system prompts from major AI providers. `Anthropic/claude-fable-5.md` contains the system prompt for Claude models.
- **Exact OpenCode support type:** **Reference-only.**
- **When to use it:** Studying prompt engineering techniques, anti-hallucination guardrails, and formatting instructions used by frontier models.
- **When NOT to use it:** As an executable tool in production pipelines.
- **Final verdict:** **STUDY MATERIAL.** Excellent for crafting custom agent prompts based on industry-leading system prompts.

---

## 20. anthropics/claude-cookbooks

- **What it actually does:** Official Anthropic repository (`anthropics/claude-cookbooks`) containing code recipes, notebooks, and architectural patterns for building with Claude.
- **Exact OpenCode support type:** **Reference-only.**
- **When to use it:** Referencing official Anthropic implementation patterns for tool use, vision, structured output, and context management.
- **When NOT to use it:** Direct agent installation (it is a notebook/code example repo).
- **Final verdict:** **OFFICIAL REFERENCE STANDBY.** Essential learning reference.

---

## Final Phase 5 Summary

All 20 verified named resources evaluated with full 5-point breakdowns. No unconfirmed items included.

**Saved to `research/05-remaining-resources.md`.**
