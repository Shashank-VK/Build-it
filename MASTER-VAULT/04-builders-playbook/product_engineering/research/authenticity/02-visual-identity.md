# 02 — Visual Identity & Design Originality

**The Omniscient Resource Atlas · product_engineering / research / authenticity**
**Built 2026-10-10 · Read-only research. Claim labels: Verified / Corroborated / Inferred / Proposed / Unknown (see 01, P-06).**

Scope: user prompt §16. For each identity element: what excellent teams do (per documented design systems), the AI-default failure mode, and when the "suspect" treatment is legitimate. Nothing here bans any technique outright — see 01 P-06/P-08.

---

## V-01 · Distinctive visual identity: decisions, not defaults

Across sources, identity is not a style — it is the residue of product-specific decisions. The dev.to analysis (E02) contrasts three admired products: **Linear** (restraint — tight palette, deliberate density, fast purposeful motion; every choice made *against* the average), **Notion** (color used *semantically* — a color means a state or category — not decoratively), **Stripe** (identity built from craft most teams skip: custom illustration, precise intentional gradients, typographic voice). Common thread: "good design comes from somewhere" — a point of view about who the product is for (E02, paraphrased). **Label: Corroborated** (community; convergent first-hand readings of public products).

The mechanism of losing identity is named precisely in E05: a **saturated anchor** — a reference so widely imitated by generative tools (Linear, Vercel, Stripe, Raycast, Notion, Figma, Apple) that asking for it yields the *average of the imitations*, not the reference. Naming a saturated anchor in the brief is described as the bug itself. **Label: Proposed** (single community source, but consistent with P-02).

## V-02 · The fifteen identity elements

### V-02a · Typography: selection and hierarchy

- **What systems do.** Material 3 defines a five-role type scale — Display, Headline, Title, Body, Label — each with size/weight/leading tokens (E22). Carbon pairs IBM Plex (open SIL OFL license) with tightening display line-heights and relaxed body leading (E23: 1.17 at display-xl → 1.50 at body). Hierarchy is carried by *scale contrast and role*, not by bolding everything (cf. catalogue C-V10).
- **AI failure mode.** One default grotesk (Inter/Geist/Roboto) at one or two sizes, or "thick typography everywhere"; no typographic voice (E07, E38).
- **What preserves identity.** One display voice + one workhorse text face, chosen for the product's register (editorial, engineering, clinical…); type scale as tokens; restraint with weight. **Label: Corroborated** (systems primary-adjacent + community consensus).

### V-02b · Spacing systems and layout rhythm

