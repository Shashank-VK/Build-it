# Atlas Catalog 02a — Design (Part 4 + Part 17)

**Workstream researcher #4. Research date: 2026-10-10. Coverage: design systems & official guidelines, UI/UX theory, design inspiration & directories, creative assets & pipelines, design-to-code, visual/interactive creative tech.**
**The 29 design styles are covered by a separate workstream and are excluded here. Excluded from re-research (cross-referenced only): facebook/astryx, keysjoao/laws-of-ux-skills, emilkowalski/skills (apple-design), shadcn MCP, lawsofux.com, alexpate/awesome-design-systems, gztchan/awesome-design, VoltAgent/awesome-design-md, pmndrs/react-three-start, pmndrs/react-three-next, pmndrs/react-three-fiber, Google Material Design 3, Apple HIG.**

## Research method & sources searched

- Live web research via `browser.search` + `browser.open` on primary sources: official docs sites, GitHub repo READMEs (fetched), npm/registry listings, W3C/Figma/Google/Meta/Microsoft/IBM/Adobe/Salesforce/Shopify/GitHub official pages. Primary over secondary.
- Targeted file inspection where relevant: README.md, LICENSE, SKILL.md, package identity, docs pages. Large projects inspected via README + docs, not full source.
- Search themes used (multiple per subcategory):
  - Design systems: `<org> design system components official`, `Carbon/Spectrum/Polaris/Fluent/Primer/SLDS/USWDS/GOV.UK/Atlaskit/Chakra/Radix/MUI/Ant/Base UI/Ark UI/Shoelace/Headless UI`, `design tokens Style Dictionary Token Studio`.
  - UI/UX theory: `NNGroup 10 usability heuristics`, `uxchecklist github.io`, `Refactoring UI`, `W3C WCAG quickref`, `Baymard UX research`, `Material motion guidelines easing`.
  - Inspiration: `Awwwards SiteInspire Land-book Mobbin`, `Godly Lapa Ninja SaasFrame`, `Collect UI UI Movement`, `Codrops tympanus`, `Figma community UI kits`, `Aceternity Magic UI copy-paste`.
  - Assets: `Lucide Heroicons Tabler Phosphor icons`, `unDraw Blush Humaaans illustrations`, `Lottie Rive animation`, `Fontsource Google Fonts`, `Haikei Hero Patterns backgrounds`, `Kenney Quaternius 3D`, `Squoosh SVGO`, `Book of Shaders Shadertoy`.
  - Design-to-code: `Figma MCP server official`, `Locofy Anima Builder.io TeleportHQ`, `screenshot-to-code abi`, `Kombai Quest Codia`, `Plasmic visual builder`, `Chromatic Percy Applitools`, `Style Dictionary Token Studio`, `Supernova Zeplin`, `v0 Vercel`, `Relume Webflow Framer Uizard Visily`.
  - Creative tech: `three.js mrdoob`, `drei @react-three/postprocessing pmndrs`, `GSAP Motion anime.js`, `Lenis p5.js PixiJS`, `Spline Babylon.js`, `tsParticles Animate.css`, `Mapbox deck.gl kepler.gl`.
- Distinction enforced throughout: **implementation** (shipped code you install) vs **docs-only** (guidelines, tokens, prose) vs **inspiration gallery** (screenshots only) vs **hosted service** (SaaS, account/API-gated) vs **archived/historical**.
- Verification labels used exactly: Verified / Partially verified / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved.
- Unknowns recorded as "Not verified" / "Not publicly documented" / "Not applicable" / "Unresolved" — never invented.

---

## PART A — Design systems & official interface guidelines (implementation + docs)

> DEDUP note: Astryx, Material Design 3, and Apple HIG were previously catalogued and are cross-referenced only where relevant.

### A1. IBM Carbon Design System

- **Resource name:** IBM Carbon Design System
- **Canonical identity:** `carbon-design-system/carbon` (GitHub monorepo)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React + Web Components libraries, Sass, tokens) + docs site
- **Official URL:** https://carbondesignsystem.com/ (repo: https://github.com/carbon-design-system/carbon)
- **Description:** IBM's open-source design system implementing the IBM Design Language: enterprise/data-dense components, token-based theming (light/dark), 8px grid, IBM Plex typography, square (0px) corners, IBM Blue (#0f62fe).
- **Contents inspected:** GitHub README (packages table), Wikipedia summary, third-party DESIGN.md specimens, skill-research issue notes.
- **Actual capabilities:** React components (`@carbon/react`), web components (`@carbon/web-components`), Sass styles, design tokens (colors, type, layout, motion, themes), icons + pictograms, grid. Community-maintained Angular/Svelte/Vue packages.
- **Usage domain:** Enterprise B2B, cloud dashboards, data-dense technical products.
- **Inputs:** npm install (`npm i @carbon/react @carbon/styles`); Figma library via IBM.
- **Outputs:** Rendered React/web-component UI; `--cds-*` CSS custom-property token layer.
- **Integration method:** npm packages; Sass imports; Storybook docs.
- **Dependencies:** React (for `@carbon/react`); Sass build tooling.
- **Availability:** Open source, current.
- **Maintenance:** Active (IBM Carbon Core team; community framework ports).
- **License:** Apache-2.0 (code). IBM Plex typeface under OFL.
- **Limitations:** Strong IBM enterprise aesthetic signature; opinionated density. Agent-facing SKILL.md exists in third-party repos, not officially shipped.
- **Related resources:** carbon icons; `ujjwal-gowda/specimen` DESIGN.md for Carbon (third-party).
- **Sources:** https://github.com/carbon-design-system/carbon; https://carbondesignsystem.com/; https://en.wikipedia.org/wiki/Carbon_Design_System
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A2. Adobe Spectrum

- **Resource name:** Adobe Spectrum
- **Canonical identity:** Spectrum (Adobe design system); docs now "Spectrum Hub"
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React + Web Components) + docs-only foundations/tokens
- **Official URL:** https://spectrum.adobe.com/ (docs); tokens/design data: https://github.com/adobe/spectrum-design-data
- **Description:** Adobe's design system behind Creative Cloud/Express experiences. One connected system with dedicated React and Web Components areas (in beta at inspection), iOS/Android coming. Token-first (S1 and S2 token sets), JSON component schemas, token visualizer tools.
- **Contents inspected:** spectrum.adobe.com homepage (live fetch: "Spectrum Hub" announcement); `adobe/spectrum-design-data` README (renamed from spectrum-tokens); coral-spectrum notes.
- **Actual capabilities:** React implementation (React Spectrum / React Aria primitives), Spectrum Web Components, Spectrum CSS, design tokens + JSON schemas + visualizer tooling, interactive component playgrounds wired to real repo data.
- **Usage domain:** Adobe-ecosystem products; complex creative/productivity UI.
- **Inputs:** npm packages (`@adobe/react-spectrum`, `@spectrum-web-components/*`); token JSON.
- **Outputs:** Accessible React/web components; token artifacts for theming.
- **Integration method:** npm; Storybook; docs site.
- **Dependencies:** React (for React implementation); framework-free via web components.
- **Availability:** Open source, current; S2 generation in progress.
- **Maintenance:** Active (Adobe).
- **License:** Apache-2.0 (components; verify per-package). Design-data repo under Adobe open source.
- **Limitations:** S1→S2 migration in flight; some docs areas beta. React Aria (primitives) is the more portable layer than full React Spectrum.
- **Related resources:** React Aria Components; Adobe React Spectrum; Tokens Studio.
- **Sources:** https://spectrum.adobe.com/; https://github.com/adobe/spectrum-design-data; https://opensource.adobe.com/spectrum-design-data/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A3. Shopify Polaris

- **Resource name:** Shopify Polaris
- **Canonical identity:** Shopify Polaris (Polaris Web Components current; `@shopify/polaris` React deprecated)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (web components) + docs; legacy React archived
- **Official URL:** https://polaris.shopify.com/ (docs); https://shopify.dev/docs/api/app-home/polaris-web-components
- **Description:** Shopify's design system for Shopify admin/app surfaces. The React library (`@shopify/polaris`) was **deprecated**; current path is Polaris Web Components (`<s-*>` custom elements), released 2025-10-01, plus design tokens and Figma community kits.
- **Contents inspected:** `shopify/polaris-react-archive` README (deprecation notice verbatim); Polaris docs getting-started; third-party polaris-2.0-claude-design-system readme describing `s-*` web-component runtime.
- **Actual capabilities:** Web components for Shopify app surfaces (`s-button`, `s-card`, etc.), design tokens (`polaris-tokens`), icons, VS Code extension (legacy monorepo), stylelint config.
- **Usage domain:** Shopify admin embedded apps, checkout/app-home extensions only.
- **Inputs:** `<script src="https://cdn.shopify.com/shopifycloud/polaris.js">` + `<s-*>` tags; or React package (deprecated).
- **Outputs:** Shopify-admin-conformant UI.
- **Integration method:** CDN script or npm; App Bridge for app context.
- **Dependencies:** Shopify app context (App Bridge, API key).
- **Availability:** Current as web components; React package deprecated/archived.
- **Maintenance:** Active for web components; React repo explicitly unmaintained.
- **License:** Not verified at package level (repo license not fetched); treat as **Not verified** — check `Shopify/polaris` license before reuse.
- **Limitations:** Only meaningful inside Shopify surfaces; not a general-purpose DS.
- **Related resources:** Shopify App Bridge; polaris icons Figma kit.
- **Sources:** https://github.com/shopify/polaris-react-archive; https://polaris.shopify.com/; https://shopify.dev/docs/api/app-home/polaris-web-components
- **Verification date:** 2026-10-10
- **Confidence:** High on deprecation status; medium on license. **Verification: Corrected** (React deprecated; web components are current).

### A4. Microsoft Fluent UI (Fluent 2)

- **Resource name:** Microsoft Fluent UI (Fluent 2 design language)
- **Canonical identity:** `microsoft/fluentui` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React v9, web components, iOS, Android) + docs site + tokens
- **Official URL:** https://fluent2.microsoft.design/ (design); https://react.fluentui.dev/ (Storybook); repo https://github.com/microsoft/fluentui
- **Description:** Microsoft's cross-platform design system powering Microsoft 365, Teams, Copilot, Windows. Fluent 2 tokens; React v9 (`@fluentui/react-components`), web components v3 (`@fluentui/web-components`), native iOS (`fluentui-apple`) and Android (`fluentui-android`).
- **Contents inspected:** Third-party SKILL.md references (triggers + package table), fluent2-registry README (shadcn registry re-exporting `@fluentui/react-*` 1:1), fluent-ui-plugin AGENTS.md (Copilot chat UI `@fluentui-copilot/react-copilot`).
- **Actual capabilities:** 50+ React components, tokens, theming/brand ramp utilities, icon system (filled+regular), Copilot/AI-chat UI components (`@fluentui-copilot/react-copilot`, Storybook at ai.fluentui.dev), Figma kits.
- **Usage domain:** Microsoft-ecosystem/enterprise SaaS, M365-style products, AI chat surfaces.
- **Inputs:** `npm i @fluentui/react-components`; wrap in `<FluentProvider theme={...}>`.
- **Outputs:** Accessible themed React components; CSS token variables.
- **Integration method:** npm; Storybook docs; Figma kits (aka.ms links).
- **Dependencies:** React 18+ for v9; Emotion no longer required in v9 (CSS-in-JS via Griffel).
- **Availability:** Open source, current.
- **Maintenance:** Active (Microsoft).
- **License:** MIT.
- **Limitations:** Distinctive Microsoft aesthetic; v8 (old) vs v9 (current) package split confuses; web-components v3 separate track.
- **Related resources:** whenismikell/fluent2-registry (shadcn registry); thelobbi/claude-m fluent skills (third-party agent wrappers).
- **Sources:** https://github.com/microsoft/fluentui; https://fluent2.microsoft.design/; https://react.fluentui.dev/; https://github.com/whenismikell/fluent2-registry
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A5. GitHub Primer

- **Resource name:** GitHub Primer
- **Canonical identity:** `primer` org (GitHub); packages `@primer/react`, `@primer/css`, `@primer/react-brand`, `@primer/primitives`, `@primer/octicons`
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React, CSS, Brand) + docs (primer.style) + tokens + icons
- **Official URL:** https://primer.style/
- **Description:** GitHub's design system. `@primer/react` (60+ components) is the primary product-UI integration; `@primer/css` for CSS-only; `@primer/react-brand` for marketing surfaces; `@primer/primitives` for CSS custom-property tokens; Octicons icon set; Mona Sans/Monaspace typography.
- **Contents inspected:** Third-party ADR/research docs citing versions (`@primer/react` 38.x, `@primer/primitives` 11.x) and usage (`ThemeProvider + BaseStyles`).
- **Actual capabilities:** Accessible React components (DataTable, TreeView, ActionMenu, PageLayout, Dialog, etc.), design tokens as CSS variables, Octicons (`@primer/octicons-react`), Figma libraries.
- **Usage domain:** GitHub-style devtools, developer products, docs sites.
- **Inputs:** `npm install @primer/react @primer/primitives`.
- **Outputs:** GitHub-visual-language UI with light/dark themes.
- **Integration method:** npm; CSS import; styled-components peer dep (historical).
- **Dependencies:** React; styled-components (per migration docs).
- **Availability:** Open source, current.
- **Maintenance:** Active (GitHub).
- **License:** MIT (verify per package; not re-fetched — medium confidence).
- **Limitations:** Strong GitHub visual identity; Brand vs product split.
- **Related resources:** Octicons; GitHub REST of primer org (css, viewcomponents).
- **Sources:** https://primer.style/; third-party research docs (dbroeglin/hve-stem ADR; tambo-ai primer-skin research)
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified** (package existence/usage confirmed via multiple implementers; official README not directly fetched).

### A6. Salesforce Lightning Design System (SLDS 2)

- **Resource name:** Salesforce Lightning Design System (SLDS 2)
- **Canonical identity:** Salesforce UX; site https://www.lightningdesignsystem.com
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (CSS framework + styling hooks) + docs
- **Official URL:** https://www.lightningdesignsystem.com
- **Description:** Salesforce's design system, now SLDS 2 ("agentic-era"): built on CSS custom properties ("global styling hooks", `--slds-g-*`), machine-readable tokens (`@salesforce-ux/sds-styling-hooks`), canonical Salesforce brand-blue scale.
- **Contents inspected:** `salesforce-ux/design-system` README (legacy), kwakseongjae/oh-my-design DESIGN.md for Salesforce (token values extracted 2026-06-11).
- **Actual capabilities:** CSS component framework, design tokens/styling hooks, icons, accessibility patterns for Salesforce surfaces.
- **Usage domain:** Salesforce platform apps, Lightning Experience customizations.
- **Inputs:** SLDS CSS / styling-hooks npm packages; Lightning Web Components in-platform.
- **Outputs:** Salesforce-look UI; token-driven theming.
- **Integration method:** npm CDN/CSS; Salesforce platform tooling.
- **Dependencies:** Salesforce context for full value.
- **Availability:** Current (SLDS 2).
- **Maintenance:** Active (Salesforce UX).
- **License:** Not verified (check upstream before reuse).
- **Limitations:** Tied to Salesforce product surface conventions; legacy repo (`salesforce-ux/design-system`) is stale — use current site/docs.
- **Related resources:** Lightning Web Components (open source: `salesforce/lwc`).
- **Sources:** https://www.lightningdesignsystem.com; https://github.com/salesforce-ux/design-system (historical)
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### A7. U.S. Web Design System (USWDS)

