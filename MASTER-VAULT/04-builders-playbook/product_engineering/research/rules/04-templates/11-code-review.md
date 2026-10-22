# Template 11 — Code Review (author checklist + reviewer checklist)

**Use when:** every production change. **Enforces:** R-14 (small changes), R-20 (second pair of eyes), R-13 (AI-assisted scrutiny).

## For the author (before requesting review)

- [ ] The diff is small and single-purpose; refactors are separated from behaviour changes
- [ ] I ran the verification steps in the task definition (template 08, §5)
- [ ] AI-assisted portions: I have read every line, I can explain each one, tests cover the behaviour (Willison's boundary — reviewed/tested/explainable or it doesn't ship)
- [ ] No secrets, no commented-out code, no repurposed flags/identifiers (R-15, R-16)
- [ ] The PR description says *why*, links the task/design doc, and names the risk tier: **low / standard / high** (high = auth, money, data migration, security boundary, agent permissions)

## For the reviewer

*Review the highest-risk parts first. A 30-second "LGTM" on a high-risk diff is a process failure, not a review.*

### Correctness
- [ ] Does it do what the task says? Are the acceptance criteria met?
- [ ] Edge cases and error paths handled — what happens when inputs are empty, malformed, oversized, malicious?
- [ ] Concurrency considered where relevant (two writers, double-submit, retries)?

### Design
- [ ] Fits the existing architecture; no speculative generality (R-08)?
- [ ] Failure strategy present for any new integration (R-10)?
- [ ] Boring choices where possible (R-07)?

### Security (high-risk tier: mandatory deep pass)
- [ ] AuthN/authZ correct; no privilege escalation; least privilege (R-21)?
- [ ] Input validated, output encoded; no injection surface?
- [ ] AI-generated security logic independently verified (R-13)?

### Operability
- [ ] Golden signals instrumented for new behaviour (R-28)?
- [ ] Logs structured and useful; no secrets in logs (R-15)?
- [ ] Rollback story clear (R-25)?

### Tests
- [ ] Tests prove the behaviour through realistic paths (R-19), not just the author's fixtures?
- [ ] Would these tests have caught the last similar bug?

## Review outcomes

- **Approve** — ship it.
- **Approve with nits** — ship after fixing; no re-review needed.
- **Request changes** — specific, actionable; re-review required.
- **Escalate** — needs a second reviewer (high-risk tier, or reviewer is unsure).

## Acceptance criteria

- [ ] Reviewer is someone other than the author (branch protection enforces)
- [ ] High-risk diffs got a qualified human reviewer, not just an AI pass
- [ ] Every checkbox is checked or explicitly N/A with a reason
- [ ] The review happened before merge — post-merge "reviews" don't count

## Anti-patterns this blocks

AP-09 (AI code without verification) · rubber-stamp reviews · AP-08 (weak security via unreviewed auth code).
