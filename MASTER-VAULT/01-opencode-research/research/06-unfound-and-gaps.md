# OpenCode Research — Unfound Items & Ecosystem Gaps Summary

> Session completed: 2026-08-09  
> Purpose: Explicit record of items that could not be verified, repos that failed to resolve as named, and structural gaps in the ecosystem.

---

## 1. Unverifiable / Distorted Resources (Items Not Found)

| Name As Given | Search Status | Finding & Resolution |
|---|---|---|
| `okjpg/llm-council` | ❌ Not Found | No public GitHub repository exists under this handle. The `llm-council` ecosystem has many forks, but this specific username/repo does not exist as named. Use `ngmeyer/skills` or the native `deliberation` plugin instead. |
| `KanakMalpani/Loop-Engineering` | ✅ Confirmed (corrected from prior error) | Repo exists at `https://github.com/KanakMalpani/Loop-Engineering` — confirmed live. Prior research incorrectly flagged this as non-existent and confused it with `KanakMalpani/LoopBench`. **Both repos exist and are separate.** Loop-Engineering is the framework; LoopBench is the benchmark suite. |
| `ngmeyer/council-review` | ✅ Confirmed Live (corrected from prior error) | `https://github.com/ngmeyer/council-review` is **live and active**, not archived. Page title confirmed: *"Claude Code skill: Run decisions, code, and plans through a council of 5 AI advisors with anonymous peer review."* Prior research was incorrect. `ngmeyer/skills` is the monorepo/consolidated version; `council-review` is the standalone skill — **both exist in parallel.** |
| `gsd-build/get-shit-done` | ⚠️ Archived / Security Warning | Original repo archived June 2026 after security concerns over deep shell permissions. Do NOT use original package. Active maintained fork confirmed at `https://github.com/open-gsd/gsd-core` (page title: *"Git. Ship. Done - Core"*). |
| `walkinglabs` 5-layers URL | ⚠️ Path Misalignment | URL `https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/resources/templates/index.md` is live, but the 5-layer framework is not at that path. The framework exists elsewhere in the repo with different layer names (*Instructions, State, Verification, Scope Boundaries, Lifecycle Handoff*). |

---

## 2. Identified Ecosystem Gaps (What Doesn't Exist Yet)

### Gap 1: No Turnkey Backend Equivalent of Astryx
- **The Gap:** There is no pre-packaged, opinionated backend design system with an embedded MCP server and `--dense` LLM context flag equivalent to Meta's Astryx for frontend.
- **Current Workaround:** DIY conversion of OpenAPI specs into MCP servers using `cnoe-io/openapi-mcp-codegen` or `awslabs/openapi-mcp-server`, or writing schema grounding tables into `AGENTS.md`.

### Gap 2: No Native Zero-Config OpenCode ↔ Antigravity Terminal/DOM Integration
- **The Gap:** Running OpenCode in Antigravity's terminal panel does not automatically link OpenCode to Antigravity's IDE-level DOM inspection or browser tools.
- **Current Workaround:** Manually adding a Puppeteer/Playwright MCP server (`@modelcontextprotocol/server-puppeteer`) to `opencode.json`.

### Gap 3: No Official n8n ↔ OpenCode Pipeline Import Path
- **The Gap:** n8n and OpenCode operate as separate ecosystems. n8n treats OpenCode as a sub-node model, rather than OpenCode invoking n8n workflows as tools. No official workflow import path exists.
- **Current Workaround:** Use OpenCode native orchestration plugins (`FlowDeck`, `Open Dynamic Workflows`, `deliberation`) instead of n8n.

### Gap 4: No Centralized Official OpenCode Plugin Marketplace
- **The Gap:** OpenCode lacks a centralized official plugin marketplace CLI (GitHub Feature Request #7467 remains open).
- **Current Workaround:** Community workarounds: `awesome-opencode`, `CKGrafico/opencode-market`, `NikiforovAll/opencode-marketplace`, and `kdcokenny/ocx`.

### Gap 5: No Customizable `statusLine` Shell Hook in OpenCode
- **The Gap:** OpenCode does not yet support Claude Code's native `statusLine` hook for piping session state to custom shell scripts (Feature Requests #30295 & #8619).
- **Current Workaround:** OpenTUI sidebar plugins like `sub-agent-statusline` or token-tracker footers.

### Gap 6: No Official Python SDK for OpenCode
- **The Gap:** Official SDKs exist for JS/TS (`@opencode-ai/sdk`) and Go (generated via Fern), but no official Python SDK exists (Issue #4031 open).
- **Current Workaround:** Programmatic execution via `opencode run` subprocess calls or JS/TS wrapper scripts.

### Gap 7: No Config Linter for `opencode.json` Security Settings
- **The Gap:** No standalone security linter exists to audit `opencode.json` files for overly permissive tool permissions or unsafe wildcard combinations.
- **Current Workaround:** Manual audit against permission mode guidelines or sandboxing via Docker (`fabianlema/opencode-sandbox`).

---

## Complete Research File Map

1. [`research/00-verification.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/00-verification.md) — Anti-hallucination verification pass
2. [`research/01-existing-summary.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/01-existing-summary.md) — Summary of all 26 elements in the OpenCode ecosystem catalog
3. [`research/02-ui-ux.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/02-ui-ux.md) — UI/UX design systems, Astryx, backend gap, 3D templates
4. [`research/03-multi-agent-council.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/03-multi-agent-council.md) — Multi-agent verification, council configuration, n8n evaluation
5. [`research/04-harness-environment.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/04-harness-environment.md) — Harness, Antigravity environment, DoD template, context anxiety
6. [`research/05-remaining-resources.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/05-remaining-resources.md) — Standardized 5-point breakdowns for all 20 verified remaining resources
7. [`research/06-unfound-and-gaps.md`](file:///C:/Users/Shashank%20Karamudi/.gemini/antigravity-ide/scratch/opencode-research/research/06-unfound-and-gaps.md) — Final summary of unfound items & ecosystem gaps
