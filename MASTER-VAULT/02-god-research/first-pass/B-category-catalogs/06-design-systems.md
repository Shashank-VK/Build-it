# 06 — Design Systems (open-source / corporate systems, guidelines, tokens, Figma, CLI, agent integrations, validators)

> Method: read-only WebSearch + WebFetch (no install/execute). Verified 2026-10-09 (UTC).
> Record spec (atlas standard, same in 06/07/08/21):
> `Name | URL | Type | Description | License (as stated in docs/repo) | Restrictions/Notes (docs-verbatim scope, no interpretation) | Agent/CLI integration`
> License field records only what docs state; "Unverified in this pass" means check repo LICENSE before reuse.

## A. Verified spotlight — Astryx (facebook/astryx)

### 01. Astryx — facebook/astryx
- URL: https://github.com/facebook/astryx
- Type: Open-source React design system + CLI + themes + templates
- Description: Meta-grown system (150+ accessible components, brand theming, dark mode, templates). Built on React 19+ and StyleX. Packages: `@astryxdesign/core`, `@astryxdesign/cli`, `@astryxdesign/build`, `@astryxdesign/theme-*`.
- License: MIT (root README badge + `## License — MIT`).
- Restrictions/Notes: Requires React 19+ (peer deps `react`, `react-dom`); `@astryxdesign/lab` internal/not on npm; `@astryxdesign/vega` / `@astryxdesign/charts` only under `@canary` dist-tag, no stable release (per README).
- Agent/CLI integration: **CLI-only — no MCP per direct README fetch (2026-10-09).** CLI is stated as "primary interface for humans and machines alike" via terminal, typed JSON API (`--json` envelopes, `astryx manifest --json`), and programmatic imports (`@astryxdesign/cli/api`). Commands: `search, component, hook, docs, template, theme, build, swizzle, upgrade, discover, doctor, gap-report, init, integration, blog, layout [deprecated]`. Neither root README nor `packages/cli/README.md` fetched mentions an MCP server. Agents use CLI + `manifest --json` + `--dense/--detail` flags, not MCP.

## B. Corporate / open-source systems & guidelines

### 02. MUI — Material UI (mui/material-ui)
- URL: https://github.com/mui/material-ui
- Type: Corporate/open component system + guidelines (Material)
- Description: React component library implementing Material Design; docs, theming, Figma kit.
- License: MIT (as stated in repo).
- Restrictions/Notes: Trademark "Material" / Google fonts/icons carry separate licenses; check Figma kit terms before redistributing.
- Agent/CLI integration: CLI via `npx @mui/codemod`; no first-party MCP; agent use via docs/code.

### 03. Ant Design (ant-design/ant-design)
- URL: https://github.com/ant-design/ant-design
- Type: Enterprise design system (Alibaba)
- Description: React enterprise dashboards/SaaS system; tokens, Figma files, Pro templates.
- License: MIT (as stated in repo).
- Restrictions/Notes: Pro templates/examples may carry separate commercial terms; verify per template.
- Agent/CLI integration: Codemods / CLI tools in repo; no first-party MCP.

### 04. IBM Carbon (carbon-design-system/carbon)
- URL: https://github.com/carbon-design-system/carbon
- Type: Corporate open-source system (IBM Design Language)
- Description: Monorepo: React + Web Components, Sass, tokens, icons, pictograms, tooling. Figma kit in `carbon-design-kit`.
- License: Apache-2.0 (as stated in repo + LICENSE).
- Restrictions/Notes: IBM Plex typeface separate OFL-ish terms; Sketch kit unmaintained, Figma is maintained (per kit README).
- Agent/CLI integration: No first-party MCP; automation via packages + tokens.

### 05. GitHub Primer — primer/react + primer/primitives
- URL: https://github.com/primer/react / https://github.com/primer/primitives
- Type: Corporate design system + token primitives
- Description: React implementation + color/spacing/typography primitives (Style Dictionary based).
- License: MIT (both repos, as stated).
- Restrictions/Notes: Octicons/brand assets have separate terms; primitives distributed on npm as `@primer/primitives`.
- Agent/CLI integration: No first-party MCP; tokens consumable via Style Dictionary.

