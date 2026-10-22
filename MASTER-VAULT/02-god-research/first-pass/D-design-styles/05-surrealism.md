# 05 — Surrealism (Dreamlike / Uncanny Web)

> Style researcher 5/10. Read-only, no installs. Search-verified 2026-10-09.

## 1. Documented meaning
- Art lineage (Breton 1924; Dalí/Magritte/Ernst: dream logic, uncanny scale, metamorphosis) transposed to interactive web: impossible physics, morphing bodies, floating fragments, dream navigation.
- Documented in: Detroit UX Style Encyclopedia entry "Dreamlike, uncanny, Magritte/Dalí imagery | Surrealism" — https://ux.detroit3d.com/styles/STYLE-INDEX.html — 🔍 Search-verified; Awwwards "Surreal WebGL Scroll Experience" (Organimo) as digital exemplar — 🔍 Search-verified.
- Digital meaning: wonder/memorability for brand/hero moments; high craft cost, high exclusion risk if overdone.

## 2. Characteristic visual elements
- Floating/disembodied objects, impossible scale, melting/morphing geometry, eyes/hands/cloud motifs.
- Mist/particle fields, liquid chrome, iridescent gradients, double-exposure collage.
- Non-linear scroll: scroll-driven metamorphosis, portal transitions, cursor-reactive dreamscapes.
- Distorted serif + grotesque type collisions;rêve-like copy fragments.

## 3. Digital applications
- Hero/experiential layers, fragrance/fashion/festival campaigns, portfolio showpieces, WebGL product configurators with dream coat, installation companion sites.

## 4. Implementation resources (with verification)
### Repos / CSS
- GAP — no dedicated surrealism CSS framework verified (correctly: the style lives in WebGL/shader/canvas, not stylesheets). Do not pad with generic UI kits.
### Libs / 3D / animation (shared but primary here — strong coverage)
- Three.js (WebGL/WebGPU) — https://threejs.org + resources hub https://threejsresources.com/tool/three-js — 🔍 Search-verified.
- MDN "Building up a basic demo with Three.js" (r185, 2026-updated) — https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_on_the_web/Building_up_a_basic_demo_with_Three.js — 🔍 Search-verified.
- React Three Fiber / drei / GSAP ScrollTrigger / Lenis smooth scroll / GLSL shaders — standard experiential stack — 🔍 Search-verified as ecosystem (threejsresources showcase tags: GSAP 22, R3F 15, GLSL 2).
- Showcase refs: threejsresources showcase https://threejsresources.com/showcase + Awwwards surreal WebGL scroll piece https://www.awwwards.com/inspiration/surreal-webgl-scroll-experience-organimo — 🔍 Search-verified.
### DESIGN.md
- GAP — no verified surrealism DESIGN.md.
### Figma
- GAP — Figma cannot author real surreal WebGL; moodboard-only use. No dedicated kit verified.
### Templates
- GAP (dedicated surreal template pack) — direction: Three.js examples / Bruno Simon-style portfolio forks (inspect licenses individually; none pinned here).
### Fonts
- GAP (dedicated) — direction: high-contrast display serifs + grotesques; license per project.
### Icons
- GAP — custom SVG/cursor artifacts per piece; no pack verified.
### Textures
- GAP (single verified pack) — direction: grain/gradient-mesh/cloud PNG + procedural GLSL noise; no canonical pack pinned.
### Tutorials
- MDN Three.js demo guide (above) + three.js manual fundamentals https://threejs.org/manual/#en/fundamentals — 🔍 Search-verified (cited in Medium intro excerpt).
- three.js forum showcase/discourse (shader/particle threads) — https://discourse.threejs.org/t/interactive-webgl-visuals-portfolio/87771 — 🔍 Search-verified.
### Galleries
- Awwwards surreal tag + threejsresources showcase (above) — 🔍 Search-verified.
- webgpu.com Three.js articles (131 articles) — https://www.webgpu.com/tag/three-js — 🔍 Search-verified as aggregator.
### Prompts
- GAP — no verified surreal-web prompt pack (image-gen prompts exist for stills, not verified for interactive builds; do not conflate).
### Audit tools
- GAP (style-specific) — shared: Lighthouse perf (WebGL weight), prefers-reduced-motion gate, axe; context-loss handling per three.js forum thread — 🔍 Search-verified as risk source.

## 5. Cross-refs
- Shares experiential stack with 09 Scrapbook (collage planes) and 02 Maximalism (excess), but dream-logic rather than density-logic.
- Feasible fallback when WebGL budget missing: CSS-only parallax collage (see 09).
