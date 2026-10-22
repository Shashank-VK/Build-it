# 08 — Visual Assets (icons, SVG, fonts, 3D, shaders, optimization, licenses)

> Method: read-only WebSearch + WebFetch (no install/execute). Verified 2026-10-09 (UTC).
> Record spec (same as 06): `Name | URL | Type | Description | License (as stated) | Restrictions/Notes (docs scope only) | Agent/CLI integration`

## A. Icons / SVG sets

### 01. Lucide (lucide-icons/lucide)
- URL: https://github.com/lucide-icons/lucide
- Type: Icon library (ISC, Feather fork lineage)
- Description: ~1.5k+ stroke icons; React/Vue/Svelte/TS-native packages; Figma + IconSearch exports.
- License: ISC for icons listed (as stated in LICENSE + lucide.dev/license).
- Restrictions/Notes: Copyright notice + permission notice retention per ISC; no attribution display required beyond notice.
- Agent/CLI integration: npm (`lucide-react`, etc.); copy-as-JSX/SVG pipelines.

### 02. Heroicons (tailwindlabs/heroicons)
- URL: https://github.com/tailwindlabs/heroicons
- Type: Tailwind Labs hand-crafted SVG set (outline/solid/mini)
- Description: 24px grid, MIT; React/Vue components.
- License: MIT (as stated).
- Restrictions/Notes: No attribution required; Tailwind trademarks excluded.
- Agent/CLI integration: npm (`@heroicons/react/vue`).

### 03. Tabler Icons (tabler/tabler-icons)
- URL: https://github.com/tabler/tabler-icons
- Type: 6,100+ MIT stroke icons (24×24, 2px)
- Description: Webfont + SVG + React/Vue/Svelte; font-forge build.
- License: MIT (as stated).
- Restrictions/Notes: Stroke-width customization supported; keep LICENSE notice on redistribute.
- Agent/CLI integration: npm (`@tabler/icons-react`, etc.).

### 04. Phosphor Icons (phosphor-icons)
- URL: https://github.com/phosphor-icons/homepage (weights in `phosphor-icons/core`)
- Type: Flexible 6-weight family (thin→fill, duotone)
- Description: 10k+ variants; React/Vue/Flutter/Swift.
- License: MIT (as stated).
- Restrictions/Notes: No attribution required.
- Agent/CLI integration: npm (`phosphor-react`, `@phosphor-icons/react`).

### 05. Feather Icons (feathericons/feather) — maintenance mode
- URL: https://github.com/feathericons/feather
- Type: Minimal predecessor set (286 icons)
- Description: Basis for Lucide; still widely vendored.
- License: MIT (as stated).
- Restrictions/Notes: Unmaintained upstream — prefer Lucide for new work.
- Agent/CLI integration: npm (`feather-icons`).

### 06. Bootstrap Icons (twbs/icons)
- URL: https://github.com/twbs/icons
- Type: 2,000+ MIT SVG set
- Description: Webfont + SVG sprite + Figma.
- License: MIT (as stated).
- Restrictions/Notes: Bootstrap trademark excluded.
- Agent/CLI integration: npm (`bootstrap-icons`).

### 07. Remix Icon (Remix-Design/RemixIcon)
- URL: https://github.com/Remix-Design/RemixIcon
- Type: 2,800+ outlined/filled glyphs
- Description:SVG + iconfont.
- License: Apache-2.0 (as stated).
- Restrictions/Notes: Apache patent grant/notice rules apply.
- Agent/CLI integration: npm (`remixicon`).

### 08. Material Symbols / Material Icons (Google)
- URL: https://fonts.google.com/icons / https://github.com/google/material-design-icons
- Type: Variable-font icon system (weight/fill/grade/size axes)
- Description: 15k+ (Symbols Light) glyphs, 24px grid, SVG + variable fonts.
- License: Apache-2.0 (as stated on Fonts + GitHub).
- Restrictions/Notes: Google trademarks excluded; variable axes need supporting stack.
- Agent/CLI integration: npm (`material-symbols`), fontsource mirrors.

### 09. Simple Icons (simple-icons/simple-icons) + Skill/Devicon sets
- URL: https://github.com/simple-icons/simple-icons
- Type: Brand/SVG logos set
- Description: 3k+ brand marks (single-color SVG).
- License: CC0-1.0 for data (as stated) — high trademark risk: brand rights remain.
- Restrictions/Notes: Trademark risk HIGH (per fullsvgicons matrix); do not imply endorsement; verify each brand's guidelines.
- Agent/CLI integration: npm (`simple-icons`); SVGO-managed.

### 10. Font Awesome Free (FortAwesome/Font-Awesome)
- URL: https://github.com/FortAwesome/Font-Awesome
- Type: Freemium icon set (Free vs Pro)
- Description: Solid/regular/brands, SVG + webfont + kits.
- License: Free: Icons CC-BY-4.0, code MIT (as stated); Pro proprietary.
- Restrictions/Notes: CC-BY attribution REQUIRED for Free icons (docs/credits); Pro needs paid license/seats.
- Agent/CLI integration: npm (`@fortawesome/*`); Kit CDN.

## B. Fonts / type delivery

### 11. Google Fonts (platform)
- URL: https://fonts.google.com
- Type: Font catalog + hosting API
- Description: Variable + static families; CSS2 API, `display=swap` patterns.
- License: Per-family (majority SIL OFL-1.1; some Apache-2.0; Ubuntu Ubuntu Font License 1.0) — check family page.
- Restrictions/Notes: OFL forbids selling font alone, reserves names; embedding generally allowed; always read family license.
- Agent/CLI integration: `google-fonts-helper`, `fontsource` mirrors, `next/font/google`.

