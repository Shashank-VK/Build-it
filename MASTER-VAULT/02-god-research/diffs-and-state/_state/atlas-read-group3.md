# Atlas Read — Group 3 (9 catalog files, read to EOF, no execution)

Base: `/mnt/c/Users/Shashank Karamudi/Desktop/God research/atlas/catalogs/`
Date read: 2026-10-09 (catalog verification date in-files: 2026-10-10)
Mode: read-only, paginated to EOF. No installs/builds/executions of catalog contents.

## Totals

- Files read: 9 / 9 to EOF
- Total lines (wc -l): **17,601**
  - 01a 3215 + 01b 3585 + 01c 1887 + 02a 2427 + 02b 593 + 03a 763 + 03b 885 + 04 2846 + 05a 1400 = 17601
- EOF markers observed: 01a `(End of file - total 3215 lines)`, 01b `(End of file - total 3585 lines)`, 01c `(End of file - total 1887 lines)`, 02a `(End of file - total 2427 lines)`, 02b `(End of file - total 593 lines)`, 03a `(End of file - total 763 lines)`, 03b `*Catalog 03b-agents.md completed 2026-10-10* (885 lines)`, 04 `(End of file - total 2846 lines)`, 05a `(End of file - total 1400 lines)`.

---

## 1. 01a-languages-build.md — 3215 lines

- **Scope:** OMNISCIENT ATLAS Catalog 01a; Parts 3.1 (languages/browser tech) + 3.4 (build/compile/package). Researcher Workstream #1, subagent 7663c8a1. 35 search themes logged + 3 primary opens (rolldown, oxc, biome READMEs).
- **Resource counts (per in-file coverage note):** 155 distinct records, 19 subcategories (1.1=14, 1.2=5, 1.3=9, 1.4=15, 1.5=9, 1.6=6, 2.1=9, 2.1b=7, 2.2=6, 2.3=14, 2.4=7, 2.5=4, 2.6=12, 2.7=8, 2.8=11, 2.9=9, 2.10=4, 2.11=4, 2.12=2).
- **Verification status (in-file):** Verified 9, Partially verified 107, Unverified 39. No Archived/Historical in this file; Rye + tsup are Verified-deprecated records, Volta flagged "stood down" inside a Partially-verified record.
- **Notable new vs known passes:**
  - ES2026 approved 2026-06-30 (Temporal Stage 4, Math.sumPrecise, Array.fromAsync, JSON.rawJSON, decorators); Temporal ship claims single-sourced.
  - TypeScript 7.0 GA 2026-07-08 ("Corsa" Go port, 8–12x builds; no programmatic API in 7.0 → 7.1; 6.x "Strada" maintained); community ferrotype/tsr Rust port noted.
  - WASI 0.3.0 ratified 2026-06-11 (async in canonical ABI); 0.3.1 shipped 2026-08-11, 0.3.2 scheduled 2026-10-13; Wasm 3.0 live-standard 2025-09-17.
  - Node 24 "Krypton" Active LTS (EOL 2028-04-30), Node 26 Current→LTS 2026-10-28, yearly-majors from 27; npm 11.19+ skips install scripts by default.
  - Bun 1.4.1 (Anthropic acquisition Dec 2025, Zig→Rust rewrite experimental, Bun.SQL/Redis, Cruller Zig fork); Deno 2.7.x; Vite 8 (Mar 2026) unified on Rolldown+Rust/Oxc/Lightning CSS; tsup unmaintained→tsdown; Rye deprecated→uv; Volta stood down→mise; Corepack removed in Node 25+.
  - Dedup honored (not re-researched): facebook/astryx CLI, shadcn MCP, upstash/context7, code-yeongyu/oh-my-openagent, anomalyco/opencode, opencode.ai docs.

## 2. 01b-frontend.md — 3585 lines (largest)

