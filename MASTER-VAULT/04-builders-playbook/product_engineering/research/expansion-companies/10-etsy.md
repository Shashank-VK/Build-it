# Etsy — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Etsy is the origin point of two industry-standard practices: blameless postmortems (John Allspaw, 2012) and continuous deployment at web scale. The Allspaw primary (etsy.com/codeascraft/blameless-postmortems) is cited across sources but was not fetched directly this pass — its lineage and influence are Corroborated from multiple independent secondaries.

## Findings

### Process / culture
- Claim: John Allspaw's "Blameless PostMortems and a Just Culture" (Etsy Code as Craft, May 2012) is the origin of the blameless-postmortem norm in software: treat the mistake as information about the system, not the person; premise that everyone acted reasonably given what they knew at the time (countering hindsight bias). Label: **Corroborated** — cited as canonical by 4+ independent sources (kipi-system, tech-operator-crm-cards, production-framework, swe-assistant skill).
- Claim: Intellectual lineage: Richard Cook's "How Complex Systems Fail" (proposition 8: hindsight bias as the primary obstacle to accident investigation), Sidney Dekker's "Just Culture," James Reason's systems approach; transplanted from safety-critical industries (aviation NTSB, medicine M&M conferences) into software. Label: **Corroborated** — multiple secondaries.
- Claim: The practice includes the "Second Story" — digging into the circumstances and environment the engineer was in, asking "why did the fix appear correct at the surface?" Label: **Corroborated** — production-framework research notes quoting Allspaw.
- Claim: Known tension: Allspaw treats *action items as a non-goal* of the learning review; Google's SRE book makes them *mandatory*. Teams must decide where they land. Label: **Corroborated** — kipi-system research notes. Lesson: the point of the ritual (learning vs accountability) must be explicit or it degrades into compliance theater.
- Claim: Counterfeit signal: organisations that say "blameless" but deliver "sanctionless" (no punishment, but blame still assigned) — "people can tell the difference, and it determines what they tell you." Label: **Corroborated** — tech-operator-crm-cards (citing the STELLA report).

### Deployment
- Claim: Etsy went from fragile deployments and outages to 50+ deploys per day via CI/CD automation, with engineers trusted to ship and a culture of learning over blame. Label: **Corroborated** — em360tech DevOps culture survey (secondary). The "50 deploys/day" figure is widely repeated; treat the exact number as era-specific (early 2010s).
- Claim: The deploy pipeline included guardrails that made speed safe (one-click rollback is cited as a canonical action item from an Etsy deploy-failure postmortem). Label: **Corroborated** — lev-os blameless-postmortems skill (secondary).

### Monitoring / incident response
- Claim: Etsy's postmortem template and culture were adopted into Google's SRE book (chapter 15, Postmortem Culture) — the Allspaw-derived template became industry standard. Label: **Corroborated** — swe-assistant skill + cto-curriculum resources.

### Documented failures
1. Etsy homepage-down bad deploy (early era): blameless finding was missing rollback automation + new on-call engineer; action items were one-click rollback, better on-call onboarding, expanded deploy checklist. Label: **Corroborated** (secondary); the incident predates the 2012 essay and is presented as a motivating example.

### Transferable lessons
- Blamelessness is an *information* strategy: the alternative to blamelessness is concealment, and concealment costs more than any individual error. Label: **Corroborated**.
- Ask "what made this possible?" not "who caused this?" — and mean it; sanctionless-but-blameful is detectable by engineers. Label: **Corroborated**.
- Deploy frequency is a cultural outcome (trust + automation + learning), not a tooling purchase. Label: **Corroborated**.
- Decide explicitly whether postmortems produce action items (Google) or pure learning (Allspaw) — ambiguity produces theater. Label: **Corroborated**.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| ET-01 | Allspaw origin, lineage (Cook/Dekker/Reason), action-item tension | https://github.com/assafkip/kipi-system/blob/HEAD/q-system/research/code-rca-resources-2026-06-02.md | Secondary (research synthesis) | assafkip | 2026 | 2026-10-10 | Medium |
| ET-02 | Just culture, sanctionless-vs-blameless, STELLA | https://github.com/raphaelthomas/tech-operator-crm-cards/blob/HEAD/learn/blameless-postmortem.md | Secondary (learning cards) | raphaelthomas | 2026 | 2026-10-10 | Medium |
| ET-03 | Second Story concept, Allspaw quotes | https://github.com/atyab124/production-framework/blob/HEAD/docs/research/decision-d-b-root-cause-vs-symptom-2026-04-30.md | Secondary (research notes) | atyab124 | 2026 | 2026-10-10 | Medium |
| ET-04 | 50 deploys/day, fragile-to-automated arc | https://em360tech.com/tech-articles/building-devops-culture-challenges-and-successful-stories | Secondary (survey) | em360tech | 2026 | 2026-10-10 | Low-medium |
| ET-05 | Blameless postmortem maturity, Etsy deploy-failure example | https://github.com/lev-os/agents/blob/HEAD/skills-db/thinking/patterns/blameless-postmortems/SKILL.md | Secondary (skill) | lev-os | 2026 | 2026-10-10 | Low-medium |
| ET-06 | Cloudflare/AWS 2025 postmortem close reading | https://www.sherlocks.ai/blog/blameless-postmortems-explained-lessons-from-real-outages | Secondary (essay) | Sherlocks AI | 2026 | 2026-10-10 | Low-medium |

## Narrative audit (retrofit 2026-10-10)
- **"Blameless" is really "sanctionless" — and that's the point.** Allspaw's formulation is often softened to "don't blame"; the sharper reading is that Etsy *removed sanctions* for surfacing failure, which is what made reporting honest. Blamelessness isn't kindness — it's an *information-extraction* strategy. Teams copying the ritual without removing career consequences get theater.
- **Deploy-on-day-one depends on the architecture.** Etsy's continuous deployment (and the "deploy your first day" ritual) works because of the machinery underneath: atomic deploys, feature flags, fast rollback. The *culture* is downstream of the *architecture*. Copying "deploy early" without the safety machinery is how you get Knight Capital (file 16).
- **Does the culture outlive its founders?** Etsy's engineering influence peaked in the Allspaw era (2009–2015). The general test of any culture claim: does it survive the people who built it? Partially unknown here — and the question applies to every "culture" case in this workstream.
