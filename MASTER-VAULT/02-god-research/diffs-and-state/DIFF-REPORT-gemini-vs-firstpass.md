# DIFF REPORT — Gemini Second Pass vs First Pass (Muse)

Date: 2026-10-09 (UTC)
Role: Reconciler-Auditor — read-only analysis, no installs, no executions, no prompt-body reproduction.
Task todos (via files only): ✅ sample-read key files · ✅ verify/adjudicate known conflicts · ✅ count gemini-only additions · ✅ write 3 reports (this file + `00-README-second-pass.md` + `A-master-index.md`).

## 1. Method

Sample-read (full or head + targeted grep, line counts via `wc`):

- First pass (`/mnt/c/Users/Shashank Karamudi/Desktop/God research/`):
  - `00-phase0-inventory.md` (214 lines) — full read
  - `C-named-register-23.md` (272 lines) — full read
  - `E-prompt-directory-meta-only.md` (146 lines) — full read
  - `D-design-styles/00-index-29.md` (55 lines) — full read
  - `B-category-catalogs/` — directory listing + `23-watchlist.md` head (60 lines; byte-identical duplicate of `C-named-register-23.md` for the portion read) + per-file line counts for all 23 catalogs
  - `_state/resource-index.json` — read (single-line JSON index)
- Second pass (`/mnt/c/Users/Shashank Karamudi/Desktop/God research - gemini/`):
  - `06-watchlist-prompts.md` (136 lines) — full read
  - `02-design-styles.md` (628 lines) — full read lines 1–622 (capped at 50 KB by reader; tail matrix rows 26–29 + closing not re-read, non-load-bearing)
  - `01-core-web-tech.md` (960 lines) — head 80 + section headers
  - `03-skills-mcp.md` (545 lines) — head 80 + §5 catalog (lines 454–513) + grep for totals
  - `04-agents-harness-context.md` (910 lines) — head 80 + Part IV index (lines 80–104)
  - `05-infra-ops.md` (1043 lines) — head 80 + Pillar 7 index (lines 80–109)

No web re-checks performed (per task: adjudicate from file contents, no web needed).
Star/fork/commit counts below are point-in-time excerpts recorded in the source files, not live guarantees.

## 2. Counts table

| Source | Files | Claimed totals (from file headers) | Lines (wc) |
|---|---|---|---|
| First pass — `B-category-catalogs/` (23 files) | 23 | Catalog Elements 1–26: **163 usable / 43 excluded** (per `00-phase0-inventory.md` §B) | 01:497, 02:579, 03:540, 04:503, 05:619, 06:177, 07:173, 08:177, 09:579, 10:784, 11:518, 12:480, 13:479, 14:524, 15:422, 16:461, 17:426, 18:421, 19:421, 20:463, 21:175, 22:146, 23:272 |
| First pass — `C-named-register-23.md` (+ dup `B/23-watchlist.md`) | 1 (+1 dup) | **13 RESOLVED / 1 PARTIAL / 9 UNRESOLVED** of 23 | 272 |
| First pass — `D-design-styles/` | 30 (00-index + 29 styles; task brief says 00–29) | **29 styles**, per-style code-coverage verdicts + fetch ledger | 00-index: 55 |
| First pass — `E-prompt-directory-meta-only.md` | 1 | **12 records P-01–P-12** (8 inspected; P-09/P-10/P-12 placeholders) | 146 |
| First pass — `00-phase0-inventory.md` | 1 | Inventory of 23 upstream source files + §§A–F | 214 |
| Gemini `01-core-web-tech.md` | 1 | **82 resources** (9 domains: 10+10+10+10+12+10+8+6+6) | 960 |
| Gemini `02-design-styles.md` | 1 | **29 styles** + design-systems landscape + D2C pipelines + assets + 3D | 628 |
| Gemini `03-skills-mcp.md` | 1 | **56 resources** (§5 catalog; "DONE. 56 resources cataloged") | 545 |
| Gemini `04-agents-harness-context.md` | 1 | **68 resources** (18 agents + 16 multi-agent + 18 harness + 16 context/memory) | 910 |
| Gemini `05-infra-ops.md` | 1 | **70 resources** (7 pillars × 10) | 1043 |
| Gemini `06-watchlist-prompts.md` | 1 | **23/23 watchlist RESOLVED + 3 prompt archives** | 136 |
| **Gemini total** | **6** | **≈276 resources + 29 styles + 23 watchlist + 3 archives** (watchlist/archive overlap with first pass; bulk of the 276 is net-new baseline coverage — see §3) | 4222 |

