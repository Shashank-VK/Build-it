# DIFF REPORT — atlas vs all prior passes

Date: 2026-10-09 UTC. Scope: atlas (33 files, 33459 lines, read-complete per `atlas-READ-LOG.md`) vs three prior trees + two existing diffs.
Prior trees: (1) first pass `God research/` — B/01-23, C, D/29, E; (2) gemini sibling — 6 files (~276 resources); (3) agy-pass — 6 files (~400 resources).
Existing diffs preserved: `DIFF-REPORT-gemini-vs-firstpass.md`, `DIFF-REPORT-agy-vs-both.md`. This report does not re-resolve them; it adjudicates atlas against all.

## 1. Counts

- Atlas canonical scale (per `registers/coverage.md:37` + `index/master-index.md:1433` header + group2 cell audit): **~1210 canonical / 1281 raw** (71 duplicates folded). Master-index status-cell audit: **914 Verified / 141 Partially verified / 29 Unverified / 8 Historical / 8 Unresolved / 3 Corrected / 3 Archived / 104 Not-labeled** = 1210. Matches header claim exactly.
- A-master-index.md (1378) variant wording: 1210 assembled, 71 dups folded, 58 meta removed → 1152 directory rows. I-coverage-register.md carries both wordings (L6: 1152 directory rows / 1210 raw; L11: 1210 canonical / 1281 raw) — internal wording tension, not a recount. Use 1210/1281 as canonical (registers/coverage.md + master-index audit).
- Prior scale (context): first pass ~163-resource OpenCode catalog + 20 named 5-point + Phase-8 + B/01-23 + C + D/29 + E; gemini ~276 resources / 6 files; agy ~400 resources / 6 files. Atlas is ~3–7× larger than any single prior pass and the first to publish per-record verification labels at 4-digit scale.
- Watchlist: **18 Verified / 1 Corrected / 2 Partially / 2 Unresolved (of 23)** — consistent across C (433), registers/named-watchlist (435), I/coverage.
- Prompt archives: **19 records; existence 18 Verified / 1 Partially; authenticity 6 Verified / 3 Partially / 9 Unverified / 1 N-A (tool)** — consistent across E (446), registers/prompt-archives (440), I/coverage.
- Catalog workstream counts (per coverage + group3/4 reads): 01a 155 · 01b 195 · 01c ~240 (verification-debt: parses to 303 incl. overlap — treat 303 authoritative) · 02a 97+~95 · 02b 29 styles/~60–150 · 03a ~48 · 03b 34 · 04 82+~30 · 05a 57 · 05b 58 · 06a 111 · 06b 119 · 06c ~337.

## 2. NEW in atlas vs prior

