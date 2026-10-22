# Solo AI Product Engineering System — Master Framework (File 1 of 4)

This is the constitution the other three files answer to. `01-phases-1-to-5.md`, `02-phases-6-to-10.md`, and `03-phases-11-to-15.md` each assume everything in this file is already read and locked before their phases start. Read this file first, every time, even if you've read it before — it's short enough to re-read and important enough that skipping it is how drift happens.

---

## Purpose

Reverse-engineer the actual *control system* that a small set of high-performing engineering organizations use to take an idea to shipped, maintained, evolving software — not the documents they produce as artifacts, but the underlying failure-prevention logic those documents exist to enforce — and compress that control system into an operating system that one developer, working with AI, can actually run without the coordination overhead a 200-person organization needs and a solo operator does not.

The four files together are both the research plan and the actual prompts used to execute it. Every phase is written to be handed to a fresh session on its own and understood without needing the whole conversation history that produced it.

---

## The Governing Principle

Every practice discovered anywhere in this research gets run through the same seven-link chain. This chain is the actual point of the entire project — not a formality to mention once and move past. Phases, documents, and roles all exist only to answer it accurately, for every practice, at every org:

**What failure mode does this practice exist to prevent → what mechanism controls that failure → what does the mechanism cost → does a solo developer even have this failure mode → what is the minimum effective solo equivalent → can AI perform it, review it, or automate it → how do you verify AI did it correctly?**

A finding that stops at "here's what they do" without reaching "here's the failure it prevents and whether that failure applies to me" is incomplete, no matter how well-sourced or well-written it is. Test every finding against this chain before writing it down as done. If you can only answer the first two or three links, say so explicitly rather than quietly treating the finding as complete.

**Worked mini-example of the chain, so it's unambiguous what "answering it" looks like:**
*Practice:* Amazon requires a written narrative (six-pager) instead of a slide deck for major decisions.
*Failure mode prevented:* slide decks let a persuasive presenter paper over weak logic with formatting and delivery; a narrative forces the argument to survive on its own.
*Mechanism:* a required document format plus a silent-reading period at the start of the meeting before any discussion.
*Cost:* meeting time is front-loaded into silent reading (20–30 minutes), and the document itself takes real writing time before the meeting even happens.
*Does a solo developer have this failure mode?* Partially — you can't be swayed by someone else's charisma, but you absolutely can be swayed by your own certainty and a persuasive-looking chart you made yourself.
*Minimum solo equivalent:* write the actual decision out in full sentences before acting on it, specifically because writing forces gaps in your own reasoning to surface that a bullet list would hide.
*AI equivalent:* have the AI draft the narrative from your bullet points, then have it (in a separate pass) attempt to find the weakest claim in the narrative it just wrote.
*Verification:* check whether the AI's "weakest claim" pass actually finds something real, by occasionally testing it against a narrative with a deliberately planted flaw (this exact mechanism is formalized later in Phase 14).

Every phase in Files 2–4 is expected to produce findings at this level of completeness, not just the first two links.

---

## The Standard Research Question Chain

Phases 2 through 11 (spread across Files 2 and 3) all apply this same underlying chain to their slice of the lifecycle, instead of inventing unrelated bespoke questions each time:

**Decision → owner → information used → artifact produced → who reviews it → gate/condition required to pass → failure prevented → consequence if skipped**

Every phase adds specific, concrete sub-questions on top of this chain. The chain is the non-negotiable floor of what each phase must answer, not the ceiling.

---

## How To Use These Four Files

Run one phase per research session wherever practical — a phase from File 2, File 3, or File 4 is meant to be pasted into a session on its own. Save each phase's output as its own findings file (`phase-01-findings.md`, `phase-02-findings.md`, and so on) before starting the next phase. Update `research-log.md` after every phase (format at the end of this file).

**If a session ends mid-phase:** the phase is not complete. Save what's found so far in that phase's findings file under a `## IN PROGRESS — resume here` heading, listing exactly which orgs and which sub-questions are covered and which aren't. The next session opens that file first, confirms what's covered, and continues — it does not restart the phase or silently skip what's uncovered.

**Effort cap / diminishing-returns rule (applies to every phase in Files 2–4):** for any single sub-question, stop actively searching once two consecutive independent search attempts produce no new `[PRIMARY]` or `[INFERRED]` information beyond what's already found. Record what was found, tag it honestly, and mark the sub-question "not further pursued — diminishing returns." An unbounded phase is itself a failure mode: it burns the one resource a solo researcher actually has (time) for no added signal.

