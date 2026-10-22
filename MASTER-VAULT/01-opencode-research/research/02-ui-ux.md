# Phase 2 — UI/UX, Design Systems, Frontend & Backend Resources

> Research completed: 2026-08-09  
> Scope: Frontend design resources, their OpenCode-usability status, backend equivalent gap assessment, 3D template candidates

---

## SECTION A — Confirmed Starting Point: facebook/astryx

**Status: Confirmed real and active.**

Meta released Astryx publicly in June 2026 (announcement ~June 18–28, 2026). It was built internally at Meta over eight years and powers 13,000+ internal applications. It is MIT licensed and currently the strongest single frontend pick for agent-driven development.

**What it is:** A React 19+ / StyleX design system with 150+ accessible components, page templates, brand-level theming, and dark mode.

**Why it matters for OpenCode specifically:**
- Ships a native **MCP server** — agents can programmatically query components, retrieve documentation, and map configurations without guessing props
- Includes a CLI (`astryx` or `xds`) with a `--dense` flag that produces token-efficient output optimized for LLM context windows
- Running `npx @astryxdesign/cli init --features agents` auto-generates an `AGENTS.md` file with component inventory and install paths

**OpenCode support type:** Open standard (MCP server) — add to `opencode.json` under `mcp` key.

**Verdict: TOP PICK #1.** Purpose-built for the exact problem (agents hallucinating component props or installing non-existent components). Nothing else in this sweep comes close on this specific axis.

---

## SECTION B — Design/UX Resources: Per-Item Findings

### lawsofux.com
**Real site, reference-only.** Jon Yablonski's Laws of UX — 30+ UX psychological principles (Hick's Law, Fitts's Law, Jakob's Law, Miller's Law, Gestalt principles, etc.). No MCP server exists. No skill wrapper found independently at lawsofux.com itself.

**There IS a skill wrapper: `keysjoao/laws-of-ux-skills`** (see next entry).

---

### keysjoao/laws-of-ux-skills
**Confirmed real, installable SKILL.md package — not just documentation.**

- Three core skills: **Advisor** (design guidance based on UX laws), **Audit** (analyzes interfaces for UX violations), **Pre-ship Checklist** (checks for UX law compliance before deployment)
- Companion reference file `ux-laws-complete.md` maps each law to: practical definition, common violations, actionable fixes
- Pure Markdown files — zero dependencies, zero build step
- Follows the Agent Skills standard (`SKILL.md` format)

**OpenCode support type:** Open standard — copy skill directory to `.opencode/skills/` or `~/.config/opencode/skills/`.

**Verdict: TOP PICK #2.** Directly actionable: install it once and the agent will automatically apply UX law validation to any frontend task. This is reference material distilled into agent-usable form — no manual prompting required.

---

### alexpate/awesome-design-systems
**Confirmed real, actively maintained. ~25k stars.**

A curated list of real-world design systems from Google, IBM, Shopify, Atlassian, Airbnb, and hundreds more. Links to each system's documentation, component libraries, and style guides.

**OpenCode support type:** Reference-only. Not installable as a skill or MCP server. Use value: browse when choosing a design system for a project; agents could reference the linked systems directly but there's no agent-ready wrapper.

**Gap note:** This is a discovery/reference catalog, not an executable tool. Worth bookmarking, not including in an active OpenCode setup.

---

### gztchan/awesome-design
**Confirmed real. ~17.4k stars, actively maintained.**

Comprehensive list of UI/UX tools, frameworks, visual resources — color tools, typography resources, icon sets, inspiration sites, design handoff tools.

**OpenCode support type:** Reference-only. No skill or MCP wrapper found. Same use profile as alexpate/awesome-design-systems — a discovery list for human browsing.

**Gap note:** Worth a bookmark; not something to integrate into an active agent setup.

---

### kevindeasis/awesome-ui
**Confirmed it exists as a GitHub repo.**

Curated list of UI theory, color psychology, typography rules, grid standards, interaction design references.

