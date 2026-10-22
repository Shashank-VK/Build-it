# Template 14 — Release Readiness (go / no-go)

**Use when:** every production release. **Enforces:** R-25, R-26, R-27, R-18, R-22. The release does not ship with unchecked boxes — each needs a check or a named, dated exception.

## 1. Release identity

- Artefact: _… (immutable build ID / tag)_ · Built from: _commit …_ · Pipeline run: _link_

## 2. Verification

- [ ] CI green on the release artefact (build + test + scan — R-12, R-18)
- [ ] Critical-path tests pass (template 10, §2)
- [ ] Code review complete per template 11 (risk tier: _…_)
- [ ] Security: ASVS L1 gap register current; no blocking findings (template 13)
- [ ] UX & visual QA passed for user-facing changes (template 12)

## 3. Rollout plan

- Strategy: _big-bang (trivial only) / rolling / canary / blue-green / flagged_
- Progressive steps: _… (e.g., 1% → 10% → 50% → 100%, with bake time and promotion criteria)_
- Feature flags involved: _name, owner, expiry, default state_
- Database/data migration: _expand/contract steps; down-migration or forward-fix plan_

## 4. Reversibility (mandatory)

- Rollback procedure: _exact steps, not "re-deploy old version"_
- Rollback rehearsed: _date_ · Time to rollback: _…_
- Kill switch (if flagged): _how to disable without a deploy_

## 5. Operability

- [ ] Golden-signal dashboards ready and linked (R-28)
- [ ] Alerts for this release's risks, with runbook links (R-29)
- [ ] On-call engineer aware of the release and its risks
- [ ] AI cost instrumentation in place if the release adds model calls (R-32)

## 6. Communication

- [ ] Changelog / release notes drafted (user-facing language)
- [ ] Stakeholders notified: _…_
- [ ] Support briefed on what's changing and known issues

## Decision

- [ ] **GO** — all boxes checked or exceptions named below
- [ ] **NO-GO** — blocking items: _…_ · next review: _…_

*Exceptions (each needs a name and date):*

| Exception | Owner | Expires |
|---|---|---|
| | | |

## Acceptance criteria

- [ ] The shipped artefact is the tested artefact (R-12)
- [ ] Rollback is a written, rehearsed procedure — not a hope
- [ ] Every unchecked box is a named, dated exception, not an oversight

## Anti-patterns this blocks

Irreversible big-bang releases (R-25) · untested rollbacks (Knight Capital's lesson) · silent launches.