- **What systems do.** Carbon: 2px-base token scale `$spacing-01` (2px) → `$spacing-13` (160px), plus layout tokens `$layout-01`–`$layout-07` for page structure; arbitrary values (13px, 23px) are explicitly marked wrong (E23). 4/8pt rhythm is the industry default elsewhere.
- **AI failure mode.** Arbitrary or uniform spacing; sections separated by identical padding regardless of content relationship; rhythm that never varies (E23's "incorrect" examples are exactly what generators emit).
- **What preserves identity.** Spacing tokens committed before screens; section rhythm that varies with content weight. **Label: Corroborated** (Carbon docs via mirrors, E23).

### V-02c · Colour palettes and semantic colour roles

- **What systems do.** Material 3 replaced "pick a palette" with **colour roles**: Primary, On-Primary, Primary Container, Surface, On-Surface, Error, etc. — each role describes *what the colour does* (E22). Ant Design generates a 10-step algorithmic palette around a seed hue with hue-tilting to avoid muddiness (community decode, E25-adjacent). Notion (E02) assigns meaning per colour.
- **AI failure mode.** Tailwind defaults untouched (`indigo-500`, `slate-900`); colour as decoration — accents sprinkled "for vibes" (E02); rainbow gradients; one accent used on buttons, icons, badges, glows simultaneously (E38).
- **What preserves identity.** Seed → tonal palette → semantic roles; one accent with a *job*; neutrals doing structural work. **Label: Corroborated** (M3 docs via secondary, E22).

### V-02d · Contrast and readability

- Research floor: WCAG AA 4.5:1 normal text, 3:1 large text and UI components (E27, **Verified**). Glow/shadow treatments must not be the thing carrying text legibility (E38); glass panels over busy backgrounds routinely fail this (E38).
- AI failure mode: grey-on-grey secondary text, gradient text at small sizes, frosted panels over imagery. **Label: Corroborated.**

### V-02e · Density and information hierarchy

- Carbon is the documented counterexample to "whitespace = premium": enterprise density is *functional* — background-colour zoning and 48px section rhythm instead of vast padding (E23). Density is a product decision (trading terminal vs. marketing page), not a quality signal either way.
- AI failure mode: one density everywhere — either airy landing-page rhythm applied to data UI, or cramped defaults. **Label: Corroborated** (E23 + E41 on surface-appropriate divergence).

### V-02f · Grids and alignment

- Carbon: 16-column 2x grid, 1584px max, 32px gutters (E23). M3: adaptive breakpoints compact→expanded (E22).
- AI failure mode: centered, symmetrical, everything-in-a-3-column-grid composition with no compositional intent (E07, E38).
- Identity move: one deliberate compositional decision *before* placing elements — asymmetry, editorial bands, staggered grids — chosen for the content (E04: "start from a strong compositional decision"). **Label: Corroborated.**

### V-02g · Component consistency

- Systems ship do/don't guidance per component (Ant Design "strongly opinionated" best practices, E25; Polaris component pages with usage rules, E24).
- AI failure mode: same component styled three ways on one page; or identical `rounded-2xl shadow-lg border` on every surface so nothing earns emphasis (E07).
- The fix is tokens + one radius/shadow language per elevation level (Carbon: sharp 0px corners as philosophy; shadows only on modal/notification — E23). **Label: Corroborated.**

### V-02h · Iconography

- Systems: single stroke width per layer, token sizes, one style (filled *or* outline) per hierarchy level (E38, community skill consensus; consistent with Primer/Material icon guidance in spirit).
- AI failure mode: emoji as structural icons — font-dependent, inconsistent across platforms, uncontrollable via tokens (E38, three independent skills agree); mixed Lucide/Heroicons with no custom touch (E38).
- Legitimate emoji use: inside user-generated content, reactions, empty-state illustrations with brand voice — never as nav/system iconography. **Label: Corroborated.**

### V-02i · Illustration, imagery, photography

- NN/g-cited finding (via E34): users respond best to photos of *real people from the company*; staged stock reads as inauthentic and is spotted quickly. UXCambridge/FOWD photo research (E34-adjacent): generic stock fails empathy — "often they don't look like 'real' people." Practitioner consensus (E35, E02): one high-quality real visual beats five mediocre ones; show the *actual product* — skewed screenshots, real outputs — as the hero visual (E46).
- AI failure mode: unrelated stock handshakes, generated abstract blobs, AI "team" photos. **Label: Corroborated** (NN/g via secondary + practitioner convergence).

### V-02j · Brand voice and microcopy

- Polaris treats Content as a co-equal nav section with Design and Components; fundamentals include "Keep it lean," "Write like merchants talk," "Inspire action"; voice/tone historically had its own pages (E24). Microcopy is identity: error messages, empty states, button verbs carry the brand.
- AI failure mode: "Transform/Elevate/Unlock" vagueness (E04), puffery clusters (E31), hedged dutiful reassurance (E32). See catalogue copywriting section. **Label: Corroborated.**

### V-02k · Design tokens

- DTCG-style three-tier tokens (primitive → semantic → component) are the documented industry practice (E38: "Ekasit's Law" — never invent arbitrary hex; new tokens need explicit approval). Tokens are what let identity *survive* AI-assisted implementation: the model fills slots instead of inventing values.
- **Label: Corroborated** (community practice; W3C DTCG is a real community group — **Verified** existence, Corroborated adoption claims).

### V-02l · Responsive behaviour

- M3 adaptive layouts; Carbon breakpoints; generated pages commonly desktop-only screenshots or breakpoints that collapse gracefully by accident (E38 "desktop-screenshot-only layouts").
- Production bar: real breakpoints, readable measure, touch targets ≥44×44 (platform guidance; WCAG 2.5.8 minimum 24×24 CSS px — E27/E51, **Verified** standard, Corroborated practice). **Label: Corroborated.**

### V-02m · Motion and interaction restraint

- Every animation should serve feedback, continuity, hierarchy, or delight — "if the answer is 'it looks cool,' delete it" (E30, community). Frequency governs intensity: button press ≤100ms, dropdown 150–200ms, modal 200–300ms (E30). Ease-out entrances, ease-in exits; animate transform/opacity only (E30). Never scroll-reveal body copy (E30). Respect `prefers-reduced-motion`: remove travel, keep meaning via opacity/color (E28, E29).
- **Labels:** timing/easing guidance **Corroborated** (community, convergent); reduced-motion requirement **Verified** (E27/E28).

---

## V-03 · The "suspect combos": why they read as derivative, and when each is appropriate

The rule from 01 stands: these are tripwires, not bans (E04: "do not ban these patterns globally"). For each: the *unexamined* failure, then legitimate uses.

| Combo | Why it reads derivative unexamined | When it IS appropriate (with rationale) | Label |
|---|---|---|---|
| Purple/blue gradients | Tailwind `indigo-500` defaults; Adam Wathan's Aug-2025 apology post for normalizing it (E19, unverified directly) made it the #1 generation tell (E07) | Brand hue genuinely is violet (e.g., a creative-tool brand); Stripe-style *crafted* multi-stop gradients with illustration (E43); aurora as a deliberate brand motif with tokens | Corroborated |
| Purple-and-black palettes | Reads as "AI startup uniform" (E03): near-black + purple-to-blue radial glow + sparkle icon | Developer/infra tools used at night; gaming; brands whose identity predates the trend — with a written rationale (E03: "only if dark mode says something true about your product") | Corroborated |
| Glassmorphism / liquid-glass | Frosted panels stacked on gradients as reflex, "applied as reflex, not for layering meaning" (E07) | True layering semantics: iOS-style sheets over content, nav over scrolling imagery — one or two surfaces, with contrast verified (E27) | Corroborated |
| Oversized typography | Giant ultra-bold grotesk headlines are a cross-category statistical attractor (E40) | Editorial brands, poster-like confidence *as a stated direction* (E40: "if they do call for it, state that reasoning explicitly") | Inferred |
| Generic cards | `rounded-2xl shadow-lg border` on every surface; identical 3-up icon+heading+text grids = "no hierarchy; every feature equally important" (E07) | Real card semantics: heterogeneous content needing containment (dashboards, listings); then vary size/rhythm deliberately | Corroborated |
| Glowing accents / neon | "Decoration masquerading as depth" (E07); glow on everything at once (E38) | Single focal glow as brand signature; status/energy semantics in gaming or music products | Inferred |
| Repetitive layouts | Centered badge + H1 + two CTAs + three cards, repeated per section (E04) | Marketing pages where the *structure* is a conversion convention (E43: best SaaS pages share structure, differ in style) — then differentiate within the structure | Corroborated |

## V-04 · Establishing direction BEFORE generating (the §16 workflow)

1. **Write the Design DNA first.** One page: palette with roles (V-02c), type scale (V-02a), spacing tokens (V-02b), radius/shadow language (V-02g), icon style (V-02h), motion budget (V-02m), voice notes (V-02j). E04's validator model: P0/P1 conflicts with the DNA get fixed or explicitly justified.
2. **Counter-anchor outside software** (E05): one reference from print, signage, instruments, architecture.
3. **Differentiator line** (E05): what a viewer sees in three seconds that a default would not show.
4. **Tokens before screens** (V-02k): generate into slots, not into free choice.
5. **Audit against the DNA**, not against a ban list (E04 severity/certainty format; 03 catalogue as tripwires).

**Label: Corroborated** as a workflow (community convergence); **Unknown** whether it experimentally outperforms alternatives.

## V-05 · Counterexamples that keep the honest (great products using "suspect" patterns well)

- **Stripe's animated gradient hero** — the signature gradient became "a cultural moment in itself"; it works because it is crafted, ownable, and paired with custom illustration (E42, E43).
- **Notion's colour** — semantic, not decorative (E02).
- **Linear's dark UI** — dark because the product is a dense professional tool; restraint as positioning (E42, E03).
- **Warm light interfaces** in a dark-mode category — differentiation by inversion (E03).
- **Bento grids** — legitimate when content has genuine heterogeneous-card semantics (E04 warns against *decorative* bento, not bento).

These exist to prevent the catalogue (file 03) from hardening into law. **Label: Corroborated** (public products, first-hand readings).
