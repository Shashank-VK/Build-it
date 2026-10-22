# Loop Engineering — Phase 16 doctrine

Carried from `files/solo-levelling/phase-16-loop-engineering.md` (SKILL card
`files/solo-levelling/phase-16-loop-engineering.md` in how-to-use/04-commands-workflows.md).
This is why the solo-levelling copies of the 9 process skills label their tail section
"Loop Architecture (Phase 16 compliance)" while deve's label it "Loop rails".

## Lineage (verbatim from the research)
- **ReAct** (Yao et al., ICLR 2023): reason -> act -> observe -> repeat is the origin of the loop shape.
- **Loop engineering** (coined by Addy Osmani, June 7 2026; popularized by Peter Steinberger / Boris Cherny, early June 2026): designing sense-decide-act-check cycles with explicit termination, not prompt-wording.
- **IAL** (Infinite Agentic Loops; "When Agents Do Not Stop", arXiv:2607.01641): a structural execution failure where feedback paths re-trigger without a termination condition. Triggers: goal ambiguity; tool-output misinterpretation (empty response read as "retry").
- **ECT** (Evidence-Carrying Termination, arXiv:2608.23623): return a complete signal only with a typed certificate binding claims to in-scope reproducible evidence. 0 unsafe completions vs high failure rate in subjective critics.

## Minimum rails (what this OS implements)
1. `max_steps` per loop (global 15; per-skill budgets) — hard rail.
2. Identical tool+args twice consecutively -> fatal (debounce hook). The research notes this exact mechanism is a proposal for this OS, not an evidenced production feature.
3. Deterministic termination: external exit code (ECT certificate), never conversational self-assessment.
4. Budget circuit breaker (spend-log) so a silent loop cannot burn a day unnoticed.

## Skill-tail naming note
Deve skills end with `## Loop rails`; solo skills end with `## Loop Architecture (Phase 16 compliance)` and cite the above. Both are the same three fields (max_steps / termination / self_certification). When you see either label, this doctrine applies.