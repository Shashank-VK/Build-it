# §20 — Demo Authenticity Checklist

- **Workstream:** ux-states, research only — discover, inspect, identify, verify, categorize, explain usage, record sources. Researched 2026-10-10; all sources accessed 2026-10-10.
- **Purpose:** a practical checklist for judging whether a demo (live demo, recorded walkthrough, interactive tour, sandbox) accurately represents the product. Demo ≠ product is normal and often legitimate; *undisclosed* divergence is the problem.
- **Claim labels:** **Verified** = authoritative source · **Corroborated** = ≥2 independent sources · **Inferred** = logical extension · **Proposed** = practitioner recommendation · **Unknown** = no reliable source.
- Evidence: `04-evidence-register.md`.

## How to use it

Score each item **Pass / Fail / N/A**. A demo fails the authenticity test not when it is polished or rehearsed — stage demos are *always* rehearsed (even Apple and Microsoft rehearse heavily; on-stage demos routinely fudge timing for smoothness) — but when a buyer or user would make a different decision if they knew the truth. The operative question per item: **"Would knowing this change the evaluator's decision?"**

---

## Checklist

### 1. The demo actually runs the product
- [ ] **The actions shown execute real product code paths**, not a clickable mockup, video masquerade, or Wizard-of-Oz human behind the curtain — or the simulation is disclosed (see §3).
  - *How to check:* ask for an unscripted task ("show me that with my data / a different input"); request the browser devtools network tab during a live demo; look for canned responses that don't vary with input.
  - *Red flag:* every input produces suspiciously perfect output; the presenter avoids deviations from the script; "we can't show that part live."
  - *Green flag:* the demo visibly hits the network, handles an unexpected input gracefully, shows real latency.
- [ ] **Failure is demonstrated, not hidden.** A demo that never shows an error state, a retry, an offline moment, or a validation message is hiding the product's true surface area. Evaluators are explicitly advised to demand failure handling in demos.
  - *How to check:* "Show me what happens when this fails / when you're offline / with bad input."

### 2. The data is honest
- [ ] **Sample data is realistic** — messy enough to resemble production (typos, edge cases, long strings), not a sanitized happy path.
- [ ] **Simulated or mock data is disclosed** as such, in the demo itself — not buried in fine print. Undisclosed mock data that a viewer could mistake for real results is misrepresentation.
  - *Red flag:* dashboards full of round numbers and perfect trends; "customer" names that are alliterative or joke names; demo content never replaced (a documented fraud signal in scam-site analysis).
- [ ] **Performance claims are measured, not staged.** "Loads instantly" on a local build with a warm cache and 10 rows is not a performance claim — it's theater. Ask: measured how, on what hardware/network, at what data volume, at which percentile.
- [ ] **Screenshots and marketing visuals match the shipped implementation.** A screenshot of a feature that doesn't exist (or no longer looks like that) is the visual form of a fake demo.

### 3. Simulated vs real is labeled
- [ ] Any Wizard-of-Oz, concierge, or human-in-the-loop step is disclosed where the viewer would reasonably assume automation.
- [ ] Prototype/alpha/beta status is stated plainly; roadmap items are labeled "planned," never presented in present tense as shipped.
  - *Red flag:* present-tense feature lists for unbuilt features; "coming soon" pages with no date and no progress signal.

### 4. Onboarding, trials, and sandboxes are real
- [ ] **Interactive onboarding lets the user touch the product** — real buttons, real actions, sample data provided so actions work. Passive tours and long welcome carousels are weaker but not dishonest; a tour that *pretends* to be interactive is.
- [ ] **Demo accounts / sandboxes** provision a working environment with realistic seed data, clearly reset/scoped, without requiring a sales call to see anything real. Inability to test the product before sign-in is a documented trust red flag.
- [ ] Sandbox limitations (rate limits, disabled features, data reset cadence) are stated up front.

### 5. Social proof is genuine
- [ ] **No fabricated customers, metrics, or testimonials.** Customer logos shown are actual customers (with permission); testimonials are from real, verifiable people reflecting genuine experience; metrics are measured and defined (what counts as a "user"? over what period?).
  - *Legal floor:* the FTC's fake-review rule (effective 21 Oct 2024) prohibits creating, buying, or disseminating fake reviews/testimonials, including AI-generated ones; undisclosed insider reviews and suppressed negative reviews are covered; civil penalties apply. The UK's DMCC Act separately outlaws fake reviews. **Corroborated.**
  - *Red flags:* stock-photo "customers"; testimonials with no verifiable identity; suspiciously uniform 5-star distributions; review counts that can't be found on the cited platform; logos of companies that never agreed.
