# 08 — Neumorphism (Soft UI / Neomorphism)

> Style researcher 8/10. Read-only, no installs. Search + fetch verified 2026-10-09.

## 1. Documented meaning
- 2019–2020 trend (Alexander Plyuto concept; popularized by neumorphism.io): skeuomorphism + flat hybrid — surfaces extruded from background via dual opposing soft shadows (light + dark) on same-hue ground.
- Documented in: neumorphism.io "What is Neumorphism?" explainer (on-page) — ✅ Fetched (page live, generator present); MDN-adjacent coverage; Detroit UX encyclopedia "Soft extruded shapes, soft UI | Neumorphism" entry — 🔍 Search-verified.
- Digital meaning: tactile calm for dashboards/music/health apps; notorious a11y weakness (low contrast) — use for decoration, never sole affordance.

## 2. Characteristic visual elements
- Monochromatic ground (#e0e0e0 archetype); elements same-color as background, defined only by `box-shadow: light + dark` pairs.
- Large radii (16–50px), pill sliders, concave (inset) vs convex (raised) states; no borders.
- Pastel/low-saturation palette; soft blurred shadows (high blur, low opacity); inner-highlight top-left lighting (consistent angle).
- Minimal flat icons embossed/debossed; quiet sans type; low visual noise.

## 3. Digital applications
- Music players, smart-home controls, fitness cards, settings panels, calculator/keypad UIs, dark-mode soft dashboards.

## 4. Implementation resources (with verification)
### Repos / CSS libs (dedicated — strong)
- adamgiebl/neumorphism — neumorphism.io generator source (React, 6.1k★/326 forks) — https://github.com/adamgiebl/neumorphism — 🔍 Search-verified.
- pulkit-jasti/neumorphism-css-code-generator — alt generator — https://github.com/pulkit-jasti/neumorphism-css-code-generator (live: https://neumorphism-generator.netlify.app/) — 🔍 Search-verified.
- ismail9k/neomorphism — UI components library in neomorphism style (npm `neomorphism`) — https://github.com/ismail9k/neomorphism — 🔍 Search-verified (59★, dated — review).
- jsanchez91/neumo-ui — modern neumorphism CSS lib: light/dark via `light-dark()`, directional lighting attrs, theme files, pure CSS — https://github.com/jsanchez91/neumo-ui + docs https://jsanchez91.github.io/neumo-ui — 🔍 Search-verified.
- neumorphic-ui (Tailwind v4 + Base UI, WAI-ARIA, shadcn `add` support) — https://neumorphic-ui.vercel.app/ — 🔍 Search-verified.
- gutbits/ui-design-demos neumorphism demo page — https://github.com/gutbits/ui-design-demos/blob/main/trends/neumorphism.html — 🔍 Search-verified.
### Generators (dedicated)
- https://neumorphism.io/ — ✅ Fetched 200 (generator live; copy-paste `box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff` archetype confirmed in search excerpt).
### DESIGN.md
- GAP — no verified neumorphism DESIGN.md; neumo-ui docs page is closest procedural doc — 🔍 Search-verified as existing.
### Figma
- GAP — no canonical neumorphism Figma kit verified this pass (keyword "Shadow UI" in DEV roundup hints at depth-focused libs — ⚠️ second-hand, verify). Shared: Figma inner/outer shadow recipes.
### Templates
- neumorphism.io community gallery ("Browse all" + per-user Get code links, e.g. 97K-view top) — ✅ Fetched as existing section.
### Fonts
- GAP (dedicated) — doctrine: quiet rounded sans (Nunito, Quicksand, Poppins via Google Fonts, shared) — cross-ref.
### Icons
- GAP (dedicated embossed set) — shared Lucide/Feather rendered same-color + shadows — cross-ref 01.
### Textures
- GAP — doctrine forbids texture (same-hue plastic only). State explicitly.
### 3D
- GAP — faux-3D via shadows only; no WebGL pack (correctly none).
### Animation
- GAP (dedicated motion lib) — convention: shadow-swap press states (`.nui-clickable`), soft transitions; no verified lib.
### Tutorials
- neumo-ui docs (intro/features/customization/themes) — docs URL above — 🔍 Search-verified.
- DEV "20 Niche CSS Libraries" Shadow UI mention — https://dev.to/butterflycss/20-niche-css-libraries-for-2026-f5 — 🔍 Search-verified as citation only.
### Galleries
- neumorphism.io gallery (above) — ✅ Fetched.
- Uiverse.io neumorphic elements (linked from neumorphism.io footer) — https://uiverse.io — 🔍 Search-verified as linked domain.
### Prompts
- GAP — no verified neumorphism prompt pack.
### Audit tools
- GAP (style-specific) — shared axe color-contrast (will flag neumorphic text — expected), Lighthouse; author rule: never convey state by shadow alone — cross-ref all.

## 5. Cross-refs
- Shadow grammar contrasts 04 Brutalism (hard) and 06 Neo-brutalism (hard offset); frosted competitor is 10 Glassmorphism; tactile competitor is claymorphism (out of scope).
