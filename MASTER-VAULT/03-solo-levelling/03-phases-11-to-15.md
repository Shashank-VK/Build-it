# Solo AI Product Engineering System — Phases 11–15 (File 4 of 4)

Read `00-master-framework.md` first if you haven't already this session. Everything in it applies in full to every phase below.

---

## Phase 11 — Observability, Incident Response, and Postmortems

**Why this phase exists:** a postmortem that gets written and never changes anything is worse than no postmortem at all — it creates the appearance of learning without the substance of it, and gives false confidence that the same failure won't happen again. This phase exists to find whether these orgs' postmortem processes actually close the loop, or just produce a document.

**Objective:** Standard chain plus Lens 4 (Change Management). How incidents get detected and turned into a genuine, permanent process change, rather than a filed-and-forgotten document.

**Per-org research angles:**
- **Amazon:** investigate Amazon's known "Correction of Errors" (COE) process by name — this is a specifically documented, named Amazon mechanism worth prioritizing; check what its required sections are and whether action items have documented follow-through tracking.
- **Google:** the SRE book series has an entire well-known chapter on postmortem culture — this is one of the strongest, most specific public sources in the entire six-org set for this phase; prioritize it and extract the actual template structure it describes.
- **Meta:** investigate what's publicly known about Meta's incident-response tooling and postmortem practice, including any public accounts of specific high-profile Meta outages and how the postmortem was described afterward.
- **Netflix:** investigate how chaos engineering (deliberately injecting failure) interacts with postmortems — does routinely-induced failure change what counts as a "real" incident worth a formal postmortem, versus expected/absorbed failure?
- **Stripe:** investigate any public Stripe writing on incident response given the criticality of payment infrastructure uptime.
- **Basecamp/Linear:** investigate whether a formal blameless-postmortem process exists at this scale, or whether incident learning is handled more informally — again, a legitimate "informal, no formal template found" answer is acceptable.

**Exhaustive question set (per org):**
1. What triggers a formal postmortem — any incident above a severity threshold, any customer-visible outage, something else?
2. Who runs the postmortem, and is "blameless" a stated policy with an enforcement mechanism, or just an aspiration?
3. What is the actual output artifact, and is there a real, traceable example of a specific postmortem leading to a specific, verifiable process change?
4. How is a postmortem's action-item list tracked to completion — a real mechanism, or reliance on goodwill?
5. When priorities shift mid-incident-response, what's the actual re-prioritization process (Lens 4)?

**Common pitfall specific to this phase:** treating the existence of a postmortem template as evidence that the loop actually closes. The harder, more valuable finding is whether there's a real traceable instance of "incident happened → specific thing changed as a direct result" — a template alone doesn't prove that.

**Deliverable format — Per-Claim Documentation Format, applied per org:**
```
## [Org Name]

**Q1 — Postmortem trigger threshold:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q2 — Blameless policy and its enforcement:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q3 — Traceable example of postmortem causing a real process change:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q4 — Action-item tracking mechanism:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q5 — Mid-incident re-prioritization process (Lens 4):**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Evidence-density note:** ...
```

**Gate:** the exact path from "incident happens" to "a specific process changed as a result" is described for every org where evidence exists, with at least one concrete traceable example across the full set. Additionally, every claim above carries a complete Per-Claim Documentation trail (search queries used, named source, verification-pass result) per the Master Framework's Verification Protocol — a claim with a tag but no trail is treated as incomplete, and must be either finished properly or downgraded to `NOT FOUND`. No claim in this phase may rest on general reasoning about "how companies probably do this" presented as if it were a sourced finding.

---

## Phase 12 — AI's Documented Role and Verified Correctness Across the Lifecycle (public evidence only)

**Read this before starting, seriously:** this phase is, by design, the one most likely to come back thin, because internal AI tooling is treated by every one of these orgs as competitive infrastructure the same way a search-ranking algorithm is. A thin result here is the correct, honest outcome — not a sign the research failed. Resist the pull to upgrade a `[SPECULATIVE]` claim to `[INFERRED]` just because a fuller-looking phase feels better to produce.

**Objective — two parts.** First: where have these orgs *publicly* said AI fits into their own engineering lifecycle today (coding assistance, review automation, test generation, incident triage, documentation)? Second — the AI Evaluation dimension: how are they known, publicly, to check that AI output is actually correct — benchmarks used, disagreement rate against human reviewers, escaped-defect rate, success rate, cost, latency, hallucination-detection method?

