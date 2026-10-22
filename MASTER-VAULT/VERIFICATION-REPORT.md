# VERIFICATION-REPORT — final.md -> MASTER-VAULT/

Source: `final.md` — 158,282 lines, 16,157,074 bytes
Banners: **836** real banners (1 mention(s) in prose ignored)
Parsing rule: **extended** — body = banner+1 to next banner, trailing blanks trimmed.

## Line accounting

| Bucket | Lines | Written to vault? |
|---|---|---|
| `final.md` total | 158,282 | — |
| Banner lines (structural metadata) | 836 | no |
| File body lines (extended parse) | 149,740 | yes |
| Unbannered region lines (7 regions) | 7,702 | yes |
| Blank separator lines left by block joining | 4 | no (empty) |
| **Total** | **158,282** | |

**Unassigned non-blank lines: 0** — every line of `final.md` is accounted for exactly once, with nothing dropped and nothing written twice.

Lines written into the vault: **157,504** across **851** entries.

## Byte-parity against on-disk sources

| Result | Files |
|---|---|
| Byte-identical to source on disk | **833** |
| Differs (post-merge drift) | 3 |
| Source directory unavailable | 0 |

This check compares the **pre-redaction** body against disk. 10 files are caveman-redacted and therefore intentionally differ from disk afterwards.

### Files differing from current on-disk state

These differ by invisible/whitespace edits made to the source *after* the merge snapshot was taken. The vault preserves the merge's version.

| vault path | banner declared | vault lines | disk lines |
|---|---|---|---|
| `02-god-research/diffs-and-state/_state/resource-index.json` | 0 | 15 | 1 |
| `03-solo-levelling/deve-source/scripts/verify.sh` | 75 | 76 | 75 |
| `03-solo-levelling/the harness/phase-2/verify/CROSSBATCH_TENSION.md` | 168 | 168 | 168 |

## Under-declared banners (declared `(N lines)` < real body length)

37 files. Under the strict-count rule these would each lose their final line(s); the extended rule keeps them whole and matches the on-disk originals.

| vault path | declared | actual | shortfall |
|---|---|---|---|
| `01-opencode-research/catalog.md` | 2993 | 2994 | +1 |
| `02-god-research/atlas/B1-core-web-technologies.md` | 928 | 929 | +1 |
| `02-god-research/atlas/B2-design-and-visual.md` | 147 | 148 | +1 |
| `02-god-research/atlas/B3-agent-ecosystem.md` | 249 | 250 | +1 |
| `02-god-research/atlas/B4-multiagent-harness-context.md` | 150 | 151 | +1 |
| `02-god-research/atlas/B5-infrastructure-quality.md` | 472 | 473 | +1 |
| `02-god-research/diffs-and-state/_state/resource-index.json` | 0 | 15 | +15 |
| `02-god-research/first-pass/B-category-catalogs/09-skills.md` | 579 | 580 | +1 |
| `03-solo-levelling/deve-source/.pytest_cache/v/cache/lastfailed` | 0 | 1 | +1 |
| `03-solo-levelling/deve-source/.pytest_cache/v/cache/nodeids` | 47 | 48 | +1 |
| `03-solo-levelling/deve-source/scripts/verify.sh` | 75 | 76 | +1 |
| `03-solo-levelling/the harness/.harness/README.md` | 33 | 34 | +1 |
| `03-solo-levelling/the harness/.harness/permissions/policies.cedar` | 80 | 81 | +1 |
| `03-solo-levelling/the harness/.harness/permissions/presets.json` | 116 | 117 | +1 |
| `03-solo-levelling/the harness/.harness/skills/index.json` | 567 | 568 | +1 |
| `03-solo-levelling/the harness/elements/D-1_EXECUTION.md` | 161 | 162 | +1 |
| `03-solo-levelling/the harness/elements/D-2_CONTEXT.md` | 205 | 206 | +1 |
| `03-solo-levelling/the harness/elements/D-3_INTEGRATION.md` | 227 | 228 | +1 |
| `03-solo-levelling/the harness/elements/D-4_SAFETY.md` | 183 | 184 | +1 |
| `03-solo-levelling/the harness/elements/D-5_DX_META.md` | 139 | 140 | +1 |
| `03-solo-levelling/the harness/elements/D-6_A_B_TIER.md` | 119 | 120 | +1 |
| `03-solo-levelling/the harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md` | 111 | 112 | +1 |
| `03-solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_PARTIAL.md` | 84 | 85 | +1 |
| `03-solo-levelling/the harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md` | 108 | 109 | +1 |
| `03-solo-levelling/the harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md` | 94 | 95 | +1 |
| `03-solo-levelling/the harness/phase-2/RANKINGS.md` | 120 | 121 | +1 |
| `03-solo-levelling/the harness/phase-2/RUBRIC.md` | 47 | 48 | +1 |
| `03-solo-levelling/the harness/phase-3.5/VALIDATION_PLAN.md` | 31 | 32 | +1 |
| `03-solo-levelling/the harness/phase-3.5/VALIDATION_REPORT.md` | 56 | 57 | +1 |
| `03-solo-levelling/the harness/phase-3/PLAN.md` | 49 | 50 | +1 |
| `03-solo-levelling/the harness/phase-3/TOOL_SELECTION_INDEX.md` | 92 | 93 | +1 |
| `03-solo-levelling/the harness/phase-3/tools/T-D_SAFETY.md` | 679 | 682 | +3 |
| `03-solo-levelling/the harness/update.md` | 59 | 60 | +1 |
| `04-builders-playbook/product_engineering/research/build-ship/05-evidence-register.md` | 111 | 112 | +1 |
| `05-superior-os/.harness/permissions/presets.json` | 94 | 95 | +1 |
| `05-superior-os/os/LOOP-ENGINEERING.md` | 20 | 21 | +1 |
| `05-superior-os/os/third-party-index.json` | 226 | 227 | +1 |

