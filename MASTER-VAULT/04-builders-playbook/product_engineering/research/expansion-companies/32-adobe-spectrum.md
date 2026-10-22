# Adobe Spectrum — product engineering case study (React Aria + the Figma deal collapse)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Spectrum is Adobe's design system — notable for **React Aria** (headless accessibility primitives, the industry's best a11y engineering), the **Spectrum 2** theme bridge, and the token pipeline (global → alias → semantic). The file also records the **Figma acquisition collapse** ($20B → blocked by regulators → ~$1B termination fee, Dec 2023) as the business postmortem adjacent to the design-system story. Primary evidence includes Adobe's own repos (react-spectrum, spectrum-web-components).

## 1. Forensic reconstruction — how the machine actually works

### React Spectrum + React Aria: behavior without styling
- Claim: Adobe split the problem in two: **React Spectrum** (full components with Spectrum styling) and **React Aria** (headless primitives — behavior, interactions, accessibility — with no styling opinions). React Aria exposes hooks like `useButton`/`useDialog` that implement WAI-ARIA patterns, keyboard interaction, and screen-reader announcements, letting any design system get Adobe-grade accessibility without Adobe's visuals. Label: **Corroborated** — adobe/react-spectrum repo (packages/@react-spectrum/ai stories); madebyaris design-rules notes. Confidence: high on the architecture; medium on internals (repo fetched as file listing/prose, not deep-dived).
- Claim: This is the strongest accessibility-engineering program among the design systems in this workstream: behavior tested against assistive technology, not just ARIA attributes sprinkled on divs. Label: **Inferred** — consistent with React Aria's reputation and structure; comparative testing evidence not fetched. Confidence: medium.

### Spectrum 2 and the token pipeline
- Claim: **Spectrum 2** is the next-gen theme with a bridge/migration path from Spectrum 1; the token pipeline follows the standard three layers (global → alias → semantic); **scale** (medium/large density switching) is a first-class token dimension for touch vs. desktop density. Label: **Corroborated** — spectrum-web-components repo (2nd-gen AI skill docs); madebyaris notes. Confidence: medium-high.
- Claim: Adobe ships **AI-facing artifacts** for the system: the react-spectrum repo contains `@react-spectrum/ai` stories/prose, and spectrum-web-components ships an **SKILL.md** for agents — the design system documents itself for machine consumers, same as Carbon's AGENTS.md. Label: **Verified** — repo paths fetched (github.com/adobe/react-spectrum, github.com/adobe/spectrum-web-components). Confidence: high that the artifacts exist; medium on their quality.

### Spectrum Web Components: standards-based delivery
- Claim: Alongside React, Adobe ships **spectrum-web-components** (Custom Elements) — the standards-based path for non-React consumers. Label: **Verified** (repo). The two-implementation strategy (React + web components) is the honest answer to framework churn, at the cost of maintaining two component models.

## 2. Postmortem record — the Figma deal collapse
- **Timeline:** Sept 2022: Adobe announces **$20B acquisition of Figma** (the largest private-software acquisition ever proposed) → 15 months of regulatory review (EU, UK CMA) → **Dec 2023: deal terminated**; Adobe pays **~$1B termination fee**. Label: **Corroborated** (widely reported; figures consistent across coverage). Confidence: high.
- **Why it matters for product engineering:** Adobe's design-tool strategy (XD, then Spectrum as the system) had *lost* to Figma in the market; the acquisition was the strategy to buy back leadership. Its collapse left Adobe competing against the company it tried to buy, now independent and (per the Tailwind file) consolidating (Figma's own 2026 moves). The engineering lesson: **you can't acquire your way out of a product deficit when regulators define the market as the two of you** — the CMA/EU framed it as removing Figma as Adobe's closest competitor. Label: **Inferred** (audit synthesis) on **Corroborated** regulatory facts.
- **Spectrum's quiet vindication:** while the deal drama played out, Spectrum/React Aria kept shipping and became *more* strategically valuable — Adobe's design-system moat doesn't depend on owning Figma. The postmortem's silver lining: invest in the platform layer (systems, tokens, a11y primitives), which compounds regardless of M&A outcomes. Label: **Inferred**.