### 06. Salesforce Lightning Design System (SLDS)
- URL: https://github.com/salesforce-ux/design-system
- Type: Corporate CSS/HTML + tokens system
- Description: CRM/SaaS blueprints, tokens (Theo lineage), Figma kits.
- License: As stated in repo (BSD-3-Clause family — verify LICENSE in this pass marked unverified, check before reuse).
- Restrictions/Notes: Salesforce trademarks excluded; see repo trademark notice.
- Agent/CLI integration: No first-party MCP; Theo/Style Dictionary pipeline.

### 07. Microsoft Fluent UI (microsoft/fluentui)
- URL: https://github.com/microsoft/fluentui
- Type: Corporate cross-platform system
- Description: React components (`@fluentui/react-components`), tokens, Figma toolkits.
- License: MIT (as stated in repo).
- Restrictions/Notes: Fluent brand assets excluded from code license; Figma kits under separate Community terms.
- Agent/CLI integration: No first-party MCP; codemods in repo.

### 08. Adobe Spectrum — React Spectrum / Spectrum CSS
- URL: https://github.com/adobe/react-spectrum
- Type: Corporate system for pro tools
- Description: Accessible React collections + Spectrum tokens + Figma libraries.
- License: Apache-2.0 (as stated in repo).
- Restrictions/Notes: Adobe trademarks excluded; check Spectrum Figma license.
- Agent/CLI integration: No first-party MCP.

### 09. Shopify Polaris (Shopify/polaris)
- URL: https://github.com/Shopify/polaris
- Type: Corporate e-commerce admin system
- Description: React components, tokens, Figma kit, guidelines.
- License: MIT — Unverified in this pass, check repo LICENSE before reuse.
- Restrictions/Notes: Shopify brand assets excluded.
- Agent/CLI integration: CLI (`@shopify/polaris-migrator` codemods); no first-party MCP.

### 10. Atlassian Design System — AtlasKit
- URL: https://bitbucket.org/atlassian/atlas-kit (mirror docs at atlassian.design)
- Type: Corporate collaboration-tool system
- Description: `@atlaskit/*` React packages, tokens, Figma libraries.
- License: Apache-2.0 (as stated in docs) — verify per-package LICENSE.
- Restrictions/Notes: Atlassian trademarks excluded.
- Agent/CLI integration: No first-party MCP.

## C. Tokens — build, sync, Figma

### 11. Style Dictionary (style-dictionary/style-dictionary)
- URL: https://github.com/style-dictionary/style-dictionary
- Type: Token build CLI + Node lib (DTCG forward-compatible)
- Description: Single source JSON/JS tokens → iOS, Android, CSS, JS, docs. CLI + config.
- License: Apache-2.0 (as stated).
- Restrictions/Notes: None stated beyond Apache-2.0; DTCG spec compatibility noted on site.
- Agent/CLI integration: CLI (`style-dictionary build`); consumed by Tokens Studio sd-transforms; agent-friendly JSON.

### 12. Tokens Studio for Figma (+ @tokens-studio/sd-transforms)
- URL: https://tokens.studio / https://github.com/tokens-studio/sd-transforms
- Type: Figma plugin + transforms (open core)
- Description: Token authoring in Figma, GitHub sync, Penpot/VS Code integrations; `sd-transforms` bridges to Style Dictionary.
- License: `sd-transforms` MIT; Tokens Studio core open-source, paid Studio platform proprietary (as stated on site) — verify per repo.
- Restrictions/Notes: Figma file access requires Figma credentials; transforms require Style Dictionary v4+ matrix (see compatibility table).
- Agent/CLI integration: CLI/SDK (`tokens-studio` CLI per site); no first-party MCP.

### 13. Theo (salesforce-ux/theo) — archived
- URL: https://github.com/salesforce-ux/theo
- Type: Token transform CLI (legacy)
- Description: JSON/YAML tokens → per-platform outputs.
- License: BSD-3-Clause (as stated) — Status: ARCHIVED.
- Restrictions/Notes: Archived; use Style Dictionary for new work per community guidance.
- Agent/CLI integration: CLI only.

### 14. Quieto Tokens (dillonschultz93/quieto-tokens, npm `@quieto/tokens`)
- URL: https://github.com/dillonschultz93/quieto-tokens
- Type: Token-scaffold CLI (3-tier: primitive/semantic/component, DTCG-aligned)
- Description: Interactive init, light/dark, iOS/Android/CSS/Figma-Variables outputs, `inspect`/`migrate`/`update --dry-run`, changelog.
- License: MIT (as stated).
- Restrictions/Notes: Figma output is static `tokens.figma.json` artifact only — "no Figma API integration" (per README).
- Agent/CLI integration: CLI + agent skills (`design-token-init/audit/migrate/component/category-add/contrast/update`); no MCP.

