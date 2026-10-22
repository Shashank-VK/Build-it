# 01 — Authenticity Principles

**The Omniscient Resource Atlas · product_engineering / research / authenticity**
**Built 2026-10-10 · Read-only research: discover, inspect, identify, verify, categorize, explain usage, record sources. No installation, building, ranking, or recommendation.**

Scope: user prompt §§15–17. This file answers §15: what "authenticity" means for product interfaces, what design research actually supports, and how AI can be used productively without producing generic output. Companion files: `02-visual-identity.md` (§16), `03-anti-pattern-catalogue.md` (§17), `04-evidence-register.md` (per-finding metadata).

## Claim-label legend (used in all four files)

- **Verified** — confirmed against a primary source (peer-reviewed paper, official docs, statute, standards body) inspected or multiply corroborated.
- **Corroborated** — reported by ≥2 independent sources, or one primary source cited through a credible secondary; single chain of custody.
- **Inferred** — follows reasonably from verified/corroborated premises but not directly evidenced.
- **Proposed** — a single practitioner's or community's claim; plausible, not yet corroborated.
- **Unknown** — could not be established; recorded as a gap.

Evidence classes: **primary** (paper, official docs, statute, standards), **first-hand** (direct practitioner account of their own work), **corroborating** (independent source agreeing), **community** (skill repos, forum/blog consensus), **secondary** (press/blog reporting on primary), **unverified** (single uncheckable claim).

---

## P-01 · Operational definition of "authenticity" (Proposed → Corroborated)

"Authentic" here does **not** mean hand-made, human-only, or anti-AI. Across the surveyed sources it converges on four observable properties of an interface (paraphrased from the four root causes named in the krirox anti-slop skill, E06, and convergent with E04, E05, E14):

1. **Hierarchy** — the eye is led; elements carry visibly different weight.
2. **Specificity** — concrete copy, real numbers, named entities, product-specific visuals.
3. **Restraint** — each decorative device used sparingly and deliberately.
4. **Opinion** — the design could not belong to any company; some aesthetic risk is visible.

**Label: Corroborated** (community) — the four properties recur independently across E02, E04, E05, E06, E14, E46, though no peer-reviewed study states them in this form. They are a useful diagnostic, not a law.

## P-02 · The mechanism: distributional convergence (Verified mechanism; Corroborated application to UI)

When a model is asked for "a modern website," it returns the statistical center of its training distribution — the most probable, least objectionable answer. A 2024 *Nature* paper by Shumailov et al. (E01) formalized the underlying dynamic for recursive training: models trained on generated data undergo **model collapse**, losing the tails of the distribution — the rare, distinctive cases — first, converging to reduced variance. Community design writing (E02, E06) applies this as an analogy to single-pass generation: asking for the average produces the average, and "the most likely version is also the most average version" (E47, paraphrased).

**Labels:** the collapse mechanism itself — **Verified** (primary, peer-reviewed, E01). The claim that single-pass UI generation regresses to a stylistic mean — **Corroborated** (community) as an observational regularity, **Inferred** as a causal explanation; the Nature paper concerns recursive training, not one-shot prompting. Do not cite E01 as proof that one prompt produces the mean; cite it as the mechanism that makes the analogy plausible, and E02/E06/E47 for the observation.

## P-03 · Thin input ⇒ cliché output (Corroborated)

The sharadvermasv design-intelligence skill (E40) states the relationship precisely: the "generic AI look" is not one fixed aesthetic — it is *whatever is most probable given the information provided*, and thin input makes the probable answer the cliché one. Corroborated by E48 (prompt specificity determines output quality in AI site builders) and E14 ("the difficult part is still giving it enough constraints that the object belongs to this product").

**Implication:** the highest-leverage anti-generic move is informational, not stylistic — supply brand, audience, differentiator, real product detail, point of view *before* generating. **Label: Corroborated** (community, multiple independent).

## P-04 · What design research supports (Verified)

These are findings from established research, distinct from taste:

| # | Finding | Source | Label |
|---|---|---|---|
| P-04a | **Aesthetic–usability effect.** Users perceive attractive interfaces as more usable than they are (Kurosu & Kashimura 1995; confirmed by Tractinsky et al.; discussed by Don Norman). Beauty buys patience for minor issues — but can mask real usability problems. | NN/g, "The Aesthetic-Usability Effect" (E08) | **Verified** (primary org; peer-reviewed origins) |
| P-04b | **50-millisecond first impressions.** Aesthetics judgments form ~50ms after landing (Lindgaard et al.); rarely revised with more time. | NN/g, "First Impressions Matter" (E10) | **Verified** |
| P-04c | **Prominence–interpretation theory** (Fogg). The more prominent an element, the larger its impact on credibility judgments — positive or negative. Moving/annoying elements actively *reduce* credibility. | NN/g, "First Impressions Matter" (E10) | **Verified** |
| P-04d | **Aesthetic & minimalist design (heuristic #8).** Interfaces should contain only necessary, high-information-value elements; every extra unit competes with relevant ones. "Clarity will always win over visual flourish." | NN/g (E09) | **Verified** |
| P-04e | **Jakob's Law.** Users prefer sites that work like the ones they already know. | Laws of UX (E13) | **Verified** (long-standing, multiply replicated) |
| P-04f | **Von Restorff (isolation) effect.** The item that differs from its neighbors is most likely remembered. | Laws of UX (E13) | **Verified** |
| P-04g | **Generative UI ≠ AI-assisted design.** NN/g distinguishes interfaces the *AI* initiates (genUI) from AI tools used inside a professional workflow (AI-assisted design); in the latter, human judgment remains the steering layer. NN/g's survey found UX professionals use genAI mostly for *text*, far less for design-specific tasks. | NN/g (E12) | **Verified** (org primary; survey with reported significance) |
| P-04h | **Taste vs. technical skill.** As genAI removes technical barriers, discernment — not production ability — becomes the differentiator. | NN/g (E12) | **Corroborated** (org position paper; philosophical more than empirical) |
| P-04i | **Contrast minimums.** 4.5:1 normal text, 3:1 large text (WCAG AA); 3:1 for UI components. | W3C WCAG (E27) | **Verified** (standard) |
| P-04j | **Animation-from-interactions / reduced motion.** Non-essential motion must be suppressible; vestibular-triggering motion (parallax, large transforms, autoplay) harms users with vestibular disorders. | WCAG / WebKit guidance (E27, E28) | **Verified** (standard + vendor guidance) |

## P-05 · The Jakob's-law / differentiation tension (Inferred, widely corroborated)

P-04e and P-04f pull in opposite directions, and that tension is the whole game: **conventions should be borrowed for usability mechanics** (navigation, forms, checkout, icons-as-language) and **broken for identity** (color, type voice, composition, illustration). The pixeldarts analysis of Stripe/Linear/Vercel (E42) notes the monochrome-plus-one-accent system "still works and still wins" — while warning it is becoming "the new 'blue for trust'": a seriousness signal that says nothing specific about *who you are*. **Label: Inferred** — no study draws this line explicitly; it is the synthesis the evidence points to.

## P-06 · What counts as "research-backed" vs "taste" (Proposed framework; apply skeptically)

| Tier | Example claims | Status |
|---|---|---|
| Research-backed | aesthetic-usability effect; 50ms impressions; contrast ratios; modal-interruption costs (E11); fake-review illegality (E20) | Act on these as constraints |
| Professional consensus | semantic color roles; 8pt/4pt spacing scales; one type voice; restraint in motion; real product visuals over decoration | Strong defaults; allow justified exceptions |
| Community pattern-language | "purple gradient = slop", "three cards = slop", "bento = slop" | Useful tripwires, **not laws** — E04 explicitly warns against global bans |
| Taste / positioning | anti-design imperfection-as-authenticity (E49); "never center a hero" | Treat as one stance among several; record, don't universalize |

**Label: Proposed** — this tiering is the author's synthesis for the Atlas; it is offered as a working tool, not a finding.

## P-07 · The productive AI workflow (Corroborated)

NN/g's framing (E12) plus practitioner sources converge on one workflow:

1. **Decide before generating.** Establish a written design direction first — NN/g: designers must "shift attention toward outcomes and constraints" (E12); E14: "the screen is consistent before it has earned consistency" because generated interfaces carry no scars from real constraints.
2. **Counter-anchor.** Pair any saturated reference (Linear, Vercel, Stripe — E05) with a reference from *outside* software (print, signage, instruments, architecture); "not Linear" alone does not escape the mean.
3. **Differentiator test.** E05: require a written answer to "what will a viewer see in three seconds that a generated default would not have?" Adjective soup ("clean, modern, premium") fails the test.
4. **Generate, then audit.** Use the anti-pattern catalogue (file 03) as a tripwire list; E04's audit format — severity, certainty, *why it reads generic*, product justification, correction — is the right shape.
5. **Keep humans on states, not just screens.** E04: generated UI is "happy-path-only" — loading, error, focus, pressed, empty states are where production-readiness shows.

**Label: Corroborated** (community + org; no controlled study of the workflow itself — **Unknown** whether it outperforms alternatives experimentally).

## P-08 · Two failure modes, not one (Inferred)

Sources describe two opposite ways to fail: **the polished mean** (purple gradients, glass, bento — over-decorated convergence) and **the sterile mean** (flat white, thin grey borders, no texture, no identity — E04's "sterile default," produced by over-filtering without direction). Banning the first without supplying a direction produces the second, which "reads as AI-generated just as loudly as a purple gradient" (E05). **Label: Inferred** from E04/E05; corroborated observationally across catalogs.

## P-09 · Honest unknowns

- **Unknown:** whether users *consciously* detect "AI-generatedness" or merely react to low specificity/low craft; the "three-second tell" (E02) is practitioner introspection, not an experiment.
- **Unknown:** the 2025-study claim that "80%+ of AI-generated websites had almost the same underlying structure" (E17) — a third-hand citation chain (2025 study → Jan 2026 Medium article → Sept 2026 dev.to post); treat as **Proposed**, not evidence.
- **Unknown:** the "Design Theater" benchmark numbers (120 interfaces, 1-in-4 fabricated rationales, E15) — single practitioner source, no published methodology; **Proposed**.
- **Unknown:** whether anti-slop checklists measurably improve user outcomes vs. simply adding a design-review step; no comparative study found.
