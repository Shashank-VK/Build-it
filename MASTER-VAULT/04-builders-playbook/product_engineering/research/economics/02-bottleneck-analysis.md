# Bottleneck Analysis: Where AI Moves the Constraint
**Does automation remove bottlenecks or shift them? Baseline comparisons.**
Atlas research · workstream: economics · 2026-10-10

## The central finding (Corroborated)

AI coding tools compress the *implementation* step of software delivery while the steps
around it — specification, review, testing, integration, security, deployment, operation —
absorb the freed capacity and then some. The bottleneck does not disappear; it migrates
downstream, from "writing the code" to "proving the code is safe to ship." Multiple
independent evidence streams converge on this:

1. **Volume rises faster than completion.** Feature-branch throughput +7.7% YoY while
   main-branch throughput stays flat; PRs/author +20% YoY while incidents/PR +23.5% and
   change failure +~30% (Cortex 2026). More work enters the pipe than exits it.
2. **Review becomes the narrow part.** Merged PRs up 98% where AI adoption is high while
   review time rises 91% (Faros AI); AI PRs wait 4.6× longer before first review (LinearB);
   human-review coverage of AI PRs fell 89%→68% in one tracked company.
3. **Stability falls as throughput rises.** DORA 2024: +25% AI adoption → −1.5% throughput,
   −7.2% stability. DORA 2025: throughput sign flips positive, stability stays negative —
   "speed without stability is accelerated chaos." DORA's own reading: "teams are adapting
   for speed before their underlying systems have caught up."

DORA 2025's framing, from the primary Google Cloud announcement: AI is "an amplifier of
the systems already surrounding a team" — strong teams get faster, struggling teams get
faster at producing mess — and the report explicitly recommends **value-stream mapping**
to find where work waits between idea and customer delivery.

## The delivery pipeline, stage by stage

Think of delivery as six stations. For each: what AI did to it, and where the queue formed.

### 1. Specification — "what should we build?"
**Plain English:** turning a customer need into a precise-enough description that code can
be written against it.

- **Effect (Inferred):** AI barely touches this stage — DORA 2025 found AI is used mostly
  for writing/modifying/debugging code, *least* for requirements analysis, planning, and
  architecture. Practitioner consensus (multiple secondary sources): as generation gets
  cheap, the value of precise specification *rises*, because the agent can only build what
  was specified. No controlled measurement of spec quality or spec time under AI adoption
  was found (**Unknown**).
- **Bottleneck status:** unchanged or relatively more binding — specification errors now
  get *amplified* into code faster (Amazon logistics incident, Mar 2026: an AI change
  following an outdated wiki corrupted delivery estimates for 6.3M orders in six hours;
  the code compiled and passed tests — a specification/context failure, not a coding one).

### 2. Implementation — "write the code"
**Plain English:** the typing-and-thinking step. The one step AI directly accelerates.

- **Effect (Verified, with task-type dependence):** +55% on a greenfield toy task (Peng
  2023); +26% completed tasks in real enterprise work (Cui 2025); −19% for experts in
  mature codebases (METR 2025); +24% merged PRs with agentic CLI tools (Microsoft 2026).
  DX aggregates: median +7.7% PR throughput, "nobody hit 2x, 5x, or 10x."
- **Bottleneck status:** removed as the binding constraint for most teams. Devaland's
  91-day measurement found programming estimates "too high by a factor of tens" — a
  "two focused days" task took 10 minutes of actual programming. The items that took days
  were stuck *outside* the code: client material, sign-offs, acceptance, verification.

### 3. Review — "is this correct and safe?"
**Plain English:** human (or automated) checking before merge.

- **Effect (Corroborated):** the single best-documented bottleneck shift. Review time +91%
  (Faros AI); AI PRs wait 4.6× longer pre-review (LinearB); PRs 154% larger; 38% of
  developers say reviewing AI code takes more effort than a colleague's (Sonar); only 48%
  always check AI code before committing. Anthropic's asymmetry: users reject 3% of
  individual agent commands but 39% of presented plans.
- **Structural reason (Inferred):** verification scales with *output volume × output
  unfamiliarity*. AI increases both simultaneously — more code, written by no one, in
  styles the reviewer didn't choose. Review is cognitively harder than writing for the
  same change, and AI widened the gap between the two.
- **Bottleneck status:** **the new binding constraint** for most AI-adopting teams.

### 4. Testing & integration — "does it work together?"
**Plain English:** CI pipelines, integration tests, merging without conflicts.

- **Effect (Corroborated/Inferred):** "AI produces pull requests faster than CI pipelines
  can process them" — teams handling dozens of PRs/day now face hundreds, with testing
  backlogs lasting days (secondary reporting on the 2026 State of Software Delivery).
  Main-branch success rates at 70.8%, a five-year low vs a 90% benchmark (single
  secondary source — **unverified**, direction consistent with incident data).
  Cortex: incidents/PR +23.5% YoY; change failure +~30%.
- **Bottleneck status:** binding wherever test automation and integration maturity lag
  behind generation speed. DORA 2025: "without robust control systems — strong automated
  testing, mature version control, fast feedback loops — an increase in change volume
  leads to instability."

### 5. Security & compliance — "is it allowed to ship?"
**Plain English:** vulnerability scanning, security review, policy gates.

