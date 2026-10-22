# Search Coverage Register

**Maintained by:** Atlas coordinator | **Last updated:** 2026-10-10 | **All 15 workstreams COMPLETE**

**Grand totals:** 1,210 canonical index records (1,281 raw, 71 duplicates folded) + Phase 0 base (~200 names). Verification mix (index-wide): 914 Verified / 141 Partially verified / 29 Unverified / 8 Historical / 8 Unresolved / 3 Corrected / 3 Archived / 104 Not labeled (record carried no explicit label; see source catalog).

| # | Workstream | Output file | Status | Resources | Notes |
|---|---|---|---|---|---|
| 0 | Phase 0 inventory | index/phase0-inventory.md | Done | ~200+ names | All files in ~/workspace/user/files/ read; 16 corrections preserved; 10 gaps; 8 open questions |
| 1 | Languages, browser tech, build tooling | catalogs/01a-languages-build.md | **Done** | 155 | 9 Verified / 107 Partially / 39 Unverified; key 2026 findings: ES2026 approved 2026-06-30 (Temporal Stage 4); TS 7.0 GA 2026-07-08 (Go port, 8–12×); WASI 0.3 ratified 2026-06-11; Vite 8 (Mar 2026, Rolldown+Oxc); tsup→tsdown; Rye→uv; Volta→mise; pnpm 10/11 blocks build scripts by default; npm 11.19 skips install scripts |
| 2 | Frontend frameworks, styling, components | catalogs/01b-frontend.md | **Done** | 195 | 190 full records + 5 cross-refs; 10 Verified / 175 Partially / 4 Historical / 1 Unresolved (+10 unresolved sub-items incl. Slate archive, GSAP terms, licenses); A1–A16 + B1–B17 subcategories; dedup honored |
| 3 | Backend/APIs, databases, services, generators, architecture refs | catalogs/01c-backend-data-platforms.md | **Done** | ~240 | 3 Verified (primary) / ~225 Partially / 4 Unverified / 2 Unresolved / 1 Historical; 5 Corrected (Cal.com closed-source + cal.diy fork; Stytch→Twilio; Lemon Squeezy→Stripe; Payload CMS→Figma; Auth.js→Better Auth); 3 Archived (Atlas App Services EOL 2025-09-30, Optic, Dredd); Astryx-backend gap still Unresolved (candidates: Convex, Encore, Hastry metadata) |
| 4 | Design systems, UX theory, inspiration, assets, design-to-code, creative tech | catalogs/02a-design.md | **Done** | 97 full + ~95 compact mentions | 72 Verified / 23 Partially / 1 Corrected (Polaris React deprecated → web components) / 1 Unresolved (Supernova); 1 Archived (BackstopJS); 1 Historical (Lost Pixel); dedup honored |
| 5 | All 29 design styles | catalogs/02b-design-styles.md | **Done** | 29 styles, ~60 resources | 2 style gaps: Surrealism (0 interface resources), Victorian (only .btn-victorian + commercial fonts); per-style counts 0–11; unresolved: classic-css ownership, NES.css mirror, snes.css upstream, tattoo-studio repos need live-browser re-open |
| 6 | Skills ecosystem | catalogs/03a-skills.md | **Done** | ~48 new | 11 Verified / ~30 Partially / 2 Unresolved; 19 official company collections; dedup honored |
| 7 | Coding agents & extensions | catalogs/03b-agents.md | **Done** | 34 | 15 named agents; 8 Verified/9 Partially/2 Historical/17 Unverified mentions/4 Unresolved; Gemini CLI folded into Antigravity CLI (agy); Windsurf Cascade now Devin Desktop; Kimi CLI = alias of Kimi Code CLI |
| 8 | MCP servers + interop alternatives | catalogs/04-mcp.md | **Done** | 82 + ~30 sub-records | ~14 Verified/~50 Partially/~18 entry-level; spec, SDKs (10 langs), official servers, 12 vendor integrations, 10 registries, 21 functional servers, dev/debug/security tooling, 10 MCP alternatives; CVE-2025-49596 (MCP Inspector v2) noted |
| 9 | Multi-agent + orchestration + harness + autonomous dev | catalogs/05a-orchestration.md | **Done** | 57 | 26 Verified / 24 Partially / 2 Historical / 1 Archived / 2 Unresolved; AutoGen→AG2/MAF successor chain confirmed |
| 10 | Context/memory/codebase intelligence | catalogs/05b-context.md | **Done** | 58 | 29 context/memory + 18 repo intelligence + 11 doc grounding; 3 Verified (primary: Mem0, Graphiti, Serena) / 52 Partially / 2 Archived (Bloop, Sourcetrail) / 1 Historical (Cody); license correction: Serena is GPL-3.0 (not MIT) |
| 11 | Scraping/crawling/research + public APIs | catalogs/06a-data-acquisition.md | **Done** | 111 | 90 full records + 21 compact; 68 data-acquisition / 25 API directories / 18 research-ingestion; corrections: Docling→docling-project, Gitingest→coderamp-labs, ScrapingBee→Oxylabs (Jan 2026), ReqRes keyless rejection (2026); 8 Unverified need primary passes |
| 12 | Testing/QA + security/sandboxing | catalogs/06b-quality.md | **Done** | 119 | 75 testing/QA + 44 security/safety across 34 subcategories; corrections: pa11y LGPL-3.0-only; mcp-scan→Snyk Agent Scan rename; Gitpod→Ona (OpenAI, Classic sunset 2026-10-15); incident: CVE-2026-33634 Trivy action hijack (2026-03-19); CVE-2026-80521 kernel container-escape (2026-09-22); gaps: R-60 Cover-Agent Unverified; S-25 incidents 2–5 secondary-only |
| 13 | CI/CD/cloud/infra + SEO/analytics/CMS/commerce | catalogs/06c-operations.md | **Done** | ~337 | 297 full records + ~40 compact across 44 subcategories; 2026 corrections: Deno team→Cloudflare (Deploy sunsets ~Apr 2027); Langfuse→ClickHouse; Statsig→OpenAI→Amplitude; Intercom rebranded Fin (Salesforce pending); Railway/Koyeb free tiers removed; Mixpanel Nov 2025 breach; unresolved: Xata status, Gitpod 2026 direction, Directus license (BSL 1.1) |
| 14 | Named watchlist (23 items) | registers/named-watchlist.md | **Done** | 23 | 18 Verified / 1 Corrected / 2 Partially / 2 Unresolved |
| 15 | Prompt archives | registers/prompt-archives.md | **Done** | 19 | Existence 18 Verified/1 Partially; authenticity 6 Verified/3 Partially/9 Unverified/1 N/A |

## Cross-workstream items to reconcile at final assembly

- OpenCode sandbox contradiction (C5): workstream 12 should provide evidence; mark outcome.
- Output-styles gap (C6): workstream 7 should note any style-switcher plugins.
- Official SDK identity (C7): workstream 13 should clarify @opencode-ai/sdk vs anomalyco repos.
- gstack status (C8): workstream 6 noted Claude-Code-primary evidence; workstream 7 should check current state.
- vercel/deepsec → vercel-labs/deepsec (C14): workstream 12 should record corrected org.
- Backend Astryx equivalent (gap): workstream 3 to confirm/refute.
- "Designs" + backend design skill (unresolved): workstreams 6/14 note as unresolved.
- NotebookLM skill: workstream 14 found stefandsl/notebooklm-skill — workstream 10 may cross-ref for memory context.
- Munder Difflin: workstream 9 recorded as harness find; workstream 14 recorded as watchlist item — dedupe to one canonical record at assembly.
- Serena license: GPL-3.0-or-later (workstream 10, primary read 2026-10-10), not MIT — override any secondary MIT claims in final assembly.
