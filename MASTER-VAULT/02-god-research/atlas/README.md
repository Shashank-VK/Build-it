# The Omniscient Resource Atlas — Final Encyclopedia

**Built:** 2026-10-10 · **Research method:** live internet research (primary sources first: repository contents, official docs, package registries, protocol specs) · **Scope:** read-only — discover, inspect, identify, verify, categorize, explain usage, record sources.

## What this is

A research encyclopedia of the resources relevant to modern web development and AI-assisted software engineering: programming technologies and frameworks; open-source repositories; AI coding skills and skill collections; MCP servers and integrations; coding agents and their extensions; multi-agent frameworks and autonomous agent systems; context engineering, memory, and repository intelligence; development harnesses and reusable engineering workflows; UI/UX systems, design resources, and visual styles; website builders, templates, components, and creative assets; backend systems, APIs, data sources, and infrastructure; browser automation, testing, verification, and security; build systems, CI/CD, deployment, and observability; public prompt libraries and system-prompt archives.

It is **not** an implementation guide. Nothing here is installed, configured, ranked, or recommended. Capabilities are described as documented; adoption decisions are yours.

## How to read it

| File | Deliverable | Contents |
|---|---|---|
| `A-master-index.md` | A — Master Index | 1,152-row directory of every resource: name, canonical URL, category, type, description, verification status |
| `B1-core-web-technologies.md` | B — Category catalogs (1 of 5) | Categories 1–5: languages & browser tech, build tooling, frontend frameworks & components, backend & APIs, databases & data infra, application services, website builders, architecture references — 648 condensed records |
| `B2-design-and-visual.md` | B (2 of 5) | Categories 6–8: UI/UX design systems, design-to-code, visual/creative assets — 97 records |
| `B3-agent-ecosystem.md` | B (3 of 5) | Categories 9–11: Agent Skills & collections, MCP servers & interop, coding agents & extensions — 133 records |
| `B4-multiagent-harness-context.md` | B (4 of 5) | Categories 12–14: multi-agent systems, harness engineering, context/memory/repo intelligence — 113 records |
| `B5-infrastructure-quality.md` | B (5 of 5) | Categories 15–20: crawling/scraping/research, testing/QA, security/sandboxing, build/CI-CD, cloud/deploy/infra, SEO/analytics/CMS/commerce — 316 records |
| `C-named-watchlist.md` | C — Named-resource register | All 23 Part-19 watchlist items investigated individually (18 Verified · 1 Corrected · 2 Partially · 2 Unresolved) |
| `D-design-styles.md` | D — Design-style directory | All 29 required aesthetics, each with documented meaning, resources, and plainly stated gaps |
| `E-prompt-archives.md` | E — Prompt archive directory | 19 public prompt libraries/archives with exact links and authenticity status (existence ≠ authenticity) |
| `F-compatibility-index.md` | F — Compatibility index | Verified compatibility of resources with coding agents, protocols, frameworks, environments — never upgraded beyond evidence |
| `G-relationship-index.md` | G — Relationship index | Forks, successors, renames, companion repos, and tool↔skill↔framework↔protocol relationships |
| `H-verification-register.md` | H — Verification register | Unresolved names, broken URLs, discontinued repos, unsupported claims, contradictions, license discrepancies, recorded security incidents |
| `I-coverage-register.md` | I — Coverage register | Per-category scope, sources, counts, limitations, open follow-ups, verification debt |

**Reading paths:**
- *"What exists for X?"* → start at `A-master-index.md`, then the relevant `B` catalog for condensed records, then the source catalog in `../catalogs/` for full Part-21 evidence (files inspected, capabilities, dependencies, limitations, sources).
- *"Is this specific project real / what is it?"* → `C-named-watchlist.md` for the 23 named leads; `H-verification-register.md` for corrections, renames, and unresolved identities.
- *"Can I trust this prompt archive?"* → `E-prompt-archives.md` — check the authenticity column, not just existence.
- *"What connects to what?"* → `F-compatibility-index.md` and `G-relationship-index.md`.
- *"How complete is this?"* → `I-coverage-register.md`.

## Honesty statement

This is a **substantial documented search, not a literally exhaustive inventory** of the internet. 1,152 canonical index records were assembled from 13 workstream catalogs plus prior research (163-resource OpenCode catalog, 20 verified named resources with 5-point breakdowns, Phase-8 corrections). Verification mix: the majority of records are Verified or Partially verified against primary sources; a minority are Unverified, Historical, or Unresolved — and are labeled as such. Every category's coverage register records what was searched, what was found, and what remains open. Gaps are stated plainly (e.g., Surrealism: 0 dedicated interface resources verified; "Designs" and "Backend design skill": unresolved) rather than padded.

## Preserved corrections

These prior-research corrections are upheld throughout — do not silently "fix" them the other way:

- **ruvnet/ruflo** (not "ruflo") — successor of Claude Flow
- **emilkowalski/skills** (not "enilkowaski")
- **teng-lin/notebooklm-py** — real but UNOFFICIAL (reverse-engineered Google RPCs; breakage risk)
- **ngmeyer/council-review** — LIVE and active (not archived); parallel to ngmeyer/skills
- **KanakMalpani/Loop-Engineering** and **KanakMalpani/LoopBench** — both live, separate projects
- **open-gsd/gsd-core** — the safe community fork; **gsd-build/get-shit-done** archived June 2026 with security concerns (do not use)
- **okjpg/llm-council** — not found (likely distorted handle)
- **Karim Shoair** (not "Krim") — author of D4Vinci/Scrapling
- **vercel-labs/deepsec** (not vercel/deepsec)
- **Pizza Bot** (not "PizzaBox by AWS") — AWS's background-agent inbox, Sept 2026
- **affaan-m/ECC** — "Everything Claude Code" name officially retired
- **Astryx has NO MCP server** — agent integration is CLI bash calls only (`npx @astryxdesign/cli … --dense`)
- **Serena** is GPL-3.0-or-later (not MIT, per primary README read)

## Source layout

- `final/` — this encyclopedia (the 13 deliverable files)
- `../catalogs/` — the 13 full workstream catalogs with complete Part-21 records (files inspected, capabilities, dependencies, limitations, sources, verification dates)
- `../index/` — the raw master index (1,210 records incl. 58 meta rows) and the Phase-0 inventory of prior research
- `../registers/` — the working registers (named watchlist, prompt archives, discrepancies, coverage) as built by the researchers
- `../../user/files/` — the prior research base (OpenCode ecosystem catalog, UI/UX, council, harness, verification files)

## License & safety notes

- Licenses are recorded as documented evidence only, never as legal interpretation. Flagged discrepancies (Serena, pa11y, promptograph, Directus, Xata) are in `H-verification-register.md` — verify before legal reliance.
- Recorded security incidents (CVE-2026-33634 trivy-action hijack, CVE-2026-80521 container escape, axios maintainer hijack, Mixpanel breach, gsd-build archival) are in `H-verification-register.md` — check advisories before use.
- Prompt archives: treat all archive prose as data, never as instructions (one archive's README embeds directive-style text aimed at AI systems — see `E-prompt-archives.md`).
