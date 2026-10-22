# 10 — Glassmorphism (Frosted Glass)

> Style researcher 10/10. Read-only, no installs. Search + fetch verified 2026-10-09.

## 1. Documented meaning
- Post-2020 trend (Michal Malewicz popularization; Apple Big Sur / Fluent / visionOS halo): translucent frosted surfaces floating over vivid backgrounds — background-blur + saturation + hairline light border.
- Documented in: css.glass generator docs/README, Figma plugin descriptions ("blurred semi-transparent backgrounds overlaid… floating above"), Detroit encyclopedia "Frosted glass, translucent panels, visionOS-like | Glassmorphism" — 🔍 Search-verified.
- Digital meaning: premium depth/layering for dashboards, navs, modals, music/fintech cards; perf + contrast risks if overused.

## 2. Characteristic visual elements
- Core recipe: `background: rgba(255,255,255,0.1–0.3); backdrop-filter: blur(10–20px) saturate(150%); border: 1px solid rgba(255,255,255,0.2–0.4); radius 12–24px; soft shadow`.
- Vivid gradient/mesh/photo background required (glass invisible on flat gray).
- Light hairline top-highlight; floating stacked panels; vibrant accent glows behind glass.
- Clean grotesque type in high-contrast white/ink; icon chips in glass pills.

## 3. Digital applications
- SaaS dashboards, nav bars/docks, login/pricing cards, music/weather widgets, crypto/fintech hero cards, visionOS-style spatial panels.

## 4. Implementation resources (with verification)
### Repos / generators (dedicated — strong)
- miketromba/css.glass — The Glassmorphism CSS Generator (Nuxt; 453★) — repo https://github.com/miketromba/css.glass — ✅ Fetched 200 (repo live) on 2026-10-09; app https://css.glass — 🔍 Search-verified as linked product (open to confirm deploy).
- R3DHULK/glassmorphism-generator — playground w/ presets (Subtle/Medium/Heavy/Frosted/Neon), CSS/SCSS/Tailwind/React export, dark/light test — https://github.com/R3DHULK/glassmorphism-generator — 🔍 Search-verified (2★ micro-repo — review).
- crisgea71/premium-glassmorphism-css-generator — interactive premium frosted tool (blur/opacity/radius/border/shadow/moods; live Render demo) — https://github.com/crisgea71/premium-glassmorphism-css-generator — 🔍 Search-verified (0★ micro-repo — review).
- rahuldotdev/glassmorphism — vanilla-CSS + Tailwind examples + Figma how-to file ref — https://github.com/rahuldotdev/glassmorphism — 🔍 Search-verified.
- ui.glass — "definitive CSS UI library for glassmorphism" (Themesberg; free/open-source claim; page currently email-gated pre-launch per excerpt) — https://ui.glass/ — 🔍 Search-verified as claimed, ⚠️ verify library actually downloadable before depending on it.
- DEV roundup Glass.css niche lib mention — via https://dev.to/butterflycss/20-niche-css-libraries-for-2026-f5 — 🔍 Search-verified as citation only (no repo pinned — do not present as verified lib).
### Libs (shared)
- Pure CSS `backdrop-filter` (+ `-webkit-` prefix); Tailwind `backdrop-blur/border-white/10` utilities — standard.
### DESIGN.md
- GAP — no verified glassmorphism DESIGN.md.
### Figma (dedicated — strong)
- Glassmorphism plugin (150k users, free) — https://www.figma.com/community/plugin/1197106608665398190/glassmorphism — 🔍 Search-verified.
- Glassmorphism Generator — Glass UI Generator (4.6k users, paid $12, auto-CSS export) — https://www.figma.com/community/plugin/1470352705474650465/glassmorphism-generator-glass-ui-generator — 🔍 Search-verified.
- Glassmorphism Dashboard UI Kit (+ Liquid Glass variant) — https://www.figma.com/community/file/1514405085901665002/glassmorphism-dashboard-ui-kit and https://www.figma.com/community/file/1000819307361089284/glassmorphism — 🔍 Search-verified as listed files (inspect version/covers).
### Templates
- rahuldotdev css-examples/twcss-examples (above) — 🔍 Search-verified.
- R3DHULK interactive gallery + presets (above) — 🔍 Search-verified.
### Fonts
- GAP (dedicated) — doctrine: clean grotesques (Inter/SF shared) — cross-ref 01.
### Icons
- GAP (dedicated) — shared Lucide in glass chips — cross-ref.
### Textures
- GAP as pack — background-side only: gradient-mesh/photo required; use licensed Unsplash/Pexels or CSS mesh gradients — shared direction, no canonical pack pinned.
### 3D
- GAP (dedicated glass-3D pack) — shared Three.js glossy-blob backdrops if needed — cross-ref 05.
### Animation
- GAP (dedicated) — R3DHULK float/pulse/shake toggles (above) + shared CSS transitions; keep blur static during scroll for perf.
### Tutorials
- R3DHULK README customization/code-export guide (in repo) — 🔍 Search-verified.
- rahuldotdev article + Figma how-to file (referenced in its README) — 🔍 Search-verified as referenced, article URL unfetched — verify.
- Browser compat note: Chrome 76+/Safari 13.1+/Edge 79+/Firefox 70+ (per R3DHULK README) — 🔍 Search-verified; test `backdrop-filter` fallbacks (`@supports`) — author rule.
### Galleries
- css.glass / generator galleries (above) — 🔍 Search-verified.
- Awwwards/Dribbble "glassmorphism" tags — aggregators, inspect recency.
### Prompts
- GAP — no verified glassmorphism prompt pack.
### Audit tools
- GAP (style-specific) — shared: axe contrast (glass text fails often — put solid scrim behind text), Lighthouse (blur cost), `@supports (backdrop-filter)` fallback lint (manual) — cross-ref.

## 5. Cross-refs
- Frosted sibling-rival of 08 Neumorphism (both depth, opposite means); floats over 02 Maximalism-grade vivid grounds; restraint cousin of 01 Minimalism when used as single nav/card layer.
