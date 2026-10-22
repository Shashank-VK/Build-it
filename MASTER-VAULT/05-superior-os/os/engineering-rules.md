# Solo AI Product Engineering System v1.0
# Engineering Rules and Anti-Patterns

## The 10 Rules

1. Write the appetite BEFORE the solution. [Basecamp / Shape Up]
2. Write the press release BEFORE the spec. [Amazon / Working Backwards]
3. Non-Goals must have at least 2 explicit items. [Google design doc culture]
4. Every design decision requires at least 1 rejected alternative documented. [Google design docs]
5. Document known-bad approaches (Rabbit Holes) BEFORE implementation. [Basecamp / Shape Up]
6. Write a design note for any change requiring >1 day or touching an external interface. [Google]
7. Uphill (uncertain) scopes are worked BEFORE downhill (clear) scopes. [Basecamp / Hill Chart]
8. Pre-commit the rollback threshold BEFORE deploying. [Netflix]
9. Every incident above defined severity gets a 3-section postmortem with dated corrective actions. [Google SRE]
10. AI-generated code in HIGH-STAKES paths requires independent human re-implementation + comparison. [high-stakes isolation]

## The 5 Anti-Patterns (explicitly named, not just implied)

- DESIGNING FOR SCALE YOU DON'T HAVE YET. [solo risk: premature architecture]
- MIXING REFACTORING WITH FEATURE WORK IN THE SAME TASK. [solo risk: self-enforce separation]
- ENORMOUS PRs. [solo risk: self-enforce small PRs]
- TREATING "THE AI SAID SO" AS A PRIMARY SOURCE. [solo risk: no published AI correctness metrics]
- FILING A POSTMORTEM WITHOUT TRACKING CORRECTIVE ACTIONS IN THE PROJECT TASK LIST. [solo risk: untracked actions]

## Loop Engineering Anti-Patterns

- INFINITE AGENTIC LOOPS (IALs): structural failure where feedback paths trigger without termination condition. [IALs]
- SELF-CERTIFICATION: agent declares completion via text without a deterministic external gate. [self-certification / evidence-carrying termination]
- ON-THE-FLY SYNTHESIS: real-time improvisation that bypasses rigorous SE processes. [on-the-fly synthesis]
- SAME-CONTEXT SELF-REVIEW: asking AI to review its own work in the same context = reviewer collusion, inherits own blind spots. [same-context review]

## Bureaucracy Discarded (real org practices that do NOT apply solo)

1. Narrative meeting: the scheduled multi-stakeholder PR/FAQ review assembly. KEEP the PR/FAQ; DISCARD the meeting.
2. Betting Table meeting: scheduled group decision on which pitches proceed. KEEP the Pitch + appetite; DISCARD the meeting.
3. Cross-stakeholder Non-Goals sign-off meeting: Non-Goals committed by solo developer personally; no meeting.
4. Full technical design doc for implementation details: implementation decisions live in Build Log, not a separate spec.
5. LCE team as separate organizational unit: the Launch Checklist artifact is what matters; solo developer administers it.
6. Readability Certification program: locked style guide + automated linting is the equivalent.
7. Kayenta-scale canary analysis infrastructure: pre-committed rollback threshold + 10-minute window is the solo equivalent.
8. Cross-org postmortem sharing ceremony: postmortems stored in git repository, searchable; no sharing meeting.
9. Formal senior engineer sign-off program: stakes-tiering (high/medium/low) + independent re-implementation for high-stakes replaces it.