1. **Full catalog scale.** 13 workstream catalogs (01a–06c) with per-section coverage notes, verification distributions, and dedup lists. No prior pass had this breadth (languages → frontend → backend → design → skills → agents → MCP → orchestration → context → acquisition → quality → operations).
2. **MCP spec currency.** 04-mcp: spec **2025-11-25 Final** (OIDC discovery, incremental scope, icons, sampling tool-calling, Client ID Metadata Docs, Tasks exp., JSON Schema 2020-12) + 2026-07-28 revision (no stateful handshake); **AAIF donated 2025-12-09** (MCP+AGENTS.md+goose, 49→250+ members); **A2A joined 2026-08-17/20**; MCP Apps extension 2026-01-26; Inspector v2; registry sizes point-in-time (official ~9.6K, mcp.so ~20–23K, Glama ~33–50K, Smithery ~6–7.3K, MCPFind ~13.9K); safety spine (Filesystem high-risk, Inspector CVE-2025-49596, Snyk Agent Scan 15+ cats).
3. **Build-chain currency.** Vite 8 (Mar 2026) on Rolldown+Rust/Oxc/Lightning CSS; TS 7.0 GA 2026-07-08 (Go port 8–12×); ES2026 2026-06-30; WASI 0.3 2026-06-11; tsup→tsdown; Rye→uv; Volta→mise; Node 24 LTS / 26 Current.
4. **Auth correction.** Auth.js → **Better Auth** recommendation (next-auth README opened, Verified+Corrected); Lucia discontinued (Historical). New in atlas vs all priors.
5. **19 prompt archives with existence-vs-authenticity split.** First systematic treatment: R1–R4 official, R5–R8 large unofficial, R9–R12 alleged-leak, R13–R17 agent repos/tools, R18–R19 evals. Authenticity 6V/3P/9U/1N-A; R5 asgeirtj split-provenance (Official/ clean, rest alleged); R13 Piebald-AI npm-extraction strongest methodology; R17 promptograph corpus metrics unverified + license NOASSERTION-vs-MIT.
6. **29-style gaps.** Surrealism **0** dedicated interface resources; Victorian effectively **0** (only `.btn-victorian` + commercial fonts); Bohemian THIN (2); Body-art PARTIAL (1 verified genome + 10 studio repos needing live-browser re-verification). D/H/I consistent; master-index reproduces thinness (Victorian 1 row, Surrealism 2 incl. gap record).
7. **Compatibility + relationship ledgers.** F (8-class legend, 38 selected rows, 4 explicit non-integrations); G (30 renames/successors, 16 companions, 8 collisions-NOT-relationships). No prior pass had either.
8. **Verification/discrepancy/coverage registers.** H (10 sections), discrepancies.md (20 identity + 8 license + 11 status + 6 incidents + 9 contradictions + 4 dedup), coverage.md (workstream table + 12-item debt). First machine-checkable debt list.
9. **2026 event currency.** Cal.com privatized 2026-04-14→cal.diy; Stytch→Twilio $104.1M; Lemon→Stripe Managed; Payload→Figma Jun 2025; Neon→Databricks May 2025; Atlas App Services EOL 2025-09-30; Deno→Cloudflare Deploy sunset ~Apr 2027; Statsig→OpenAI→Amplitude; Intercom→Fin/Salesforce pending; Mixpanel breach Nov 2025; CVE-2026-33634 trivy-action hijack; CVE-2026-80521 container escape; Windsurf→Devin Desktop; Gemini CLI→agy sunset 2026-06-18; Gitpod→Ona Classic sunset 2026-10-15.

## 3. CONFLICTS — adjudication

### 3.1 Astryx MCP: NO-MCP (atlas internal consensus)
- Atlas is unanimous across C §11, F (F3 Corrected + F4 non-integration), G (G2 CLI-only packages), H (H2 "Astryx MCP"→WRONG), phase0, README: **facebook/astryx has NO MCP server; agent surface = CLI bash only** (`npx @astryxdesign/cli … --dense`), re-confirmed 2026-10-10 (Phase-8 `packages/mcp-server`+`packages/mcp` 404, CLI README zero MCP refs).
- Adjudication: **aligns with first pass** (CLI-only). **Nuances gemini hosted-route claim**: gemini's hosted-route/MCP-adjacent reading is recorded as a *different scope* (remote/hosted adapter pattern), not as the canonical repo's own MCP server. Record both scopes: canonical repo = NO MCP (atlas+first-pass win on primary evidence); hosted/adapter route = gemini-scoped claim, needs primary URL before promotion. Do not flip atlas correction.

### 3.2 DeepSec org: vercel-labs canonical
- Atlas unanimous (A L1229, C §12, G G1, H H2, phase0 C14): **`vercel-labs/deepsec`** (Verified-with-org-correction); TS CLI `npx deepsec init`; static pre-scan → agent investigate (Opus 4.7 / GPT 5.5) → revalidate; cost warning $1k–$10k+.
- Adjudication: **aligns gemini + agy** (both already at vercel-labs); **corrects old first-pass `vercel/deepsec`** Phase-5 row (which phase0 itself flags as superseded by watchstream-14 re-verification). Canonical = `https://github.com/vercel-labs/deepsec`.

