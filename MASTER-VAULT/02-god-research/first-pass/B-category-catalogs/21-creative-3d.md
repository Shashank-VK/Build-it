# 21 — Creative 3D (SVG/Canvas/WebGL/Three.js/R3F/shaders/particles/maps, templates)

> Method: read-only WebSearch + WebFetch (no install/execute). Verified 2026-10-09 (UTC).
> Record spec (same as 06): `Name | URL | Type | Description | License (as stated) | Restrictions/Notes (docs scope only) | Agent/CLI integration`

## A. Foundations — SVG / Canvas / WebGL

### 01. Three.js (mrdoob/three.js)
- URL: https://github.com/mrdoob/three.js
- Type: WebGL/WebGPU renderer + scene graph (foundation for all below)
- Description: Geometries, materials, lights, loaders (GLTF/FBX), `examples/jsm` postfx/controls.
- License: MIT (as stated).
- Restrictions/Notes: Third-party model/texture licenses separate; `three >=0.160` needed for WebGPU paths.
- Agent/CLI integration: npm (`three`, `@types/three`); Vite/Next templates.

### 02. React Three Fiber (pmndrs/react-three-fiber)
- URL: https://github.com/pmndrs/react-three-fiber
- Type: React renderer for Three.js (declarative scene graph)
- Description: `<Canvas>`, hooks (`useFrame/useThree/useLoader`), events, concurrent-safe loop.
- License: MIT (as stated).
- Restrictions/Notes: Peer `three >=0.156`, React 18/19 per version; WebGPU needs async `gl` prop pattern (see threeparticles recipe).
- Agent/CLI integration: npm (`@react-three/fiber`); R3F ecosystem CLIs/scaffolds.

### 03. Drei (pmndrs/drei)
- URL: https://github.com/pmndrs/drei
- Type: R3F helper library (controls, staging, shapes, portals, WebXR helpers)
- Description: `OrbitControls, Environment, Float, Html, Line, Trail, Caustics`, etc.; docs at drei.docs.pmnd.rs.
- License: MIT (as stated).
- Restrictions/Notes: HDRIs/models in examples carry own licenses; version-lock to matching `@react-three/fiber`/`three`.
- Agent/CLI integration: npm (`@react-three/drei`).

### 04. SVG path → 3D extrude primitives (three `ExtrudeGeometry` + opentype.js)
- URL: https://threejs.org/docs/#examples/en/geometries/ExtrudeGeometry / https://github.com/opentypejs/opentype.js
- Type: Vector-to-geometry technique + font parser
- Description: Pattern reused by 3dsvg/vectorforge/emoji generators (paths → layered extrusions, Z-offset draw order).
- License: Three MIT; opentype.js MIT (as stated).
- Restrictions/Notes: Font outlines inherit font license (OFL/Apache) — check family terms before shipping 3D type.
- Agent/CLI integration: Code pattern; no CLI.

## B. Shaders / postFX

### 05. react-postprocessing + postprocessing (pmndrs + vanruesc)
- URL: https://github.com/pmndrs/react-postprocessing / https://github.com/vanruesc/postprocessing
- Type: EffectPass chain for R3F (Bloom/Vignette/SMAA/FXAA/MotionBlur, blend-funcs)
- Description: Single-triangle fullscreen ops, MSAA default, gamma-correct; saves 100s LOC vs `examples/jsm`.
- License: `react-postprocessing` MIT; `postprocessing` Zlib (as stated).
- Restrictions/Notes: Effect count affects GPU budget; WebGL2 MSAA assumed; mobile: gate bloom/motion-blur.
- Agent/CLI integration: npm (`@react-three/postprocessing`, `postprocessing`).

### 06. Shader Park (shader-park/shader-park) — note
- URL: https://github.com/shader-park/shader-park
- Type: JS→GLSL creative-coding dialect + three/R3F bindings
- Description: SDF sculpting playground + exportable shaders.
- License: MIT — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Playground pieces may carry CC terms; verify before reuse.
- Agent/CLI integration: npm (`shader-park-code`); live editor.

### 07. Okaybabe Shaders (live-background pack, R3F path)
- URL: https://github.com/Okay-Babe/okaybabe-shaders
- Type: 13 product-grade GLSL backgrounds with R3F materials
- Description: See 08/16; `HalationMaterial` etc. with `intensity/brandHue` props; 15KB tree-shaken +12.96KB R3F.
- License: MIT (as stated).
- Restrictions/Notes: Needs `LinearSRGBColorSpace` Canvas opt-in for brand accuracy (per README).
- Agent/CLI integration: `import { HalationMaterial } from '@okaybabe/shaders/r3f'`.

