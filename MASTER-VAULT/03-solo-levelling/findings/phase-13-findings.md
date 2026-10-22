# Phase 13 — Compression: Company Process → Solo + AI Equivalent — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

**Structure:** Pass 13.1 covers Phases 2–7 (idea through security/reliability review). Pass 13.2 covers Phases 8–12 (implementation through AI's documented role). Every row is traced to a specific phase, org, and question entry.

---

## Pass 13.1 — Phases 2–7: Idea → Architecture and Security/Privacy/Reliability

---

**Row 1**
[Source: Phase 2, Amazon, Q1]
Company process: PR/FAQ requires a 1-page press release written from the customer's perspective before any resource commitment. Every PR/FAQ requires review at a "narrative meeting" where the document is read silently and critiqued.
Underlying principle: A decision isn't real until it's written as if it were done — writing forces precision and exposes vagueness that conversation hides.
Failure it prevents: Starting build on a vague idea; discovering mid-build that the product hypothesis was never clearly stated.
Does a solo developer have this failure mode: YES — acutely. A solo developer has no narrative meeting forcing the discipline.
Solo equivalent: Write a one-page press release for any non-trivial project before writing a line of code. Read it aloud. If the customer benefit isn't clear in the first paragraph, the idea isn't ready.
AI equivalent: Use AI to draft the press release from a bullet-point idea, then use AI playing "skeptical customer" to challenge every sentence. Iterate until no obvious holes remain.
Human vs AI Delegation Boundary: AI-assisted — AI drafts and critiques, human finalizes and commits.
Automation/agent/MCP opportunity: A "Working Backwards" agent workflow that turns a raw idea into a draft press release + 3 critical customer questions automatically.
Bureaucracy to discard: The formal narrative meeting attendance, multi-stakeholder scheduling, and iterative revision cycles (the process cost of persuading a room) — a solo developer has no room to schedule. The discipline of writing the press release survives; the meeting format does not.

---

**Row 2**
[Source: Phase 2, Basecamp, Q1]
Company process: Basecamp's "Pitch" format requires five sections before a bet is placed: Problem, Appetite, Solution, Rabbit Holes, No-gos.
Underlying principle: The appetite (time budget) must be set before the solution, not after — otherwise the solution expands to fill whatever time is available.
Failure it prevents: Scope creep starting from the idea stage; building a solution without agreeing on how much time it's worth.
Does a solo developer have this failure mode: YES — severely. Without an appetite decision, a solo project can consume indefinitely.
Solo equivalent: For any project, write the appetite first (how many days/hours is this idea worth?), then define the solution within that budget.
AI equivalent: Have AI generate a "minimum viable solution that fits a [N-day] appetite" prompt rather than "the best solution" — forcing budget-first thinking.
Human vs AI Delegation Boundary: Human decides the appetite (only the human knows their real time constraints); AI assists with fitting the solution to it.
Automation/agent/MCP opportunity: A "Pitch Checker" that takes a written solution and challenges it against the stated appetite: "Does this realistically fit in [N] days for a solo developer?"
Bureaucracy to discard: The Betting Table decision meeting. A solo developer is the betting table — the decision is: "do I commit to this or not?" The artifact (the Pitch document) survives; the meeting format does not.

---

**Row 3**
[Source: Phase 3, Google, Q2 and Q3]
Company process: Google design docs include an explicit "Non-Goals" section. Once written, the Non-Goals section shifts the burden of proof for scope additions to the person requesting the addition.
Underlying principle: What you explicitly exclude is as important as what you include — an unstated exclusion is an implicit permission.
Failure it prevents: Scope creep during build; "while we're at it" feature additions that weren't agreed to; relitigating exclusion decisions.
Does a solo developer have this failure mode: YES — especially bad solo because there's no external check. The solo developer can convince themselves any addition is justified.
Solo equivalent: Every project document must have a "Not in this version" section with at least 3 items explicitly listed. Any scope addition must be measured against this list first.
AI equivalent: Before implementation begins, ask AI: "What are 5 things someone might expect this to do that it intentionally won't do? List them." Use AI's output as the starting Non-Goals list.
Human vs AI Delegation Boundary: AI-assisted for generation; human finalizes and commits.
Automation/agent/MCP opportunity: A "scope gate" check built into the task workflow: before adding any new task, the system asks "Is this in the agreed Non-Goals list?"
Bureaucracy to discard: The cross-stakeholder review of the Non-Goals section (getting multiple teams to sign off). The solo equivalent is writing and committing to it personally — no meeting needed.

---

**Row 4**
[Source: Phase 3, Basecamp, Q3]
Company process: Basecamp's three-layer enforcement against scope creep: No-gos (pre-build exclusion list), Scope Hammer (active mid-build questioning: "is this a must-have?"), Circuit Breaker (hard deadline — project stops, not extends).
Underlying principle: Scope discipline requires three mechanisms operating at different stages — pre-build exclusion, mid-build active cutting, and a hard time boundary that makes unlimited extension impossible.
Failure it prevents: Scope expanding at each of three stages: before build (No-gos prevent it from entering), during build (Scope Hammer cuts it), and at the deadline (Circuit Breaker stops the bleed).
Does a solo developer have this failure mode: YES at all three stages.
Solo equivalent: (1) No-gos at pitch stage. (2) A weekly "must-have test" for every open task: "Can I ship without this? Yes or No?" (3) A personal circuit breaker: a pre-committed date after which the current version ships as-is, regardless of what isn't done.
AI equivalent: AI runs the weekly must-have test: "Here are my open tasks. Tell me which ones are genuinely blocking a shippable version and which aren't."
Human vs AI Delegation Boundary: AI-assisted for the must-have test; human sets and enforces the circuit breaker date.
Automation/agent/MCP opportunity: A "ship date enforcer" — a scheduled agent that checks open tasks against the circuit breaker date and flags any that would blow the deadline.
Bureaucracy to discard: The formal Betting Table involvement in circuit breaker enforcement (returning unfinished projects to the shaping queue). A solo developer simply ships what's done and starts a new pitch for the rest.

---

**Row 5**
[Source: Phase 4, Google, Q2 and Q4]
Company process: Google design docs require an "Alternatives Considered" section. Rejected alternatives and their specific rejection reasons are preserved in the same document as the chosen approach.
Underlying principle: A decision isn't trustworthy unless real alternatives were seriously weighed and specifically rejected for stated reasons.
Failure it prevents: Relitigating rejected approaches months later; anchoring on the first workable idea without checking for better ones.
Does a solo developer have this failure mode: YES — acutely. No colleague to ask "did we consider X."
Solo equivalent: Before implementation, write at least 2 rejected alternatives with specific rejection reasons. (See also Phase 13 worked example in the spec.)
AI equivalent: AI generates 2–3 genuinely different alternative approaches before a design decision is committed to.
Human vs AI Delegation Boundary: AI-assisted — AI generates alternatives, human rejects with reasons.
Automation/agent/MCP opportunity: A "devil's advocate" planning step run automatically before implementation begins on any non-trivial decision.
Bureaucracy to discard: The formal committee review Google may attach to this section. A solo developer doesn't need a meeting — they need to write the alternatives down.

---

**Row 6**
[Source: Phase 4, Basecamp, Q2 and Q3]
Company process: Basecamp's Pitch document includes "Rabbit Holes" — a named section for technical or design complexities considered and rejected. The specific example: "notifications per message" considered and rejected in favor of "notifications per thread."
Underlying principle: Pre-implementation exploration of known-bad paths prevents the team from rediscovering them expensively during build.
Failure it prevents: Spending build time on known-bad approaches that the shaper already considered and ruled out.
Does a solo developer have this failure mode: YES — repeatedly. Solo developers often "rediscover" the same dead-end approaches because they didn't document them the first time.
Solo equivalent: Rabbit Holes section in the Pitch/PRD: "Things I considered and already know are bad, with the specific reason." Minimum: 1 item before any implementation.
AI equivalent: Ask AI: "What are the obvious-seeming approaches to [problem] that have known failure modes? List them and explain why they fail."
Human vs AI Delegation Boundary: AI-assisted — AI lists known failure modes, human confirms from their specific context.
Automation/agent/MCP opportunity: A "dead-end library" — a searchable log of rejected approaches with reasons, so the same rabbit hole isn't re-explored in future similar projects.
Bureaucracy to discard: None — this practice scales down to zero overhead. Even a solo developer adding one rabbit hole note takes two minutes.

---

**Row 7**
[Source: Phase 5, Google, Q1 and Q6]
Company process: Google design docs have a defined trigger (>10 engineering days, or >1 engineer, or significant API change) and a standard template structure (Context, Goals, Non-Goals, Design, Alternatives Considered, Cross-cutting Concerns).
Underlying principle: Threshold-gated documentation prevents both over-documentation (wasting time on trivial changes) and under-documentation (shipping complex decisions without a written plan).
Failure it prevents: Writing a design doc for every tiny change (process overhead kills velocity) OR never writing them (complex decisions become untrackable).
Does a solo developer have this failure mode: YES — tends toward neither extreme (either obsessive over-documentation or zero documentation) without a calibrated threshold.
Solo equivalent: Define a personal trigger: any change requiring >1 day of focused work, or affecting an external interface, or making an irreversible decision, requires a lightweight design note (not a full doc — 200–500 words, the key sections only).
AI equivalent: AI writes the first draft design note from a brief; human edits to accuracy.
Human vs AI Delegation Boundary: AI-first-human-approved — AI drafts the note, human corrects and signs off.
Automation/agent/MCP opportunity: A "design note starter" — on creating a new project branch or task above a size threshold, the system auto-creates a design note template pre-filled with the task name, date, and blank Alternatives Considered section.
Bureaucracy to discard: The full design doc committee review cycle, multiple-week elapsed time, and formal "sign-off" language — a solo developer's design note is approved when the human writes the final version and begins implementation.

---

**Row 8**
[Source: Phase 5, Basecamp, Q1 and Q4]
Company process: Basecamp deliberately does not write technical design docs before implementation. Implementation is left to the 2-person team building within the 6-week cycle.
Underlying principle: Excessive upfront specification reduces implementer ownership and wastes planning time on details that change during build.
Failure it prevents: (From the other side) Over-documentation; planning paralysis; "design by committee" for implementation details.
Does a solo developer have this failure mode: PARTIALLY — solo developers don't have committee paralysis but can fall into analysis paralysis.
Solo equivalent: Don't write a technical design doc for implementation details — trust the build process. Write only the Pitch/PRD and let implementation decisions emerge. BUT: document significant decisions made during build in a running "build log" (one paragraph per significant decision, date-stamped).
AI equivalent: AI helps make implementation decisions as they arise during build — not planned upfront.
Human vs AI Delegation Boundary: AI-assisted for in-build decision making; human commits each decision.
Automation/agent/MCP opportunity: A "build log" template auto-started at the beginning of each implementation cycle.
Bureaucracy to discard: Detailed upfront technical design documents for implementation details — confirmed by Basecamp as over-engineering the planning process. Solo equivalent of "you build it, you run it" means the plan lives in your head and a lightweight log.

---

**Row 9**
[Source: Phase 6, Amazon, Q2]
Company process: Amazon's Two-Pizza Team (6–10 people) bounds architectural scope by organizational structure — a team that can't coordinate across many teams is structurally prevented from taking on cross-team-dependency architecture.
Underlying principle: Small team size creates a forcing function for architectural simplicity — you can only build what your team can coordinate and operate.
Failure it prevents: Over-engineering for scale or cross-team dependencies that the team cannot actually support operationally.
Does a solo developer have this failure mode: YES — extremely. A solo developer can design for scale they'll never have, or build dependencies on systems they can't maintain.
Solo equivalent: Before designing any architecture, write: "What is the maximum number of users/requests/data volume I'll realistically have in 12 months?" and design for that number only, not a 10× headroom version.
AI equivalent: Ask AI to critique any architecture plan for over-engineering: "Is any part of this design for scale or flexibility I don't currently need? Specifically name it."
Human vs AI Delegation Boundary: AI-assisted — AI flags, human decides what to actually simplify.
Automation/agent/MCP opportunity: A "scale justification check" built into any architecture decision — before adding a queue, cache, microservice, or abstraction layer, require a written "why I need this now" answer.
Bureaucracy to discard: The formal ORR process (a team of reviewers checking operational readiness). A solo developer's ORR equivalent is: can I operate this myself, and do I know what to do when it breaks?

---

**Row 10**
[Source: Phase 6, Netflix, Q2]
Company process: Netflix's "designed for failure" philosophy — designing systems that survive component failure rather than designing to prevent all failure — functions as the anti-over-engineering mechanism.
Underlying principle: Building for resilience against failure is cheaper than building to prevent all failure; the former scales better and requires less upfront planning.
Failure it prevents: Premature abstraction to prevent hypothetical failures; massive upfront reliability engineering for scenarios that don't materialize.
Does a solo developer have this failure mode: YES — often builds "bulletproof" systems for failure modes that never happen while ignoring the ones that do.
Solo equivalent: Design for "what's the simplest thing that can fail gracefully?" rather than "what's the most robust thing I can build?" Default: every external dependency can fail; every third-party API will be unavailable; design with those assumptions rather than against them.
AI equivalent: AI runs "failure mode analysis": "Given this design, what are the three most likely ways this breaks in production? How would a user experience each one?"
Human vs AI Delegation Boundary: AI-assisted for failure mode enumeration; human decides which failure modes to tolerate vs. prevent.
Automation/agent/MCP opportunity: A "failure mode checklist" run before any integration with an external service.
Bureaucracy to discard: Chaos engineering at production scale (randomly killing services in production). Solo equivalent: design for graceful degradation in your code, not via external tooling.

---

**Row 11**
[Source: Phase 7, Google, Q1–Q3]
Company process: Google's LCE (Launch Coordination Engineering) team has a Launch Coordination Checklist covering architecture, capacity, monitoring, security, failover, and load testing. If the checklist can't be cleared, the launch doesn't proceed. The error budget is an automatic launch halt mechanism.
Underlying principle: A launch readiness checklist converts implicit reliability standards into a sequential binary test — each item either passes or fails, with no room for "good enough."
Failure it prevents: Launching a service that isn't actually ready for production load, monitoring, or failure recovery — and discovering this post-launch when the cost is higher.
Does a solo developer have this failure mode: YES — launches without a checklist almost always discover missing monitoring, missing error handling, or missing rollback plans after something goes wrong in production.
Solo equivalent: A personal Launch Checklist (minimum 8 items): monitoring set up, error rate alert configured, rollback plan tested, external dependencies healthy, API error handling complete, secrets not hardcoded, load tested at 2× expected volume, postmortem template ready.
AI equivalent: AI runs through the Launch Checklist against the current project and reports which items are not yet satisfied.
Human vs AI Delegation Boundary: AI-assisted — AI checks the current state against the checklist, human resolves any gaps before launching.
Automation/agent/MCP opportunity: A pre-launch gate agent: given a repository and a Launch Checklist, the agent checks each item and blocks deployment until all pass.
Bureaucracy to discard: The LCE team as a named, separate team of dedicated reviewers. A solo developer is the LCE team — the checklist artifact is what matters, not the organizational structure.

---

## Pass 13.2 — Phases 8–12: Implementation → AI's Documented Role

---

**Row 12**
[Source: Phase 8, Basecamp, Q1 and Q5]
Company process: Basecamp's Scopes (named units of work) + Hill Charts (uphill = figuring it out, downhill = making it happen) + Scope Hammer (mid-build cutting) form a complete implementation tracking system.
Underlying principle: A project's progress is better tracked by "how many unknowns remain?" than "how many tasks are completed?" — an unknown-first tracking model.
Failure it prevents: False confidence from task completion when the hard parts (the unknowns) haven't been addressed; discovering late that the hard parts were never figured out.
Does a solo developer have this failure mode: YES — acutely. Solo developers often track "tasks done" while the critical architectural unknowns sit unaddressed.
Solo equivalent: For any implementation: (1) List your scopes (independent shippable pieces). (2) For each scope, classify it as "uphill" (unknowns remain) or "downhill" (clear path to done). (3) Work on uphill scopes first — don't defer the scary parts.
AI equivalent: Use AI to identify the uphill scopes: "Here is my project. Which parts have open questions or unknowns that could block completion? Rank them by risk."
Human vs AI Delegation Boundary: AI-assisted for unknown-identification; human decides the order of attack.
Automation/agent/MCP opportunity: A "risk-first task sorter" — on planning a sprint, automatically surfaces the highest-uncertainty tasks first.
Bureaucracy to discard: The formal Hill Chart visual tool (requires specific Basecamp software). The underlying principle — "address unknowns first" — requires no tooling at all.

---

**Row 13**
[Source: Phase 9, Google, Q1 and Q4]
Company process: Google's Readability Certification — a named, seniority-independent review authority. A new readability mentor can reject a senior engineer's code for style violations. The style guide is the ultimate authority; reviewer preference beyond it is not grounds for blocking a merge.
Underlying principle: Review authority must be structurally independent of the author's seniority — otherwise review is social theater rather than a real check.
Failure it prevents: Senior-engineer code bypassing review based on deference; style drift where each senior engineer imposes personal preferences.
Does a solo developer have this failure mode: YES — in a different form. A solo developer reviewing their own code will defer to themselves. This is the "reviewer collusion" failure mode from Phase 14.
Solo equivalent: For code review: (1) A defined checklist (style guide + automated linting) that the human must pass regardless of how confident they feel. (2) A deliberate time-gap between writing and reviewing (minimum 24 hours for non-trivial changes). (3) AI as the readability reviewer — but from a fresh context window with no memory of why the code was written that way.
AI equivalent: AI readability review using a locked style guide as the reference — not "does this seem right" but "does this comply with the specific rules in [document]?"
Human vs AI Delegation Boundary: AI-first-human-approved — AI runs the review against defined rules, human resolves genuine ambiguities.
Automation/agent/MCP opportunity: An automated linting + AI style review gate that must pass before any PR is merged — even a PR by the solo developer to their own repository.
Bureaucracy to discard: The readability certification program (the human mentorship path, the formal certification grant). A solo developer uses a locked style guide + automated tools as the institutional equivalent.

---

**Row 14**
[Source: Phase 10, Netflix, Q1]
Company process: Netflix uses Canary + Red/Black + Kayenta Automated Canary Analysis (automated metric-gated progression) — authority to halt is encoded in automated gates, not human judgment calls.
Underlying principle: Rollout safety gates should be encoded in automated systems rather than relying on human judgment under pressure — humans under deployment pressure will rationalize away warning signs.
Failure it prevents: Rationalizing a warning metric away and proceeding with a bad rollout because "it's probably fine"; no human is reliably cautious under deployment pressure.
Does a solo developer have this failure mode: YES — the "it's probably fine" rationalization is an acute solo failure mode with no second opinion to check it.
Solo equivalent: Define deployment gates before deployment begins, when there's no pressure: "If [error rate] exceeds [X]% in the first 10 minutes, I roll back immediately, no exceptions." Write this down and commit to it before deploying.
AI equivalent: AI monitors the defined metrics during deployment and alerts immediately if any threshold is crossed — removes the human rationalization step.
Human vs AI Delegation Boundary: Automated — the gate criteria are pre-committed; AI/monitoring executes automatically; human rollback decision is constrained to "cross the line = rollback."
Automation/agent/MCP opportunity: A deployment gate agent that monitors a pre-defined metric set post-deploy and triggers automatic rollback if thresholds are breached.
Bureaucracy to discard: The Kayenta-scale infrastructure (a dedicated canary analysis service). A solo developer's equivalent: a 10-minute observation window post-deploy with a pre-committed rollback trigger at a defined error rate threshold.

---

**Row 15**
[Source: Phase 11, Google, Q2–Q4]
Company process: Google's blameless postmortem (named mechanism) + Shakespeare Sonnet++ example showing action items categorized as Mitigate, Prevent, and Process + action items tracked in the bug system + postmortem shared broadly.
Underlying principle: An incident is only useful if it permanently changes something — a filed-and-forgotten postmortem is worse than no postmortem because it creates false confidence.
Failure it prevents: The same failure recurring because the postmortem produced a document but no mechanism for tracking action items to completion.
Does a solo developer have this failure mode: YES — solo postmortems are typically "I'll remember not to do that" which has near-zero retention.
Solo equivalent: After any incident above a defined severity (anything that took >30 minutes to diagnose or caused user-visible downtime): write a 3-section postmortem — What happened (timeline), Root cause (chain to system, not self-blame), Corrective actions (named, date-committed). Add corrective actions to the project task list, not just the postmortem document.
AI equivalent: AI writes the first draft postmortem from an incident log/notes; human corrects; AI generates the corrective action items.
Human vs AI Delegation Boundary: AI-assisted — AI drafts, human commits to the corrective actions.
Automation/agent/MCP opportunity: A postmortem trigger and template agent: on a severity-qualifying event, automatically opens a postmortem document and prompts for the three required sections.
Bureaucracy to discard: The formal cross-organization postmortem sharing ceremony. A solo developer's equivalent: store postmortems in the project repository (git-tracked), searchable later.

---

**Row 16**
[Source: Phase 12, Amazon, Q4 and Phase 12 Summary]
Company process: Amazon's addition of senior engineer sign-off for Tier-1 AI-assisted code changes (an implicit acknowledgment that AI output requires additional review in high-stakes contexts). Phase 12's finding that no org publicly releases AI correctness metrics.
Underlying principle: AI-generated code is not equivalent to human-authored code in terms of review requirements — higher-stakes contexts require proportionally higher human oversight of AI output.
Failure it prevents: Treating AI code suggestions as trustworthy without additional review; assuming AI accuracy is verified because the tool is used internally.
Does a solo developer have this failure mode: YES — and worse, because there's no senior engineer sign-off available, and no internal data on how often the AI is wrong.
Solo equivalent: A tiered review rule for AI-assisted code: (1) Low-stakes (utility functions, boilerplate) — AI-first, cursory human review. (2) Medium-stakes (business logic, data handling) — AI-assisted, careful line-by-line human review. (3) High-stakes (security, payments, data integrity, external API changes) — AI-assisted draft only; human writes the critical paths independently and compares.
AI equivalent: AI generates the first draft; for high-stakes paths, a separate AI context (no memory of the original code) reviews the code against a requirements specification — not reviewing its own work.
Human vs AI Delegation Boundary: Human-only for high-stakes final implementation; AI-assisted for medium; AI-first for low.
Automation/agent/MCP opportunity: A "stakes classifier" that flags code as low/medium/high-stakes based on file path, module name, or explicit annotation, and enforces the appropriate review tier.
Bureaucracy to discard: The formal senior engineer sign-off program as an institutional process. The underlying principle (higher stakes = more human oversight) is what survives, applied through personal discipline and automated tiering.

---

## AI System Shape Decision (from row patterns)

Reviewing all 16 rows: the pattern that emerges across them is:

- **No rows require full autonomy** — every row has either "human decides" or "human approves" at some point.
- **Most rows are "AI-assisted" or "AI-first-human-approved"** — AI generates the first draft, runs the check, or flags the issue; human resolves.
- **Two categories of rows exist:** (a) Pre-build planning rows (Rows 1–11) where AI assists with drafting and critique, and (b) Build-and-operation rows (Rows 12–16) where AI assists with review and monitoring.
- **No row requires multiple specialized agents** — a single general-purpose AI with a defined workflow (prompted correctly) handles all rows.

**Shape conclusion:** The solo AI system should be **a single AI assistant operating within defined workflows, not a multi-agent system.** The workflows are the structure; the AI is the executor within them. Multiple specialized agents add coordination overhead that is bureaucracy for a solo operator. One agent, many named workflows.

Automation/agent opportunities (consolidated from all rows):
1. Working Backwards agent (PR/FAQ draft + customer critique)
2. Scope gate checker (Non-Goals vs new tasks)
3. Alternatives generator (devil's advocate before design decisions)
4. Failure mode analyzer (before integrations)
5. Launch Checklist runner (pre-deploy gate)
6. Deployment monitor (post-deploy metric gate)
7. Postmortem template opener (severity-triggered)
8. Stakes classifier for AI-assisted code review
9. Unknown-first task sorter (uphill scope identifier)

These 9 workflows are the skeleton of the Phase 15 AI Operating Model.

---

## "Bureaucracy to Discard" — Consolidated List (for Phase 15)

Every entry below must appear by name in Phase 15 Section 9 (Engineering Rules and Anti-Patterns):

1. Narrative meeting (scheduled multi-stakeholder assembly to review a PR/FAQ) → discard
2. Betting Table meeting (scheduled group to decide which pitches proceed) → discard
3. Cross-stakeholder Non-Goals sign-off meeting → discard
4. Full technical design document for implementation details → discard
5. LCE team as a separate named organizational unit → discard
6. Readability Certification program (human mentorship path) → discard
7. Kayenta-scale canary analysis infrastructure → discard
8. Cross-org postmortem sharing ceremony → discard
9. Formal senior engineer sign-off program as institutional process → discard

What survives from each discarded bureaucracy:
- The artifact (PR/FAQ, Pitch, Non-Goals list, Launch Checklist, Postmortem document) → survives
- The principle (write before committing, set appetite first, exclude explicitly, launch-ready gate, learn from failures) → survives
- The meeting/role/infrastructure created to enforce it at org scale → discarded