**Per-org research angles:**
- **Amazon:** Amazon has publicly discussed internal use of AI coding assistance (including its own developed tooling) in various AWS re:Invent talks and blog posts — investigate the most recent public statements specifically, since this space moves fast and older claims may be stale.
- **Google:** Google has published research and blog content on AI-assisted code review and internal tooling — investigate Google's own published papers/blog posts on this specifically (distinct from Google's external AI products, which are a different thing from internal engineering tooling).
- **Meta:** investigate any public Meta engineering blog content on internal AI-assisted development tooling.
- **Netflix:** investigate whether Netflix has published anything specifically on AI use in its own engineering lifecycle (this may be one of the thinner entries — that's fine, say so).
- **Stripe:** investigate Stripe's public statements on AI use in its own engineering and support/review workflows.
- **Basecamp/Linear:** investigate whether either has published anything on internal AI tooling use — smaller companies are sometimes more candid publicly about tooling specifics precisely because it's not treated as as significant a competitive secret at their scale.

**Exhaustive question set (per org, applied to both parts of the objective) — each one uses the Per-Claim Documentation Format, with `NOT FOUND` expected to be a very common, entirely acceptable tag in this phase specifically:**

```
## [Org Name]

**Q1 — AI-assisted tooling publicly named/described:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q2 — Lifecycle stage(s) where AI use is publicly acknowledged vs. no statement either way:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q3 — How AI output correctness is publicly said to be measured:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Q4 — Public statements on AI-related incidents/failures:**
Claim: ...
Search queries used: ...
Source: ...
Verification pass: ...
Tag: ...

**Evidence-density disclosure (required, per org):** state plainly, in one line, roughly how much of this org's section landed as `[PRIMARY]` vs. `[INFERRED]` vs. `[SPECULATIVE]`/`NOT FOUND`. A disclosure reading "almost entirely NOT FOUND" is a correct, honest, complete answer for this phase — do not let the Per-Claim format's rigor tempt you into stretching a thin source into a fuller-sounding claim than it supports.
```

**Gate:** no claim in this phase is presented as more certain than its source supports. The evidence-density disclosure has been written honestly for every org, including orgs where it reads close to "almost entirely not publicly documented." Several lifecycle stages having no confirmed public answer, across most or all orgs, is an acceptable and correctly-reported outcome, not a phase to be reworked until it looks fuller. Additionally, every claim above carries a complete Per-Claim Documentation trail (search queries used, named source, verification-pass result) per the Master Framework's Verification Protocol — a claim with a tag but no trail is treated as incomplete, and must be either finished properly or downgraded to `NOT FOUND`. No claim in this phase may rest on general reasoning about "how companies probably do this" presented as if it were a sourced finding.

---

## Phase 13 — Compression: Company Process → Solo + AI Equivalent

**Why this phase exists — restated in full because this is the backbone phase:** this is the actual "10 → 3 → 1" step described in the original project brief. Every other phase exists to feed this one. If this phase is rushed, everything downstream (Phase 14's stress-test, Phase 15's final spec) inherits a shallow foundation no amount of later polish can fix.

**Structure — run as two internal passes, not two separate phases** (this split follows a real seam — pre-code versus code-and-beyond — not document type, so it isn't the artificial fragmentation the ground rules warn against):

**Pass 13.1 covers Phases 2 through 7** (idea through architecture and security/privacy/reliability review).
**Pass 13.2 covers Phases 8 through 12** (implementation through AI's documented role).

**Traceability requirement:** every row in this table must name which phase and which org's specific Per-Claim entry it's compressing (e.g. "from Phase 5, Google, Q1") — a compression row that can't be traced back to a specific documented claim is not compressing a finding, it's inventing one at the compression stage, which defeats the entire verification protocol this project depends on.

For every practice surfaced in the relevant phases, produce one full row of this chain:

`[Source: Phase X, Org, Qn] → Company process → underlying principle → failure it prevents → does a solo developer actually have that failure mode (yes/no/partially, with a one-line reason) → solo equivalent → AI equivalent → Human vs AI Delegation Boundary (human-only / AI-assisted / AI-first-human-approved / autonomous / automated) → automation/agent/MCP opportunity, if any → bureaucracy to discard, if any`

**Worked example row, to make the expected level of specificity unambiguous** (using the Phase 5 finding about Google design docs' "Alternatives Considered" section as the source practice):

```
Company process: Google design docs require an explicit "Alternatives Considered" section before architecture approval.
Underlying principle: a decision isn't trustworthy just because it wasn't challenged — it's trustworthy because real alternatives were seriously weighed and specifically rejected for stated reasons.
Failure it prevents: relitigating a rejected approach months later because nobody wrote down why it was rejected the first time; also prevents anchoring on the first workable idea without checking for a better one.
Does a solo developer have this failure mode: yes, arguably worse — a solo developer has no colleague to ask "did we consider X" and will simply forget their own earlier reasoning under time pressure.
Solo equivalent: before starting implementation on any non-trivial decision, write down at least two rejected alternatives and the specific reason each was rejected, in the same document as the chosen approach.
AI equivalent: have the AI generate two to three genuinely different alternative approaches before you commit to one, specifically instructed to make each alternative a real contender rather than a strawman.
Human vs AI Delegation Boundary: AI-assisted — AI generates the alternatives, human makes the final call on which to reject and why.
Automation/agent/MCP opportunity: a "devil's advocate" step built into any planning workflow, run automatically before implementation begins on anything above a defined size threshold.
Bureaucracy to discard: the formal committee review Google may attach to this step — a solo developer doesn't need a scheduled meeting to weigh alternatives, just the discipline of writing them down.
```

The shape of the eventual AI system — one agent, several specialized agents, skills-only, workflow-based, or hybrid — is decided here, from the pattern that emerges across all rows, not decided in advance.

**Explicit instruction on the "bureaucracy to discard" column:** every entry here must be carried forward by name into Phase 15's Engineering Rules and Anti-Patterns section. This column does not exist to be interesting here and then vanish — if you write something in it, you must be able to point to exactly where it lands in the final spec.

**Gate:** every row either has a real solo/AI equivalent filled in, or is explicitly marked "does not apply to a solo operator" with a one-line reason (Apple-style compartmentalization is the canonical legitimate example of "does not apply"). Every "bureaucracy to discard" entry has a named destination in the Phase 15 spec.

---

## Phase 14 — System Stress-Test: Failure Modes of the Solo System Itself

**Why this phase exists:** the single biggest structural risk in a solo-plus-AI system is the disappearance of genuinely independent review. A company has separate humans with separate incentives who can tell you your idea is bad. A solo developer working with AI has, by default, nobody — and an AI asked to "review its own work" inside the same context that produced the work is not actually independent, it's the same reasoning checking itself, which is one of the exact failure modes this phase exists to catch.

**Required failure modes the adversarial mechanism must specifically be checked against, explained:**
- **Correlated errors** — the same underlying blind spot appearing in both the "builder" and "reviewer" role because it's the same model with the same training biases.
- **Hallucinations** — confidently stated but false claims.
- **Context loss** — forgetting or misremembering something established earlier in a long task.
- **Overconfidence** — stating a weak or uncertain conclusion as if it were solid.
- **Prompt injection** — an external document or data source the system reads containing embedded instructions that hijack its behavior.
- **Reviewer collusion** — the AI agreeing with itself across roles because it has already anchored on its own prior reasoning and isn't approaching the review with genuinely fresh eyes.
- **Premature convergence** — settling on the first plausible answer instead of genuinely exploring alternatives (this connects directly back to the Phase 13 worked example above).
- **Bad tool use** — misusing an available tool (wrong parameters, wrong tool for the job, ignoring a tool's actual output).

Also required: what happens when requirements change mid-build, and how you'd actually notice this system quietly producing plausible-looking but wrong output rather than working correctly.

**The gate for this phase is not satisfied by a designed mechanism alone.** A mechanism that sounds adversarial ("ask the AI to red-team its own PRD") but runs in the same context with the same prior reasoning already in view is not actually independent — that's reviewer collusion happening inside your own mitigation. To pass this gate:

1. Design at least one concrete adversarial mechanism — for example: a genuinely fresh context with no memory of the original reasoning; an evaluation rubric written and locked *before* the output it will judge exists; or a structured devil's-advocate pass explicitly instructed to find the strongest case against the current decision, not merely to comment on it.
2. **Deliberately inject one real, specific flaw** into a mock artifact — a wrong assumption buried in a fake PRD, a skipped edge case in a fake test plan, a silently-broken backward-compatibility change in a fake design doc.
3. Run the mechanism against the flawed artifact and confirm, concretely and specifically, that it catches the injected flaw. If it doesn't catch it, the mechanism is not done — revise it and re-test. Documenting a miss and moving on does not satisfy this gate. This same test doubles as a check on the mechanism's ability to catch fabricated-but-plausible claims specifically: one of the deliberately injected flaws across your test runs should be a confident-sounding but unsourced claim slipped into a mock findings entry, to confirm the adversarial mechanism (and by extension, you) can actually spot the exact failure mode this whole four-file project is built to prevent.

**Deliverable template:**
```
## Adversarial Mechanism Design
[description of the mechanism]

## Injected-Flaw Test
Flaw injected: ...
Mock artifact: ...
Mechanism's output when run against it: ...
Did it catch the flaw? [Yes/No — if No, revise and re-test before proceeding]

## Failure-Mode Coverage Check
Correlated errors: [how addressed, or honest admission it isn't yet]
Hallucinations: ...
Context loss: ...
Overconfidence: ...
Prompt injection: ...
Reviewer collusion: ...
Premature convergence: ...
Bad tool use: ...

## Mid-Build Change Handling
[what happens when requirements shift partway through, and how it's detected]

## Silent-Failure Detection
[how you'd notice this system producing confidently wrong output rather than correct output]
```

**Gate:** at least one concrete adversarial mechanism exists, has been tested against a deliberately injected flaw as described above, and demonstrably caught it. Each named failure mode has an explicit one-line note on how it's addressed, or an honest admission that it isn't yet — no failure mode is silently skipped.

---

## Phase 15 — Master Synthesis: The Solo AI Product Engineering System

**Why this phase exists:** everything before this point has been research and pressure-testing. This phase is where it becomes a usable system — and the two worked examples exist specifically to prove it's a *system*, not just a well-organized research report.

**Deliverable — the full operating-system specification. Every section below is required. The "bureaucracy to discard" list from Phase 13 lands explicitly inside section 9, by name, not summarized away:**

1. **Product Development Lifecycle** — the full sequence, solo-adapted, from idea to deprecation.
2. **Role/Responsibility Model** — human vs. AI, using the Phase 13 delegation taxonomy throughout.
3. **Artifact Chain** — creator, reviewer, rejection authority, what carries forward, per stage.
4. **Decision Architecture** — who decides/vetoes/escalates, reversible-vs-irreversible classification rules, kill/pause/pivot criteria, consolidating every Lens 1 finding from Phases 2–11.
5. **Decision Gates & Review System.**
6. **Process Cost Model** — the minimum effective version of each practice, per the Lens 2 findings.
7. **Context & Traceability Model** — how links between requirements, decisions, code, tests, and metrics are actually preserved in the solo system, per the Lens 3 findings.
8. **Change Management Protocol** — per the Lens 4 findings.
9. **Engineering Rules and Anti-Patterns** — includes, by name, every entry from Phase 13's "bureaucracy to discard" column across both passes.
10. **Quality, Security, and Reliability System.**
11. **Release and Experimentation System.**
12. **AI/Agent Operating Model** — the shape decided in Phase 13 from evidence, not assumed.
13. **Tooling/MCP Architecture.**
14. **Adversarial Review Mechanism** — from Phase 14, including the tested-and-passed injected-flaw check. Non-optional; this is not an appendix.
15. **Reusable Toolkit** — templates, agent definitions, skill definitions, MCP tool definitions, as one consolidated section.

**Worked Example A — AI-powered expense tracker (required).** Run this idea through the complete assembled system end to end:

`idea → evidence → PR/FAQ → PRD → flows → design doc → technical design → RFC → implementation plan → tasks → code → review → tests → security → deployment → monitoring → experiment → post-launch → iteration`

Every step names its artifact and states which human or which AI role produces and reviews it. The walkthrough must include, explicitly marked:
- at least one reversible-vs-irreversible decision point, with the classification stated and justified
- one mid-build change-management event (something realistic changes partway through — a requirement shifts, an assumption turns out wrong)
- one point where the Phase 14 adversarial mechanism actually catches something, with the caught issue specifically named

**Worked Example B — a structurally different second project (required, not optional).** Choose something that is *not* a user-facing web app — for example a batch data-processing pipeline, or a research/analysis tool with no end users at all. Run it through the same assembled system.

**The explicit purpose of Example B is to test whether the system generalizes** or whether it secretly assumed "web app with a UI and end users" throughout Example A. Where a section of the system doesn't cleanly apply to Example B — for instance, "UX flows" may not mean much for a headless batch pipeline — that gap must be written down honestly as a finding, with a note on what the system should say instead for that kind of project, rather than smoothed over or silently skipped.

**Gate:** neither worked example skips a step, and every step in both traces back to a specific finding from Phases 1–14 rather than a fresh, undocumented assumption made for the first time here. Any place where Example B exposes an assumption baked in from Example A's shape is explicitly flagged as a real, named limitation of the system, not patched over quietly to make the final document look more complete than it is. Concretely: every non-trivial claim inside the 15-section spec itself should be traceable, on request, to a specific phase and org's Per-Claim entry — the master synthesis inherits the verification discipline of everything beneath it; it does not get a pass to state things more confidently just because it's the final document.

---

## This Is The End of the Four-File Set

Once Phase 15's gate is met, the system is done being *researched*. What happens next — actually running your own first real project through it — is a different kind of work than what these four files cover, and deserves its own fresh start rather than being squeezed into this document's remaining space.