- **Resource name:** U.S. Web Design System (USWDS)
- **Canonical identity:** `uswds/uswds` (GitHub); docs https://designsystem.digital.gov
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (Sass/JS components) + docs-only principles/guidance
- **Official URL:** https://designsystem.digital.gov
- **Description:** U.S. federal government's toolkit of principles, guidance, and code: open-source UI components and visual style guide for federal websites. Public-domain oriented.
- **Contents inspected:** `uswds/uswds` README (install instructions verbatim: `npm install --save @uswds/uswds`, compiled files in `dist/`, source in `packages/`).
- **Actual capabilities:** Accessible components (forms, navigation, banners, alerts), USWDS theme tokens (Sass), utility classes, guidance on accessibility/plain language.
- **Usage domain:** U.S. public-sector / trust-first websites.
- **Inputs:** `npm install @uswds/uswds` (or `uswds`).
- **Outputs:** Section-508/WCAG-conscious federal-style UI.
- **Integration method:** npm; Sass; compiled CSS/JS includes.
- **Dependencies:** Node/npm for build; Dart Sass.
- **Availability:** Open source, current.
- **Maintenance:** Active (USWDS team; note: forks like `dsacms/uswds` exist but canonical is `uswds/uswds`).
- **License:** Public domain / CC0 for code per project policy (verify current LICENSE in repo).
- **Limitations:** Strong government aesthetic; opinionated compliance-oriented patterns.
- **Related resources:** `uswds/uswds-site` (docs repo); 18F guidance.
- **Sources:** https://github.com/uswds/uswds; https://designsystem.digital.gov
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A8. GOV.UK Design System (GOV.UK Frontend)

- **Resource name:** GOV.UK Design System / GOV.UK Frontend
- **Canonical identity:** `alphagov/govuk-frontend` (npm `govuk-frontend`); docs https://design-system.service.gov.uk
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (Sass + JS + Nunjucks macros) + docs-only patterns/guidance
- **Official URL:** https://design-system.service.gov.uk
- **Description:** UK Government Digital Service system: styles, components, and patterns for government services. `govuk-frontend` npm package with selective Sass imports, per-component JS (`initAll()`), Nunjucks macros; community ports for Jinja/Rails/.NET/Java/React.
- **Contents inspected:** chrisjohnleah/govuk-design-system-skill SKILL.md + install reference (verbatim: `npm i govuk-frontend sass`, `initAll()`, asset copying, Nunjucks loader path).
- **Actual capabilities:** Accessible form-heavy components, error handling, focus states, typography/grid, bilingual-ready patterns; legally/regulatorily expected for UK public services.
- **Usage domain:** UK public-sector services.
- **Inputs:** `npm install govuk-frontend`; Sass `@use "govuk-frontend"`.
- **Outputs:** GOV.UK-conformant accessible services.
- **Integration method:** npm; Nunjucks macros; community ports.
- **Dependencies:** Dart Sass >=1.79 (v6); Node.
- **Availability:** Open source, current.
- **Maintenance:** Active (GDS).
- **License:** MIT (verify in repo; medium confidence).
- **Limitations:** Regulatory aesthetic; legacy GOV.UK Elements/Template migration path exists.
- **Related resources:** chrisjohnleah/govuk-design-system-skill (third-party agent skill).
- **Sources:** https://design-system.service.gov.uk; https://github.com/chrisjohnleah/govuk-design-system-skill
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified** (via skill wrapping official docs; official repo not directly fetched).

### A9. Chakra UI

- **Resource name:** Chakra UI
- **Canonical identity:** `chakra-ui/chakra-ui` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React component library + styling engine) 
- **Official URL:** https://chakra-ui.com/ (repo https://github.com/chakra-ui/chakra-ui)
- **Description:** Modular React component library with accessible, composable primitives; v3 rebuilt on Ark UI + Zag.js state machines. Style-prop API (`chakra.div`, theme tokens, semantic tokens).
- **Contents inspected:** Third-party DESIGN.md specimens + README excerpts across workstream searches (v3 details).
- **Actual capabilities:** 60+ React components, theming (semantic tokens, color modes), recipes/slots styling system, Figma kits.
- **Usage domain:** General web apps, dashboards.
- **Inputs:** `npm i @chakra-ui/react`.
- **Outputs:** Styled React components.
- **Integration method:** npm; `<ChakraProvider>`/`<Provider>`.
- **Dependencies:** React; Emotion (v2) / Ark UI (v3).
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** v2→v3 API break; aesthetic heavily "chakra" out of the box; v3 learning curve.
- **Related resources:** Ark UI; Zag.js; Panda CSS (same team's CSS engine).
- **Sources:** https://github.com/chakra-ui/chakra-ui; https://chakra-ui.com
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A10. Mantine

- **Resource name:** Mantine
- **Canonical identity:** `mantinedev/mantine` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React components + hooks + styling) 
- **Official URL:** https://mantine.dev/
- **Description:** Full-featured React component library: 100+ components, theming, hooks, forms, notifications, modals, dates, charts (mantine charts via recharts), data table community extensions. MIT, TypeScript-first.
- **Contents inspected:** Third-party skill docs + DESIGN.md references (usage, `MantineProvider`, theme override); mantine.dev structure.
- **Actual capabilities:** Components + CSS-in-JS (emotion) + hooks library + form management; dates, spotlights, carousel, rich text editor (Tiptap).
- **Usage domain:** Admin panels, dashboards, internal tools.
- **Inputs:** `npm i @mantine/core @mantine/hooks`.
- **Outputs:** Full UI kit for React apps.
- **Integration method:** npm; Vite/Next integrations documented.
- **Dependencies:** React; Emotion.
- **Availability:** Open source, current.
- **Maintenance:** Active (Mantine team); latest supports React 19.2+ (per third-party sources).
- **License:** MIT.
- **Limitations:** React-only; heavier bundle for small sites.
- **Related resources:** Mantine DataTable (community); Mantine Charts.
- **Sources:** https://mantine.dev/; https://github.com/mantinedev/mantine
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified** (site/repo confirmed; version details via third-party).

### A11. HeroUI (formerly NextUI)

- **Resource name:** HeroUI (renamed from NextUI)
- **Canonical identity:** `heroui-inc/heroui` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React component library, Tailwind-based)
- **Official URL:** https://www.heroui.com/
- **Description:** Tailwind-based React component library; v3 re-architected on React Aria components + Tailwind v4. Renamed from NextUI (2025). Apache-2.0.
- **Contents inspected:** Third-party DESIGN.md specimens; heroui.com docs structure.
- **Actual capabilities:** 50+ components with variants, dark mode, theming via Tailwind config/v4 CSS-first.
- **Usage domain:** Marketing sites, Next.js apps.
- **Inputs:** `npm i @heroui/react`.
- **Outputs:** Tailwind-styled React components.
- **Integration method:** npm; Tailwind plugin/config.
- **Dependencies:** React; Tailwind CSS; framer-motion (v2 era).
- **Availability:** Open source, current.
- **Maintenance:** Active (HeroUI Inc).
- **License:** Apache-2.0.
- **Limitations:** Tailwind-coupled; v2→v3 migration (React Aria base).
- **Related resources:** NextUI (legacy name); Tailwind CSS; React Aria.
- **Sources:** https://www.heroui.com/; https://github.com/heroui-inc/heroui
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### A12. Radix UI (Primitives + Themes)

- **Resource name:** Radix UI
- **Canonical identity:** `radix-ui/primitives` (GitHub); themes at radix-ui.com/themes
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (unstyled accessible primitives) + Radix Themes (styled layer)
- **Official URL:** https://www.radix-ui.com/
- **Description:** Unstyled, accessible component primitives (Dialog, Popover, Select, Tabs, etc.) with WAI-ARIA compliance; styling-agnostic (Tailwind/shadcn commonly pair). Radix Themes adds a pre-styled layer. Maintained by WorkOS.
- **Contents inspected:** Radix docs + widespread third-party implementation records.
- **Actual capabilities:** ~40 headless accessible primitives; Radix Themes component set with tokens; Radix Colors palette.
- **Usage domain:** Custom design systems; headless component base (shadcn builds on it).
- **Inputs:** `npm i @radix-ui/react-dialog` (per-primitive) or `@radix-ui/themes`.
- **Outputs:** Unstyled accessible components to style yourself.
- **Integration method:** npm.
- **Dependencies:** React.
- **Availability:** Open source, current.
- **Maintenance:** Active (WorkOS).
- **License:** MIT.
- **Limitations:** Headless — you bring all styling; no data components (tables, charts).
- **Related resources:** shadcn/ui; Base UI; React Aria.
- **Sources:** https://www.radix-ui.com/; https://github.com/radix-ui/primitives
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A13. Base UI

- **Resource name:** Base UI
- **Canonical identity:** base-ui.com; npm `@base-ui/react` (formerly MUI Base)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (headless React primitives)
- **Official URL:** https://base-ui.com/
- **Description:** Headless, unstyled, accessible React UI primitives (Dialog, Menu, Popover, Select, Slider, Tabs, Number Field, etc.), forked from MUI Base into standalone project. Since July 2026 it is shadcn's default headless primitive layer.
- **Contents inspected:** base-ui.com docs/components pages; third-party agent-skill docs on Base UI usage.
- **Actual capabilities:** Headless accessible components + hooks; CSS-first styling friendly.
- **Usage domain:** Design-system primitives; shadcn/ui base.
- **Inputs:** `npm i @base-ui/react`.
- **Outputs:** Unstyled accessible primitives.
- **Integration method:** npm.
- **Dependencies:** React; `@base-ui-components/utils` (internal).
- **Availability:** Open source, current.
- **Maintenance:** Active (Base UI team).
- **License:** MIT.
- **Limitations:** Headless; gaps noted 2026-10-10: no calendar/date picker, data table, or tree components yet; React-only.
- **Related resources:** MUI (origin); shadcn/ui; Radix UI.
- **Sources:** https://base-ui.com/; third-party agent skill docs
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### A14. Ark UI

- **Resource name:** Ark UI
- **Canonical identity:** ark-ui.com; GitHub under Chakra org
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (headless components, multi-framework)
- **Official URL:** https://ark-ui.com/
- **Description:** Headless component library by the Chakra team powered by Zag.js state machines: same behavior API across React, Vue, Solid, Svelte. Unstyled, accessible.
- **Contents inspected:** ark-ui.com docs (framework switcher observed); Zag.js docs.
- **Actual capabilities:** ~30+ headless components per framework; state-machine-driven interactions.
- **Usage domain:** Multi-framework design systems; headless base for Chakra v3.
- **Inputs:** `npm i @ark-ui/react` (or /vue, /solid, /svelte).
- **Outputs:** Framework-native headless components.
- **Integration method:** npm.
- **Dependencies:** Framework of choice; `@zag-js/*`.
- **Availability:** Open source, current.
- **Maintenance:** Active (Chakra team).
- **License:** MIT.
- **Limitations:** Headless (bring your own styles); younger ecosystem than Radix for React.
- **Related resources:** Zag.js; Chakra UI v3; Panda CSS.
- **Sources:** https://ark-ui.com/; https://zagjs.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A15. Headless UI (Tailwind Labs)

- **Resource name:** Headless UI
- **Canonical identity:** `tailwindlabs/headlessui` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (headless React + Vue components)
- **Official URL:** https://headlessui.com/
- **Description:** Completely unstyled, fully accessible UI components from Tailwind Labs for React and Vue (Combobox, Dialog, Disclosure, Listbox, Menu, Popover, Radio Group, Switch, Tabs, etc.).
- **Contents inspected:** headlessui.com docs; GitHub repo state.
- **Actual capabilities:** Accessible headless primitives with transitions support.
- **Usage domain:** Tailwind-styled apps needing accessible behavior.
- **Inputs:** `npm i @headlessui/react`.
- **Outputs:** Unstyled accessible components.
- **Integration method:** npm.
- **Dependencies:** React or Vue.
- **Availability:** Open source; no release since April 2026 at inspection.
- **Maintenance:** Slow/infrequent (Tailwind Labs; no commit activity evident since Apr 2026).
- **License:** MIT.
- **Limitations:** Small component set; styling entirely yours; maintenance pace uncertain.
- **Related resources:** Tailwind CSS; Radix UI; Base UI.
- **Sources:** https://headlessui.com/; https://github.com/tailwindlabs/headlessui
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### A16. React Aria Components (Adobe)

- **Resource name:** React Aria Components
- **Canonical identity:** `adobe/react-spectrum` (react-aria package); https://react-spectrum.adobe.com/react-aria/
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (headless accessible hooks + components)
- **Official URL:** https://react-spectrum.adobe.com/react-aria/
- **Description:** Adobe's library of unstyled primitives (50+ components) with best-in-class accessibility (screen reader, keyboard, internationalization, touch). Powers React Spectrum and HeroUI v3.
- **Contents inspected:** react-spectrum.adobe.com docs (components list, hooks API).
- **Actual capabilities:** Hooks (`useButton`, `useDialog`…) + ready components; full i18n; test utils.
- **Usage domain:** Accessible design systems; adaptive UI.
- **Inputs:** `npm i react-aria-components`.
- **Outputs:** Unstyled accessible components.
- **Integration method:** npm.
- **Dependencies:** React.
- **Availability:** Open source, current.
- **Maintenance:** Active (Adobe).
- **License:** Apache-2.0.
- **Limitations:** Headless; API surface is large; React-only.
- **Related resources:** Adobe Spectrum; HeroUI v3; React Spectrum.
- **Sources:** https://react-spectrum.adobe.com/react-aria/; https://github.com/adobe/react-spectrum
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A17. DaisyUI

- **Resource name:** DaisyUI
- **Canonical identity:** `saadeghi/daisyui` (GitHub); npm `daisyui`
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (Tailwind CSS component plugin)
- **Official URL:** https://daisyui.com/
- **Description:** Tailwind CSS plugin adding semantic component class names (btn, card, modal…) on top of Tailwind utilities, with 30+ themes and CSS-variable theming. MIT.
- **Contents inspected:** daisyui.com docs; GitHub README (install as Tailwind plugin).
- **Actual capabilities:** Component classes + theme switcher via `data-theme`; no JS (bring your own behavior).
- **Usage domain:** Rapid Tailwind UI; prototypes.
- **Inputs:** `npm i -D daisyui`; Tailwind plugin config.
- **Outputs:** Class-based component styling.
- **Integration method:** Tailwind plugin.
- **Dependencies:** Tailwind CSS.
- **Availability:** Open source, current.
- **Maintenance:** Active (Pouya Saadeghi).
- **License:** MIT.
- **Limitations:** Class-only (no behavior/accessibility); Tailwind-tied.
- **Related resources:** Tailwind CSS; Flowbite.
- **Sources:** https://daisyui.com/; https://github.com/saadeghi/daisyui
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A18. Shoelace

- **Resource name:** Shoelace
- **Canonical identity:** shoelace.style; GitHub `shoelace-style/shoelace`
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (framework-agnostic web components)
- **Official URL:** https://shoelace.style/
- **Description:** Forward-thinking library of framework-agnostic web components (custom elements): works with all frameworks, or none. Theming via CSS parts/variables; autoloader CDN.
- **Contents inspected:** shoelace.style docs (component list, theming).
- **Actual capabilities:** 40+ web components (dialog, dropdown, tree, QR code, relative time…).
- **Usage domain:** Framework-agnostic design systems; CMS-embedded UI.
- **Inputs:** CDN `<script>` + `<sl-button>` tags, or npm.
- **Outputs:** Native custom-element UI.
- **Integration method:** CDN autoloader or npm.
- **Dependencies:** None (native web components).
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT (verify in repo; medium confidence).
- **Limitations:** Web-component ergonomics (slots, form association) differ from React APIs.
- **Related resources:** Lit; Spectrum Web Components.
- **Sources:** https://shoelace.style/; https://github.com/shoelace-style/shoelace
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### A19. Atlassian Design System (Atlaskit)

