# DIFF REPORT — agy-pass Third Pass vs First Pass + Gemini Second Pass

Date: 2026-10-09 (UTC)
Role: Reconciler — read-only analysis, no installs, no executions, no prompt-body reproduction.
Method: sample-read `DIFF-REPORT-gemini-vs-firstpass.md` (full) + `agy-pass/06-watchlist-prompts.md` (full, incl. Astryx/deepsec tail) + directory listings + `wc` line counts + head/tail greps of agy-pass 01–05 headers/claims. No web re-checks (adjudication from file contents only).

## 1. Model provenance

Sonnet attempted 6× via agy, all 429 quota (resets ~118h); all six agy-pass files fell back to **gemini-3.8-flash-high** (line-1 header in every file + tail attestations). Treat as Gemini-high redo of the Gemini-medium second pass, not an independent Sonnet cross-check. Details: `agy-pass/00-README-third-pass.md`.

## 2. Counts table (first / second / third)

| Slot | First pass (Muse) | Second pass (Gemini flash-medium) | Third pass (agy-pass, gemini-3.8-flash-high) |
|---|---|---|---|
| Core web tech | `B-/01-core-web-tech.md` (agentic slice; part of 163 usable / 43 excluded over Elements 1–26) | `01` — **82 res** / 960 lines | `01` — **76 res** (9 disciplines) / 961 lines |
| Design styles | `D-/00–29` — **29 styles** + fetch ledger (00-index: 55 lines) | `02` — **29 styles** / 628 lines | `02` — **34 items** (29 styles + 4 infra sections + Astryx analysis) / 837 lines |
| Skills / MCP | `B-/09-skills.md` + `10-mcp.md` (part of 26-element catalog; Element 1: 14 usable / 28 excl.) | `03` — **56 res** / 545 lines | `03` — **65 res** / 841 lines |
| Agents / harness / context | `B-/11-agents.md`, `12-multi-agent.md`, `13-harness.md`, `14-context-memory.md` | `04` — **68 res** (18+16+18+16) / 910 lines | `04` — **75 res** (7 categories; 9 coding agents) / 638 lines |
| Infra / ops | `B-/15-scraping.md`, `16-testing.md`, `17-security.md`, `18-cicd.md`, `19-cloud-deploy.md`, `20-seo-cms-commerce.md` (first-infra bundle per brief: ~124) | `05` — **70 res** (7×10) / 1043 lines | `05` — **131 res** / 614 lines |
| Watchlist + prompts | `C-named-register-23.md` — **13 RESOLVED / 1 PARTIAL / 9 UNRESOLVED** / 272 lines; `E-prompt-directory-meta-only.md` — **12 records P-01–P-12** / 146 lines | `06` — **23/23 claimed + 3 archives** / 136 lines | `06` — **21 resolved/pattern/convention + 1 partial + 1 provisional** (23 addressed) **+ 3 archives + 4 official in-repo sources** / 401 lines |
| Totals | 23 catalogs + 30 design files + register + prompt dir | ≈276 res + 29 styles + 23 + 3 / 4222 lines | ≈404 res + 34 design items + 23 + 3 / 4292 lines |

## 3. NEW in agy-pass vs both

Density gains concentrate in 03/04/05; watchlist adds redirect/nuance pins:

- **Infra 131 vs 70 vs ~124:** near-2× Gemini; adds HTTP-client tier, scraper-compliance attestation, multi-tier isolation hierarchy (L0 prompt-only → L5 hypervisor) and sandboxing comparison matrix on top of Gemini's ENFORCEABLE-vs-PROMPT-ONLY taxonomy.
- **Skills/MCP 65 vs 56 vs Element-1/6/19 excerpts:** adds validators/linters, pruning/optimizer routers, marketplaces/discovery registries, MCP clients, and counted non-MCP-alternative slots (native tool-calling 1, LSP 1, A2A 3).
- **Agents/harness 75 vs 68:** 9-agent deep dives + supervisor/DAG state-transition framing + formal DoD/verification-gate section; count table by 7 categories (agents/runtime/harness/DoD/AST/AST-embeddings/memory).
- **Core 76 vs 82:** slightly narrower; same 9-discipline shape, target-60+ framing with per-discipline Yes matrix.
- **Design 34 items vs 29 vs 29:** countable infra sections (systems, W3C DTCG tokens, D2C pipelines, assets/3D) + dedicated `facebook/astryx` README/MCP section.
- **Newly resolved vs both (watchlist pins):**
  - `D4Vinci/Scrapling` — author linkage closed: **Karim Shoair = @D4Vinci** (was 429/unverified in first, provisional in Gemini).
  - `HarnessMD/munder-difflin` — canonical redirect: **`chaitanyagiri/munder-difflin` → HTTP 301 → `HarnessMD/munder-difflin`** (first UNRESOLVED; Gemini had only the pre-move org).
  - `Leonxlnx/taste-skill` — author Leon Lin + `tasteskill.dev`, "anti-slop" SKILL.md, HTTP 200 (was absence-note in first).
  - `usestrix/strix` — PyPI `strix-agent`, Docker PoC sandbox, ASUS-rog disambiguation (was collision in first).
  - `PleasePrompto/notebooklm-skill` — HTTP 200 as canonical + `sanjay3290/` + `claude-world/` variants enumerated (was no-pin in first, multi-candidate in Gemini).
  - **Vercel deepsec:** `vercel/deepsec` **404** vs `vercel-labs/deepsec` **200** both live-tested 2026-10-09, description *"security harness for finding vulnerabilities … powered by coding agents"*, `npx deepsec init` quoted (Gemini's claim now independently repeated with test-date + description + init quote).
  - **Astryx dual-surface nuance:** local = CLI-only (no `@astryxdesign/mcp`, no `astryx mcp`, no stdio daemon; `npx @astryxdesign/cli <cmd> --dense` / `manifest --json`) + remote = Streamable HTTP at **`https://astryx.atmeta.com/mcp`** (`apps/docsite/src/app/mcp/route.ts`, `mcp-handler`+`zod`, tools **`search(query,type?,limit?)`** ~1.5K-token briefs from `.doc.mjs` index / **`get(name,type)`**). Repeats Gemini's §4a finding with route + tool-signature detail.
  - Plus: ChatDev v2.0/DevAll CADET/Vue3/branch note; cookbooks singular→plural 301; Firecrawl mendableai→firecrawl 301; `asgeirtj` dual-provenance + per-dir census retained; §2.4 adds 4 official in-repo ground-truth sources (Astryx AGENTS/CLAUDE, eve agent/, ECC, Ruflo USERGUIDE/STATUS).

## 4. CONFLICTS adjudication

- **Astryx — now 3-WAY AGREE (dual-surface):** first pass CLI-only (caveated, local scope) + Gemini remote-endpoint + agy-pass repeats both scopes with route/signature. Verdict: **Corrected-nuanced CONFIRMED** — local CLI-only stands for builds; remote MCP is opt-in (auth/rate-limit/cost review first).
- **deepsec — now 2-of-2 AGREE (vercel-labs canonical):** first pass Aug-✅→Oct-404 internal tension; Gemini `vercel-labs/deepsec` 200; agy-pass re-tests both live (404 vs 200) + description + `npx deepsec init`. Verdict: **upgrade from Unresolved-pending-reverify to Provisionally-canonical `vercel-labs/deepsec`** — still capture a fresh live fetch (status + README + dates + redirect banner) before hard-citing, but quarantine can lift to provisional-cite.
- **Watchlist provisionals reduced (9 → effectively 1 + 1 partial + conventions):** Scrapling, Munder Difflin, Taste, Strix, NotebookLM move provisional→resolved-per-file-evidence; backend-design and Designs stay convention/pattern (correct — no single repo); PizzaBox stays unresolved-provisional (conflation explicitly disclaimed); awesome-claude-skills stays multi-org partial (now 5-way: travisvn earliest / ComposioHQ largest / karanb192 dev / BehiSecc taxonomy / VoltAgent meta-registry).
- **Counts inflation note:** 131/65/75 are file-internal claims (denser but not live-pinned); authority rule unchanged — first pass builds, second+third reference.

## 5. Still open

1. **PizzaBox unresolved-provisional** — no `*/PizzaBox` under AWS; `pizza-bot-app/pizza-bot` is a functional candidate only (Two-Pizza/1U conflation). Needs exact-string retry.
2. **awesome-claude-skills multi-org partial** — no bare-name canonical; always org-qualify (5 registries above).
3. **Backend-design convention, not official folder** — absent from `anthropics/skills`; community `skills/backend-design` / `docs/backend-design.md` only.
4. Carryovers: `okjpg/llm-council` exact URL; walkinglabs five-layer page; MEDUSA `.opencode/`; science-superpowers/Baton/shanraisshan paths; Superpowers star dating; open issues (#4031, #30295/#8619/#23539, #7467, #11743, #12472); `E` follow-ups (hashes, doc versions, dataset pins, registry freshness); Astryx remote-MCP adoption check (pinned commit + auth/cost).

## 6. Recommendation

1. **Keep first pass as build authority; adopt second + third as reference layers.** Promote agy-pass redirect/nuance pins (HarnessMD 301, deepsec 404/200 + init quote, Astryx route + tool signatures, D4Vinci author link) into `C-named-register-23.md` / `A-master-index.md` appendices.
2. **Apply adjudications:** Astryx → corrected-nuanced confirmed; deepsec → provisional-canonical `vercel-labs/deepsec` (one fresh live pin to close); 5 ex-provisionals → resolved-per-file-evidence (one README/PyPI pin each to harden); PizzaBox stays provisional; awesome-lists stay partial; backend-design/Designs stay convention/pattern.
3. **Single verification sprint:** close deepsec + 5 harden-pins + PizzaBox exact search in one live session (capture HTTP + commit hash + access date), then fold into register + master index.

(End — 23/23 addressed: 21 resolved/pattern/convention, 1 partial, 1 provisional; 3 archives meta-only, 0 bodies.)