### 15. DesignPull CLI (kuriouscreator/designpull.dev, npm `designpull`)
- URL: https://github.com/kuriouscreator/designpull.dev
- Type: Markdown-to-Figma-variables CLI
- Description: `designpull init/sync/doctor`; parses `design-token.md` → Primitives/Semantic/Typography collections via Claude Code + Figma MCP `figma-use` skill.
- License: MIT (as stated).
- Restrictions/Notes: Requires Node 20+, Claude Code CLI, Figma MCP server, `FIGMA_ACCESS_TOKEN` (`figd_`) + file edit access; `.env` gitignored.
- Agent/CLI integration: CLI that spawns Claude Code subprocess; uses official Figma MCP (OAuth/PAT) for writes.

### 16. Grimorio CLI (npm `grimorio`)
- URL: https://github.com/sergioazoc/grimorio
- Type: Design-system infra CLI + validator + Figma importer + MCP bridge
- Description: `grimorio validate`, `figma:import`, `figma:validate`, `tokens:list/validate/export`; specs in `specs/`, `tokens.json`.
- License: MIT (as stated on npm).
- Restrictions/Notes: Figma import requires `FIGMA_TOKEN` / config; deterministic (non-AI) mapper per docs.
- Agent/CLI integration: CLI + MCP exposure (per npm description); config `grimorio.config.ts`.

## D. Figma access + validators

### 17. Figma Official MCP / Dev Mode MCP
- URL: https://developers.figma.com/docs/dev-mode-mcp-server/
- Type: First-party Figma agent bridge (read + write via OAuth)
- Description: File reads/creation via OAuth; zero PAT setup per downstream docs.
- License: Proprietary (Figma Terms) — code-access via MCP; check Figma plan limits.
- Restrictions/Notes: Rate limits apply on Free/Starter; Desktop app state required for some writes.
- Agent/CLI integration: MCP ( `figma-use` skill family).

### 18. @geeveeh/figma-cli (Shadowgandor/figma-cli)
- URL: https://github.com/Shadowgandor/figma-cli
- Type: Figma CLI + MCP server (21 tools, read + comment-post)
- Description: Inspect files/projects/components/styles/variables; `--json` everywhere; retry/backoff.
- License: MIT (as stated on npm).
- Restrictions/Notes: Token auth via `FIGMA_TOKEN` env or `~/.config/figma/config.json`; write scope limited to comments.
- Agent/CLI integration: CLI (`figma`) + MCP server (`figma-mcp`).

### 19. axe-core (dequelabs/axe-core)
- URL: https://github.com/dequelabs/axe-core
- Type: Accessibility validator engine (powers Lighthouse, Pa11y runners)
- Description: WCAG 2.0/2.1/2.2 A/AA/AAA + best-practice rules; embeds in Jest/Cypress/Playwright.
- License: MPL-2.0 (as stated + LICENSE, 3rd-party terms in LICENSE-3RD-PARTY.txt).
- Restrictions/Notes: MPL-2.0 file-level copyleft; Larger Work combination rules apply (see §3.3).
- Agent/CLI integration: Library (no native CLI); wrapped by Pa11y/axe-cli; JSON output for agents.

### 20. Pa11y + Lighthouse CI (validators)
- URL: https://github.com/pa11y/pa11y / https://github.com/GoogleChrome/lighthouse-ci
- Type: Validator runners (a11y + perf/SEO/a11y budgets)
- Description: Pa11y CLI wraps axe-core/HTML_CodeSniffer; LHCI (`lhci`) gates PRs, self-hostable server.
- License: Pa11y LGPL-3.0; Lighthouse CI Apache-2.0 (as stated).
- Restrictions/Notes: Headless Chrome required; Pa11y-dashboard/webservice separate components.
- Agent/CLI integration: CLIs with exit codes/assertions + HTML/JSON/CSV reports for agents.

---
Counts: 20 records (01–20). Astryx CLI-only/no-MCP verified via direct fetch of `facebook/astryx` root README + `packages/cli/README.md` on 2026-10-09.
