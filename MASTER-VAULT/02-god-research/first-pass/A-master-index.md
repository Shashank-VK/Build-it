# A — Master Index (Unified: First Pass + Gemini Second Pass)

Date: 2026-10-09 (UTC) · Reconciler-Auditor, read-only. No installs. Prompt bodies: none reproduced.
Detailed evidence reasoning: `DIFF-REPORT-gemini-vs-firstpass.md` (same folder).
Second-pass folder guide: `../God research - gemini/00-README-second-pass.md`.

## Legend

- ✅ verified in first pass (2026-08-09 → 2026-10-09) · 🔶 provisional gemini-only (needs live pin)
- ⚠️ corrected-nuanced · ❌ not found / quarantined · ⏳ pending re-verify
- FP = `/mnt/c/Users/Shashank Karamudi/Desktop/God research/` · G = `/mnt/c/Users/Shashank Karamudi/Desktop/God research - gemini/`

## 1. First-pass categories → gemini pointers

| FP category | FP files | Gemini pointer | Relation |
|---|---|---|---|
| Phase 0 inventory + corrections | `00-phase0-inventory.md`, `_state/resource-index.json` | G-`06` §watchlist #11/#12 | Astryx ⚠️ corrected-nuanced; deepsec ⏳ quarantine |
| Core web tech (Elements / catalog) | `B-category-catalogs/01-core-web-tech.md` | G-`01` (82 res) | G is net-new baseline; FP slice was agentic-only |
| Frontend / backend / data / builders | `B-/02-frontend.md`, `03-backend.md`, `04-data.md`, `05-builders.md` | G-`01` §§2–9, G-`05` Pillars 2/6/7 | Complementary; no entity conflicts sampled |
| Design systems / D2C / visual assets / 3D | `B-/06-design-systems.md`, `07-design-to-code.md`, `08-visual-assets.md`, `21-creative-3d.md` | G-`02` §§1–4 | Complementary specs + recipes |
| Design styles ×29 | `D-design-styles/00-index-29.md` + `01–29` | G-`02` §5 + matrix | Same 29 slots; FP=fetch ledger, G=implementation recipes |
| Skills | `B-/09-skills.md` | G-`03` §§1–2 + cat.1–4, G-`04` #12 | G adds spec schema + CLI/validator tooling |
| MCP | `B-/10-mcp.md` | G-`03` §§3–5 (SDKs, registries, reference servers, gateways) | G is superset catalog (56) |
| Agents / multi-agent | `B-/11-agents.md`, `12-multi-agent.md` | G-`04` Parts I–II (34 items, runtime-vs-roleplay) | G adds baseline + taxonomy |
| Harness / context-memory | `B-/13-harness.md`, `14-context-memory.md` | G-`04` Parts III–IV (34 items) | G adds vector/AST/memory catalog |
| Scraping / testing / security / CI-CD / cloud / SEO-CMS | `B-/15-scraping.md`, `16-testing.md`, `17-security.md`, `18-cicd.md`, `19-cloud-deploy.md`, `20-seo-cms-commerce.md` | G-`05` Pillars 1–7 (70 res) | G adds ENFORCEABLE-vs-PROMPT-ONLY taxonomy |
| Prompt archives (meta-only) | `E-prompt-directory-meta-only.md` (P-01–P-12), `B-/22-prompt-archives-meta.md` | G-`06` Part 2 (3 archives) | asgeirtj shared; LouisShark + Piebald-AI 🔶 new; FP P-05–P-12 preserved |
| Watchlist 23 | `C-named-register-23.md` (+dup `B-/23-watchlist.md`) | G-`06` Part 1 (23 items) | 13 agree; 9 🔶 new/provisional; 1 stays PARTIAL — see §2 |

## 2. Watchlist unified status

| # | Name | FP status | Gemini claim | Unified |
|---|---|---|---|---|
| 1 | OpenViking | ✅ `volcengine/OpenViking` | ✅ same | ✅ resolved |
| 2 | PizzaBox AWS | ❌ unresolved (candidates refused) | `pizza-bot-app/pizza-bot` | 🔶 provisional — exact-name evidence still missing |
| 3 | Scrapling Krim Shoair | ❌ (429) | `D4Vinci/Scrapling` | 🔶 provisional — needs README/PyPI pin |
| 4 | ChatDev 2.0/devAll | ✅ `OpenBMB/ChatDev` | ✅ same | ✅ resolved |
| 5 | Munder Difflin | ❌ (429) | `chaitanyagiri/munder-difflin` | 🔶 provisional |
| 6 | Taste skill | ❌ (not in `anthropics/skills`) | `Leonxlnx/taste-skill` | 🔶 provisional (community skill explains absence) |
| 7 | Frontend design skill | ✅ `anthropics/skills#frontend-design` | ✅ same | ✅ resolved |
| 8 | Backend design skill | ❌ (no `backend-design` first-party) | convention (`vadimcomanescu/codex-skills`, `xenitV1/claude-code-maestro`, `docs/backend-design.md`) | 🔶 convention, no single canonical |
| 9 | public-apis | ✅ `public-apis/public-apis` | ✅ same | ✅ resolved |
| 10 | Agent Skills standard | ✅ `agentskills/agentskills` + spec site | ✅ same | ✅ resolved |
| 11 | Astryx | ✅ CLI-only (caveated) | CLI + hosted MCP (`apps/docsite/src/app/mcp/route.ts`) | ⚠️ corrected-nuanced — both true at different scopes |
| 12 | DeepSec | FP-internal: ✅ Aug → ❌ 404 Oct | `vercel-labs/deepsec` (404→200) | ⏳ unresolved-pending-reverify — cite neither yet |
| 13 | affaan-m/ECC | ✅ | ✅ same | ✅ resolved |
| 14 | ruvnet/ruflo | ✅ | ✅ same | ✅ resolved |
| 15 | anthropics/claude-cookbooks | ✅ | ✅ same + singular→plural 301 | ✅ resolved (adopt redirect note) |
| 16 | Designs | ❌ generic | Claude Design Variant Pattern | 🔶 pattern, not a repo |
| 17 | Firecrawl | ✅ `firecrawl/firecrawl` | ✅ same + mendableai→firecrawl 301 | ✅ resolved (adopt redirect note) |
| 18 | vercel/eve | ✅ | ✅ same | ✅ resolved |
| 19 | Strix | ❌ collision | `usestrix/strix` (PyPI `strix-agent`) | 🔶 provisional |
| 20 | DESIGN.md convention | ✅ `google-labs-code/design.md` | ✅ same (convention framing) | ✅ resolved |
| 21 | awesome-claude-skills | PARTIAL (4 orgs) | ComposioHQ + karanb192 (+VoltAgent comparator) | PARTIAL retained — org qualifier required |
| 22 | anthropics/skills | ✅ | ✅ same | ✅ resolved |
| 23 | NotebookLM skill | ❌ no pin | `PleasePrompto/` + `sanjay3290/` + `claude-world/` variants | 🔶 multi-candidate, no single canonical |