- **Scope:** Researcher #2, Parts 3.2 + 3.3 (frontend frameworks/app-dev; styling/UI primitives/component systems). 16 search themes. 10 primary repo opens.
- **Resource counts (in-file coverage note):** 195 distinct entries (Part A 100, Part B 95); 190 full records + 5 cross-ref/mini (Astro-as-SSG, React Aria xref, Context7, shadcn MCP, in-repo agent surfaces).
- **Verification status (in-file):** Verified 10 (shadcn-ui/ui, mui/material-ui, zustand, TanStack/query, react, vuejs/core, storybook, tailwindcss, astro, nuxt); Partially verified 175; Historical 4 (Recoil, Gatsby, Stitches, Docz); Unresolved 4 (Slate archived-2026-02-04 claim needs primary check; Astro NOASSERTION-vs-MIT license mismatch; styled-components maintenance-mode claim; Headless UI no-release-since-Apr-2026 claim).
- **Notable new vs known passes:**
  - TanStack ecosystem breadth (Router/Start/Store/DB/Table/Virtual/Form) + in-repo AGENTS.md/AI_POLICY.md surfaces; shadcn registry model (Base UI default since Jul 2026, Radix lineage, Magic/Aceternity/Cult/Kibo/Animate/React Bits/ReUI/Tailark/21st.dev/uishelf); Origin UI→cosscom/coss AGPL relicense; Aceternity license unresolved (no public repo).
  - GSAP post-Webflow license (free incl. commercial, NOT OSI; no fork/redistribute) flagged for primary check; p5.js LGPL, BlockNote XL GPL-3.0, Remotion commercial nuance flagged.
  - Slate reported archived 2026-02-04 by one secondary (Unresolved); Gatsby declining/Historical.
  - Dedup honored: astryx, shadcn MCP, laws-of-ux-skills, awesome-design-systems, gztchan/awesome-design, awesome-design-md.

## 3. 01c-backend-data-platforms.md — 1887 lines

- **Scope:** Researcher #3, Parts 3.5–3.9 (backend frameworks/API, databases/persistence/search, app services, site platforms/generators, arch references). 30 themed searches + 3 primary opens.
- **Resource counts (in-file):** ~240 distinct (full records + table rows, dedup excluded). Per-subcategory table 3.5.1(13) through 3.9.5(3) sums to ~240.
- **Verification status (in-file):** Inspected primary 3 (nextauthjs/next-auth, bbonnin/openapi-to-mcp, TykTechnologies/api-to-mcp); Verified 3; Corrected 5; Archived 3; Partially verified ~225; Unverified 4 (§3.5.9.3–5, §3.5.9.7); Unresolved 2 (anythingmcp; §3.6.11 Astryx-for-backends gap); Historical 1 (Lucia).
- **Notable new vs known passes (corrections are the signal):**
  - Auth.js→Better Auth recommendation (next-auth README opened, Verified+Corrected); Lucia discontinued.
  - Cal.com privatized 2026-04-14 → closed-source + MIT cal.diy fork (Corrected); Stytch acquired by Twilio ($104.1M, closed 2025-11-14); Lemon Squeezy acquired by Stripe (Jul 2024)→Stripe Managed Payments; Payload CMS acquired by Figma (Jun 2025); Neon acquired by Databricks (May 2025); MongoDB Atlas App Services EOL 2025-09-30 (Archived); Optic archived Jan 2026; Dredd archived May 2024.
  - New alternatives: bbonnin/openapi-to-mcp + Tyk api-to-mcp (both Verified); Convex as closest "agent-grounded backend" + Encore infra-from-code (gap analysis: no turnkey Astryx-for-backends equivalent — Unresolved).
  - Dedup honored: openapi-mcp-codegen/ck-anthony/awslabs-openapi-mcp-server, cloudflare/composio/upstash skills.

## 4. 02a-design.md — 2427 lines