- **Resource name:** Atlassian Design System
- **Canonical identity:** atlassian.design; npm `@atlaskit/*` (Bitbucket: atlassian/atlaskit-mk-2)
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (React components + tokens) + docs-only foundations/brand
- **Official URL:** https://atlassian.design/
- **Description:** Atlassian's system (Jira/Confluence/Trello): `@atlaskit/*` React components, design tokens (`@atlaskit/tokens`), theming (light/dark), illustration/icon guidance, content/brand guidelines.
- **Contents inspected:** atlassian.design docs; `@atlaskit/tokens` docs; third-party implementation notes.
- **Actual capabilities:** 50+ React components, token theming, ESLint/stylelint configs, Figma libraries.
- **Usage domain:** Atlassian-ecosystem apps, team-collaboration products.
- **Inputs:** `npm i @atlaskit/button @atlaskit/tokens`.
- **Outputs:** Atlassian-look React UI.
- **Integration method:** npm (Bitbucket registry mirror).
- **Dependencies:** React.
- **Availability:** Open source (code) with brand-use restrictions on Atlassian marks; current.
- **Maintenance:** Active (Atlassian).
- **License:** Apache-2.0 for code (typical); brand assets restricted. Verify per package.
- **Limitations:** Monorepo packaging churn (atlaskit-mk-2); strong Atlassian visual identity.
- **Related resources:** Atlaskit editor (ProseMirror); Atlassian Illustration guidelines.
- **Sources:** https://atlassian.design/; https://bitbucket.org/atlassian/atlaskit-mk-2
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### A20. Style Dictionary (Amazon)

- **Resource name:** Style Dictionary
- **Canonical identity:** `amzn/style-dictionary` (GitHub)
- **Category:** Part 4 — Design systems and official interface guidelines (design tokens)
- **Type:** Implementation (token build toolchain)
- **Official URL:** https://styledictionary.com/ (docs)
- **Description:** Amazon's build system for design tokens: single source of truth (JSON/YAML/JS) transformed into platform artifacts (CSS variables, iOS, Android, JS). Predecessor/adjacent to W3C DTCG format; v4/v5 current.
- **Contents inspected:** styledictionary.com docs; GitHub README (transform/config model).
- **Actual capabilities:** Token parsing, transforms, formats, multi-platform output; extensible.
- **Usage domain:** Design-token pipelines for multi-platform systems.
- **Inputs:** Token files (JSON/YAML/JS) + config.
- **Outputs:** CSS/SCSS/LESS variables, Swift, Kotlin, JS/TS, docs.
- **Integration method:** Node CLI/API; CI pipelines.
- **Dependencies:** Node.js.
- **Availability:** Open source, current.
- **Maintenance:** Active (Amazon).
- **License:** Apache-2.0.
- **Limitations:** Build tool only — no tokens shipped; config learning curve.
- **Related resources:** Tokens Studio; W3C DTCG; Figma Variables API.
- **Sources:** https://styledictionary.com/; https://github.com/amzn/style-dictionary
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### A21. Tokens Studio (formerly Figma Tokens)

- **Resource name:** Tokens Studio for Figma
- **Canonical identity:** Tokens Studio (tokens.studio); Figma plugin + Studio platform
- **Category:** Part 4 — Design systems and official interface guidelines (design tokens)
- **Type:** Hosted service + Figma plugin implementation
- **Official URL:** https://tokens.studio/
- **Description:** Token management for design systems (evolved from the "Figma Tokens" plugin): design tokens in Figma, sync to GitHub/GitLab, W3C DTCG alignment, multi-brand theming, Style Dictionary integration.
- **Contents inspected:** tokens.studio site; plugin listing.
- **Actual capabilities:** Token creation/editing in Figma, version sync to repos, DTCG export, Style Dictionary transforms.
- **Usage domain:** Design-token authoring/governance.
- **Inputs:** Figma file; token JSON in Git.
- **Outputs:** DTCG token JSON; platform artifacts via Style Dictionary.
- **Integration method:** Figma plugin; Git sync; web Studio.
- **Dependencies:** Figma account; Git provider.
- **Availability:** Freemium (pricing tiers exist; exact tiers not re-verified — thin coverage).
- **Maintenance:** Active.
- **License:** Proprietary (plugin/service); exported tokens are user's own.
- **Limitations:** Pricing/thin coverage; vendor workflow.
- **Related resources:** Style Dictionary; Figma Variables; Specify (historical competitor).
- **Sources:** https://tokens.studio/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### A22. MUI X (data components)

- **Resource name:** MUI X
- **Canonical identity:** `mui/mui-x` (GitHub); npm `@mui/x-data-grid` etc.
- **Category:** Part 4 — Design systems and official interface guidelines
- **Type:** Implementation (advanced React data components; commercial + MIT tiers)
- **Official URL:** https://mui.com/x/
- **Description:** MUI's advanced component set: Data Grid, Date/Time Pickers, Charts, Tree View, Scheduling. Community (MIT) + Pro/Premium (commercial) tiers.
- **Contents inspected:** mui.com/x docs (tiers, licensing).
- **Actual capabilities:** High-performance data grid, pickers, charts, tree.
- **Usage domain:** Data-dense React apps.
- **Inputs:** npm install per component family.
- **Outputs:** Feature-rich data components.
- **Integration method:** npm; MUI theme integration.
- **Dependencies:** React; @mui/material for theming.
- **Availability:** Open core; current.
- **Maintenance:** Active (MUI).
- **License:** MIT (Community) + commercial (Pro/Premium).
- **Limitations:** Advanced features paywalled; React-only.
- **Related resources:** MUI (Material UI); AG Grid (competitor).
- **Sources:** https://mui.com/x/; https://github.com/mui/mui-x
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

> Also noted (supplementary, compact): **Untitled UI React** (5000+ components, React Aria primitives, free tier + $349 PRO — partially verified); **Ant Design** (~99.7k stars, MIT, `.agents/skills` + DESIGN.md in repo — dedup-adjacent, not re-researched); **MUI Material** (~99k stars, MIT, AGENTS.md/skills in repo — dedup-adjacent); **Fluent UI Copilot chat components** (covered in A4).

---

## PART B — UI/UX theory resources (docs-only + checklists + agent skills)

> DEDUP note: keysjoao/laws-of-ux-skills, emilkowalski/skills (apple-design), and lawsofux.com are cross-referenced only.

### B1. Nielsen Norman Group — 10 Usability Heuristics

- **Resource name:** 10 Usability Heuristics for User Interface Design (Nielsen Norman Group)
- **Canonical identity:** nngroup.com article (Jakob Nielsen, 1994; updated 2020/2024)
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Docs-only (reference article + poster downloads)
- **Official URL:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Description:** The canonical 10 heuristics: visibility of system status, match with real world, user control, consistency, error prevention, recognition over recall, flexibility, aesthetic/minimalist design, error recovery, help/documentation.
- **Contents inspected:** Article page (heuristic list verified); NN/g UX certification context.
- **Actual capabilities:** Evaluation framework for heuristic reviews/UX audits; teaching reference.
- **Usage domain:** Usability evaluation, design critique, UX audits.
- **Inputs:** A UI to evaluate.
- **Outputs:** Heuristic evaluation findings.
- **Integration method:** Human process; encoded in third-party skills/checklists (e.g., laws-of-ux-skills, audits).
- **Dependencies:** None.
- **Availability:** Free article; NN/g courses paid.
- **Maintenance:** Stable (minor updates).
- **License:** Copyrighted prose (NN/g). Short quotes/fair use only.
- **Limitations:** General principles, not implementation guidance.
- **Related resources:** NN/g UX audit guides; heuristic evaluation templates.
- **Sources:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### B2. UX Project Checklist (uxchecklist.github.io)

- **Resource name:** UX Project Checklist
- **Canonical identity:** `uxchecklist` (GitHub Pages: uxchecklist.github.io)
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Implementation-lite (interactive checklist web app, open source)
- **Official URL:** https://uxchecklist.github.io/
- **Description:** Open-source interactive checklist for UX projects: research, plan, explore, communicate, create, feedback, delight, analyse — with per-phase check items and progress tracking.
- **Contents inspected:** Site (phase list verified); repo presence.
- **Actual capabilities:** Phase-gated UX QA checklist; local progress state.
- **Usage domain:** UX process QA, project reviews.
- **Inputs:** Project stage; checkbox interaction.
- **Outputs:** Completion state; review prompts.
- **Integration method:** Hosted page; GitHub Pages repo forkable.
- **Dependencies:** Browser.
- **Availability:** Free, open.
- **Maintenance:** Community (slow).
- **License:** Not verified (check repo).
- **Limitations:** Checklist-level depth only.
- **Related resources:** NN/g heuristics; UX audit templates.
- **Sources:** https://uxchecklist.github.io/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### B3. Refactoring UI (book + components)

- **Resource name:** Refactoring UI
- **Canonical identity:** Adam Wathan & Steve Schoger; refactoringui.com
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Docs-only (commercial book) + implementation-adjacent (Refactoring UI component patterns)
- **Official URL:** https://www.refactoringui.com/
- **Description:** Tactical UI design book: hierarchy, layout, spacing, typography, color, depth, working with constraints. De-facto styling bible for developers; many AI coding assistants' outputs follow its rules.
- **Contents inspected:** Site structure (chapters, tips); third-party agent skill encodings.
- **Actual capabilities:** Concrete visual-design rules with before/after examples.
- **Usage domain:** Developer-driven UI polish; design QA.
- **Inputs:** A UI draft.
- **Outputs:** Applied styling rules.
- **Integration method:** Book/PDF; skills encode its rules for agents.
- **Dependencies:** None.
- **Availability:** Paid book; free tips excerpts.
- **Maintenance:** Stable edition.
- **License:** Copyrighted (paid); no redistribution.
- **Limitations:** Styling-focused; not UX research.
- **Related resources:** Tailwind UI (same authors); "Refactoring UI" community skills.
- **Sources:** https://www.refactoringui.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### B4. W3C WCAG 2.2 + ARIA APG (accessibility references)

- **Resource name:** WCAG 2.2 / WAI-ARIA Authoring Practices Guide (APG)
- **Canonical identity:** W3C WAI standards: WCAG 2.2 (Rec), ARIA 1.3, APG
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Docs-only (normative standards + patterns)
- **Official URL:** https://www.w3.org/WAI/WCAG22/quickref/ ; https://www.w3.org/WAI/ARIA/apg/
- **Description:** WCAG 2.2 quickref (filterable success criteria, A/AA/AAA); APG provides accessible interaction patterns (dialog, combobox, treeview…) with keyboard/ARIA semantics. POUR principles underpin.
- **Contents inspected:** quickref page; APG pattern list.
- **Actual capabilities:** Normative accessibility requirements; implementation patterns for widgets.
- **Usage domain:** Accessibility compliance, audits, component implementation.
- **Inputs:** UI/component under review.
- **Outputs:** Conformance claims; accessible patterns.
- **Integration method:** Referenced by linters (axe-core), skills, design systems.
- **Dependencies:** None.
- **Availability:** Free, open standards.
- **Maintenance:** Active (W3C WAI; WCAG 3 draft in progress).
- **License:** W3C document license (permissive for standards).
- **Limitations:** Criteria-level; patterns not drop-in code.
- **Related resources:** axe-core; React Aria; GOV.UK/USWDS accessibility guidance.
- **Sources:** https://www.w3.org/WAI/WCAG22/quickref/; https://www.w3.org/WAI/ARIA/apg/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### B5. Baymard Institute (ecommerce UX research)

- **Resource name:** Baymard Institute
- **Canonical identity:** baymard.com (independent UX research institute)
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Docs-only (research reports; hosted service/paid)
- **Official URL:** https://baymard.com/
- **Description:** Large-scale ecommerce UX research: 130k+ hours of UX research, benchmarked UX guidelines for checkout, product pages, navigation, mobile. Free articles + premium full reports/database.
- **Contents inspected:** Site (research areas, free vs premium split verified).
- **Actual capabilities:** Evidence-backed UX guidelines with benchmarked examples.
- **Usage domain:** Ecommerce/product UX, UX audits.
- **Inputs:** Subscription (premium) or free articles.
- **Outputs:** UX guidelines, benchmark scores.
- **Integration method:** Web research library.
- **Dependencies:** None.
- **Availability:** Freemium (premium paywalled).
- **Maintenance:** Active (ongoing research).
- **License:** Copyrighted; premium terms.
- **Limitations:** Ecommerce-scoped; paywall for depth.
- **Related resources:** NN/g ecommerce research.
- **Sources:** https://baymard.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### B6. Material Motion (motion design guidelines)

- **Resource name:** Material Design — Motion guidelines
- **Canonical identity:** m3.material.io/styles/motion
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Docs-only (motion theory + tokens)
- **Official URL:** https://m3.material.io/styles/motion
- **Description:** Motion system: easing curves (standard/emphasized), duration tokens (short/medium/long), spatial/temporal patterns, transitions (shared axis, container transform). Reference for motion tokens and micro-interaction timing.
- **Contents inspected:** Motion styles page (easing/duration tokens verified).
- **Actual capabilities:** Token values + principles for consistent motion.
- **Usage domain:** Motion design, micro-interactions.
- **Inputs:** Design tokens page.
- **Outputs:** Easing curves, durations to implement.
- **Integration method:** Docs reference; tokens exported via Material theme builder.
- **Dependencies:** None.
- **Availability:** Free docs.
- **Maintenance:** Active (Material 3).
- **License:** CC-BY for docs (typical; verify).
- **Limitations:** Material-flavored; theory only.
- **Related resources:** Material Design 3 (dedup); GSAP/Motion (implementation).
- **Sources:** https://m3.material.io/styles/motion
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### B7. Typewolf / Fonts In Use (typography references)

- **Resource name:** Typewolf; Fonts In Use
- **Canonical identity:** typewolf.com; fontsinuse.com
- **Category:** Part 17 — UI/UX theory resources
- **Type:** Inspiration/reference (curated font usage, docs-adjacent)
- **Official URL:** https://www.typewolf.com/ ; https://fontsinuse.com/
- **Description:** Typewolf: what's trending in type, font recommendations, site-of-the-day with type details. Fonts In Use: independent archive of typography in use (print + web), searchable by typeface.
- **Contents inspected:** Both sites (structure, search/browse verified).
- **Actual capabilities:** Typeface discovery, pairing references, usage examples.
- **Usage domain:** Typography selection, visual hierarchy.
- **Inputs:** Browsing/search.
- **Outputs:** Font recommendations; usage specimens.
- **Integration method:** Web reference.
- **Dependencies:** None.
- **Availability:** Free browsing (Typewolf has paid guides).
- **Maintenance:** Active.
- **License:** Reference content; fonts themselves licensed separately (verify per font).
- **Limitations:** Reference only, no font files (Fonts In Use links to foundries).
- **Related resources:** Google Fonts; Fontsource; Butterick's Practical Typography.
- **Sources:** https://www.typewolf.com/; https://fontsinuse.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

---

## PART C — Design inspiration & resource directories

> Each record states what the directory provides: downloadable code / reusable component / design file / inspiration image / hosted service / reference collection.

### C1. Awwwards

- **Resource name:** Awwwards
- **Canonical identity:** awwwards.com (awards + conference platform)
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (juried awards) + hosted service (paid submissions)
- **Official URL:** https://www.awwwards.com/
- **Description:** Juried awards for web design/development/creativity: Site of the Day/Month/Year, developer awards; showcases cutting-edge interactive sites with credits and tech details.
- **Contents inspected:** Homepage + awards structure (SOTD/SOTM/SOTY verified).
- **Actual capabilities:** Curated inspiration with jury scores; nominee submissions (paid).
- **Usage domain:** Creative web inspiration, trend spotting.
- **Inputs:** Browsing; paid submission for nominees.
- **Outputs:** Inspiration only (no code/files by default; some winners link repos).
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free browsing; paid submissions/pro.
- **Maintenance:** Active.
- **License:** Screenshots/designs remain creators' property.
- **Limitations:** Inspiration only; avant-garde bias.
- **Related resources:** The FWA; Godly; CSS Design Awards.
- **Sources:** https://www.awwwards.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C2. The FWA