### 08. R3F FBO Ping-Pong Starter (heinergiehl/r3f-fbo-pingpong-starter)
- URL: https://github.com/heinergiehl/r3f-fbo-pingpong-starter
- Type: GPGPU simulation template (particles/flocking/Game-of-Life/fluids)
- Description: Vite+React+TS, `vite-plugin-glsl`, double-buffer swap (`FBOParticles.tsx`), `simulation/render` vert/frag pairs, drei OrbitControls/Stats.
- License: MIT (as stated in highlights) — verify LICENSE file.
- Restrictions/Notes: Float RGBA FBOs + Nearest filtering assumed; edit sim-frag to repurpose data layout.
- Agent/CLI integration: Template clone; Vercel demo included.

## C. Particles

### 09. Three-VFX (mustache-dev/Three-VFX, fork jacktoptal/Three-VFX; npm `r3f-vfx`)
- URL: https://github.com/mustache-dev/Three-VFX
- Type: GPU-compute particle system (WebGPU native + WebGL CPU fallback) for R3F/TresJS/Threlte
- Description: Emitters (point/box/sphere/cone/disk/edge), bezier curves (size/opacity/velocity/rotation), turbulence/attractors/collisions, trails, custom geometry/material/shaders, GPU bitonic sort.
- License: MIT (as stated).
- Restrictions/Notes: Targets WebGPU (79% global per README) with fallback; WebGPU renderer required for full path.
- Agent/CLI integration: `npm i r3f-vfx`; `<VFXParticles debug>` + typed props.

### 10. threeparticles (threeparticles/threeparticles, npm `@threeparticles/core`)
- URL: https://github.com/threeparticles/threeparticles
- Type: WebGPU particle engine + R3F subpath + visual editor
- Description: Config-based (`particles/emitter/render` incl. gravity, gradients, fadeAlpha/Size, blending); fire/fountain recipes; docs + editor sites.
- License: MIT (as stated).
- Restrictions/Notes: Requires `three >=0.160` + `WebGPURenderer.init()` + async Canvas `gl` pattern.
- Agent/CLI integration: `npm i @threeparticles/core three`; `import { Particles } from '@threeparticles/core/react'`.

### 11. r3f-particle-system (sampstrong/r3f-particle-system, npm `r3f-particle-system`)
- URL: https://github.com/sampstrong/r3f-particle-system
- Type: Declarative FBO particle kit (`ParticleSystem/Emitters/Forces/Particles`)
- Description: Mesh/Sphere emitters, forces, PointParticle (circle/soft/point, colorModes, alphaFade, blending), imperative `stop/start/createBurst`.
- License: MIT (as stated, v1.0.3 experimental).
- Restrictions/Notes: Experimental — breaking changes possible; peers `@react-three/drei ^9`, `fiber ^8`, `react ^18`, `three ^0.170`.
- Agent/CLI integration: npm; context-wrapper pattern.

### 12. R3F Flow-Field Particles (sebastien-lempens/r3f-flow-field-particles)
- URL: https://github.com/sebastien-lempens/r3f-flow-field-particles
- Type: GPGPU flow-field + mouse-repulsion component (disc/ring/sphere/square)
- Description: `FlowFieldParticles` with `size/interactive/colors/disturbIntensity/repulsionForce/shape/lightSource`; child-mesh sampling.
- License: MIT (as stated).
- Restrictions/Notes: Single-author gist distribution; test perf on integrated GPUs.
- Agent/CLI integration: Copy-in component (`/components/FlowFieldParticles.jsx`).

### 13. creativedev.particles (Kevinparra535/creativedev.particles)
- URL: https://github.com/Kevinparra535/creativedev.particles
- Type: GPU particle lab (WebGL2 FBO + CPU fallback) + legacy post-FX
- Description: R3F + GLSL3 sim/draw, FXAA/Bloom/MotionBlur pipeline, 4k→4m presets (65k sweet spot @1080p60), Leva/Zustand/styled-components.
- License: MIT (as stated).
- Restrictions/Notes: Bundle heavy (three+shaders) — code-split UI/effects; mobile: adaptive amounts, bloom off by default (per README).
- Agent/CLI integration: Vite template; `docs/` playbooks.

### 14. Particle Experience 100k (Abdelqoddoussellouizi/Particle-Experience-)
- URL: https://github.com/Abdelqoddoussellouizi/Particle-Experience-
- Type: 100k morph-target showcase (9 shapes + hand-tracking)
- Description: Sphere/Galaxy/Disc/Wave/Torus/Spiral/Explosion/Nebula/Chaos blending q6s; simplex-noise drift; GSAP/Framer entrance; MediaPipe HandLandmarker; Tailwind v4 + Leva.
- License: MIT (as stated).
- Restrictions/Notes: Webcam/hand path needs user permission + capable GPU; awwwards-grade but demo-tuned.
- Agent/CLI integration: Vite+React19 template.

