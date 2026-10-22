# 07 — Design-to-Code (Figma-to-code, token extraction, screenshot-to-code, visual QA)

> Method: read-only WebSearch + WebFetch (no install/execute). Verified 2026-10-09 (UTC).
> Record spec (same as 06): `Name | URL | Type | Description | License (as stated) | Restrictions/Notes (docs scope only) | Agent/CLI integration`

## A. Figma-to-code (deterministic + agent pipelines)

### 01. Figma REST API (platform primitive)
- URL: https://developers.figma.com/docs/rest-api/
- Type: First-party file/nodes/images/variables API
- Description: Basis for all extractors below; cloud files only for most tools.
- License: Proprietary (Figma Terms + plan quotas).
- Restrictions/Notes: Requires PAT (`figd_`) with `file_content:read` (+ `library_content:read`, `file_variables:read` Enterprise); rate limits; unsaved local `.fig` not accessible.
- Agent/CLI integration: Consumed via CLI/MCP wrappers; not agent-native alone.

### 02. Figma Official MCP Server
- URL: https://developers.figma.com/docs/dev-mode-mcp-server/
- Type: First-party MCP (read + write via OAuth)
- Description: File creation + reads without PAT; used as base by pipeline tools.
- License: Proprietary (Figma Terms).
- Restrictions/Notes: Cloud round-trip, plan rate limits; some flows need Desktop bridge.
- Agent/CLI integration: MCP (OAuth, zero PAT setup per downstream READMEs).

### 03. spfr/figma-design-pipeline
- URL: https://github.com/spfr/figma-design-pipeline
- Type: MCP pipeline: inspect → safe mutations → token sync → codegen
- Description: Design-intelligence MCP + high-perf Figma plugin bridge (30–60× faster writes, 43 action types); works with Claude Code / Codex CLI / Gemini CLI; website capture.
- License: MIT (as stated).
- Restrictions/Notes: Needs official Figma MCP (OAuth) + local plugin manifest (`~/.figma-design-pipeline/plugin/manifest.json`) + WebSocket ports 4010–4014.
- Agent/CLI integration: MCP tools (`figma_get_tree/audit/extract_tokens/find_nodes/get_components/get_styles/diff_tokens/export_images`, `figma_plan_*/figma_map_components/figma_generate_page/figma_generate_schema/figma_export_tokens`, `figma_execute/plugin_status`).

### 04. khanglvm/figma-lens
- URL: https://github.com/khanglvm/figma-lens
- Type: Token-efficient headless Figma inspector (CLI or MCP, read-only)
- Description: `scout/extract/focus/focus-set/detail/search/export`; screenshots + exact layout/typography/assets without Desktop; concurrency-safe cache.
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Strictly read-only; cannot bypass permissions/rate limits, edit, distribute fonts, or read unsaved `.fig`; vision claims require host that opens screenshots.
- Agent/CLI integration: CLI + native MCP tools; skill chooses MCP when available.

### 05. tortastudios/figtree-cli (npm `figtree-cli`)
- URL: https://github.com/tortastudios/figtree-cli
- Type: Figma token extractor → multi-format code (no plugins/Dev Mode)
- Description: Colors/text/effects/grids → CSS, SCSS, Tailwind, JS, JSON, Android XML, SwiftUI; optional AI codegen or copy-paste prompt.
- License: Business Source License 1.1 (as stated — NOT OSI open-source).
- Restrictions/Notes: BSL-1.1 time-delay/field limits apply — see LICENSE; requires Figma token; AI path sends data to provider.
- Agent/CLI integration: CLI (`figtree`, `--output/--token/--debug`).

### 06. gettokken / tokken (PixelPappa/tokken, npm `tokken`/`gettokken`)
- URL: https://github.com/PixelPappa/tokken
- Type: Figma → VitePress doc-site + CSS framework generator (deterministic)
- Description: `tokken init/extract/generate/dev/build/sync`; pulls colors/typography/spacing/borders/effects/components/icons → `design-tokens.json`, PNGs/SVGs, searchable icon library, AI-ready spec.
- License: AGPL-3.0 (as stated on npm).
- Restrictions/Notes: AGPL network-copyleft; Figma token in `.env`/CI `FIGMA_ACCESS_TOKEN`; zero-dep Node generate step.
- Agent/CLI integration: CLI only; output is agent-consumable docs.

### 07. gregorymm/design-tokens (Claude Code plugin)
- URL: https://github.com/gregorymm/design-tokens
- Type: Figma variables/styles → W3C DTCG / CTI + write-back + rebind
- Description: 3-layer (Primitive/Semantic/Component) extraction across pages/files → `tokens.json/css/scss/style-dictionary.config.json`; merges Light/Dark; pushes back + rebinds layers to variables.
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Write-back route depends on plan: Enterprise REST `POST /v1/files/:key/variables`; Pro/Org generated plugin; Starter unsupported (use Tokens Studio/upgrade) — per README.
- Agent/CLI integration: Claude Code skill (`/design-tokens`); Desktop MCP or REST.