## 3. NEW in Gemini (not in first pass)

Nature of the delta: first pass is **deep, OpenCode-build-targeted** (26 catalog elements mapped to INCLUDE/EXCLUDE build dispositions, harness templates, DoD gates); Gemini is **broad, encyclopedic baseline** (languages → deploy → SEO/commerce). Overlap is narrow (Astryx, eve, ruflo, ECC, Agent Skills standard, `anthropics/skills`, cookbooks, public-apis, Firecrawl, Context7, MCP/tooling concepts). Everything below is gemini-only to the extent of the sampled surface:

- `01-core-web-tech.md` (82): full language / framework / runtime / data / cloud baseline first pass never cataloged as such — TypeScript, JS, HTML5, CSS3, Wasm, Python, Go, Rust, PHP, Ruby; React, Vue, Angular, Svelte, SolidJS, Preact, Lit, Alpine.js, HTMX, Qwik; Tailwind, Sass, PostCSS, CSS Modules, styled-components, Emotion, Panda CSS, shadcn/ui, Radix, daisyUI; Vite, Webpack, Rollup, esbuild, Turbopack (+5 more build/runtime entries); backend/fullstack/API protocols (12); databases/ORMs (10); cloud/auth/dev-services (8); scaffolders/monorepo (6); architecture patterns/specs (6). First pass covered only the agentic slice of this (shadcn MCP, Radix primitives, Context7, OpenAPI→MCP proxies).
- `03-skills-mcp.md` (56): standards/spec layer + MCP SDK/registry breadth — `agentskills.io` frontmatter schema + progressive-disclosure lifecycle, MCP JSON-RPC/stdio/Streamable-HTTP spec, `modelcontextprotocol/*` TS/Python/Go/Rust/Kotlin/C#/Swift SDKs, registries (Smithery, Glama, PulseMCP, mcp.so, mcprun, official `servers` mono-repo), reference servers (filesystem/github/postgres/sqlite/memory/brave-search/fetch/puppeteer/slack/git/sentry/docker), FastMCP/LiteMCP; plus adjacent paradigms (A2A, FIPA-ACL, LSP, REST/OpenAPI function-calling) and tooling (`vercel-labs/skills` CLI, `skills-cli`, Serverpod CLI, AgentGym, skills.sh, agenticskills.io, EvoSkill, HappyCapy optimizer). First pass has MCP servers/registries only via catalog Element 6/19 excerpts.
- `04-agents-harness-context.md` (68): coding-agent matrix (OpenCode, Claude Code, Cursor, Codex CLI/Operator, Gemini CLI/Antigravity, Copilot, Windsurf/Cascade, Cline, Roo, Aider + specs: MCP spec, Skills standard, AGENTS.md, Claude Agent SDK, Cursor Rules, OpenCode permission schema, Cline/Roo modes); multi-agent runtime-vs-roleplay taxonomy (Subagents/Teams, OpenCode subagents, Agents SDK/Swarm, ADK/A2A, LangGraph, CrewAI, AutoGen/MAF, MetaGPT-as-roleplay-archetype, OpenHands, Devin/Cognition, orchestrator-worker, evaluator-optimizer/planner-executor, council-voting, red/blue-team, blackboard, ACP); harness guardrails (Spec Kit, OpenSpec/OPSX, Conductor, DoD gates, TDD loops, `--max-turns`, background daemons, checkpointing, worktrees, Docker/Firecracker/WASM sandboxes, handoffs, living docs, pre-commit, OTel evidence, permission tiers, token budgeting, self-improving loops, SWE-bench); context/memory (OpenAI/Gemini/Cohere-Voyage embeddings, pgvector, Pinecone, Weaviate, Qdrant, Milvus/Zilliz, Chroma, LanceDB, Tree-sitter, ast-grep, Aider repo-map, Repomix/CodePack, Context7, session-compaction protocols). Net-new vs first pass: the general-agent baseline, the runtime-vs-roleplay framing, and the vector/AST memory catalog.
- `05-infra-ops.md` (70): 7×10 operational pillars — scraping (Scrapy, Crawlee, Apify, Firecrawl, Crawl4AI, BeautifulSoup4, lxml, Cheerio, Playwright-extraction, curl_cffi); public-API standards (GitHub, Stripe, Twilio, OpenAI, Algolia, Open-Meteo, IPinfo, Open Exchange Rates, Resend, Unsplash); QA (Vitest, Jest, pytest, Playwright Test, Cypress, axe-core, Postman/Newman, Pact, Testcontainers, k6); security/sandboxing with **[ENFORCEABLE] vs [PROMPT-ONLY]** taxonomy (Docker, gVisor, Firecracker, nsjail/seccomp-bpf, E2B, Semgrep, CodeQL, TruffleHog vs NeMo Guardrails, prompt/policy files); CI/CD (git/worktrees, pre-commit, Husky/lint-staged, Actions, GitLab, Jenkins, CircleCI, Argo, Dagger, OpenTofu/Terraform); cloud/deploy (Vercel, Netlify, Cloudflare Workers/Pages, Fly.io, Lambda, K8s, Supabase, Vault, OTel, Datadog); SEO/CMS/commerce (Next.js Metadata API, Schema.org/JSON-LD, Search Console, Lighthouse/CWV, Contentful, Strapi, Sanity, Shopify, Medusa.js, Stripe Checkout). First pass covers only scattered equivalents (Playwright MCP, guards, hooks, worktrees).
- `02-design-styles.md` (29-style taxonomy): same 29-slot list as first-pass `D/`, but different treatment — token-level UI spec per style (meaning/elements/uses/resources), design-systems landscape (Astryx, Polaris, M3, Carbon, Atlassian, Radix/Shadcn, Primer, HIG), D2C pipeline architecture (W3C DTCG → Style Dictionary → Mitosis/Locofy/v0), asset pipelines (Lucide/Heroicons/Phosphor/Tabler/SVGL, unDraw/Open Peeps/Storyset, Unsplash/Pexels, Image CDNs), 3D/motion (Three.js/R3F/Drei, Spline, Babylon, GLSL/TSL, Framer Motion, GSAP, Theatre.js, Rive, Lottie), summary comparison matrix. Explicit GAPs declared for **Maximalism, Surrealism, Neoclassical, Luxury-type, Bohemian, Victorian, Graffiti, Body-art** (custom-build with R3F/GSAP/Tailwind/font/SVG stacks instead of kits). Complements first-pass `D/` fetch-ledger approach (see §4c).
- Watchlist resolutions (§4b) + prompt archives (§4d): 9 newly asserted canonicals + file-level `asgeirtj` census (1264 files/17 dirs) + 2 new archives (`LouisShark`, `Piebald-AI`) + `VoltAgent/awesome-agent-skills` comparator.