### 15. tsParticles (tsparticles/tsparticles + @tsparticles/react)
- URL: https://github.com/tsparticles/tsparticles
- Type: Dependency-free 2D canvas particle presets (confetti/fireworks/backgrounds) with framework wrappers
- Description: React/Vue/Angular/Svelte/jQuery/Preact/Solid/Web Components; CDN + npm; CRA templates.
- License: MIT (as stated).
- Restrictions/Notes: `@tsparticles/react` archived (use `.../react` successor path per repo); large preset catalog, pick per-bundle.
- Agent/CLI integration: npm (`tsparticles`, `@tsparticles/react`, `.../slim`); `cra-template-particles[-typescript]`.

## D. SVG→3D products / maps

### 16. 3dsvg (renatoworks/3dsvg, npm `3dsvg`)
- URL: https://github.com/renatoworks/3dsvg
- Type: SVG/text → interactive React 3D (`<ExtrudedSVG>`) + visual editor (3dsvg.design)
- Description: 4 inputs (text-10-Google-Fonts/pixel/SVG-code/upload), 10 materials (plastic/metal/glass/rubber/chrome/gold/clay/emissive/holographic), 7 anims, procedural textures; export PNG-4K/video-MP4-WebM/GLB-STL-OBJ-PLY/embed JSX.
- License: MIT (as stated).
- Restrictions/Notes: Stack Next16/R3F/Three/opentype/FFmpeg-WASM/shadcn/Tailwind v4; font use inherits Google-Fonts OFL.
- Agent/CLI integration: `packages/engine` embed + editor export.

### 17. Glyphrise 3D / vectorforge (bernaferrari/vectorforge)
- URL: https://github.com/bernaferrari/vectorforge
- Type: Browser 3D-icon motion editor (SVG + Material Symbols → extrude/material/keyframes → GLB/WebM/R3F/Filament)
- Description: Per-path depth/scale/color, glass/gel/metal/cut finishes, timeline easing/snapping; local-first (no accounts/sync).
- License: As stated in repo — Unverified in this pass, check LICENSE.
- Restrictions/Notes: Prototype scope: R3F export is starter (custom shaders simplified); Android export is static Filament viewer.
- Agent/CLI integration: Next16/React19/Tailwind4 editor; copy-starter workflow.

### 18. Leaflet + React-Leaflet (2D map baseline)
- URL: https://github.com/Leaflet/Leaflet / https://github.com/PaulLeCam/react-leaflet
- Type: Lightweight 2D map renderer + React bindings
- Description: Tile layers, markers/popups, CRS; React-Leaflet v4/5 context pattern.
- License: Leaflet BSD-2-Clause (as stated); React-Leaflet Hicks/olf — verify (Hippocratic-adjacent history, check version LICENSE).
- Restrictions/Notes: Tile-provider ToS/attribution REQUIRED (OSM/Carto/Mapbox terms); not a 3D globe.
- Agent/CLI integration: npm (`leaflet`, `react-leaflet`).

### 19. deck.gl (visgl/deck.gl) + fiber.gl + deck.gl-leaflet
- URL: https://github.com/visgl/deck.gl / https://github.com/deckgl-fiber-renderer/fiber.gl
- Type: WebGL2 geospatial viz (layers) + React renderer + Leaflet plugin
- Description: Scatter/Arc/Hex/Heat/Trip layers; `fiber.gl` adds nesting/hooks/generics/tree-shaking; weatherlayers/deck.gl-leaflet bridges.
- License: deck.gl MIT; fiber.gl MIT; deck.gl-leaflet MIT (as stated).
- Restrictions/Notes: Basemap/data licenses separate (MapLibre/CARTO); GPU-heavy layers need viewport culling.
- Agent/CLI integration: npm (`deck.gl`, `@deckgl-fiber-renderer/dom`, `deck.gl-leaflet`).

### 20. MapLibre GL JS + D3 (open-map / dataviz pair)
- URL: https://github.com/maplibre/maplibre-gl-js / https://github.com/d3/d3
- Type: Open vector-map renderer + SVG/Canvas dataviz grammar
- Description: MapLibre (Mapbox GL fork): styles/sprites/glyphs, PMTiles; D3: scales/geo-projections/force/cartography overlays.
- License: MapLibre BSD-3-Clause; D3 ISC (as stated).
- Restrictions/Notes: Style/data sources need attribution + license check (OSM ODbl, Natural Earth public domain); glyph hosting self-managed.
- Agent/CLI integration: npm (`maplibre-gl`, `d3`); Vite/Next templates; PMTiles CLI for offline tiles.

---
Counts: 20 records (01–20).