### 08. lewiscutey/figma-to-code-agent (npm `figma-to-code-agent`)
- URL: https://github.com/lewiscutey/figma-to-code-agent
- Type: Figma → React/Vue (+ CSS Modules/Tailwind/CSS) + MCP + Kiro Skill
- Description: Extract (cached, rate-limit aware) → parse AST → transform → generate → optimize; 2× images, vector-icon detect, token extraction, a11y, lazy-load/splitting, consistency checker, prototype gen.
- License: MIT (as stated).
- Restrictions/Notes: Requires Figma token; optional AI keys; Node 18+.
- Agent/CLI integration: CLI flags (`--token/--file/--node/--framework/--style/--typescript/--output/--preview/--mcp`); MCP server mode; Kiro Skill.

### 09. followtheart/d2c
- URL: https://github.com/followtheart/d2c
- Type: End-to-end D2C pipeline (Figma REST / `.fig` binary / Make / Sketch / native JSON → React+Tailwind / Vue SFC / HTML+CSS / RN / Flutter)
- Description: IR + token extraction (`TokenSet`, Tailwind preset, style-dictionary JSON), antd/MUI matching, responsive inference, `// ai:ignore` regions, high-fidelity `.fig` renderer, stage snapshots, multimodal LLM compare, Playwright visual-feedback loop.
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Cloud REST only for cloud files; local `.fig` via binary engine; visual-feedback requires `--reference-image --platform html` + pngjs + Playwright.
- Agent/CLI integration: CLI (`-i/-o/-p/-f --emit-ir/--emit-tokens/--emit-tailwind/--emit-diff --figma-token/--figma-file-key`, etc.).

### 10. felixAnhalt/figma-to-code-mcp
- URL: https://github.com/felixAnhalt/figma-to-code-mcp
- Type: MCP that compacts Figma data to CSS-aligned LLM format
- Description: Claims 99.5% size cut; inline styles, flexbox primitives, variable resolution, SVG export, pattern collapsing.
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Scopes `file_content:read`, `library_content:read`, `file_variables:read` (Enterprise, optional); rate-limit/API-call table in README.
- Agent/CLI integration: MCP tools (`get_figma_design`, `get_image_fills`, `render_node_images`, `read_vector_svg`); env/flag config.

### 11. rudraptpsingh/figbridge
- URL: https://github.com/rudraptpsingh/figbridge
- Type: Figma plugin + local MCP (bidirectional: import URL→Figma, audit, diff→patch, match-mockup loop)
- Description: 48 MCP tools; live-URL import (+hybrid snapshot, responsive sets), 5-dimension audit, `diff_to_source`/`generate_patch`, `match_mockup` render→diff→refine, `get_agent_bundle` offline zip (DESIGN.md/hierarchy/tokens DTCG+CSS/flow.mmd/ISSUES/CHANGES/AGENTS.md/manifest+screenshots).
- License: MIT (as stated: "Free. MIT. Runs entirely on your machine.").
- Restrictions/Notes: "No account, no token. Uses existing Figma desktop session" (local bridge `:7331` + Chrome ext for auth tabs/localhost); ES2017-safe plugin sandbox.
- Agent/CLI integration: MCP (stdio + HTTP/SSE) + plugin Run-button panel.

### 12. boring-km/figma-draft-to-code
- URL: https://github.com/boring-km/figma-draft-to-code
- Type: Figma Desktop ↔ Claude Code selection exporter (MCP + WebSocket :9001)
- Description: Saves only selected nodes → images/SVGs/tokens/structure to disk; context-token saving.
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Requires Figma Desktop plugin ("Development → Figma Draft to Code") + Claude Code running; selection-scoped.
- Agent/CLI integration: MCP tools (`figma_export_images/icons/tokens/structure/all/by_ids`); recommended `figma_export_all` → inspect `structure.json` → selective SVG/PNG fetch.

### 13. catisfy2/figma-cli (fork, figma-ds-cli) + @geeveeh/figma-cli
- URL: https://github.com/catisfy2/figma-cli / https://github.com/Shadowgandor/figma-cli
- Type: Local-Desktop (CDP) vs Cloud-REST CLI pair
- Description: `figma-ds-cli`: local Desktop build via CDP (no token, no rate limit, offline, DESIGN.md/Tailwind/CSS/tokens.json/Storybook import + export PNG/SVG/JSX/DTCG); `@geeveeh/figma-cli`: REST reads + comment write + 21 MCP tools.
- License: Both MIT (as stated).
- Restrictions/Notes: CDP path needs Desktop open + `connect`; token path needs `FIGMA_TOKEN`; token-cost table in README favors local path.
- Agent/CLI integration: CLI (`connect/import/export`) + MCP (`figma-mcp`); works with Claude Code/Cursor.