- **Effect (Mixed):** Veracode: 45% of AI-generated code contains an OWASP Top-10 issue
  (2025); Summer 2026 retest: 56% average security pass rate across 11 frontier models.
  LaunchDarkly: 91% of engineers have low trust shipping AI code; 81% ship with
  unresolved risks. **Counterevidence:** Kraishan 2026's in-the-wild data shows agent PRs
  *less* likely to contain security smells than human PRs (OR 0.63) — lab-generated code
  and reviewed agent PRs are different populations.
- **Bottleneck status:** binding as a *risk* bottleneck even where it isn't a *time*
  bottleneck — teams ship with unresolved risks under delivery pressure, converting a
  review queue into production incidents.

### 6. Deployment & operation — "is it healthy in production?"
**Plain English:** release, monitoring, incident response, maintenance.

- **Effect (Corroborated):** incidents per PR rising (+23.5% YoY per Cortex; +242.7% over
  two years per Faros.ai's DORA-dataset analysis — magnitude needs primary verification).
  New Relic 2026: 78% of leaders saw AI-tied incident spikes; 82% had ≥1 major
  AI-attributed production failure in six months; 86% report more senior-engineer time on
  emergency fixes. Lightrun 2026: 43% of AI changes needed manual production debugging
  *after passing QA/staging*.
- **Maintenance debt (Corroborated):** GitClear: refactoring share of changes 21%→<4%;
  legacy maintenance −74%; duplication +81%. The maintenance burden compounds — today's
  generated code is tomorrow's legacy code, and it is being generated faster than ever.
- **Bottleneck status:** the *deferred* bottleneck — costs arrive quarters later as
  incidents and maintenance load.

## Baseline comparisons: before vs after

| Stage metric | Pre-AI baseline | AI-era reading | Source class |
|---|---|---|---|
| Flow efficiency (active ÷ elapsed) | 5–20% typical | Unmeasured in AI era; proxies worsen | Community / Unknown |
| Code review time | Baseline | +91% where AI adoption high | Vendor benchmark (Faros AI) |
| PR size | Baseline | +154% | Secondary reporting |
| PR acceptance (AI vs human) | 84.4% human | 32.7% AI-generated | Vendor benchmark (LinearB) |
| Time to first review (AI PRs) | — | 4.6× longer wait; 12.6h median (Claude Code) | Vendor / academic |
| Change failure rate | Baseline | +~30% YoY | Vendor benchmark (Cortex) |
| Incidents per PR | Baseline | +23.5% YoY | Vendor benchmark (Cortex) |
| Delivery stability (DORA) | Baseline | Negative relationship with AI adoption, 2 yrs running | Primary technical (DORA) |
| Delivery throughput (DORA) | Baseline | Negative (2024) → positive (2025) | Primary technical (DORA) |
| Refactoring share of changes | ~21% (2022) | <4% (2026) | Primary technical (GitClear) |
| Code duplication | 40/1M lines | 73/1M lines (+81%) | Primary technical (GitClear) |
| Human review coverage of AI PRs | 89% | 68% (one tracked company) | Secondary |
| Main-branch success rate | ~90% benchmark | 70.8% (five-year low) | Single secondary — unverified |

**Reading note:** baselines are rarely from the same population as the AI-era reading
(different companies, different years). Treat the table as directionally consistent
evidence, not a controlled before/after.

## When the bottleneck does NOT shift (the amplifier finding)

DORA 2025's most important result is a moderator, not a main effect: AI amplifies the
system it lands in. The seven capabilities that flip AI from harm to help — clear AI
stance, healthy data ecosystem, AI-accessible internal data, strong version control,
small batches, user-centric focus, quality internal platforms — are all *pre-existing
engineering disciplines*. Concretely:

- **Small batches + fast feedback + strong tests** → the extra volume flows through
  without destabilizing (Microsoft's internal AI code review: >90% of PRs touched,
  completion times −10–20%).
- **Standardized, low-judgment work** → near-zero human intervention is achievable
  (Spotify: 2.5M maintenance PRs auto-merged over 18 months, humans on exceptions only).
- **Mature codebases + expert developers** → AI can slow the work down (METR −19%);
  gains concentrate in greenfield, boilerplate, and less-experienced developers (Cui et
  al.; Peng et al.; DX: juniors use AI most at 41.3% daily, seniors save more time per
  use because they judge output better).

The honest summary: **AI removes the implementation bottleneck and promotes the
verification bottleneck.** Teams that had already industrialized verification (tests,
review discipline, platforms, small batches) capture the gain. Teams that had not get
faster at generating the rework, incidents, and technical debt they were already
producing — "accelerated chaos."

## What "removing" a bottleneck would actually require

A bottleneck is removed only when the *binding* constraint on customer lead time moves.
For AI to do that, the evidence implies all of the following must be true at once —
none is established by any single study:

1. Specification quality keeps pace with generation speed (unmeasured).
2. Review capacity (human + automated) scales with PR volume (currently shrinking in
   coverage terms).
3. Test automation and CI throughput scale with change volume (lagging per all
   incident data).
4. Rework and churn stay flat or fall (currently rising).
5. Maintenance keeps pace with the larger, more duplicated codebase (currently falling:
   refactoring −70%, legacy maintenance −74%).

Until then, "AI made us faster" claims should be read as "AI made *coding* faster" —
a local optimization of a step that was, for most teams, ~15% of the delivery timeline.