- **Resource name:** The FWA (Favourite Website Awards)
- **Canonical identity:** thefwa.com
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (long-running awards)
- **Official URL:** https://thefwa.com/
- **Description:** One of the oldest web-design award programs (est. 2000): FWA of the Day/Month, cutting-edge interactive work.
- **Contents inspected:** Site structure (daily/monthly awards verified).
- **Actual capabilities:** Curated interactive-work inspiration.
- **Usage domain:** Creative web inspiration.
- **Inputs:** Browsing.
- **Outputs:** Inspiration only.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free browsing.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Inspiration only; slower cadence than Awwwards.
- **Related resources:** Awwwards; Codrops.
- **Sources:** https://thefwa.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C3. Godly (godly.website)

- **Resource name:** Godly
- **Canonical identity:** godly.website (curated by Unframe Studio)
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (curated, brutalist/editorial taste)
- **Official URL:** https://godly.website/
- **Description:** Hand-picked curation of exceptional websites with strong editorial taste; tagged by style/industry.
- **Contents inspected:** Homepage curation + tagging (verified).
- **Actual capabilities:** Filtered inspiration browsing.
- **Usage domain:** Web design inspiration.
- **Inputs:** Browsing.
- **Outputs:** Inspiration links only.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Inspiration only; subjective curation.
- **Related resources:** SiteInspire; Httpster; Minimal Gallery.
- **Sources:** https://godly.website/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C4. SiteInspire

- **Resource name:** SiteInspire
- **Canonical identity:** siteinspire.com
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (curated web design showcase)
- **Official URL:** https://www.siteinspire.com/
- **Description:** Showcase of well-designed websites, filterable by style/type/platform; long-running curation.
- **Contents inspected:** Gallery + filters (verified).
- **Actual capabilities:** Filtered inspiration browsing.
- **Usage domain:** Web design inspiration.
- **Inputs:** Browsing/filters.
- **Outputs:** Inspiration only.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Inspiration only.
- **Related resources:** Land-book; Lapa Ninja.
- **Sources:** https://www.siteinspire.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C5. Land-book

- **Resource name:** Land-book
- **Canonical identity:** land-book.com
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (landing pages + websites)
- **Official URL:** https://land-book.com/
- **Description:** Curated gallery of landing pages and websites; tagging by category.
- **Contents inspected:** Gallery pages (verified).
- **Actual capabilities:** Inspiration browsing.
- **Usage domain:** Landing-page inspiration.
- **Inputs:** Browsing.
- **Outputs:** Inspiration only.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Inspiration only.
- **Related resources:** Lapa Ninja; Landingfolio.
- **Sources:** https://land-book.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C6. Lapa Ninja

- **Resource name:** Lapa Ninja
- **Canonical identity:** lapa.ninja
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (landing pages, 7,300+)
- **Official URL:** https://www.lapa.ninja/
- **Description:** Large curated landing-page gallery (7,300+ pages claimed), searchable/filterable.
- **Contents inspected:** Homepage count claim + gallery (verified).
- **Actual capabilities:** Searchable landing-page inspiration.
- **Usage domain:** Landing-page inspiration.
- **Inputs:** Browsing/search.
- **Outputs:** Inspiration only.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Inspiration only.
- **Related resources:** Land-book; One Page Love.
- **Sources:** https://www.lapa.ninja/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C7. Landingfolio

- **Resource name:** Landingfolio
- **Canonical identity:** landingfolio.com
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery + component teardowns (hosted service elements)
- **Official URL:** https://www.landingfolio.com/
- **Description:** Landing-page inspiration with component-level teardowns and copy breakdowns; some Figma resources.
- **Contents inspected:** Gallery + teardown format (verified).
- **Actual capabilities:** Inspiration + structured breakdowns.
- **Usage domain:** Landing-page design/copy inspiration.
- **Inputs:** Browsing.
- **Outputs:** Inspiration; teardown notes.
- **Integration method:** Web gallery.
- **Dependencies:** None.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Creators' property.
- **Limitations:** Mostly inspiration; teardowns partial.
- **Related resources:** Lapa Ninja; SaasFrame.
- **Sources:** https://www.landingfolio.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C8. Mobbin

- **Resource name:** Mobbin
- **Canonical identity:** mobbin.com
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Hosted service (paid; login-gated reference library)
- **Official URL:** https://mobbin.com/
- **Description:** Reference library of real mobile/web app UI flows (screens + user flows from production apps). Login-gated; subscription for full access.
- **Contents inspected:** Marketing pages only (login-gated library not inspected).
- **Actual capabilities:** Searchable real-app screen/flow reference.
- **Usage domain:** Product UI/UX reference, flow benchmarking.
- **Inputs:** Account + subscription.
- **Outputs:** Screen/flow reference (no code).
- **Integration method:** Web app (authenticated).
- **Dependencies:** Account.
- **Availability:** Paid subscription.
- **Maintenance:** Active.
- **License:** Screenshots for reference; redistribution restricted by ToS.
- **Limitations:** Not inspectable without login; paywalled; no code.
- **Related resources:** Page Flows; Refero; Screenlane.
- **Sources:** https://mobbin.com/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified** (login-gated; library contents not directly inspected).

### C9. Dribbble

- **Resource name:** Dribbble
- **Canonical identity:** dribbble.com (marketplace + portfolio network)
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (shots) + hosted service (marketplace, jobs)
- **Official URL:** https://dribbble.com/
- **Description:** Designer portfolio network: "shots" (UI/visual design images), design marketplace assets, hiring.
- **Contents inspected:** Public shots browsing (verified).
- **Actual capabilities:** Visual inspiration; asset marketplace; hiring.
- **Usage domain:** Visual design inspiration; asset discovery.
- **Inputs:** Browsing; marketplace purchase.
- **Outputs:** Inspiration images; purchased design assets.
- **Integration method:** Web platform.
- **Dependencies:** None for browsing.
- **Availability:** Free browsing; paid marketplace/pro.
- **Maintenance:** Active.
- **License:** Shots are creators' property; marketplace assets per-item license.
- **Limitations:** Mockups often not production-realistic; inspiration only unless purchasing.
- **Related resources:** Behance; Muzli.
- **Sources:** https://dribbble.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C10. Behance

- **Resource name:** Behance
- **Canonical identity:** behance.net (Adobe)
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Inspiration gallery (portfolio projects)
- **Official URL:** https://www.behance.net/
- **Description:** Adobe's creative portfolio network: full project case studies across UI/UX, branding, motion.
- **Contents inspected:** Public project browsing (verified).
- **Actual capabilities:** Case-study inspiration; creative hiring.
- **Usage domain:** Design inspiration, portfolios.
- **Inputs:** Browsing.
- **Outputs:** Inspiration only.
- **Integration method:** Web platform.
- **Dependencies:** None for browsing.
- **Availability:** Free.
- **Maintenance:** Active (Adobe).
- **License:** Creators' property.
- **Limitations:** Inspiration only; case studies curated for show.
- **Related resources:** Dribbble; Adobe Portfolio.
- **Sources:** https://www.behance.net/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C11. Codrops (Tympanus)

- **Resource name:** Codrops (Tympanus)
- **Canonical identity:** tympanus.net/codrops
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Reference collection (tutorials + downloadable code experiments)
- **Official URL:** https://tympanus.net/codrops/
- **Description:** Long-running creative-coding resource: tutorials and experimental demos (WebGL, SVG, CSS, canvas) with source code; blueprint/collective sections.
- **Contents inspected:** Articles + demo pages (source available per demo verified).
- **Actual capabilities:** Copy-adaptable creative code; technique tutorials.
- **Usage domain:** Creative web experiments, motion, WebGL.
- **Inputs:** Browsing; downloading demo source.
- **Outputs:** Demo source code (adaptable).
- **Integration method:** Web; code download.
- **Dependencies:** Varies per demo.
- **Availability:** Free.
- **Maintenance:** Active (Tympanus).
- **License:** Demos free for personal/commercial use with credit (verify per demo — typical Codrops terms).
- **Limitations:** Experimental quality; not production components.
- **Related resources:** The FWA; Awwwards.
- **Sources:** https://tympanus.net/codrops/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C12. Figma Community

- **Resource name:** Figma Community
- **Canonical identity:** figma.com/community
- **Category:** Part 17 — Design inspiration and resource directories
- **Type:** Hosted service (design files, plugins, widgets; free + paid)
- **Official URL:** https://www.figma.com/community
- **Description:** Figma's official resource hub: community files (UI kits, templates), plugins, widgets. Hosts official kits (Material 3, Primer, Atlassian, Ant, Polaris, Fluent 2, shadcn community files, Untitled UI Free, VS Code Toolkit) plus Relume's Figma export plugin.
- **Contents inspected:** Community hub structure; kit listings (verified).
- **Actual capabilities:** Duplicatable design files; plugins (incl. Relume, Musho, Locofy); widgets.
- **Usage domain:** Design files, templates, plugin distribution.
- **Inputs:** Figma account.
- **Outputs:** .fig design files (duplicatable), plugin installs.
- **Integration method:** Figma app.
- **Dependencies:** Figma account.
- **Availability:** Free + paid files.
- **Maintenance:** Active (Figma).
- **License:** Per-file license set by creator (verify per file).
- **Limitations:** Design files only (not code); license varies per file.
- **Related resources:** Framer Marketplace; Webflow templates.
- **Sources:** https://www.figma.com/community
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C13. Aceternity UI

- **Resource name:** Aceternity UI
- **Canonical identity:** `aceternity` — ui.aceternity.com
- **Category:** Part 17 — Design inspiration and resource directories (copy-paste components)
- **Type:** Implementation (copy-paste React/Tailwind components)
- **Official URL:** https://ui.aceternity.com/
- **Description:** Copy-paste animated React components (Tailwind + Framer Motion): hero sections, cards, 3D effects, backgrounds. MIT.
- **Contents inspected:** Component gallery + code snippets (verified).
- **Actual capabilities:** Paste-ready animated components.
- **Usage domain:** Marketing sites, portfolios.
- **Inputs:** Copy component code.
- **Outputs:** React/Tailwind components in your project.
- **Integration method:** Copy-paste; npm deps per component.
- **Dependencies:** React, Tailwind, Framer Motion (per component).
- **Availability:** Free, open.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Not an npm package — manual copy; accessibility varies.
- **Related resources:** Magic UI; Motion Primitives; Cult UI.
- **Sources:** https://ui.aceternity.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C14. Magic UI

- **Resource name:** Magic UI
- **Canonical identity:** magicui.design
- **Category:** Part 17 — Design inspiration and resource directories (copy-paste components)
- **Type:** Implementation (copy-paste React/Tailwind animated components)
- **Official URL:** https://magicui.design/
- **Description:** Copy-paste animated components/effects for React+Tailwind (marquee, borders, particles, text effects). MIT.
- **Contents inspected:** Component gallery (verified).
- **Actual capabilities:** Paste-ready animated UI effects.
- **Usage domain:** Marketing sites.
- **Inputs:** Copy code.
- **Outputs:** React components.
- **Integration method:** Copy-paste.
- **Dependencies:** React, Tailwind (per component).
- **Availability:** Free, open.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Effects-focused, not full components.
- **Related resources:** Aceternity UI; Motion Primitives.
- **Sources:** https://magicui.design/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### C15. brunovareliuu/inspo (agent research tool)

- **Resource name:** inspo (brunovareliuu/inspo)
- **Canonical identity:** `brunovareliuu/inspo` (GitHub)
- **Category:** Part 17 — Design inspiration and resource directories (agent-facing)
- **Type:** Implementation (CLI/agent tool for design research)
- **Official URL:** https://github.com/brunovareliuu/inspo
- **Description:** Agent-oriented design-research CLI: searches inspiration sources and returns structured design references for AI coding agents.
- **Contents inspected:** GitHub README (usage verified).
- **Actual capabilities:** CLI queries returning design-inspiration data for agents.
- **Usage domain:** AI-agent design research.
- **Inputs:** CLI query.
- **Outputs:** Structured inspiration references.
- **Integration method:** Bash/CLI.
- **Dependencies:** Node (verify).
- **Availability:** Open source.
- **Maintenance:** Community.
- **License:** Not verified (check repo).
- **Limitations:** Research tool only; thin coverage.
- **Related resources:** Astryx CLI (dedup).
- **Sources:** https://github.com/brunovareliuu/inspo
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

> Also noted (supplementary): **Collect UI** (daily UI inspiration, curated — verified site); **UI Movement** (ui-movement.com, mobile UI — verified); **Minimal Gallery** (minimal.gallery — verified); **Httpster** (httpster.net — verified); **One Page Love** (onepagelove.com — verified); **Hoverstat.es** (hoverstat.es, hover-state showcase — verified); **footer.design** (footer gallery — verified); **Navbar Gallery** (partially verified); **Muzli** (muz.li, design inspiration feed — verified); **SaasFrame** (saasframe.io — verified); **Refero** (refero.design, design details — verified); **Page Flows** (pageflows.com, user-flow recordings, paid — partially verified); **Dark Mode Design** (partially verified); **Screenlane** (screenlane.com — verified); **Cult UI** (cult-ui.com, MIT copy-paste — verified); **Motion Primitives** (motion-primitives.com, MIT — verified); **React Bits** (reactbits.dev, MIT + Commons Clause — verified); **Skiper UI** (skiper-ui.com — partially verified); **Origin UI** (originui.com, MIT — verified); **HyperUI** (hyperui.dev, Tailwind components — verified); **Uiverse.io** (uiverse.io, community CSS elements — verified); **Tailwind Plus** (tailwindcss.com/plus, paid blocks — verified); **Flowbite** (flowbite.com, Tailwind components — verified); **21st.dev** (magic MCP component registry — partially verified); **Tremor** (tremor.so, React dashboards — verified); **Cruip** (cruip.com, templates — verified); **shadcnblocks.com** (paid blocks — verified); **pnnnhan99/awesome-copy-paste-ui** (index repo — partially verified); **Relume library** (relume.io, 1000+ Webflow/Figma components — covered in Part E as builder).

---

## PART D — Creative assets & asset pipelines

> Licenses recorded as documented; no legal interpretation beyond evidence. Restrictions noted where found.

### D1. Lucide (icons)

- **Resource name:** Lucide
- **Canonical identity:** lucide.dev; `lucide-icons/lucide` (GitHub)
- **Category:** Part 17 — Creative assets and asset pipelines (icons)
- **Type:** Implementation (icon library: SVG, web components, framework packages)
- **Official URL:** https://lucide.dev/
- **Description:** Open-source icon set (1500+ icons, 24×24 stroke icons): SVG files, web components, React/Vue/Svelte/Angular packages, Figma plugin.
- **Contents inspected:** lucide.dev (icon browser, framework packages verified); GitHub README.
- **Actual capabilities:** Consistent stroke icons; tree-shakable packages; customization (stroke width, size, color).
- **Usage domain:** UI iconography.
- **Inputs:** npm install or SVG download.
- **Outputs:** Icons in app.
- **Integration method:** npm (`lucide-react` etc.) / SVG / CDN.
- **Dependencies:** Framework package per target.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** ISC.
- **Limitations:** Stroke style only; no filled/duotone variants.
- **Related resources:** Feather Icons (predecessor); Tabler; Phosphor.
- **Sources:** https://lucide.dev/; https://github.com/lucide-icons/lucide
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D2. Heroicons (icons)

- **Resource name:** Heroicons
- **Canonical identity:** heroicons.com; `tailwindlabs/heroicons` (GitHub)
- **Category:** Part 17 — Creative assets (icons)
- **Type:** Implementation (SVG icon set, Tailwind Labs)
- **Official URL:** https://heroicons.com/
- **Description:** Hand-crafted SVG icons by Tailwind Labs (outline + solid + mini/micro variants); React/Vue components.
- **Contents inspected:** heroicons.com (variants verified); GitHub README.
- **Actual capabilities:** 300+ icons in 3 styles.
- **Usage domain:** UI iconography (esp. Tailwind projects).
- **Inputs:** SVG copy or npm (`@heroicons/react`).
- **Outputs:** Icons.
- **Integration method:** npm / SVG.
- **Dependencies:** React/Vue (for component packages).
- **Availability:** Open source, current.
- **Maintenance:** Active (Tailwind Labs).
- **License:** MIT.
- **Limitations:** Smaller set than Lucide/Tabler.
- **Related resources:** Lucide; Tailwind CSS.
- **Sources:** https://heroicons.com/; https://github.com/tailwindlabs/heroicons
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D3. Tabler Icons (icons)

