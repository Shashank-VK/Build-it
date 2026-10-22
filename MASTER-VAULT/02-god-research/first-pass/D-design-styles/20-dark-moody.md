# 20 — Dark Moody

> Research date: 2026-10-09 | Researcher: Styles 11-20 | Methods: WebSearch + WebFetch

## Meaning
Atmospheric dark design where darkness is composition, not just inverted light mode. Ranges from Dark Mode Minimal (#0A0A0A, information only) to Dark Editorial (moody magazine in dim room, imagery as event) to Dark Glassmorphism (moody + sophisticated, linked to dark mode). Goal: focus, depth, cinematic gravitas with sustained readability.

## Key Elements
- Near-black not pure black: base #0A0A0A / #121212 / #161617; 3-5 dark tones for layers; elevation = lighter surfaces (translucent white overlays), not shadows
- Text levels only 3: primary #E8E8E8 / secondary #A0A0A0 / disabled #666; avoid pure-white body (halation); left-align, bold not italic for emphasis
- 1px borders #2A2A2A define space; fills avoided except semantic; structure from line
- Accents desaturated, used sparingly + semantically: blue #3B82F6 interactive / green success / amber caution / red error; no saturated glow that vibrates
- Glass variant: `backdrop-filter: blur(12-20px)`, alpha-gradient bg (lighter top-left), `1px rgba(255,255,255,0.1)` light-catcher border; needs dynamic glowing bg, invisible on flat black
- Imagery: full-bleed heroes, 16:9 / 2.35:1 cinematic crops, desaturated/high-contrast treatments; scrim under text; generous negative space to offset heaviness
- A11y + tech: `color-scheme: light dark` on `:root`, persist toggle pre-paint, WCAG AA 4.5:1 body / 3:1 UI, test focus/disabled states in dark

## Applications
- Dev tools, streaming, gaming, fintech dashboards, music/studio, luxury black sites, Halloween/time-based themes, code/editing focus modes
- Examples: Qase (navy+purple glow), YouTube/Trello dark, Dark Editorial magazine layouts, Firework minimal system

## Verified Resources
1. MadeGood — Dark Mode Design best practices (tokens, palette, CSS vars, pre-paint toggle) — https://madegooddesigns.com/dark-mode-design
2. Halo Lab — 11 tips for dark website design (saturation, shadows, hierarchy) — https://uxplanet.org/dark-ui-design-11-tips-for-dark-mode-design-f075b7e01749
3. Dark Editorial spec — moody magazine + dark UI, grids, palette, type — https://github.com/chrislemke/website_designs/blob/main/designs/Dark_Editorial.md
4. Firework — Dark Mode Minimal system (#0A0A0A, 1px borders, semantic color) — https://fireworkwebdesign.com/design-styles/dark-mode-minimal
5. Designmodo — Dark mode websites tips + examples (Qase, YouTube, Trello) — https://designmodo.com/dark-mode-websites
6. Chrome modern-web-guidance — dark-mode.md (`color-scheme`, `light-dark()`) — https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/guides/user-experience/dark-mode.md
7. MustBeWebCode — Dark Glassmorphism 2026 (alpha gradients, blur, borders) — https://medium.com/@developer_89726/dark-glassmorphism-the-aesthetic-that-will-define-ui-in-2026-93aa4153088f

## Gap
None. Mature guidance + tokens + code patterns verified.
