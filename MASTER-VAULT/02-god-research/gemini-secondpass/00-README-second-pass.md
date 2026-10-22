# 00 — README: Second Pass (Gemini)

Date: 2026-10-09 (UTC)
Status: read-only research drop; no installs, no executions, metadata-only for prompt archives.

## What this folder is

Second-pass breadth survey of the same "God research" program, produced independently of the
first-pass (Muse) tree at `/mnt/c/Users/Shashank Karamudi/Desktop/God research/`.
It re-covers the watchlist + prompt archives + design styles and adds a wide baseline
(core web tech → skills/MCP → agents/harness/context → infra/ops) that the first pass
never cataloged as such.

## Claimed provenance (per task brief; headers corroborate in part)

- Model: **gemini-3.8-flash-medium** (task brief), run **via `agy` 1.3.1 under WSL**.
- In-file headers say: "Google Gemini (Read-Only Mode)", "Antigravity Agentic Pair Programmer",
  "Internet Research Specialist (Google Gemini)". No prompt bodies, no bypass, no installs claimed.

## Contents — 6 files

| File | Title (short) | Claimed count |
|---|---|---|
| `01-core-web-tech.md` | Core Web Technologies directory (languages, frontend, styling, build/runtimes, backend/APIs, data, cloud/auth, scaffolders, patterns/specs) | **82 resources** (10+10+10+10+12+10+8+6+6) |
| `02-design-styles.md` | UI/UX architecture + 29 design styles compendium (incl. Astryx CLI-vs-MCP audit, D2C pipelines, assets, 3D/motion, comparison matrix) | **29 styles** |
| `03-skills-mcp.md` | Agent Skills + MCP + extensibility (spec, manifests, security, compatibility, §5 catalog) | **56 resources** ("DONE. 56 resources cataloged") |
| `04-agents-harness-context.md` | Coding agents + multi-agent runtime-vs-roleplay + harness guardrails + context/memory (Parts I–IV) | **68 resources** (18+16+18+16) |
| `05-infra-ops.md` | Infrastructure & operations across 7 pillars (scraping, public APIs, QA, security/sandboxing with ENFORCEABLE-vs-PROMPT-ONLY taxonomy, CI/CD, cloud/deploy, SEO/CMS/commerce) | **70 resources** (7×10) |
| `06-watchlist-prompts.md` | 23-item watchlist investigation (Part 1) + system-prompt archives metadata (Part 2) | **23/23 claimed RESOLVED + 3 archives** (`asgeirtj` 1264 files/17 dirs, `LouisShark`, `Piebald-AI`) |

Total: **≈276 resources + 29 styles + 23 watchlist items + 3 prompt archives**
(watchlist/archive/style topics overlap the first pass; the ~276 baseline is overwhelmingly net-new).

## Relation to first pass

- **Overlap (same entities, second look):** Astryx, `vercel/eve`, `vercel/deepsec`, ruflo, ECC,
  Agent Skills standard, `anthropics/skills`, cookbooks, public-apis, Firecrawl, DESIGN.md convention,
  awesome-claude-skills, 29 design styles, `asgeirtj` archive. Adjudications live in
  `../God research/DIFF-REPORT-gemini-vs-firstpass.md` (§4): Astryx = Corrected-nuanced
  (CLI-local + hosted remote MCP); deepsec = Unresolved-pending-reverify
  (`vercel/deepsec` 404 vs `vercel-labs/deepsec` claim); 9 watchlist items = provisional/convention/pattern.
- **Net-new (use as reference layer):** language/framework/runtime/data/cloud baseline, MCP SDK + registry
  matrix, agent/harness/context taxonomy, 70-item ops catalog, per-style implementation recipes,
  file-level `asgeirtj` census, `LouisShark` + `Piebald-AI` archives, `VoltAgent/awesome-agent-skills` comparator.
- **Authority rule:** first pass remains the build authority (locked architecture, DoD gates, dispositions);
  this folder is the breadth/reference layer until its provisional items are live-pinned.

## Limits

- Counts and HTTP statuses are file-internal claims sampled 2026-10-09; several second-pass
  resolutions lack captured README excerpts in the sampled surface — treat §4c "provisional" items accordingly.
- Prompt archives are metadata-only by policy; nothing here authorizes reproduction or bypass use.