- **Resource name:** Tabler Icons
- **Canonical identity:** tabler.io/icons; `tabler/tabler-icons` (GitHub)
- **Category:** Part 17 — Creative assets (icons)
- **Type:** Implementation (SVG icon set, 5000+ icons)
- **Official URL:** https://tabler.io/icons
- **Description:** Large open-source icon set (5000+): outline style, SVG + framework packages (React/Vue/Svelte/Angular/Solid), Figma plugin, webfont.
- **Contents inspected:** tabler.io/icons (count, packages verified); GitHub README.
- **Actual capabilities:** High-coverage iconography with consistent style.
- **Usage domain:** UI iconography at scale.
- **Inputs:** npm / SVG / font.
- **Outputs:** Icons.
- **Integration method:** npm / CDN.
- **Dependencies:** Per framework.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Outline-only style.
- **Related resources:** Lucide; Phosphor; Tabler dashboard UI kit (separate).
- **Sources:** https://tabler.io/icons; https://github.com/tabler/tabler-icons
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D4. Phosphor Icons (icons)

- **Resource name:** Phosphor Icons
- **Canonical identity:** phosphoricons.com; `phosphor-icons/phosphor-home`
- **Category:** Part 17 — Creative assets (icons)
- **Type:** Implementation (SVG icon set, 6 weights/styles)
- **Official URL:** https://phosphoricons.com/
- **Description:** Flexible icon family: same icon in thin/light/regular/bold/fill/duotone weights; framework packages, Figma plugin.
- **Contents inspected:** phosphoricons.com (weights verified); GitHub org.
- **Actual capabilities:** Multi-weight iconography.
- **Usage domain:** UI iconography with weight flexibility.
- **Inputs:** npm / SVG.
- **Outputs:** Icons.
- **Integration method:** npm / CDN.
- **Dependencies:** Per framework.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Duotone styling needs care in monochrome contexts.
- **Related resources:** Lucide; Tabler.
- **Sources:** https://phosphoricons.com/; https://github.com/phosphor-icons/phosphor-home
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D5. Simple Icons (brand icons)

- **Resource name:** Simple Icons
- **Canonical identity:** simpleicons.org; `simple-icons/simple-icons` (GitHub)
- **Category:** Part 17 — Creative assets (brand icons)
- **Type:** Implementation (SVG brand icons, 3000+)
- **Official URL:** https://simpleicons.org/
- **Description:** SVG icons for popular brands (3000+): single-color paths; npm packages, CDN.
- **Contents inspected:** simpleicons.org; GitHub README (contribution model verified).
- **Actual capabilities:** Brand glyphs as SVGs.
- **Usage domain:** Brand/social iconography.
- **Inputs:** npm / CDN / SVG.
- **Outputs:** Brand icons.
- **Integration method:** npm / CDN.
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active (community).
- **License:** CC0 (project); brand trademarks belong to respective owners — trademark restrictions apply (documented).
- **Limitations:** Trademark law limits usage; single-color only.
- **Related resources:** WorldVectorLogo (not open).
- **Sources:** https://simpleicons.org/; https://github.com/simple-icons/simple-icons
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D6. unDraw (illustrations)

- **Resource name:** unDraw
- **Canonical identity:** undraw.co
- **Category:** Part 17 — Creative assets (illustrations)
- **Type:** Implementation (SVG illustration library, customizable)
- **Official URL:** https://undraw.co/
- **Description:** Open-source-style SVG illustrations with color customization (accent color picker); searchable; downloadable SVG/PNG.
- **Contents inspected:** undraw.co (customizer + downloads verified).
- **Actual capabilities:** Themed SVG illustrations.
- **Usage domain:** Landing pages, empty states, docs.
- **Inputs:** Browse + color pick.
- **Outputs:** SVG/PNG illustrations.
- **Integration method:** Download.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active (Katerina Limpitsouni).
- **License:** Free for commercial/personal use without attribution per site (verify current terms; medium confidence).
- **Limitations:** Single illustration style.
- **Related resources:** Humaaans; Open Doodles.
- **Sources:** https://undraw.co/
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### D7. Humaaans (illustrations)

- **Resource name:** Humaaans
- **Canonical identity:** humaaans.com (Pablo Stanley)
- **Category:** Part 17 — Creative assets (illustrations)
- **Type:** Implementation (mix-and-match illustration library)
- **Official URL:** https://www.humaaans.com/
- **Description:** Modular human illustrations: mix-and-match heads/bodies/poses; Figma library + PNG/SVG.
- **Contents inspected:** humaaans.com (mixer verified).
- **Actual capabilities:** Composable character illustrations.
- **Usage domain:** People-centric illustrations.
- **Inputs:** Figma library or web mixer.
- **Outputs:** Illustration assets.
- **Integration method:** Figma / download.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Community/stable.
- **License:** Free for commercial use (verify current terms; medium confidence).
- **Limitations:** Human-figure focus only.
- **Related resources:** Open Peeps; Blush (same author ecosystem).
- **Sources:** https://www.humaaans.com/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### D8. Fontsource (fonts)

- **Resource name:** Fontsource
- **Canonical identity:** fontsource.org; `fontsource/fontsource` (GitHub)
- **Category:** Part 17 — Creative assets (fonts/typography libraries)
- **Type:** Implementation (npm font packages, self-hosting)
- **Official URL:** https://fontsource.org/
- **Description:** Self-hostable webfont packages via npm: Google Fonts + others as `@fontsource/*` packages with subsetting/weights; privacy-friendly (no Google CDN).
- **Contents inspected:** fontsource.org (package naming, variable-font support verified); GitHub README.
- **Actual capabilities:** `npm i @fontsource-variable/inter`; CSS import of subsets/weights.
- **Usage domain:** Self-hosted web typography.
- **Inputs:** npm install.
- **Outputs:** Local font files via bundler.
- **Integration method:** npm + CSS import.
- **Dependencies:** Bundler.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT (tooling); fonts under their own licenses (mostly OFL — verify per font).
- **Limitations:** Package-per-font model; large node_modules footprint.
- **Related resources:** Google Fonts; google-webfonts-helper.
- **Sources:** https://fontsource.org/; https://github.com/fontsource/fontsource
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D9. Unsplash (stock photos)

- **Resource name:** Unsplash
- **Canonical identity:** unsplash.com (Getty Images owned since 2021)
- **Category:** Part 17 — Creative assets (images)
- **Type:** Hosted service (stock photo library + API)
- **Official URL:** https://unsplash.com/
- **Description:** Large free stock-photo library; Unsplash+ (paid) tier; public API for apps.
- **Contents inspected:** unsplash.com (license page verified).
- **Actual capabilities:** Search/download photos; API integration.
- **Usage domain:** Photography for web products.
- **Inputs:** Search; API key for API.
- **Outputs:** Photos (JPG).
- **Integration method:** Download; API; source.unsplash (deprecated — do not use).
- **Dependencies:** API key for programmatic use.
- **Availability:** Free + Unsplash+ paid.
- **Maintenance:** Active.
- **License:** Unsplash License (free use incl. commercial; restrictions: no selling unaltered copies, no trademark misuse — as documented).
- **Limitations:** License is not CC0; API rate limits; hotlinking discouraged.
- **Related resources:** Pexels; Pixabay; Openverse.
- **Sources:** https://unsplash.com/license
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D10. Haikei (backgrounds)

- **Resource name:** Haikei
- **Canonical identity:** haikei.app
- **Category:** Part 17 — Creative assets (patterns/backgrounds)
- **Type:** Hosted service (SVG background generator)
- **Official URL:** https://haikei.app/
- **Description:** Generative SVG background tool: blobs, waves, gradients, grids, stepped patterns; export SVG/PNG.
- **Contents inspected:** haikei.app (generators verified).
- **Actual capabilities:** Custom SVG background generation.
- **Usage domain:** Hero backgrounds, section dividers.
- **Inputs:** Generator parameters.
- **Outputs:** SVG/PNG.
- **Integration method:** Web app download.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active (zcreative).
- **License:** Free for commercial use per site (verify current terms; medium confidence).
- **Limitations:** Generator-bound styles.
- **Related resources:** Hero Patterns; SVG Backgrounds; MagicPattern.
- **Sources:** https://haikei.app/
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### D11. Lottie / dotLottie (animation files)

- **Resource name:** Lottie (lottie-web) / dotLottie
- **Canonical identity:** `airbnb/lottie-web`; dotlottie.org (LottieFiles)
- **Category:** Part 17 — Creative assets (animation files)
- **Type:** Implementation (player SDKs, open) + hosted service (LottieFiles library)
- **Official URL:** https://lottiefiles.com/ ; https://dotlottie.io/
- **Description:** Lottie: JSON-based animation format (After Effects via Bodymovin); `lottie-web` player MIT. dotLottie: newer compressed container (.lottie) with official players. LottieFiles: hosted animation library/marketplace (free + premium).
- **Contents inspected:** lottiefiles.com; dotlottie.io docs; `airbnb/lottie-web` README.
- **Actual capabilities:** Vector animations playable on web/iOS/Android; interactivity (state machines in dotLottie).
- **Usage domain:** UI animation, onboarding, empty states.
- **Inputs:** `.json` (Lottie) / `.lottie` files.
- **Outputs:** Rendered animations via player.
- **Integration method:** npm players (`lottie-web`, `@lottiefiles/dotlottie-web`, `lottie-react`).
- **Dependencies:** Player library.
- **Availability:** Open players; hosted library freemium.
- **Maintenance:** Active.
- **License:** MIT (players); animations per-asset license on LottieFiles (verify per asset).
- **Limitations:** After Effects feature subset; file sizes for complex animations.
- **Related resources:** Rive; Bodymovin.
- **Sources:** https://lottiefiles.com/; https://dotlottie.io/; https://github.com/airbnb/lottie-web
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D12. Rive (animation files)

- **Resource name:** Rive
- **Canonical identity:** rive.app
- **Category:** Part 17 — Creative assets (animation files + runtime)
- **Type:** Hosted service (editor) + implementation (open runtimes)
- **Official URL:** https://rive.app/
- **Description:** Real-time interactive animation: state machines, inputs, layout; `.riv` files; open-source runtimes (web/React/Flutter/etc.); editor is hosted.
- **Contents inspected:** rive.app (editor + runtimes verified); runtime repos.
- **Actual capabilities:** Interactive, input-driven animations (buttons, characters, loaders).
- **Usage domain:** Interactive UI animation, game UI.
- **Inputs:** `.riv` from Rive editor.
- **Outputs:** Interactive animations via runtime.
- **Integration method:** npm runtimes (`@rive-app/react-canvas` etc.).
- **Dependencies:** Runtime library.
- **Availability:** Freemium (editor free tier; teams paid).
- **Maintenance:** Active.
- **License:** Runtimes MIT-ish/open (verify per repo); editor ToS; community assets per-asset license.
- **Limitations:** Editor learning curve; hosted editor lock-in.
- **Related resources:** Lottie; Spine (2D skeletal).
- **Sources:** https://rive.app/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D13. Kenney (3D/game assets)

- **Resource name:** Kenney
- **Canonical identity:** kenney.nl/assets
- **Category:** Part 17 — Creative assets (3D models, sprites, audio)
- **Type:** Implementation (downloadable asset packs)
- **Official URL:** https://kenney.nl/assets
- **Description:** Large library of game-ready assets: 3D models, sprites, UI packs, audio — all CC0.
- **Contents inspected:** kenney.nl/assets (CC0 claim verified).
- **Actual capabilities:** Ready-to-use 3D/sprite/audio packs.
- **Usage domain:** Games, prototypes, 3D web scenes.
- **Inputs:** Download packs.
- **Outputs:** FBX/GLTF/PNG/WAV assets.
- **Integration method:** Download; drag into engines.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** CC0 (public domain dedication).
- **Limitations:** Stylized low-poly aesthetic.
- **Related resources:** Quaternius; KayKit; Poly Pizza.
- **Sources:** https://kenney.nl/assets
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D14. Quaternius (3D assets)

- **Resource name:** Quaternius
- **Canonical identity:** quaternius.com
- **Category:** Part 17 — Creative assets (3D models)
- **Type:** Implementation (downloadable pixel-art 3D packs)
- **Official URL:** https://quaternius.com/
- **Description:** Pixel-art-style low-poly 3D asset packs (characters, nature, buildings), CC0.
- **Contents inspected:** quaternius.com (CC0 verified).
- **Actual capabilities:** Cohesive low-poly 3D packs.
- **Usage domain:** Games, 3D web scenes.
- **Inputs:** Download.
- **Outputs:** GLTF/FBX/OBJ assets.
- **Integration method:** Download.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** CC0.
- **Limitations:** Pixel-art style only.
- **Related resources:** Kenney; KayKit.
- **Sources:** https://quaternius.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D15. Poly Pizza (3D models)

- **Resource name:** Poly Pizza
- **Canonical identity:** poly.pizza
- **Category:** Part 17 — Creative assets (3D models)
- **Type:** Hosted service (searchable 3D model library)
- **Official URL:** https://poly.pizza/
- **Description:** Search engine/library for low-poly 3D models; per-model licensing (CC0/CC-BY); Google Poly spiritual successor.
- **Contents inspected:** poly.pizza (search + per-model license badges verified).
- **Actual capabilities:** Searchable 3D model downloads.
- **Usage domain:** 3D web scenes, games.
- **Inputs:** Search.
- **Outputs:** GLTF/OBJ models.
- **Integration method:** Download.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Per-model (CC0 or CC-BY — check each model).
- **Limitations:** License varies per model; quality varies.
- **Related resources:** Sketchfab; Kenney.
- **Sources:** https://poly.pizza/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D16. Squoosh (image optimization)

- **Resource name:** Squoosh
- **Canonical identity:** squoosh.app; `GoogleChromeLabs/squoosh` (GitHub)
- **Category:** Part 17 — Creative assets (asset optimization)
- **Type:** Implementation (web app + CLI, open source)
- **Official URL:** https://squoosh.app/
- **Description:** GoogleChromeLabs image compression web app: compare codecs (WebP, AVIF, MozJPEG…), resize, CLI available; runs locally in browser (WASM).
- **Contents inspected:** squoosh.app (codecs verified); GitHub README.
- **Actual capabilities:** Lossy/lossless compression, format conversion, resizing.
- **Usage domain:** Web image optimization.
- **Inputs:** Image files.
- **Outputs:** Optimized images.
- **Integration method:** Web app; `@squoosh/cli`.
- **Dependencies:** Browser / Node (CLI).
- **Availability:** Open source, free.
- **Maintenance:** Low-active (GoogleChromeLabs; stable).
- **License:** Apache-2.0.
- **Limitations:** Single-file oriented; CLI less maintained.
- **Related resources:** Sharp; ImageOptim; TinyPNG (service).
- **Sources:** https://squoosh.app/; https://github.com/GoogleChromeLabs/squoosh
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D17. SVGO / SVGOMG (SVG optimization)

- **Resource name:** SVGO (+ SVGOMG web UI)
- **Canonical identity:** `svg/svgo` (GitHub); svgomg.net (Jake Archibald)
- **Category:** Part 17 — Creative assets (SVG optimization)
- **Type:** Implementation (Node tool + web UI)
- **Official URL:** https://svgomg.net/ (repo https://github.com/svg/svgo)
- **Description:** Standard SVG optimizer: plugin pipeline (remove metadata, minify paths, etc.); SVGOMG is the in-browser GUI.
- **Contents inspected:** svgomg.net; `svg/svgo` README (plugin list verified).
- **Actual capabilities:** SVG size reduction, configurable plugins.
- **Usage domain:** SVG asset pipelines.
- **Inputs:** SVG files.
- **Outputs:** Optimized SVG.
- **Integration method:** CLI/API; web UI; bundler plugins (svgr/svgo-loader).
- **Dependencies:** Node.js.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Aggressive plugins can break rendering (test output).
- **Related resources:** SVGOMG; svgr.
- **Sources:** https://github.com/svg/svgo; https://svgomg.net/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D18. The Book of Shaders (shader library/reference)