- **Scope:** Researcher #4, Part 4 + 17 (design systems/guidelines, UI/UX theory, inspiration directories, creative assets/pipelines, design-to-code, creative tech). 29 styles explicitly out of scope (separate workstream).
- **Resource counts (in-file):** 97 full records + ~95 supplementary compact mentions. Subcats: A systems 22, B theory 7, C inspiration 15, D assets 20, E design-to-code 19, F creative tech 14.
- **Verification status (in-file table):** Verified 72, Corrected 1 (Shopify Polaris React deprecated→web components current), Partially verified 23, Unresolved 1 (Supernova E13); plus Archived (BackstopJS dormant 2024), Historical (Lost Pixel joining Figma).
- **Notable new vs known passes:**
  - Polaris correction is the headline; Base UI gaps (no calendar/table/tree, Jul 2026 shadcn default); Headless UI slow since Apr 2026; GSAP custom (not OSI) license; Animate.css Hippocratic-2.1; Shadertoy CC BY-NC-SA default (non-commercial); Simple Icons CC0 + trademark caveat.
  - Login-gated limits (Mobbin, Supernova) honestly marked; Figma MCP + Dev Mode + Code Connect verified; Onlook 25.9k stars verified.
  - Dedup honored: astryx, laws-of-ux-skills, apple-design, shadcn MCP, lawsofux, awesome-design-systems, gztchan/awesome-design, awesome-design-md, react-three-fiber/start/next, M3, Apple HIG.

## 5. 02b-design-styles.md — 593 lines (smallest)

- **Scope:** Workstream #5, Part 5 — all 29 design styles, live web research, tiered confidence (file opens = high, excerpts = medium).
- **Resource counts (this read):** ~150 dedicated resources across 29 styles (tallied from section bodies); cross-style note confirms per-style dedicated-resource verdicts.
- **Verification status (this read + in-file labels):** Verified ~13 (minimal.css; maximalism trend file 445 lines; feliciatiffany collage; ekmas/neobrutalism-components 5.5k★; 19-scrapbook-collage 602 lines; papercade; Bohemian DESIGN-GUIDE; Nightwire w/ license caveat; CYBERCORE CSS sebyx07; graffiti-ui 547 lines; tattoo_flash.ink genome 306 lines; ethereal design system 567 lines; anthropomorphic SKILL 216 lines); Partially verified bulk (~125); Unverified ~6 (Brutalist Framework, Tiny Brutalism, Concrete.css, RetroUI, neobrutalism-vue, ethereal Figma file); Archived 1 (unsetbit/collage); Gaps with zero verified dedicated resources: #5 Surrealism, #23 Victorian (only `.btn-victorian` variant + commercial templates).
- **Notable new vs known passes:**
  - Strongest new systems: Nightwire (dark-only cyberpunk, license NOASSERTION-vs-MIT unresolved), CYBERCORE CSS (901-line README, MIT, +charts/svelte satellites), tattoo_flash.ink genome (full component/motion spec), ethereal design system (named atmospheres, night-sky dark mode), Bohemian arch system, graffiti-ui full token/component spec.
  - Identity caveats preserved: Classic-CSS incasedev-vs-wecoded-dev; snes.css upstream vs stale fork; AmiBlue path duplication; claymorphism tri-mirror origin unresolved; cybercore "framework brand vs aesthetic movement" split; gothic blackletter-vs-dark-ornate split; Y2K chrome-futurism vs GeoCities-amateur + Frutiger Aero succession.

## 6. 03a-skills.md — 763 lines