**Depth-balance rule (applies to every phase covering multiple orgs):** as a soft guide, no single org within a phase should consume more research effort than the other five combined. If Amazon or Google — the richest public trail — start dominating simply because there's more to find, stop and move to the next org. The lean-team org (Basecamp/37signals or Linear) is on the list specifically *because* it's the most structurally relevant to a solo operator; it must not be the org that quietly gets the thinnest treatment just because less has been written about it publicly.

---

## Ground Rules (non-negotiable, apply to every phase in every file, without exception)

**Source-confidence tagging — a tag is not valid without the source trail defined in the Verification Protocol below.** Every specific claim is tagged:
- `[PRIMARY]` — stated by an engineer, technical leader, or the company itself, in a *technical* account: an engineering blog post, a conference talk (QCon, InfoQ, Strange Loop, re:Invent technical tracks, etc.), a process retrospective, a book written by someone who worked there. `[PRIMARY]` explicitly **excludes promotional or marketing copy.** "We deploy 100 times a day" from a corporate landing page is not automatically PRIMARY just because the company said it — only a technical, process-focused account qualifies.
- `[INFERRED]` — consistent across at least **two independent, credible sources** that did not simply copy each other. Five aggregator articles quoting the same original blog post is one source, not five — check independence before upgrading confidence.
- `[SPECULATIVE]` — plausible and reasoned, explicitly flagged as reasoning rather than a found fact, with the reasoning itself stated. A phase heavy on `[SPECULATIVE]` tags is an honest phase, not a failed one — especially anything touching internal AI tooling.
- `NOT FOUND` — a genuine attempt was made (per the effort-cap rule) and nothing turned up. This is not a failure state to hide; it is a correct, complete answer, and must be recorded as explicitly as any other tag, with the queries that were tried.

**Public process vs. internal AI tooling stay strictly separate**, in clearly separated subsections of every phase's output. How a company writes a design doc is researchable. How its internal AI agents are prompted is almost never public. Don't chase leaked internal prompts as a goal; anything that surfaces incidentally is `[SPECULATIVE]` at best and nothing later builds on it as solid ground.

**Nothing before Phase 13 assumes the shape of the final AI system.** No "orchestrator agent," no implied single coordinating agent anywhere in Phases 1–12. The shape — one agent, several, skills-only, workflow-based, or hybrid — is an output of evidence gathered, decided explicitly in Phase 13.

**Uniform structure across companies is not required, and gates never quietly force it.** "Does not exist" or "not publicly documented" is a complete, valid answer for a given org/artifact pair. No phase gate is phrased as a hard numeric requirement like "true for 3 orgs" — instead every gate requires covering every org, with either real findings or an explicit one-line "not documented" note. No org is silently skipped; no org is force-fit into a template it doesn't have.

**Illustrative examples never get baked into a research question's wording.** A question phrased around one company's specific pattern anchors the research toward confirming that one pattern instead of discovering what's actually there. Every question below describes the *class* of thing being researched, never a single instance of it.

**No premature system-building.** Phases 2 through 12 are research only. The solo+AI system doesn't get designed until Phase 13.

**Periodic tag-integrity audits.** Tagging discipline erodes over long stretches, the way code-comment discipline does. At the checkpoints marked inside Files 2–4, re-open the two or three most-cited claims from two phases back and confirm the tag still honestly reflects the source. Correct in place if not — don't carry a bad tag forward.

**Every phase ends with an explicit, checkable gate.** A phase is complete when its gate is specifically, actually true — not when a lot of text has been produced.


---

## The Verification Protocol — No Guessing, Ever

This section exists because of one specific, dangerous failure mode: an AI asked to research "how Google writes design docs" already has a strong, fluent, plausible-sounding sense of how large tech companies probably operate, drawn from general training-data pattern-matching — entirely independent of whether it actually finds a real source in a given session. That fluent sense is not research. It reads exactly like a real finding, which is precisely what makes it dangerous — a fabricated claim and a sourced claim look identical on the page unless the format forces the difference to show.

**The rule, as plainly as it can be stated: a claim only exists in this research if it can be traced to a specific source that was actually retrieved and read during this session.** Not "this is generally how large tech companies operate." Not "this is a well-known industry pattern." Not "based on general reasoning about how this probably works." If a specific webpage, blog post, talk, or book passage was not actually found and read this session, the claim does not get written down as a finding — the honest entry is `NOT FOUND`, even when a fluent, plausible-sounding answer is sitting right there and would be easy to write instead.