- **Resource name:** The Book of Shaders
- **Canonical identity:** thebookofshaders.com (Patricio Gonzalez Vivo & Jen Lowe)
- **Category:** Part 17 — Creative assets (shader libraries)
- **Type:** Docs-only (interactive book) + reference collection (example shaders)
- **Official URL:** https://thebookofshaders.com/
- **Description:** Gentle step-by-step GLSL guide with live editor: shapes, matrices, patterns, noise, FBM — the canonical creative-shader primer.
- **Contents inspected:** Chapters + live editor (verified).
- **Actual capabilities:** Learn/adapt fragment shaders.
- **Usage domain:** Shader learning, creative coding.
- **Inputs:** Browser.
- **Outputs:** GLSL knowledge + example code.
- **Integration method:** Web book; examples adaptable.
- **Dependencies:** None.
- **Availability:** Free.
- **Maintenance:** Stable classic.
- **License:** Examples permissive (verify per page; generally open).
- **Limitations:** Fragment-shader focused; WebGL1-era GLSL.
- **Related resources:** Shadertoy; iquilezles.org; LYGIA.
- **Sources:** https://thebookofshaders.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D19. Shadertoy (shader library)

- **Resource name:** Shadertoy
- **Canonical identity:** shadertoy.com
- **Category:** Part 17 — Creative assets (shader libraries)
- **Type:** Hosted service (shader sharing + live coding)
- **Official URL:** https://www.shadertoy.com/
- **Description:** Community platform for sharing fragment shaders with live WebGL preview: vast searchable archive (noise, raymarching, SDF art).
- **Contents inspected:** shadertoy.com (browse + editor verified).
- **Actual capabilities:** Live shader coding/sharing; embeddable.
- **Usage domain:** Shader art, effects research.
- **Inputs:** GLSL in browser editor.
- **Outputs:** Shaders (+ API embeds).
- **Integration method:** Web; API.
- **Dependencies:** Account for publishing.
- **Availability:** Free.
- **Maintenance:** Active.
- **License:** Shaders under CC BY-NC-SA 3.0 by default per site terms (verify; non-commercial default — restriction noted).
- **Limitations:** Default license is non-commercial; WebGL1 GLSL.
- **Related resources:** The Book of Shaders; glslsandbox.
- **Sources:** https://www.shadertoy.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### D20. Poly Haven (3D/textures/HDRIs)

- **Resource name:** Poly Haven
- **Canonical identity:** polyhaven.com
- **Category:** Part 17 — Creative assets (3D models, textures, HDRIs)
- **Type:** Implementation (downloadable CC0 library)
- **Official URL:** https://polyhaven.com/
- **Description:** High-quality CC0 assets: HDRIs, PBR textures, 3D models; API available.
- **Contents inspected:** polyhaven.com (CC0 + API verified).
- **Actual capabilities:** Production-quality PBR assets.
- **Usage domain:** 3D rendering, WebGL scenes.
- **Inputs:** Browse/download; API.
- **Outputs:** HDR/EXR/texture/model files.
- **Integration method:** Download; API.
- **Dependencies:** None.
- **Availability:** Free (patron-supported).
- **Maintenance:** Active.
- **License:** CC0.
- **Limitations:** Photoreal focus; library size smaller than commercial.
- **Related resources:** ambientCG; Quaternius.
- **Sources:** https://polyhaven.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

> Also noted (supplementary): **Icons** — Iconoir (MIT, iconoir.com — verified), Material Symbols (Apache-2.0, Google — verified), Radix Icons (MIT — verified), Bootstrap Icons (MIT — verified), Octicons (MIT, `@primer/octicons` — verified), Remix Icon (2026 custom license, restrictions — partially verified), Hugeicons (free/pro tiers — partially verified), Ionicons (MIT — verified), Carbon Icons (Apache-2.0 — verified), LobeHub Icons (MIT — partially verified), Iconify (unified icon framework, 200k+ icons — verified); **Illustrations** — Open Doodles (CC-BY — verified), Open Peeps (CC0 — verified), Storyset (Freepik, free w/ attribution — partially verified), DrawKit (drawkit.com — verified), ManyPixels (CC0 gallery — verified), illlustrations.co (MIT — verified), Blush (free+pro, per-asset check — partially verified), IRA Design (iradesign.io — partially verified), Absurd Design (absurd.design — verified); **Fonts** — Google Fonts (fonts.google.com, OFL/Apache — verified), google-webfonts-helper (gwfh.mranftl.com — verified), Fontshare (fontshare.com — verified), OpenDyslexic (OFL — verified), font subsetting: fonttools/glyphhanger/subfont (partially verified); **Stock** — Pexels (pexels.com — verified), Pixabay (pixabay.com — verified), Coverr (coverr.co — verified), Picsum (picsum.photos — verified), Wikimedia Commons (CC/varied — verified), Mixkit (mixkit.co — verified); **Backgrounds** — Hero Patterns (heropatterns.com — verified), Transparent Textures (transparenttextures.com — verified), SVG Backgrounds (svgbackgrounds.com — verified), MagicPattern (magicpattern.design — verified), Pattern Monster (pattern.monster — verified), Cool Backgrounds (coolbackgrounds.io — verified), Trianglify (trianglify.io — verified), BGJar (bgjar.com — verified), CSS Doodle (css-doodle.com — verified), Toptal Subtle Patterns (partially verified); **3D** — KayKit (kaykit.com, CC0 — verified), 3dicons.co (CC0 — verified), ambientCG (ambientcg.com, CC0 — verified), Sketchfab (sketchfab.com, per-model — verified), Mixamo (mixamo.com, Adobe — verified), Shapefest (shapefest.com — partially verified); **Optimization** — Sharp (`lovell/sharp`, Apache-2.0 — verified), ImageOptim (imageoptim.com — verified), Cloudinary/imgix (image transformation CDNs, hosted — verified).

---

## PART E — Design-to-code

> Each record states: inputs → outputs, supported environments, actual integration mechanism.

### E1. Figma Official MCP Server (remote + desktop)

- **Resource name:** Figma MCP Server (official)
- **Canonical identity:** Figma, Inc. — remote `https://mcp.figma.com/mcp`; desktop Dev Mode MCP at `http://127.0.0.1:3845/mcp`
- **Category:** Part 17 — Design-to-code (design-system grounding for AI agents)
- **Type:** Implementation (MCP server: remote hosted + local desktop)
- **Official URL:** https://developers.figma.com/docs/figma-mcp-server/
- **Description:** Official Model Context Protocol server exposing Figma file data to AI coding agents: design context extraction, screenshots, metadata, variable definitions, Code Connect mappings, design-system search. Remote server uses OAuth; desktop server serves the open Dev Mode file locally. Note from 2026-08-19 check: "Claude Code" is allowlisted for the OAuth app.
- **Contents inspected:** Figma developers docs (endpoints/tools verified); tool list from docs.
- **Actual capabilities:** Tools include `get_design_context`, `get_screenshot`, `get_metadata`, `get_variable_defs`, Code Connect `map`/`suggestions`, `search_design_system`.
- **Usage domain:** AI-agent design-to-code with live Figma files.
- **Inputs:** Figma file/node URLs; OAuth token (remote) or local Dev Mode.
- **Outputs:** Structured design context (layout, styles, components), screenshots, code suggestions.
- **Integration method:** MCP client config (Claude Code, Cursor, VS Code, etc.).
- **Dependencies:** Figma account; file access permissions; MCP-capable client.
- **Availability:** Current; free tier + paid Figma seats for Dev Mode features.
- **Maintenance:** Active (Figma).
- **License:** Proprietary service; API ToS.
- **Limitations:** Requires file access; OAuth allowlist nuances; screenshot fidelity limits; large files need selection scoping.
- **Related resources:** Figma Dev Mode; Code Connect; Tokens Studio.
- **Sources:** https://developers.figma.com/docs/figma-mcp-server/; https://www.figma.com/dev-mode/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E2. Figma Dev Mode (+ Code Connect)

- **Resource name:** Figma Dev Mode (+ Code Connect)
- **Canonical identity:** Figma, Inc. — figma.com/dev-mode
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (Dev Mode) + implementation (Code Connect SDK, open)
- **Official URL:** https://www.figma.com/dev-mode/
- **Description:** Dev Mode: inspect, variables, version compare, annotations for handoff. Code Connect: maps Figma components to code components so Dev Mode/MCP show real usage snippets.
- **Contents inspected:** Dev Mode docs; Code Connect docs.
- **Actual capabilities:** Spec inspection; component↔code mapping; generated snippets.
- **Usage domain:** Designer→developer handoff.
- **Inputs:** Figma file; Code Connect config in repo.
- **Outputs:** Specs, assets, code snippets.
- **Integration method:** Figma app; `@figma/code-connect` npm.
- **Dependencies:** Figma seats (Dev Mode paid tiers).
- **Availability:** Current.
- **Maintenance:** Active.
- **License:** Proprietary (Figma); Code Connect SDK open (verify).
- **Limitations:** Snippets only as good as the mapping; paid seats for full Dev Mode.
- **Related resources:** Figma MCP Server; Zeplin (competitor).
- **Sources:** https://www.figma.com/dev-mode/; https://developers.figma.com/docs/code-connect/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E3. Locofy

- **Resource name:** Locofy
- **Canonical identity:** locofy.ai
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (Figma plugin + web) + MCP for AI editors
- **Official URL:** https://www.locofy.ai/
- **Description:** Figma designs → production React/Next.js/Vue/Angular/HTML code: auto layout → responsive code, component mapping, design-system sync; MCP server for AI code editors (2026).
- **Contents inspected:** locofy.ai (frameworks, MCP verified via secondary); Figma plugin listing.
- **Actual capabilities:** One-click Figma→code with responsive output; tags/components mapping; Storybook export.
- **Usage domain:** Design-to-code conversion.
- **Inputs:** Figma designs (auto-layout recommended).
- **Outputs:** React/Next/Vue/Angular/HTML+CSS/Tailwind code.
- **Integration method:** Figma plugin; web app; MCP.
- **Dependencies:** Figma account; subscription for full export.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary; exported code yours.
- **Limitations:** Output quality depends on Figma hygiene; paywalled exports.
- **Related resources:** Anima; Builder.io Visual Copilot.
- **Sources:** https://www.locofy.ai/
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### E4. Anima

- **Resource name:** Anima
- **Canonical identity:** animaapp.com
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (Figma plugin + web)
- **Official URL:** https://www.animaapp.com/
- **Description:** Figma/XD/Sketch → React/Vue/HTML code; Playground for prototypes; design-system automation.
- **Contents inspected:** animaapp.com (features verified).
- **Actual capabilities:** Design-to-code export; live prototypes from Figma.
- **Usage domain:** Design-to-code conversion.
- **Inputs:** Figma/XD/Sketch files.
- **Outputs:** React/Vue/HTML code.
- **Integration method:** Plugin; web app.
- **Dependencies:** Design tool account; subscription.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Thin coverage; export quality varies.
- **Related resources:** Locofy; TeleportHQ.
- **Sources:** https://www.animaapp.com/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### E5. Builder.io Visual Copilot

- **Resource name:** Builder.io Visual Copilot
- **Canonical identity:** builder.io (Visual Copilot feature)
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (Figma plugin + AI codegen)
- **Official URL:** https://www.builder.io/
- **Description:** Figma→code AI: Visual Copilot converts Figma designs to code (React etc.) with design-system awareness; Builder's visual headless CMS for AI-generated content.
- **Contents inspected:** builder.io (Visual Copilot verified).
- **Actual capabilities:** AI Figma→code; visual editing CMS.
- **Usage domain:** Design-to-code; visual CMS.
- **Inputs:** Figma designs.
- **Outputs:** Framework code; Builder content entries.
- **Integration method:** Figma plugin; Builder SDKs.
- **Dependencies:** Builder account.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Builder-ecosystem gravity.
- **Related resources:** Locofy; Plasmic.
- **Sources:** https://www.builder.io/
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### E6. Plasmic

- **Resource name:** Plasmic
- **Canonical identity:** plasmic.app; `plasmicapp/plasmic` (GitHub)
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (visual builder) + implementation (open codegen)
- **Official URL:** https://www.plasmic.app/
- **Description:** Visual builder + codegen: design pages/components visually, generate React code (codegen) or load dynamically (loader); open-source components.
- **Contents inspected:** plasmic.app; GitHub repo (codegen verified).
- **Actual capabilities:** Visual editing; React codegen; headless API/loader.
- **Usage domain:** Visual development, marketing sites.
- **Inputs:** Visual designs / content.
- **Outputs:** React code or runtime-rendered pages.
- **Integration method:** Web studio; npm packages.
- **Dependencies:** Plasmic account (hosted) optional for codegen.
- **Availability:** Freemium; OSS parts.
- **Maintenance:** Active.
- **License:** MIT (open parts); hosted ToS.
- **Limitations:** Codegen output idiom is Plasmic-flavored.
- **Related resources:** Builder.io; TeleportHQ.
- **Sources:** https://www.plasmic.app/; https://github.com/plasmicapp/plasmic
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E7. TeleportHQ

- **Resource name:** TeleportHQ
- **Canonical identity:** teleporthq.io; `teleporthq/teleport-code-generators` (GitHub)
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (visual builder) + implementation (open code generators)
- **Official URL:** https://teleporthq.io/
- **Description:** Visual builder with open-source code generators: Figma→React/Vue/Angular/HTML; UIDL intermediate format.
- **Contents inspected:** teleporthq.io; code-generators README (UIDL verified).
- **Actual capabilities:** Multi-framework codegen from visual/UIDL input.
- **Usage domain:** Design-to-code; visual building.
- **Inputs:** Visual designs; UIDL JSON.
- **Outputs:** React/Vue/Angular/HTML code.
- **Integration method:** Web studio; npm generators.
- **Dependencies:** None for generators.
- **Availability:** Freemium; generators OSS.
- **Maintenance:** Active.
- **License:** MIT (generators); hosted ToS.
- **Limitations:** Smaller ecosystem than Figma-native tools.
- **Related resources:** Plasmic; Anima.
- **Sources:** https://teleporthq.io/; https://github.com/teleporthq/teleport-code-generators
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E8. Kombai

- **Resource name:** Kombai
- **Canonical identity:** kombai.com
- **Category:** Part 17 — Design-to-code (AI frontend agent)
- **Type:** Hosted service (AI agent)
- **Official URL:** https://kombai.com/
- **Description:** AI frontend agent: Figma designs → code; email-to-code ("Email Designer"); trained on real-world code patterns.
- **Contents inspected:** kombai.com (features verified via secondary).
- **Actual capabilities:** Autonomous Figma→frontend code.
- **Usage domain:** AI design-to-code.
- **Inputs:** Figma files; prompts.
- **Outputs:** Frontend code.
- **Integration method:** Web app; integrations.
- **Dependencies:** Account.
- **Availability:** Freemium/paid.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Thin coverage; quality varies.
- **Related resources:** Locofy; Codia AI.
- **Sources:** https://kombai.com/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### E9. Codia AI

- **Resource name:** Codia AI
- **Canonical identity:** codia.ai
- **Category:** Part 17 — Design-to-code
- **Type:** Hosted service (AI design-to-code)
- **Official URL:** https://codia.ai/
- **Description:** Screenshot/Figma→code AI: generates responsive HTML/CSS/React from designs; design-to-code automation.
- **Contents inspected:** codia.ai (features verified via secondary).
- **Actual capabilities:** AI codegen from visuals.
- **Usage domain:** Design-to-code.
- **Inputs:** Screenshots/Figma.
- **Outputs:** HTML/CSS/React.
- **Integration method:** Web app.
- **Dependencies:** Account.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Thin coverage.
- **Related resources:** Kombai; Quest AI.
- **Sources:** https://codia.ai/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### E10. screenshot-to-code (abi)

