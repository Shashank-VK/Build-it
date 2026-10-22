# 04 — Brutalism (Web Brutalism)

> Style researcher 4/10. Read-only, no installs. Search + fetch verified 2026-10-09.

## 1. Documented meaning
- Web analogue of Brutalist architecture: raw, honest, anti-polish; exposed structure (system fonts, unstyled HTML edges, visible gridlines), function over seduction.
- Documented in: Brutalist Websites gallery manifesto, "Guidelines for Brutalist Web Design", superdesign.dev "Brutalist Web Design: CSS Recipe" (copy-paste recipe + 6 live examples + a11y costs), Brutalist Framework docs.
- Digital meaning: hacker/indie credibility, cheap+fast, deliberate friction; distinct from polished Neo-brutalism (see 06).

## 2. Characteristic visual elements
- Raw HTML defaults: Times/System serif + monospace, blue/purple links, visible borders, unpadded blocks.
- Stark monochrome or unblended primaries; no gradients/shadows (or 1px hard rules); square corners.
- Dense, linear, left-aligned stacks; tables, fieldsets, marquee/hr excess; exposed system chrome.
- Minimal or no imagery; images unretouched, bordered, pixelated allowed.
- Deliberate anti-UX signals: clashing focus rings, oversized hit areas, Comic-mono touches.

## 3. Digital applications
- Hacker portfolios, zines, docs/knowledge bases, event/venue pages, indie tooling landing pages, protest/activist pages.

## 4. Implementation resources (with verification)
### Repos / CSS frameworks (dedicated — best coverage in set)
- Brutalist Framework 2.7 (STATIC CORE) — open-source HTML/CSS/JS kit: BUTCH/BUIX/BFX/Blueprint Grid/ReBAR/Flavors/bIcons/BELL + boilerplates — https://github.com/pinecreativelabs/Brutalist-Framework — ✅ Fetched 200 (GitHub live, 437★/32 forks context from search). Docs: http://www.brutalistframework.com/ and https://static.brutalistframework.com/ — 🔍 Search-verified (excerpt live). ⚠️ EOL notice: main site states "End of Life since 8/22/2026, unsupported" — pin v2.7 STATIC, do not expect updates.
- BRUT (brut.css, ~8KB) — brutalist+minimalist CSS for admin interfaces — https://brut.esy.fun/index.html — 🔍 Search-verified.
- Schultz Brutalist UI — zero-dependency monochrome brutalist CSS (hard shadows, uppercase type rules) — https://github.com/stefanschultz/schultz-brutalist-ui — 🔍 Search-verified (0★ micro-repo — review before use).
- Topic indexes: https://github.com/topics/brutalist and https://github.com/topics/brutalism — 🔍 Search-verified.
### Libs (shared)
- Zero or jQuery-era vanilla JS per BF (JAB); no modern framework required — per fetched README.
### DESIGN.md
- GAP — no verified brutalism DESIGN.md; BF README + boilerplate structure is the closest procedural doc — ✅ Fetched (README).
### Figma
- GAP — no canonical brutalist Figma kit verified (anti-Figma ethos is part of the style). Shared: wireframe kits only.
### Templates
- BF boilerplates (/static bp + "View All Boilerplates") — in repo above — ✅ Fetched as listed.
- Built-with examples: MonSuperKilometre.com, ZarmaStudio.com (cited in BF legacy docs) — ⚠️ Cited second-hand, verify live before linking out.
### Fonts
- System stack + monospace doctrine: `Times New Roman / Arial / Courier New / monospace`; BFT "BUTCH" custom fonts (biorhyme, lewatur, mupen, riosark per 2.7 changelog) — 🔍 Search-verified via static site excerpt. Google-safe: Space Mono / IBM Plex Mono — shared, cross-ref.
### Icons
- bIcons (native UTF-8 symbol icon classes, incl. currency set in 2.7) — in BF — 🔍 Search-verified. Otherwise GAP for dedicated set; shared Lucide acceptable but off-doctrine.
### Textures
- GAP — doctrine: none (raw flat). BUFF filters (deep-sea/dreamy/vibrant/vintage) are image filters, not textures — 🔍 Search-verified as filter list.
### 3D
- GAP — none by doctrine; state explicitly.
### Animation
- BFX (color-shift, spazz glitch) + animated-backgrounds.css — 🔍 Search-verified via 2.7 changelog excerpt. Shared GSAP only if needed — cross-ref.
### Tutorials
- Superdesign brutalism CSS recipe + 6 live examples + a11y costs — https://superdesign.dev/styles/brutalism — 🔍 Search-verified.
- BF Reference Mode: eBook guides/screencasts/related articles (linked from BF site) — ⚠️ Cited second-hand.
- BrutalistWebsites.com + "Examples & Best Practices" + "Guidelines for Brutalist Web Design" (BF reference list) — ⚠️ Cited second-hand, verify.
### Galleries
- https://brutalistwebsites.com (canon gallery, via BF reference) — ⚠️ Cited second-hand, not fetched this pass — verify.
- Craigslist / Yale Art School (cited by superdesign.dev as live examples) — ⚠️ Via superdesign excerpt.
### Prompts
- GAP — no verified brutalism prompt pack.
### Audit tools
- GAP (style-specific) — shared Lighthouse/axe; note superdesign.dev flags honest a11y costs (contrast/focus/motion) — 🔍 Search-verified as warning source.

## 5. Cross-refs
- Donor to 06 Neo-brutalism (hard shadow/square corner grammar) and 02 Maximalism (raw stacking); opposite of 08 Neumorphism / 10 Glassmorphism (depth-via-shadow vs depth-refusal).
