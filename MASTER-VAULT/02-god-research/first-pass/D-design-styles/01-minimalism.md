# 01 — Minimalism

> Style researcher 1/10. Read-only, no installs. Search + fetch verified 2026-10-09.

## 1. Documented meaning
- Design philosophy "less is more": remove everything non-essential until only content, whitespace, and minimal UI remain.
- Documented in: Dieter Rams "Less, but better", Apple HIG clarity/deference/depth, Google Material "content-first", Nielsen Norman Group minimalist-interface guidance.
- Digital meaning: low cognitive load, fast load, high legibility; restraint as luxury/trust signal.

## 2. Characteristic visual elements
- Generous whitespace / breathing room; single-column or quiet grid.
- Neutral palette: white, off-white, black, grays; one restrained accent max.
- System or neo-grotesque sans (Inter, SF Pro, Helvetica Now); tight type scale, large line-height.
- Flat surfaces, hairline dividers, no shadows or subtle shadows only; small radius (0–8px).
- Minimal iconography (line icons), no decoration, no gradients (or single subtle gradient).
- Visible focus states, high contrast maintained despite restraint.

## 3. Digital applications
- SaaS dashboards, docs sites, portfolios, checkout flows, government/medical (trust + clarity), mobile-first marketing pages.

## 4. Implementation resources (with verification)
### Repos / CSS frameworks (dedicated or directly usable)
- Pico CSS — class-light/semantic minimalist starter, light/dark auto, ~14.8k stars context — https://picocss.com/ — ✅ Fetched 200 on 2026-10-09 (note: banner says "no longer maintained", still usable, v2.1.1).
- MVP.css — minimalist stylesheet for HTML elements — https://github.com/andybrewer/mvp — 🔍 Search-verified via awesome-css-frameworks list 2026-10-09 (not fetched; re-check before use).
- Sakura / Simple.css / Water.css / Tacit — classless minimal tribe — index via https://github.com/troxler/awesome-css-frameworks — 🔍 Search-verified 2026-10-09.
- Milligram / Chota / Pure — ultra-light minimal grids — same awesome list above — 🔍 Search-verified.
- Minimalist (schalkneethling/minimalist) — namespaced custom-property minimal base — https://github.com/schalkneethling/minimalist — 🔍 Search-verified 2026-10-09.
- mincss (995 bytes) via cdnjs — https://cdnjs.com/libraries/min — 🔍 Search-verified.
### Libs (shared, cross-ref)
- Tailwind CSS + daisyUI minimal themes — https://daisyui.com/component-library/minimal-css-framework — 🔍 Search-verified. Cross-ref: also listed under other styles as shared utility base.
### DESIGN.md
- GAP — no style-dedicated DESIGN.md file verified. Do not substitute a generic design-system doc. Shared fallback: repo owner's own DESIGN.md conventions if present.
### Figma
- GAP — no single canonical "Minimalism" Figma kit verified. Shared: Figma Community search "minimal wireframe / minimal UI kit" (unverified set, inspect before use).
### Templates
- Pico examples — https://picocss.com/#examples (same domain as above) — 🔍 Search-verified.
- OnePageLove minimal templates (aggregator) — https://onepagelove.com (via bradtraversy/design-resources list) — 🔍 Search-verified as aggregator only.
### Fonts
- Inter (Google Fonts, OFL) — https://fonts.google.com/specimen/Inter — 🔍 Search-verified (Elementor/Stylokit/Onething roundups agree it is the default minimal UI font).
- System stack (-apple-system, "Inter", "SF Pro") — no URL; convention.
### Icons
- GAP (dedicated minimal icon set) — shared: Lucide / Feather line icons — https://lucide.dev / https://feathericons.com — 🔍 Search-verified as shared resources, not minimalism-exclusive. Cross-ref all styles.
### Textures
- GAP — minimalism by definition avoids textures. State explicitly: none.
### 3D
- GAP — no dedicated minimalism 3D pack verified. Shared if needed: Three.js (cross-ref Surrealism file).
### Animation
- GAP (dedicated minimal-motion lib) — shared: CSS transitions only / View Transitions API (MDN) — https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API — ⚠️ Unfetched, standard web API.
### Tutorials
- "20 Niche CSS Libraries for 2026" (classless minimalists section) — https://dev.to/butterflycss/20-niche-css-libraries-for-2026-f5 — 🔍 Search-verified 2026-10-09.
- Pico docs quick-start — https://picocss.com/docs — 🔍 Search-verified (linked from fetched homepage).
### Galleries
- MaxiBestOf (filter minimal) — https://maxibestof.one/websites/popular — 🔍 Search-verified.
- Dribbble tag minimalism / Behance minimal web — aggregator galleries, inspect recency — ⚠️ Unfetched.
### Prompts (AI builders)
- GAP — no verified minimalism-specific prompt pack. Shared pattern: "minimalist SaaS landing, single accent #..., Inter, 8pt spacing, no gradients" — author-written, not sourced.
### Audit tools
- GAP (style-specific) — shared: Lighthouse accessibility/performance, axe DevTools, prefers-reduced-motion check — standard tooling, cross-ref all styles.

## 5. Cross-refs
- Shared with all: Tailwind, Google Fonts/Inter, Lucide/Feather, Lighthouse/axe.
- Closest sibling: 03 Swiss (grid + grotesque type); contrast with 02 Maximalism.
