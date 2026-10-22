# Atlas Read — Group 2 (C, D, E, F, G, H, I, index/master-index)

Read date: 2026-10-10 (UTC 2026-10-09). Method: full paginated reads to EOF, no execution.
Base: `/mnt/c/Users/Shashank Karamudi/Desktop/God research/atlas/`
Line counts via `wc -l`; EOF markers confirmed on every file ("(End of file - total N lines)" present in D, E, F, G, H, I, master-index; C ends at line 433 with "Alternative Strix candidates" bullet, no EOF marker line but `wc -l` = 433 and final chunk returned lines 348–433).

## Line counts (all 8)

| File | Lines | Bytes (approx) | Pages read |
|---|---|---|---|
| C-named-watchlist.md | 433 | ~60 KB | 1–347, 348–433 |
| D-design-styles.md | 678 | ~182 KB | 1–211, 212–366, 367–561, 562–678 |
| E-prompt-archives.md | 446 | ~61 KB | 1–356, 357–446 |
| F-compatibility-index.md | 99 | ~11.5 KB | 1–99 (single) |
| G-relationship-index.md | 70 | ~8.3 KB | 1–70 (single) |
| H-verification-register.md | 136 | ~11.4 KB | 1–136 (single) |
| I-coverage-register.md | 59 | ~9.5 KB | 1–59 (single) |
| index/master-index.md | 1433 | 346,502 (~340K) | 1–232, 233–424, 425–606, 607–810, 811–1074, 1075–1287, 1288–1433 |
| **Total** | **3353** | — | — |

Master-index status-cell audit (grep `| <label> |`): Verified 914 · Partially verified 141 · Not labeled 104 · Unverified 29 · Historical 8 · Unresolved 8 · Corrected 3 · Archived 3 = 1210. Matches header claim exactly (line 3, line 8).

---

## C — Named-Resource Investigation Register (433 lines, Part 19)

Stated totals (line 6, repeated line 413): **18 Verified · 1 Corrected · 2 Partially verified · 2 Unresolved (of 23)**.
String occurrences: "Verified" 38 · "Partially verified" 6 · "Unresolved" 6 · "Corrected" 5 · "Unverified" 0.

