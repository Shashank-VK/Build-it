# §30 — Testing (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## TE-01 — Playwright — ACTIVE
- Purpose / problem: Cross-browser end-to-end testing (Chromium/Firefox/WebKit); auto-waiting, trace viewer, UI mode; now also a target for AI agents driving browsers.
- OSS/commercial: OSS Apache-2.0 (Microsoft).
- Integration: All major languages; CI via `npx playwright install --with-deps chromium`; pairs with k6 for UX-under-load correlation.
- Maintenance: Active — **v1.62.1 (Jul 30, 2026)**.
- Limitations: Flakiness management still on the user; heavier than unit tests.
- Alternatives: Cypress, Selenium, k6 browser module.
- Switching costs: Medium (test code rewrite).
- Use: U(Verified) — ADRs in real repos (atlasppm ADR-0047, ispf-lab ADR-0006, raidan-ai testing SKILL; Sep 2026).

## TE-02 — Cypress — ACTIVE (financially stressed, shipping)
- Purpose / problem: Developer-friendly browser E2E/component testing (Electron/Chromium runner, time-travel debugging).
- OSS/commercial: OSS MIT (test runner) + commercial Cypress Cloud.
- Maintenance: Active but turbulent: **20% layoffs Jan 2023; no Series C raised**; still shipping — **Cypress 16.0.0 (Sep 1, 2026)**. Financial stress is the watch item, not maintenance.
- Limitations: Single-tab, Chromium-centric historically (Firefox/WebKit support added later); Cloud pricing for parallelization.
- Alternatives: Playwright, Selenium.
- Switching costs: Medium.
- Use: U(Proposed).

## TE-03 — Selenium — MAINTAINED
- Purpose / problem: The original browser-automation standard (WebDriver); grid for distributed runs.
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Maintained — **v4.48 (Aug 27, 2026)**; innovation pace slower than Playwright.
- Alternatives: Playwright, Cypress.
- Switching costs: Medium–high (legacy suites).
- Use: U(Verified) — legacy enterprise grids.

## TE-04 — Grafana k6 — ACTIVE (license caveat: AGPL-3.0)
- Purpose / problem: Load testing as code (Go engine, JS/TS test scripts); thresholds fail builds on percentiles; browser module for Web-Vitals UX testing; cloud scale via Grafana Cloud.
- OSS/commercial: OSS **AGPL-3.0** (engine) — **genuine blocker at companies whose legal teams treat AGPL as radioactive** (devtoollab, 2026). Grafana Labs acquired k6 in 2021 and kept the engine open source. Cloud: free 500 VUh/mo; Pro $19/mo + $0.150/VUh; Enterprise to 1M concurrent VUs.
- Maintenance: Active — **v2.2.0 (Aug 10, 2026)**; **k6 2.0 brought AI helpers** (`k6 x agent` script generation, `k6 x mcp` agent-run tests, `k6 x docs`, `k6 x explore`) and a serious browser-testing upgrade (Playwright-aligned APIs, `expect()` assertions).
- Limitations: AGPL-3.0; not a browser tool by default (browser mode separate, more expensive); cloud metering → runaway-test/runaway-invoice risk.
- Security: Load tests against prod need guardrails; cloud runs ship traffic data to Grafana.
- Alternatives: Gatling, Locust, Artillery, JMeter.
- Switching costs: Low (scripts are code).
- Use: U(Verified) — ADRs in real repos (atlasppm ADR-0047, Sep 2026: k6 chosen for load baselines; raidan-ai testing SKILL).

## TE-05 — Vitest — ACTIVE
- Purpose / problem: Vite-native unit testing (ESM-first, fast, TS-first-class); the Jest successor in Vite/Next ecosystems.
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026).
- Limitations: Vite-ecosystem coupled.
- Alternatives: Jest, Node test runner, Bun test.
- Switching costs: Low.
- Use: U(Verified) — ADR in real repo (ispf-lab ADR-0006, Sep 11, 2026: "127 tests run in ~2 s").

## TE-06 — Jest — MAINTAINED
- Purpose / problem: The incumbent JS unit-test framework (Meta).
- OSS/commercial: OSS MIT.
- Maintenance: Maintained; mindshare shifting to Vitest.
- Alternatives: Vitest, Bun test.
- Switching costs: Low.
- Use: U(Verified) — enormous legacy base.

## TE-07 — Gatling — ACTIVE
- Purpose / problem: Scala/Java-based load testing; enterprise cloud offering.
- OSS/commercial: Open-core (Apache-2.0 core) + Gatling Enterprise Cloud (Team plan ~5 hrs testing/mo).
- Maintenance: Active (2026).
- Alternatives: k6, Locust.
- Use: U(Proposed). (Lightly researched — depth debt.)

## TE-08 — Locust — ACTIVE
- Purpose / problem: Python-based distributed load testing.
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026).
- Alternatives: k6, Gatling.
- Use: U(Proposed). (Lightly researched — depth debt.)

## TE-09 — Detox — MAINTAINED
- Purpose / problem: Gray-box E2E testing for React Native.
- OSS/commercial: OSS MIT (Wix origin).
- Maintenance: Maintained (2026). (Depth debt on releases.)
- Alternatives: Maestro, Appium.
- Use: U(Proposed).

## TE-10 — Maestro (mobile.dev) — ACTIVE
- Purpose / problem: YAML-driven mobile UI testing (no SDK, no flakiness-prone selectors).
- OSS/commercial: OSS (Apache-2.0) + mobile.dev cloud.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Detox, Appium.
- Use: U(Proposed).

## TE-11 — BrowserStack / Sauce Labs — ACTIVE
- Purpose / problem: Real-device/browser cloud grids for cross-browser/mobile testing.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: LambdaTest, Playwright + CI.
- Use: U(Proposed).

## TE-12 — Chromatic (Storybook) — ACTIVE
- Purpose / problem: Visual regression testing for Storybook (screenshot diffing, UI review).
- OSS/commercial: Commercial (Chroma).
- Maintenance: Active (2026).
- Alternatives: Percy (BrowserStack), Applitools.
- Switching costs: Low–medium.
- Use: U(Proposed). (Lightly researched — depth debt.)

## TE-13 — MSW (Mock Service Worker) — ACTIVE
- Purpose / problem: API mocking at the network level for tests and dev.
- OSS/commercial: OSS MIT.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Nock, Polly.js.
- Use: U(Proposed).

## Notable status findings (testing)
- k6 — **v2.2.0 (Aug 2026)**, AI-assisted test authoring; **AGPL-3.0 is the adoption blocker to know**.
- Cypress — shipping (16.0.0 Sep 2026) but financially stressed (2023 layoffs, no Series C).
- Playwright — the 2026 default for new E2E (v1.62.1).

---

### Per-record metadata (condensed)
- k6: devtoollab.com "Best Load Testing Tools in 2026" (Sep 2026) — version, license, pricing; Medium k6 2.0 AI features (Jun 2026); grafana.com k6-browser Playwright alignment. Confidence: Medium–High.
- k6/Playwright correlation practice: Medium (Gilles Capdivila, Jan 2026), dev.to (Oct 2026). Confidence: Medium (practitioner accounts).
- Vitest/Playwright ADRs: github.com/thekovie/ispf-lab ADR-0006 (Sep 11, 2026); github.com/nicpozent/atlasppm ADR-0047; github.com/raidan-ai/opencode-settings testing SKILL. Confidence: High (primary sources).
- Cypress/Playwright/Selenium versions: summary evidence (observed 2026-10-10). Confidence: Medium–High.