## 4. CONFLICTS with adjudication

### (a) Astryx MCP — verdict: **Corrected-nuanced (BOTH TRUE at different scopes)**

- First pass evidence: `00-phase0-inventory.md:47` + `§C.1` — "Astryx CLI-only, NO MCP. packages/mcp-server + packages/mcp both 404; CLI README zero MCP refs; no `mcp` subcommand. Integration = bash `npx @astryxdesign/cli <cmd> --dense` only." `C-named-register-23.md:118-126` repeats with tree evidence (`apps/`, `packages/` core/cli/build/themes, `AGENTS.md`/`CLAUDE.md`, 15-ish commands, manifest `--json`, programmatic `@astryxdesign/cli/api`) but carries an explicit caveat (`C:125`): "full-repo grep for 'mcp' not performed (read-only fetch limit); re-verify with code search before claiming absolute absence."
- Gemini evidence: `02-design-styles.md:11-43` — repo anatomy adds `packages/{richtext,vega,charts,lab}` + `apps/docsite`; "no `@astryxdesign/mcp` package in npm or in `packages/`, and the local CLI client contains no `astryx mcp` command or local stdio MCP server daemon" (agrees with first pass **within local-distribution scope**); "MCP Server Exists Exclusively as a Remote Docsite Endpoint" at `apps/docsite/src/app/mcp/route.ts` on `mcp-handler`+`zod`, Streamable HTTP at `https://astryx.atmeta.com/mcp`, tools `search(query,type?,limit?)` (~1.5K-token briefs from `.doc.mjs` keyword index) and `get(name,type)` (props/interfaces/hooks/examples).
- Reasoning: no contradiction once scope is split — first pass checked **local distributable surface** (npm packages dir, CLI subcommands); Gemini checked **hosted app surface** (docsite route). The caveat in first-pass `C:125` is exactly where the new finding fits.
- Record: **Corrected-nuanced** — local toolchain = CLI-only (no npm MCP package, no `astryx mcp` stdio daemon); MCP capability = hosted remote endpoint only. Build guidance stands (bash/JSON CLI for local work) + add optional remote-MCP pointer with transport/approval/cost review before adoption.

