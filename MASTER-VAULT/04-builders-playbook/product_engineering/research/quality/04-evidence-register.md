# 04 — Evidence Register: quality workstream (§21–§23)

**Researched:** 2026-10-10 · **Method:** official sources (W3C/WAI, ETSI directory research, DOJ via SBA Advocacy, FTC via secondary reporting) + unofficial (a11y practitioner blogs, GitHub issues/skill repos, r/accessibility-adjacent community writing, lawsuit-trackers, QA practitioner blogs).
**Labels:** Verified (checked against primary/official source) · Corroborated (2+ independent sources agree) · Inferred (reasonable synthesis, single or indirect basis) · Proposed (author's framework, not sourced) · Unknown (could not establish).

Each entry: claim · sources (URL, type, author/org, pub date) · accessed 2026-10-10 · confidence · corroboration/contradictions · implication.

---

## A. Standards & law (§22)

**A1. WCAG 2.2 is the current W3C Recommendation (5 Oct 2023; updated 12 Dec 2024; ISO/IEC 40500:2025); SC 4.1.1 Parsing obsolete.**
Sources: W3C/WAI standards pages (official); github.com/peterbamuhigire/design-system-skills doctrine ref (unofficial, updated 2026-09-24); github.com/ayjayy/neura11y standards registry (unofficial, fetched 2026-03-13). **Label: Verified.** Confidence: high. No contradictions. Implication: the normative baseline for all compliance claims today.

**A2. WCAG 3.0 is a Working Draft (latest 10 Sept 2026; prior 3 Mar 2026, 4 Sept 2025); incomplete; conformance model still in development (single conformance level + reporting tiers under discussion; graduated scoring abandoned); W3C advises continuing WCAG 2.2 A/AA.**
Sources: w3.org/standards/history/wcag-3.0 (official); accessibility.org.au news 2026-09-10 (press); WAI wcag3-intro via GitHub mirror (official content). Full URLs: https://www.w3.org/standards/history/wcag-3.0/ · https://www.accessibility.org.au/w3c-releases-updated-wcag-3-0-working-draft/ **Label: Verified.** Confidence: high. No contradictions. Implication: WCAG 3.0 must not be used for conformance claims; track direction only.

**A3. European Accessibility Act (Directive (EU) 2019/882) applicable since 28 June 2025; covers e-commerce, banking, telecoms, transport info, e-books, AV-media access, listed hardware; non-EU vendors selling to EU consumers in scope; exemptions for microenterprise services, B2B-only, archived/pre-2025 content, third-party content outside control, disproportionate burden.**
Sources: webyes.com EAA scope blog (commercial); lyssna.com EAA blog (commercial); allyant.com EAA compliance guide (commercial). **Label: Corroborated.** Confidence: medium-high (secondary summaries agree; not verified against the directive's OJ text in this pass). Implication: sets the "who must comply" boundary for §22 blocking rules.

**A4. EN 301 549 v3.2.1 (2021-03) is the version currently cited in the EU Official Journal → legal yardstick is WCAG 2.1 AA; presumption of conformity flows from OJEU citation, not from publication.**
Sources: wcagc.com EN 301 549 explainers (practitioner, Pavel Charkasau, updated 2026-07-04 and 2026-09-04); accessiway.com legal guidance (commercial, accessed ~2026-10-09); axall.digital (commercial). Full URLs: https://wcagc.com/blog/en-301-549-vs-wcag-2-1 · https://www.accessiway.com/legal-guidance/en-301-549 · https://www.axall.digital/insights/en301549-version-4-1-1-what-changes-and-when-it-applies **Label: Corroborated.** Confidence: medium-high. Minor tension: expected citation date given as "around October 2026" (wcagc) vs "late 2026" (accessiway) — timing estimates, not substance. Implication: test to WCAG 2.1 AA for legal purposes today; add 2.2 checks as forward-looking practice.

**A5. EN 301 549 v4.1.1 published by ETSI 2 Sept 2026 (adopted 24 Aug 2026), adopts WCAG 2.2 AA; NOT yet OJEU-cited as of early Sept 2026.**
Sources: same as A4; Wikipedia EN 301 549 version table (tertiary, edited ~2026-10-10); github.com/piiix-org/inter.face ETSI-directory research 2026-08-08 (unofficial primary-document check — at that date only v4.1.0 final draft existed; superseded by the Sept publication, not contradicted). **Label: Corroborated.** Confidence: medium-high. **Unknown:** whether OJEU citation has occurred between early Sept and 2026-10-10 — re-check before asserting.

**A6. DOJ ADA Title II final rule (24 Apr 2024): WCAG 2.1 AA for state/local government websites and mobile apps; narrow content exceptions (archived, pre-existing conventional documents, certain third-party content, individualized password-protected documents, pre-existing social posts). Compliance dates extended by Apr 2026 interim final rule → 26 Apr 2027 (pop ≥50,000) and 26 Apr 2028 (smaller/special districts).**
Sources: advocacy.sba.gov 2024-04-25 (US gov); lexology.com Reed Smith client alert (legal press, ~2026-04); wcagc.com ADA explainer (practitioner, updated ~2026-10-08); github.com/nurkamol/website-build-kit compliance ref (unofficial). Full URLs: https://advocacy.sba.gov/2024/04/25/justice-department-finalizes-rule-requiring-state-and-local-governments-to-make-their-websites-accessible/ · https://wcagc.com/blog/does-ada-apply-to-websites **Label: Corroborated.** Confidence: medium-high (extension reported by multiple secondaries; not verified against the Federal Register in this pass). Implication: the one US regime with a hard technical standard and dated deadlines.

**A7. ADA Title III (private sector): no technical standard in regulation (2017 rulemaking withdrawn); DOJ 2018 position that ADA applies to websites with flexibility on method; courts/settlements converged on WCAG 2.1 AA (Robles v. Domino's, Gil v. Winn-Dixie).**
Sources: wcagc.com ADA explainer (practitioner); github.com/nickbevers/claude-rules US-ADA skill (unofficial). **Label: Corroborated.** Confidence: medium. Implication: private-sector exposure is litigation-driven; the standard is de facto, not de jure.

**A8. Section 508: WCAG 2.0 AA via 2017 refresh; no refresh scheduled.**
Sources: github.com/gitsukrit/claude-skills gov-a11y-enforcer (unofficial); github.com/nurkamol/website-build-kit (unofficial). **Label: Corroborated (weak — two unofficial sources agree).** Confidence: medium. Implication: 508 compliance ≠ current best practice; build to 2.2 AA for margin.

**A9. UK PSBAR requires WCAG 2.2 AA + published statement (public sector); Canada AODA requires WCAG 2.0 AA (Ontario).**
Sources: github.com/nurkamol/website-build-kit compliance ref (unofficial, single source for both claims). **Label: Inferred (single-source).** Confidence: low-medium. Needs verification against legislation.gov.uk / Ontario e-Laws before use in a blocking rule.

---

## B. Automated vs manual testing (§21/§22)

**B1. Deque study (2,000+ audits, 13,000+ pages, ~300,000 issues): automated testing covered ~57% of accessibility issues by volume — but counted only issues its rules could identify; did not measure task completion by disabled users.**
Sources: wcagc.com scanner buyer's guide (practitioner, ~2026-09-21); a11yflow.dev (practitioner, ~2026-07); mgifford/wcag-spine testing-methods.md (community, GitHub); LinkedIn article by Nicolas Steenhout (practitioner, ~2026-09-23). All cite Deque (2021/2023). Full URLs: https://wcagc.com/blog/accessibility-scanner-buyers-guide · https://www.a11yflow.dev/blog/automated-vs-manual-accessibility-testing **Label: Corroborated.** Confidence: medium-high for the number; high for the caveat (multiple sources stress the task-completion gap). Contradiction sought: none found — but note the number is Deque's self-reported figure from its own audits (vendor-adjacent evidence).

**B2. By share of success criteria, the machine-decidable portion is ~30–40%.**
Sources: wcagc.com; mgifford/wcag-spine (both citing the same reasoning). **Label: Corroborated (weak — two sources, shared provenance).** Confidence: medium. Implication: budget roughly half the defects for human testing whichever way you count.

**B3. WebAIM Million 2026 (Feb 2026 crawl): detectable WCAG 2 failures on 95.9% of home pages, avg 56.1 errors/page; six failure types (low contrast, missing alt, missing form labels, empty links, empty buttons, missing document language) ≈ 96% of detected errors — the reliably auto-detectable set.**
Sources: peterbamuhigire/design-system-skills doctrine ref (unofficial, citing WebAIM); a11yflow.dev (citing WebAIM Million 2026); digitalapplied.com 2026 statistics (citing WebAIM). **Label: Corroborated.** Confidence: medium-high (WebAIM primary not fetched in this pass). Implication: automation clears the highest-volume defects; the remainder needs humans.

**B4. axe-core returns an `incomplete` ("needs review") bucket — results the rule could not decide due to technical limits; some products filter it out of reports.**
Sources: wcagc.com buyer's guide (citing axe-core API docs). **Label: Corroborated (single practitioner source + official API docs referenced).** Confidence: medium. Implication: ask vendors where `incomplete` results surface; they are the explicit human-review backlog.

**B5. W3C: tools "cannot check all accessibility aspects automatically. Human judgement is required."**
Sources: wcagc.com (quoting W3C WAI). **Label: Verified (quote of official guidance via secondary).** Confidence: high.

**B6. Keyboard testing is the fastest/cheapest/highest-yield manual test; screen-reader testing needs ≥2 pairings (NVDA+Chrome, VoiceOver+Safari; JAWS differs).**
Sources: xrnavigation/web-a11y-plugin common-mistakes.md (community, GitHub); WebAIM Screen Reader Survey #10 (2024) cited therein. **Label: Corroborated.** Confidence: medium. Implication: the three-tier model (axe → keyboard → SR) in §22.

---

## C. Overlays, lawsuits, enforcement (§22 postmortems)

**C1. FTC final order 22 Apr 2025: accessiBe to pay $1M over claims its widget could make sites WCAG-compliant; barred from such claims without evidence.**
Sources: wcagc.com EN 301 549 checklist 2026 and buyer's guide (practitioner, citing FTC); digitalapplied.com 2026 statistics (citing FTC). **Label: Corroborated.** Confidence: medium-high (FTC order not fetched directly in this pass).

**C2. WebAIM practitioner survey (2021, n=758): 67% rated overlays not at all/not very effective (72% among respondents with disabilities).**
Sources: wcagc.com overlays-and-lawsuits explainer (citing WebAIM). **Label: Corroborated (single secondary citing primary).** Confidence: medium.

**C3. US litigation 2025: 4,928 suits all jurisdictions; 3,117 federal (+27% YoY); ~70% target e-commerce; 35.8% of top-500 e-retailers sued; ~29% repeat defendants (46% in federal court). 2026 pace: ~6,000 (+~20%), record; H1 2026 highest first-half volume tracked; 10 most active firms file ~84%.**
Sources: testpros.com 2026 lawsuit statistics (citing UsableNet/Seyfarth Shaw, ~2026-09-24); digitalapplied.com (citing UsableNet Jan 2026 year-end); blog.usablenet.com 2026 midyear (vendor primary); wcagc.com (citing UsableNet 2026). Full URLs: https://testpros.com/accessibility/web-accessibility-lawsuit-statistics/ · https://www.digitalapplied.com/blog/web-accessibility-statistics-2026-wcag-lawsuit-data · https://blog.usablenet.com/digital-accessibility-lawsuits-in-2026-five-trends-companies-should-know **Label: Corroborated.** Confidence: medium-high (UsableNet is a vendor with a litigation-analytics product — direction consistent across years, absolute counts are its methodology). Note: demand letters are private, so true claim volume is higher (Corroborated — UsableNet itself notes this).

**C4. France, first EAA-framework private-company decision: 4 June 2026, Tribunal judiciaire de Caen v. Carrefour — six months to full RGAA compliance, €500/day penalty thereafter, €10,000 damages; claimed 71% compliance rejected ("cannot be only somewhat accessible"; obligation of result). Parallel Auchan case dismissed 5 May 2026 (Lille) on disputed turnover-threshold reading; appealed to Douai.**
Sources: accessiway.com EAA enforcement review (~2026-09-18); digitalapplied.com 2026 statistics; medium.com/@instarenewal EAA 2026 tracker (Jul 2026); nordic-accessibility-community-group EAA enforcement tracking (community, GitHub). Full URLs: https://www.accessiway.com/blog/eaa-enforcement · https://medium.com/@instarenewal/the-2026-european-accessibility-act-what-agencies-actually-need-to-track-6064898a16b4 **Label: Corroborated.** Confidence: medium-high. Implication: partial-compliance defenses fail; civil-society litigation is the sharp end of EAA enforcement so far.

**C5. Administrative enforcement, first 15 months: only 4 fines on public record EU-wide, all Czechia, ~€580 total, all for a missing accessibility paragraph in shop terms (bundled with other breaches); Dutch ACM Mar 2026 assistive-tech test: order could not be completed at 61% of ~100 large webshops; Sweden PTS: 124 complaints, first cases Oct 2025; France DGCCRF: 20+ sites checked early 2026, action planned for ~half.**
Sources: einpresswire.com Peculiar Systems review (2026-10-02, single-studio 27-country review); medium.com/@instarenewal (ACM/PTS/BFSG figures); nordic tracker (DGCCRF). Full URLs: https://www.einpresswire.com/article/946725505/review-finds-four-eu-accessibility-act-fines-in-15-months-all-in-czechia **Label: Corroborated (with single-source components).** Confidence: medium for the pattern (slow administrative fining, paperwork-first); lower for exact fine totals. **Negative evidence:** the absence of checkout-barrier fines despite documented checkout barriers is itself a finding — regulators are starting with terms-and-conditions paragraphs.

**C6. ~20% of 2026 US defendants had an overlay widget installed; UsableNet: widgets "have not proven to be a meaningful deterrent, legally or practically."**
Sources: wcagc.com overlays explainer (2026-09-12, citing UsableNet). **Label: Corroborated (single secondary).** Confidence: medium. Caveat noted in source: overlap confounded by e-commerce concentration (~80% of filings).

---

## D. Functional-audit tooling (§21)

**D1. Broken-link detection: per-page scanner extensions (LinkAudit — concurrent HEAD-first checks, CSV/JSON export) and site crawlers; redirect chains >2 hops flagged.**
Sources: chromewebstore.google.com LinkAudit listing (vendor); github.com/bridgettmirthful637/librecrawl-mcp README (community); github.com/nasarwaljatin/lori-the-crawler crawl-accessibility-audit skill (community). **Label: Corroborated.** Confidence: medium. Implication: link integrity is fully automatable; destination *correctness* is not.

**D2. Playwright auto-waits on actionability (attached, visible, stable, enabled, receiving events) before every action; this eliminates the largest flake class. Flakiness comes from timing/test-data/environment drift, not the framework. Anti-flake discipline: assert on state not time; role/test-id selectors; isolated seeded state; traces on CI failure.**
Sources: github.com/lovelybalu/deflaky playwright-vs-cypress guide (community); dev.to Playwright-vs-Cypress CI article (~2026-09-14); github.com/dheerajreddy01/claude-skills playwright-cypress skill (community). **Label: Corroborated.** Confidence: medium-high.

**D3. Google: ~16% of tests showed some flakiness (Google Testing Blog, 2016); teams ignore alarms with a history of false signals.**
Sources: github.com/beh01lder/e2e-skills (community, citing Google). **Label: Corroborated (single secondary citing primary).** Confidence: medium. Dated (2016) — magnitude may have shifted; direction (flakiness is endemic at scale) stands.

**D4. LLM-generated tests reproduce human anti-patterns (tests that pass without asserting); "iterate until green" loops push agents toward weakening assertions to vacuity; an agent's green check is weaker evidence than a person's.**
Sources: github.com/beh01lder/e2e-skills (citing arXiv:2410.10628 and testomat.io analysis); playwright best-practices/eslint-plugin-playwright `no-conditional-expect` rule cited therein. **Label: Corroborated.** Confidence: medium. Implication: §23's assertion-strength review at Gate 5.

**D5. Visual regression: Playwright `toHaveScreenshot` (free, local baselines, no review UI, font-rendering false positives without consistent CI env) vs hosted Percy/Chromatic/Applitools (cross-browser, review/approval workflow, cost at scale, external dependency). Hosted tools earn cost in the review workflow, not raw diffing.**
Sources: testdino.com Playwright-vs-Percy (~2026-08); qaskills.sh Percy-vs-Applitools-vs-Chromatic 2026; github.com/graycodeai/graycode-skills visual-regression-testing (community); github.com/vicenteopaso/vicenteopaso-sdd VISUAL_REGRESSION_TESTING.md (practitioner). Full URLs: https://testdino.com/blog/playwright-vs-percy · https://qaskills.sh/blog/percy-vs-applitools-vs-chromatic-2026 **Label: Corroborated.** Confidence: medium-high. Implication: screenshot diffing proves pixels changed, never whether the change is correct.

**D6. Crawlers cannot bypass login screens — auth/payment flows need scripted, credentialed e2e.**
Sources: librecrawl-mcp README (community). **Label: Corroborated (weak — single community source, but consistent with tool design).** Confidence: medium. Implication: §21 inventory items 1.9–1.10 are manual/scripted by construction.

---

## E. Quality gates (§23)

**E1. Release-readiness practice converges on: frozen scope (tagged commits/ticket list; late additions re-trigger affected tests), named owners per check, evidence artifacts per gate, and GO/NO-GO/NOT-ASSESSED verdicts where unknown ≠ pass.**
Sources: momentic.ai QA release checklist (~2026-09-26, 12 steps with owners + evidence); github.com/ganesh18kadiri/devops-skills release-readiness (6 gates: deployment safety, reliability, observability, security, operational, verification); github.com/pavelgolitsyn/speccaster release-readiness (go/no-go with accountable approvers); github.com/ababqq/claude-code-service-studios launch/release checklists (verdict precedence NO-GO > NOT ASSESSED > GO). Full URLs: https://momentic.ai/blog/qa-release-checklist **Label: Corroborated.** Confidence: medium (practitioner/vendor and community sources agree on mechanics). Implication: the gate structure in 03-quality-gates.md.

**E2. Calibrate the bar to the product: a payments service and an internal tool are not held to the same line.**
Sources: ganesh18kadiri/devops-skills release-readiness (community). **Label: Corroborated (single community source stating a widely held SRE principle).** Confidence: medium. Implication: the Tier 1/2/3 risk model in §23.

**E3. QA/Security/DevOps tracks run parallel to development from day one, not after "code complete."**
Sources: medium.com/@sohag933 BRD-to-build development-readiness gate (Sep 2026, practitioner). **Label: Corroborated (single practitioner source).** Confidence: medium. Implication: §23 §0.4.

**E4. "Conditional" (proceed with named, owned, dated open items) is the honest middle state between ready and blocked.**
Sources: medium.com/@sohag933 (same). **Label: Inferred from practitioner framing.** Confidence: medium. Adopted as Proposed gate mechanics in 03.

---

## F. Diminishing-returns log & open unknowns

- **Stopped:** further tool-by-tool comparisons (Percy vs Chromatic pricing minutiae) — does not change the methodology. Further EAA member-state penalty schedules beyond the cited examples — national-law detail for counsel, not for the gate system.
- **Unknown:** (1) whether EN 301 549 v4.1.1 has been OJEU-cited between early Sept and 2026-10-10; (2) exact current EAA fine totals (single-studio review); (3) whether DOJ will revive Title III web rulemaking; (4) WCAG 3.0 finalization date ("a few years," no commitment); (5) current flakiness rate at Google-scale (2016 figure is dated).
- **Negative evidence sought and found:** no contradiction of the Deque 57% figure in 2026 sources (consistent citation); no evidence that any overlay has survived a compliance challenge; no EAA fines for actual checkout barriers in the first 15 months despite documented barriers (C5).
- **Single-source claims needing verification before use as blocking rules:** UK PSBAR WCAG 2.2 AA (A9); "13% of WCAG 2.1 AA criteria reliably auto-flaggable" (noted in 01 §4 as uncertain); exact penalty maxima per member state.