- **Scope:** Researcher #6, Part 6 — Agent Skills standard, official company collections, installers, validators/scanners, generators, evaluators, marketplaces.
- **Resource counts (in-file):** ~48 new resources (19 company + 4 installer entries/7 tools + 8 validator entries/11 tools + 8 generator + 8 marketplace + 4 evaluator + 6 community); 27 full Part-21 records; 11 primary READMEs + ~25 secondary snippets inspected.
- **Verification status (in-file):** Verified 11 (agent-skills standard xref, vercel-labs/agent-skills, skills CLI, getsentry/skills, huggingface/skills, stripe/ai, trailofbits/skills, microsoft/skills, netlify/context-and-tools, supabase/agent-skills, figma/mcp-server-guide README-level); Partially verified ~30; Unresolved 2 (skills-ref Neon CI validator, EverMind-AI/SkillCorpus).
- **Notable new vs known passes:**
  - Anchor_preferred installer: `npx skills` (vercel-labs/skills, 33.5k★, ~80 agents) + 4-way skillkit disambiguation (rohitg00/alex-1q84/rfxlamia/saanjaypatil78); `hf skills` CLI (only vendor CLI that generates its own skill + marketplace).
  - Official suites newlyindepth: Vercel 8 skills, Sentry ~30 + skill-writer/scanner, Expo 12, HF ~28, Stripe best-practices, Trail of Bits ~50 plugins (CC-BY-SA-4.0), Microsoft 174–175 skills (warns "context rot"), Figma 7 canvas-operator skills (seat-gated MCP), Netlify 15 + hosted manifest w/ SHA-256, Supabase 2 + .well-known, Neon branches/egress-optimizer, ClickHouse chdb, HashiCorp lifecycle-status metadata, Better Auth 6, LambdaTest 15, Capgo 49, OpenAI legacy-vs-plugins split, Anthropic gallery + knowledge-work-plugins.
  - Security spine: AIR TOCTOU incident (brand-landingpage cleared scanners via mutable URL) + 8 scanner entries (Cisco/francoischastel/husk/skillscanner/Sentry/snyk/etc.); skill-factory tuning loop (29%→81% detection).

## 7. 03b-agents.md — 885 lines

- **Scope:** Researcher #7, Part 8 — coding agents, plugins, dev environments. OpenCode + Claude hooks deduped by design.
- **Resource counts (in-file):** 17 records (15 full + VS Code marketplace host + Kimi legacy alias) + 5 emerging medium-depth (Qwen, Crush, Kilo, Goose, Continue) + 12 brief mentions (Grok/Reasonix/Deep Agents/Codebuff/MiniMax/Mistral Vibe/MiMo/Open Interpreter/SWE-agent/Roomote/ZCode/OH-MY-PI).
- **Verification status (in-file):** High/Verified 8, Partially verified 9, Historical 2 (Gemini CLI, Kimi CLI legacy), Unverified 17 (mostly brief mentions), Unresolved 4 (Amp editor status; Pi Rust-rewrite relation; Crush license MIT-vs-FSL; `~/.cursor/commands` path).
- **Notable new vs known passes:**
  - Gemini CLI dead for consumers (I/O 2026-05-19 → Antigravity `agy` Go CLI, serving ended 2026-06-18); Windsurf→Devin Desktop (`.devin/rules/` preferred); Kimi CLI→Kimi Code CLI (`kimi.plugin.json`); Qwen Code fork of Gemini CLI v0.8.2 chasing Claude parity.
  - Convergence finding: SKILL.md/hooks/MCP/AGENTS.md near-universal; differentiators are distribution (marketplace vs git-clone vs none) + subagent authoring (files vs auto-spawn vs modes); Claude-compat shims as de-facto interop (Copilot/Cursor/Kimi/Factory/Cline-Roo); ACP emerging as editor-embedding standard.
  - Compatibility matrix (17 cols × agents) is the densest new artifact in this file.

## 8. 04-mcp.md — 2846 lines