- [ ] **Material connections disclosed** — paid placements, investor-portfolio logos presented as customers, employee reviews. (FTC Endorsement Guides.)
- [ ] **Metrics defined, not vanity.** "10,000+ users" should survive the questions: registered or active? over what window? measured how? Research on startup "façading" documents the escalation path from exaggerated metrics → falsified evidence → staged operational environments; evaluators should treat unverifiable headline numbers as unproven. **Corroborated** (academic study + enforcement reporting).

### 6. Planned vs available is explicit
- [ ] A clear, maintained distinction between **available now**, **in beta** (with access criteria), and **planned** (with rough horizon or explicitly "no date committed").
- [ ] Changelog / release notes exist and are consistent with what's demoed — a feature demoed but absent from any release note is a question, not a fact.
- [ ] Pricing shown in the demo matches the pricing page; no hidden tiers, no "contact us" hiding the actual cost of the demoed configuration.

### 7. AI-specific honesty (where applicable)
- [ ] **AI limitations are stated:** what the AI can't do, confidence/error modes, where humans review or take over, how user data is used for training.
  - *Legal floor (EU):* AI Act Article 50 transparency duties effective 2 Aug 2026 — disclose AI interaction, machine-mark synthetic content, disclose deepfakes/public-interest AI text. **Corroborated.**
- [ ] The demo distinguishes the **demo path** (curated prompt, clean data, no guardrails) from the **production path** (input cleaning, scoping, hallucination checks, abuse detection, cost/latency budgets). A practitioner essay contrasts exactly these two pipelines as the demo-vs-product gap.
- [ ] No implication that a prototype's economics work at scale — token cost, latency under load, and abuse handling are part of "does it work," not footnotes.

### 8. The boring completeness signals
These are cheap to fake in a mockup and expensive to build for real — their presence is weak evidence of authenticity, but their *absence* in a "finished product" demo is a strong tell:
- [ ] Real favicon, working footer links, no lorem ipsum, no dead "#" links.
- [ ] Loading, empty, and error states exist (see `02-ux-state-matrix.md`) — a demo with only the happy path is either a mockup or an unfinished product.
- [ ] The product works on a phone-width viewport, not just the presenter's laptop.
- [ ] Contact/support path is real and reachable; company identity (legal name, address/jurisdiction) is published.

---

## Cautionary cases (brief, factual)

- **Ovation (1983):** announced an integrated software package and showed a demo to raise funding; per the *New York Times*, the demo was fake and the software never existed — the canonical vaporware case. **Corroborated** (Built In summary citing NYT).
- **Magic Leap (reported 2016):** reporting alleged the company's promotional demos overstated how far its mixed-reality technology had progressed while it was years behind schedule. Lesson: cinematic "product videos" are marketing, not evidence of a working product. **Corroborated** (The Information via The Verge/Slashdot).
- **Fake AI storefronts (2026):** a documented toolkit enabled 100+ professional-looking AI-service sites with billing and Google sign-in for ~$249; red flags included no pre-signup trial, unverifiable user-count claims, and unreplaced demo content. Lesson: SSL, polished design, and familiar auth buttons are no longer trust signals on their own. **Corroborated** (DeafNews dossier summary).
- **Startup "façading" (academic, 2026):** Imperial/Emlyon research models the escalation from exaggerated metrics → falsified documents → fully staged demos ("parallel realities") under investor pressure. Lesson: verify, don't trust, headline traction. **Corroborated** (Innovation Village summary of the study).
- **On-stage tech demos generally:** even the most legitimate companies rehearse heavily and fudge timing; Steve Jobs's 1984 Macintosh demo famously used a more powerful machine than the one being sold (confirmed by engineer Andy Hertzfeld). Lesson: rehearsal is normal; *concealment of material divergence* is the line. **Corroborated** (Gizmodo; Folklore.org via Hertzfeld).

## Scoring guidance

- **Authentic:** all applicable items pass; any simulation disclosed; failures demonstrated.
- **Conditionally authentic:** minor gaps (e.g., sandbox limits unstated) that don't affect a purchase/adoption decision — note them and move on.
- **Not authentic:** any fail in §1, §2, §5, or §6 — these change decisions. Treat "we'll show you after the contract" for core functionality as a fail until proven otherwise; evaluators are explicitly advised to demand production pilots over demos for anything load-bearing.

*Polish details: `01-polish-details.md`. State matrix: `02-ux-state-matrix.md`. Evidence: `04-evidence-register.md`.*