**The test to run, silently, before writing any claim down:** *can I state exactly which source this came from — and if pressed, could I quote or closely paraphrase the specific passage that supports it?* If the honest answer is "no, but this sounds like the kind of thing they'd do," that is a guess wearing a finding's clothes. Either go find an actual source, or write `NOT FOUND` / `[SPECULATIVE — reasoning, not a sourced finding]` and say so plainly. Never let a fluent sentence substitute for an actual retrieved fact.

**The Per-Claim Documentation Format — required for every single claim in every phase, no exceptions.** This is what makes a tag checkable later instead of merely trusted on faith. Every claim, in every phase's findings file, is recorded in this shape:

```
Claim: [the actual finding, stated plainly]
Search queries used: [the actual query or queries typed to find this]
Source: [name/publication/speaker and, wherever possible, the specific passage, sentence, or excerpt that supports the claim — not just "a blog post said this"]
Verification pass: [a second, genuinely different search attempted specifically to confirm or contradict this claim — the query used, and the result: confirmed / contradicted / nothing found either way]
Tag: [PRIMARY / INFERRED / SPECULATIVE / NOT FOUND]
```

A bare tag with no queries, no named source, and no verification-pass result attached is not acceptable output from any phase in this project — it is exactly the unsupported assertion this whole protocol exists to prevent.

**The Mandatory Verification Pass, explained.** After finding a source for a claim, do not stop there. Run one additional search specifically trying to confirm or contradict it — not the same query reworded, but a genuinely different angle: a different search term, a search for a rebuttal or contrasting account, a search for the same claim described by a different named source. Log this pass explicitly, every time. A claim that survives this pass with a confirming or neutral (nothing found either way) result keeps its tag as found. A claim that a second pass actually contradicts requires **both accounts to be recorded**, with the conflict stated plainly in the findings file — never silently pick whichever version sounds better and quietly discard the other. A real conflict between sources is itself a valid, useful, interesting finding — it is not a problem to be smoothed away before writing it down.

**Exhaustiveness — every question, every org, nothing quietly skipped or merged.** Being "extensive" means every question in every phase's exhaustive question set is actually attempted for every one of the six orgs individually — not answered only where it happened to be easy to find something, and not silently combined into a shorter answer that skips the harder sub-questions. Where nothing is found after a genuine attempt (per the effort-cap rule in the earlier section), that is recorded explicitly as `NOT FOUND — attempted with queries: [x], [y]`, sitting in the findings file exactly where a real answer would have gone, not omitted or glossed over.

**Why this is not the same thing as "make it longer."** Padding a finding with more adjectives, more restated context, or more confident-sounding prose does not make it more true — it just makes a possible guess harder to spot. The Per-Claim Documentation Format above is often *more* work to produce than a fluent paragraph, but it is not primarily about producing more text: it is about making every claim in this research either genuinely checkable against a real source, or honestly labeled as not found. That is what "detailed" means for this project, and it is enforced structurally from here forward, not just requested as a preference.
---

## Cross-Cutting Research Lenses

These four lenses apply *inside* Phases 2–11 as questions asked of every stage — never as separate phases of their own.

**Lens 1 — Decision Architecture.** Who decides, who advises, who can veto, when does escalation happen, how is genuine disagreement resolved (not just "consensus," but what happens when consensus fails). Is the decision reversible (a "two-way door") or irreversible (a "one-way door"), and does that distinction change who's allowed to make the call. Also covers how a project/feature gets killed, paused, or pivoted at this stage — what evidence triggers it, who holds authority, what guards against sunk-cost bias.

**Lens 2 — Process Cost.** The real time, headcount, meeting load, cognitive overhead, and calendar delay a practice imposes at the org's actual scale — the raw material Phase 13 uses to find the *minimum effective version* for one developer.

**Lens 3 — Context & Traceability.** What information actually survives the trip from idea through PRD, design, architecture, code, tests, launch, and outcome. Are links between a requirement, the decision about it, the code implementing it, the test verifying it, and the metric measuring its outcome preserved and traceable, or do they quietly decay.

**Lens 4 — Change Management.** What happens at this stage specifically when requirements, assumptions, architecture, or priorities shift mid-way. What gets re-approved, by whom, and what's allowed to continue unchanged.

---

## Project-Level Decision Architecture: Kill / Pause / Pivot Criteria For This Research Project Itself

Lens 1 is applied to every company studied. It's applied here, once, to this project directly.