- **Scope:** Workstream #8, Part 7 — MCP spec/governance, SDKs, reference servers, vendor integrations, registries, community servers, frameworks/inspection/security/config, clients, adapters, web-dev composite, MCP alternatives.
- **Resource counts (in-file):** 82 records (1–82) + 12 archived reference servers note + 2–8 sub-projects inside Records 5/32/33/34/53/58/62. Sections: spec/gov 2, SDKs 3 (10 langs), ref servers 7+12 archived, vendor 12 (1 dedup), registries 10 (~20 named dirs), community functional 21, dev/security/config 11, clients 1 (~15 hosts), adapters 4, web-dev composite 1, alternatives 10.
- **Verification status (in-file):** Verified ~14, Partially verified ~50, Entry-level/low ~18, Archived 12 (AWS KB, Brave Search→brave org, EverArt, GitHub→github org, GitLab, Drive, Maps, Postgres, Puppeteer, Redis, Sentry→Zencoder, SQLite). "No record presented above its evidence."
- **Notable new vs known passes:**
  - Spec 2025-11-25 Final (OIDC discovery, incremental scope, icons, sampling tool-calling, Client ID Metadata Docs, Tasks exp., JSON Schema 2020-12) + 2026-07-28 revision (no stateful handshake); AAIF donated 2025-12-09 (MCP+AGENTS.md+goose, 49→250+ members), A2A joined 2026-08-17/20, MCP Apps extension shipped 2026-01-26.
  - Registry sizes point-in-time: official ~9.6K, mcp.so ~20–23K, Glama ~33–50K w/ A–F grades + gateway, Smithery ~6–7.3K (monetization terms disputed), MCPFind ~13.9K (live-pruning), luciferforge scraper 18,146.
  - Safety-critical: Filesystem high-risk, Git medium, Stripe live-mode financial writes, K8s/Docker socket max-risk, Inspector CVE-2025-49596 (`DANGEROUSLY_OMIT_AUTH`), Snyk Agent Scan (ex-mcp-scan) 15+ risk cats + 5.5% poisoning stat (single-source caveat).
  - New server finds: qore-mcp read-only (Verified, Apache-2.0), Mimir AES-256-GCM, Servex offline, FastMCP v3 (~70% claim), Inspector v2 (Web+CLI+TUI).

## 9. 05a-orchestration.md — 1400 lines

- **Scope:** Workstream #9, Parts 9+10 (multi-agent/orchestration + harness engineering/autonomous dev). 15+ thematic queries, 5 primary opens.
- **Resource counts (in-file):** 57 total (55 full + 2 xref). Frameworks 16, protocols 8+1 xref, harnesses 16+1 xref, benchmarks 8, telemetry 7.
- **Verification status (in-file):** Verified 26, Partially verified 24, Historical 2 (OpenAI Swarm, Tessl pivoted), Archived 1 (IBM ACP merged into A2A Aug 2025), Unresolved 2 (Hermes Agent single-source/167k★ implausible; SpecWeave single-source).
- **Notable new vs known passes:**
  - AutoGen maintenance-mode banner (verbatim, ~2025-10-02, use Microsoft Agent Framework) + AG2 fork owns `autogen` PyPI; MAF 1.0 PyPI 2026-04-02; MetaGPT org geekan→FoundationAgents (quiet since Jan 2026, MGX commercial focus).
  - New harness: Munder Difflin GOD orchestrator (PTY-isolated CLI riding, worktrees, blackboard/mailboxes, memory palace); Spec Kit v1.1.0 (140k★, 30+ agents, /speckit-* skills); OpenSpec propose→apply→archive; SpecWeave evidence ledger; Kiro GA Nov 2025 (replaced Q Developer, EARS specs); SWE-agent superseded by mini-SWE-agent (~100-line 65% Verified); EnIGMA CTF mode; Terminal-Bench Harbor runner (harness ±7pt swings); SWE-bench Pro 1,865 tasks/4 langs + Live anti-contamination + SWE-rebench V2 arXiv:2602.23866.
  - Protocol disambiguation: 4 different "ACP"s (IBM archived vs Zed editor vs Commerce OpenAI/Stripe live 2026-02-16 vs AGNTCY archived) + AP2 (A2A payments extension) + AG-UI v1.0 2026-09-30 + ANP/W3C CG drafts.

---

## Method note

Each file was read in sequential offset windows to its stated EOF (see per-file line totals above). Verification/resource numbers are those asserted in each file's own coverage note, spot-checked against section bodies during the read (e.g., 02b tallied to ~150 from bodies; 03b/04/05a section enumerations match their coverage tables). License fields marked "not re-verified / verify per file" in-source are preserved as such — no legal interpretation added.