### (b) `vercel/deepsec` — verdict: **Unresolved-pending-reverify (needs live re-check)**

- First pass internal tension: `00-phase0-inventory.md:62` (2026-08-09) = "✅ Confirmed … https://github.com/vercel/deepsec"; `C-named-register-23.md:128-136` (2026-10-09) = direct fetch → **HTTP 404**, status UNRESOLVED, "needs org/rename/transfer search."
- Gemini evidence: `06-watchlist-prompts.md:27` — `vercel/deepsec` → 404; canonical = **`vercel-labs/deepsec`** (HTTP 200), `npx deepsec init`.
- Reasoning: Gemini's rename/transfer hypothesis is plausible (Vercel commonly ships under `vercel-labs/`), but first pass never checked that org, and Gemini's 200 is a file-internal claim with no captured README excerpt in the sample. Time gap (Aug-confirmed → Oct-404) is consistent with move/privatization/deletion, but also with transient/rate-limit artifacts (first pass hit several 429s this session).
- Record: **Unresolved-pending-reverify** — do NOT cite either URL as canonical. Retry queue: fetch both `github.com/vercel/deepsec` and `github.com/vercel-labs/deepsec` live, capture HTTP status + README/about + created/pushed dates, check org-transfer/redirect banners before updating the register.

### (c) Watchlist counts — first 13/1/9 vs Gemini 23/23 — verdict: **9 gemini-only assertions, confidence varies; keep PARTIAL on awesome-lists**

First-pass baseline (`C:250-254`): RESOLVED 13 (1,4,7,9,10,11,13,14,15,17,18,20,22); PARTIAL 1 (21); UNRESOLVED 9 (2,3,5,6,8,12,16,19,23).