### 3.3 Watchlist 18V/1C/2P/2U
- Resolved 21/23. Unresolved preserved: **#8 Backend design skill** (5 author-specific candidates, no canonical match) + **#16 "Designs"** (bare name, no match). Partially: #7 Frontend design skill (mirrors only), #19 Strix (primary candidate usestrix/strix + 3 alts, identity decision owed).
- **Internal upgrade-vs-partial inconsistency (flagged, not resolved):** C says Partially for Frontend-design (#7) and Strix (#19); **master-index rows 1289/1297 say Verified** (Strix row with EMPTY description). C is the evidence record and wins until the canonical-tree check (frontend-design) and identity decision (Strix) in I debt #7 are actually performed. Do not treat master-index upgrade as resolution.
- PizzaBox→Pizza Bot Corrected consistent (C + master row 1293).

### 3.4 Master-index 22-vs-23 row gap
- Named-watchlist section header says (22) and carries **22 rows, not 23**: watchlist **#22 anthropics/skills** (official skills repo, Verified in C) has **no row** in master-index. Adjudication: omission, not merge — re-add #22 at assembly. Count gap acknowledged in group2 §5a and I debt.

### 3.5 Munder Difflin fork-vs-canonical pointer split
- Orchestration row 1252 → fork `chaitanyagiri/munder-difflin`; watchlist row 1290 → canonical `jeffreycayao/munder-difflin`. I:42 + discrepancies F both flag for dedupe to **one canonical (jeffreycayao)** at assembly. Still split in this extract — preserved as debt, not silently resolved.

### 3.6 asgeirtj split-provenance
- E-R5 / registers/prompt-archives R5: `asgeirtj/system_prompts_leaks` — `Anthropic/Official/` subfolder = provenance-clean (dated copies of Anthropic release-notes prompts); everything else = alleged extraction, no per-file method, single-file authenticity Unverified. 10+ same-name forks; CC0-1.0 unconfirmed on repo page; downstream WaPo/CEPS citations unverified. Master-index row 1321 carries it as single Not-labeled row with none of this nuance — **E wins on provenance; master row must not be cited for authenticity**.
- Related: E "6 Verified" authenticity bucket overstates R4 (Meta formats, itself Partially) — bucket label counts a partial member as Verified. Read as 5 full + 1 partial.

### 3.7 Licenses + incidents (6 unres)
- License discrepancies: Serena **GPL-3.0-or-later wins** over secondary MIT claims (05b B1 primary read); pa11y LGPL-3.0-only (Corrected); Directus BSL-1.1 verify-before-legal; Xata shutdown-vs-active conflict; promptograph / nightwire / Astro NOASSERTION-vs-MIT-badge; jujumilk3 no license; openai/evals NOASSERTION-vs-MIT minor; Slate archive single-source. **6 unres preserved**: promptograph, nightwire, Astro, Slate, Directus, Xata.
- Security incidents (do not re-verify blindly): CVE-2026-33634/GHSA-69fq-xp46-6x23 trivy-action hijack 2026-03-19; CVE-2026-80521 kernel escape 2026-09-22; CVE-2025-49596 Inspector; axios Mar-2026 hijack; Mixpanel Nov-2025 28M (+LiteLLM/Bitwarden/KICS secondary-only); gsd-build archived Jun-2026 DO NOT USE (safe fork open-gsd/gsd-core).
- G G3 Serena-license collision note agrees with GPL primary-read-wins.

## 4. Still-open list (preserved, not resolved)

1. Backend design skill (#8) + "Designs" (#16) — unresolved.
2. Frontend-design canonical-tree check + Strix identity decision (+ master-index upgrade rollback) — I debt #7.
3. Master-index #22 anthropics/skills row re-add.
4. Munder Difflin dedupe to jeffreycayao.
5. asgeirtj: CC0-1.0 confirm; R12 stats/license; R17 license; HF datasets; R1 staleness (Fable 5.1/Opus 5.5 check).
6. 01c count (240 vs parsed 303 — 303 authoritative); 03b depth (~17 agents brief); 06a/06c compact mentions; 01b 10 sub-items.
7. 104 Not-labeled spot-check; backend-Astryx re-run (Convex/Encore/Hasura candidates); H3 contradictions (sandbox, output-styles #5199, SDK identity, gstack, #30295, Smithery monetization).
8. License flags (6 above) + ~30 "widely reported" LICENSE sweep (06b); pricing snapshots not live-verified; Xata/Gitpod direction; Directus/Restate/DBOS terms; R-60 Cover-Agent primary; S-25 incidents 2–5 blast radius; BEAM/RULER/SCIP/Chroma single-source items; gitingest canonical drift in 05b (05b says cyclotruc, 06a corrects to coderamp-labs — 06a wins).
9. Scrapling author spelling: README correction says **Karim** Shoair; A-master row retains "Krim" — Karim wins.
10. I L6-vs-L11 wording tension (1152/1210 vs 1210/1281) — use 1210/1281.