**OpenCode support type:** Reference-only. No skill or MCP wrapper. Minimal practical advantage over the UX laws skill already covered by keysjoao/laws-of-ux-skills.

**Verdict: Low priority for this setup.** The laws-of-ux-skills already covers the actionable subset.

---

### batoreh/awesome-ux
**Confirmed it exists as a GitHub repo.**

Resources on information architecture, user research, usability testing, and interaction models.

**OpenCode support type:** Reference-only. No skill or MCP wrapper found. Leans more toward UX research methodology than agent-usable rules.

**Verdict: Skip for this setup.** Covers territory relevant to product researchers, not agent-driven frontend coding.

---

### VoltAgent/awesome-design-md
**Confirmed real, actively maintained.**

A curated collection of `DESIGN.md` files — plain-text markdown files that codify a project's design language so AI coding agents can generate consistent, brand-accurate UI. Introduced by the Google Stitch format. Includes files for brands like Stripe, Vercel, Notion, Apple, and others.

**What a DESIGN.md contains:**
- Design tokens (color palettes, typography, spacing, border radii) in YAML/Markdown
- Design intent (look and feel, layout principles, responsive behaviors) in human-readable prose
- Validation support via `npx @google/design.md lint` for WCAG and token integrity checks

**OpenCode support type:** Open standard — drop a `DESIGN.md` into the project root; prompt the agent with "follow the visual language defined in DESIGN.md." Works with any agent that can read files, including OpenCode natively.

**Version note:** The previous project clone may be stale — this format has evolved and new brand files have been added. Worth re-pulling if using brand-specific DESIGN.md files.

**Verdict: TOP PICK #3.** Highly practical — a single file drop that constrains all agent UI work to a consistent visual language. Pairs naturally with Astryx (use Astryx for component accuracy, DESIGN.md for brand/visual consistency).

---

### Google Material Design 3 (m3.material.io)
**Real, maintained by Google. Standard rules for grid systems, color tokens (60:30:10), accessibility, motion.**

**OpenCode-usable skill or MCP:** No official OpenCode-specific MCP or skill found from Google. However:
- The **shadcn/ui** system (see below) includes Material-adjacent token patterns
- A `DESIGN.md` for Material Design could be manually authored using VoltAgent's awesome-design-md format
- Context7 (already in the catalog) can pull Material Design docs on demand via MCP

**Verdict:** Reference-only natively, but can be made agent-usable via a custom DESIGN.md. Not a priority install — Astryx and shadcn/ui cover the actionable component layer already.

---

### Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines)
**Real, maintained by Apple. Spatial layout, interaction design, touch targets, accessibility.**

**OpenCode-usable skill or MCP:** No official skill or MCP wrapper found from Apple. The emilkowalski/skills repo (confirmed in Phase 0 as the correct name for the voice-to-text "enilkowaski" entry) provides Apple HIG-adjacent skills for component-level UI patterns, but not a full HIG wrapper.

**Custom skill opportunity:** High value for iOS/macOS agent work; a custom SKILL.md distilling HIG touch target minimums, safe area rules, and typography hierarchy would be worth building. Straightforward to create — HIG content is static and well-structured.

**Verdict:** Reference-only natively. Not a priority for web-first OpenCode work; add to a custom skill backlog for mobile contexts.

---

### shadcn-ui/ui
**Confirmed real, actively maintained. The dominant accessible component system built on Tailwind CSS + Radix UI primitives.**

**OpenCode-usable MCP:** **Yes, confirmed.** Two paths:
1. **Official shadcn MCP** (remote): `https://www.shadcn.io/api/mcp?token=${SHADCNIO_TOKEN}` — add to `opencode.json` under `mcp` key; agent can browse registry, query component props, and install components without hallucinating
2. **Community server**: `@jpisnice/shadcn-ui-mcp-server` via `npx` for self-hosted/local alternative