| # | Original | First pass | Gemini canonical | Adjudication |
|---|---|---|---|---|
| 2 | PizzaBox AWS | UNRESOLVED (no exact `*/PizzaBox`; candidates listed but refused) | `pizza-bot-app/pizza-bot` RESOLVED + Two-Pizza/1U conflation note | **Downgrade to provisional** — Gemini's functional/conflation argument is reasoning, not name evidence; first pass correctly notes neither candidate claims the name. Keep retry for exact string. |
| 3 | Scrapling Krim Shoair | UNRESOLVED (429, no fetch) | `D4Vinci/Scrapling` + author Krim Shoair (@D4Vinci) | **Accept provisionally** — linkage (author handle = name string) is coherent; needs README/PyPI pin to close. |
| 5 | Munder Difflin | UNRESOLVED (429) | `chaitanyagiri/munder-difflin` (local-first multi-agent harness, "Michael" lead, Office parody) | **Accept provisionally** — specific org/repo + function; needs fetch pin. |
| 6 | Taste skill | UNRESOLVED (absent from `anthropics/skills` tree) | `Leonxlnx/taste-skill` (`tasteskill.dev`, "anti-slop" SKILL.md) | **Accept provisionally** — explains absence (community skill, not first-party); needs registry/README pin. |
| 8 | Backend design skill | UNRESOLVED (no `backend-design` in `anthropics/skills`) | `skills/backend-design` convention via `vadimcomanescu/codex-skills`, `xenitV1/claude-code-maestro`, `docs/backend-design.md` | **Accept as convention, not single repo** — no single canonical URL asserted; treat like DESIGN.md convention. |
| 12 | DeepSec | UNRESOLVED (404) | `vercel-labs/deepsec` | **Unresolved-pending-reverify** (see §4b). |
| 16 | Designs | UNRESOLVED (generic) | Claude Design Variant Pattern (`claude.ai/design`, `design-shotgun`) | **Accept as pattern, not repo** — interpretive resolution; do not cite as a repository. |
| 19 | Strix | UNRESOLVED (collision) | `usestrix/strix` (PyPI `strix-agent`, pentest harness, PoCs in Docker) | **Accept provisionally** — disambiguation from ASUS/hardware noted; needs fetch pin. |
| 23 | NotebookLM skill | UNRESOLVED (no pin) | `PleasePrompto/notebooklm-skill` + `sanjay3290/…` + `claude-world/…` | **Accept as multi-candidate** — community-skill pattern, no single canonical; pin one with README compare before citing. |
| 21 | awesome-claude-skills | PARTIAL (travisvn earliest 15.3k vs ComposioHQ largest 64–74k vs BehiSecc 10k vs karanb192 541) | RESOLVED as ComposioHQ + karanb192 vs `anthropics/skills` + `VoltAgent/awesome-agent-skills` | **Keep PARTIAL** — same-name/different-org ambiguity persists; Gemini adds the `VoltAgent` comparator (net-new) but drops travisvn/BehiSecc. Org qualifier still required. |

Agreed items (both RESOLVED, same canonical): OpenViking, ChatDev 2.0/DevAll, frontend-design skill, public-apis, Agent Skills standard, Astryx (modulo §4a nuance), ruflo, cookbooks (plural canonical + singular→plural 301 — net-new redirect detail), Firecrawl (mendableai→firecrawl 301 — net-new), eve, DESIGN.md convention, `anthropics/skills`.

### (d) Prompt archives — verdict: **complementary; 2 new archives + file-level census**

- `asgeirtj/system_prompts_leaks`: first pass (`E:P-01`) = 69.2k ⭐ / 11.3k forks / 777 watchers / **851 commits**, 16 vendor folders observed via README+tree, recent-additions table (Haiku 5.5 2026-10-07, Dots + Muse Spark 1.3 2026-10-05/04, Grok 4.7 2026-10-03, Fable 5.1 + GPT-6.1-Sol + Sonnet 5.5 2026-09-29/30), provenance ALLEGED-LEAK/UNVERIFIED, press claims flagged unverified. Gemini (`06:§2.1`) = created 2025-05-03, push 2026-10-09, **1264 files / 17 dirs** with per-dir counts (Anthropic 577 = claude-code 455 + official 42 + claude-design 32 + cowork 5 + old 10 + raw 6 + root 27; Meta 474 = muse-agent 389 + muse-code 83 + root 2; OpenAI 124 = Codex 35 + dots 32 + Old 15 + API 8 + root 34; Google 24; Misc 23; xAI 16; Perplexity 5; Microsoft 5; Kimi/Mistral/Qwen 2 each; Cursor/DeepSeek/GLM/Notion/Pi 1 each; root 5), 10-commit sample 2026-10-06–09, **dual provenance** (bulk alleged-leak + `Anthropic/official/` 42-file official-mirror sub-archive 2024-07-12–2026-10-07 + constitutions v1/v2). No conflict — Gemini deepens the census; adopt its tree + the official-subdir distinction, keep first-pass authenticity limits (no bodies, no bypass, verify vs vendor docs).
- NEW archives (gemini-only):
  - `LouisShark/chatgpt_system_prompt` — 2023-11-01 → push 2026-10-08, 10.8k ⭐, ~30.5 MB; `prompts/{official-product,gpts,opensource-prj}` + `GETTING_STARTED/RESOURCES/SECURITY/TOC.md`; alleged-leak/unverified (crowdsourced injections).
  - `Piebald-AI/claude-code-system-prompts` — 2025-11-18 → push 2026-10-08, 12.8k ⭐, ~6.5 MB; `system-prompts/` 900+ files (sub-agent states/hooks/tool wrappers) + `tools/`; alleged-leak/unverified (binary reverse-engineering).
