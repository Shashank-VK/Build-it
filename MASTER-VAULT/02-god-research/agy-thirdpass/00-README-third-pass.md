# 00 — README: Third Pass (agy-pass)

Date: 2026-10-09 (UTC)
Status: read-only research drop; no installs, no executions, metadata-only for prompt archives.
Role: Reconciler (read-only analysis + this README; no web re-checks).

## Model provenance

- Intended model: **Sonnet** (via `agy`), attempted **6×** — every attempt hit **429 quota**, resets cited at **~118h**.
- Actual model on all 6 files (per line-1 header in each file): **gemini-3.8-flash-high (sonnet-quota-fallback)**.
- Corroboration: `head -n 1` of all six `agy-pass/*.md` returns identical `model-used: gemini-3.8-flash-high (sonnet-quota-fallback)`; tails carry `Verification Date: 2026-10-09 · Model: gemini-3.8-flash-high (sonnet-quota-fallback)`.
- Treat as a **Gemini-high redo of the Gemini-medium second pass**, not an independent Sonnet cross-check.

## Contents — 6 files

| File | Title (short) | Claimed count (in-file) | Lines (wc) |
|---|---|---|---|
| `01-core-web-tech.md` | Core web tech, 9 disciplines | **76 resources** (target 60+ exceeded) | 961 |
| `02-design-styles.md` | 29 styles + 4 infra sections + Astryx README/MCP nuance | **34 items** (29 styles + 4 sections + Astryx analysis) | 837 |
| `03-skills-mcp.md` | Skills spec + MCP spec/SDKs/registries + alternatives | **65 catalogued** | 841 |
| `04-agents-harness-context.md` | 9 coding agents + multi-agent + harness/DoD + context/memory | **75 resources**, 7 categories | 638 |
| `05-infra-ops.md` | Scraping/APIs/QA/security/CI-CD/cloud/SEO-CMS | **131 resources** | 614 |
| `06-watchlist-prompts.md` | 23-item watchlist + 3 prompt archives (meta-only) | **23 items** (21 resolved/pattern/convention, 1 multi-org partial, 1 provisional) **+ 3 archives** (asgeirtj 1264 files/17 dirs) | 401 |
| **Total** | | **≈404 resources + 34 design items + 23 watchlist + 3 archives** | 4292 |

## Relation to the other two passes

- **First pass (Muse)** at `../` — `B-category-catalogs/01–23`, `C-named-register-23.md` (13/1/9), `D-design-styles/00–29`, `E-prompt-directory-meta-only.md` (P-01–P-12), `00-phase0-inventory.md`, `A-master-index.md`. Remains the **build authority** (locked architecture, DoD gates, dispositions).
- **Second pass (Gemini flash-medium via agy)** at `../../God research - gemini/` — 82 / 29 / 56 / 68 / 70 / 23+3 over 4222 lines. The breadth/reference layer.
- **This third pass** re-covers the same six slots at higher density in skills/MCP (65 vs 56), agents/harness (75 vs 68), and infra (131 vs 70); slightly narrower core (76 vs 82); design adds countable infra sections (34 items vs 29 styles). Watchlist deltas vs both are adjudicated in `../DIFF-REPORT-agy-vs-both.md`.
- **Authority rule unchanged:** first pass builds, second + third pass reference. Promote third-pass pins (redirect/nuance evidence) into appendices; do not rebuild on them.

## Limits

- Counts and HTTP statuses are file-internal claims sampled 2026-10-09; live re-verify before citing provisionals.
- Prompt archives are metadata-only by policy (0 bodies reproduced claimed).
- Known still-open items: PizzaBox unresolved-provisional; awesome-claude-skills multi-org partial; backend-design convention (no official folder). See `../DIFF-REPORT-agy-vs-both.md` §5.

(End — 6 files, ≈404 resources + 34 design items + 23 watchlist + 3 archives, 4292 lines.)