## Folder breakdown (actual, vs. the task brief's stated counts)

| Folder | Extracted | Brief claimed | Note |
|---|---|---|---|
| `00-INDEX-AND-MAP.md/` | 1 | — |  |
| `01-opencode-research/` | 23 | 23 | matches |
| `02-god-research/` | 115 | 80 | brief said 80; `God research/` actually holds 108 files (+7 gemini = 115) |
| `03-solo-levelling/` | 303 | 303 | total matches, but sourced from TWO roots: `solo-levelling/` (240) + `deve/` (63 -> deve-source/) |
| `04-builders-playbook/` | 266 | 266 | matches (banner paths were stale; remapped) |
| `05-superior-os/` | 130 | 130 | brief said 130; only 129 were ever merged — `scripts/verify.sh` exists on disk but has no banner |
| `06-unbannered-addendums/` | 13 | — |  |

## Duplicate content preserved

7 verbatim duplicate blocks (3,593 lines) plus one orphan line sit in the final region of `final.md` with no banner. Each was hash-verified against its canonical copy and written under `06-unbannered-addendums/_duplicates/`. Two further duplicates live inside the Part 18 addendum: `BUILD-PROMPT-UNIVERSAL.md` (blank-line drift only) and `THE GOD PROMPT v1.0`.

| # | duplicate file | canonical copy | lines |
|---|---|---|---|
| 1 | `06-unbannered-addendums/_duplicates/01-01-hackathon-win-system.md` | `04-builders-playbook/01-hackathon-win-system.md` | 119 |
| 2 | `06-unbannered-addendums/_duplicates/02-02-project-execution-plan.md` | `04-builders-playbook/02-project-execution-plan.md` | 138 |
| 3 | `06-unbannered-addendums/_duplicates/03-A-expansion-companies.md` | `04-builders-playbook/product_engineering/appendices/A-expansion-companies.md` | 107 |
| 4 | `06-unbannered-addendums/_duplicates/04-B-expansion-tools.md` | `04-builders-playbook/product_engineering/appendices/B-expansion-tools.md` | 111 |
| 5 | `06-unbannered-addendums/_duplicates/05-C-expansion-practices.md` | `04-builders-playbook/product_engineering/appendices/C-expansion-practices.md` | 56 |
| 6 | `06-unbannered-addendums/_duplicates/06-D-forensics-digest.md` | `04-builders-playbook/product_engineering/appendices/D-forensics-digest.md` | 68 |
| 7 | `06-unbannered-addendums/_duplicates/07-catalog.md` | `01-opencode-research/catalog.md` | 2994 |

## Caveman redaction

Rule 4 requested removal of `JuliusBrussee/caveman`. **44 occurrences** across **12 files** were replaced in place with `[REDACTED-caveman]` / `[REDACTED]`. Line counts and table structure are preserved; every edit is logged in `CAVEMAN-LEDGER.json`. `sha256_final` in `MANIFEST.json` is computed post-redaction; `sha256_preredact` preserves the original digest.

| vault path | occurrences |
|---|---|
| `01-opencode-research/BUILD-PROMPT-FINAL.md` | 7 |
| `01-opencode-research/BUILD-PROMPT-UNIVERSAL.md` | 6 |
| `01-opencode-research/catalog.md` | 7 |
| `01-opencode-research/research/01-existing-summary.md` | 1 |
| `02-god-research/atlas/catalogs/03a-skills.md` | 1 |
| `02-god-research/atlas/catalogs/05b-context.md` | 3 |
| `02-god-research/atlas/index/phase0-inventory.md` | 1 |
| `02-god-research/diffs-and-state/_state/atlas-read-group4.md` | 1 |
| `02-god-research/first-pass/00-phase0-inventory.md` | 1 |
| `04-builders-playbook/product_engineering/research/expansion-practices/01-contrarian-methodologies.md` | 3 |
| `06-unbannered-addendums/_duplicates/07-catalog.md` | 7 |
| `06-unbannered-addendums/part-18-b1-b10-overlap-and-universal.md` | 6 |

## Running the `05-superior-os` gate

`bash 05-superior-os/scripts/verify.sh` passes end to end: secret-scan, `py_compile` syntax check, 52 pytest tests, coverage gate, claim check (exit 0).

Note that it is **not side-effect free** — `py_compile` writes `__pycache__/*.pyc` bytecode inside `05-superior-os/`. Those files are not part of the extraction and are deliberately absent from `MANIFEST.json`. Re-running `unpack_final.py --force --recover-missing` restores a pristine vault; the run is deterministic and idempotent.

## Integrity checks

- [x] bannered files written == banners (836)
- [x] no body shorter than its declared count
- [x] no duplicate vault paths
- [x] every on-disk source byte-identical or listed as drift
- [x] every final.md line assigned (banner / content / region / separator)

## Complete line accounting

| | Lines |
|---|---|
| `final.md` total | 158,282 |
| Assigned to a banner / file body / region | 158,278 |
| Blank separator lines left by block joining | 4 |
| **Unassigned non-blank lines** | **0** |
| Double-counted lines | 0 |

## Files recovered from disk (NOT part of the merge)

These exist in the source tree but have **no banner in `final.md`**, so they were never merged. They were copied verbatim from disk only because `--recover-missing` was passed. They are not extracted content.

| vault path | lines | source |
|---|---|---|
| `05-superior-os/scripts/verify.sh` | 15 | `/mnt/c/Users/Shashank Karamudi/Desktop/theeeeeeeee/superior-os/scripts/verify.sh` |
