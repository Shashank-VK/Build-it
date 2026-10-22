# Solo AI Product Engineering System v1.0
# Product Development Lifecycle — Solo AI Product Engineering System

## Complete Sequence (idea to deprecation)

IDEA
 ↓
[Gate 1: Appetite Check] Set appetite (days/hours) BEFORE defining the solution. No appetite = no proceed.
 ↓
PR/FAQ DRAFT: One-page press release from customer perspective + 3 hard FAQ answers. AI drafts, human iterates.
 ↓
[Gate 2: Press Release Passes] AI skeptical-customer challenge must not destroy the value proposition.
 ↓
PITCH DOCUMENT: Problem, Appetite, Solution (breadboards/sketches), Rabbit Holes, No-gos (minimum 3).
 ↓
[Gate 3: Pitch Self-Approval] Can I actually build this within the appetite? Do I bet on it? Human decides.
 ↓
LIGHTWEIGHT DESIGN NOTE (required if: >1 day effort, external interface change, OR irreversible decision)
  Sections: Context, Goals, Non-Goals (min 2), Design, Alternatives Considered (min 2), Rabbit Holes, Cross-cutting Concerns
 ↓
[Gate 4: Design Note FCAR] Fresh-context adversarial review against locked rubric. Any fail = revise first.
 ↓
LAUNCH CHECKLIST PRE-CHECK: 8-item checklist verified before any implementation begins.
 ↓
IMPLEMENTATION: Work uphill (uncertain) scopes FIRST. Maintain build log. Each PR goes through Gate 5.
 ↓
[Gate 5: Per-PR Quality Gate] Automated linting (hard veto) + AI style review (soft) + stakes-tiered human review.
 ↓
SECURITY/RELIABILITY CHECK: Tiered by stakes (low/medium/high — see quality-security.md).
 ↓
[Gate 6: Launch Checklist Complete] All 8 items pass before ANY deploy. No exceptions.
 ↓
DEPLOY: Staged. 10-minute observation window. Rollback threshold pre-committed BEFORE deploying.
 ↓
MONITORING: Error rate + latency alerts configured BEFORE launch, not after.
 ↓
EXPERIMENT: If A/B applicable — hypothesis and success metric defined BEFORE test, not after.
 ↓
POST-LAUNCH REVIEW: Weekly. Check metrics vs launch-day baseline.
 ↓
[On incident] POSTMORTEM: 3 sections — timeline, Five-Whys root cause chain, corrective actions with due dates.
 ↓
ITERATION: Re-enter at Pitch stage for next scope of work.
 ↓
DEPRECATION: Criteria defined upfront — "I will deprecate if [X] by [date]."

## Sources
PR/FAQ: Amazon (Working Backwards, Bryar & Carr 2021)
Pitch, No-gos, Appetite, Circuit Breaker, Scope Hammer: Basecamp (Shape Up, Ryan Singer)
Design Note, Non-Goals, Alternatives Considered: Google (industrialempathy.com, Malte Ubl)
Launch Checklist: Google SRE book series
Staged deploy + pre-committed rollback: Netflix (Netflix TechBlog)
Postmortem (3-section + Five Whys): Google SRE + Amazon COE (Correction of Errors)
Loop Engineering: Addy Osmani (June 2026), ReAct (Yao et al. ICLR 2023), ECT (arXiv:2608.23623)