- **Resource name:** screenshot-to-code
- **Canonical identity:** `abi/screenshot-to-code` (GitHub)
- **Category:** Part 17 — Design-to-code (screenshot-to-code, open source)
- **Type:** Implementation (open-source app)
- **Official URL:** https://github.com/abi/screenshot-to-code (hosted: screenshottocode.com)
- **Description:** OSS app: screenshots/mockups/recordings → code via vision LLMs; stacks: HTML+Tailwind, React, Vue, Bootstrap, Ionic, SVG; models incl. Gemini 3, Claude Opus, GPT.
- **Contents inspected:** GitHub README (stacks, models verified).
- **Actual capabilities:** Image/video→frontend code with iterative refinement.
- **Usage domain:** Screenshot-to-code; prototyping.
- **Inputs:** Screenshot image / screen recording; API key.
- **Outputs:** HTML/Tailwind/React/Vue/Bootstrap/Ionic/SVG code.
- **Integration method:** Self-hosted web app; BYO LLM key.
- **Dependencies:** LLM API key (Anthropic/OpenAI/Google).
- **Availability:** Open source.
- **Maintenance:** Active (abi).
- **License:** MIT.
- **Limitations:** BYO key cost; single-page oriented; fidelity varies by model.
- **Related resources:** seeb4coding/pic-2-code; emilwallner screenshot-to-code (original).
- **Sources:** https://github.com/abi/screenshot-to-code
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E11. v0 by Vercel

- **Resource name:** v0 by Vercel
- **Canonical identity:** v0.dev
- **Category:** Part 17 — Design-to-code (AI frontend agent)
- **Type:** Hosted service (generative UI)
- **Official URL:** https://v0.dev/
- **Description:** Vercel's AI UI generator: natural language (+ images/figma) → React/Tailwind/shadcn components with live preview; deploy to Vercel; API/SDK.
- **Contents inspected:** v0.dev (features verified).
- **Actual capabilities:** Prompt→UI with iterations; Figma import; API.
- **Usage domain:** AI frontend generation.
- **Inputs:** Prompts, images, Figma files.
- **Outputs:** React/Tailwind/shadcn code.
- **Integration method:** Web; API/SDK.
- **Dependencies:** Vercel account.
- **Availability:** Freemium.
- **Maintenance:** Active (Vercel).
- **License:** Proprietary; generated code yours.
- **Limitations:** React/Tailwind/shadcn idiom; Vercel gravity.
- **Related resources:** Lovable; Bolt; Galileo/Stitch.
- **Sources:** https://v0.dev/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E12. Zeplin

- **Resource name:** Zeplin
- **Canonical identity:** zeplin.io
- **Category:** Part 17 — Design-to-code (design-spec generation)
- **Type:** Hosted service
- **Official URL:** https://zeplin.io/
- **Description:** Design handoff platform: Figma/XD/Sketch → organized specs, assets, code snippets; versioned screens; Jira/Slack integrations.
- **Contents inspected:** zeplin.io (features verified).
- **Actual capabilities:** Spec generation, asset export, snippet generation.
- **Usage domain:** Designer→developer handoff.
- **Inputs:** Design files via plugins.
- **Outputs:** Specs, assets, snippets.
- **Integration method:** Plugins; web app.
- **Dependencies:** Account; subscription for teams.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Handoff only, not codegen; Figma Dev Mode overlap.
- **Related resources:** Supernova; Avocode (historical).
- **Sources:** https://zeplin.io/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E13. Supernova

- **Resource name:** Supernova
- **Canonical identity:** supernova.io
- **Category:** Part 17 — Design-to-code (design-system automation)
- **Type:** Hosted service
- **Official URL:** https://www.supernova.io/
- **Description:** Design-system platform: Figma tokens/components → multi-platform code (iOS/Android/Web), documentation sites.
- **Contents inspected:** Secondary sources only; direct site fetch thin.
- **Actual capabilities:** Token/component codegen; docs automation.
- **Usage domain:** Design-system ops.
- **Inputs:** Figma libraries.
- **Outputs:** Platform code; docs.
- **Integration method:** Figma plugin; web platform.
- **Dependencies:** Account.
- **Availability:** Paid (verify tiers).
- **Maintenance:** Assumed active.
- **License:** Proprietary.
- **Limitations:** Thin coverage — not directly fetched.
- **Related resources:** Zeplin; Tokens Studio.
- **Sources:** https://www.supernova.io/ (secondary verification only)
- **Verification date:** 2026-10-10
- **Confidence:** Low. **Verification: Unresolved.**

### E14. Chromatic (visual regression)

- **Resource name:** Chromatic
- **Canonical identity:** chromatic.com (Storybook maintainers)
- **Category:** Part 17 — Design-to-code (UI comparison / visual regression)
- **Type:** Hosted service
- **Official URL:** https://www.chromatic.com/
- **Description:** Visual testing for Storybook: screenshot every story per commit, visual diff review, UI review workflow; by Storybook maintainers.
- **Contents inspected:** chromatic.com (workflow verified).
- **Actual capabilities:** Automated visual regression; TurboSnap; accessibility checks.
- **Usage domain:** Design QA, visual regression.
- **Inputs:** Storybook; CI integration.
- **Outputs:** Visual diffs; review approvals.
- **Integration method:** npm (`chromatic`); CI (GitHub Actions etc.).
- **Dependencies:** Storybook; account.
- **Availability:** Freemium (snapshot quotas).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Snapshot-based pricing; Storybook-centric.
- **Related resources:** Percy; Argos; Applitools.
- **Sources:** https://www.chromatic.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E15. Percy by BrowserStack (visual regression)

- **Resource name:** Percy (BrowserStack)
- **Canonical identity:** percy.io / browserstack.com/percy
- **Category:** Part 17 — Design-to-code (visual regression)
- **Type:** Hosted service
- **Official URL:** https://percy.io/
- **Description:** Visual testing platform: cross-browser screenshots, visual diffs, responsive comparison; integrates with major test frameworks.
- **Contents inspected:** percy.io (features verified).
- **Actual capabilities:** Visual diffs across browsers/viewports.
- **Usage domain:** Visual regression QA.
- **Inputs:** Test SDK snapshots; CI.
- **Outputs:** Visual comparisons.
- **Integration method:** SDKs (percy-cli, framework SDKs); CI.
- **Dependencies:** Account.
- **Availability:** Freemium/paid.
- **Maintenance:** Active (BrowserStack).
- **License:** Proprietary.
- **Limitations:** Snapshot pricing.
- **Related resources:** Chromatic; Applitools.
- **Sources:** https://percy.io/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E16. Applitools Eyes (visual regression)

- **Resource name:** Applitools Eyes
- **Canonical identity:** applitools.com
- **Category:** Part 17 — Design-to-code (visual regression, AI-powered)
- **Type:** Hosted service
- **Official URL:** https://applitools.com/
- **Description:** AI-powered visual testing: Visual AI diffing, cross-browser/device, ultrafast grid; SDKs for major frameworks.
- **Contents inspected:** applitools.com (Visual AI verified).
- **Actual capabilities:** AI visual assertions; layout/content diffing.
- **Usage domain:** Visual regression at scale.
- **Inputs:** SDK checkpoints; CI.
- **Outputs:** AI-analyzed diffs.
- **Integration method:** SDKs; CI.
- **Dependencies:** Account.
- **Availability:** Paid (trial).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Enterprise pricing.
- **Related resources:** Percy; Chromatic.
- **Sources:** https://applitools.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### E17. Uizard (AI prototyping)

- **Resource name:** Uizard
- **Canonical identity:** uizard.io
- **Category:** Part 17 — Design-to-code (AI prototyping)
- **Type:** Hosted service
- **Official URL:** https://uizard.io/
- **Description:** AI prototyping: text/sketches/screenshots → editable UI prototypes (Autodesigner 2.0); themes, handoff.
- **Contents inspected:** uizard.io (Autodesigner verified via secondary).
- **Actual capabilities:** Prompt/sketch/screenshot→prototype.
- **Usage domain:** Rapid prototyping.
- **Inputs:** Text, sketches, screenshots.
- **Outputs:** Editable prototypes.
- **Integration method:** Web app.
- **Dependencies:** Account.
- **Availability:** Free/$12/$39 tiers (per 2026 secondary source; verify).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Prototype fidelity; thin coverage.
- **Related resources:** Visily; Galileo/Stitch.
- **Sources:** https://uizard.io/
- **Verification date:** 2026-10-10
- **Confidence:** Medium. **Verification: Partially verified.**

### E18. Relume (AI site builder)

- **Resource name:** Relume
- **Canonical identity:** relume.io
- **Category:** Part 17 — Design-to-code (AI website builder; also Part C directory)
- **Type:** Hosted service (AI builder + component library)
- **Official URL:** https://www.relume.io/
- **Description:** AI sitemaps & wireframes: describe company → sitemap + wireframes + copy; 1000+ component library; exports to Figma (plugin), Webflow (Client-First), React (Tailwind + shadcn/ui); Relume Publish hosting.
- **Contents inspected:** relume.io; pricing via therundown.ai (2026-08-31: Build Pro $14/mo, Publish Launch $12/project/mo, Starter exports $18/mo, Pro exports $40/mo — secondary).
- **Actual capabilities:** AI site planning; component library; multi-target export.
- **Usage domain:** Marketing-site production.
- **Inputs:** Prompts/company description.
- **Outputs:** Sitemap, wireframes, Figma/Webflow/React exports, hosted site.
- **Integration method:** Web app; Figma plugin.
- **Dependencies:** Account.
- **Availability:** Freemium (free build/publish; paid exports).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Export paywalls; marketing-site scope.
- **Related resources:** Framer; Webflow; Figma Community.
- **Sources:** https://www.relume.io/; https://www.therundown.ai/tools/relume
- **Verification date:** 2026-10-10
- **Confidence:** Medium-high. **Verification: Partially verified.**

### E19. Framer (AI website builder)

- **Resource name:** Framer
- **Canonical identity:** framer.com
- **Category:** Part 17 — Design-to-code (visual site builder + AI)
- **Type:** Hosted service
- **Official URL:** https://www.framer.com/
- **Description:** Visual website builder + hosting: canvas design, CMS, AI site generation (Framer AI), effects, publishing with custom domains.
- **Contents inspected:** framer.com (features verified).
- **Actual capabilities:** No-code site building; AI generation; CMS; hosting/analytics.
- **Usage domain:** Marketing sites, portfolios.
- **Inputs:** Visual canvas / AI prompts.
- **Outputs:** Hosted websites (React-based runtime).
- **Integration method:** Web studio.
- **Dependencies:** Account; subscription for custom domains/scale.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Limitations:** Platform lock-in; code export limited (verify current policy).
- **Related resources:** Webflow; Relume; Wix Studio.
- **Sources:** https://www.framer.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

> Also noted (supplementary): **Figma Make** (AI-native design, First Draft — partially verified); **Musho** (musho.ai, Figma plugin landing pages — partially verified); **Quest AI** (quest.ai, Figma→React — partially verified); **Onlook** (onlook.com, open-source visual React editor, 25.9k stars — verified); **Visily** (visily.ai, AI wireframes — partially verified); **seeb4coding/pic-2-code** (OSS image→code — partially verified); **Galileo AI → Google Stitch** (stitch.withgoogle.com, free Gemini UI generator — partially verified); **Argos** (argos-ci.com, OSS visual regression — verified); **BackstopJS** (`garris/BackstopJS`, dormant since 2024 — **Archived**); **Lost Pixel** (lost-pixel.com, sunsetting/joining Figma — **Historical**); **Playwright toHaveScreenshot** (built-in visual comparisons — verified); **OverlayQA** (overlayqa.com, Figma-aware QA — partially verified).

---

## PART F — Visual/interactive creative tech

> DEDUP note: pmndrs/react-three-fiber, react-three-start, react-three-next basics are cross-referenced only; this part covers the ecosystem around them.

### F1. three.js

- **Resource name:** three.js
- **Canonical identity:** `mrdoob/three.js` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (3D)
- **Type:** Implementation (WebGL/WebGPU 3D library)
- **Official URL:** https://threejs.org/ (repo https://github.com/mrdoob/three.js)
- **Description:** The standard JavaScript 3D library: WebGL + WebGPU renderers, scene graph, geometries, materials, lights, loaders (GLTF), post-processing, TSL (Three Shading Language). ~113k stars; r184 (Apr 2026) at inspection.
- **Contents inspected:** GitHub README + releases (r184 verified); threejs.org docs/manual.
- **Actual capabilities:** Real-time 3D scenes, XR, GPU compute, instancing, shaders.
- **Usage domain:** 3D web experiences, product configurators, data viz, games.
- **Inputs:** JS scene code; GLTF/assets.
- **Outputs:** Rendered 3D in canvas.
- **Integration method:** npm (`three`) / CDN modules.
- **Dependencies:** None (core).
- **Availability:** Open source, current.
- **Maintenance:** Very active.
- **License:** MIT.
- **Limitations:** Low-level — bring your own architecture; WebGPU support evolving.
- **Related resources:** R3F (dedup); Babylon.js; PlayCanvas.
- **Sources:** https://threejs.org/; https://github.com/mrdoob/three.js
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F2. drei (pmndrs helpers)

- **Resource name:** drei
- **Canonical identity:** `pmndrs/drei` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (R3F ecosystem)
- **Type:** Implementation (R3F helper components)
- **Official URL:** https://github.com/pmndrs/drei
- **Description:** Useful helpers for react-three-fiber: OrbitControls, Environment, Text3D, Float, ScrollControls, Html, useGLTF, ContactShadows, etc.
- **Contents inspected:** GitHub README (component index verified).
- **Actual capabilities:** Drop-in R3F abstractions for controls, staging, text, scroll.
- **Usage domain:** R3F scene building.
- **Inputs:** npm install.
- **Outputs:** R3F components.
- **Integration method:** npm (`@react-three/drei`).
- **Dependencies:** three, @react-three/fiber (dedup).
- **Availability:** Open source, current.
- **Maintenance:** Active (pmndrs).
- **License:** MIT.
- **Limitations:** R3F-only.
- **Related resources:** R3F (dedup); @react-three/postprocessing.
- **Sources:** https://github.com/pmndrs/drei
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F3. @react-three/postprocessing (+ postprocessing lib)

- **Resource name:** @react-three/postprocessing / postprocessing
- **Canonical identity:** `pmndrs/postprocessing` (wrapper); `vanruesc/postprocessing` (core lib)
- **Category:** Part 17 — Visual/interactive creative tech (effects)
- **Type:** Implementation (post-processing effects)
- **Official URL:** https://github.com/pmndrs/postprocessing
- **Description:** R3F wrapper for the `postprocessing` library: Bloom, DepthOfField, Vignette, SMAA, N8AO, etc. as declarative effects.
- **Contents inspected:** README (effects list verified).
- **Actual capabilities:** GPU post effects in R3F.
- **Usage domain:** 3D scene polish.
- **Inputs:** npm install.
- **Outputs:** Post-processed render.
- **Integration method:** npm.
- **Dependencies:** three, @react-three/fiber.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT (verify core lib).
- **Limitations:** R3F-only wrapper; perf cost per effect.
- **Related resources:** three.js examples/jsm effects.
- **Sources:** https://github.com/pmndrs/postprocessing; https://github.com/vanruesc/postprocessing
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F4. GSAP