## B. Screenshot-to-code

### 14. abi/screenshot-to-code (upstream; forks: liseami, Lijun21, flokiyf)
- URL: https://github.com/abi/screenshot-to-code
- Type: Screenshot/mockup/Figma/video → code (React/Vite + FastAPI)
- Description: Stacks: HTML+Tailwind, HTML+CSS, React+Tailwind, Vue+Tailwind, Bootstrap, Ionic+Tailwind; models: Gemini 3/3.1 Pro, GPT-5.5/5.4 Mini, Claude Opus 4.6/4.8, z-image-turbo (Replicate); asset extraction, bg removal, self-render check via Playwright Chromium.
- License: MIT (as stated).
- Restrictions/Notes: Self-host needs ≥1 provider key (OpenAI/Anthropic/Gemini strongly recommended + Replicate for images); screenshots stay local only when self-hosted; hosted app at screenshottocode.com is paid.
- Agent/CLI integration: Docker Compose / Poetry+pnpm; mock mode (`MOCK=true`); agent consumes generated code.

### 15. Anima Playground — Image to Code
- URL: https://animaapp.com/blog/ai-en/image-to-code/
- Type: Proprietary image→app (HTML/React) workflow
- Description: Upload screenshot/mockup → delayer to text/assets/layout → responsive HTML/React + chat refine + publish/export.
- License: Proprietary (paid plans; check terms).
- Restrictions/Notes: Quality depends on clear/cropped image + intent prompt; live-website clone is separate workflow.
- Agent/CLI integration: Web app + export; no OSS CLI/MCP.

### 16. Locofy.ai (proprietary comparator)
- URL: https://www.locofy.ai
- Type: Proprietary Figma-plugin D2C (React/Gatsby/Next.js)
- Description: Native layer/component-structure aware export.
- License: Proprietary subscription; no self-host (as documented in comparisons).
- Restrictions/Notes: Per-export/seat pricing; designs processed on vendor infra.
- Agent/CLI integration: Figma plugin; no OSS agent surface.

### 17. Builder.io Visual Copilot (proprietary comparator)
- URL: https://www.builder.io
- Type: Proprietary visual CMS + D2C (React/Angular/Vue)
- Description: Visual editing + content workflow + code export.
- License: Proprietary subscription.
- Restrictions/Notes: Platform lock-in vs single-step converters.
- Agent/CLI integration: Hosted platform; export only.

## C. Visual QA (regression / fidelity gates for generated UI)

### 18. Chromatic (Storybook)
- URL: https://www.chromatic.com
- Type: Proprietary visual QA (Storybook-native)
- Description: Snapshot baselines, TurboSnap, a11y + interaction tests in CI.
- License: Proprietary (free tier + paid; check terms).
- Restrictions/Notes: Best with Storybook; snapshot quotas apply.
- Agent/CLI integration: CLI (`chromatic`) + GitHub checks; JSON reports for agents.

### 19. Percy by BrowserStack + Lost Pixel + Argos CI (open-source-friendly tier)
- URL: https://percy.io / https://github.com/lost-pixel/lost-pixel / https://argos-ci.com
- Type: Visual regression services / self-hostable runner
- Description: Percy: cross-browser snapshots (proprietary); Lost Pixel: OSS self-hostable (`lost-pixel` Docker, Playwright/Cypress/Storybook); Argos: GitHub-integrated screenshot diffing (usage-based).
- License: Lost Pixel MPL-2.0 (verify in repo); Percy/Argos proprietary.
- Restrictions/Notes: Baseline storage/quotas; self-host keeps images local (Lost Pixel).
- Agent/CLI integration: CLIs + CI status; diff images consumable by vision agents.

### 20. BackstopJS + Playwright Visual + Applitools (matrix)
- URL: https://github.com/garris/BackstopJS / https://playwright.dev/docs/test-snapshots / https://applitools.com
- Type: OSS engine + framework snapshots + commercial AI-eyes
- Description: BackstopJS (Resemble.js scenarios, Docker); Playwright `toHaveScreenshot` (built-in, free); Applitools Eyes (AI diff, proprietary).
- License: BackstopJS MIT; Playwright Apache-2.0; Applitools proprietary.
- Restrictions/Notes: Backstop needs reference-image curation; Playwright needs deterministic rendering (fonts/animations); Applitools seat/run pricing.
- Agent/CLI integration: CLI (`backstop test/approve`, `playwright test --update-snapshots`); artifacts feed `match_mockup`-style loops.

---
Counts: 20 records (01–20).
