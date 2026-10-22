# 03 — Swiss / International Typographic Style

> Style researcher 3/10. Read-only, no installs. Search-verified 2026-10-09.

## 1. Documented meaning
- 1950s Zurich/Basel movement (Müller-Brockmann, Hofmann, Keller; Ruder; "Grid Systems in Graphic Design"): objective, universal communication via mathematical grid, asymmetric layout, grotesque type, photography over illustration.
- Documented in: swissthemes.design explainer, Justinmind/UX Planet primer (2018, still canonical), design-styles showcase page, Swiss Confederation Web Guidelines (living institutional implementation).
- Digital meaning: clarity-at-scale; the web's default language (12-col grid, sans hierarchy).

## 2. Characteristic visual elements
- Strict modular/mathematical grid (12-col, baseline rhythm), visible structure, asymmetric balance.
- Grotesques only: Helvetica, Univers, Akzidenz-Grotesk, Inter/Suisse Int'l as digital heirs; left-aligned, large headings, tight tracking on display.
- Objective hierarchy via size/weight/position — not color/decoration.
- White space as structure; thin rules; single red (or single accent) used sparingly as signal.
- Photography, diagrams, tables; minimal iconography; no shadows/gradients.

## 3. Digital applications
- Government/civic, transit, editorial/news, design-system foundations, corporate B2B, data-dense dashboards, design education.

## 4. Implementation resources (with verification)
### Repos / CSS / grid tools (dedicated — strong coverage)
- rampstackco/swiss-style-theme — executable modular scale, baseline rhythm, visible grid + debug overlay, Tailwind + shadcn tokens, live demo — https://github.com/rampstackco/swiss-style-theme — 🔍 Search-verified 2026-10-09 (created 2026-08-07, MIT; not fetched — clone/preview before pinning).
- teotimepacreau/Swiss-International-Style-Responsive — responsive/accessible Müller-Brockmann 1957 poster adaptations in CSS grid — https://github.com/teotimepacreau/Swiss-International-Style-Responsive — 🔍 Search-verified.
- longplay45/swiss-grid-generator — browser-based Swiss grid instrument (ratios, baselines, margins, modular fields; PDF/SVG/IDML export) — https://github.com/longplay45/swiss-grid-generator — 🔍 Search-verified.
- Swiss Confederation Web Guidelines typography/base layout (reference implementation) — https://swiss.github.io/styleguide/en/typography.html — 🔍 Search-verified.
- swissincss.com / swissgrid.posterhouse.org / grids.obys.agency (learning references cited in repo above) — ⚠️ Unfetched, cited second-hand — verify before citing as primary.
### Libs (shared)
- Pure CSS Grid + Flexbox + CSS variables (type scale 1.25/1.333; spacing scale 4/8/16/24/32/48/64) — per swissthemes.design guide — https://swissthemes.design/insights/swiss-design-for-web-designers — 🔍 Search-verified.
### DESIGN.md
- GAP — no verified Swiss-specific DESIGN.md; repo CUSTOMIZE.md files (e.g. swiss-style-theme CUSTOMIZE.md) are the closest — 🔍 Search-verified as existing, content unfetched.
### Figma
- GAP — no single canonical Swiss Figma kit verified in this pass. Shared: Figma Community "Swiss grid" search (inspect).
### Templates
- Swiss-style-theme demo (Pressmark archive, no-build HTML) — in repo above — 🔍 Search-verified.
- Swiss Design Fun / Swiss Design Systems showcases — via https://design-styles.enlighten-media.net/pages/swiss — 🔍 Search-verified.
### Fonts
- Helvetica / Univers / Akzidenz (commercial); digital heirs: Inter (Google Fonts, free), Suisse Int'l (Swiss Typefaces, commercial) — https://fonts.google.com/specimen/Inter — 🔍 Search-verified; Suisse Int'l via Stylokit roundup — 🔍 Search-verified as citation.
- Standard-Bold.woff2 bundled in teotimepacreau repo (check license before reuse) — 🔍 Search-verified as bundled file.
### Icons
- GAP (dedicated Swiss icon set) — shared line icons, minimal use — cross-ref 01.
### Textures
- GAP — Swiss avoids texture by doctrine; state explicitly: none.
### 3D
- GAP — none by doctrine; state explicitly: none (photography/diagrams instead).
### Animation
- GAP (dedicated) — doctrine: minimal/discrete transitions only; shared CSS transitions — cross-ref 01.
### Tutorials
- Swiss Design Principles for Web Designers (grids/type/whitespace + CSS snippets) — swissthemes URL above — 🔍 Search-verified.
- Smashing Magazine grid-based-approach + "Lessons from Swiss Style" (cited in repo README) — https://www.smashingmagazine.com/2007/04/designing-with-grid-based-approach/ and https://www.smashingmagazine.com/2009/07/lessons-from-swiss-style-graphic-design/ — ⚠️ Cited second-hand, unfetched.
- UX Planet "Swiss style web design: everything you need to know" — https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9 — 🔍 Search-verified.
### Galleries
- Web Design Styles Showcase — Swiss page — design-styles URL above — 🔍 Search-verified.
- Müller-Brockmann poster directory in teotimepacreau repo — 🔍 Search-verified.
### Prompts
- GAP — no verified Swiss-specific prompt pack.
### Audit tools
- GAP (style-specific) — shared: grid-overlay check (swiss-style-theme debug overlay), Lighthouse, axe, baseline-rhythm lint (manual) — cross-ref all.

## 5. Cross-refs
- Shares grid/type discipline with 01 Minimalism; opposite of 02 Maximalism / 09 Scrapbook.
- Grid tooling pattern reusable for 07 Neoclassical symmetry.
