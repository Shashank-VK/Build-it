# IBM Carbon — product engineering case study (design system at enterprise scale)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Carbon is IBM's open-source design system — the exemplar of *token-driven theming at enterprise scale* (4 themes, semantic tokens, 14,866 commits, 1,087 releases in the monorepo). This file is built substantially from the primary source: the public GitHub repo itself (fetched 2026-10-10). Carbon Next (v12, "AI design intelligence" + MCP) is covered as the current frontier — with the marketing audited.

## 1. Forensic reconstruction — how the machine actually works

### The repo as the machine (primary evidence)
- Claim: Carbon is a **monorepo** (github.com/carbon-design-system/carbon, created 2017, Apache 2.0) containing: `@carbon/react` (React components + styles), `@carbon/web-components` (standards-based web components), `@carbon/styles` (Sass), `@carbon/themes`, `@carbon/colors`, `@carbon/type` (tokens paired with IBM Plex), `@carbon/grid`, `@carbon/layout`, `@carbon/motion`, `@carbon/icons`, `@carbon/pictograms`, `@carbon/elements` (foundations). Community-maintained Angular/Svelte/Vue bindings exist. Label: **Verified** — repo README fetched 2026-10-10. 9,533 stars, 2,283 forks, 14,866 commits, 1,087 releases (weak signals, recorded as such).
- Claim: The governance surface is visible in the repo: CONTRIBUTING.md, GitHub Discussions, a Discord community, Code of Conduct, OpenSSF Best Practices badge, CI workflows, e2e (Playwright) + unit (Jest) configs, and an **AGENTS.md** at repo root — the design system is maintained with AI-agent contribution in mind. Label: **Verified** (repo file listing). The AGENTS.md is a nice forensic detail: the system documents itself for machine contributors.

### The token machine: 4 themes, semantic layers
- Claim: Carbon's theming runs on **design tokens** in three layers — global (raw values) → alias → semantic (e.g., `background`, `text-primary`) — with **4 themes** (White/G10/G90/G100: two light, two dark/gray). Products theme by swapping token values, not by overriding CSS. Label: **Corroborated** — carbondesignsystem.com docs (via the bothsides-platform-dev skill notes on color themes); consistent with the `@carbon/themes` package. Confidence: high on the structure; medium on exact theme names' currency (v12 may revise).
- Claim: **Carbon Next (v12)** introduces token-naming conventions, an "AI design intelligence" layer, and **MCP (Model Context Protocol)** exposure — plus open-sourcing an internal library (reported as 21 components / 24 patterns). Label: **Corroborated** — carbondesignsystem.com/carbon-next; secondary AI-design-resources notes. Confidence: medium (announcement-grade; implementation depth Unknown).

### The adoption machine
- Claim: Carbon's adoption model is *open-source + IBM-internal mandate*: it's public (anyone can use it) but its primary user is IBM's own product portfolio — the dogfooding loop is the whole company. Label: **Inferred** — consistent with the repo's scale and IBM's public positioning; internal adoption metrics not public. Confidence: medium.

## 2. Postmortem record — failures hunted down
- **No public incident postmortems found** for Carbon as a system (it's a component library; its "incidents" are breaking changes). **Verified-absent**.
- **The breaking-change record as postmortem proxy:** 1,087 releases and major-version migrations (v10 → v11 → v12/Next) are where design-system failures live — migration pain, token renames, component API churn. No consolidated public postmortem of a Carbon migration was found this pass; the *migration guides* in the repo (README links "Migrate") are the institutional memory. Label: **Inferred**; gap recorded.
- **Version-fragmentation risk (structural):** with 1,087 releases across a decade, IBM products inevitably run mixed Carbon versions — the classic enterprise design-system failure (the system exists, but the portfolio doesn't converge on it). Whether IBM has converged is **Unknown** — no public audit found.

## 3. Narrative audit — dismantling with receipts
- **"AI design intelligence" — audit the adjective.** Carbon Next's headline is AI-flavored (MCP exposure, "design intelligence"). The receipts: what's verifiable is *machine-readable exposure* of tokens/components (MCP server, AGENTS.md, structured docs) — genuinely useful, genuinely new. What's not verified: anything deserving the word "intelligence" (generative UI? autonomous theming? unproven). The dismantling: strip "AI" and the substance is *excellent API hygiene for agents* — which is the actual story and doesn't need the adjective. Label: **Inferred** (audit synthesis) on **Verified** repo evidence.
- **Open-source as governance theater?** Carbon is Apache-2.0 and genuinely public — but its roadmap is set by IBM's needs, and community PRs flow into IBM's release train. The audit: "open source" here means *source-available and reusable*, not *community-governed*. That's fine — but teams citing Carbon as "community-driven design" should note the steering wheel stays in Armonk. Contrast with genuinely community-governed systems. Label: **Inferred**.
- **The monorepo's honest cost.** 14,866 commits and 1,087 releases across a dozen packages is also a *coordination surface*: every token change fans out across React, web components, Angular/Vue/Svelte community bindings, and IBM's products. The repo's sophistication (Lerna, Nx, multi-framework builds) is the price of the scale story. Small teams copying "monorepo all the things" should price the release-train machinery, not just the folder structure. Label: **Inferred** on **Verified** repo structure.
- **Token layers as the real transferable idea.** Beneath the marketing, the durable contribution is the three-layer token model (global → alias → semantic) with 4 swappable themes — the mechanism that makes dark mode, white-labeling, and accessibility contrast requirements *configuration* instead of *rewrites*. That's the piece worth stealing, and it predates the AI narrative by years. Label: **Inferred**; the token structure is **Corroborated**.

## Transferable lessons
1. **Tokens in three layers** (raw → alias → semantic) turn theming, dark mode, and rebrands into configuration. This is the single most portable idea in the file.
2. **Document for machine contributors.** AGENTS.md at the repo root + MCP exposure is the 2026 version of CONTRIBUTING.md — design systems now onboard agents, not just humans.
3. **Dogfood at company scale.** A design system's quality is bounded by its hardest internal customer; mandate internal adoption before claiming external success.
4. **Open-source ≠ community-governed.** Be explicit about who steers the roadmap; "public" and "participatory" are different claims.
5. **Migration guides are the postmortems.** For component libraries, the breaking-change migration doc is where the failure learning lives — write them like postmortems, not changelogs.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| CB1 | Monorepo contents, packages, community, governance files (primary) | https://github.com/carbon-design-system/carbon | Primary technical (repo) | IBM Carbon team | Live (fetched 2026-10-10) | 2026-10-10 | High |
| CB2 | Carbon Next: AI design intelligence, MCP, token naming, open-sourcing internal library | https://www.carbondesignsystem.com/carbon-next | Primary (announcement) | IBM Carbon | n.d. (2025–2026) | 2026-10-10 | Medium (announcement-grade) |
| CB3 | Color themes; token structure notes | https://github.com/bothsides-platform-dev/both-sides/blob/HEAD/.claude/skills/ibm-carbon-design-system/rules/color-themes.md | Secondary (skill notes) | bothsides-platform-dev | n.d. | 2026-10-10 | Low-medium |
| CB4 | AI design-system research context (Carbon/Atlassian/Adobe comparison) | https://github.com/atebit/ai-product-design-resources/blob/HEAD/docs/research/foundational/02-ai-design-systems.md | Secondary synthesis (GitHub) | atextit | n.d. | 2026-10-10 | Low-medium |

**Gaps:** v10→v11→v12 migration postmortems (not found); IBM internal adoption/convergence metrics (Unknown); Carbon Next implementation depth (announcement-grade only).