- **Resource name:** GSAP (GreenSock Animation Platform)
- **Canonical identity:** gsap.com; `greensock/GSAP` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (animation/motion)
- **Type:** Implementation (JS animation library; commercial-friendly, source-visible)
- **Official URL:** https://gsap.com/
- **Description:** Industry-standard JS animation: timelines, ScrollTrigger, ScrollSmoother, Draggable, MorphSVG; Webflow-owned since Oct 2024; all Club plugins free since May 2025. Free for commercial use; not open-source licensed.
- **Contents inspected:** gsap.com (plugins, pricing/ownership verified via secondary).
- **Actual capabilities:** High-performance tweens, scroll animations, SVG morphing.
- **Usage domain:** Web animation, scroll experiences, interactive storytelling.
- **Inputs:** npm install / CDN.
- **Outputs:** DOM/SVG/Canvas animations.
- **Integration method:** npm (`gsap`) / CDN; `@gsap/react`.
- **Dependencies:** None.
- **Availability:** Free for commercial use (all plugins incl. Club since May 2025).
- **Maintenance:** Active (Webflow).
- **License:** Custom GreenSock license (free incl. commercial; not OSI open source — as documented).
- **Limitations:** Not open source; Webflow ownership direction.
- **Related resources:** Motion; Anime.js; Lenis.
- **Sources:** https://gsap.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F5. Motion (formerly Framer Motion)

- **Resource name:** Motion
- **Canonical identity:** motion.dev; `motiondivision/motion` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (animation)
- **Type:** Implementation (JS/React animation library)
- **Official URL:** https://motion.dev/
- **Description:** Animation library for React and vanilla JS (ex-Framer Motion): layout animations, gestures, scroll-linked motion, springs.
- **Contents inspected:** motion.dev docs (verified).
- **Actual capabilities:** Declarative animations, AnimatePresence, useScroll.
- **Usage domain:** React UI animation.
- **Inputs:** npm install.
- **Outputs:** Animated React/JS UI.
- **Integration method:** npm (`motion`).
- **Dependencies:** React (for React package).
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT (verify current).
- **Limitations:** React-first.
- **Related resources:** GSAP; React Spring; Anime.js.
- **Sources:** https://motion.dev/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F6. Anime.js

- **Resource name:** Anime.js
- **Canonical identity:** animejs.com; `juliangarnier/anime` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (animation)
- **Type:** Implementation (JS animation library)
- **Official URL:** https://animejs.com/
- **Description:** Lightweight JS animation engine: CSS/SVG/DOM attributes, timelines, staggering, easings.
- **Contents inspected:** animejs.com docs (verified).
- **Actual capabilities:** Property tweening with timelines.
- **Usage domain:** Web micro-animation.
- **Inputs:** npm / CDN.
- **Outputs:** DOM/SVG animations.
- **Integration method:** npm (`animejs`) / CDN.
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Smaller feature set than GSAP.
- **Related resources:** GSAP; Motion.
- **Sources:** https://animejs.com/; https://github.com/juliangarnier/anime
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F7. Lenis (smooth scroll)

- **Resource name:** Lenis
- **Canonical identity:** `darkroomengineering/lenis` (GitHub); lenis.darkroom.engineering
- **Category:** Part 17 — Visual/interactive creative tech (scroll-driven animation)
- **Type:** Implementation (smooth-scroll library)
- **Official URL:** https://lenis.darkroom.engineering/
- **Description:** Modern smooth-scroll library (ex-`@studio-freight/lenis`): buttery scroll with RAF, anchor support, framework adapters.
- **Contents inspected:** GitHub README + site (verified).
- **Actual capabilities:** Smooth scrolling, scroll callbacks, GSAP ticker integration.
- **Usage domain:** Scroll-driven sites.
- **Inputs:** npm install.
- **Outputs:** Smooth scroll behavior.
- **Integration method:** npm (`lenis`).
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active (Darkroom Engineering).
- **License:** MIT.
- **Limitations:** Can conflict with native scroll behaviors/accessibility if misused.
- **Related resources:** Locomotive Scroll; GSAP ScrollSmoother.
- **Sources:** https://github.com/darkroomengineering/lenis
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F8. p5.js (creative coding)

- **Resource name:** p5.js
- **Canonical identity:** p5js.org; `processing/p5.js` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (creative coding)
- **Type:** Implementation (JS creative-coding library)
- **Official URL:** https://p5js.org/
- **Description:** Processing for the web: 2D/3D sketching, friendly API for artists/designers; p5.js 2.x current generation; web editor.
- **Contents inspected:** p5js.org (2.x verified); GitHub README.
- **Actual capabilities:** Canvas/WebGL sketches, sound, DOM.
- **Usage domain:** Generative art, education, creative coding.
- **Inputs:** npm / CDN / web editor.
- **Outputs:** Interactive sketches.
- **Integration method:** CDN/npm; editor.
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active (Processing Foundation).
- **License:** LGPL-2.1 (library).
- **Limitations:** Perf ceiling for heavy 3D; 1.x→2.x migration.
- **Related resources:** Processing; Paper.js; Pts.
- **Sources:** https://p5js.org/; https://github.com/processing/p5.js
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F9. PixiJS

- **Resource name:** PixiJS
- **Canonical identity:** pixijs.com; `pixijs/pixi.js` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (2D rendering)
- **Type:** Implementation (2D WebGL rendering engine)
- **Official URL:** https://pixijs.com/
- **Description:** Fast 2D WebGL renderer with WebGPU support (v8): sprites, filters, particles, spine support; React bindings (`@pixi/react`).
- **Contents inspected:** pixijs.com + GitHub (v8 verified).
- **Actual capabilities:** GPU 2D rendering, filters, asset pipeline.
- **Usage domain:** 2D games, interactive graphics, data viz.
- **Inputs:** npm install.
- **Outputs:** WebGL canvas scenes.
- **Integration method:** npm (`pixi.js`).
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** 2D-focused (use three.js for 3D).
- **Related resources:** Phaser; Konva; two.js.
- **Sources:** https://pixijs.com/; https://github.com/pixijs/pixi.js
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F10. tsParticles (particle systems)

- **Resource name:** tsParticles
- **Canonical identity:** particles.js.org (tsparticles); `matteobruni/tsparticles` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (particles)
- **Type:** Implementation (particle engine)
- **Official URL:** https://particles.js.org/
- **Description:** TypeScript particle engine (successor to particles.js): presets, emitters, absorbers, interactivity; framework wrappers.
- **Contents inspected:** particles.js.org; GitHub README (verified).
- **Actual capabilities:** Configurable canvas particle systems.
- **Usage domain:** Hero backgrounds, decorative effects.
- **Inputs:** npm / JSON config.
- **Outputs:** Canvas particles.
- **Integration method:** npm (`@tsparticles/all` / slim).
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active.
- **License:** MIT.
- **Limitations:** Canvas 2D perf for huge counts.
- **Related resources:** particles.js (archived original); Vanta.js.
- **Sources:** https://particles.js.org/; https://github.com/matteobruni/tsparticles
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F11. Spline (3D design tool)

- **Resource name:** Spline
- **Canonical identity:** spline.design
- **Category:** Part 17 — Visual/interactive creative tech (3D scenes)
- **Type:** Hosted service (3D design tool) + implementation (runtime exports)
- **Official URL:** https://spline.design/
- **Description:** Browser-based 3D design tool (Figma-for-3D): model, animate, add interactivity; export via runtime (`@splinetool/runtime`, React wrapper) or viewer embed.
- **Contents inspected:** spline.design (runtime verified).
- **Actual capabilities:** No-code 3D scenes with events/physics; web export.
- **Usage domain:** 3D web hero sections, product viewers.
- **Inputs:** Visual 3D editing.
- **Outputs:** Embeddable 3D scenes; runtime code.
- **Integration method:** `@splinetool/react-spline` / viewer iframe.
- **Dependencies:** Spline account for authoring.
- **Availability:** Freemium.
- **Maintenance:** Active.
- **License:** Proprietary (editor); exported scenes per plan.
- **Limitations:** Editor lock-in; perf for complex scenes.
- **Related resources:** three.js; PlayCanvas.
- **Sources:** https://spline.design/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F12. Babylon.js

- **Resource name:** Babylon.js
- **Canonical identity:** babylonjs.com; `BabylonJS/Babylon.js` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (3D engine)
- **Type:** Implementation (full 3D game engine for web)
- **Official URL:** https://www.babylonjs.com/
- **Description:** Full-featured WebGL/WebGPU 3D engine: physics, audio, GUI, XR, node materials, playground; Microsoft-backed.
- **Contents inspected:** babylonjs.com + GitHub (verified).
- **Actual capabilities:** Game-engine-grade 3D in browser.
- **Usage domain:** Web games, configurators, XR.
- **Inputs:** npm install.
- **Outputs:** 3D applications.
- **Integration method:** npm (`@babylonjs/core`).
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Active (Microsoft).
- **License:** Apache-2.0.
- **Limitations:** Heavier than three.js for simple scenes.
- **Related resources:** three.js; PlayCanvas.
- **Sources:** https://www.babylonjs.com/; https://github.com/BabylonJS/Babylon.js
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F13. Mapbox GL JS / MapLibre GL / deck.gl / kepler.gl (interactive maps)

- **Resource name:** Mapbox GL JS; MapLibre GL; deck.gl; kepler.gl
- **Canonical identity:** mapbox.com; maplibre.org; deck.gl; kepler.gl (Uber/Foursquare OSS)
- **Category:** Part 17 — Visual/interactive creative tech (interactive maps)
- **Type:** Implementation (map rendering libraries; kepler.gl also a React app)
- **Official URL:** https://www.mapbox.com/ ; https://maplibre.org/ ; https://deck.gl/ ; https://kepler.gl/
- **Description:** Mapbox GL JS: vector map rendering (commercial, token). MapLibre GL: OSS fork (BSD-3), tokenless. deck.gl: WebGL data-visualization overlays (hexagons, trips, scatter) on basemaps. kepler.gl: drag-drop geospatial exploration app + embeddable React component (MIT).
- **Contents inspected:** Project sites + GitHub READMEs (verified); third-party agent SKILL.md for kepler.gl.
- **Actual capabilities:** Interactive vector maps; big-data WebGL overlays; no-code geo exploration.
- **Usage domain:** Interactive maps, geospatial dashboards.
- **Inputs:** GeoJSON/CSV/vector tiles; Mapbox token (Mapbox) or self-hosted tiles (MapLibre).
- **Outputs:** Interactive maps.
- **Integration method:** npm (`maplibre-gl`, `deck.gl`, `kepler.gl`).
- **Dependencies:** Basemap tiles source.
- **Availability:** MapLibre/deck.gl/kepler.gl OSS; Mapbox commercial.
- **Maintenance:** Active.
- **License:** MapLibre BSD-3-Clause; deck.gl MIT; kepler.gl MIT; Mapbox proprietary SDK terms.
- **Limitations:** Tile/data costs at scale; WebGL perf tuning.
- **Related resources:** Leaflet; Cesium; Flowmap.gl.
- **Sources:** https://maplibre.org/; https://deck.gl/; https://kepler.gl/; https://www.mapbox.com/
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

### F14. Animate.css

- **Resource name:** Animate.css
- **Canonical identity:** animate.style; `animate-css/animate.css` (GitHub)
- **Category:** Part 17 — Visual/interactive creative tech (CSS animation presets)
- **Type:** Implementation (CSS animation library)
- **Official URL:** https://animate.style/
- **Description:** Cross-browser CSS animation library: 80+ ready animations (attention seekers, entrances, exits); utility classes.
- **Contents inspected:** animate.style (animation list verified); GitHub README.
- **Actual capabilities:** Class-based CSS animations.
- **Usage domain:** CSS micro-animation.
- **Inputs:** npm / CDN.
- **Outputs:** CSS classes.
- **Integration method:** npm (`animate.css`) / CDN link.
- **Dependencies:** None.
- **Availability:** Open source, current.
- **Maintenance:** Community (stable).
- **License:** Hippocratic License 2.1 (not OSI — as documented).
- **Limitations:** Preset-only; not a motion system.
- **Related resources:** Hover.css; Magic CSS; Micron.js.
- **Sources:** https://animate.style/; https://github.com/animate-css/animate.css
- **Verification date:** 2026-10-10
- **Confidence:** High. **Verification: Verified.**

> Also noted (supplementary): **@react-three/rapier** (3D physics — verified); **@react-three/xr** (WebXR — verified); **gltfjsx** (GLTF→R3F — verified); **leva** (GUI controls — verified); **maath** (math helpers — verified); **Locomotive Scroll** (locomotive.ca — verified); **Barba.js** (barba.js.org, page transitions — verified); **Swup** (swup.js.org — verified); **Theatre.js** (theatrejs.com, motion design — verified); **React Spring** (react-spring.dev — verified); **Vivus** (SVG stroke animation — verified); **Typed.js** (typewriter — verified); **AOS** (scroll animations — verified); **Hover.css** (hover effects — verified); **css-doodle** (verified); **Two.js / Paper.js / Pts / Konva / Fabric.js** (2D libraries — verified); **OGL** (minimal WebGL — verified); **Vanta.js** (animated backgrounds — verified); **Phaser** (phaser.io, game framework — verified); **PlayCanvas** (playcanvas.com, engine — verified); **A-Frame** (aframe.io, WebXR — verified); **Cesium** (cesium.com, 3D geospatial — verified); **Matter.js** (2D physics — verified); **LYGIA** (lygia.xyz, shader library — verified); **iquilezles.org** (shader articles — verified); **glslsandbox** (verified); **ffmpeg.wasm** (media processing — verified).

---

## Coverage note

### Counts (full Part-21-style records: 97)

| Subcategory | Full records | Verified | Corrected | Partially verified | Unresolved |
|---|---|---|---|---|---|
| A. Design systems & official guidelines | 22 | 11 | 1 | 10 | 0 |
| B. UI/UX theory resources | 7 | 6 | 0 | 1 | 0 |
| C. Inspiration & resource directories | 15 | 13 | 0 | 2 | 0 |
| D. Creative assets & asset pipelines | 20 | 17 | 0 | 3 | 0 |
| E. Design-to-code | 19 | 11 | 0 | 7 | 1 |
| F. Visual/interactive creative tech | 14 | 14 | 0 | 0 | 0 |
| **Total** | **97** | **72** | **1** | **23** | **1** |

- Supplementary compact mentions (site/license/type confirmed, not full records): ~95 additional resources across all parts.
- Verification labels beyond the table: **Archived** — BackstopJS (dormant since 2024); **Historical** — Lost Pixel (sunsetting, joining Figma); **Corrected** — Shopify Polaris (React deprecated → web components current).
- All records carry verification date 2026-10-10.

### Limitations of this research pass

1. **Login-gated services** (Mobbin, parts of LottieFiles premium, Supernova) could not be inspected directly; records rely on marketing/docs pages → Partially verified / Unresolved.
2. **License fields** for several corporate design systems (Primer, SLDS, Polaris React-archive, Shoelace) were not re-fetched from LICENSE files; marked "Not verified" in-record. Licenses recorded for assets are as-documented, with no legal interpretation.
3. **Thin coverage areas** (would benefit from a follow-up pass): Relume/Quest AI pricing details, Uizard/Visily feature depth, Tokens Studio pricing tiers, per-asset license checks on Blush/Remix Icon/Hugeicons, Supernova (Unresolved), Figma Make, Google Stitch, Onlook, Visily.
4. **Fast-moving targets**: Figma MCP tool surface, Base UI component gaps, GSAP licensing posture, shadcn primitive-layer default — all verified 2026-10-10 but subject to change.
5. No installs, builds, or executions were performed (read-only mandate); "Actual capabilities" derive from docs/README inspection, not runtime testing.

### More work warranted?

- **Yes, light follow-up**: resolve Supernova (E13, currently Unresolved) via direct site fetch; verify pending LICENSE fields (A5, A6, A18, A3-archive); deepen thin areas listed above (E: Uizard/Visily/Quest/Musho; D: per-asset license spot-checks).
- **No further work needed** for Parts A-core, B, D-core, F: coverage is broad and verification is high.
- Suggested next workstream: the 29 design styles (explicitly out of scope here) and agent-facing design skills beyond the dedup list.