- First-pass P-05–P-08 registry census (travisvn/ComposioHQ/BehiSecc/karanb192) + P-09 docs + P-10 datasets + P-11 in-repo instructions + P-12 unverified-dumps bucket have no Gemini counterpart — preserved as-is.

### (e) Design styles 29 vs 29 — verdict: **same slot list, complementary methods, no hard conflicts**

- Slot alignment holds for styles 01–20 per `D/00-index-29.md` §§29/11-20 (Minimalism → Dark-moody); Gemini taxonomy continues 21–29 (Cyberpunk, Anthropomorphic, Victorian, Cybercore, Synthwave, Graffiti, Gothic, Mixed-media, Body-art) matching first-pass filenames `21-cyberpunk.md` … `29-body-art-inspired.md` (names match; per-file bodies not re-read this session).
- Method contrast: first pass = fetch-ledger per style (fetched-200 anchors: Pico, Brutalist-Framework†EOL 2026-08-22, neobrutalism.dev v4, neumorphism.io, css.glass, clay.css, bento-grid superdesign.dev, Y2K Webflow+Wikipedia) with honest GAPs (Maximalism, Surrealism-as-CSS, Neoclassical, Scrapbook-as-code; partial 13/14/18/19). Gemini = token/pattern spec per style + shared-stack production recipes, GAPs on 8 (Maximalism, Surrealism, Neoclassical, Luxury-type, Bohemian, Victorian, Graffiti, Body-art). Use together: first pass for **verified code anchors + freshness risks**, Gemini for **implementation recipes + comparison matrix**.

## 5. Gaps still open (consolidated retry queue)

1. `vercel/deepsec` vs `vercel-labs/deepsec` — live re-check both (status + README + dates + redirect). (Highest priority — blocks citation.)
2. `PizzaBox AWS` exact string — still no name-evidence; retry exact + org-qualified + registry search.
3. Provisional pins needed (fetch README/about + dates): `D4Vinci/Scrapling`, `chaitanyagiri/munder-difflin`, `Leonxlnx/taste-skill`, `usestrix/strix`, one NotebookLM skill (`PleasePrompto` vs `sanjay3290` vs `claude-world`), backend-design convention instances.
4. `awesome-claude-skills` — retain org qualifier permanently (travisvn/ComposioHQ/BehiSecc/karanb192 + VoltAgent comparator).
5. First-pass carryovers (untouched by Gemini, still open): `okjpg/llm-council` exact URL; walkinglabs five-layer canonical page; MEDUSA `.opencode/` coverage; science-superpowers/Baton/shanraisshan OpenCode paths; Superpowers star-count dating; open GitHub issues (Python SDK #4031, statusLine #30295/#8619/#23539, marketplace #7467, plugin toggle #11743, Claude-hooks #12472); `E` follow-ups (asgeirtj per-file dates/hashes, P-09 doc versions, P-10 dataset pins, P-05–P-08 freshness).
6. Astryx remote MCP — optional adoption check only: confirm `apps/docsite/src/app/mcp/route.ts` at a pinned commit + auth/rate-limit/cost posture before use; local-build guidance unchanged.

## 6. Recommendation

1. **Adopt Gemini as breadth layer, keep first pass as build authority.** Do not merge blindly: promote Gemini's 276-resource baseline, 29-style recipes, ENFORCEABLE-vs-PROMPT-ONLY taxonomy, and archive census into reference appendices; keep all build decisions (walkinglabs sole state, loop stack, two-judge, dual commit gate, CLI-first Astryx, plugin/marketplace workarounds) on first-pass evidence.
2. **Apply adjudications:** Astryx → Corrected-nuanced (§4a); deepsec → quarantine until re-verified (§4b); 9 watchlist items → provisional/convention/pattern status per table (§4c), awesome-lists stay PARTIAL; prompt archives → adopt dual-provenance + 2 new archives (§4d).
3. **Next verification sprint (single live session):** clear retry queue items 1–3 + 6 in one pass, capture HTTP statuses + commit hashes + access dates, then fold results into `C-named-register-23.md` and `A-master-index.md` unresolved lists.
