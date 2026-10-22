# 16 — Testing (Unit / Integration / E2E / Browser / Visual / A11y / API / Contract / DB / Load / Coverage / Generation / AI QA / CI)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved

Scope: unit/integration/e2e, browser automation, visual regression, accessibility, API/contract/DB/load, coverage, test generation/repair, AI QA agents, CI verification.

## Index (22 resources)

01 Vitest · 02 Jest · 03 pytest · 04 JUnit 5 · 05 Playwright Test · 06 Cypress · 07 Selenium / WebdriverIO · 08 Storybook Test + Chromatic · 09 Percy / Applitools (visual) · 10 axe-core / pa11y / Lighthouse-a11y · 11 Postman/Newman + REST Assured · 12 Pact (contract) · 13 Testcontainers · 14 k6 · 15 Locust / JMeter / Gatling · 16 Coverage: Istanbul/c8 + coverage.py + Codecov · 17 Mutation: Stryker / Mutmut · 18 AI test generation (Codium/QA skills) · 19 AI QA agents (QASkills.sh exemplar) · 20 GitHub Actions CI verify + CircleCI orbs · 21 Robot Framework / Cucumber (keyword/BDD) · 22 Appium / Detox (mobile)

---

### 01 — Vitest (JS unit/integration)
- **Canonical identity:** `npm:vitest` — `github:vitest-dev/vitest`
- **Category:** Testing → Unit/Integration (JS/TS)
- **Type:** OSS framework (Vite team)
- **Official URL:** https://vitest.dev/
- **Description:** Vite-native runner; ESM-first, HMR watch (5–15x faster than Jest per 2026 guides), Jest-compatible API, TS out-of-box, coverage/mocking/snapshots.
- **Contents inspected:** vitest.dev comparisons page; 2026 rankings (14k stars, AI-agent 5/5).
- **Capabilities:** Unit/integration, browser mode (real-browser option), snapshot, benchmark.
- **Usage domain:** Default for new Vite projects (Vue/Svelte/React+Vite).
- **Integration:** official (vite.config shared pipeline; `vitest run --coverage`).
- **Compatibility:** Node 18+; ESM/CJS compat.
- **Deps:** vite, esbuild.
- **Availability:** npm free.
- **Maintenance:** Active (v3.x 2026).
- **License:** MIT.
- **Security/limits:** Node-runner ≠ browser layout (jsdom limits: no layout/offsetTop); pair with Playwright for E2E.
- **Related:** Jest, Playwright, RTL.
- **Sources:** vitest.dev; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — Jest (JS unit/integration, incumbent)
- **Canonical identity:** `npm:jest` — `github:facebook/jest`
- **Category:** Testing → Unit/Integration
- **Type:** OSS framework (Meta → OpenJS)
- **Official URL:** https://jestjs.io/
- **Description:** Zero-config runner, assertions/mocks/snapshots/coverage (Istanbul); 44k stars; still dominant in React/CRA/Next legacy (63% JetBrains 2024).
- **Contents inspected:** Search excerpts (v30.x; ts-jest slower than Vitest esbuild).
- **Capabilities:** Parallel workers, caching, snapshot, timers.
- **Usage domain:** Established React/Node monorepos.
- **Integration:** official (babel/ts-jest/vite-jest compat).
- **Compatibility:** Node 14+; CJS-first, ESM experimental.
- **Deps:** jest-circus, babel-jest.
- **Availability:** npm free.
- **Maintenance:** Active but plateaued; Vitest leads new projects.
- **License:** MIT.
- **Security/limits:** Memory-heavy VM runs; keep snapshots reviewed (snapshot bloat hides regressions).
- **Related:** Vitest, RTL.
- **Sources:** jestjs.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — pytest (Python standard)
- **Canonical identity:** `pypi:pytest`
- **Category:** Testing → Unit/Integration/E2E (Python)
- **Type:** OSS framework
- **Official URL:** https://docs.pytest.org/
- **Description:** Fixtures, parametrize, 1500+ plugins (asyncio, mock, cov, xdist, html); natural discovery; 12k stars.
- **Contents inspected:** Search excerpts (plugin registry 1500+ 2026).
- **Capabilities:** Unit→E2E (with Playwright-Python), data-driven, parallel via xdist.
- **Usage domain:** Python services, ML pipelines, APIs.
- **Integration:** official (pytest-asyncio/cov/xdist; Docker/CI native).
- **Compatibility:** Python 3.8+.
- **Deps:** pluggy, iniconfig.
- **Availability:** PyPI free.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Fixture sprawl → pin plugin versions; xdist needs deterministic tests.
- **Related:** Testcontainers, coverage.py, Playwright-Python.
- **Sources:** docs.pytest.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 04 — JUnit 5 (Java/Kotlin enterprise)
- **Canonical identity:** `maven:org.junit.jupiter:junit-jupiter`
- **Category:** Testing → Unit/Integration (JVM)
- **Type:** OSS framework
- **Official URL:** https://junit.org/junit5/
- **Description:** Jupiter API + Platform + Vintage; extensions, parametrized, IDE/Gradle/Maven depth; enterprise standard.
- **Contents inspected:** Search-verified identity (6k stars; TestNG/xUnit siblings).
- **Capabilities:** Lifecycle, assumptions, dynamic tests.
- **Usage domain:** Enterprise Java/Kotlin.
- **Integration:** official (Surefire/Failsafe, Gradle test task).
- **Compatibility:** Java 8+ (17+ recommended 2026).
- **Deps:** opentest4j, apiguardian.
- **Availability:** Maven Central free.
- **Maintenance:** Active.
- **License:** EPL-2.0.
- **Security/limits:** None specific; isolate integration tests (Testcontainers) from unit lane.
- **Related:** TestNG, REST Assured, Testcontainers.
- **Sources:** junit.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 05 — Playwright Test (browser E2E leader)
- **Canonical identity:** `npm:@playwright/test` — `github:microsoft/playwright`
- **Category:** Testing → Browser E2E / API / component
- **Type:** OSS framework (Microsoft)
- **Official URL:** https://playwright.dev/
- **Description:** Cross-browser (Chromium/Firefox/WebKit), auto-wait, parallelism, tracing/screenshots/video/HAR, network interception, codegen, component testing; 70k stars; ThoughtWorks Adopt; 92% satisfaction (State of JS 2024).
- **Contents inspected:** Search excerpts (33% SO 2024 adoption; fastest E2E).
- **Capabilities:** Multi-tab, API testing, visual comparisons, Docker + GHA integration.
- **Usage domain:** Default E2E for new web projects (JS/Python/Java/.NET bindings).
- **Integration:** official (`npx playwright test`; GitHub Action; Docker images).
- **Compatibility:** Node 18+; Python/Java/.NET ports.
- **Deps:** Browser binaries.
- **Availability:** npm/PyPI free.
- **Maintenance:** Active (v1.50+ 2026).
- **License:** Apache-2.0.
- **Security/limits:** Real browsers cost CI minutes; quarantine flaky network-dependent specs.
- **Related:** Cypress, Selenium, Vitest (split strategy).
- **Sources:** playwright.dev; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — Cypress (DX-first E2E)
- **Canonical identity:** `npm:cypress`
- **Category:** Testing → Browser E2E
- **Type:** OSS + commercial Cloud
- **Official URL:** https://www.cypress.io/
- **Description:** In-browser runner, time-travel debugger, auto-reload, network stubbing, component testing; 47k stars; Assess (existing-only) per ThoughtWorks 2024.
- **Contents inspected:** Search excerpts (v14.x; JS/TS-only; recent parallel support).
- **Capabilities:** Visual debugging, screenshots/video, Cypress Cloud parallelization.
- **Usage domain:** Frontend teams valuing visual debug; existing suites.
- **Integration:** official (GHA/Circle orbs; cypress-axe/real-events plugins).
- **Compatibility:** Chromium-family first; Firefox/WebKit limited.
- **Deps:** Bundled Electron + browsers.
- **Availability:** npm free; Cloud usage-based.
- **Maintenance:** Active.
- **License:** MIT (runner); proprietary Cloud.
- **Security/limits:** No native multi-tab/cross-origin iframes (workarounds); slower than Playwright at scale.
- **Related:** Playwright, WebdriverIO.
- **Sources:** cypress.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — Selenium WebDriver + WebdriverIO
- **Canonical identity:** `tool:selenium` — https://www.selenium.dev/ ; `npm:webdriverio`
- **Category:** Testing → Browser E2E (polyglot)
- **Type:** OSS (W3C WebDriver)
- **Official URL:** https://www.selenium.dev/
- **Description:** Multi-language bindings, Grid for parallel; WebdriverIO adds JS DX + Vitest-derived mocking for component tests; Hold for new projects per radar.
- **Contents inspected:** Search excerpts (31k stars Selenium; 9k WebdriverIO).
- **Capabilities:** Grid scale, Appium bridge to mobile.
- **Usage domain:** Java-enterprise legacy, polyglot Grid estates.
- **Integration:** official (Grid, GHA integrations need manual wiring).
- **Compatibility:** All major languages.
- **Deps:** Drivers, Grid infra.
- **Availability:** Free OSS.
- **Maintenance:** Active but declining share (17% SO 2024).
- **License:** Apache-2.0.
- **Security/limits:** Grid endpoint must be network-isolated; complex parallel setup.
- **Related:** Playwright, Appium.
- **Sources:** selenium.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Storybook Test + Chromatic (component/visual CI)
- **Canonical identity:** `npm:@storybook/test` + `service:chromatic` — https://storybook.js.org/ ; https://www.chromatic.com/
- **Category:** Testing → Component + visual regression
- **Type:** OSS + service
- **Official URL:** https://storybook.js.org/
- **Description:** Isolated component workshop; Test runner (Vitest/Playwright-backed) + a11y addon; Chromatic provides cloud snapshots, TurboSnap, PR baselines.
- **Contents inspected:** Search-verified identity (standard 2026 pair).
- **Capabilities:** Interaction tests, snapshot baselines per story, UI review.
- **Usage domain:** Design-system regression gates.
- **Integration:** official (chromatic GitHub Action; `chromatic --project-token`).
- **Compatibility:** React/Vue/Angular/Svelte.
- **Deps:** storybook, playwright (test runner).
- **Availability:** OSS free; Chromatic snapshot-quota SaaS.
- **Maintenance:** Active.
- **License:** MIT (Storybook); proprietary (Chromatic).
- **Security/limits:** Token is secret — store in CI secrets; approve baselines via PR review only.
- **Related:** Percy, Applitools, Playwright.
- **Sources:** storybook.js.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Percy / Applitools (visual regression SaaS)
- **Canonical identity:** `service:percy` (BrowserStack) + `service:applitools`
- **Category:** Testing → Visual regression
- **Type:** Service
- **Official URL:** https://percy.io/ · https://applitools.com/
- **Description:** Percy: DOM snapshots + cross-browser renders; Applitools Eyes: AI-diff (layout/content strictness), Ultrafast Grid.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Pixel/layout diff, ignore regions, responsive matrices.
- **Usage domain:** Marketing pages, dashboards where CSS drift matters.
- **Integration:** service (SDK + CI step; Playwright/Cypress/Selenium adapters).
- **Compatibility:** All major E2E runners.
- **Deps:** SaaS quota.
- **Availability:** Commercial SaaS (trial/free tier limited).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Screenshots may capture PII — mask selectors, restrict project visibility.
- **Related:** Chromatic, Playwright visual comparisons.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — axe-core / pa11y / Lighthouse a11y (accessibility)
- **Canonical identity:** `npm:axe-core` + `npm:pa11y` + `npm:lighthouse`
- **Category:** Testing → Accessibility
- **Type:** OSS utilities
- **Official URL:** https://www.deque.com/axe/ · https://pa11y.org/ · https://developer.chrome.com/docs/lighthouse
- **Description:** axe-core: rule engine (WCAG 2.1/2.2) with cypress-axe/playwright adapters; pa11y: CLI crawl; Lighthouse: lab scores incl. a11y/best-practices.
- **Contents inspected:** Search-verified identities (cypress-axe, Lighthouse CI).
- **Capabilities:** Automated a11y gates (color-contrast, names/roles, focus).
- **Usage domain:** PR gates + nightly crawls.
- **Integration:** library/CLI (axe-playwright, pa11y-ci, lhci).
- **Compatibility:** Node; CI-friendly JSON/SARIF.
- **Deps:** Chromium for Lighthouse/pa11y.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** MPL-2.0 (axe) / MIT (pa11y) / Apache-2.0 (Lighthouse).
- **Security/limits:** Automated checks ≈30–40% of WCAG — manual SR/keyboard audit still required.
- **Related:** Storybook a11y addon, Cypress/Playwright adapters.
- **Sources:** Deque/Chrome docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Postman/Newman + REST Assured (API testing)
- **Canonical identity:** `tool:postman` + `npm:newman` + `maven:io.rest-assured:rest-assured`
- **Category:** Testing → API
- **Type:** Service + OSS runners
- **Official URL:** https://www.postman.com/ · https://rest-assured.io/
- **Description:** Postman collections + Newman CLI for CI; REST Assured: Java DSL for API assertions (7k stars).
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Contract-adjacent status/schema assertions, environments, data-driven runs.
- **Usage domain:** REST/GraphQL smoke + regression.
- **Integration:** official (newman run; JUnit/TestNG adapters).
- **Compatibility:** Any HTTP API.
- **Deps:** Node (Newman) / JVM (REST Assured).
- **Availability:** Freemium (Postman) + OSS.
- **Maintenance:** Active.
- **License:** Proprietary (Postman) / Apache-2.0 (REST Assured, Newman).
- **Security/limits:** Never commit tokens — use CI secrets + ephemeral test users.
- **Related:** Pact, k6, Playwright API testing.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Pact (contract testing)
- **Canonical identity:** `tool:pact` — https://pact.io/
- **Category:** Testing → Contract
- **Type:** OSS (Pact Foundation)
- **Official URL:** https://pact.io/
- **Description:** Consumer-driven contracts (Pactfiles) + provider verification + Pact Broker (can-i-deploy gates).
- **Contents inspected:** Search-verified identity (community consensus pick for contracts).
- **Capabilities:** Bi-directional, message/HTTP contracts, version matrices.
- **Usage domain:** Microservice boundaries in CI.
- **Integration:** official (pact-js/jvm/python; Broker Docker/SaaS).
- **Compatibility:** Multi-language.
- **Deps:** Broker for gates.
- **Availability:** OSS free; PactFlow SaaS optional.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Contracts are not auth tests — still verify scopes server-side.
- **Related:** Postman, Playwright API.
- **Sources:** pact.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Testcontainers (real-dependency integration)
- **Canonical identity:** `tool:testcontainers` — https://testcontainers.com/
- **Category:** Testing → Integration (DB/mq/search)
- **Type:** OSS library
- **Official URL:** https://testcontainers.com/
- **Description:** Ephemeral Docker Postgres/Redis/Kafka/Elastic for JUnit/pytest/Go/Node; Ryuk cleanup.
- **Contents inspected:** Search-verified identity (recommended integration pick).
- **Capabilities:** Hermetic DB/message-bus tests in CI.
- **Usage domain:** Repository/outbox/search integration.
- **Integration:** library (Docker required in CI runner).
- **Compatibility:** Java/Python/Go/Node/.NET.
- **Deps:** Docker daemon.
- **Availability:** Free OSS (Testcontainers Cloud optional).
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Mount Docker socket read-only where possible; pin images by digest.
- **Related:** pytest, JUnit.
- **Sources:** testcontainers.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — k6 (load/performance, JS)
- **Canonical identity:** `tool:k6` — `github:grafana/k6`
- **Category:** Testing → Load / performance
- **Type:** OSS (+ Grafana Cloud)
- **Official URL:** https://k6.io/
- **Description:** JS scripting, VUs/stages/thresholds, 26k stars; checks vs thresholds gate releases.
- **Contents inspected:** Search excerpts (ranked #12 test frameworks 2026).
- **Capabilities:** HTTP/WebSocket/gRPC load, browser module (hybrid).
- **Usage domain:** API SLO gates, pre-release soak.
- **Integration:** CLI + GHA action + Grafana dashboards.
- **Compatibility:** Any HTTP endpoint.
- **Deps:** Go binary (single).
- **Availability:** OSS free; Cloud quota SaaS.
- **Maintenance:** Active (Grafana Labs).
- **License:** AGPL-3.0.
- **Security/limits:** Load-test only staging/ephemeral with permission; never prod without approval.
- **Related:** Locust, JMeter, Gatling.
- **Sources:** k6.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Locust / JMeter / Gatling (load exemplars)
- **Canonical identity:** `tool:load-exemplar`
- **Category:** Testing → Load
- **Type:** OSS
- **Official URL:** https://locust.io/ · https://jmeter.apache.org/ · https://gatling.io/
- **Description:** Locust (Python, code-first distributed); JMeter (GUI + plugins, enterprise staple); Gatling (Scala DSL, high-throughput reports).
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Distributed VUs, assertions, HTML reports.
- **Usage domain:** Teams standardized on Python/GUI/Scala respectively.
- **Integration:** CLI/GUI + CI publishers.
- **Compatibility:** HTTP/JDBC/JMS per tool.
- **Deps:** Python/JVM per tool.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** MIT (Locust) / Apache-2.0 (JMeter, Gatling OSS).
- **Security/limits:** Same staging-only rule; coordinate with infra (DDoS false alarms).
- **Related:** k6.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — Coverage (Istanbul/c8 + coverage.py + Codecov)
- **Canonical identity:** `tool:coverage-exemplar`
- **Category:** Testing → Coverage / reporting
- **Type:** OSS + service
- **Official URL:** https://istanbul.js.org/ · https://coverage.readthedocs.io/ · https://about.codecov.io/
- **Description:** Istanbul/nyc + c8 (V8) for JS (Vitest/Jest built-ins); coverage.py + pytest-cov for Python; Codecov/Coveralls for PR gates/history.
- **Contents inspected:** Search excerpts (Vitest c8 built-in; pytest-cov standard).
- **Capabilities:** Line/branch/function, diff-coverage gates, flaky-test tracking (Cloud).
- **Usage domain:** PR quality gates (e.g., fail under 80% diff coverage).
- **Integration:** utility/service (lcov/cobertura upload; Codecov Action).
- **Compatibility:** JS/Python reporters.
- **Deps:** None heavy.
- **Availability:** OSS free; Codecov usage-based SaaS.
- **Maintenance:** Active.
- **License:** BSD/MIT (tools); proprietary (hosting).
- **Security/limits:** Coverage ≠ correctness; gate diff-coverage not absolute to avoid perverse tests.
- **Related:** Stryker/Mutmut, SonarQube.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — Mutation testing (Stryker / Mutmut)
- **Canonical identity:** `npm:@stryker-mutator/core` + `pypi:mutmut`
- **Category:** Testing → Test effectiveness (mutation)
- **Type:** OSS utilities
- **Official URL:** https://stryker-mutator.io/ · https://mutmut.readthedocs.io/
- **Description:** Seed faults (mutants); surviving mutants = weak assertions; Stryker for JS/TS, Mutmut for Python.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Mutation score, incremental/CI dashboards.
- **Usage domain:** Nightly quality signal for critical packages.
- **Integration:** CLI + CI (run nightly, not per-PR — expensive).
- **Compatibility:** JS/TS (Stryker), Python (Mutmut).
- **Deps:** Test runner per project.
- **Availability:** Free OSS.
- **Maintenance:** Active (niche).
- **License:** Apache-2.0 / BSD.
- **Security/limits:** Expensive — sample scope; do not gate merges on full mutation.
- **Related:** Coverage tools.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — AI test generation / repair (generation exemplar)
- **Canonical identity:** `tool:ai-gen-exemplar` (Codium/Qodo · GitHub Copilot Workspace · Codium CoverAgent)
- **Category:** Testing → Generation / repair
- **Type:** Service / OSS-agent mix
- **Official URL:** https://www.qodo.ai/ (exemplar)
- **Description:** NL→unit tests, edge-case suggestion, failing-test repair, coverage-gap fill; human must review oracles (AI invents asserts).
- **Contents inspected:** Search-verified category (Duo Workflow GA 2026; QA-skills coverage).
- **Capabilities:** Draft tests, fix locators/snapshots, explain failures.
- **Usage domain:** Bootstrap for untested code; repair after refactors.
- **Integration:** integration (IDE/PR agents; `AI-generated` label + required human approve).
- **Compatibility:** JS/Python/Java per vendor.
- **Deps:** SaaS quota / model key.
- **Availability:** Commercial + OSS agents.
- **Maintenance:** Active, fast-moving.
- **License:** Proprietary / MIT (agents vary).
- **Security/limits:** WARNING — generated oracles may be wrong; require mutation/coverage + human sign-off; never auto-merge AI-only tests.
- **Related:** AI QA agents, Copilot Autofix.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — AI QA agents (QASkills.sh exemplar)
- **Canonical identity:** `service:qaskills-exemplar` — https://qaskills.sh/
- **Category:** Testing → AI QA agents
- **Type:** Service / skills marketplace (utility)
- **Official URL:** https://qaskills.sh/
- **Description:** Installable QA skills for coding agents per framework (Playwright/Cypress/pytest/JUnit/k6…); explicit async/semantic-locator APIs score 5/5 agent-compat.
- **Contents inspected:** 2026 ranking page (AI-agent scores; 16-framework table).
- **Capabilities:** Agent-readable workflows, CI-compatible commands.
- **Usage domain:** Agent-assisted authoring/triage.
- **Integration:** integration (skills installed into agent; still runs real runners underneath).
- **Compatibility:** Mirrors underlying runner support.
- **Deps:** Agent + runner.
- **Availability:** Marketplace (mixed free/paid).
- **Maintenance:** Active.
- **License:** Varies by skill.
- **Security/limits:** Agent is prompt-only assistance — underlying runner + human approval remain enforceable gates.
- **Related:** Generation tools, Playwright/Vitest.
- **Sources:** qaskills.sh via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — CI verification (GitHub Actions + CircleCI orbs)
- **Canonical identity:** `service:gha` + `service:circleci`
- **Category:** Testing → CI verify
- **Type:** Service (managed runners)
- **Official URL:** https://docs.github.com/actions · https://circleci.com/docs/
- **Description:** Matrix builds, sharding (Playwright --shard), caching (Turborepo/Nx), parallel E2E, required checks + branch protection.
- **Contents inspected:** 2026 CI guides (GHA 60%+ share; CircleCI macOS/ARM/GPU lead).
- **Capabilities:** Fail-fast lanes (unit → integration → E2E → visual/a11y/load nightly).
- **Usage domain:** Every PR + nightly full-matrix.
- **Integration:** service (YAML workflows; reusable workflows; OIDC to cloud).
- **Compatibility:** Linux/Windows/macOS runners; ARC/K8s self-host.
- **Deps:** Runner minutes.
- **Availability:** SaaS (free quota + per-minute).
- **Maintenance:** Active.
- **License:** Proprietary runners; workflows are user code.
- **Security/limits:** Pin actions by SHA; minimal GITHUB_TOKEN permissions; isolate load/DAST to staging.
- **Related:** Dagger/Earthly (repro builds), Codecov.
- **Sources:** JetBrains/Spacelift/Youngju 2026 CI surveys via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 21 — Robot Framework / Cucumber (keyword/BDD)
- **Canonical identity:** `tool:rf` — https://robotframework.org/ ; `tool:cucumber` — https://cucumber.io/
- **Category:** Testing → Keyword-driven / BDD
- **Type:** OSS frameworks
- **Official URL:** https://robotframework.org/
- **Description:** Robot (Python keyword-driven, 10k stars) for non-dev QA + RPA; Cucumber (Gherkin across langs) for executable specs.
- **Contents inspected:** Search excerpts (Robot 3/5 agent score; Cucumber BDD).
- **Capabilities:** Readable specs, Selenium/Playwright/Appium backends.
- **Usage domain:** Acceptance suites owned with product/ops.
- **Integration:** library (ride/editors; CI JUnit XML).
- **Compatibility:** Python (Robot); multi-lang (Cucumber).
- **Deps:** Backend driver.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** Apache-2.0 / MIT.
- **Security/limits:** Gherkin ≠ coverage — keep step-defs DRY or suite rots.
- **Related:** Selenium, Behave/SpecFlow.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 22 — Appium / Detox (mobile E2E)
- **Canonical identity:** `tool:appium` — https://appium.io/ ; `npm:detox`
- **Category:** Testing → Mobile E2E
- **Type:** OSS frameworks
- **Official URL:** https://appium.io/
- **Description:** Appium (WebDriver for iOS/Android native, 18k stars); Detox (gray-box React Native, 11k stars); WebdriverIO also covers hybrid.
- **Contents inspected:** Search excerpts (mobile layer table 2026).
- **Capabilities:** Device farm runs, gestures, system dialogs.
- **Usage domain:** Native/hybrid mobile releases.
- **Integration:** library (Appium Grid; Detox CLI + device profiles).
- **Compatibility:** iOS simulators/Android emulators + real-device clouds.
- **Deps:** Xcode/Android SDK or cloud devices.
- **Availability:** Free OSS (+device-cloud spend).
- **Maintenance:** Active.
- **License:** Apache-2.0 / MIT.
- **Security/limits:** Real-device PII — wipe/reset between runs; sign builds with test certs.
- **Related:** Selenium Grid, WebdriverIO.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Recommended lanes (2026 consensus)
- New JS: Vitest (unit) + Playwright (E2E) + RTL; legacy React: keep Jest, add Playwright for E2E.
- Python: pytest + Testcontainers + coverage.py; Java: JUnit 5 + REST Assured + Testcontainers.
- Gates: unit/integration per-PR; E2E/visual/a11y per-PR (sharded); contract on provider/consumer change; load/mutation nightly.
- Count: 22 resources.