**Pause-and-reconsider trigger:** if, by the end of Phase 6, three or more completed phases show a majority of findings landing in `[SPECULATIVE]` or "not publicly documented" rather than `[PRIMARY]`/`[INFERRED]`, stop and explicitly reassess — don't push through the remaining phases assuming the evidence base will improve. The honest response to systemically thin evidence is to narrow scope or accept a smaller, more honestly-labeled system, not to quietly upgrade tags to keep the project feeling like it's working.

**Who can invoke this:** you, at the end of any phase from Phase 3 onward, using the same evidence-based standard the research demands of the companies it studies.

**What allows resuming unchanged:** if the thinness turns out concentrated in specific stages rather than spread evenly, resume unchanged — narrow expectations for those specific phases rather than restructuring the whole plan.

---

## Organization Shortlist

Chosen for complementary public evidence, not brand reputation — each illuminates a different part of the lifecycle unusually well.

1. **Amazon** — PR/FAQ process, six-pagers, bar raiser mechanism, DRI ownership, "working backwards" culture. Rich trail via *Working Backwards* (Bryar & Carr) and many former-employee technical accounts.
2. **Google** — design doc culture, readability/review certification, launch review process, capacity-planning discipline. Rich trail via the SRE book series and public design-doc templates.
3. **Meta** — RFC culture, bootcamp-driven onboarding and norms, fast-iteration culture, feature-flag-heavy progressive rollout.
4. **Netflix** — "freedom and responsibility" culture, chaos engineering (Chaos Monkey and successors), blameless postmortems, extreme decentralization.
5. **Stripe** — API-design obsession, documentation as a first-class product, unusually candid public engineering writing.
6. **One lean/small-team counterexample** — Basecamp/37signals or Linear, whichever proves the stronger public writing trail in Phase 1 — included because a 6-to-30 person team's actual discipline transfers to a solo developer far more directly than a 200,000-person company's does.

**Apple is deliberately excluded.** Its defining trait is extreme secrecy and compartmentalization — the opposite of what a solo operator needs, since you can't silo information from yourself. It can be added back only if Phase 1 finds a genuinely strong public source on Apple's actual process, not brand mythology — and if added, it inherits the same tagging and depth-balance rules as every other org.

**Starting search anchors per org** (well-established public reference points to orient searches from — not conclusions, verify everything against the tagging rules above):
- Amazon: "PR/FAQ," "working backwards," "bar raiser," "six-pager," Amazon Leadership Principles as they relate to process (not the principles themselves, their *procedural* enforcement)
- Google: "Google design doc template," "Google readability review," "Google SRE book," "launch readiness review"
- Meta: "Meta engineering RFC process," "Meta bootcamp," "Meta Gatekeeper feature flags"
- Netflix: "Netflix freedom and responsibility," "Chaos Monkey," "Netflix blameless postmortem," Netflix Technology Blog
- Stripe: Stripe engineering blog, "Stripe API design," Stripe's public API documentation practices
- Basecamp/Linear: "Shape Up" (Basecamp's public methodology book), Linear's public "Linear Method" writing

---

## Session Continuity Protocol

Keep a single running `research-log.md`, updated after every phase (and after any mid-phase pause) with: phase number, one-paragraph summary of findings, an evidence-density note (rough sense of how much landed as `[PRIMARY]` vs. the other tags), and a reference to that phase's findings file. Review this log before starting any new phase, and before resuming any interrupted one, so nothing already established gets silently re-derived, contradicted, or repeated.

---

## Where Each Phase Lives

- **File 2 — `01-phases-1-to-5.md`:** Phase 1 (Ground Rules & Org Lock-In), Phase 2 (Idea → Evidence → Product Thesis), Phase 3 (Requirements, Scope, Non-Goals), Phase 4 (UX Flows & Product Spec), Phase 5 (Design Docs, Technical Design Docs, RFCs)
- **File 3 — `02-phases-6-to-10.md`:** Phase 6 (Architecture, APIs, System Context), Phase 7 (Security, Privacy, Reliability Review), Phase 8 (Implementation Planning & Task Decomposition), Phase 9 (Code Review & Quality Systems), Phase 10 (Testing, Experimentation, Progressive Rollout)
- **File 4 — `03-phases-11-to-15.md`:** Phase 11 (Observability, Incident Response, Postmortems), Phase 12 (AI's Documented Role & Verified Correctness), Phase 13 (Compression: Company → Solo + AI), Phase 14 (System Stress-Test), Phase 15 (Master Synthesis + two worked examples)