**What the MCP enables:** Agent fetches the *actual* current props and variants from the shadcn registry in real time — prevents the common failure mode where agents use outdated 2023/2024 component APIs. As of July 2026, MCP servers are stateless per updated spec, making this more reliable and easier to host.

**Verdict: TOP PICK #4 (paired with Astryx for non-Astryx projects).** If a project doesn't use Astryx (e.g., it's Tailwind-based), shadcn/ui MCP is the equivalent hallucination-prevention tool. Use Astryx for Meta-ecosystem work; shadcn/ui MCP for Tailwind/Radix work.

---

### refactoringui.com (Refactoring UI)
**Real book/site by Adam Wathan and Steve Schoger (creators of Tailwind CSS). Tactical UI design principles for developers.**

**OpenCode-usable skill or MCP:** No official skill or MCP wrapper found. The content is a paid book/video course, not open-source, so building a skill from it would require manual extraction.

**Verdict:** Reference-only. Foundational reading for understanding why certain UI decisions work, but not directly actionable in an agent setup without manual work to extract principles into a SKILL.md.

---

## SECTION C — Backend Equivalent: Honest Assessment

**Direct question from the spec:** Is there anything that does for backend architecture what Astryx does for frontend components — structured, agent-readable API/schema specifications that prevent an agent from inventing endpoints or schema fields that don't exist?

**Honest answer: Nothing at Astryx's level of polish exists for the backend. But the underlying capability does exist via a different path.**

### What exists:

