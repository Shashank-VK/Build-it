# Atlas READ LOG — all 33 files, read-complete

Date: 2026-10-09 UTC (in-file Built dates 2026-10-10). Mode: read-only, paginated to EOF. No installs / builds / executions.
Sources: `_state/atlas-read-group1.md` (8 files, 3593 lines), `_state/atlas-read-group2.md` (8 files, 3353 lines), `_state/atlas-read-group3.md` (9 files, 17601 lines), `_state/atlas-read-group4.md` (8 files, 8912 lines).
Base: `atlas/`

Total: **33 files, 33459 lines, all read-complete.**

## Full table

| # | File (relative to `atlas/`) | Lines | Records / notes | Read-complete |
|---|---|---|---|---|
| 1 | README.md | 70 | entrypoint; 1152-row / watchlist / style / archive totals declared; no resource table | yes (1–70, EOF) |
| 2 | index/phase0-inventory.md | 194 | ~50+ URLs; 20 Phase-5 rows + 27 other-verified + 26-element lists; C1–C16, Q1–Q8 | yes (1–194, EOF) |
| 3 | A-master-index.md | 1378 | ~1152 directory rows (71 dups folded, 58 meta removed) | yes (paginated, EOF 1378) |
| 4 | B1-core-web-technologies.md | 929 | 648 condensed records | yes (EOF) |
| 5 | B2-design-and-visual.md | 148 | 97 condensed (22+7+15+19+20+14) | yes (EOF 148) |
| 6 | B3-agent-ecosystem.md | 250 | 133 condensed (28 skills + 84 MCP + 21 agents) | yes (EOF) |
| 7 | B4-multiagent-harness-context.md | 151 | 113 condensed (24+31+58) | yes (EOF) |
| 8 | B5-infrastructure-quality.md | 473 | 316 condensed (90+75+44+0+0+107) | yes (EOF) |
| 9 | C-named-watchlist.md | 433 | 23 items: 18V/1C/2P/2U | yes (wc 433, 1–433) |
| 10 | D-design-styles.md | 678 | 29 styles; 25 covered / 1 GAP / 2 THIN / 1 PARTIAL | yes (EOF) |
| 11 | E-prompt-archives.md | 446 | 19 records; existence 18V/1P; authenticity 6V/3P/9U/1N-A | yes (EOF) |
| 12 | F-compatibility-index.md | 99 | 8-class legend; 38 selected-resource rows | yes (1–99) |
| 13 | G-relationship-index.md | 70 | 30 renames + 16 companions + 8 collisions | yes (1–70) |
| 14 | H-verification-register.md | 136 | H1–H10 (15 unres names, 13 corrections, 5+2 contradictions, 19 archived, 9 licenses, 6 incidents) | yes (1–136) |
| 15 | I-coverage-register.md | 59 | 1152-row / 1210-raw wording; 16-row workstream table; 12-item debt | yes (1–59) |
| 16 | index/master-index.md | 1433 | 1210 canonical records; 43 sections; audited 914V/141P/104NL/29U/8Hist/8Unres/3C/3Arch | yes (EOF 1433) |
| 17 | catalogs/01a-languages-build.md | 3215 | 155 rec | yes (EOF 3215) |
| 18 | catalogs/01b-frontend.md | 3585 | 195 rec (190+5 xref) | yes (EOF 3585) |
| 19 | catalogs/01c-backend-data-platforms.md | 1887 | ~240 rec | yes (EOF 1887) |
| 20 | catalogs/02a-design.md | 2427 | 97 full + ~95 compact | yes (EOF 2427) |
| 21 | catalogs/02b-design-styles.md | 593 | ~150 rec across 29 styles | yes (EOF 593) |
| 22 | catalogs/03a-skills.md | 763 | ~48 new rec (27 full Part-21) | yes (EOF 763) |
| 23 | catalogs/03b-agents.md | 885 | 34 (17 rec + 5 medium + 12 brief) | yes (885-line completion marker) |
| 24 | catalogs/04-mcp.md | 2846 | 82 rec + 12 archived ref servers | yes (EOF 2846) |
| 25 | catalogs/05a-orchestration.md | 1400 | 57 (55 full + 2 xref) | yes (EOF 1400) |
| 26 | catalogs/05b-context.md | 1380 | 58 (29+18+11) | yes (EOF 1380) |
| 27 | catalogs/06a-data-acquisition.md | 2322 | 111 (90 full + 21 compact) | yes (EOF 2322) |
| 28 | catalogs/06b-quality.md | 2779 | 119 (75R+44S) | yes (EOF 2779) |
| 29 | catalogs/06c-operations.md | 2436 | ~337 (297 full + ~40 compact) | yes (EOF 2436) |
| 30 | registers/coverage.md | 37 | 1210 canonical / 1281 raw; 914V/141P/29U/8Hist/8Unres/3Corr/3Arch/104 Not-labeled | yes (1–37) |
| 31 | registers/discrepancies.md | 83 | 20 identity + 8 license + 11 status + 6 incidents + 9 contradictions + 4 dedup | yes (1–83) |
| 32 | registers/named-watchlist.md | 435 | 23 items: 18V/1C/2P/2U | yes (EOF 435) |
| 33 | registers/prompt-archives.md | 440 | 19 items: existence 18V/1P; authenticity 6V/3P/9U/1N-A | yes (EOF 440) |
| | **Total** | **33459** | **33 files** | **all read-complete** |

Check: 3593 (group1) + 3353 (group2) + 17601 (group3) + 8912 (group4) = 33459.

## Structural notes

- Nested `atlas/atlas` duplicate: **removed** (not present in current extract; `ls -R atlas/` shows single level: 14 top-level .md + `catalogs/` 13 + `index/` 2 + `registers/` 4 + `evidence/`).
- `evidence/`: **empty** — absent from zip extract (0 entries, `ls -la atlas/evidence/` returns only `.`/`..`). No evidence payloads to log.
- EOF markers confirmed on all files except C-named-watchlist.md (ends line 433 on content bullet, `wc -l` = 433) — treated read-complete via full pagination 1–433.
- A-master-index.md (1378) vs index/master-index.md (1433): both read; 55-line / section-header delta preserved, not merged.
- C-named-watchlist.md (433) vs registers/named-watchlist.md (435): both read; 2-line delta preserved.
- E-prompt-archives.md (446) vs registers/prompt-archives.md (440): both read; 6-line delta preserved.
- H (136) vs registers/discrepancies.md (83) and I (59) vs registers/coverage.md (37): distinct deliverable-vs-register pairs, both sides read.
- D (678) vs catalogs/02b (593): distinct synthesis-vs-workstream pair, both read.