### 12. Fontsource (fontsource/fontsource)
- URL: https://github.com/fontsource/fontsource
- Type: Self-host font packager (npm, zero-layout-shift)
- Description: 1.5k+ families as npm packages with unicode subsets/weights.
- License: Wrapper MIT; fonts retain upstream OFL/Apache/Ubuntu licenses (per README + per-package README).
- Restrictions/Notes: "Always read license for each font" (per README); subsetting does not change font license.
- Agent/CLI integration: npm (`@fontsource/*`); CLI scaffolds in repo.

## C. 3D / emoji / illustration packs

### 13. 3dicons (realvjy/3dicons, 3dicons.co)
- URL: https://github.com/realvjy/3dicons / https://3dicons.co
- Type: Blender-rendered 3D icon renders (1500+ on site)
- Description: 4 styles × 3 camera angles; Figma/Sketch/XD + PNG/Blend.
- License: CC0-1.0 Universal (as stated in repo + site: no attribution required).
- Restrictions/Notes: CC0 waives copyright but not trademark/model rights; premium renders on site may differ — check pack page.
- Agent/CLI integration: Direct download; no CLI.

### 14. Quaternius (quaternius/quaternius)
- URL: https://quaternius.com (GitHub mirror)
- Type: Pixel/game 3D + 2D packs
- Description: Modular characters/tiles/items, Godot/Unity-ready.
- License: CC0-1.0 (as stated) — Unverified in this pass, check pack LICENSE.
- Restrictions/Notes: No attribution required per CC0 claim; verify before commercial game use.
- Agent/CLI integration: Direct ZIP; itch.io mirrors.

### 15. Twemoji-based 3D emoji generator (papiguy/3d-emoji-assets-generator)
- URL: https://github.com/papiguy/3d-emoji-assets-generator
- Type: SVG→extruded 3D emoji (GLB/OBJ/STL/USDZ) + CLI batch
- Description: Twemoji SVG → `ExtrudeGeometry`, single-material atlas option; 4,009 prebuilt GLBs (bubble/coin/flat).
- License: Code MIT; Graphics CC-BY-4.0 (Twemoji by Twitter/X Corp) — see LICENSE + LICENSE-GRAPHICS.
- Restrictions/Notes: Distributing generated assets REQUIRES Twemoji attribution (per README).
- Agent/CLI integration: Browser app (emoji3d.org) + CLI batch; Three.js pipeline.

## D. Shaders / gradient surfaces (static + live)

### 16. Okaybabe Shaders (Okay-Babe/okaybabe-shaders, npm `@okaybabe/shaders`)
- URL: https://github.com/Okay-Babe/okaybabe-shaders
- Type: 13 hand-authored GLSL background shaders (zero-dep React + optional R3F)
- Description: Aperture Bloom, Halation, Quarry, Opt, Fox-cycle, Hess weave, Chroma Bleed, Membrane, etc.; raw `.glsl` + wrappers + MP4 previews; DPR 65%, triple-gate loop, reduced-motion + no-WebGL CSS fallback.
- License: MIT (as stated: free personal/commercial, no attribution).
- Restrictions/Notes: Brand-prismatic anchored to `#7C3AED/#6366F1`; r3f needs `outputColorSpace LinearSRGB` for color accuracy (per README).
- Agent/CLI integration: npm import (3-line) + `/r3f` subpath (peer `three`, `@react-three/fiber`).

## E. Optimization / delivery

### 17. SVGO (svg/svgo)
- URL: https://github.com/svg/svgo
- Type: SVG optimizer CLI + lib
- Description: Plugin pipeline (remove dims, minify, prefix IDs); config `svgo.config.js`.
- License: MIT (as stated).
- Restrictions/Notes: Multipass can break references/animations — test `cleanupIds` on sprites.
- Agent/CLI integration: CLI (`npx svgo`), Node API, bundler plugins.

### 18. Squoosh (GoogleChromeLabs/squoosh) + Sharp (lovell/sharp)
- URL: https://github.com/GoogleChromeLabs/squoosh / https://github.com/lovell/sharp
- Type: Image encode/compare app + high-perf Node pipeline
- Description: Squoosh: browser MozJPEG/WebP/AVIF compare; Sharp: libvips resize/convert pipeline.
- License: Squoosh Apache-2.0; Sharp Apache-2.0 (as stated).
- Restrictions/Notes: Sharp native binary (libvips) per platform; AVIF encode slow — gate in CI.
- Agent/CLI integration: Squoosh CLI (`@squoosh/cli`); Sharp API/CLI in build scripts.

### 19. ImageOptim / Trimage lineage (GUI) — note
- URL: https://imageoptim.com
- Type: Proprietary-freemium GUI (macOS) + open batch alternatives
- Description: Lossy/lossless batch; EXIF strip option.
- License: Proprietary (app) — do not treat as OSS; prefer Sharp/Squoosh for pipelines.
- Restrictions/Notes: Check per-version terms; stripping metadata may affect rights info.
- Agent/CLI integration: No OSS CLI; script via Sharp instead.

### 20. IconSearch + FullSVGIcons license matrices (reference, not asset)
- URL: https://iconsearch.info/licenses / https://fullsvgicons.com/licenses
- Type: License-comparison references (229 packs / SPDX matrix)
- Description: Side-by-side MIT/ISC/Apache/CC-BY/CC0, attribution flags, trademark-risk flags, bundle weights.
- License: Site content proprietary; data points to upstream licenses.
- Restrictions/Notes: Use only as pointer — always confirm in upstream repo LICENSE before shipping (matrix may lag).
- Agent/CLI integration: Browser studio (size/stroke/color → React/Vue/Svelte/PNG/WebP/SVG).

---
Counts: 20 records (01–20).