**OpenAPI → MCP conversion (the closest equivalent):**
- `cnoe-io/openapi-mcp-codegen` — generates an MCP server from any OpenAPI spec, including optional LangGraph ReAct agent alongside the server. Any backend with an OpenAPI/Swagger spec can be wrapped as an MCP server that an agent calls to discover and validate real endpoint shapes.
- `ckanthony/openapi-mcp' and `awslabs/openapi-mcp-server` — proxy servers that dynamically convert OpenAPI paths and operations into MCP tools; add to `opencode.json` like any other MCP server.

**The key difference from Astryx:** These are DIY — you generate the MCP server from *your* OpenAPI spec. Astryx uses a CLI bash-call integration (no MCP server — see Phase 8 correction). For backend, *you* have to create the OpenAPI spec first (if you don’t already have one) and then wrap it. This is meaningful additional work, not a drop-in solution.

**Pattern that works well:** Define your backend's schema in OpenAPI format → run `openapi-mcp-codegen` → add the generated server to `opencode.json` → agent can now query real endpoints before writing code. This effectively prevents endpoint hallucination for *your* specific backend, but it doesn't provide the universal design-system-level polish that Astryx provides for component APIs.

**What doesn't exist yet:** A backend equivalent of Astryx's opinionated, pre-packaged, design-system-style collection of architectural patterns, schema conventions, and validation rules that agents can query without any manual setup work. This gap is real. The closest things — structured OpenAPI MCP proxies — require you to already have a well-defined API spec and then do additional tooling work. For greenfield backend work where an agent is *creating* the schema from scratch, nothing prevents hallucination as cleanly as Astryx does on the frontend side.

**Recommendation:** For any project with an existing OpenAPI spec, use the openapi-mcp-codegen approach. For greenfield backend work, write schema definitions into AGENTS.md as structured reference tables (endpoints, types, required fields) and use that as the agent's grounding contract — imperfect but the best available option.

---

## SECTION D — 3D Website Templates: Agent-Usable Candidates

**Criterion from the spec:** Templates with clear, extendable code structure an agent could actually work with — not static showcase demos meant purely for human browsing. TypeScript, modular architecture, and a build tool the agent can reason about are the key markers.

### Candidate 1: pmndrs/react-three-start
**GitHub: `pmndrs/react-three-start`**

The official meta-framework from the React Three Fiber (R3F) creators. File-based scene composition: add a file (`cube.scene.tsx`, `hud.dom.tsx`) and the framework automatically wires up the 3D layer and DOM overlay. TypeScript-first, Vite-based.

**Why it's agent-friendly:** File-based composition means an agent can add new scene elements without touching the rendering loop — each element is isolated. The opinionated structure gives the agent clear placement rules: where to put geometries, lights, physics components.

**Best for:** Creative portfolios, interactive product experiences, anything where the 3D content is the primary feature.

**Verdict: TOP 3D PICK.** Most directly extendable by an agent; structure is explicit enough to give the agent reliable guidance without needing detailed prompting.

---

### Candidate 2: Vite + React Three Fiber (R3F) + TypeScript manual scaffold
**Repos:** `pmndrs/react-three-fiber` (docs/reference) + manual Vite scaffold

The standard 2026 industry setup: `npm create vite@latest -- --template react-ts` then `npm install three @types/three @react-three/fiber @react-three/drei`.

**Why it's agent-friendly:** Fully componentized Three.js — agents can modify specific scene parts (lights, meshes, materials) without breaking the rendering loop. Component isolation is the key structural property. Add `r3f-perf` for dev-time monitoring.

**Best for:** Projects where you want full control over structure and don't need the meta-framework conventions of react-three-start.

**Verdict: Solid second choice.** Requires more initial setup decisions, but gives agents a clear component-based structure to work within.

---

### Candidate 3: react-three-next (pmndrs/react-three-next)
**GitHub: `pmndrs/react-three-next`**

R3F + Next.js template. Adds SSR and routing on top of the standard R3F stack.

**Why it's agent-friendly:** Same R3F component model as Candidate 2, with Next.js file-based routing giving agents clear module boundaries.

**Best for:** 3D experiences that need SEO, multiple routes, or server-side data fetching alongside 3D content.

**Verdict: Use when you need Next.js; use react-three-start otherwise.** The added complexity of Next.js is only worth it if the project genuinely needs it.

---

### On pure Three.js (no React) templates:
**Bruno Simon's Three.js Journey starter** (Vite-based) exists and is high quality for learning. However, imperative vanilla Three.js is harder for agents to reason about than declarative React component models — the agent can't isolate a "mesh component" cleanly in an imperative codebase. For agent-driven 3D work, the R3F component model is strictly preferable.

---

## Recommendations Summary

| Priority | Resource | Type | Install Path |
|---|---|---|---|
| **#1** | facebook/astryx | React design system + CLI bash integration (NO MCP server — Phase 8 correction: MCP package not found in repo) | `npx @astryxdesign/cli init --features agents`, then bash calls: `npx @astryxdesign/cli component <Name> --dense` |
| **#2** | keysjoao/laws-of-ux-skills | OpenCode skill (SKILL.md) | Copy to `.opencode/skills/` |
| **#3** | VoltAgent/awesome-design-md | DESIGN.md file drop | Drop into project root |
| **#4** | shadcn/ui MCP | MCP server | Add to `opencode.json` (for non-Astryx projects) |

**3D templates (ordered):**
1. `pmndrs/react-three-start` — file-based, most agent-friendly structure
2. Vite + R3F + TypeScript manual scaffold — full control, well-understood by agents
3. `pmndrs/react-three-next` — use only if Next.js is genuinely needed

**Backend gap:** No turnkey backend equivalent of Astryx exists. The OpenAPI → MCP conversion path (`cnoe-io/openapi-mcp-codegen`, `awslabs/openapi-mcp-server`) is the best available approach for projects with existing API specs. For greenfield work, AGENTS.md schema tables are the current practical fallback.

**Reference-only resources (not integrated into active agent setup):**
- alexpate/awesome-design-systems — human discovery catalog
- gztchan/awesome-design — human discovery catalog
- kevindeasis/awesome-ui — covered by laws-of-ux-skills
- batoreh/awesome-ux — UX research methodology, not agent-coding-relevant
- refactoringui.com — paid book, no open-source skill wrapper
- Google Material Design 3 — reference-only; DESIGN.md custom file if needed
- Apple HIG — reference-only; custom SKILL.md backlog item for mobile contexts
