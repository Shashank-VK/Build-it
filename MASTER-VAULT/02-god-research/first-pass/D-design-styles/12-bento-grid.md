# 12 — Bento Grid / Layout

> Research date: 2026-10-09 | Researcher: Styles 11-20 | Methods: WebSearch + WebFetch

## Meaning
Layout pattern named after Japanese bento boxes: one tray divided into rounded compartments of different sizes. One 2x2 hero cell anchors the main feature; smaller 1x1 / 2x1 cells fill supporting details. Popularized by Apple product pages (~2023), now default for SaaS feature sections and dashboards. Solves scanning: 6-9 value props visible in one paint vs 2-3 in stacked layout.

## Key Elements
- CSS Grid: `repeat(4, minmax(0,1fr))`, `grid-auto-rows: 180px`, `gap: 16px`, `grid-auto-flow: dense`
- Cells: `border-radius: 20-28px` (signature — under 16px reads as plain card grid), `padding: 24px`, `overflow: hidden`, bg light `#f5f5f7` / dark `#161617 + 1px rgba(255,255,255,0.08)`
- Hierarchy: exactly one 2x2 hero + 1-2 wide 2x1 + rest 1x1; max ~8 cells; size encodes priority
- One idea per cell: heading 17-21px semibold + one 14-15px support line; no paragraphs
- Media edge-to-edge clipped to radius; glass-blur cells need bottom scrim `rgba(0,0,0,0.55)->transparent` for 4.5:1
- Hover only motion: scale 1.02 + soft shadow 200ms; nothing autoplays (except hero)
- Responsive: 4col -> 2col (<768px) -> 1col (<480px, reset spans, `auto` rows); keep DOM = reading order, don't rely on `dense` for meaning (WCAG 1.3.2 / 2.4.3)

## Applications
- SaaS homepages, feature sections, product showcases, portfolios, landing CTAs
- Dashboards (cells map 1:1 to widgets), docs hubs, photography curation, AI product marketing (Raycast, Amie, GitHub Copilot, Apple MacBook Air examples)
- B2B SaaS 2026 standard per ThunderClap C.O.N.V.E.R.T., Figma Grid GA May 2026

## Verified Resources
1. Superdesign Bento recipe — CSS + Tailwind, live minis, 4 verified live examples, 2026 usage stats (208k generations), a11y limits — https://superdesign.dev/styles/bento-grid — **Fetched + verified 2026-10-09**
2. Bento Grids gallery — 100+ sourced examples (Apple, Linear Asks, Vercel Geist, Notion, Tailwind UI) — https://bentogrids.com/
3. Prototypr guide — modern approach to UI layouts — https://blog.prototypr.io/embracing-the-bento-grid-a-modern-approach-to-ui-layouts-4a15f618e751
4. Senko UI Bento component (shadcn, glow, 12-col spans) — https://senko-ui.vercel.app/docs/components/bento-grid
5. Bento Dashboard Guide 2026 (CSS structure, Figma, a11y) — https://www.orbix.studio/blogs/bento-grid-dashboard-design-aesthetics
6. Figma community files — https://www.figma.com/community/file/1515273569496410462/modern-bento-grid-layout and https://www.figma.com/community/file/1480583557493388975/bento-grid-ui-the-future-of-engaging-web-layouts

## Gap
None. Abundant code + examples + 2026 trend data.
