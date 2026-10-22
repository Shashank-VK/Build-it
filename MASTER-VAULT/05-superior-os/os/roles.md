# Solo AI Product Engineering System v1.0
# Role/Responsibility Model

## Delegation Taxonomy

### Human-Only (never delegate these)
- Setting the appetite before defining the solution
- Circuit breaker enforcement (kill/pause/pivot final call)
- Finalizing and committing to corrective actions from postmortems
- Classifying decisions as reversible vs. irreversible
- Final implementation of high-stakes code paths (independent re-implementation required)
- Approving any waiver of a Gate requirement

### AI-Assisted (AI drafts, human approves)
- PR/FAQ first draft + skeptical-customer critique
- Pitch document drafting
- Non-Goals generation (human commits to minimum 2 explicit items)
- Alternatives Considered generation (AI generates 1-2 real contenders; human rejects with reasons)
- Design note first draft
- Failure mode analysis (top-3 per external integration)
- Launch checklist verification
- Deployment metric monitoring and alert

### AI-First-Human-Approved (AI leads, human validates output)
- Style review against locked rubric (code review soft gate)
- Postmortem first draft (3-section structure)
- Corrective action item generation

### Automated (no human in the execution loop)
- Linting (hard gate — blocks merge on failure, no override)
- CI test suite (hard gate — blocks merge on failure, no override)
- Deployment metric gate (triggers rollback at pre-committed threshold automatically)
- Scope gate check (new task against Non-Goals list)
- Pre-tool guard script (security check before every tool execution)

## The 9 Named Workflows

| # | Workflow | Trigger | AI Role | Human Role |
|---|----------|---------|---------|------------|
| 1 | Working Backwards | New idea | Draft PR/FAQ + skeptical-customer challenge | Iterate; approve |
| 2 | Scope Gate Check | New task proposed | Check task against Non-Goals list | Decide: add / reject / revise Non-Goals |
| 3 | Alternatives Generator | Before any design decision | Generate 1-2 real alternatives (NOT strawmen) | Reject with reasons; commit to chosen |
| 4 | Failure Mode Analyzer | Before any external integration | List top-3 failure modes + user-visible impact | Decide which to prevent vs. tolerate |
| 5 | Launch Checklist Runner | Before every deploy | Check project state against 8-item checklist | Resolve any gaps |
| 6 | Deployment Monitor | Immediately post-deploy | Watch pre-defined metric; alert if threshold crossed | Roll back if alerted (no deliberation) |
| 7 | Postmortem Opener | Any incident above defined severity | Generate 3-section postmortem draft | Correct; commit corrective actions |
| 8 | Stakes Classifier | Before implementing any code | Classify path as low/medium/high-stakes | Apply corresponding review tier |
| 9 | Unknown-First Sorter | Start of any implementation cycle | Identify uphill vs. downhill scopes | Work uphill scopes first |
