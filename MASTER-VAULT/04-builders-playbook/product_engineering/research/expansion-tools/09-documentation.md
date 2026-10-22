# §30 — Documentation & Developer Portals (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## DC-01 — Mintlify — ACTIVE (acquiring; repriced 2026)
- Purpose / problem: Hosted docs-as-a-service: MDX-based docs sites with AI-assisted writing, API references from OpenAPI, custom React components, analytics.
- OSS/commercial: Commercial SaaS (proprietary). Starter $0; Pro paid — **repriced during 2026** (re-verify at decision time, per a Sep 2026 tooling evaluation).
- Maintenance: Active; **acquired Helicone (Mar 3, 2026)** — expanding from docs into AI/LLM observability.
- Limitations: Vendor lock-in (hosted, proprietary); migration cost high (conversion + lock-in per 2026 evaluation); AI extraction but no docstring renderer.
- Alternatives: Fern, Docusaurus, Starlight, GitBook.
- Switching costs: High (use OpenAPI as source of truth to stay portable — per dev.to practitioner advice).
- Use: U(Verified) — Trophy (dev.to case study) chose Mintlify for docs while managing SDKs with Fern.

## DC-02 — Fern — ACTIVE (acquired by Postman; OSS future unclear)
- Purpose / problem: API-first docs + SDK generation from an API definition (Fern definition or OpenAPI).
- OSS/commercial: Was commercial SaaS with OSS components; **acquired by Postman (Jan 2026)** — consolidation tracker notes "Fern's OSS future unclear."
- Maintenance: Under Postman (2026); watch for roadmap absorption into Postman's API platform.
- Limitations: Post-acquisition uncertainty; historically Fern-definition vs OpenAPI portability debate.
- Alternatives: Mintlify, Scalar, Redoc.
- Switching costs: Medium (OpenAPI source keeps you portable).
- Use: U(Proposed).

## DC-03 — Docusaurus — MAINTAINED (v4 stalled; feature freeze)
- Purpose / problem: React-based static docs sites with versioning, i18n (Meta).
- OSS/commercial: OSS MIT; self-hosted free.
- Maintenance: **Effectively feature-frozen on v3**: last stable **v3.9.2 (Oct 17, 2025)**; v4 umbrella issue (opened Feb 6, 2026) only **20% complete** (6/30), requires Node 24+/React 19.2+/TS 6+/Rspack v2 — no timeline announced. 64k stars, 414k npm/week, but migration momentum away is documented: Glasskube/Distr → Starlight (HN, May 2025), others → Fumadocs (OpenAPI, customization); 30+ minute builds on large sites reported.
- Limitations: Build performance at scale; v3 feature freeze; plugin maintenance costs estimated $500–2,000/mo (Featurebase).
- Alternatives: Starlight, Fumadocs, VitePress, Nextra.
- Switching costs: High (RST→MDX, JS toolchain).
- Use: U(Verified) — still the category star-count leader; widely deployed.

## DC-04 — Starlight (Astro) — ACTIVE
- Purpose / problem: Performance-first docs framework (Astro): zero client JS, 12kB bundle, 0.8s LCP.
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026); 2x YoY growth; the DX/performance leader per 2026 analyses.
- Limitations: Documentation-only (no marketing pages); no versioned docs (per community review); smaller npm footprint than Fumadocs.
- Alternatives: Fumadocs, VitePress, Docusaurus.
- Switching costs: High (from RST/Sphinx).
- Use: U(Verified) — Glasskube/Distr migration (HN May 2025, 58 pts).

## DC-05 — Fumadocs — ACTIVE
- Purpose / problem: Next.js-based docs framework; strong OpenAPI + customization story.
- OSS/commercial: OSS.
- Maintenance: Active (2026); leading Starlight on npm downloads.
- Alternatives: Starlight, Nextra.
- Use: U(Proposed).

## DC-06 — VitePress — ACTIVE
- Purpose / problem: Vue-powered static docs (Vite); 17k stars, 218k npm/week.
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026).
- Alternatives: Starlight, Docusaurus.
- Use: U(Proposed).

## DC-07 — MkDocs Material — ACTIVE (maintenance-mode claim disputed)
- Purpose / problem: Pythonic docs (Markdown + mkdocstrings); huge polish.
- OSS/commercial: OSS MIT; 26k stars.
- Maintenance: A 2026 catalog claimed "maintenance mode" — **the underlying evidence disputes it** (26k stars, 1 open issue cited as counter-evidence). Treat as active; the "maintenance mode" claim is contested.
- Alternatives: Sphinx, Docusaurus.
- Use: U(Proposed).

## DC-08 — Scalar — ACTIVE (rising)
- Purpose / problem: Modern API reference docs (OpenAPI); 14k stars; momentum vs Swagger UI stagnation.
- OSS/commercial: OSS.
- Maintenance: Active (2026); ranked as potentially #1–2 in API docs subcategory by 2026 momentum.
- Alternatives: Redoc, Swagger UI, Fern.
- Use: U(Proposed).

## DC-09 — DocsGPT — ACTIVE (AI-native wave)
- Purpose / problem: Open-source AI docs assistant (18k stars): chat over docs, AI-generated documentation.
- OSS/commercial: OSS.
- Maintenance: Active (2026); early leader of the AI-native docs wave (with Promptless YC W25, Context7).
- Alternatives: Mintlify AI, Inkeep.
- Use: U(Proposed). (Lightly researched — depth debt.)

## DC-10 — GitBook — ACTIVE
- Purpose / problem: Hosted docs collaboration with Git sync.
- OSS/commercial: Commercial (closed source); free OSS tier limited.
- Maintenance: Active (2026).
- Alternatives: Mintlify, Archbee.
- Use: U(Proposed). (Depth debt.)

## DC-11 — ReadMe — ACTIVE
- Purpose / problem: Interactive API docs hub with analytics.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Mintlify, Fern.
- Use: U(Proposed).

## DC-12 — llms.txt — EXPERIMENTAL (emerging standard)
- Purpose / problem: Proposed standard (Sep 2024→) for AI-consumable documentation (a /llms.txt manifest for agents).
- OSS/commercial: Open proposal.
- Maintenance: Emerging; slow adoption through 2026.
- Alternatives: Sitemap.xml, robots.txt conventions.
- Use: U(Proposed). (Lightly researched — depth debt.)

## Notable status findings (docs)
- **Postman acquired Fern (Jan 2026)** — OSS future unclear.
- **Mintlify acquired Helicone (Mar 2026)** — docs vendor expanding into LLM observability; repriced 2026.
- **Docusaurus v4 stalled** (20% complete, no timeline) — v3 feature freeze; Starlight/Fumadocs eating share.
- The category is splitting into three waves: mature (Docusaurus, Swagger UI), growth (Starlight, Fumadocs, VitePress, Scalar), AI-native (DocsGPT, llms.txt).

---

### Per-record metadata (condensed)
- Consolidation + wave analysis: github.com/bra1ndump/skillpack documentation agent runs (Mar 2026). Confidence: Medium (single research artifact, well-sourced internally).
- Docusaurus v4 stall: facebook/docusaurus issue #11719 + milestone (Feb 2026). Confidence: High (primary).
- Mintlify repricing: github.com/kgrizz-git/guiskindose documentation tooling evaluation (Sep 6, 2026). Confidence: Medium (single evaluation).
- Fern→Mintlify migration practice: dev.to (Trophy case study). Confidence: Medium.
- MkDocs Material maintenance dispute: bra1nDump findings. Confidence: Low–Medium (contested claim both ways).