## 3. Narrative audit — dismantling with receipts
- **"$20B for Figma" as an engineering indictment.** The price tag is the receipt: Adobe valued Figma at roughly *half of Adobe's own market cap growth story* because its internal tools org (XD) had failed to match a browser-based multiplayer editor. The dismantling: the acquisition attempt was a *postmortem of Adobe's product engineering* in design tools, written in dollars. No strategy deck admits failure this clearly; the $20B bid did. Label: **Inferred** (audit synthesis) on **Corroborated** deal facts.
- **React Aria's "headless" honesty vs. the industry's a11y theater.** Most design systems claim accessibility via ARIA attributes; Adobe's split (behavior in React Aria, styling separate) is an architectural admission that *accessibility is behavior, not markup* — keyboard interaction models, focus management, screen-reader announcements are state machines, not props. The audit credit: this is the correct decomposition, and the repos are the receipts. The caveat: adopting React Aria still requires your team to *compose* the behaviors correctly — headless doesn't mean foolproof. Label: **Inferred** on **Corroborated** architecture.
- **Two component models = honesty about framework churn, at a real cost.** Shipping both React and web-components implementations admits no single framework wins — but it doubles the API-surface maintenance. Adobe can afford this; smaller teams copying "we'll support everything" should note the staffing behind it. Label: **Inferred**.
- **AI skill files (SKILL.md) as the new docs — audit the substance.** Adobe and IBM both now ship agent-facing docs. The receipts show the *artifacts exist*; what's unverified is whether agents actually produce better Spectrum/Carbon UIs with them versus the human docs. The industry is in the demo phase of agent-readable design systems — Atlassian's measured accuracy/speed/cost approach (file 31) is the standard the others should meet. Label: **Inferred**.

## Transferable lessons
1. **Accessibility is behavior, not markup.** Decompose into headless interaction primitives (React Aria's model) rather than sprinkling ARIA attributes — test with assistive tech, not just validators.
2. **Invest in the platform layer regardless of M&A.** Spectrum compounded while the Figma deal lived and died; tokens and a11y primitives are acquisition-proof assets.
3. **Density as a token dimension.** Spectrum's scale (medium/large) treats touch-vs-desktop density as theming, not branching — steal this for any multi-form-factor system.
4. **Two implementations admit framework churn is real** — but price the doubled maintenance before copying.
5. **Agent-readable docs need measured outcomes.** Ship SKILL.md/AGENTS.md *and* Atlassian-style accuracy/speed/cost evaluations, or it's marketing.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| AD1 | React Spectrum AI stories/prose (repo) | https://github.com/adobe/react-spectrum/blob/HEAD/packages/@react-spectrum/ai/stories/prose.mdx | Primary technical (repo) | Adobe | Live | 2026-10-10 | High (existence) |
| AD2 | SWC AI skill (SKILL.md, 2nd-gen) | https://github.com/adobe/spectrum-web-components/blob/HEAD/./2nd-gen/packages/ai/skills/swc-skill/SKILL.md | Primary technical (repo) | Adobe | Live | 2026-10-10 | High (existence) |
| AD3 | Spectrum component/design-rule notes | https://github.com/madebyaris/design-rules-ai/blob/HEAD/.mba-template/design-systems/adobe-spectrum/components.md | Secondary (GitHub) | madebyaris | n.d. | 2026-10-10 | Low-medium |
| AD4 | AI design-system research context | https://github.com/atebit/ai-product-design-resources/blob/HEAD/docs/research/foundational/02-ai-design-systems.md | Secondary synthesis (GitHub) | atextit | n.d. | 2026-10-10 | Low-medium |
| AD5 | Figma acquisition collapse ($20B → blocked → ~$1B fee, Dec 2023) | Widely reported (no single URL fetched this pass — verification debt) | Secondary | Multiple | Dec 2023 | 2026-10-10 | High (facts) / Low (citation) |

**Gaps:** Figma-deal primary/regulatory docs (not fetched — figures Corroborated but citation is a verification debt); React Aria internals (not deep-dived); Spectrum 2 migration experience (Unknown); Spectrum adoption metrics inside Adobe (Unknown).