## 3. Prompt archives unified status

| Archive | FP record | Gemini record | Unified |
|---|---|---|---|
| `asgeirtj/system_prompts_leaks` | E:P-01 — 69.2k⭐/851 commits/16 dirs, alleged-leak | 1264 files/17 dirs, dual provenance (+`Anthropic/official/` 42-file mirror) | ✅ resolved-meta (metadata only; adopt census + official-subdir note; keep authenticity limits) |
| `LouisShark/chatgpt_system_prompt` | — (P-12 bucket) | 10.8k⭐ ~30.5MB, alleged-leak | 🔶 new, metadata only |
| `Piebald-AI/claude-code-system-prompts` | — (P-12 bucket) | 12.8k⭐ ~6.5MB/900+ files, alleged-leak | 🔶 new, metadata only |
| Registries (travisvn/ComposioHQ/BehiSecc/karanb192) | E:P-05–P-08 ✅ meta | Partial (+VoltAgent comparator) | ✅ FP authoritative; adopt VoltAgent pointer |
| Official docs / datasets / in-repo instructions | E:P-09/P-10/P-11 (placeholders + official) | — | ✅ preserved as-is (still pending pins) |

## 4. Unresolved list (preserved verbatim + adjudication tags)

1. `PizzaBox AWS` — 🔶 gemini candidate `pizza-bot-app/pizza-bot` unconfirmed as same entity; retry exact search.
2. `Scrapling Krim Shoair` — 🔶 `D4Vinci/Scrapling`; pin README/PyPI.
3. `Munder Difflin (+Dunder Mifflin variants)` — 🔶 `chaitanyagiri/munder-difflin`; pin fetch.
4. `Taste skill` — 🔶 `Leonxlnx/taste-skill`; pin registry/README.
5. `Backend design skill` — 🔶 convention only; pin instances before citing.
6. `DeepSec vercel/deepsec` — ⏳ do not cite; re-check `vercel/deepsec` + `vercel-labs/deepsec` live.
7. `Designs (exact+variants)` — 🔶 pattern resolution only; needs qualified search if a repo is meant.
8. `Strix (exact+variants)` — 🔶 `usestrix/strix`; pin fetch + disambiguation.
9. `NotebookLM skill` — 🔶 3 candidates; pin one with README compare.
10. `awesome-claude-skills` — PARTIAL by design; always org-qualify.
11. First-pass carryovers: `okjpg/llm-council` (exact URL needed); walkinglabs five-layer page; MEDUSA `.opencode/`; science-superpowers/Baton/shanraisshan OpenCode paths; Superpowers star dating; open issues (#4031, #30295/#8619/#23539, #7467, #11743, #12472); `E` follow-ups (per-file hashes, doc versions, dataset pins, registry freshness).

## 5. File map

- FP root: `00-phase0-inventory.md` (inventory) · `C-named-register-23.md` (watchlist authority) · `E-prompt-directory-meta-only.md` (archive authority) · `DIFF-REPORT-gemini-vs-firstpass.md` (this audit) · `A-master-index.md` (this file)
- FP dirs: `B-category-catalogs/01–23` · `D-design-styles/00–29` · `_state/resource-index.json`
- G dir: `00-README-second-pass.md` · `01-core-web-tech.md` (82) · `02-design-styles.md` (29) · `03-skills-mcp.md` (56) · `04-agents-harness-context.md` (68) · `05-infra-ops.md` (70) · `06-watchlist-prompts.md` (23+3)

## 6. Third pass (agy-pass, gemini-3.8-flash-high fallback)
- Guide: `agy-pass/00-README-third-pass.md` · audit: `DIFF-REPORT-agy-vs-both.md` (this folder).
- Sonnet 6× attempted, all 429 (~118h resets); all 6 files = gemini-3.8-flash-high.
- Counts: 76 / 34 items / 65 / 75 / 131 / 23+3 over 4292 lines (≈404 res total).
- Astryx 3-way agree dual-surface (CLI-local + `astryx.atmeta.com/mcp` search/get).
- deepsec 2-of-2 agree: `vercel/deepsec` 404 vs `vercel-labs/deepsec` 200 + `npx deepsec init`.
- New pins: D4Vinci author, HarnessMD 301, taste-skill, usestrix/strix, PleasePrompto/notebooklm.
- Still open: PizzaBox provisional; awesome-lists partial; backend-design convention only.
- Authority unchanged: first pass builds; second + third pass reference only.
(End - third-pass pointer appended 2026-10-09.)