- 23 numbered items §§1–23 + Summary table (lines 387–411) + "Key corrections" (415–422) + "New leads" (424–432).
- Statuses per summary table: Verified ×18 (#1,3,4,5,6,9,10,11,12,13,14,15,17,18,20,21,22,23); Corrected ×1 (#2 PizzaBox→Pizza Bot); Partially verified ×2 (#7 Frontend design skill — canonical candidate anthropics/skills `frontend-design`, verified only via mirrors; #19 Strix — usestrix/strix primary candidate + 3 alternatives, not claimed as intended); Unresolved ×2 (#8 Backend design skill — 5 author-specific candidates, no canonical match; #16 "Designs" — bare name, no match).
- Preserved corrections (line 8): ruvnet/ruflo (ex-Claude Flow) · emilkowalski/skills · teng-lin/notebooklm-py (unofficial) · ngmeyer/council-review LIVE · Loop-Engineering vs LoopBench separate · open-gsd/gsd-core safe fork (gsd-build archived June 2026) · okjpg/llm-council not found · Karim Shoair (not "Krim") · vercel-labs/deepsec (not vercel/deepsec) · Pizza Bot (not "PizzaBox") · affaan-m/ECC name retired · Astryx NO MCP server.
- DeepSec claim (§12, lines 189–201): org corrected to **vercel-labs/deepsec**; Vercel Labs agent-powered vuln scanner; TS CLI `npx deepsec init`; static pre-scan → agent investigate (Claude Opus 4.7 / GPT 5.5 max reasoning) → revalidate → git enrichment → ticket export; cost warning (thousands–tens of thousands $ on large repos); Verified.
- Astryx claim (§11, lines 173–185): facebook/astryx, Meta design system, 150+ React 19 components, StyleX-authored, 7 themes; agent surface = **CLI bash calls only, NO MCP server** (prior correction re-confirmed 2026-10-10; `--dense` flag carried over, not re-verified); Verified.
- asgeirtj provenance: NOT in C (cross-referenced; lives in E/R5).
- NotebookLM (§23): distinct skill stefandsl/notebooklm-skill (RoboNuggets) built on teng-lin/notebooklm-py (unofficial RPC reverse-engineering, breakage risk); Verified.

## D — Design-Style Directory (678 lines, Part 5, all 29 styles)

At-a-glance table (lines 8–38): covered ×25 (incl. Body-art PARTIAL) · GAP ×1 (Surrealism, 0 resources) · THIN ×2 (Bohemian 2 resources; Victorian 1 component class + commercial fonts) · PARTIAL ×1 (Body-art, 11 tattoo-studio repos needing live-browser re-verification).
String occurrences: "Verified" 15 · "Partially verified" 133 · "Unverified" 6 · "Unresolved" 3 · "Corrected" 2 · "Label:" 152.
Fully-opened files (high confidence): growthaudit maximalism.md (445 lines), feliciatiffany maximalism-collages README, andriusgodeliauskas 19-scrapbook-collage SKILL.md (602 lines), ekmas/neobrutalism-components README, incasedev/classic-css README (1240 lines), anandparth/papercade README (363 lines), jaredcosulich ethereal.md (567 lines, lines 0–487 read), utkarsh7106 anthropomorphic SKILL.md (216 lines), jeanclawdvandayum graffiti-ui SKILL.md (547 lines), oshtz/motif tattoo_flash.ink genome (306 lines), sebyx07/cybercore-css README (901 lines), cativo23/nightwire README.

- 29-style gaps: #5 Surrealism (0 dedicated interface resources — art-direction only, Design+Encyclopedia refs only); #23 Victorian (only `.btn-victorian` + commercial fonts, no design system); #19 Bohemian (2 resources, no component system); #29 Body-art PARTIAL (1 verified genome + 10 studio repos via search excerpts, index URLs unavailable — needs live-browser re-verification).
- Unresolved sub-items carried: classic-css ownership (incasedev vs @wecoded-dev); NES.css maintenance; snes.css upstream (dmattox10 vs devMiguelCarrero, seanwinslow28 stale fork); AmiBlue duplicate paths (makalin/AmiBlue vs makalin/amiblue); Skeci UI naming (repo sketchy-ui vs CLI skeci-ui); cybercore-css mirror (nordevelopment); Nightwire license (NOASSERTION vs MIT claim); clay.css canonical repo not opened; claymorphism SKILL canonical origin; swiss-design canonical origin; diary-scrapbook notes duplication (two jiawei248 repos).
- Confusable pairs kept separate with source terminology: Cyberpunk vs Cybercore vs Synthwave; Brutalism vs Neo-brutalism; Gothic (blackletter vs dark-ornate conflation noted) vs Victorian vs Dark-moody.
- Cross-style note (lines 640–676): styles with zero verified dedicated resources = #5 Surrealism, #23 Victorian only.

## E — Prompt Archive Directory (446 lines, Part 18, R1–R19)

Stated totals (line 8; repeated line 430): **19 records. Existence: 18 Verified / 1 Partially verified. Authenticity: 6 Verified (officially published) / 3 Partially verified / 9 Unverified / 1 N/A (tool).**
Authenticity table (lines 408–428): R1 Verified (partial disclosure) · R2 Verified (stale HEAD 2025-11-17) · R3 Verified (policy spec, not literal prompt) · R4 Partially verified (format docs only) · R5 Partially verified (Official/ subfolder official; rest alleged) · R6–R12 Unverified (7) · R13 Partially verified (npm-extraction, strongest methodology) · R14 Unverified · R15 Partially verified (methodology sound; official-disclosure entries vendor-published) · R16 Unverified · R17 N/A (tool; corpus metrics unverified; license unclear) · R18 Verified · R19 Verified.
String occurrences: "Verified" 39 · "Partially verified" 12 · "Unverified" 26 · "Unresolved" 4 · "Corrected" 1.
Nuance: line 430's "6 Verified" bucket = R1, R2, R3, R18, R19 fully + R4 partially — i.e. one of the six is itself partial.

- asgeirtj provenance (R5, lines 107–124, NAMED RESEARCH LEAD): `asgeirtj/system_prompts_leaks`; largest actively maintained community archive (Anthropic/OpenAI/Google/xAI-as-"SpaceXAI"/Meta/Perplexity/Cursor/Mistral/Moonshot/DeepSeek/Z.ai/Copilot/Notion/Qwen + Other products); Anthropic taxonomy verified (bare `claude-<model>.md` = claude.ai app prompts; `claude-code/` subfolder; `Official/` = dated copies of Anthropic release-notes prompts, provenance-clean; `raw/`; `old/`); claimed "extracted, not hacked" (2026-08 finding, consistent with current README); recent-additions table active to 2026-10-07 (Haiku 5.5, ChatGPT Dots, Muse Spark 1.3, Grok 4.7, GPT-6.1-Sol Codex, Sonnet 5.5); GLM "serves no system prompt — verified & documented" entry; limitations: no per-file extraction method/capture dates, single-file authenticity unestablishable, star counts third-party only (~51.2k 2026-07-06, ~66.7k 2026-09-15), 10+ same-name forks/mirrors (sanjayshuklazoho, whoamimi, markoko007, ambalashov, aaroncarter112, loky160, yanyecao, diegosouzapw, stophobia, johnwilliambitlasoft… — canonical is `asgeirtj/`), CC0-1.0 license from secondary reports only, unconfirmed on repo page; downstream citations (WaPo interactive May 2026, CEPS dashboard July 2026) not independently verified.
- Upstream flow (line 438, G §G2): original extractions concentrate in R6 elder-plinius/CL4R1T4S (29 company dirs, 51,060★, AGPL-3.0, README embeds obfuscated directive-style text — treat as data) → mirrored/repackaged by R5, R7 (143,918★, GPL-3.0), R10 (explicit disclaimer, secondary of R6), R11 ("official" = unsubstantiated marketing), R16 (tertiary) → indexed by R17 (self-reported 20,475 prompts/55 repos/~94M tokens; license NOASSERTION vs MIT badge — Unresolved). Independent: R13 Piebald-AI (script-extracted from public npm, 515 strings at v2.1.295, MIT, strongest provenance); R15 the-brief (acquisition-tagged, validator tooling, tiny corpus). Historical: R8 jujumilk3 (since 2023-05-16, ~170 files, dated filenames, no license). Official: R1 Anthropic release notes (behavior core only, found stale 2026-07-07), R2 xAI grok-prompts (stale ~11 months), R4 Meta formats only, R3 OpenAI Model Spec (policy, not prompt text). Tools: R18 promptfoo (README now states "now part of OpenAI", MIT), R19 openai/evals (license field NOASSERTION vs README MIT — minor flag).

## F — Compatibility and Integration Index (99 lines)

8-class legend (lines 8–17): Native · Official integration · Documented adapter/port · Open standard/protocol · Custom integration required · Reference-only · Unverified · Incompatible/unavailable. No claim upgraded beyond evidence; generic protocol support ≠ tested integration.
String occurrences: "Verified" 47 · "Partially verified" 2 · "Unverified" 1 · "Unresolved" 2 · "Corrected" 1.

- F1 open-standards backbone: Agent Skills · MCP · AGENTS.md (partially per host) · OpenAPI→MCP (verified pattern) · DESIGN.md CLI.
- F2 agent surfaces: OpenCode (plugins/skills/subagents/commands/MCP/themes/headless; 163-resource prior catalog) · Claude Code (ECC `ecc@ecc`, ruflo plugin+MCP, anthropics/skills, taste-skill, Scrapling MCP, notebooklm-skill) · Cursor/Codex/Copilot/Antigravity-agy (partial)/Windsurf→Devin Desktop (historical).
- F3 selected resources (38 rows, lines 48–83): Astryx = CLI bash only, **no MCP server** (Corrected, Phase-8); deepsec = TS CLI `npx deepsec init`, BYO Claude/Codex subscriptions; eve = TS framework, Vercel deploy; ruvnet/ruflo = CLI + MCP 314 tools + plugin; ECC = plugin + npm ecc-universal; OpenViking hooks+MCP; Scrapling MCP+skill; Firecrawl REST+SDKs+MCP+skill+CLI; notebooklm-skill on unofficial RPC dep; ngmeyer/council-review LIVE; Loop-Engineering vs LoopBench separate; open-gsd/gsd-core safe fork.
- F4 explicit non-integrations: Astryx↔MCP (none) · eve↔OpenCode (reference-only) · n8n↔OpenCode (no official import) · Antigravity DOM↔OpenCode (no native link).
- F5 needs-more-evidence: garrytan/gstack × OpenCode (mixed — Unresolved) · Windsurf post-rebrand surface · agy plugin/skill details · Factory Droid/Qwen/Pi internals (secondary only) · Xata status (Unresolved).

## G — Resource Relationship Index (70 lines)

No verification-label strings (relationship ledger, evidence column per row).

- G1 renames/successors (30 rows, lines 10–38): Claude Flow→ruvnet/ruflo · gsd-build→open-gsd/gsd-core (archived June 2026) · "Everything Claude Code"→affaan-m/ECC (3 non-interchangeable ids) · Gemini CLI→Antigravity agy (sunset 2026-06-18) · Windsurf/Cascade→Devin Desktop · Kimi CLI→Kimi Code CLI · Gitpod→Ona (OpenAI, Classic sunset 2026-10-15) · AutoGen→AG2/MAF · ACP→A2A · vercel/deepsec→vercel-labs/deepsec · tsup→tsdown · Rye→uv · Volta→mise · mcp-scan→Snyk Agent Scan · DCP→"Sleev" · DS4SD→docling-project · Scrapinghub→Zyte · ScrapingBee→Oxylabs · Cal.com→cal.diy (closed-source 2026-04-14) · Auth.js→Better Auth · Stytch→Twilio · Lemon Squeezy→Stripe · Payload CMS→Figma · Langfuse→ClickHouse · Statsig→OpenAI→Amplitude · Intercom→Fin · Deno team→Cloudflare · Lost Pixel→Figma · promptfoo→OpenAI.
- G2 companions/dependencies (16 bullets): Agent Skills chain (spec→site→reference impl→vendor repos→CLIs→validators→marketplaces) · anthropics frontend-design mirrors · ngmeyer parallel repos · Loop-Engineering vs LoopBench · notebooklm-py→notebooklm-skill · Astryx npm packages (CLI-only agent surface) · shadcn MCP official+community · OpenAPI→MCP DIY pattern · design.md→awesome-design-md→getdesign.md + consumer skills · prompt-archive upstream flow (R6→R5/R7/R10/R11/R16→R17; R5 Official/ provenance-clean; R13 independent npm-extraction; R15 tagged) · Munder Difflin canonical jeffreycayao + forks · Pizza Bot community project · Taste Skill→TasteCode · OpenCode prior-catalog cross-refs · Firecrawl repo→service/self-host/MCP/CLI/skills.
- G3 collisions NOT relationships (8 rows): alibaba vs spencermarx open-code-review · Leonxlnx vs sprungundlandung/lamwon taste-skill · 4× Strix · ComposioHQ vs 5 same-name awesome-claude-skills · jbeck018/agents-opencode (misleading, actually Claude fork) · changedetection.io forks · Gitingest forks · Serena license (GPL-3.0 primary read wins).

## H — Verification and Discrepancy Register (136 lines)

H1 unverified names (15 rows): okjpg/llm-council (no repo; voice-to-text suspected) · "Designs" (#16) · "Backend design skill" (#8, 5 candidates) · taste-skill variants · Strix (primary candidate usestrix/strix, Partially) · Frontend design skill (Partially, mirrors only) · R-60 Cover-Agent · Baton/tutti/opengoat · K-Dense-AI · leohuang8688 · Nia/Deepcon metric claims · labac-dev metadata (Unresolved).
H2 corrected identities (13 rows): ruflo→ruvnet/ruflo · enilkowaski→emilkowalski/skills · Krim→Karim Shoair · PizzaBox→Pizza Bot · Everything Claude Code→affaan-m/ECC · vercel/deepsec→vercel-labs/deepsec · "Astryx MCP"→WRONG (CLI only) · claude-fable-5.md path (Anthropic/ subfolder) · Gitingest→coderamp-labs · Docling→docling-project · changedetection.io→dgtlmoon · mcp-scan→Snyk Agent Scan · Serena→GPL-3.0-or-later.
H3 preserved contradictions (5 + 2 additional): OpenCode sandbox (no-sandbox vs native bwrap/gVisor/Firecracker/Seatbelt) · Output styles (8 themes vs genuine gap, #5199 open) · SDK identity (@opencode-ai/sdk vs anomalyco/*) · gstack status (mixed) · #30295 open vs Closed · Smithery monetization · backend-Astryx gap (candidates Convex/Encore/Hasura-Atlas).
H4 misleading URLs/names · H5 discontinued/archived/unsafe (19 rows incl. gsd-build SECURITY WARNING, Gemini CLI sunset, AutoGen maintenance, Deno Deploy ~Apr 2027) · H6 shaky claims (thekishandev "official", x1xhlol "largest", prompt-hub 1,627, promptograph 20,475, grok-prompts "regularly updated" vs 2025-11-17 HEAD, Anthropic page staleness, Designs/backend-skill) · H7 license discrepancies (9 rows: Serena GPL, pa11y LGPL-3.0-only, promptograph/nightwire/Astro unresolved, Directus BSL, Xata conflict, openai/evals minor, grok-prompts/OpenViking/Firecrawl AGPL-3.0, jujumilk3 no license) · H8 security incidents (CVE-2026-33634 trivy-action hijack, CVE-2026-80521 container-escape, CVE-2025-49596 MCP Inspector, axios hijack, Mixpanel breach, gsd-build) · H9 incomplete compat claims · H10 research limitations (URL≠maintenance, README≠proof, protocol≠integration, stars point-in-time, text-fetch only, no prompt bodies by design).

## I — Search Coverage Register (59 lines)

Grand totals (lines 6, 11): two wordings — L6: "1,152 canonical directory rows in Deliverable A (1,210 raw index records, 71 duplicates folded, 58 meta rows removed) + Phase-0 base (~200)"; L11: "1,210 canonical index records (1,281 raw, 71 duplicates folded) + Phase 0 base". Verification mix (index-wide): 914 Verified / 141 Partially verified / 29 Unverified / 8 Historical / 8 Unresolved / 3 Corrected / 3 Archived / 104 Not labeled — matches master-index header and audited cell counts exactly.
Workstream table (lines 15–30, 16 rows: Phase 0 + workstreams 1–15): 01a 155 · 01b 195 · 01c ~240 (verification-debt #1: catalog actually parses to 303 rows incl. overlap — treat 303 as authoritative) · 02a 97+~95 · 02b 29 styles/~60 · 03a ~48 · 03b 34 · 04 82+~30 · 05a 57 · 05b 58 · 06a 111 · 06b 119 · 06c ~337 · watchlist 23 (18/1/2/2) · prompt-archives 19 (existence 18/1; authenticity 6/3/9/1).
Cross-workstream reconcile list (lines 34–43): sandbox, output-styles, SDK identity, gstack, deepsec org, backend-Astryx gap, Designs/backend-skill unresolved, notebooklm cross-ref, Munder Difflin dedupe, Serena GPL override.
Verification debt (lines 48–58, 12 items): 01c count · 03b depth (~17 agents brief) · 06a/06c compact mentions · 01b 10 sub-items · prompt-archives 6 follow-ups (R1 entry list, R5 license, R12 stats, R17 license, HF datasets, Fable 5.1/Opus 5.5 check) · watchlist 4 resolutions (Designs, backend-skill, Strix, notebooklm-py liveness, anthropics frontend-design canonical check) · H3 contradictions · backend-Astryx re-run · 104 Not-labeled spot-check · license flags · Xata/Gitpod/Smithery conflicts.

## index/master-index.md (1433 lines, 1210 canonical records)

Header (lines 1–8): built 2026-10-10; 1210 canonical (71 duplicates folded); sources catalogs/*.md (13) + registers + phase0-inventory; label conventions incl. Confidence High/Medium/Low → Verified/Partially/ Unverified mapping; Not labeled = no explicit label.
Sections (43, in file order): Agent skills (29) · Build/CI/cloud/ops (48) · Coding agents (28) · Context/memory (57) · Backend/data/platforms (85) · Frontend frameworks (192) · Languages/browser/build (169) · Data acquisition & APIs (89) · 29 per-style sections — Anthropomorphic (4), Bento (5), Body-art (11), Bohemian (2), Brutalism (5), Claymorphism (3), Sketch (6), Cybercore (4), Cyberpunk (6), Dark moody (5), Editorial (4), Ethereal (4), Glassmorphism (5), Gothic (2), Graffiti (4), Luxury (5), Maximalism (6), Minimalism (4), Mixed-media (6), Neo-brutalism (10), Neoclassical (3), Neumorphism (5), Pixel art (7), Scrapbook (5), Surrealism (2), Swiss (5), Synthwave (4), Victorian (1), Y2K (4) · Design systems/assets/design-to-code (88) · MCP & interop (87) · Multi-agent/orchestration (54) · Named watchlist Part 19 (22) · Prompt archives (19) · Testing/QA/security (106).
Per-style row counts sum to 131; all 29 styles present; thinnest: Victorian 1 (commercial templates only), Surrealism 2 (encyclopedia + gap record), Bohemian 2, Gothic 2.

---

## Conflicts and discrepancies (cross-file)

1. Watchlist resolutions vs UNRESOLVED: C resolves 21/23 (18 Verified + 1 Corrected + 2 Partially verified); the 2 UNRESOLVED are #8 Backend design skill (5 candidates, H-H1/H2 watch) and #16 "Designs" (no match). The 2 Partially verified (#7 frontend-design via mirrors only; #19 Strix candidate-not-claim) are one canonical-tree check and one identity decision away from resolution — both listed in I debt #7.
2. asgeirtj provenance: E-R5 splits it — `Anthropic/Official/` subfolder is provenance-clean (dated copies of Anthropic's own release-notes page); everything else is alleged extraction with no per-file method, so single-file authenticity is Unverified. 10+ same-name forks risk stale/tampered copies; CC0-1.0 license unconfirmed on repo page (I debt #6b). Master-index carries it as one row with status Not labeled (line 1321), inheriting none of this nuance.
3. 29-style gaps: Surrealism (0) and Victorian (effectively 0 open-source) are genuine gaps recorded in D, H, and I consistently. Bohemian (THIN) and Body-art (PARTIAL, live-browser re-verification owed) are the soft gaps. Master-index faithfully reproduces the thinness (Victorian 1 row, Surrealism 2 rows incl. gap record).
4. DeepSec/Astryx claims: consistent across C (§§11–12), F (F3 + F4), G (G1 org correction; G2 CLI-only packages), H (H2). No internal contradiction: deepsec = vercel-labs/deepsec, Verified-with-org-correction; Astryx = no MCP server, CLI bash only, re-confirmed 2026-10-10.
5. Master-index vs C conflicts (upgrades beyond evidence):
   a. Named watchlist section has 22 rows, not 23 — watchlist #22 (anthropics/skills, Anthropic's official skills repository, Verified in C) has no row; section header says "(22)".
   b. Frontend design skill: C = Partially verified → master row 1289 = Verified.
   c. Strix: C = Partially verified (candidate, alternatives recorded) → master row 1297 = Verified with EMPTY description.
   d. PizzaBox→Pizza Bot Corrected is consistent (C Corrected; master row 1293 Corrected).
6. Munder Difflin canonical-URL split inside master-index: orchestration row 1252 points at fork `chaitanyagiri/munder-difflin`; watchlist row 1290 points at canonical `jeffreycayao/munder-difflin`. I lines 42 explicitly flags this for dedupe to one canonical record — still split.
7. I internal wording tension: line 6 "1,152 canonical directory rows in Deliverable A (1,210 raw…)" vs line 11 "1,210 canonical index records (1,281 raw…)" — two different canonical/raw pairs; I debt #1 acknowledges the parallel 01c count problem (workstream ~240 vs parsed 303).
8. E "6 Verified" authenticity bucket includes R4 (Meta formats), which E itself rates Partially verified — the bucket label overstates that member.
