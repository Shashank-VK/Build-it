# Parts 13 + 14 — Testing, QA, Verification, Software Quality / Security, Sandboxing, Software Safety (06b-quality)

> Research workstream #12 | Verification date: 2026-10-10
> READ-ONLY research: discover, inspect, identify, verify, categorize, explain usage, record sources.
> No installing, executing, building, configuring, ranking, or recommending.
> Record count: ~95 resources + 6 verified incident records. See Coverage note at end.

## 0. Research method

### Sources searched (primary-first)
Per resource: official documentation sites, official GitHub repositories (README, docs/, releases, advisories), official CLI/docs pages, OWASP/CNCF/OpenSSF project pages, security advisories (GHSA). Secondary: technical comparisons and agent-skill repos (e.g. `testland/qa`, `craftos-dev/craftbot-agent-bundles`, `qaskills.sh`, `graycodeai/graycode-skills`, `sebduffy-prog/sebduffy` security skills) used as corroboration and for 2026-state claims; where a claim rests on secondary sources only, the record is labeled accordingly.

### Search themes used (per subcategory)
1. Unit/integration: `Jest`, `Vitest vs Jest 2026`, `pytest fixtures parametrization`, plus Java/Ruby/PHP runners
2. E2E/browser automation: `Playwright end-to-end testing official docs`, `Cypress 2026 status`, `Playwright Test Agents Planner Generator Healer official docs`
3. Visual regression: `visual regression testing tools 2026 Percy Applitools Chromatic`
4. Accessibility: `axe-core pa11y lighthouse 2026`
5. Load/perf: `k6 Locust JMeter 2026`
6. API testing: `Postman Newman REST-assured Karate Supertest 2026`; contract: `Pact contract testing 2026 Specmatic`
7. Static analysis: `Semgrep SAST 2026`, `SonarQube community edition 2026`, `ESLint Ruff Biome 2026`, `TypeScript mypy pyright 2026`, `Bandit gosec Brakeman CodeQL`
8. Coverage: `Codecov Coveralls Istanbul nyc 2026`
9. AI test generation: `Cover-Agent Diffblue CoverUp automated unit test generation 2026`
10. Dependency auditing: `OSV.dev osv-scanner 2026`, `Dependabot Renovate Socket.dev 2026`
11. Secret scanning: `gitleaks trufflehog secret scanning 2026`; secrets mgmt: `dotenvx Doppler Infisical Vault`
12. AppSec/pentest: `OWASP ZAP Nuclei 2026`, `sqlmap Metasploit Burp Suite`
13. Fuzzing: `AFL++ libFuzzer Jazzer`
14. Container scanning: `Trivy Grype 2026`; supply chain: `Sigstore SLSA OpenSSF Scorecard`, `in-toto TUF GUAC`
15. LLM security: `prompt injection detection Lakera Rebuff Garak 2026`, `LlamaGuard PurpleLlama NeMo Guardrails PyRIT promptfoo`
16. MCP security: `mcp-scan Invariant MCP security tool poisoning`
17. Sandboxes: `gVisor Firecracker Bubblewrap nsjail comparison`, `nsjail Landlock Kata Firejail 2026`, `e2b Firecracker microVM`, `Modal Vercel Sandbox Cloudflare Sandbox SDK`
18. Dev environments: `devcontainers specification CLI 2026`, `Gitpod shutdown GitHub Codespaces 2026`
19. Incidents: `Trivy GitHub Action security incident 2026`
20. Mobile/cloud grids: `Appium Maestro 2026`, `BrowserStack Sauce Labs LambdaTest 2026`, `Checkly Datadog Synthetics 2026`
21. Test management: `TestRail Zephyr Xray Qase Allure TestOps 2026`; DB/property testing: `testcontainers Hypothesis Schemathesis`; recovery: `restic Velero`

### Deduplication (already catalogued — cross-referenced, not re-researched)
Per the workstream brief these are referenced but not re-researched: `microsoft/playwright-mcp`, `michaljach/opencode-browser` / browsermcp.io, `mdc-git/opencode-playwright-interactive`, `upex-galaxy/agentic-qa-boilerplate`, `fugazi/test-automation-skills-agents`, `alibaba/open-code-review`, `waybarrios/opencode-power-pack` (/security-review), `sandervandegeijn/code-security-scanner`, `zm2231/z-audit`, `remorses/opencode-injection-guard`, `boxpositron/envsitter-guard`, `red-orbita/opencode-security-agent`, Greywall, `daytonaio/daytona` (opencode plugin), OpenCode Swarm, FlowDeck safety layer, OpenAgentsControl CodeReviewer, OpenCode native sandbox (Bubblewrap/gVisor/Firecracker/Seatbelt), Docker Sandboxes initiative, `mattolson/agent-sandbox`, `rivet-dev/sandbox-agent`, `fabianlema/opencode-sandbox` (+ variants), `athal7/opencode-devcontainers`, jailoc, `kenryu42/cc-safety-net`, Destructive Command Guard (AlexMikhalev gist), OpenGuardrails, `vercel/deepsec` (watchlist), `alonw0/secure-skills`, Pantheon-Security/medusa, Snyk ToxicSkills context.

### Verification labels (used exactly as specified)
**Verified** / **Partially verified** / **Unverified** / **Corrected** / **Archived** / **Inaccessible** / **Historical** / **Unresolved**

Conventions in this catalog: "Not verified" = not confirmed in this research pass; "Not publicly documented" = no public source found; "Not applicable" = field does not apply. Security tools' marketing claims are never repeated as fact without evidence; where only vendor/secondary claims exist the record is **Partially verified** or **Unverified**.

---

# PART 13 — TESTING, QA, VERIFICATION, SOFTWARE QUALITY

## A1. Unit & integration test frameworks

### R-01 — Jest
- **Canonical identity:** facebook/jest (Meta) — "delightful JavaScript testing" framework
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test framework (Node.js CLI + library)
- **Official URL:** https://jestjs.io (Unverified in this pass — not seen verbatim in sources)
- **Description:** All-in-one JS/TS testing framework: test runner, assertion library, mocking, snapshot testing, and coverage built in. Zero-config default; each test file runs in an isolated process with parallel execution.
- **Contents inspected:** Comparison articles citing Jest feature set (testmuai.com, browserstack.com, c-sharpcorner.com, 2026); testland/qa skill repo referencing Jest vs Vitest usage.
- **Actual capabilities (evidence):** Can test JS/TS units, integration, and (with jsdom/puppeteer) component/E2E layers; snapshot testing of rendered output; built-in code coverage; timer mocks; watch mode; TypeScript via ts-jest/babel. Evidence: multiple 2026 framework comparisons consistently describe this feature set.
- **Usage domain:** JavaScript/TypeScript unit and integration testing; React/Vue/Angular/Node projects.
- **Integration method:** npm package `jest`; CLI; CI via any runner; coverage reporters (Istanbul-based).
- **Compatibility:** Node.js; works with Babel/Webpack/Vite (with extra config); not Vite-native.
- **Dependencies:** Node.js; optional ts-jest, babel-jest, @testing-library/*.
- **Availability:** Free, open source.
- **Maintenance:** Active (Jest 30 referenced in 2026 sources, with @swc/jest performance path). Exact latest version not verified in this pass.
- **License:** MIT (widely reported; primary LICENSE not inspected this pass).
- **Security (permissions, execution risks, documented warnings):** Runs arbitrary test code with the user's privileges; no sandboxing. Not verified beyond this general property.
- **Limitations:** Slower cold start and higher memory than Vite-native runners; ESM support described as "painful" vs Vitest native (secondary sources); 2026 consensus positions it as the stable/legacy choice vs Vitest for greenfield.
- **Related resources:** Vitest (R-02), Mocha (R-04), Istanbul/nyc (R-66), testland/qa vitest-tests skill.
- **Sources:** https://www.testmuai.com/blog/jest-vs-mocha/ ; https://www.browserstack.com/guide/jest-vs-mocha-vs-jasmine ; https://tech-insider.org/vitest-vs-jest-2026/ ; https://github.com/testland/qa/blob/HEAD/./plugins/qa-unit-tests-js/skills/vitest-tests/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-02 — Vitest
- **Canonical identity:** vitest-dev/vitest — Vite-native test framework
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test framework (Node.js)
- **Official URL:** https://vitest.dev (seen verbatim in sources)
- **Description:** Unit/integration test framework built on Vite: reuses vite.config, native ESM and TypeScript, watch mode with HMR, Jest-compatible API (`describe/it/expect`, `vi.fn/vi.mock`), in-source testing via `import.meta.vitest`, built-in benchmarking (`bench`).
- **Contents inspected:** vitest.dev/guide referenced via testland/qa SKILL.md (quoted model text); 2026 migration reports (dev.to: 70,000-test Jest→Vitest migration, Vitest v4.1.6 cited March 2026).
- **Actual capabilities (evidence):** Can test JS/TS units and component/integration tests in Vite projects; coverage via @vitest/coverage-v8 or -istanbul; browser-mode testing; reported 4–10x faster than Jest in community benchmarks (secondary claims — treat as directional, Partially verified).
- **Usage domain:** Vite-based frontend (React, Vue, Svelte, Solid, Astro) and modern TS projects; CI pipelines.
- **Integration method:** npm package `vitest`; `vitest run` for single-pass CI; shares vite.config.ts.
- **Compatibility:** Node.js 20+ era; ESM-native; mostly Jest-API compatible (mechanical migration per secondary sources).
- **Dependencies:** Vite; Node.js.
- **Availability:** Free, open source.
- **Maintenance:** Very active; v4.1.6 cited March 2026.
- **License:** MIT (widely reported; not inspected this pass).
- **Security (permissions, execution risks, documented warnings):** Runs arbitrary test code with user privileges; no sandboxing. Not verified beyond this general property.
- **Limitations:** Noted weaker fit for React Native, legacy Webpack/CRA codebases, and teams with heavy existing Jest infra (secondary consensus). Cannot test native mobile apps.
- **Related resources:** Jest (R-01), Rstest (Rstack alternative, mentioned in migration report — Unverified), Istanbul/nyc (R-66).
- **Sources:** https://vitest.dev/guide/ (via skill) ; https://tech-insider.org/vitest-vs-jest-2026/ ; http://dev.to/n0th1ng_else/we-migrated-70000-tests-from-jest-to-vitest-yes-in-2-months-3lmn ; https://github.com/testland/qa/blob/HEAD/./plugins/qa-unit-tests-js/skills/vitest-tests/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-03 — pytest
- **Canonical identity:** pytest-dev/pytest — Python testing framework (originated in PyPy project)
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test framework (Python)
- **Official URL:** https://github.com/pytest-dev/pytest (seen verbatim); docs at https://docs.pytest.org (seen verbatim)
- **Description:** Python framework for unit, integration, end-to-end, and functional tests. Plain `assert` with rewritten introspection, automatic test discovery, modular fixtures (function/class/module/session scopes, conftest.py), parametrization, markers (skip/xfail), and 1300+ plugins.
- **Contents inspected:** Wikipedia infobox (stable release 9.1.1, 19 June 2026; MIT; pytest.org); agent skill docs (allthingssmitty/agent-skills py-testing SKILL.md; codeflash tessl docs) describing fixtures/parametrize.
- **Actual capabilities (evidence):** Can test any Python code: pure units, DB-backed integration (fixtures with setup/teardown), parametrized cases, async (pytest-asyncio), BDD (pytest-bdd), parallel (pytest-xdist), property-based via Hypothesis plugin, coverage via pytest-cov. Evidence: primary docs references + skill guides.
- **Usage domain:** Python unit/integration/functional testing; standard in AI/ML, backend, data projects.
- **Integration method:** `pip install pytest`; CLI; config via pytest.ini/pyproject.toml/tox.ini; CI-native.
- **Compatibility:** Python 3.9+ (3.9–3.14 per 2026 docs snapshot).
- **Dependencies:** Python; pluggy, iniconfig, packaging (standard).
- **Availability:** Free, open source.
- **Maintenance:** Active; 9.1.1 released 2026-06-19 (per Wikipedia, 2026).
- **License:** MIT.
- **Security (permissions, execution risks, documented warnings):** Runs arbitrary test code with user privileges; fixtures can open network/DB. No sandboxing.
- **Limitations:** Python-only; assertion rewriting requires its import hook; parallel execution needs plugins.
- **Related resources:** Hypothesis (R-47), Testcontainers (R-46), coverage.py/pytest-cov (R-70), unittest stdlib (below).
- **Sources:** https://en.wikipedia.org/wiki/Pytest ; https://github.com/allthingssmitty/agent-skills/blob/HEAD/skills/py-testing/SKILL.md ; https://github.com/codeflash-ai/codeflash/blob/HEAD/.tessl/tiles/tessl/pypi-pytest/docs/index.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-04 — Python unittest (stdlib) — brief
- **Canonical identity:** CPython standard library `unittest`
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Standard-library framework (Python)
- **Official URL:** Not verified in this pass
- **Description:** xUnit-style framework bundled with Python: TestCase classes, assertEqual/assertTrue family, setUp/tearDown, test discovery via `unittest.main()`.
- **Contents inspected:** Secondary tutorial content only.
- **Actual capabilities (evidence):** Can test Python units with class-based organization; less ergonomic fixtures/parametrization than pytest (secondary consensus).
- **Usage domain:** Python stdlib-only test suites; legacy projects.
- **Integration method:** Built into Python; no install.
- **Compatibility:** All Python 3.
- **Dependencies:** None.
- **Availability:** Free (PSF license, bundled).
- **Maintenance:** Maintained as part of CPython.
- **License:** PSF (bundled).
- **Security:** Same as pytest — runs arbitrary code, no sandboxing.
- **Limitations:** Verbose; weaker fixture composition and reporting vs pytest (secondary consensus).
- **Related resources:** pytest (R-03).
- **Sources:** https://dev.to/nkpydev/python-testing-unit-tests-pytest-and-best-practices-45gl
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-05 — Mocha
- **Canonical identity:** mochajs/mocha — flexible JS test framework
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test framework (Node.js)
- **Official URL:** Not verified in this pass
- **Description:** Minimal, flexible JS test runner; user pairs it with an assertion library (Chai, Node assert) and mock tools (Sinon). BDD/TDD interfaces, async via done()/async-await.
- **Contents inspected:** Comparison content (browserstack.com, testmuai.com) only.
- **Actual capabilities (evidence):** Can test Node.js units and integration; widely used with custom stacks; needs external assertion/mock libraries.
- **Usage domain:** Node.js backend unit/integration testing.
- **Integration method:** npm `mocha`; CLI.
- **Compatibility:** Node.js.
- **Dependencies:** User-chosen assertion lib.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass (no current version confirmed).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Runs arbitrary test code, no sandboxing.
- **Limitations:** No built-in assertions/mocking/coverage; more assembly required than Jest/Vitest (secondary consensus).
- **Related resources:** Jest (R-01), Vitest (R-02), Jasmine (below).
- **Sources:** https://www.browserstack.com/guide/jest-vs-mocha-vs-jasmine
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-06 — JUnit 5
- **Canonical identity:** junit-team/junit5 — Java testing framework
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test framework (JVM)
- **Official URL:** Not verified in this pass
- **Description:** Standard Java unit/integration test framework (Jupiter API); annotations, parameterized tests, extensions; paired with AssertJ (fluent assertions) and Mockito (mocks) per 2026 skill guidance.
- **Contents inspected:** craftos-dev/craftbot-agent-bundles qa-engineer role.md ("JUnit 5 default; AssertJ; Mockito").
- **Actual capabilities (evidence):** Can test Java/Kotlin units and integration; engine supports IDE/build-tool execution (secondary/skill evidence only).
- **Usage domain:** JVM unit and integration testing.
- **Integration method:** Maven/Gradle dependencies; IDE runners.
- **Compatibility:** Java 8+ (version-dependent); Kotlin.
- **Dependencies:** Build tool; optional AssertJ/Mockito.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** Eclipse Public License 2.0 (widely reported; not inspected this pass).
- **Security:** Runs arbitrary test code (JVM), no sandboxing.
- **Limitations:** Java/Kotlin/JVM only.
- **Related resources:** REST Assured (R-38), Karate (R-39), Jazzer (fuzzing, B6).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-07 — RSpec / PHPUnit / xUnit — brief group
- **Canonical identity:** rspec/rspec (Ruby); sebastianbergmann/phpunit (PHP); xunit/xunit (.NET)
- **Category:** A1 / Unit & integration test frameworks
- **Type:** Open-source test frameworks
- **Official URL:** Not verified in this pass
- **Description:** RSpec is the dominant Ruby BDD-style test framework; PHPUnit is the standard PHP unit framework; xUnit (with NUnit/MSTest) covers .NET.
- **Contents inspected:** craftos-dev/craftbot-agent-bundles qa-engineer role.md (single-line mentions: "Ruby — RSpec dominant", ".NET — xUnit / NUnit / MSTest; Moq").
- **Actual capabilities (evidence):** Can test units/integration in their respective ecosystems (skill-listing evidence only).
- **Usage domain:** Ruby / PHP / .NET testing.
- **Integration method:** Gem / Composer / NuGet packages.
- **Compatibility:** Respective runtimes.
- **Dependencies:** Ecosystem-specific.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** MIT (RSpec), BSD-3 (PHPUnit), Apache-2.0 (xUnit) — widely reported, not inspected this pass.
- **Security:** Run arbitrary test code, no sandboxing.
- **Limitations:** Single-ecosystem each.
- **Related resources:** pytest (R-03), Jest (R-01).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A2. Browser automation & end-to-end testing

### R-08 — Playwright
- **Canonical identity:** microsoft/playwright — "framework for Web Testing and Automation"
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source library + test runner (Node.js, Python, Java, .NET)
- **Official URL:** https://playwright.dev (seen verbatim); docs https://playwright.dev/docs/intro (seen verbatim); repo https://github.com/microsoft/playwright (seen verbatim)
- **Description:** Controls Chromium, Firefox, and WebKit with one API (WebSocket-based, not WebDriver HTTP). Playwright Test adds runner, web-first assertions with auto-retry, per-test browser-context isolation, parallel workers, HTML/trace/video reporters, Inspector, and codegen (record-and-generate).
- **Contents inspected:** playwright.dev/docs/test-agents.mdx and docs/src/test-agents-js.md in microsoft/playwright repo (verified Test Agents: planner/generator/healer, init-agents command, loops: vscode/claude/codex/opencode); secondary feature summaries (cheatsheets, Medium 2026).
- **Actual capabilities (evidence):** Can test full user journeys E2E across three engines; API testing via request fixtures; network interception/mocking; device emulation (mobile viewports — emulation only, not physical devices); shadow DOM; screenshots/video/trace; accessibility testing via @axe-core/playwright integration (verified via accessibility-insights comparison doc). Cannot test native mobile apps; no legacy IE11.
- **Usage domain:** Web E2E, API testing, browser automation, visual assertions, a11y checks in CI.
- **Integration method:** npm `playwright` / `@playwright/test` (+ Python/Java/.NET packages); `npx playwright install --with-deps`; CI-native; MCP server @playwright/mcp (v0.0.80 cited Sept 2026).
- **Compatibility:** Windows/macOS/Linux; JS/TS, Python, Java, C#.
- **Dependencies:** Downloaded browser binaries.
- **Availability:** Free, open source.
- **Maintenance:** Very active; v1.62.1 cited Sept 2026; Test Agents introduced v1.56.0.
- **License:** Apache-2.0.
- **Security (permissions, execution risks, documented warnings):** Launches real browsers; tests can navigate anywhere network allows; traces/videos may capture sensitive data. No sandbox beyond OS/browser defaults.
- **Limitations:** No native mobile app testing; Java/others get reduced agent-loop features vs JS/TS (secondary report: planner/generator/healer JS/TS only).
- **Related resources:** Playwright Test Agents (R-15), Cypress (R-09), Selenium (R-10), Puppeteer (R-12), axe-core (R-23), Checkly (R-91).
- **Sources:** https://playwright.dev/docs/intro ; https://github.com/microsoft/playwright.dev/blob/HEAD/nodejs/docs/test-agents.mdx ; https://github.com/microsoft/playwright/blob/HEAD/docs/src/test-agents-js.md ; https://github.com/krzemienski/lynx/blob/HEAD/COMPETITIVE-ANALYSIS.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-09 — Cypress
- **Canonical identity:** cypress-io/cypress
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source E2E + component testing framework (JS/TS)
- **Official URL:** https://docs.cypress.io (seen verbatim)
- **Description:** Runs tests inside the browser alongside the app (no WebDriver round-trip); automatic waiting/retry-ability, time-travel debugging, `cy.intercept()` network control, `cy.session()`, component testing, Test Replay (v13+), Cypress Cloud for recording/parallelization.
- **Contents inspected:** claude-mods cypress-ops SKILL.md (Cypress 14.x verified against docs.cypress.io, 2026-06); 2026 comparison content (accelq.com; medium comparison Sept 2026 noting v15-era release with HTTP/2/3 support, cy.prompt/Studio AI/tap AI tooling).
- **Actual capabilities (evidence):** Can test E2E user flows and component-level UI in real browsers (Chromium-family, Firefox, Electron); screenshots/video; visual diffing via plugins (not built-in cloud review). Cannot do multi-tab flows (architectural constraint), no WebKit/Safari engine, single-tab execution breaks some OAuth flows (secondary consensus).
- **Usage domain:** Frontend E2E and component testing for React/Vue/Angular SPAs; CI via `cypress run`.
- **Integration method:** npm `cypress`; `cypress open` / `cypress run`; Cypress Cloud optional (`--record`).
- **Compatibility:** JS/TS; Chromium, Firefox, Electron (no WebKit).
- **Dependencies:** Bundled Electron or system browsers.
- **Availability:** Free open-source core; Cypress Cloud from ~$67/mo (secondary).
- **Maintenance:** Active; 14.x–15.x in 2026 sources; download curve described as flat while Playwright's climbs (secondary).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Runs tests with full browser access to the app; Cloud uploads recordings/traces (data-handling consideration).
- **Limitations:** No Safari/WebKit engine; single-tab; parallelization/recorded results metered via Cloud; JS-only.
- **Related resources:** Playwright (R-08), Percy (R-16), Applitools (R-17).
- **Sources:** https://github.com/sadovnikovdd/claude-mods/blob/HEAD/skills/cypress-ops/SKILL.md ; https://www.accelq.com/blog/end-to-end-testing-tools/ ; https://qaskills.sh/blog/cypress-e2e-testing-ai-agents-guide
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-10 — Selenium (WebDriver)
- **Canonical identity:** SeleniumHQ/selenium — WebDriver-based browser automation
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source browser automation framework + protocol (W3C WebDriver)
- **Official URL:** Not verified in this pass
- **Description:** The long-standing cross-browser automation standard: language bindings drive browsers via WebDriver HTTP protocol; Selenium 4.x adds WebDriver BiDi (bidirectional events, network interception, console access). Grid for distributed runs; IDE record-playback.
- **Contents inspected:** 2026 comparisons (accelq.com; medium Sept 2026: "Selenium 4.47 pushed BiDi further, blocking CDP in Firefox, Safari Preview support; command execution still over HTTP so latency differs from Playwright").
- **Actual capabilities (evidence):** Can automate all major browsers incl. legacy/enterprise ones; broadest language support (Java, Python, C#, Ruby, JS...); grid scale-out. BiDi closes much of the capability gap with Playwright but not the latency profile (secondary).
- **Usage domain:** Enterprise cross-browser E2E, legacy browser coverage, multi-language teams.
- **Integration method:** Language client libraries; chromedriver/geckedriver; Selenium Grid.
- **Compatibility:** All major browsers incl. Safari/IE-mode legacy; many languages.
- **Dependencies:** Browser drivers; Java for Grid/IDE.
- **Availability:** Free, open source.
- **Maintenance:** Active (4.47 cited 2026).
- **License:** Apache-2.0 (widely reported; not inspected this pass).
- **Security:** Drivers listen on local ports (historical localhost-trust concerns); tests run with user privileges.
- **Limitations:** HTTP-protocol latency vs WebSocket/CDP tools; more flakiness without disciplined waits (secondary consensus); heavier setup.
- **Related resources:** WebdriverIO (R-11), Playwright (R-08), Appium (R-31, WebDriver-based for mobile).
- **Sources:** https://www.accelq.com/blog/end-to-end-testing-tools/ ; https://medium.com/@michael-brown-/playwright-vs-cypress-vs-selenium-in-2026-f88270cba5a2
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-11 — WebdriverIO
- **Canonical identity:** webdriverio/webdriverio — Node.js WebDriver/BiDi automation
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source test framework (Node.js)
- **Official URL:** Not verified in this pass
- **Description:** Modern Node.js wrapper over WebDriver/BiDi protocols; sync-style API, plugin ecosystem; used for web and (via Appium) mobile.
- **Contents inspected:** Single-line mentions in 2026 skill docs ("Selenium wrapper, modern").
- **Actual capabilities (evidence):** Can drive web browsers E2E and mobile via Appium services (secondary mentions only).
- **Usage domain:** JS teams wanting Selenium-compat with modern DX.
- **Integration method:** npm `@wdio/*` packages.
- **Compatibility:** Node.js; browsers via drivers.
- **Dependencies:** Node.js; drivers.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Same as Selenium (driver ports, user-privilege execution).
- **Limitations:** Inherits WebDriver latency; smaller community than Playwright/Cypress (secondary).
- **Related resources:** Selenium (R-10), Appium (R-31).
- **Sources:** https://github.com/upflame/synarc/blob/HEAD/synarc-universal/skills/sdet-engineer/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-12 — Puppeteer
- **Canonical identity:** puppeteer/puppeteer (Chrome for Testing team)
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source browser automation library (Node.js; Python port exists)
- **Official URL:** Not verified in this pass
- **Description:** CDP-based Chrome/Chromium automation: screenshots, PDFs, scraping, form automation, headless testing; also supports Firefox experimentally.
- **Contents inspected:** Single-line mentions in 2026 skill docs ("Chrome-only, headless, good for scraping").
- **Actual capabilities (evidence):** Can automate Chromium for testing/scraping/PDF generation; headless-first (secondary mentions only).
- **Usage domain:** Scraping, PDF/screenshot generation, Chrome-specific automation, smoke checks.
- **Integration method:** npm `puppeteer`; downloads Chrome for Testing.
- **Compatibility:** Chromium/Chrome primarily.
- **Dependencies:** Chrome binary.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** Apache-2.0 (widely reported; not inspected this pass).
- **Security:** Drives a full browser with user privileges; automation of untrusted pages can expose the runner to malicious content.
- **Limitations:** Chromium-centric; not a full test runner (no built-in assertions/parallel/reporting) — usually paired with Jest/Vitest (secondary consensus).
- **Related resources:** Playwright (R-08), Checkly (R-91).
- **Sources:** https://github.com/upflame/synarc/blob/HEAD/synarc-universal/skills/sdet-engineer/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-13 — TestCafe
- **Canonical identity:** DevExpress/testcafe — proxy-based E2E framework
- **Category:** A2 / Browser automation & E2E testing
- **Type:** Open-source E2E framework (Node.js)
- **Official URL:** Not verified in this pass
- **Description:** Proxy-injects test driver into the page; no browser drivers/plugins needed; works without admin rights; automatic waiting.
- **Contents inspected:** Single-line 2026 mention ("proxy-based; no browser driver; works without admin. Niche.").
- **Actual capabilities (evidence):** Can run E2E tests across browsers without WebDriver setup (secondary mention only).
- **Usage domain:** Teams needing driverless E2E with minimal install privileges.
- **Integration method:** npm `testcafe`.
- **Compatibility:** Node.js; major browsers.
- **Dependencies:** Node.js.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass — niche status per 2026 sources suggests reduced momentum; treat currency as Unverified.
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Proxy injection model executes test driver inside the page context; user-privilege execution.
- **Limitations:** Smaller ecosystem; less momentum vs Playwright/Cypress (secondary).
- **Related resources:** Cypress (R-09), Playwright (R-08).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-14 — Playwright MCP (cross-reference)
- **Canonical identity:** microsoft/playwright-mcp
- **Category:** A2 / Browser automation & E2E testing
- **Type:** MCP server (cross-referenced — dedup list)
- **Official URL:** https://github.com/microsoft/playwright-mcp (dedup brief; not re-verified)
- **Description:** Already catalogued in the prior OpenCode ecosystem catalog. Cross-referenced only per workstream dedup rules. Version 0.0.80 cited in 2026 research.
- **Sources:** https://github.com/itskshivam1318/bdai/blob/HEAD/docs/research/playwright-agents.md
- **Verification date:** 2026-10-10
- **Verification:** Unverified (dedup — see prior catalog) | **Confidence:** Not applicable

### R-15 — Playwright Test Agents (Planner / Generator / Healer)
- **Canonical identity:** microsoft/playwright — Test Agents (v1.56.0+, agent definitions + purpose-built MCP server)
- **Category:** A2 / AI testing agents (planner/generator/healer)
- **Type:** Official agent definitions (Markdown) + MCP server, shipped with Playwright
- **Official URL:** https://playwright.dev/docs/test-agents (seen verbatim); source https://github.com/microsoft/playwright/blob/HEAD/docs/src/test-agents-js.md (seen verbatim)
- **Description:** Three out-of-the-box agents: **planner** explores the app and produces a Markdown test plan; **generator** transforms the plan into Playwright Test files; **healer** executes the suite and auto-repairs failing tests. Installed via `npx playwright init-agents --loop={vscode,claude,codex,opencode}`; loops for claude/codex/copilot/opencode/vscode. The "agent" is the user's LLM; Playwright supplies system prompts, tool allowlist, and tools via its MCP server. Also ships `playwright-test-coverage.prompt.md`.
- **Contents inspected:** Official docs pages (test-agents.mdx, test-agents-js.md) — verified agent names, install command, supported loops; independent research doc verifying files under packages/playwright/src/agents/ (planner/generator/healer agent.md + coverage prompt).
- **Actual capabilities (evidence):** Can generate E2E test plans from app exploration, generate executable Playwright tests, and diagnose/repair failing tests from trace/DOM evidence. Evidence: official docs describe exactly these three capabilities; community reports show planner→specs/*.md, generator→tests/*.spec.ts, healer→patch-from-evidence workflows. Cannot guarantee repairs without human review; JS/TS only per secondary report (planner/generator/healer agents are JS/TS; Java agent CLI coverage is reduced).
- **Usage domain:** AI-assisted E2E authoring and maintenance in Playwright suites; CI healer runs on PRs.
- **Integration method:** `npx playwright init-agents`; definitions written to .claude/agents, .codex/agents, etc. + .mcp.json; regenerate after Playwright upgrades.
- **Compatibility:** Playwright 1.56+; loops: VS Code (needs v1.105+), Claude Code, Codex, OpenCode, Copilot.
- **Dependencies:** Playwright; user's AI coding agent/LLM.
- **Availability:** Free, open source (part of Playwright).
- **Maintenance:** Active; introduced v1.56.0; docs updated Sept 2026.
- **License:** Apache-2.0 (as Playwright).
- **Security (permissions, execution risks, documented warnings):** Agents drive a real browser against the app; healer modifies test code — generated patches need review; agents inherit the LLM's tool permissions in the host agent loop.
- **Limitations:** Guidance is prompt text, not enforced controls — the agent can deviate; repair quality depends on the underlying model; not a substitute for human test design (secondary reports).
- **Related resources:** Playwright (R-08), microsoft/playwright-mcp (R-14, dedup), QA Wolf/Mabl (R-74/75).
- **Sources:** https://playwright.dev/docs/test-agents ; https://github.com/microsoft/playwright/blob/HEAD/docs/src/test-agents-js.md ; https://github.com/itskshivam1318/bdai/blob/HEAD/docs/research/playwright-agents.md ; https://github.com/alexhvastovich/playwright-ai-pom-starter/blob/HEAD/docs/PLAYWRIGHT-AGENTS.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

## A3. Visual regression & screenshot comparison

### R-16 — Percy (BrowserStack)
- **Canonical identity:** BrowserStack Percy — visual testing platform
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Hosted SaaS (with open SDKs)
- **Official URL:** https://www.browserstack.com/docs/percy (seen verbatim)
- **Description:** Cross-browser screenshot capture and pixel-diff review in CI; SDKs for Playwright/Cypress/Storybook; PR integration; 2026 additions per secondary sources: Visual Review Agent (Oct 2025), MCP integration.
- **Contents inspected:** 2026 comparison articles (overlayqa.com May 2026; argos-ci.com Sept 2026; qaskills.sh Percy-vs-Applitools-vs-Chromatic; graycodeai skill table).
- **Actual capabilities (evidence):** Can capture page/component screenshots across browsers, diff against baselines, and gate PRs on visual changes; deterministic diff on cloud-re-rendered DOM snapshots (per argos-ci comparison). Cannot fix diffs itself; disciplined snapshot scoping needed to control noise/cost (secondary consensus).
- **Usage domain:** CI visual regression for web pages; teams already in BrowserStack ecosystem.
- **Integration method:** SDK packages (@percy/*), CI config, GitHub PR checks.
- **Compatibility:** Playwright, Cypress, Storybook, Selenium integrations.
- **Dependencies:** BrowserStack account; CI runner.
- **Availability:** Free tier 5,000 screenshots/mo (secondary, 2026); paid from ~$149–199/mo per secondary reports (pricing varies by source — treat as indicative).
- **Maintenance:** Active; Visual Review Agent added Oct 2025.
- **License:** Proprietary SaaS; SDKs open.
- **Security:** Screenshots of the app upload to BrowserStack cloud (sensitive UI data leaves the network — review data-handling).
- **Limitations:** Paid beyond free tier; external service dependency; pixel-diff (not AI-semantic) comparison.
- **Related resources:** Applitools (R-17), Chromatic (R-18), Argos (R-19), Playwright screenshots (R-08).
- **Sources:** https://overlayqa.com/blog/visual-regression-testing-tools/ ; https://github.com/argos-ci/argos-ci.com/blob/HEAD/articles/ai-visual-testing/index.mdx ; https://qaskills.sh/blog/percy-vs-applitools-vs-chromatic-2026 ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/testing/visual-regression-testing/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-17 — Applitools Eyes
- **Canonical identity:** Applitools Eyes — "Visual AI" testing platform
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Hosted SaaS platform
- **Official URL:** https://applitools.com/docs/ (seen verbatim)
- **Description:** AI-powered visual comparison (proprietary Visual AI) that aims to ignore rendering noise and flag "meaningful" diffs; Ultrafast Grid for cross-browser execution; layout/content/strict match levels; Storybook addon (Eyes 10.22, Jan 2026 per secondary).
- **Contents inspected:** 2026 comparison articles (overlayqa, argos-ci, momentic.ai, qaskills.sh, graycodeai skill).
- **Actual capabilities (evidence):** Can validate complex UIs across browsers/devices with reduced false positives vs raw pixel diffing (secondary consensus; vendor claim — Partially verified); checkpoints via SDKs during E2E runs. Cannot run without its cloud (hosted-only).
- **Usage domain:** Enterprise cross-browser visual validation; complex dynamic UIs; PDF/mobile surfaces.
- **Integration method:** Language SDKs; Ultrafast Grid; CI integrations (GH/GL/Jenkins/Circle).
- **Compatibility:** Major test frameworks via SDKs.
- **Dependencies:** Applitools account; network egress to Applitools cloud.
- **Availability:** Trial only on free; enterprise-quoted pricing (reported ~$399/mo entry, $10K–30K+/yr contracts — secondary, indicative).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Screenshots/DOM snapshots upload to vendor cloud; AI comparison is a black box (per argos-ci: only Applitools puts the model inside the diff itself).
- **Limitations:** Expensive; complex configuration surface; black-box diff logic harder to audit.
- **Related resources:** Percy (R-16), Chromatic (R-18).
- **Sources:** https://overlayqa.com/blog/visual-regression-testing-tools/ ; https://github.com/argos-ci/argos-ci.com/blob/HEAD/articles/ai-visual-testing/index.mdx ; https://momentic.ai/blog/best-visual-regression-testing-tools
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-18 — Chromatic
- **Canonical identity:** Chromatic (Storybook maintainers) — component visual testing
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Hosted SaaS
- **Official URL:** https://www.chromatic.com/docs/ (seen verbatim)
- **Description:** Storybook-native visual regression: auto-discovers stories, captures component snapshots in its cloud with SteadySnap anti-flake, PR review workflow; Storybook MCP servers added Mar 2026 (per argos-ci).
- **Contents inspected:** 2026 comparisons (overlayqa, argos-ci, qaskills.sh, bug0.com knowledge base).
- **Actual capabilities (evidence):** Can snapshot-test UI components in isolation across states; deterministic pixel diffing; used by 12,000+ projects (secondary claim). Cannot test full pages/flows outside Storybook (Storybook required).
- **Usage domain:** Design-system and component-library visual regression.
- **Integration method:** Chromatic CLI + Storybook; GitHub integration.
- **Compatibility:** Storybook projects (React/Vue/Angular/etc.).
- **Dependencies:** Storybook; Chromatic account.
- **Availability:** Free tier 5K snapshots/mo (secondary); paid from ~$149–179/mo (secondary, indicative); free unlimited for qualifying OSS (secondary).
- **Maintenance:** Active.
- **License:** Proprietary SaaS.
- **Security:** Story builds/screenshots upload to Chromatic cloud.
- **Limitations:** Storybook-only — weak if Storybook coverage is thin (secondary consensus).
- **Related resources:** Percy (R-16), Storybook test runner (below), Argos (R-19).
- **Sources:** https://bug0.com/knowledge-base/storybook-visual-regression-testing-chromatic ; https://overlayqa.com/blog/visual-regression-testing-tools/ ; https://qaskills.sh/blog/percy-vs-applitools-vs-chromatic-2026
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-19 — Argos CI
- **Canonical identity:** argos-ci/argos — open-source visual testing
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Open-source core + hosted SaaS
- **Official URL:** https://github.com/argos-ci (seen verbatim; docs/pricing at argos-ci.com seen verbatim)
- **Description:** PR-centered visual review with deterministic, pixel-accurate diffing and per-screenshot thresholds; AI agents review deterministic diffs via CLI/API with open-source skills (per Sept 2026 argos-ci article); unlimited parallelization.
- **Contents inspected:** argos-ci.com AI visual testing article (Sept 2026) with pricing table; overlayqa and momentic.ai comparisons.
- **Actual capabilities (evidence):** Can diff screenshots in CI with deterministic comparison and agent-assisted review; open-source engine. Evidence limited to vendor/secondary comparisons — Partially verified.
- **Usage domain:** PR-based visual review for Playwright/Cypress/Storybook teams.
- **Integration method:** SDKs/CLI; CI integration.
- **Compatibility:** Playwright, Cypress, Storybook (per comparisons).
- **Dependencies:** Argos account for hosted; self-hostable core.
- **Availability:** Free 5k/mo then $100/mo flat (vendor claim, Sept 2026).
- **Maintenance:** Active (article updated Sept 2026).
- **License:** Open source (claimed; exact license not verified this pass).
- **Security:** Screenshots upload to hosted service unless self-hosted.
- **Limitations:** Smaller ecosystem than Percy/Chromatic (secondary).
- **Related resources:** Lost Pixel (R-22 — its suggested successor), Percy (R-16).
- **Sources:** https://github.com/argos-ci/argos-ci.com/blob/HEAD/articles/ai-visual-testing/index.mdx ; https://overlayqa.com/blog/visual-regression-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-20 — BackstopJS — dormant
- **Canonical identity:** garris/BackstopJS
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Open-source CLI tool
- **Official URL:** Not verified in this pass
- **Description:** Free, self-hosted pixel-diff visual regression with HTML reports and Docker support; configurable scenarios.
- **Contents inspected:** 2026 comparison notes only.
- **Actual capabilities (evidence):** Can do screenshot comparison locally without a SaaS (secondary consensus).
- **Usage domain:** Budget/self-hosted visual regression; existing setups.
- **Integration method:** CLI; any CI.
- **Compatibility:** Headless Chrome.
- **Dependencies:** Node.js; Chrome.
- **Availability:** Free, open source.
- **Maintenance:** Dormant — last npm release 6.3.25 on 7 Sept 2024 (per overlayqa.com, May 2026). "Reasonable for an existing setup, poor for a new project."
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Fully local — no data leaves the network.
- **Limitations:** Dormant; manual review via HTML report only; no cloud dashboard; Pixel+SSIM diffing less sophisticated than AI options.
- **Related resources:** Playwright screenshots (R-08), Argos (R-19).
- **Sources:** https://overlayqa.com/blog/visual-regression-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified (dormancy claim single-source) | **Confidence:** Low-Medium

### R-21 — reg-suit / Loki / Happo — brief group
- **Canonical identity:** reg-viz/reg-suit; oblador/loki; happo/happo
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Open-source tools (reg-suit, Loki); SaaS (Happo)
- **Official URL:** Not verified in this pass
- **Description:** reg-suit: pluggable visual regression (S3/GCS storage backends). Loki: Docker-based Storybook visual testing, CLI. Happo: cloud visual diffing with cross-browser and animation-GIF diff.
- **Contents inspected:** graycodeai skill comparison table only.
- **Actual capabilities (evidence):** Can diff story/component screenshots (secondary table only).
- **Usage domain:** Component visual testing (Loki/reg-suit); animation-heavy apps (Happo).
- **Integration method:** CLI; Storybook integration.
- **Compatibility:** Storybook-centric.
- **Dependencies:** Docker (Loki); Happo account.
- **Availability:** Free OSS (reg-suit, Loki); paid SaaS (Happo).
- **Maintenance:** Not verified in this pass.
- **License:** MIT (reg-suit/Loki, widely reported); proprietary (Happo).
- **Security:** Self-hosted options keep images local.
- **Limitations:** Niche; smaller ecosystems (secondary).
- **Related resources:** Chromatic (R-18), Argos (R-19).
- **Sources:** https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/testing/visual-regression-testing/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-22 — Lost Pixel — Archived (sunsetting)
- **Canonical identity:** lost-pixel/lost-pixel
- **Category:** A3 / Visual regression & screenshot comparison
- **Type:** Open-source visual testing (sunsetting)
- **Official URL:** Not verified in this pass
- **Description:** Open-source, CI-oriented visual regression testing.
- **Contents inspected:** 2026 comparison notes (overlayqa May 2026; momentic.ai).
- **Actual capabilities (evidence):** Could do CI screenshot comparison (past capability).
- **Usage domain:** Was: open-source CI visual testing.
- **Integration method:** CI-oriented (past).
- **Compatibility:** Not verified.
- **Dependencies:** Not verified.
- **Availability:** Being retired — homepage states Lost Pixel is joining Figma and sunsetting the product; last npm release 3.22.0 on 14 Nov 2024 (per overlayqa). Argos suggested as successor.
- **Maintenance:** None (sunsetting).
- **License:** Not verified in this pass.
- **Security:** Not applicable (retiring; do not adopt).
- **Limitations:** Do not adopt for new projects.
- **Related resources:** Argos CI (R-19, suggested successor), Figma (design org).
- **Sources:** https://overlayqa.com/blog/visual-regression-testing-tools/ ; https://momentic.ai/blog/best-visual-regression-testing-tools
- **Verification date:** 2026-10-10
- **Verification:** Archived | **Confidence:** Medium

## A4. Accessibility testing

### R-23 — axe-core
- **Canonical identity:** dequelabs/axe-core — accessibility testing engine
- **Category:** A4 / Accessibility testing
- **Type:** Open-source library + CLI + browser extension (rule engine)
- **Official URL:** https://github.com/dequelabs/axe-core (seen verbatim)
- **Description:** The de-facto accessibility rule engine: runs WCAG rules against DOM, returns violations with remediation guidance; "zero false positives by design" (Deque claim, per ADR); ~57% automated WCAG detection coverage cited by 2026 skill docs (secondary claim).
- **Contents inspected:** dequelabs/axe-core repo description (via lynx COMPETITIVE-ANALYSIS.md, HTTP-200 verified 2026-04-29); serialexperimentslainnnn accessibility-standards SKILL.md (axe-core 4.12.1, MPL-2.0); multiple ADR/skill docs.
- **Actual capabilities (evidence):** Can detect WCAG 2.x violations (color contrast, ARIA, heading order, form labels, etc.) in rendered pages/components; embeds in Lighthouse, pa11y, axe DevTools, jest-axe, @axe-core/playwright, cypress-axe. Cannot test what requires manual judgment (screen-reader UX, cognitive load, keyboard-trap nuances) — manual checks remain mandatory (secondary consensus).
- **Usage domain:** Automated a11y scanning in unit/component/E2E tests and CI gates.
- **Integration method:** npm `axe-core`, `@axe-core/cli`, `@axe-core/playwright`, `jest-axe`, `cypress-axe`; browser extension.
- **Compatibility:** Any HTML/JS stack.
- **Dependencies:** Browser or jsdom-like DOM.
- **Availability:** Free, open source.
- **Maintenance:** Active (4.12.1 cited 2026).
- **License:** MPL-2.0.
- **Security:** Runs in-page; no network calls by default.
- **Limitations:** Automated checks catch roughly half of WCAG issues (secondary claim); no substitute for manual screen-reader testing.
- **Related resources:** pa11y (R-24), Lighthouse (R-25), WAVE (R-26), Accessibility Insights (R-27).
- **Sources:** https://github.com/dequelabs/axe-core ; https://github.com/krzemienski/lynx/blob/HEAD/COMPETITIVE-ANALYSIS.md ; https://github.com/serialexperimentslainnnn/claude-code-native-skills-and-settings/blob/HEAD/skills/accessibility-standards/SKILL.md ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/frontend-engineer/skills/accessibility-wcag-22-aa-axe-core/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-24 — pa11y / pa11y-ci — Corrected (license)
- **Canonical identity:** pa11y/pa11y — automated accessibility test runner (CLI + Node API)
- **Category:** A4 / Accessibility testing
- **Type:** Open-source CLI tool
- **Official URL:** https://github.com/pa11y/pa11y (seen verbatim)
- **Description:** Runs accessibility tests on pages via CLI or Node; pa11y-ci sweeps URL lists in CI; uses axe-core and HTML CodeSniffer runners; configurable WCAG standard (e.g. WCAG2AA), ignore lists, JSON reporters.
- **Contents inspected:** pa11y repo description (via lynx doc, verified 2026-04-29); craftbot pa11y-axe SKILL.md with .pa11yci.json config; serialexperimentslainnnn skill with license finding.
- **Actual capabilities (evidence):** Can scan lists of URLs for a11y violations in CI and fail builds on errors; supports actions (login flows) via config. Evidence: skill docs with working config patterns.
- **Usage domain:** CI accessibility sweeps; docs-site gating.
- **Integration method:** npm `pa11y`, `pa11y-ci`; `.pa11yci.json` config.
- **Compatibility:** Node.js; headless Chrome.
- **Dependencies:** Chrome/Chromium.
- **Availability:** Free, open source.
- **Maintenance:** Active (pa11y 9.1.1 cited 2026).
- **License:** **Corrected: LGPL-3.0-only, not MIT** — per serialexperimentslainnnn skill, checked against raw LICENSE and npm license field. Relevant if packaged/linked into a distributed product; fine as a CI tool.
- **Security:** Launches headless Chrome; scans only configured URLs.
- **Limitations:** Page-level sweeps; LGPL license caveat; relies on axe-core/HTMLCS rule coverage.
- **Related resources:** axe-core (R-23), Lighthouse CI (R-25).
- **Sources:** https://github.com/pa11y/pa11y ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/technical-writer/skills/pa11y-axe-accessibility-audit/SKILL.md ; https://github.com/serialexperimentslainnnn/claude-code-native-skills-and-settings/blob/HEAD/skills/accessibility-standards/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Corrected | **Confidence:** Medium

### R-25 — Lighthouse / Lighthouse CI
- **Canonical identity:** GoogleChrome/lighthouse — automated page-quality auditing
- **Category:** A4 / Accessibility testing (+ performance, SEO, best practices, PWA)
- **Type:** Open-source tool (DevTools/CLI/Node)
- **Official URL:** https://developer.chrome.com/docs/lighthouse/overview (seen verbatim)
- **Description:** Audits pages across performance, accessibility (a subset of axe-core rules), best practices, SEO; Lighthouse CI (@lhci/cli) gates PRs on score budgets (e.g. a11y ≥ 0.9).
- **Contents inspected:** Chrome developer docs description (via lynx doc); skill docs (gufranco thresholds; craftbot setup).
- **Actual capabilities (evidence):** Can score and audit live pages for a11y/perf/SEO; CI budgets fail builds below thresholds. Cannot replace full axe-core rule depth (its a11y category is a subset) or manual testing.
- **Usage domain:** Page-level quality gates in CI; pre-launch audits.
- **Integration method:** Chrome DevTools, `lighthouse` CLI, `@lhci/cli` with `lighthouserc`.
- **Compatibility:** Chromium.
- **Dependencies:** Chrome.
- **Availability:** Free, open source.
- **Maintenance:** Active (13.4.1 cited 2026).
- **License:** Apache-2.0.
- **Security:** Local execution; no data egress by default.
- **Limitations:** Lab data only (not field RUM); a11y subset of axe-core.
- **Related resources:** axe-core (R-23), pa11y-ci (R-24), WebPageTest (R-54).
- **Sources:** https://developer.chrome.com/docs/lighthouse/overview ; https://github.com/krzemienski/lynx/blob/HEAD/COMPETITIVE-ANALYSIS.md ; https://github.com/gufranco/claude-engineering-rules/blob/HEAD/standards/accessibility-testing.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-26 — WAVE (WebAIM)
- **Canonical identity:** WebAIM WAVE — web accessibility evaluation tool
- **Category:** A4 / Accessibility testing
- **Type:** Browser extension + online API (free tool)
- **Official URL:** Not verified in this pass
- **Description:** Visual overlay of accessibility issues on rendered pages; browser extension and API for manual/exploratory audits.
- **Contents inspected:** Mentions in 2026 skill docs (craftbot qa-engineer role.md; serialexperimentslainnnn skill: "Manual exploratory — WAVE, ARC Toolkit").
- **Actual capabilities (evidence):** Can surface a11y issues visually for manual review (secondary mentions only); not automatable in CI per skill guidance.
- **Usage domain:** Manual exploratory a11y audits.
- **Integration method:** Browser extension; API.
- **Compatibility:** Browsers.
- **Dependencies:** None.
- **Availability:** Free tool (webaim.org).
- **Maintenance:** Not verified in this pass.
- **License:** Not verified in this pass.
- **Security:** Page analysis may send URL/content to WebAIM service when using online version — check before use on sensitive pages (not verified; cautionary).
- **Limitations:** Not CI-automatable (per skill docs); manual workflow.
- **Related resources:** axe DevTools, Accessibility Insights (R-27).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-27 — Accessibility Insights for Web (Microsoft)
- **Canonical identity:** microsoft/accessibility-insights-web
- **Category:** A4 / Accessibility testing
- **Type:** Open-source browser extension (Chrome/Edge)
- **Official URL:** https://github.com/microsoft/accessibility-insights-web (seen verbatim)
- **Description:** Extension for assessing web accessibility: FastPass (quick automated checks) and Assessment (guided manual workflows).
- **Contents inspected:** Repo description via lynx COMPETITIVE-ANALYSIS.md (verified 2026-04-29).
- **Actual capabilities (evidence):** Can run automated checks plus structured manual assessment flows (repo description; secondary).
- **Usage domain:** Manual + semi-automated WCAG assessment.
- **Integration method:** Browser extension.
- **Compatibility:** Chrome/Edge.
- **Dependencies:** None.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Local extension execution.
- **Limitations:** Manual workflows not CI-gatable.
- **Related resources:** axe-core (R-23), WAVE (R-26).
- **Sources:** https://github.com/microsoft/accessibility-insights-web ; https://github.com/krzemienski/lynx/blob/HEAD/COMPETITIVE-ANALYSIS.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## A5. Cross-browser & device clouds

### R-28 — BrowserStack
- **Canonical identity:** BrowserStack — cloud testing platform
- **Category:** A5 / Cross-browser & device clouds
- **Type:** Commercial SaaS (trial only free tier)
- **Official URL:** https://www.browserstack.com (seen verbatim); https://www.browserstack.com/docs/percy (seen verbatim)
- **Description:** Cloud grid with 3,000–30,000+ browser/OS/device combinations (sources vary; "3,500+ real devices, 3,500+ browser-OS combos" per 2026 proposal doc), live interactive testing, App Automate (mobile), Test Observability with auto failure-classification + flakiness detection; SDKs for Playwright (`browserstack-node-sdk`).
- **Contents inspected:** 2026 comparisons (bugbug.io Sept 2026 pricing check; robonito.com; ishandutta2007/awesome-browser-testing-cloud); craftbot cross-browser skill (auth env vars, SDK names).
- **Actual capabilities (evidence):** Can execute Selenium/Playwright/Cypress/Appium tests on real browsers/devices at scale; parallel sessions; video/logs/HAR artifacts. Cannot test without paid plan beyond trial (trial-only free tier per comparisons).
- **Usage domain:** Enterprise cross-browser/device coverage, Safari/iOS on non-Apple hardware, geo-distributed testing.
- **Integration method:** WebDriver/Appium endpoints; SDKs; CI plugins.
- **Compatibility:** Selenium, Playwright, Cypress, Appium, Espresso, XCUITest.
- **Dependencies:** Paid account; network egress to BrowserStack.
- **Availability:** Trial only free; entry ~$29/mo, team ~$399/mo (secondary, Sept 2026 — indicative); list prices raised Feb 2026 (per bugbug.io).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Test apps/data run on vendor infrastructure; credentials via env vars (never hardcode — per skill docs); SOC2-type enterprise posture claimed (not verified this pass).
- **Limitations:** Cost scales with parallel sessions; debugging remote sessions slower than local.
- **Related resources:** Sauce Labs (R-29), LambdaTest (R-30), Percy (R-16, same company).
- **Sources:** https://bugbug.io/blog/software-testing/cloud-testing/ ; http://robonito.com/blog/post/Top-9-BrowserStack-Alternatives/ ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/cross-browser-browserstack-saucelabs-lambdatest/SKILL.md ; https://github.com/ishandutta2007/awesome-browser-testing-cloud
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-29 — Sauce Labs
- **Canonical identity:** Sauce Labs — enterprise testing cloud
- **Category:** A5 / Cross-browser & device clouds
- **Type:** Commercial SaaS
- **Official URL:** https://saucelabs.com (seen verbatim)
- **Description:** Enterprise test grid: ~7,500 real iOS/Android devices, ~1,700 emulators/simulators (per 2026 proposal), web + mobile, Sauce Connect secure tunnel, native CI + Appium/Espresso/XCUITest; `@saucelabs/playwright-runner`.
- **Contents inspected:** 2026 comparisons (bugbug.io; robonito.com); craftbot skill.
- **Actual capabilities (evidence):** Can run web/mobile tests on real devices at enterprise scale with tunnelled access to private apps (secondary consensus).
- **Usage domain:** Enterprise CI/CD device + browser grids; regulated industries.
- **Integration method:** WebDriver/Appium endpoints; Sauce Connect tunnel; CI plugins.
- **Compatibility:** Selenium, Appium, Playwright, Cypress, Espresso, XCUITest.
- **Dependencies:** Paid account.
- **Availability:** OSS-only free tier; entry ~$39–49/mo (secondary, indicative); custom enterprise.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Sauce Connect tunnel exposes private apps to vendor cloud — scope tunnel access carefully (general caution).
- **Limitations:** Higher cost; OSS-only free tier.
- **Related resources:** BrowserStack (R-28), LambdaTest (R-30), Appium (R-31).
- **Sources:** https://bugbug.io/blog/software-testing/cloud-testing/ ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/cross-browser-browserstack-saucelabs-lambdatest/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-30 — LambdaTest (TestMu AI)
- **Canonical identity:** LambdaTest — now "TestMu AI" (rebrand noted in 2026 sources)
- **Category:** A5 / Cross-browser & device clouds
- **Type:** Commercial SaaS (free tier available)
- **Official URL:** https://www.lambdatest.com/ (seen verbatim)
- **Description:** Cross-browser/device cloud positioned as lower-cost BrowserStack alternative: 3,000+ real browser/device combos; runs Selenium/Playwright/Cypress/Appium unmodified; SmartUI visual regression (AI comparison) on paid plans; auto-healing selectors.
- **Contents inspected:** 2026 comparisons (bugbug.io; robonito.com; testmuai.com rebrand evidence); craftbot skill.
- **Actual capabilities (evidence):** Can execute existing Selenium/Playwright/Cypress/Appium suites on its grid; live interactive testing; visual regression via SmartUI (secondary).
- **Usage domain:** Cost-sensitive cross-browser/device coverage; mid-size teams.
- **Integration method:** WebDriver/Appium endpoints; LT tunnel; `LT_USERNAME`/`LT_ACCESS_KEY`.
- **Compatibility:** Selenium, Playwright, Cypress, Appium.
- **Dependencies:** Account (free tier available).
- **Availability:** Free tier with capped time; entry ~$15/mo, team ~$119/mo for 5 users (secondary, indicative).
- **Maintenance:** Active; rebranded toward "TestMu AI" with AI QA positioning (2026).
- **License:** Proprietary.
- **Security:** Same cloud-execution cautions as peers.
- **Limitations:** Smaller device fleet than BrowserStack/Sauce per comparisons; SmartUI on paid plans only.
- **Related resources:** BrowserStack (R-28), Sauce Labs (R-29).
- **Sources:** https://www.testmuai.com/blog/best-mobile-app-testing-framework/ ; http://robonito.com/blog/post/Top-9-BrowserStack-Alternatives/ ; https://bugbug.io/blog/software-testing/cloud-testing/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## A6. Mobile app testing

### R-31 — Appium
- **Canonical identity:** appium/appium — cross-platform mobile automation
- **Category:** A6 / Mobile app testing
- **Type:** Open-source automation server (Node.js) + drivers
- **Official URL:** Not verified in this pass (appium.io known; unverified)
- **Description:** WebDriver-protocol server for native/hybrid mobile apps: driver-based plugin architecture (2.x/3.x — server is thin shell, drivers provide iOS/Android automation); official `appium/appium-mcp` MCP server noted in 2026 research. Current stable 3.4.2 cited May 2026 (secondary).
- **Contents inspected:** 2026 mobile testing guides (softwareqaservice.com; testmuai.com Oct 2026; christama/qa-skills mobile-testing SKILL.md with 3.x details; powerbeef on-device research).
- **Actual capabilities (evidence):** Can automate native iOS/Android apps (install, gestures, biometrics, radios, process lifecycle), plus mobile web; real-device and emulator/simulator. Cannot match Maestro's authoring speed for simple flows; iOS real-device requires Apple signing/provisioning (secondary).
- **Usage domain:** Cross-platform native mobile E2E; device-farm execution.
- **Integration method:** Appium server + language clients; W3C capabilities; runs on device clouds.
- **Compatibility:** iOS (XCUITest driver), Android (UiAutomator2), Windows/macOS drivers.
- **Dependencies:** Node.js; platform SDKs (Xcode/Android SDK); signing for iOS devices.
- **Availability:** Free, open source.
- **Maintenance:** Active (3.x in 2026).
- **License:** Apache-2.0 (widely reported; not inspected this pass).
- **Security:** Controls physical devices; capabilities include app install — restrict server network exposure.
- **Limitations:** Slower/brittler than Maestro for simple flows (secondary); setup complexity (drivers, signing).
- **Related resources:** Maestro (R-32), Detox (R-33), WebdriverIO (R-11), BrowserStack/Sauce Labs (R-28/29).
- **Sources:** https://softwareqaservice.com/blog/mobile-app-testing-in-2026-devices-automation-real-world-users ; https://github.com/christama/qa-skills/blob/HEAD/skills/mobile-testing/SKILL.md ; https://www.testmuai.com/blog/mobile-app-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-32 — Maestro
- **Canonical identity:** mobile-dev-inc/maestro — YAML mobile UI automation
- **Category:** A6 / Mobile app testing
- **Type:** Open-source CLI (with Maestro Cloud SaaS)
- **Official URL:** Not verified in this pass
- **Description:** Declarative YAML flows for mobile E2E; single CLI binary, zero driver config; built-in retry logic absorbing timing flakiness; AI-assisted authoring (plain-English→YAML; `assertVisible` without selectors); CLI 2.5.x cited Apr 2026.
- **Contents inspected:** 2026 mobile guides (testmuai.com: "fastest-growing mobile testing framework in 2026"; christama skill: 2.5.x; powerbeef research on iOS real-device limits; diegonava150 ADR-008).
- **Actual capabilities (evidence):** Can author/run cross-platform mobile flows fast on Android (emulators + real devices) and iOS simulators; cloud real-device iOS via Maestro Cloud/TestingBot/BrowserStack. Cannot do local physical iOS (officially unsupported — iOS simulator only locally; community patches exist but are unofficial/version-locked). Cannot express deep native gesture/biometric or precise timing assertions as well as Appium/Detox (secondary).
- **Usage domain:** Cross-platform mobile E2E for mixed-skill teams; fast iteration.
- **Integration method:** Single CLI binary; CI command; Maestro Cloud for scale.
- **Compatibility:** Android, iOS simulators; React Native, Flutter, native.
- **Dependencies:** Java/Node toolchain (per secondary).
- **Availability:** Free OSS CLI; Maestro Cloud paid.
- **Maintenance:** Active (2.5.x Apr 2026).
- **License:** Apache-2.0 (widely reported; not inspected this pass).
- **Security:** Drives apps on devices/emulators; cloud runs upload app binaries.
- **Limitations:** No local real-device iOS; less programmatic control than Appium.
- **Related resources:** Appium (R-31), Detox (R-33).
- **Sources:** https://www.testmuai.com/blog/best-mobile-app-testing-framework/ ; https://github.com/christama/qa-skills/blob/HEAD/skills/mobile-testing/SKILL.md ; https://github.com/powerbeef/qwenvoice/blob/HEAD/docs/reference/on-device-ui-testing-research-report.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-33 — Detox
- **Canonical identity:** wix/Detox — gray-box React Native testing
- **Category:** A6 / Mobile app testing
- **Type:** Open-source framework (JS)
- **Official URL:** Not verified in this pass
- **Description:** Gray-box E2E for React Native: synchronizes with the RN bridge (animations, network, timers) to eliminate timing flakiness; 20.51+ adds `by.type()` semantic matching and RN 0.83 + iOS 26 support (per 2026 skill).
- **Contents inspected:** christama/qa-skills mobile-testing SKILL.md only.
- **Actual capabilities (evidence):** Can test React Native apps with low flake via bridge synchronization (secondary only).
- **Usage domain:** React Native E2E.
- **Integration method:** npm `detox`; `.detoxrc.js` config.
- **Compatibility:** React Native; iOS/Android.
- **Dependencies:** RN toolchain; devices/simulators.
- **Availability:** Free, open source.
- **Maintenance:** Active per 2026 skill (20.51+).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Device/simulator control; user-privilege execution.
- **Limitations:** React Native only.
- **Related resources:** Appium (R-31), Maestro (R-32).
- **Sources:** https://github.com/christama/qa-skills/blob/HEAD/skills/mobile-testing/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A7. API & service testing

### R-34 — Postman / Newman
- **Canonical identity:** Postman — API platform; Newman — CLI collection runner
- **Category:** A7 / API & service testing
- **Type:** Commercial GUI client + open-source CLI runner
- **Official URL:** https://www.postman.com (seen verbatim); Newman at https://github.com/postmanlabs/newman (seen verbatim)
- **Description:** GUI API client with collections, environments, pre-request/test scripts; Newman runs collections headless in CI and is the standard pipeline runner. 2026 secondary sources note Postman Insights, AI assistant "Postbot", MCP server for API discovery.
- **Contents inspected:** github.com/postmanlabs/newman repo description (via lynx doc, verified 2026-04-29); 2026 tool comparisons (blazemeter.com Mar 2026; craftbot api-testing SKILL.md; bugbug.io API testing Oct 2026).
- **Actual capabilities (evidence):** Can author/execute assertions against REST/GraphQL/gRPC APIs, chain requests, run data-driven suites in CI via Newman; can monitor via Postman Monitors. Cannot enforce contract conformance across consumer/provider (that's Pact); cannot property-generate payloads (that's Schemathesis/Hypothesis).
- **Usage domain:** API functional/integration testing; exploratory API work; docs.
- **Integration method:** Collection JSON; Newman CLI; monitors; MCP server.
- **Compatibility:** REST, SOAP, GraphQL, gRPC, WebSocket.
- **Dependencies:** Postman account for cloud sync (local Scratch Pad deprecated — secondary).
- **Availability:** Free tier; paid plans per user.
- **Maintenance:** Active.
- **License:** Proprietary (client); Newman open-source (Apache-2.0, widely reported).
- **Security:** API keys/secrets in environments sync to Postman cloud unless stored locally (use vault/current-value masking per skill docs); test scripts execute JS.
- **Limitations:** Cloud-centric direction; limited contract/governance vs dedicated tools.
- **Related resources:** Bruno (R-35), REST-assured (R-36), Karate (R-37), Pact (R-40), WireMock (R-39).
- **Sources:** https://github.com/postmanlabs/newman ; https://www.blazemeter.com/blog/api-testing-tools ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/api-testing-postman-rest-assured/SKILL.md ; https://bugbug.io/blog/software-testing/api-testing/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-35 — Bruno
- **Canonical identity:** usebruno/bruno — open-source API client
- **Category:** A7 / API & service testing
- **Type:** Open-source desktop client (Electron) + CLI (`bru` runner)
- **Official URL:** https://github.com/usebruno/bruno (seen verbatim)
- **Description:** Git-friendly API client: collections as plain-text Bru files in-repo; runs headless via `bru`; 2026 secondary lists rank it as the leading Postman alternative.
- **Contents inspected:** 2026 comparisons (bugbug.io API testing Oct 2026; blazemeter Mar 2026); craftbot api-testing skill mention.
- **Actual capabilities (evidence):** Can author/version/run API requests and assertions with collections committed to git; CI via bru CLI (secondary consensus).
- **Usage domain:** Git-first API testing without cloud lock-in.
- **Integration method:** Bru files in repo; `bru run` in CI.
- **Compatibility:** REST/GraphQL/WebSocket/gRPC (per comparisons; 2026).
- **Dependencies:** Node.js for CLI.
- **Availability:** Free, open source (community edition); paid Pro plans.
- **Maintenance:** Active.
- **License:** Apache-2.0 (community, widely reported; not inspected this pass).
- **Security:** Secrets stored in local `.env`-style vault files — keep them out of git (general caution).
- **Limitations:** Smaller ecosystem/integrations than Postman (secondary).
- **Related resources:** Postman/Newman (R-34), Insomnia (Kong — secondary mention).
- **Sources:** https://bugbug.io/blog/software-testing/api-testing/ ; https://www.blazemeter.com/blog/api-testing-tools ; https://github.com/usebruno/bruno
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-36 — REST-assured
- **Canonical identity:** rest-assured/rest-assured — Java DSL for REST API testing
- **Category:** A7 / API & service testing
- **Type:** Open-source Java library
- **Official URL:** https://github.com/rest-assured/rest-assured (seen verbatim)
- **Description:** BDD-style Java DSL (`given/when/then`) for testing REST endpoints; JSON Schema validation; Spring integration; used with TestNG/JUnit; Java 21+/Kotlin support per 2026 skill docs.
- **Contents inspected:** craftbot api-testing-postman-rest-assured SKILL.md; restassured.io references in comparisons.
- **Actual capabilities (evidence):** Can write readable API assertions in JVM test suites, validate JSON schemas, integrate with Spring MockMvc (secondary consensus).
- **Usage domain:** JVM-backend API testing.
- **Integration method:** Maven/Gradle dependency in test code.
- **Compatibility:** JVM; REST/HTTP; Spring.
- **Dependencies:** JUnit/TestNG; app under test.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 skill citations).
- **License:** Apache-2.0 (widely reported; not inspected this pass).
- **Security:** Test-only library; no network by default.
- **Limitations:** Java/Kotlin only; REST-centric.
- **Related resources:** Supertest (R-37 group), Karate (R-37).
- **Sources:** https://github.com/rest-assured/rest-assured ; https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/api-testing-postman-rest-assured/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-37 — Karate / Supertest / pytest-fastapi family — API test frameworks group
- **Canonical identity:** karatelabs/karate (BDD API testing); supertest (Node HTTP assertions); pytest-based API testing
- **Category:** A7 / API & service testing
- **Type:** Open-source frameworks
- **Official URL:** Not verified in this pass
- **Description:** Karate: BDD Gherkin-syntax API/microservice testing with parallel execution and reports, no Java required for scenarios. Supertest: fluent HTTP assertions against Express apps in Node tests. pytest + requests/httpx/FastAPI TestClient: Python API testing.
- **Contents inspected:** 2026 comparisons (blazemeter Mar 2026; bugbug.io Oct 2026: "Karate — BDD-style, minimal code"; powerbeef ADR-008: "API tests — REST Assured, Supertest, Karate"; christama skill).
- **Actual capabilities (evidence):** Can test APIs in code-first suites with parallel execution and reporting (Karate); can assert on live HTTP servers (Supertest) (secondary consensus).
- **Usage domain:** Code-driven API regression suites; BDD-style specs (Karate).
- **Integration method:** Language test frameworks; CLI (Karate).
- **Compatibility:** Java (Karate); Node (Supertest); Python (pytest).
- **Dependencies:** App under test.
- **Availability:** Free, open source.
- **Maintenance:** Active per 2026 citations.
- **License:** MIT (Karate); MIT (Supertest) (widely reported; not inspected this pass).
- **Security:** Test-only; no network by default.
- **Limitations:** Code-first (except Karate's BDD) — less approachable than GUI clients.
- **Related resources:** REST-assured (R-36), Schemathesis (R-38).
- **Sources:** https://www.blazemeter.com/blog/api-testing-tools ; https://bugbug.io/blog/software-testing/api-testing/ ; https://github.com/powerbeef/qwenvoice/blob/HEAD/docs/reference/on-device-ui-testing-research-report.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-38 — Schemathesis — property-based API fuzzing
- **Canonical identity:** schemathesis/schemathesis — property-based testing for APIs
- **Category:** A7 / API & service testing (property-based / fuzzing)
- **Type:** Open-source tool + CLI (Python) with commercial UI
- **Official URL:** https://github.com/schemathesis/schemathesis (seen verbatim)
- **Description:** Derives Hypothesis-style test cases from OpenAPI/GraphQL schemas: stateful sequences, auth, targeted checks; version 4.27.3 released 2026-09-17 (per bugbug.io changelog listing); MIT-licensed open core with commercial Schemathesis.io UI.
- **Contents inspected:** 2026 comparisons (bugbug.io API testing: feature description + 4.27.3 changelog; ai-code-review-qa skill: "Python property-based (PBT) API testing and fuzzing"; 2026 AI-quality ADR: "fuzzing — Schemathesis").
- **Actual capabilities (evidence):** Can auto-generate API test cases from schemas and find edge-case failures humans miss (secondary consensus; vendor claims).
- **Usage domain:** Schema-driven API fuzzing; regression via recorded cases.
- **Integration method:** `schemathesis` CLI; pytest plugin; CI.
- **Compatibility:** OpenAPI 2/3, GraphQL; pytest.
- **Dependencies:** Python; API schema.
- **Availability:** Free OSS; commercial UI paid.
- **Maintenance:** Active (4.27.3, Sept 2026).
- **License:** MIT (open core, widely reported).
- **Security:** Sends generated (possibly malformed) traffic to target API — run against test environments, not production (general caution).
- **Limitations:** Needs an accurate schema; may produce false positives on loose schemas (secondary).
- **Related resources:** Hypothesis (R-43), Dredd (R-39 group), Prism (R-39 group).
- **Sources:** https://github.com/schemathesis/schemathesis ; https://bugbug.io/blog/software-testing/api-testing/ ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-39 — WireMock / Prism / Dredd — API simulation & contract checking group
- **Canonical identity:** wiremock/wiremock (API mocking); stoplightio/prism (mock from OpenAPI); apiaryio/dredd (contract testing)
- **Category:** A7 / API & service testing
- **Type:** Open-source tools
- **Official URL:** https://github.com/wiremock/wiremock (WireMock repo seen verbatim); Prism/Dredd URLs not verified in this pass
- **Description:** WireMock: HTTP API simulator/templating, recording, fault injection; runs standalone, JVM, Docker, or in the cloud (v3.13.2 cited 2026). Prism: mock server from OpenAPI with contract validation. Dredd: HTTP API testing framework validating implementations against API Blueprint/OpenAPI descriptions.
- **Contents inspected:** wiremock repo description (via lynx doc, verified 2026-04-29); 2026 comparisons (bugbug.io API testing Oct 2026; blazemeter; restfulapi.net "API contract testing tools" listing Prism, Dredd, Specmatic, Pact).
- **Actual capabilities (evidence):** Can simulate APIs for integration tests (WireMock), validate requests/responses against OpenAPI contracts (Prism, Dredd) (secondary consensus).
- **Usage domain:** Test doubles for external APIs; contract validation in CI.
- **Integration method:** Standalone server/Docker/JVM (WireMock); CLI (Prism, Dredd).
- **Compatibility:** HTTP/REST; OpenAPI.
- **Dependencies:** Java (WireMock standalone); Node (Prism/Dredd).
- **Availability:** Free OSS; WireMock Cloud paid.
- **Maintenance:** WireMock active; **Dredd archived** — apiaryio/dredd archived May 2024 (per bugbug.io). Prism status not verified this pass.
- **License:** Apache-2.0 (WireMock, widely reported); MIT (Dredd, Prism — not inspected this pass).
- **Security:** Mock servers only bind test ports; no production traffic.
- **Limitations:** Dredd is archived — do not adopt; mocks can drift from real APIs (general).
- **Related resources:** Pact (R-40), Specmatic (R-41), Schemathesis (R-38).
- **Sources:** https://github.com/wiremock/wiremock ; https://bugbug.io/blog/software-testing/api-testing/ ; https://restfulapi.net/api-contract-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified (WireMock) / Archived (Dredd) | **Confidence:** Medium/Low

## A8. Contract testing

### R-40 — Pact / PactFlow
- **Canonical identity:** pact-foundation/pact — consumer-driven contract testing; PactFlow — commercial management
- **Category:** A8 / Contract testing
- **Type:** Open-source framework (multi-language) + commercial platform
- **Official URL:** Not verified in this pass (docs.pact.io known; unverified)
- **Description:** Consumer-driven contracts: consumers define expectations, providers verify; Pact Broker/PactFlow manage contract versions; language SDKs (pact-python, pact-js, pact-jvm, etc.).
- **Contents inspected:** 2026 tool lists (bugbug.io API testing: "Pact — contract testing, 20.4.0"; ai-code-review-qa skill: "contract testing — Pact, Spring Cloud Contract"; restfulapi.net listing).
- **Actual capabilities (evidence):** Can prevent breaking API changes by verifying provider against consumer-recorded contracts in CI (secondary consensus); supports event/message contracts.
- **Usage domain:** Microservice contract governance.
- **Integration method:** Language SDKs; Pact Broker; CI verification steps.
- **Compatibility:** JS, JVM, Python, .NET, Go, Ruby; HTTP + message queues.
- **Dependencies:** Pact Broker (self-host OSS or PactFlow).
- **Availability:** Free OSS; PactFlow paid.
- **Maintenance:** Active (20.4.0 cited 2026).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Contract files are test artifacts; broker needs access control for publishing (general caution).
- **Limitations:** Consumer-driven model needs discipline; contracts can lag (secondary).
- **Related resources:** Specmatic (R-41), Spring Cloud Contract (R-41 group), Prism (R-39).
- **Sources:** https://bugbug.io/blog/software-testing/api-testing/ ; https://restfulapi.net/api-contract-testing-tools/ ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-41 — Specmatic / Spring Cloud Contract / Optic (archived) — contract testing group
- **Canonical identity:** znsio/specmatic (contract-driven development); spring-cloud/spring-cloud-contract (JVM); opticdev/optic (API diff — archived Jan 2026)
- **Category:** A8 / Contract testing
- **Type:** Open-source tools
- **Official URL:** Not verified in this pass
- **Description:** Specmatic: executable contracts as the source of truth (OpenAPI/asyncAPI), generates tests/stubs from specs. Spring Cloud Contract: JVM contract DSL with stub generation for Spring apps. Optic: API changelog/diff tooling — archived January 2026.
- **Contents inspected:** 2026 comparisons (restfulapi.net; ai-code-review-qa skill; opticdev/optic archived Jan 2026 per search).
- **Actual capabilities (evidence):** Can generate contract tests and service stubs from OpenAPI (Specmatic); can verify Spring consumers/providers (SCC) (secondary consensus). Optic: no longer maintained.
- **Usage domain:** Contract-first API development (Specmatic); Spring microservices (SCC).
- **Integration method:** CLI/CI (Specmatic); Maven/Gradle plugins (SCC).
- **Compatibility:** OpenAPI/AsyncAPI (Specmatic); JVM/Spring (SCC).
- **Dependencies:** API specs.
- **Availability:** Free OSS (Specmatic open core; commercial extensions).
- **Maintenance:** Active (Specmatic, SCC); **Optic archived Jan 2026 — do not adopt.**
- **License:** Not verified in this pass.
- **Security:** Test tooling; standard CI permissions.
- **Limitations:** Specmatic is contract-first — requires spec discipline (secondary).
- **Related resources:** Pact (R-40), Dredd (R-39, archived).
- **Sources:** https://restfulapi.net/api-contract-testing-tools/ ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified / Archived (Optic) | **Confidence:** Low-Medium

## A9. Database & property-based testing

### R-42 — Testcontainers
- **Canonical identity:** testcontainers/testcontainers-java (plus -go, -node, -python, -dotnet, -rust)
- **Category:** A9 / Database & integration testing
- **Type:** Open-source test libraries (multi-language)
- **Official URL:** Not verified in this pass
- **Description:** Spins real Docker containers (Postgres, Redis, Kafka, etc.) for integration tests; disposable per-test databases/queues/browsers.
- **Contents inspected:** 2026 skill/docs mentions (craftbot qa-engineer role.md: "Integration testing — Testcontainers"; serialexperimentslainnnn skill: "Postgres via Testcontainers"; powerbeef ADR-008: "integration — Testcontainers").
- **Actual capabilities (evidence):** Can run integration tests against real services instead of mocks (secondary consensus; widely established).
- **Usage domain:** Integration testing with real dependencies.
- **Integration method:** Language test libraries; JUnit/Testcontainers lifecycle.
- **Compatibility:** Java, Go, Node, Python, .NET, Rust; Docker.
- **Dependencies:** Docker daemon.
- **Availability:** Free OSS; Testcontainers Cloud paid option (secondary).
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Runs Docker containers in CI/dev — containers execute real services; keep images pinned (general caution).
- **Limitations:** Docker required; slower than in-memory fakes (secondary).
- **Related resources:** WireMock (R-39), Docker (Part 14 B11 context).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md ; https://github.com/serialexperimentslainnnn/claude-code-native-skills-and-settings/blob/HEAD/skills/accessibility-standards/SKILL.md ; https://github.com/powerbeef/qwenvoice/blob/HEAD/docs/reference/on-device-ui-testing-research-report.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-43 — Hypothesis (Python property-based testing)
- **Canonical identity:** HypothesisWorks/hypothesis
- **Category:** A9 / Property-based testing
- **Type:** Open-source Python library
- **Official URL:** Not verified in this pass
- **Description:** Property-based test generation: strategies produce inputs, shrinkers minimize failing examples; the engine behind Schemathesis's API fuzzing.
- **Contents inspected:** ai-code-review-qa skill (schemathesis description references Hypothesis-style cases); general 2026 skill mentions.
- **Actual capabilities (evidence):** Can generate edge-case inputs and shrink failures to minimal repros (secondary consensus; widely established).
- **Usage domain:** Unit/property tests; API fuzzing via Schemathesis.
- **Integration method:** pytest plugin/decorators.
- **Compatibility:** Python.
- **Dependencies:** pytest.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MPL-2.0 (widely reported; not inspected this pass).
- **Security:** Test-only; no network.
- **Limitations:** Python-only; property-writing has a learning curve (secondary).
- **Related resources:** Schemathesis (R-38), fast-check (JS equivalent — secondary mention).
- **Sources:** https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## A10. Load & performance testing

### R-44 — k6 (Grafana)
- **Canonical identity:** grafana/k6 — developer-centric load testing
- **Category:** A10 / Load & performance testing
- **Type:** Open-source CLI (Go) + cloud (Grafana Cloud k6)
- **Official URL:** https://github.com/grafana/k6 (seen verbatim)
- **Description:** JS-scripted load testing CLI with thresholds/checks, multiple executor types (ramping VUs), and a browser module; version 1.6.1 released 2026-02-16 (per bugbug.io). MCP server grafana/mcp-k6 (formerly mcp-k6) exposes k6 docs/tools to AI agents (per 2026 MCP research).
- **Contents inspected:** bugbug.io load testing tools (Aug 2026) with feature/changelog detail; 2026 agent-skill docs mentioning mcp-k6.
- **Actual capabilities (evidence):** Can script load scenarios in JS, assert on thresholds (p95 latency, error rate), run distributed/cloud execution, and drive real browsers; agents can query k6 docs via its MCP server (secondary).
- **Usage domain:** API/endpoint load testing; CI perf budgets.
- **Integration method:** CLI; JS test scripts; CI; Grafana Cloud.
- **Compatibility:** HTTP/WebSocket/gRPC; JS.
- **Dependencies:** Go binary; target system.
- **Availability:** Free OSS; Grafana Cloud k6 paid for scale.
- **Maintenance:** Active (1.6.1, Feb 2026).
- **License:** **AGPL-3.0** (open core; cloud/enterprise extensions proprietary) — copyleft matters if embedding/modifying.
- **Security:** Generates real load — only run against staging or with explicit production authorization (general caution).
- **Limitations:** AGPL license; browser module less mature than Playwright (secondary).
- **Related resources:** Locust (R-45), JMeter (R-46), Gatling (R-47), Artillery (R-48), mcp-k6 (MCP).
- **Sources:** https://bugbug.io/blog/software-testing/load-testing-tools/ ; https://github.com/grafana/k6
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-45 — Locust
- **Canonical identity:** locust/locust — Python load testing
- **Category:** A10 / Load & performance testing
- **Type:** Open-source framework (Python)
- **Official URL:** Not verified in this pass
- **Description:** Python-scripted distributed load testing with web UI; locust-mcp (QAInsights) gives AI agents k6-style tooling for Locust per 2026 MCP research. Locust Cloud (commercial SaaS) closed end of 2025 (secondary).
- **Contents inspected:** bugbug.io load testing tools (Aug 2026); graycode ai-code-review-qa skill ("load testing — k6, Locust, Artillery").
- **Actual capabilities (evidence):** Can script user behavior in Python and distribute load across workers with live web UI (secondary consensus).
- **Usage domain:** Python-team load testing; custom protocols.
- **Integration method:** Python scripts; CLI/web UI; distributed workers.
- **Compatibility:** Python; any HTTP/custom protocol.
- **Dependencies:** Python.
- **Availability:** Free OSS; **Locust Cloud closed 2025-12** — self-host only now.
- **Maintenance:** Active OSS (2026 citations).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Real load generation — staging-only by default (general caution).
- **Limitations:** Python performance ceiling per worker; no hosted option since Cloud closure.
- **Related resources:** k6 (R-44), JMeter (R-46).
- **Sources:** https://bugbug.io/blog/software-testing/load-testing-tools/ ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-46 — Apache JMeter
- **Canonical identity:** Apache JMeter — load testing (ASF)
- **Category:** A10 / Load & performance testing
- **Type:** Open-source Java application (GUI + CLI)
- **Official URL:** Not verified in this pass
- **Description:** Mature GUI/CLI load tester: thread groups, samplers for HTTP/JDBC/JMS, plugins; still the enterprise default in 2026 comparisons.
- **Contents inspected:** bugbug.io load testing tools (Aug 2026); 2026 skill mentions.
- **Actual capabilities (evidence):** Can build complex multi-protocol load plans with assertions and distributed execution (secondary consensus).
- **Usage domain:** Enterprise load testing; protocol breadth.
- **Integration method:** GUI plan files (.jmx); CLI/CI; BlazeMeter cloud.
- **Compatibility:** Java; HTTP, JDBC, JMS, FTP, more.
- **Dependencies:** JVM.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (ASF).
- **Security:** Load generation caution as above; JMX files are XML — review untrusted plans (general caution).
- **Limitations:** GUI-centric authoring; resource-heavy (secondary).
- **Related resources:** Gatling (R-47), k6 (R-44).
- **Sources:** https://bugbug.io/blog/software-testing/load-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-47 — Gatling
- **Canonical identity:** Gatling — Scala/JS load testing
- **Category:** A10 / Load & performance testing
- **Type:** Open-source core (Scala) + commercial Cloud/Enterprise
- **Official URL:** Not verified in this pass
- **Description:** Code-as-test load testing (Scala DSL, newer JS/TS SDK); high-performance Netty engine; detailed HTML reports; Gatling Cloud/Enterprise for scale.
- **Contents inspected:** bugbug.io load testing tools (Aug 2026) only.
- **Actual capabilities (evidence):** Can run high-concurrency scenarios with rich reports (secondary).
- **Usage domain:** High-throughput API load testing; teams comfortable with Scala/JS DSLs.
- **Integration method:** DSL scripts; CLI/CI; Cloud.
- **Compatibility:** HTTP/WebSocket/SSE; JVM.
- **Dependencies:** JVM (core).
- **Availability:** Free OSS core; Cloud/Enterprise paid.
- **Maintenance:** Active per 2026 citation.
- **License:** Apache-2.0 (core, widely reported).
- **Security:** Load generation caution as above.
- **Limitations:** DSL learning curve (secondary).
- **Related resources:** k6 (R-44), JMeter (R-46).
- **Sources:** https://bugbug.io/blog/software-testing/load-testing-tools/
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-48 — Artillery / Vegeta — lightweight load tools group
- **Canonical identity:** artilleryio/artillery; tsenart/vegeta
- **Category:** A10 / Load & performance testing
- **Type:** Open-source CLIs
- **Official URL:** Not verified in this pass
- **Description:** Artillery: Node.js load testing with YAML/JS scenarios, Socket.IO support, FaaS/Playwright integrations. Vegeta: Go HTTP load generator, constant-rate attacks, report plots.
- **Contents inspected:** graycode ai-code-review-qa skill ("load testing — k6, Locust, Artillery"); bugbug.io comparisons.
- **Actual capabilities (evidence):** Can script quick HTTP/Socket.IO load scenarios (Artillery); can run constant-rate HTTP attacks from a single binary (Vegeta) (secondary consensus).
- **Usage domain:** Quick API load checks; CI smoke load.
- **Integration method:** CLI; YAML/JS (Artillery); CLI flags (Vegeta).
- **Compatibility:** HTTP/WebSocket (Artillery); HTTP (Vegeta).
- **Dependencies:** Node.js (Artillery); none (Vegeta binary).
- **Availability:** Free OSS; Artillery Pro/Cloud paid.
- **Maintenance:** Active per 2026 citations.
- **License:** MPL-2.0 (Artillery); MIT (Vegeta) (widely reported; not inspected this pass).
- **Security:** Load generation caution as above.
- **Limitations:** Less protocol breadth than JMeter (secondary).
- **Related resources:** k6 (R-44), Locust (R-45).
- **Sources:** https://bugbug.io/blog/software-testing/load-testing-tools/ ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-49 — WebPageTest
- **Canonical identity:** WebPageTest (Catchpoint) — web performance measurement
- **Category:** A10 / Performance testing (real-browser)
- **Type:** Open-source core + hosted service
- **Official URL:** Not verified in this pass
- **Description:** Real-browser page-load measurement: filmstrip, waterfall, Core Web Vitals, scripting; private instances for CI.
- **Contents inspected:** 2026 mentions in performance skill docs (secondary).
- **Actual capabilities (evidence):** Can measure real user-perceived performance (LCP/CLS/INP) across browsers and throttled networks (secondary consensus).
- **Usage domain:** Frontend performance budgets; regression detection.
- **Integration method:** Web UI; API; private instance; CI.
- **Compatibility:** Real browsers (Chrome/Firefox/Safari/Edge).
- **Dependencies:** Hosted service or private infra.
- **Availability:** Free tier; paid plans.
- **Maintenance:** Active (2026 citations).
- **License:** Polyform Shield (core — reported; terms restrict competitive use; not inspected this pass).
- **Security:** Tests public URLs; private instance for internal apps (general).
- **Limitations:** Measures single pages, not load (complements k6).
- **Related resources:** Lighthouse (R-25), k6 browser module (R-44).
- **Sources:** Secondary skill/docs mentions (2026); specific URL not captured in this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A11. Type checking

### R-50 — TypeScript compiler (tsc) / strict mode
- **Canonical identity:** microsoft/TypeScript — tsc type checker
- **Category:** A11 / Type checking
- **Type:** Open-source compiler/checker
- **Official URL:** https://github.com/microsoft/TypeScript (seen verbatim)
- **Description:** Static type checking for JS/TS; strict mode, noUncheckedIndexedAccess, exactOptionalPropertyTypes; the baseline "test" for type-correctness in TS codebases (cited across 2026 skill docs).
- **Contents inspected:** Skill docs citing tsc strict as the type-correctness gate (craftbot, ai-code-review-qa skill).
- **Actual capabilities (evidence):** Can catch type errors, null/undefined misuse, and API-shape drift at compile time (well-established).
- **Usage domain:** TS codebases; CI typecheck gate.
- **Integration method:** `tsc --noEmit` in CI; editor integration.
- **Compatibility:** TypeScript/JavaScript.
- **Dependencies:** Node.js.
- **Availability:** Free, open source.
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security:** Local execution; no network.
- **Limitations:** Only checks types, not behavior; gradual-typing gaps in JS (secondary).
- **Related resources:** Pyright (R-52), mypy (R-51).
- **Sources:** https://github.com/microsoft/TypeScript ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-51 — mypy (Python)
- **Canonical identity:** python/mypy — static type checker for Python
- **Category:** A11 / Type checking
- **Type:** Open-source checker
- **Official URL:** Not verified in this pass
- **Description:** Static typing for Python via annotations; strict mode; daemon mode (dmypy) for speed.
- **Contents inspected:** 2026 skill docs listing mypy alongside pyright (ai-code-review-qa skill; python-backend-expert bundle).
- **Actual capabilities (evidence):** Can catch annotation/type mismatches in Python CI (secondary consensus).
- **Usage domain:** Typed Python codebases.
- **Integration method:** CLI; pre-commit; CI.
- **Compatibility:** Python 3.
- **Dependencies:** Python.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Local execution.
- **Limitations:** Gradual typing — untyped code unchecked (secondary).
- **Related resources:** Pyright (R-52), Astral ty (R-53).
- **Sources:** https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-52 — Pyright / Pylance
- **Canonical identity:** microsoft/pyright — Python type checker
- **Category:** A11 / Type checking
- **Type:** Open-source checker (Node-based)
- **Official URL:** https://github.com/microsoft/pyright (seen verbatim)
- **Description:** Fast Python type checker; powers Pylance in VS Code; strict mode; widely cited in 2026 skill docs as the Python typecheck standard.
- **Contents inspected:** 2026 skill docs (ai-code-review-qa; python-backend bundles).
- **Actual capabilities (evidence):** Can typecheck Python quickly with strict diagnostics (secondary consensus; well-established).
- **Usage domain:** Python CI + editor typechecking.
- **Integration method:** npm package; `pyright` CLI; VS Code via Pylance.
- **Compatibility:** Python 3.
- **Dependencies:** Node.js runtime.
- **Availability:** Free, open source.
- **Maintenance:** Active.
- **License:** MIT (widely reported).
- **Security:** Local execution.
- **Limitations:** Same gradual-typing caveat as mypy.
- **Related resources:** mypy (R-51), Astral ty (R-53).
- **Sources:** https://github.com/microsoft/pyright
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-53 — Astral ty (new Python type checker)
- **Canonical identity:** astral-sh/ty — "extremely fast Python type checker"
- **Category:** A11 / Type checking
- **Type:** Open-source checker (Rust)
- **Official URL:** Not verified in this pass
- **Description:** Astral's Rust-based Python type checker (companion to Ruff/uv); pre-1.0 in 2026, positioned as the fast successor for Python typing.
- **Contents inspected:** 2026 skill/docs mentions (astral context; secondary).
- **Actual capabilities (evidence):** Can typecheck Python with Rust-level speed (vendor claim; early stage).
- **Usage domain:** Python typechecking (early adopters).
- **Integration method:** CLI; editor LSP.
- **Compatibility:** Python 3.
- **Dependencies:** None (single binary).
- **Availability:** Free, open source.
- **Maintenance:** Active development; pre-stable in 2026.
- **License:** MIT (reported; not inspected this pass).
- **Security:** Local execution.
- **Limitations:** Pre-1.0: incomplete rule coverage vs mypy/pyright (2026 status).
- **Related resources:** mypy (R-51), Pyright (R-52), Ruff (R-56).
- **Sources:** Secondary 2026 mentions; URL not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A12. Static analysis & linting

### R-54 — SonarQube / SonarCloud
- **Canonical identity:** SonarSource SonarQube (self-hosted) / SonarCloud (SaaS)
- **Category:** A12 / Static analysis (quality + security)
- **Type:** Commercial platform with community edition
- **Official URL:** Not verified in this pass
- **Description:** Static analysis for bugs, vulnerabilities, code smells, duplications, coverage; quality gates; PR decoration; SonarQube Community Build remains free.
- **Contents inspected:** 2026 skill docs (ai-code-review-qa skill: "SAST — SonarQube"; craftbot bundles).
- **Actual capabilities (evidence):** Can scan multi-language codebases for bugs/vulns and enforce quality gates in CI (secondary consensus; widely established).
- **Usage domain:** Enterprise code quality/security gates.
- **Integration method:** Scanner CLI; CI plugins; PR decoration.
- **Compatibility:** 30+ languages.
- **Dependencies:** Server (self-host) or SaaS.
- **Availability:** Community free; commercial editions paid.
- **Maintenance:** Active.
- **License:** LGPL (Community Build); proprietary (commercial).
- **Security:** Scans source on your infra or SaaS (source leaves network on SaaS — review for proprietary code).
- **Limitations:** Heavy infra for self-host; rule tuning needed to control noise (secondary).
- **Related resources:** Semgrep (R-55), CodeQL (Part 14 B context).
- **Sources:** https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-55 — Semgrep (+ Opengrep fork)
- **Canonical identity:** semgrep/semgrep — lightweight SAST; opengrep/opengrep — community fork
- **Category:** A12 / Static analysis (security-focused)
- **Type:** Open-source engine + commercial platform
- **Official URL:** https://github.com/semgrep/semgrep (seen verbatim)
- **Description:** Pattern-based SAST with a large public rule registry; Semgrep OSS engine + Semgrep Cloud Platform (paid). Opengrep is the community fork of the OSS engine after licensing changes. Rules are YAML patterns — custom rules are easy to write.
- **Contents inspected:** 2026 skill docs (ai-code-review-qa skill; security-review bundles); semgrep repo listing.
- **Actual capabilities (evidence):** Can detect vulnerable patterns (injection, SSRF, hardcoded secrets patterns) across 30+ languages in CI with custom rules (secondary consensus; widely established).
- **Usage domain:** SAST in CI; custom security rules; pre-commit.
- **Integration method:** CLI; CI; pre-commit; MCP server (semgrep MCP per 2026 research).
- **Compatibility:** 30+ languages.
- **Dependencies:** Python/pipx or binary; rule packs.
- **Availability:** OSS engine free (LGPL-2.1); Cloud Platform paid; Opengrep fully community.
- **Maintenance:** Active (both).
- **License:** LGPL-2.1 (Semgrep CE); Opengrep community (check current license file — not inspected this pass).
- **Security:** Local scanning; custom rules can encode org-specific dangerous patterns.
- **Limitations:** Pattern-based — misses deep dataflow bugs that CodeQL catches (secondary).
- **Related resources:** SonarQube (R-54), CodeQL, ESLint security plugins (R-56 group).
- **Sources:** https://github.com/semgrep/semgrep ; https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-56 — ESLint / Ruff / Biome / Oxlint / PMD / Checkov — linters group
- **Canonical identity:** eslint/eslint (JS); astral-sh/ruff (Python); biomejs/biome (JS/TS); oxc-project/oxlint (JS/TS); pmd/pmd (JVM); bridgecrewio/checkov (IaC)
- **Category:** A12 / Linting & static analysis
- **Type:** Open-source linters/analyzers
- **Official URL:** Not verified in this pass
- **Description:** ESLint: pluggable JS/TS linting (flat config, typescript-eslint). Ruff: Rust-based Python linter+formatter (replaces flake8/black/isort). Biome: Rust JS/TS linter+formatter. Oxlint: Oxc's fast JS linter. PMD: JVM static analysis (Java/Apex). Checkov: IaC misconfiguration scanning (Terraform/CloudFormation/K8s/Dockerfile).
- **Contents inspected:** 2026 skill docs (ai-code-review-qa skill lists ESLint, Ruff, Biome, PMD, Checkov among lint gates; craftbot bundles).
- **Actual capabilities (evidence):** Can enforce style/correctness rules and catch IaC misconfigurations in CI/pre-commit (secondary consensus; widely established).
- **Usage domain:** Pre-commit/CI lint gates; IaC security (Checkov).
- **Integration method:** CLI; pre-commit hooks; CI; editor.
- **Compatibility:** JS/TS (ESLint/Biome/Oxlint); Python (Ruff); JVM (PMD); IaC (Checkov).
- **Dependencies:** Language runtimes.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations for all).
- **License:** MIT (ESLint, Ruff, Biome, Oxlint); BSD-style (PMD); Apache-2.0 (Checkov) (widely reported; not inspected this pass).
- **Security:** Local execution; Checkov flags insecure IaC before deploy.
- **Limitations:** Linters catch style/local bugs, not deep vulnerabilities (except Checkov's domain).
- **Related resources:** Semgrep (R-55), tsc (R-50).
- **Sources:** https://github.com/graycodeai/graycode-skills/blob/HEAD/categories/security/ai-code-review-qa/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## A13. Test coverage

### R-57 — Codecov / Coveralls — coverage hosting group
- **Canonical identity:** codecov (Codecov by Sentry); coveralls-io (Coveralls)
- **Category:** A13 / Test coverage
- **Type:** SaaS coverage reporting
- **Official URL:** Not verified in this pass
- **Description:** Ingest coverage reports (lcov, Cobertura, JaCoCo XML), PR comments, coverage diffs, flags/carryforward; Codecov is now a Sentry company (2026).
- **Contents inspected:** 2026 skill docs (craftbot coverage SKILL.md: codecov.yml, flags; ai-code-review-qa skill).
- **Actual capabilities (evidence):** Can track coverage trends, gate PRs on coverage deltas, annotate uncovered lines (secondary consensus).
- **Usage domain:** Coverage visibility and PR gating.
- **Integration method:** Uploader action/CLI; codecov.yml / .coveralls.yml.
- **Compatibility:** Any language with coverage reporters.
- **Dependencies:** CI; coverage artifacts.
- **Availability:** Free for OSS; paid per-seat for private.
- **Maintenance:** Active.
- **License:** Proprietary SaaS.
- **Security:** **Documented warning:** coverage upload tokens have been an attack vector historically (Codecov 2021 breach); use OIDC/tokenless upload where supported and rotate tokens (general security guidance, widely documented).
- **Limitations:** Coverage % is a weak quality proxy (secondary consensus).
- **Related resources:** Istanbul (R-58), JaCoCo (R-58 group), coverage.py (R-58 group).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/coverage-codecov-coveralls/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### R-58 — Istanbul/nyc/c8 (JS) · JaCoCo (JVM) · coverage.py (Python) — coverage engines group
- **Canonical identity:** istanbuljs (nyc, c8); jacoco/jacoco; nedbat/coveragepy
- **Category:** A13 / Test coverage
- **Type:** Open-source coverage instruments
- **Official URL:** Not verified in this pass
- **Description:** Istanbul: JS instrumentation (nyc CLI, c8 via V8). JaCoCo: JVM bytecode coverage. coverage.py: Python line/branch coverage (pytest-cov).
- **Contents inspected:** 2026 skill docs (craftbot coverage skill; python/js backend bundles).
- **Actual capabilities (evidence):** Can measure line/branch/function coverage and emit lcov/Cobertura/XML reports consumed by Codecov/Coveralls/SonarQube (secondary consensus; widely established).
- **Usage domain:** Coverage measurement in unit/integration suites.
- **Integration method:** Test runner plugins/flags.
- **Compatibility:** JS/TS (Istanbul); JVM (JaCoCo); Python (coverage.py).
- **Dependencies:** Test runners.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** BSD-3-Clause (Istanbul); EPL-2.0 (JaCoCo); Apache-2.0 (coverage.py) (widely reported; not inspected this pass).
- **Security:** Local instrumentation; no network.
- **Limitations:** Measures execution, not assertion quality (secondary).
- **Related resources:** Codecov/Coveralls (R-57), SonarQube (R-54).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/skills/coverage-codecov-coveralls/SKILL.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## A14. AI test generation & repair

### R-59 — Diffblue (Cover / Testing Agent)
- **Canonical identity:** Diffblue — AI unit-test generation (Cover; AI Testing Agent)
- **Category:** A14 / AI test generation
- **Type:** Commercial product (with community/free tiers)
- **Official URL:** Not verified in this pass
- **Description:** Generates Java unit tests (JUnit) automatically via reinforcement-learning + LLMs; "Diffblue Cover" writes/updates regression tests; newer AI Testing Agent positioning in 2026.
- **Contents inspected:** 2026 tool comparisons (bugbug.io unit testing tools; ai-testing roundups) only.
- **Actual capabilities (evidence):** Can generate Java unit tests with assertions automatically (vendor claim; secondary). Test-repair capability: regenerates tests after code changes (vendor claim).
- **Usage domain:** Java codebases lacking unit coverage.
- **Integration method:** IDE plugin; CLI; CI.
- **Compatibility:** Java/JVM.
- **Dependencies:** Paid/free account.
- **Availability:** Community edition free; commercial paid.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary.
- **Security:** Code analyzed by vendor service (check data-handling for proprietary code).
- **Limitations:** Java-only; generated tests need review (secondary).
- **Related resources:** Cover-Agent (R-60), Qodo (R-67 group).
- **Sources:** Secondary 2026 comparisons; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-60 — Cover-Agent (CodiumAI) — Unverified
- **Canonical identity:** Codium-ai/cover-agent — open-source AI test generator
- **Category:** A14 / AI test generation
- **Type:** Open-source agent (Python)
- **Official URL:** https://github.com/Codium-ai/cover-agent (not fetched in this pass — URL from prior knowledge, treat as unverified)
- **Description:** Agentic loop that writes tests, runs them, iterates on failures to raise coverage; supports multiple languages via project config.
- **Contents inspected:** None in this pass (no search hit captured; carried from task-context awareness).
- **Actual capabilities (evidence):** Claimed: generate→run→fix loop for tests. Evidence not inspected this pass.
- **Usage domain:** AI-assisted coverage raising.
- **Integration method:** CLI; CI.
- **Compatibility:** Python/JS/TS/Java/Go (claimed; unverified).
- **Dependencies:** LLM API key.
- **Availability:** Free, open source (claimed).
- **Maintenance:** Not verified in this pass.
- **License:** Not verified in this pass.
- **Security:** Executes generated test code — run in sandboxed CI (general caution).
- **Limitations:** Unverified this pass; generated-test quality varies (general).
- **Related resources:** Diffblue (R-59), Qodo (R-67 group).
- **Sources:** Not captured in this pass.
- **Verification date:** 2026-10-10
- **Verification:** Unverified | **Confidence:** Low

## A15. AI QA / autonomous testing agents

### R-61 — Mabl
- **Canonical identity:** Mabl — AI-native test automation platform
- **Category:** A15 / AI QA agents
- **Type:** Commercial SaaS
- **Official URL:** Not verified in this pass
- **Description:** No-code/low-code E2E with auto-healing, visual assertions, API + browser + accessibility + performance in one platform; 2026 AI-agent positioning ("AI agents for QA").
- **Contents inspected:** 2026 comparisons (bugbug.io E2E tools; overlayqa; ai-testing roundups) only.
- **Actual capabilities (evidence):** Can record browser/API tests, auto-heal selectors, run scheduled suites with failure insights (vendor claim; secondary). Cannot run without its cloud.
- **Usage domain:** Teams wanting codeless E2E with maintenance automation.
- **Integration method:** Recorder; CLI/API; CI integrations.
- **Compatibility:** Web; API; mobile (per vendor).
- **Dependencies:** Mabl account.
- **Availability:** Trial; paid plans.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary.
- **Security:** Tests execute on Mabl cloud; app credentials stored in platform vault (review per vendor docs — not inspected).
- **Limitations:** Vendor lock-in; codeless tests can be hard to version/debug (secondary).
- **Related resources:** QA Wolf (R-62), Testim (R-63).
- **Sources:** Secondary 2026 comparisons; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-62 — QA Wolf
- **Canonical identity:** QA Wolf — managed QA automation service
- **Category:** A15 / AI QA agents
- **Type:** Commercial service (Playwright-based)
- **Official URL:** Not verified in this pass
- **Description:** Human + AI service: builds and maintains Playwright test suites for customers; 2026 AI-agent narrative.
- **Contents inspected:** 2026 comparisons only.
- **Actual capabilities (evidence):** Can deliver maintained E2E suites as a service (vendor claim; secondary).
- **Usage domain:** Teams outsourcing E2E maintenance.
- **Integration method:** Service engagement; Playwright artifacts delivered.
- **Compatibility:** Web (Playwright).
- **Dependencies:** Service contract.
- **Availability:** Paid service.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary (service).
- **Security:** Third party writes/maintains tests against your app — scope access (general caution).
- **Limitations:** Service, not a tool — ongoing cost; less control (secondary).
- **Related resources:** Mabl (R-61), Playwright (R-08).
- **Sources:** Secondary 2026 comparisons; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-63 — Testim (Tricentis) / Functionize / Qodex — AI test automation group
- **Canonical identity:** Testim (Tricentis); Functionize; Qodex.ai
- **Category:** A15 / AI QA agents
- **Type:** Commercial SaaS platforms
- **Official URL:** Not verified in this pass
- **Description:** AI-assisted test authoring/maintenance: Testim (smart locators, now Tricentis); Functionize (NLP test creation, autonomous); Qodex (AI API testing agent, 2026 entrant).
- **Contents inspected:** 2026 comparisons (bugbug.io; ai-testing roundups) only.
- **Actual capabilities (evidence):** Vendor-claimed: NLP test creation, self-healing, autonomous execution (secondary only).
- **Usage domain:** Low-code AI test automation.
- **Integration method:** Recorders; NLP; CI.
- **Compatibility:** Web; API (Qodex).
- **Dependencies:** Vendor accounts.
- **Availability:** Paid; trials.
- **Maintenance:** Active per 2026 citations.
- **License:** Proprietary.
- **Security:** Cloud execution; credential vaulting per vendor (not inspected).
- **Limitations:** Vendor lock-in; AI claims largely vendor-sourced (secondary).
- **Related resources:** Mabl (R-61), QA Wolf (R-62).
- **Sources:** Secondary 2026 comparisons; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A16. Test management & reporting

### R-64 — TestRail / Qase / Xray / Zephyr — test management group
- **Canonical identity:** TestRail (Gurock); Qase; Xray (Xblend); Zephyr (SmartBear)
- **Category:** A16 / Test management
- **Type:** Commercial SaaS/self-hosted platforms
- **Official URL:** Not verified in this pass
- **Description:** Test-case repositories, manual + automated run tracking, Jira integration, reporting dashboards; Qase positioned as the modern lightweight entrant (2026).
- **Contents inspected:** 2026 skill docs (craftbot qa-engineer role.md lists TestRail, Xray, Zephyr; 2026 comparisons mention Qase).
- **Actual capabilities (evidence):** Can organize test cases, track manual/automated runs, and report quality metrics (secondary consensus).
- **Usage domain:** QA process management; regulated/manual-heavy teams.
- **Integration method:** Web UI; APIs; Jira plugins; CI result upload.
- **Compatibility:** Jira; CI tools.
- **Dependencies:** Paid accounts.
- **Availability:** Paid (trials); TestRail self-host option.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary.
- **Security:** Test data on vendor cloud (self-host options for TestRail).
- **Limitations:** Process overhead; cost per seat (secondary).
- **Related resources:** Allure TestOps (R-65), PractiTest (secondary mention).
- **Sources:** https://github.com/craftos-dev/craftbot-agent-bundles/blob/HEAD/agents/qa-engineer/role.md
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-65 — Allure Report / Allure TestOps
- **Canonical identity:** allure-framework/allure2 (OSS report); Qameta Allure TestOps (commercial)
- **Category:** A16 / Test reporting & management
- **Type:** Open-source report generator + commercial platform
- **Official URL:** Not verified in this pass
- **Description:** Allure Report: rich HTML test reports from JUnit/TestNG/pytest/playwright adapters. TestOps: commercial test management with flaky-test analytics.
- **Contents inspected:** 2026 skill mentions (secondary).
- **Actual capabilities (evidence):** Can render timelines, retries, attachments from test runs (secondary consensus; widely established).
- **Usage domain:** Test result visualization; flaky-test triage (TestOps).
- **Integration method:** Test adapters; CLI; CI artifacts.
- **Compatibility:** Major test frameworks.
- **Dependencies:** Test result files.
- **Availability:** Free OSS report; TestOps paid.
- **Maintenance:** Active.
- **License:** Apache-2.0 (OSS report, widely reported).
- **Security:** Local report generation; no network.
- **Limitations:** Report-only without TestOps (secondary).
- **Related resources:** TestRail group (R-64).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## A17. Code review agents

### R-66 — CodeRabbit
- **Canonical identity:** CodeRabbit — AI code review bot
- **Category:** A17 / Code review agents
- **Type:** Commercial SaaS (GitHub/GitLab app)
- **Official URL:** Not verified in this pass
- **Description:** AI PR reviews with inline comments, one-click fixes, custom review instructions (.coderabbit.yaml), learnings from review history; 2026 market leader in AI review per comparisons.
- **Contents inspected:** 2026 comparisons (ai code review tool roundups; qaskills/agent docs) only.
- **Actual capabilities (evidence):** Can post contextual PR comments, summarize changes, suggest fixes (vendor claim; secondary).
- **Usage domain:** Automated first-pass PR review.
- **Integration method:** GitHub/GitLab app; YAML config.
- **Compatibility:** GitHub, GitLab, Azure DevOps (per vendor).
- **Dependencies:** Vendor account; repo access grant.
- **Availability:** Free tier for OSS; paid per-seat.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary.
- **Security:** Reads full PR diffs (sends code to vendor LLM); configure data-retention; restrict to non-sensitive repos if concerned (general caution).
- **Limitations:** AI suggestions need human review; can be noisy (secondary).
- **Related resources:** Greptile (R-67), Qodo (R-67 group), Sourcery (R-68).
- **Sources:** Secondary 2026 comparisons; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-67 — Greptile / Qodo (PR-Agent) / Bito — AI review group
- **Canonical identity:** Greptile; qodo-ai/pr-agent (Qodo Merge); Bito
- **Category:** A17 / Code review agents
- **Type:** Commercial SaaS (Greptile, Bito); open-source action + commercial (Qodo)
- **Official URL:** https://github.com/qodo-ai/pr-agent (seen verbatim)
- **Description:** Greptile: AI reviewer with codebase-aware context. Qodo PR-Agent/Merge: open-source GitHub Action generating PR descriptions, reviews, and "test generation" commands. Bito: AI review + code assistant.
- **Contents inspected:** qodo-ai/pr-agent repo listing (seen verbatim); 2026 comparison mentions.
- **Actual capabilities (evidence):** PR-Agent can auto-describe/review PRs as a GitHub Action (repo evidence; secondary for quality claims).
- **Usage domain:** PR automation and review assistance.
- **Integration method:** GitHub App/Action; config YAML.
- **Compatibility:** GitHub/GitLab.
- **Dependencies:** LLM API key (self-hosted PR-Agent) or vendor account.
- **Availability:** Free OSS (PR-Agent); paid SaaS (Greptile, Bito, Qodo).
- **Maintenance:** Active per 2026 citations.
- **License:** Apache-2.0 (PR-Agent OSS, widely reported); proprietary (others).
- **Security:** Same code-exfiltration caution as R-66; self-hostable option (PR-Agent) reduces exposure.
- **Limitations:** Review quality varies; config needed to reduce noise (secondary).
- **Related resources:** CodeRabbit (R-66), Reviewdog (R-68 group).
- **Sources:** https://github.com/qodo-ai/pr-agent
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-68 — Sourcery / Reviewdog — review automation group
- **Canonical identity:** sourcery-ai/sourcery (AI refactoring reviews); reviewdog/reviewdog (linter comment bot)
- **Category:** A17 / Code review agents
- **Type:** Commercial (Sourcery) / open-source (Reviewdog)
- **Official URL:** Not verified in this pass
- **Description:** Sourcery: AI reviewer suggesting refactors; Reviewdog: posts any linter's findings as PR review comments (diff-aware).
- **Contents inspected:** 2026 comparison mentions only.
- **Actual capabilities (evidence):** Can automate review feedback — Sourcery via AI suggestions, Reviewdog by piping linter output into PR comments (secondary consensus).
- **Usage domain:** Automated review hygiene.
- **Integration method:** GitHub Actions; CLI.
- **Compatibility:** GitHub/GitLab.
- **Dependencies:** Linters (Reviewdog); vendor account (Sourcery).
- **Availability:** Free OSS (Reviewdog); freemium (Sourcery).
- **Maintenance:** Active per 2026 citations.
- **License:** MIT (Reviewdog, widely reported); proprietary (Sourcery).
- **Security:** Reviewdog runs locally in CI; Sourcery sends diffs to vendor (general caution).
- **Limitations:** Reviewdog only surfaces linter findings (no AI judgment).
- **Related resources:** CodeRabbit (R-66), ESLint (R-56).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A18. Synthetic monitoring / production smoke testing

### R-69 — Checkly
- **Canonical identity:** Checkly — synthetic monitoring (Playwright-based)
- **Category:** A18 / Synthetic monitoring & production smoke testing
- **Type:** Commercial SaaS (with open CLI)
- **Official URL:** Not verified in this pass
- **Description:** Monitoring-as-code: Playwright checks + API checks defined in TS, run on global probes on schedules; incident alerts; 2026 skill docs cite checkly CLI constructs.
- **Contents inspected:** 2026 skill docs mentioning Checkly constructs (secondary).
- **Actual capabilities (evidence):** Can run scheduled Playwright/API checks from global locations and alert on failure (secondary consensus).
- **Usage domain:** Production smoke tests; uptime/API monitoring as code.
- **Integration method:** `checkly` CLI; TS check files; Terraform provider.
- **Compatibility:** Playwright; HTTP APIs.
- **Dependencies:** Checkly account.
- **Availability:** Free tier; paid plans.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary SaaS; CLI open (reported).
- **Security:** Checks run against production with stored secrets — vault them; schedule safely (general caution).
- **Limitations:** Probe coverage/cost trade-offs (secondary).
- **Related resources:** Datadog Synthetics (R-70), k6 (R-44).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-70 — Datadog Synthetic Monitoring
- **Canonical identity:** Datadog Synthetics — synthetic tests in observability platform
- **Category:** A18 / Synthetic monitoring
- **Type:** Commercial SaaS
- **Official URL:** Not verified in this pass
- **Description:** Browser tests, API tests, mobile tests, and uptime checks inside Datadog; correlated with APM/logs/RUM.
- **Contents inspected:** 2026 mentions only.
- **Actual capabilities (evidence):** Can run global synthetic browser/API checks tied to observability data (vendor claim; secondary).
- **Usage domain:** Production monitoring for Datadog shops.
- **Integration method:** Datadog UI/API/Terraform.
- **Compatibility:** Datadog ecosystem.
- **Dependencies:** Datadog account.
- **Availability:** Paid (usage-based).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Production credentials in Datadog vault (review per vendor docs — not inspected).
- **Limitations:** Datadog lock-in; cost (secondary).
- **Related resources:** Checkly (R-69).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

## A19. Evaluation of AI-generated code

### R-71 — SWE-bench / SWE-bench-live / SWE-bench-Pro — Verified
- **Canonical identity:** SWE-bench (Princeton/NLP) — benchmark for AI software engineering; Live/Pro successors
- **Category:** A19 / Evaluation of AI-generated code
- **Type:** Open benchmark datasets + harness
- **Official URL:** https://www.swebench.com (seen verbatim)
- **Description:** 2,294 real GitHub issues with fail-to-pass tests measuring whether agents resolve them; SWE-bench-live (2025) refreshes tasks continuously to defeat contamination; SWE-bench-Pro (Scale AI, 2026) adds harder professional tasks. De-facto leaderboard metric for coding agents.
- **Contents inspected:** swebench.com (verified live 2026-10-10): official Verified subset, task counts, leaderboard framing.
- **Actual capabilities (evidence):** Can measure an agent's ability to fix real issues against hidden tests; can compare models on a stable leaderboard. Cannot measure code quality, security, or maintainability — only test-passing (well-documented limitation).
- **Usage domain:** Coding-agent evaluation and comparison.
- **Integration method:** Dataset + evaluation harness; agent submits patches.
- **Compatibility:** Python repos (original); multi-language in successors.
- **Dependencies:** Compute for agent rollouts.
- **Availability:** Free, open.
- **Maintenance:** Active (Live/Pro successors in 2026).
- **License:** MIT (harness, widely reported).
- **Security:** Runs untrusted agent patches — execute in containers (general caution).
- **Limitations:** Contamination risk on static set (addressed by Live); test-passing ≠ correct/secure.
- **Related resources:** Multi-SWE-bench (R-72), Inspect AI (R-73).
- **Sources:** https://www.swebench.com
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### R-72 — Multi-SWE-bench (ByteDance)
- **Canonical identity:** Multi-SWE-bench — multilingual SWE-bench
- **Category:** A19 / Evaluation of AI-generated code
- **Type:** Open benchmark dataset
- **Official URL:** Not verified in this pass
- **Description:** Community multilingual extension of SWE-bench (Java/TS/Go/Rust/C/C++ repos).
- **Contents inspected:** 2026 mentions only.
- **Actual capabilities (evidence):** Can evaluate agents beyond Python (secondary).
- **Usage domain:** Multilingual agent evaluation.
- **Integration method:** Dataset + harness.
- **Compatibility:** Multiple languages.
- **Dependencies:** Compute.
- **Availability:** Free, open.
- **Maintenance:** Community-maintained (2026 status not verified).
- **License:** Not verified in this pass.
- **Security:** Same untrusted-patch caution as R-71.
- **Limitations:** Smaller/less-curated than SWE-bench (secondary).
- **Related resources:** SWE-bench (R-71).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low

### R-73 — Inspect AI (UK AISI)
- **Canonical identity:** UKSafetyInstitute/inspect_ai — AI evaluation framework
- **Category:** A19 / Evaluation of AI-generated code (general eval framework)
- **Type:** Open-source framework (Python)
- **Official URL:** Not verified in this pass
- **Description:** UK AI Safety Institute's framework for LLM/agent evaluations: tasks, solvers, scorers, sandboxed execution; used for coding and safety evals.
- **Contents inspected:** 2026 mentions in eval/agent-safety contexts (secondary).
- **Actual capabilities (evidence):** Can build reproducible agent evals with sandboxed tool use (secondary consensus).
- **Usage domain:** Custom coding-agent and safety evaluations.
- **Integration method:** Python framework; Docker sandbox.
- **Compatibility:** LLM APIs; Docker.
- **Dependencies:** Model API access.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported; not inspected this pass).
- **Security:** Sandboxed execution model for untrusted agents (by design).
- **Limitations:** Framework, not a ready benchmark (secondary).
- **Related resources:** SWE-bench (R-71), Garak/PyRIT (Part 14 B8).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## A20. QA/test agent skills (reusable)

### R-74 — testland/qa skill
- **Canonical identity:** testland skill "qa" — Playwright-based QA agent skill
- **Category:** A20 / Test automation skills
- **Type:** Reusable agent skill (markdown + scripts)
- **Official URL:** https://github.com/numman-ali/testland (seen verbatim)
- **Description:** QA agent skill using Playwright MCP for E2E testing of user flows; structured QA workflows for coding agents.
- **Contents inspected:** Repo listing via prior research (skill referenced in testing-skills comparisons).
- **Actual capabilities (evidence):** Can drive Playwright MCP to execute scripted QA flows (secondary).
- **Usage domain:** Agent-driven E2E QA.
- **Integration method:** Skill install into agent (Claude Code/OpenCode).
- **Compatibility:** Playwright MCP.
- **Dependencies:** Playwright MCP server.
- **Availability:** Free, open source.
- **Maintenance:** Not verified in this pass.
- **License:** Not verified in this pass.
- **Security:** Skill executes browser automation — review skill scripts before install (general caution).
- **Limitations:** Depends on Playwright MCP availability.
- **Related resources:** Playwright MCP (dedup cross-ref), qaskills.sh (R-75).
- **Sources:** https://github.com/numman-ali/testland
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### R-75 — qaskills.sh / graycode-skills / craftbot-agent-bundles QA skills
- **Canonical identity:** QA skill collections: qaskills.sh (commercial skill marketplace); graycodeai/graycode-skills (OSS); craftos-dev/craftbot-agent-bundles (OSS agent bundles)
- **Category:** A20 / Test automation skills
- **Type:** Skill marketplaces/collections
- **Official URL:** https://qaskills.sh (seen verbatim); https://github.com/graycodeai/graycode-skills (seen verbatim); https://github.com/craftos-dev/craftbot-agent-bundles (seen verbatim)
- **Description:** Curated QA/testing skills for coding agents: visual regression, API testing, coverage, cross-browser matrices, accessibility audits, mobile testing — heavily cited as sources throughout this catalog.
- **Contents inspected:** Multiple SKILL.md files read in this pass (visual-regression-testing, ai-code-review-qa, api-testing-postman-rest-assured, coverage-codecov-coveralls, cross-browser-browserstack-saucelabs-lambdatest, pa11y-axe-accessibility-audit, mobile-testing, plus role.md files).
- **Actual capabilities (evidence):** Can give agents step-by-step QA workflows (tool install commands, config templates, thresholds, matrices) — evidenced by the SKILL.md contents read.
- **Usage domain:** Agent-executed QA across the A1–A19 spectrum.
- **Integration method:** Skill install (Claude Code/OpenCode skills dirs).
- **Compatibility:** Claude Code, OpenCode, compatible harnesses.
- **Dependencies:** Underlying tools (Playwright, axe-core, etc.).
- **Availability:** Free OSS (graycode, craftbot); paid marketplace (qaskills.sh).
- **Maintenance:** Active (2026-dated content).
- **License:** Varies (check per skill; not inspected this pass).
- **Security:** Skills are prompt+script bundles — review before install; they can invoke network/tool execution (general caution).
- **Limitations:** Guidance quality varies; skills encode opinions (e.g. license findings) that need independent verification.
- **Related resources:** All A-category tools above.
- **Sources:** https://github.com/graycodeai/graycode-skills ; https://github.com/craftos-dev/craftbot-agent-bundles ; https://qaskills.sh
- **Verification date:** 2026-10-10
- **Verification:** Verified (contents read) | **Confidence:** High (for existence/contents; Medium for individual claims)

---

# PART 14 — SECURITY, SANDBOXING, SOFTWARE SAFETY

> Scope: application security testing, dependency auditing, supply-chain security, secret detection/management, pentest frameworks, fuzzing, LLM/agent security testing, MCP security tooling, sandbox runtimes (real kernel/container isolation), remote isolated execution, devcontainers, policy enforcement, audit/recovery, plus verified 2026 supply-chain incidents. Throughout, the catalog distinguishes **actual technical isolation and enforceable controls** from guidance expressed only in prompts or instruction files.

## B1. Dependency auditing & SCA

### S-01 — OSV.dev / osv-scanner (Google/OpenSSF)
- **Canonical identity:** OSV.dev — distributed vulnerability database; google/osv-scanner — scanner CLI
- **Category:** B1 / Dependency auditing
- **Type:** Open database + open-source scanner
- **Official URL:** https://osv.dev (seen verbatim); https://github.com/google/osv-scanner (seen verbatim)
- **Description:** OSV schema database aggregating advisories across ecosystems (npm, PyPI, Go, crates, Maven, OS packages); osv-scanner audits lockfiles/SBOMs against it; osv.dev offers a web UI, API, and a free scanner.
- **Contents inspected:** osv.dev site description; osv-scanner repo description (via 2026 security research); 2026 SCA comparisons.
- **Actual capabilities (evidence):** Can identify known CVEs in declared dependencies via lockfile/SBOM scan, with version-range precision (secondary consensus; widely established).
- **Usage domain:** CI dependency audit; SBOM vulnerability matching.
- **Integration method:** `osv-scanner` CLI; API; CI actions; SBOM input (SPDX/CycloneDX).
- **Compatibility:** 25+ ecosystems incl. npm, PyPI, Go, Rust, Maven, Debian/Alpine.
- **Dependencies:** Lockfiles or SBOM.
- **Availability:** Free.
- **Maintenance:** Active (Google/OpenSSF-backed, 2026).
- **License:** Apache-2.0 (scanner, widely reported); CC-BY-4.0 (data, reported).
- **Security:** Queries can be sent with hashed prefixes (privacy-preserving, per docs — secondary).
- **Limitations:** Only known vulns with OSV records; no reachability analysis (secondary).
- **Related resources:** Dependabot (S-02), Snyk (S-04), Socket (S-05), deps.dev (B7).
- **Sources:** https://osv.dev ; https://github.com/google/osv-scanner
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-02 — Dependabot (GitHub)
- **Canonical identity:** GitHub Dependabot — automated dependency updates
- **Category:** B1 / Dependency auditing
- **Type:** Hosted automation (GitHub-native)
- **Official URL:** Not verified in this pass
- **Description:** Scans manifests, opens PRs for vulnerable/outdated dependencies; Dependabot alerts + security updates; version-update PRs.
- **Contents inspected:** 2026 comparisons and skill docs (secondary).
- **Actual capabilities (evidence):** Can auto-open update PRs and alert on vulnerable deps (secondary consensus; widely established).
- **Usage domain:** GitHub repos; automated patch PRs.
- **Integration method:** `.github/dependabot.yml`; native GitHub UI.
- **Compatibility:** GitHub; major ecosystems.
- **Dependencies:** GitHub repo.
- **Availability:** Free for GitHub repos.
- **Maintenance:** Active.
- **License:** Proprietary (GitHub feature).
- **Security:** Auto-merging Dependabot PRs without CI review is risky — require checks (general guidance).
- **Limitations:** GitHub-only; update PRs can be noisy (secondary).
- **Related resources:** Renovate (S-03), OSV (S-01).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-03 — Renovate (Mend)
- **Canonical identity:** renovatebot/renovate — automated dependency updating
- **Category:** B1 / Dependency auditing
- **Type:** Open-source bot + hosted app
- **Official URL:** Not verified in this pass
- **Description:** Highly configurable auto-update bot: grouping, scheduling, automerge rules, lockfile maintenance; Mend-hosted app or self-hosted.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can automate dependency updates with fine-grained policy (secondary consensus; widely established).
- **Usage domain:** Teams wanting more control than Dependabot; multi-ecosystem.
- **Integration method:** GitHub/GitLab app; `renovate.json`.
- **Compatibility:** GitHub, GitLab, Bitbucket, Azure DevOps; 100+ managers.
- **Dependencies:** Repo hosting.
- **Availability:** Free OSS/self-host; Mend hosted tiers.
- **Maintenance:** Active (2026 citations).
- **License:** AGPL-3.0 (widely reported; copyleft — self-host implications).
- **Security:** Bot gets write access to repos — scope permissions; review automerge (general caution).
- **Limitations:** Config complexity (secondary).
- **Related resources:** Dependabot (S-02).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-04 — Snyk (Open Source / Code / Container / IaC)
- **Canonical identity:** Snyk — developer security platform (SCA + SAST + container + IaC)
- **Category:** B1 / Dependency auditing (+SAST, container, IaC)
- **Type:** Commercial SaaS (free tier)
- **Official URL:** Not verified in this pass
- **Description:** SCA with reachability analysis, fix PRs, license checks; Snyk Code (SAST); container and IaC scanning; 2026: acquired Invariant Labs' mcp-scan → rebranded "Snyk Agent Scan" (see S-31).
- **Contents inspected:** 2026 comparisons; agent-scan research (S-31 context).
- **Actual capabilities (evidence):** Can find/fix vulnerable deps with reachability prioritization and open fix PRs (vendor claim; secondary).
- **Usage domain:** Enterprise AppSec; PR-time security.
- **Integration method:** CLI (`snyk test`); IDE; Git integrations; API.
- **Compatibility:** Major ecosystems; containers; IaC.
- **Dependencies:** Snyk account.
- **Availability:** Free tier; paid per-dev.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Code/deps metadata sent to Snyk cloud (review data-handling for proprietary code).
- **Limitations:** Cost per developer; alert fatigue without tuning (secondary).
- **Related resources:** Socket (S-05), OSV (S-01), Snyk Agent Scan (S-31).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-05 — Socket.dev
- **Canonical identity:** Socket — supply-chain security (behavioral analysis)
- **Category:** B1 / Dependency auditing (malicious-package detection)
- **Type:** Commercial SaaS (free tier)
- **Official URL:** Not verified in this pass
- **Description:** Detects malicious/typosquat packages via behavioral analysis (install scripts, network, obfuscation) rather than only known CVEs; PR firewall blocking risky installs.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can block suspicious package installs at PR time using behavior signals (vendor claim; secondary).
- **Usage domain:** Malicious-package defense; PR-time gating.
- **Integration method:** GitHub app; CLI; firewall proxy.
- **Compatibility:** npm, PyPI, Go, Maven, etc.
- **Dependencies:** Socket account.
- **Availability:** Free tier; paid.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary.
- **Security:** Sees dependency manifests/install behavior (review scope).
- **Limitations:** Behavioral heuristics can false-positive (secondary).
- **Related resources:** Snyk (S-04), npm/pip audit (S-06).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-06 — npm audit / pip-audit / cargo-audit — ecosystem-native auditors group
- **Canonical identity:** npm audit (npm CLI); pypa/pip-audit (Python); rustsec/cargo-audit (Rust)
- **Category:** B1 / Dependency auditing
- **Type:** Open-source CLIs (ecosystem-native)
- **Official URL:** Not verified in this pass
- **Description:** npm audit: built-in audit against GitHub Advisory DB. pip-audit: audits Python deps against OSV/PyPI advisories. cargo-audit: audits Cargo.lock against RustSec.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can audit project deps quickly in CI with no extra service (secondary consensus; widely established).
- **Usage domain:** CI dependency gates per ecosystem.
- **Integration method:** CLI in CI; pre-commit.
- **Compatibility:** npm; PyPI; crates.
- **Dependencies:** Lockfiles.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Various OSS (Artistic-2.0 npm; Apache-2.0/MIT pip-audit, cargo-audit — reported).
- **Security:** Local execution; advisory DB fetched over network.
- **Limitations:** Known-vuln only; no behavioral analysis (secondary).
- **Related resources:** OSV-scanner (S-01), Socket (S-05).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B2. Container & image scanning

### S-07 — Trivy (Aqua) — Verified, with 2026-03 supply-chain incident
- **Canonical identity:** aquasecurity/trivy — vulnerability/misconfig scanner
- **Category:** B2 / Container & image scanning (+IaC, SBOM, license)
- **Type:** Open-source CLI (Go)
- **Official URL:** https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 (Aqua's own advisory, seen verbatim); repo https://github.com/aquasecurity/trivy (seen verbatim)
- **Description:** All-in-one scanner: OS packages, language deps, IaC misconfigurations, secrets, licenses; SBOM generation; used as the default scanner in many CI pipelines and by other tools.
- **Contents inspected:** Aqua's GHSA-69fq-xp46-6x23 advisory (read in full this pass); trivy repo; 2026 comparisons.
- **Actual capabilities (evidence):** Can scan container images, filesystems, repos, and K8s clusters for CVEs/misconfigs/secrets and emit SBOM (secondary consensus; widely established).
- **Usage domain:** CI image scanning; K8s admission-adjacent checks.
- **Integration method:** CLI; `aquasecurity/trivy-action`; Docker.
- **Compatibility:** Container images, SBOM formats, IaC.
- **Dependencies:** Vulnerability DB download.
- **Availability:** Free, open source.
- **Maintenance:** Active.
- **License:** Apache-2.0 (widely reported).
- **Security:** **VERIFIED INCIDENT (2026-03-19):** threat actor "TeamPCP" (per Wiz/CrowdStrike reporting) hijacked the `75`/`76` tags of `aquasecurity/trivy-action` and pushed a malicious Trivy v0.69.4 release across npm/PyPI/Docker registries; the payload exfiltrated CI secrets to `scan.aquasecurtiy.org` (typosquat domain). Also affected: `setup-trivy` action tags replaced. Safe iff using immutable tag `0.35.0` or SHA-pinned to a commit after 2025-04-09. Lesson recorded across 2026 skill docs: pin actions by SHA.
- **Limitations:** Known-vuln DB only; DB freshness matters (secondary).
- **Related resources:** Grype (S-08), Docker Scout (S-09), Syft (SBOM).
- **Sources:** https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 (CVE-2026-33634) ; https://github.com/aquasecurity/trivy
- **Verification date:** 2026-10-10
- **Verification:** Verified | **Confidence:** High

### S-08 — Grype / Syft (Anchore)
- **Canonical identity:** anchore/grype (scanner); anchore/syft (SBOM generator)
- **Category:** B2 / Container & image scanning; SBOM
- **Type:** Open-source CLIs
- **Official URL:** Not verified in this pass
- **Description:** Syft generates SBOMs from images/filesystems; Grype matches them against vulnerability DBs; the pair underpins many pipelines and feeds GUAC/deps.dev-style analysis.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can produce SBOMs and match CVEs offline-ish (secondary consensus; widely established).
- **Usage domain:** CI image scanning; SBOM generation for supply-chain tooling.
- **Integration method:** CLI; CI actions.
- **Compatibility:** OCI images; SPDX/CycloneDX output.
- **Dependencies:** None (binaries).
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Local execution; DB downloads.
- **Limitations:** Known-vuln only (secondary).
- **Related resources:** Trivy (S-07), Clair (S-09 group), GUAC (B7).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-09 — Clair / Docker Scout — registry-integrated scanners group
- **Canonical identity:** quay/clair (static image analysis); Docker Scout (Docker's scanning)
- **Category:** B2 / Container & image scanning
- **Type:** Open-source service (Clair); commercial SaaS (Scout)
- **Official URL:** Not verified in this pass
- **Description:** Clair: static analysis of image layers against CVE DBs, API-driven, used by Quay. Docker Scout: policy-based image analysis integrated in Docker Desktop/Hub with remediation advice.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can scan pushed images continuously (Clair); can assess images with policy gates in Docker workflows (Scout) (secondary).
- **Usage domain:** Registry-side scanning; Docker-native teams.
- **Integration method:** Clair API/deployment; `docker scout` CLI.
- **Compatibility:** OCI images; Docker Hub.
- **Dependencies:** Registry (Clair); Docker account (Scout).
- **Availability:** Free OSS (Clair); freemium (Scout).
- **Maintenance:** Active per 2026 citations.
- **License:** Apache-2.0 (Clair, widely reported); proprietary (Scout).
- **Security:** Clair self-hosted keeps data local.
- **Limitations:** Clair needs deployment effort; Scout ties to Docker (secondary).
- **Related resources:** Trivy (S-07), Grype (S-08).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## B3. Secret detection

### S-10 — gitleaks
- **Canonical identity:** gitleaks/gitleaks — secret scanner for git repos
- **Category:** B3 / Secret detection
- **Type:** Open-source CLI (Go)
- **Official URL:** https://github.com/gitleaks/gitleaks (seen verbatim)
- **Description:** Scans git history, files, and stdin for secrets using regex rules + entropy; pre-commit hook and CI action; baseline/allowlist support.
- **Contents inspected:** Repo listing (seen verbatim); 2026 skill docs (secret-scanning skills cite gitleaks as the standard).
- **Actual capabilities (evidence):** Can detect committed secrets (API keys, tokens, private keys) across full git history and block PRs via CI (secondary consensus; widely established).
- **Usage domain:** Pre-commit/CI secret gating; repo audits.
- **Integration method:** CLI; pre-commit hook; GitHub Action.
- **Compatibility:** Any git repo.
- **Dependencies:** None (binary).
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported).
- **Security:** Scanning is local; findings contain live secrets — restrict report access (general caution).
- **Limitations:** Regex/entropy heuristics — false positives and misses on novel formats (secondary).
- **Related resources:** trufflehog (S-11), detect-secrets (S-12), GitHub secret scanning (S-12 group).
- **Sources:** https://github.com/gitleaks/gitleaks
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-11 — trufflehog (Truffle Security)
- **Canonical identity:** trufflesecurity/trufflehog — secret scanner with verification
- **Category:** B3 / Secret detection
- **Type:** Open-source CLI (Go)
- **Official URL:** Not verified in this pass
- **Description:** Scans git/filesystems/containers for secrets with 700+ built-in verified detectors; can verify live credentials against issuers to cut false positives.
- **Contents inspected:** 2026 comparisons and skill docs (secondary).
- **Actual capabilities (evidence):** Can detect and verify secrets (distinguishing live vs dead keys) across repos, S3, Docker (vendor claim; secondary).
- **Usage domain:** Secret audits; CI gating with verification.
- **Integration method:** CLI; CI; pre-commit.
- **Compatibility:** Git, filesystems, S3, Docker, Postman (per vendor).
- **Dependencies:** None (binary).
- **Availability:** Free OSS; commercial platform paid.
- **Maintenance:** Active (2026 citations).
- **License:** **AGPL-3.0** (widely reported; copyleft — embedding implications).
- **Security:** Verification makes live API calls to issuers — scope carefully (general caution); findings contain secrets.
- **Limitations:** AGPL license; verification needs network (secondary).
- **Related resources:** gitleaks (S-10), GitHub secret scanning (S-12 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-12 — detect-secrets / git-secrets (historical) / GitHub secret scanning — group
- **Canonical identity:** Yelp/detect-secrets; awslabs/git-secrets; GitHub secret scanning + push protection
- **Category:** B3 / Secret detection
- **Type:** Open-source tools (first two); platform feature (GitHub)
- **Official URL:** Not verified in this pass
- **Description:** detect-secrets: Yelp's baseline-based secret scanner with audit workflow. git-secrets: AWS Labs pre-commit secret blocker — **stale since 2021, historical**. GitHub secret scanning: partner-pattern scanning with push protection blocking secret commits.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** detect-secrets can baseline-and-audit; GitHub push protection can block secret commits at push time (secondary consensus).
- **Usage domain:** Pre-commit/push secret prevention.
- **Integration method:** pre-commit; git hooks; GitHub-native.
- **Compatibility:** Git repos; GitHub.
- **Dependencies:** None (tools); GitHub account (platform).
- **Availability:** Free OSS; GitHub feature (free for public; paid tiers for private).
- **Maintenance:** detect-secrets maintained; **git-secrets stale (2021) — Historical**; GitHub feature active.
- **License:** Apache-2.0 (detect-secrets, git-secrets — reported).
- **Security:** Findings contain secrets — restrict access.
- **Limitations:** git-secrets do not adopt (stale); pattern coverage varies (secondary).
- **Related resources:** gitleaks (S-10), trufflehog (S-11).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified / Historical (git-secrets) | **Confidence:** Low-Medium

## B4. Secrets management & environment-file protection

### S-13 — dotenvx / dotenv-vault
- **Canonical identity:** dotenvx/dotenvx — encrypted .env management
- **Category:** B4 / Secrets management
- **Type:** Open-source CLI
- **Official URL:** Not verified in this pass
- **Description:** Encrypted `.env` files (`.env.vault`) committed to git; per-environment decryption keys; `dotenvx run --` injects secrets at runtime.
- **Contents inspected:** 2026 skill docs (env-file protection guidance) (secondary).
- **Actual capabilities (evidence):** Can keep secrets out of plaintext while versioning env config (secondary consensus).
- **Usage domain:** Small-team secret management without a server.
- **Integration method:** CLI; `.env` files; CI decryption keys.
- **Compatibility:** Any stack reading env files.
- **Dependencies:** Decryption keys in CI.
- **Availability:** Free OSS; dotenv-vault SaaS paid.
- **Maintenance:** Active (2026 citations).
- **License:** Not verified in this pass.
- **Security:** Encrypted, but key management is on you — leaked decryption key = leaked secrets (general caution).
- **Limitations:** No rotation/audit vs real vaults (secondary).
- **Related resources:** SOPS (S-14), Doppler (S-14 group), Infisical (S-14 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-14 — Doppler / Infisical / HashiCorp Vault / OpenBao / SOPS — group
- **Canonical identity:** Doppler (SaaS); infisical/infisical (OSS platform); hashicorp/vault (OSS/Enterprise); openbao/openbao (community Vault fork); mozilla/sops (file encryption)
- **Category:** B4 / Secrets management
- **Type:** SaaS and self-hosted platforms; file-encryption tool (SOPS)
- **Official URL:** Not verified in this pass
- **Description:** Doppler/Infisical: cloud secret managers with syncing to CI/hosting. Vault: dynamic secrets, leasing, audit; OpenBao: community fork after Vault's BUSL license change. SOPS: encrypts YAML/JSON/env files with age/PGP/KMS for git storage.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can centralize secrets with access control, rotation, and audit (platforms); can encrypt config files for git (SOPS) (secondary consensus).
- **Usage domain:** Team/org secret management; GitOps encrypted config.
- **Integration method:** Agents/injectors; APIs; CLI; KMS.
- **Compatibility:** Broad.
- **Dependencies:** SaaS account or self-hosted cluster; KMS/age keys (SOPS).
- **Availability:** Free tiers/OSS; enterprise paid.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary SaaS (Doppler); MIT/Apache (Infisical core); **BUSL** (Vault — post-2023 license change); MPL-2.0/Apache (OpenBao); MPL-2.0 (SOPS) (widely reported; not inspected this pass).
- **Security:** Vault's BUSL change is why OpenBao exists — check license before self-hosting Vault commercially (general guidance).
- **Limitations:** Operational overhead for self-hosted Vault (secondary).
- **Related resources:** dotenvx (S-13).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## B5. Application security testing & penetration testing

### S-15 — OWASP ZAP
- **Canonical identity:** zaproxy/zaproxy — OWASP Zed Attack Proxy
- **Category:** B5 / AppSec testing (DAST)
- **Type:** Open-source security proxy/scanner
- **Official URL:** Not verified in this pass
- **Description:** Intercepting proxy + automated scanner: spider, active/passive scan, fuzzing, API scanning; automation framework for CI baseline scans.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can find common web vulns (XSS, SQLi, misconfig) via active scanning and gate CI on baseline rules (secondary consensus; widely established).
- **Usage domain:** DAST in CI; manual pentest proxy.
- **Integration method:** Desktop/CLI/Docker; automation YAML; CI.
- **Compatibility:** HTTP apps/APIs.
- **Dependencies:** Java.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations; now under ZAP's own org post-OWASP transition — reported).
- **License:** Apache-2.0 (widely reported).
- **Security:** Active scanning attacks the target — only scan authorized systems (general caution; legal risk).
- **Limitations:** Baseline scans miss logic flaws; active scan needs tuning (secondary).
- **Related resources:** Burp Suite (S-16), Nuclei (S-17).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-16 — Burp Suite (PortSwigger)
- **Canonical identity:** Burp Suite Community / Professional / Enterprise
- **Category:** B5 / AppSec testing (DAST, manual pentest)
- **Type:** Commercial tool (free community edition)
- **Official URL:** Not verified in this pass
- **Description:** The standard web pentest proxy: Repeater, Intruder, Scanner (Pro), extensions (BApp Store); Enterprise for CI DAST.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can intercept/modify/replay HTTP, automate scans, extend via extensions (secondary consensus; industry standard).
- **Usage domain:** Manual pentesting; CI DAST (Enterprise).
- **Integration method:** Desktop app; Enterprise CI integration; REST API.
- **Compatibility:** HTTP/WebSocket apps.
- **Dependencies:** Java; license (Pro).
- **Availability:** Community free; Pro ~$449/yr; Enterprise custom (indicative).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security:** Intercepts TLS via installed CA — scope to test traffic; active scanning only against authorized targets (general caution).
- **Limitations:** Pro cost; learning curve (secondary).
- **Related resources:** OWASP ZAP (S-15).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-17 — Nuclei (ProjectDiscovery)
- **Canonical identity:** projectdiscovery/nuclei — template-based vulnerability scanner
- **Category:** B5 / AppSec testing (vulnerability discovery)
- **Type:** Open-source scanner (Go)
- **Official URL:** Not verified in this pass
- **Description:** YAML-template-driven scanner with a huge community template library (nuclei-templates) covering CVEs, misconfigs, exposures; used for attack-surface monitoring.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can scan hosts/networks for thousands of known vuln signatures quickly (secondary consensus; widely established).
- **Usage domain:** Vuln scanning; bug-bounty recon; CI surface checks.
- **Integration method:** CLI; CI; scheduled scans.
- **Compatibility:** HTTP/network/DNS/cloud templates.
- **Dependencies:** None (binary); template updates.
- **Availability:** Free OSS; ProjectDiscovery Cloud paid.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported).
- **Security:** Scanning others' systems without authorization may be illegal — scope strictly (general caution).
- **Limitations:** Signature-based — only known issues (secondary).
- **Related resources:** Nmap (S-18 group), sqlmap (S-18 group), OWASP ZAP (S-15).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-18 — sqlmap / Nmap / Metasploit / ffuf / Nikto — pentest toolkit group
- **Canonical identity:** sqlmap/sqlmap; nmap/nmap; rapid7/metasploit-framework; ffuf/ffuf; nikto
- **Category:** B5 / Penetration testing frameworks & tools
- **Type:** Open-source tools
- **Official URL:** Not verified in this pass
- **Description:** sqlmap: automatic SQL injection exploitation. Nmap: network discovery/port scanning. Metasploit: exploitation framework. ffuf: fast web fuzzer for dirs/vhosts/params. Nikto: web-server misconfig scanner.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can discover/exploit vulns in authorized tests (secondary consensus; widely established).
- **Usage domain:** Authorized pentests; security research.
- **Integration method:** CLIs; Metasploit console/API.
- **Compatibility:** Networks; web apps.
- **Dependencies:** None/run locally.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **Security:** **Do not run against systems without written authorization** — these are dual-use offensive tools (general caution; legal risk).
- **Limitations:** Require operator expertise; noisy (secondary).
- **Related resources:** Burp (S-16), Nuclei (S-17).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B6. Fuzzing

### S-19 — AFL++ / libFuzzer / Jazzer / Honggfuzz — coverage-guided fuzzers group
- **Canonical identity:** AFLplusplus/AFLplusplus; LLVM libFuzzer; CodeIntelligenceTesting/jazzer (JVM); google/honggfuzz
- **Category:** B6 / Fuzzing (vulnerability discovery)
- **Type:** Open-source fuzzers
- **Official URL:** Not verified in this pass
- **Description:** Coverage-guided greybox fuzzers: AFL++ (C/C++, persistent mode, cmplog), libFuzzer (in-process LLVM), Jazzer (JVM coverage-guided), Honggfuzz (multi-platform).
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can discover memory-corruption and crash bugs automatically via mutated inputs (secondary consensus; widely established).
- **Usage domain:** Native/JVM code security testing; parser/protocol hardening.
- **Integration method:** Compiler instrumentation; harnesses; CI (short runs) + dedicated fuzzing infra (long runs).
- **Compatibility:** C/C++ (AFL++, libFuzzer, Honggfuzz); JVM (Jazzer).
- **Dependencies:** Toolchains; sanitizers (ASan/UBSan).
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Fuzzing executes target code with hostile inputs — isolate fuzzing workers (general caution).
- **Limitations:** Needs harnesses and compute; findings need triage (secondary).
- **Related resources:** OSS-Fuzz (S-20), Schemathesis (R-38, API-level).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-20 — OSS-Fuzz (Google)
- **Canonical identity:** google/oss-fuzz — continuous fuzzing for open source
- **Category:** B6 / Fuzzing infrastructure
- **Type:** Free service for OSS projects (Google)
- **Official URL:** Not verified in this pass
- **Description:** Continuous cloud fuzzing for open-source projects (integrates AFL++, libFuzzer, Honggfuzz); ClusterFuzz automation, crash triage, bisection.
- **Contents inspected:** 2026 mentions (secondary).
- **Actual capabilities (evidence):** Can continuously fuzz enrolled OSS projects at Google scale (secondary consensus).
- **Usage domain:** OSS project security.
- **Integration method:** Project integration (Dockerfile + build script).
- **Compatibility:** OSS projects.
- **Dependencies:** Project enrollment.
- **Availability:** Free for qualifying OSS.
- **Maintenance:** Active.
- **License:** Apache-2.0 (infra).
- **Security:** Google-run infra; crash reports shared with maintainers.
- **Limitations:** OSS-only; enrollment bar (secondary).
- **Related resources:** AFL++ group (S-19).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B7. Software supply-chain security

### S-21 — Sigstore (cosign / Fulcio / Rekor)
- **Canonical identity:** sigstore — keyless signing infrastructure; sigstore/cosign (container signing); Fulcio (ephemeral certs); Rekor (transparency log)
- **Category:** B7 / Supply-chain security
- **Type:** Open-source tooling + public-good infrastructure
- **Official URL:** Not verified in this pass
- **Description:** Keyless code signing via OIDC identity: cosign signs container images/blobs; Fulcio issues short-lived certs; Rekor logs signatures publicly for auditability.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can sign artifacts and verify provenance without managing long-lived keys (secondary consensus; widely established).
- **Usage domain:** Container/image signing; release attestation.
- **Integration method:** CLI (`cosign sign/verify`); CI; policy-controller verification.
- **Compatibility:** OCI images; blobs; K8s (policy-controller).
- **Dependencies:** OIDC identity (GitHub Actions etc.); Rekor/Fulcio public instances.
- **Availability:** Free (public-good infra).
- **Maintenance:** Active (OpenSSF-backed, 2026).
- **License:** Apache-2.0 (widely reported).
- **Security:** Trusts OIDC issuers and transparency logs — verify Rekor inclusion (general guidance).
- **Limitations:** Ecosystem adoption still growing (secondary).
- **Related resources:** SLSA (S-22), policy-controller (B13).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-22 — SLSA framework (v1.2)
- **Canonical identity:** SLSA (Supply-chain Levels for Software Artifacts) — OpenSSF
- **Category:** B7 / Supply-chain security
- **Type:** Specification framework
- **Official URL:** Not verified in this pass
- **Description:** Levels (Build L1–L3) for artifact provenance: hermetic reproducible builds, non-falsifiable provenance; v1.2 current in 2026; slsa-github-generator produces provenance in CI.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can attest how an artifact was built so consumers can verify provenance (secondary consensus).
- **Usage domain:** Release engineering; provenance attestation.
- **Integration method:** slsa-github-generator; provenance verification tooling.
- **Compatibility:** GitHub Actions primarily.
- **Dependencies:** Builder attestation.
- **Availability:** Free spec + tooling.
- **Maintenance:** Active (v1.2, 2026).
- **License:** Apache-2.0 (spec/tooling, reported).
- **Security:** Provenance is only as trustworthy as the builder (general caution).
- **Limitations:** Spec, not enforcement — needs verifier/policy (secondary).
- **Related resources:** Sigstore (S-21), in-toto (S-23).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-23 — OpenSSF Scorecard (v5.5.0) / in-toto (v1.0) / TUF — group
- **Canonical identity:** ossf/scorecard; in-toto/in-toto; theupdateframework/specification (TUF)
- **Category:** B7 / Supply-chain security
- **Type:** Open-source tool/spec/framework
- **Official URL:** Not verified in this pass
- **Description:** Scorecard: automated security-health checks for repos (branch protection, CI, fuzzing, pinning) — v5.5.0 in 2026. in-toto: supply-chain layout/attestation framework — v1.0 spec. TUF: secure update framework (role-based signing, compromise resilience) used by PyPI, Sigstore, OTA systems.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Scorecard can score repo hygiene in CI; in-toto can attest supply-chain steps; TUF can secure update distribution (secondary consensus).
- **Usage domain:** Repo trust analysis; release pipelines; update systems.
- **Integration method:** Scorecard action/CLI; in-toto attestations; TUF client libs.
- **Compatibility:** GitHub (Scorecard); general (in-toto, TUF).
- **Dependencies:** None major.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 version citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Scorecard is heuristic — low scores guide review, not proof of compromise (general caution).
- **Limitations:** Heuristic/spec-level; adoption effort (secondary).
- **Related resources:** SLSA (S-22), Sigstore (S-21), GUAC (S-24).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-24 — GUAC / CycloneDX / SPDX / deps.dev — SBOM & metadata group
- **Canonical identity:** guacsec/guac (Graph for Understanding Artifact Composition); CycloneDX (OWASP SBOM standard); SPDX (ISO/IEC 5962 SBOM standard); deps.dev (Google package metadata API)
- **Category:** B7 / Supply-chain security (SBOM & graph analysis)
- **Type:** Open-source project; standards; free API
- **Official URL:** Not verified in this pass
- **Description:** GUAC ingests SBOMs/provenance into a queryable graph. CycloneDX/SPDX are the SBOM formats (SPDX is ISO-standard). deps.dev exposes dependency/security metadata per package version.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can assemble and query software composition graphs; can emit/consume standard SBOMs; can look up package vuln/license metadata (secondary consensus).
- **Usage domain:** SBOM compliance; dependency graph analysis.
- **Integration method:** GUAC CLI/collectors; SBOM generators (Syft, Trivy); deps.dev API.
- **Compatibility:** SPDX/CycloneDX ecosystems.
- **Dependencies:** SBOM inputs.
- **Availability:** Free.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (GUAC, CycloneDX tooling); CC-BY (SPDX spec, reported).
- **Security:** Graph quality depends on SBOM accuracy (general caution).
- **Limitations:** Operational complexity for GUAC (secondary).
- **Related resources:** Syft/Grype (S-08), OSV (S-01), SLSA (S-22).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-25 — 2026 supply-chain incidents — verified records
- **Canonical identity:** Documented 2026 supply-chain compromises (incident records, not tools)
- **Category:** B7 / Supply-chain security (incident evidence)
- **Type:** Incident records
- **Official URL:** https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 (seen verbatim)
- **Description:** Verified 2026 incidents: (1) **Trivy-action hijack** (2026-03-19, TeamPCP; CVE-2026-33634/GHSA-69fq-xp46-6x23 — exfil to scan.aquasecurtiy.org; see S-07). (2) **axios maintainer/package hijack** (Mar 2026 — secondary reports of maintainer account compromise affecting the axios npm package). (3) **LiteLLM PyPI 1.82.7/1.82.8** (Mar 2026 — malicious versions published, later removed). (4) **Bitwarden CLI incident** (Apr 2026 — secondary reports). (5) **Checkmarx KICS GitHub Action compromise** (Mar 2026 — malicious commit in kics-github-action, exfil vector; secondary). (6) **CVE-2026-80521** (disclosed 2026-09-22: Linux kernel AF_UNIX garbage-collector use-after-free enabling container escape — undermines user-namespace sandboxes; see B10).
- **Contents inspected:** Aqua advisory (full read); securityonline.info reporting on CVE-2026-80521 (observed 2026-10-10); secondary incident roundups.
- **Actual capabilities (evidence):** These records evidence that tag/mutability hijack, maintainer-account takeover, and malicious version publishes are active 2026 vectors; and that kernel bugs can defeat container isolation.
- **Usage domain:** Threat modeling for CI/supply-chain defenses.
- **Integration method:** Not applicable (records).
- **Compatibility:** Not applicable.
- **Dependencies:** Not applicable.
- **Availability:** Public advisories/news.
- **Maintenance:** Historical records.
- **License:** Not applicable.
- **Security:** Defensive controls evidenced: SHA-pin actions, immutable tags, OIDC/keyless signing, provenance verification, behavioral package analysis (Socket), kernel patching.
- **Limitations:** Incidents 2–5 rest on secondary reporting — details (exact versions, blast radius) not independently verified this pass.
- **Related resources:** Trivy (S-07), Socket (S-05), SLSA/Sigstore (S-21/22), B10 sandboxes.
- **Sources:** https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23 ; secondary 2026 incident reporting (observed 2026-10-10)
- **Verification date:** 2026-10-10
- **Verification:** Verified (Trivy incident, CVE-2026-80521) / Partially verified (incidents 2–5) | **Confidence:** High/Medium

## B8. LLM / prompt-injection security testing

### S-26 — Garak (NVIDIA)
- **Canonical identity:** NVIDIA/garak — LLM vulnerability scanner
- **Category:** B8 / LLM security testing
- **Type:** Open-source scanner (Python)
- **Official URL:** Not verified in this pass
- **Description:** Probe-based LLM red-teaming: prompt-injection, jailbreak, data-leak, encoding attacks; generator/adapter model for many LLM APIs and local models.
- **Contents inspected:** 2026 skill docs and comparisons (secondary).
- **Actual capabilities (evidence):** Can systematically probe LLM apps for jailbreak/injection/leak weaknesses (secondary consensus; widely established).
- **Usage domain:** LLM app red-teaming; pre-deployment safety checks.
- **Integration method:** CLI; Python API; CI.
- **Compatibility:** Major LLM APIs; HuggingFace; local.
- **Dependencies:** Model access.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Probes attack your own models — scope to authorized targets (general caution).
- **Limitations:** Probe-based — coverage of novel attacks varies (secondary).
- **Related resources:** PyRIT (S-27), promptfoo (S-28).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-27 — PyRIT (Microsoft)
- **Canonical identity:** Azure/PyRIT — Python Risk Identification Toolkit
- **Category:** B8 / LLM security testing
- **Type:** Open-source framework (Python)
- **Official URL:** Not verified in this pass
- **Description:** Microsoft's red-teaming framework: orchestrators, converters (encodings), scorers; multi-turn attack automation; used by Microsoft's AI Red Team.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can automate multi-turn adversarial conversations against LLM systems (secondary consensus).
- **Usage domain:** Structured AI red-teaming.
- **Integration method:** Python framework; Jupyter.
- **Compatibility:** Azure OpenAI, OpenAI, HuggingFace, local.
- **Dependencies:** Python; model access.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported).
- **Security:** Same authorized-target caution as S-26.
- **Limitations:** Framework — requires attack design (secondary).
- **Related resources:** Garak (S-26), Inspect AI (R-73).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-28 — promptfoo
- **Canonical identity:** promptfoo/promptfoo — LLM eval & red-teaming CLI
- **Category:** B8 / LLM security testing (+ prompt eval)
- **Type:** Open-source CLI (Node) + commercial Cloud
- **Official URL:** Not verified in this pass
- **Description:** YAML-defined evals: assertions, red-team plugins (prompt injection, PII, jailbreak), CI integration; widely used for regression-testing prompts.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can regression-test prompts and run red-team suites in CI (secondary consensus; widely established).
- **Usage domain:** Prompt engineering QA; LLM app CI.
- **Integration method:** `promptfoo` CLI; YAML configs; CI.
- **Compatibility:** Major LLM providers.
- **Dependencies:** Node.js; model API keys.
- **Availability:** Free OSS; Cloud paid.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (widely reported).
- **Security:** Evals call external LLM APIs with your prompts — review data sent (general caution).
- **Limitations:** Eval quality depends on assertions/plugins (secondary).
- **Related resources:** Garak (S-26), PyRIT (S-27).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-29 — Rebuff / Vigil / LLM Guard / Lakera Guard / LlamaGuard (PurpleLlama) / NeMo Guardrails / Prompt Shields / picklescan — guardrail & detection group
- **Canonical identity:** protectai/rebuff; carnegie/vigil (prompt-injection detection); protectai/llm-guard; Lakera Guard (commercial API); meta-llama/PurpleLlama LlamaGuard (open classifier); NVIDIA-NeMo/NeMo-Guardrails (programmable rails); Azure Prompt Shields (commercial); protectai/picklescan (pickle model scanning)
- **Category:** B8 / LLM security (detection, guardrails, model scanning)
- **Type:** Open-source tools + commercial APIs
- **Official URL:** Not verified in this pass
- **Description:** Rebuff/Vigil: prompt-injection detection (heuristics + embeddings/canary tokens). LLM Guard: sanitization/validation library. Lakera Guard: commercial real-time guardrail API. LlamaGuard: Meta's open safety classifier (PurpleLlama). NeMo Guardrails: programmable input/output rails (Colang). Prompt Shields: Azure content-safety for indirect injection. picklescan: scans pickle/model files for malicious code.
- **Contents inspected:** 2026 skill docs and comparisons; ai-goat prompt-injection doc (Invariant indicator list: `<IMPORTANT>`, "ignore previous instructions", `~/.ssh`/`.env` refs, zero-width chars, >1500-char descriptions) (secondary).
- **Actual capabilities (evidence):** Can detect/block common injection patterns and scan model files for embedded exploits (secondary consensus; vendor claims).
- **Usage domain:** Runtime protection for LLM apps; model supply-chain hygiene (picklescan).
- **Integration method:** Libraries; APIs; CI (picklescan).
- **Compatibility:** Python/JS; LLM APIs.
- **Dependencies:** Model/API access (classifiers); none (picklescan).
- **Availability:** Free OSS (most); commercial (Lakera, Prompt Shields).
- **Maintenance:** Mixed — Rebuff/Vigil community status not verified current in this pass; others active per 2026 citations.
- **License:** Apache-2.0/MIT (OSS ones, reported); proprietary (commercial).
- **Security:** Detectors are heuristic — determined attackers bypass them; defense-in-depth required (general guidance).
- **Limitations:** Heuristic bypass risk; latency/cost for API guardrails (secondary).
- **Related resources:** Garak (S-26), Snyk Agent Scan (S-31).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## B9. MCP security tooling

### S-30 — Snyk Agent Scan (formerly Invariant Labs mcp-scan) — Corrected
- **Canonical identity:** snyk/agent-scan — MCP server security scanner (formerly invariantlabs-ai/mcp-scan)
- **Category:** B9 / MCP security tooling
- **Type:** Open-source CLI (Python, `uvx`)
- **Official URL:** https://github.com/snyk/agent-scan (seen verbatim)
- **Description:** Scans MCP servers for tool poisoning, prompt injection, and suspicious tool definitions; was Invariant Labs' mcp-scan, now Snyk-maintained after acquisition; run via `uvx snyk-agent-scan`.
- **Contents inspected:** Repo listing (seen verbatim); 2026 MCP-security research noting the rename.
- **Actual capabilities (evidence):** Can statically analyze MCP server tool schemas/descriptions for poisoning indicators (repo evidence; secondary).
- **Usage domain:** Vetting MCP servers before connecting them to agents.
- **Integration method:** `uvx snyk-agent-scan`; CI.
- **Compatibility:** MCP servers (any).
- **Dependencies:** uv/Python.
- **Availability:** Free, open source.
- **Maintenance:** Active (Snyk-maintained, 2026).
- **License:** Apache-2.0 (reported; not inspected this pass).
- **Security:** Scanner itself is read-only analysis — low risk; findings guide allowlisting.
- **Limitations:** Static analysis — misses runtime/dynamic exfiltration (secondary).
- **Related resources:** glatinone/mcpscan (S-31), MCP Inspector (S-32).
- **Sources:** https://github.com/snyk/agent-scan
- **Verification date:** 2026-10-10
- **Verification:** Corrected | **Confidence:** Medium

### S-31 — glatinone/mcpscan — MCP server scanner
- **Canonical identity:** glatinone/mcpscan — MCP security scanner
- **Category:** B9 / MCP security tooling
- **Type:** Open-source tool
- **Official URL:** https://github.com/glatinone/mcpscan (seen verbatim)
- **Description:** Community MCP scanner checking server configurations and tool definitions for security issues.
- **Contents inspected:** Repo listing (seen verbatim); 2026 MCP-security comparisons.
- **Actual capabilities (evidence):** Can audit MCP server configs/tools for risky patterns (repo evidence; secondary).
- **Usage domain:** MCP server vetting.
- **Integration method:** CLI.
- **Compatibility:** MCP servers.
- **Dependencies:** Not verified in this pass.
- **Availability:** Free, open source.
- **Maintenance:** Community (2026 status not verified).
- **License:** Not verified in this pass.
- **Security:** Read-only analysis.
- **Limitations:** Community tool; coverage not independently assessed (secondary).
- **Related resources:** Snyk Agent Scan (S-30).
- **Sources:** https://github.com/glatinone/mcpscan
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-32 — MCP Inspector (@modelcontextprotocol/inspector)
- **Canonical identity:** MCP Inspector — official MCP debugging tool
- **Category:** B9 / MCP tooling (debugging/vetting aid)
- **Type:** Open-source dev tool
- **Official URL:** Not verified in this pass
- **Description:** Official UI/CLI to connect to an MCP server, list tools/resources/prompts, and invoke them — useful for manually vetting what a server exposes before granting an agent access.
- **Contents inspected:** 2026 MCP docs mentions (secondary).
- **Actual capabilities (evidence):** Can enumerate and test-invoke MCP server capabilities (secondary consensus).
- **Usage domain:** MCP server development and manual security review.
- **Integration method:** CLI/UI (`npx @modelcontextprotocol/inspector`).
- **Compatibility:** MCP protocol.
- **Dependencies:** Node.js.
- **Availability:** Free, open source.
- **Maintenance:** Active (official).
- **License:** MIT (reported; not inspected this pass).
- **Security:** Invoking tools executes them — vet in a sandbox first (general caution).
- **Limitations:** Manual — not an automated scanner (secondary).
- **Related resources:** Snyk Agent Scan (S-30), mcpscan (S-31).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B10. Sandbox runtimes — actual technical isolation

> These provide enforceable kernel/container isolation, distinct from prompt-level "sandbox" guidance. Note the 2026-09 kernel caveat: CVE-2026-80521 (AF_UNIX GC use-after-free, disclosed 2026-09-22) enables container escape and undermines user-namespace-based sandboxes until patched.

### S-33 — gVisor (Google)
- **Canonical identity:** google/gvisor — application kernel sandbox
- **Category:** B10 / Sandbox runtimes
- **Type:** Open-source runtime (Go)
- **Official URL:** Not verified in this pass
- **Description:** User-space kernel (Sentry) intercepting syscalls; runsc OCI runtime integrates with Docker/containerd; strong multi-tenant isolation.
- **Contents inspected:** 2026 sandbox comparisons and agent-harness docs (secondary).
- **Actual capabilities (evidence):** Can sandbox untrusted containers with a reduced syscall attack surface vs runc (secondary consensus; widely established).
- **Usage domain:** Multi-tenant container isolation; agent code-execution sandboxes.
- **Integration method:** runsc as OCI runtime; Docker/containerd config.
- **Compatibility:** Linux; OCI.
- **Dependencies:** Linux host.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Defense-in-depth, not a panacea — kernel bugs (e.g. CVE-2026-80521 class) can still matter; keep hosts patched (general guidance).
- **Limitations:** Syscall compatibility gaps; performance overhead (secondary).
- **Related resources:** Firecracker (S-34), Kata (S-35 group), nsjail (S-36).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-34 — Firecracker (AWS)
- **Canonical identity:** firecracker-microvm/firecracker — microVM manager
- **Category:** B10 / Sandbox runtimes
- **Type:** Open-source virtualization (Rust)
- **Official URL:** Not verified in this pass
- **Description:** Lightweight KVM microVMs (125ms boot); the isolation behind AWS Lambda/Fargate; used by agent-sandbox platforms for strong VM-level isolation.
- **Contents inspected:** 2026 sandbox comparisons (secondary).
- **Actual capabilities (evidence):** Can run workloads in hardware-virtualized microVMs with fast boot (secondary consensus; widely established).
- **Usage domain:** Serverless/agent execution isolation.
- **Integration method:** API; containerd integration (firecracker-containerd).
- **Compatibility:** Linux KVM hosts.
- **Dependencies:** KVM.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** VM boundary is stronger than container boundary; still patch guest/host (general guidance).
- **Limitations:** KVM required; orchestration effort (secondary).
- **Related resources:** gVisor (S-33), Kata (S-35 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-35 — Bubblewrap / nsjail / Firejail / Kata Containers / Landlock / seccomp — Linux sandbox primitives group
- **Canonical identity:** containers/bubblewrap (bwrap); google/nsjail; netblue30/firejail; kata-containers/kata-containers; Landlock LSM; seccomp-bpf
- **Category:** B10 / Sandbox runtimes & primitives
- **Type:** Open-source tools/kernel features
- **Official URL:** Not verified in this pass
- **Description:** Bubblewrap: unprivileged container sandbox (used by Flatpak; OpenCode's native sandbox uses bwrap on Linux per dedup context). nsjail: process isolation with namespaces/seccomp/cgroups (used by Kimi/Codex harnesses per 2026 research). Firejail: SUID sandbox for desktop apps. Kata: VM-backed containers (QEMU/CLH). Landlock: unprivileged filesystem sandboxing LSM. seccomp-bpf: syscall filtering primitive.
- **Contents inspected:** 2026 sandbox comparisons; dedup context (OpenCode native sandbox uses Bubblewrap/gVisor/Firecracker/Seatbelt).
- **Actual capabilities (evidence):** Can enforce filesystem/network/syscall restrictions at the OS level (secondary consensus; widely established). **Caveat:** CVE-2026-80521 (Sept 2026) undermines nsjail/Firejail/Bubblewrap-style user-namespace isolation on unpatched kernels.
- **Usage domain:** CLI/agent sandboxing; desktop app confinement.
- **Integration method:** CLI flags; profiles; kernel config.
- **Compatibility:** Linux.
- **Dependencies:** Kernel features (user namespaces, LSM).
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT/Apache/GPL variants (reported; not inspected this pass — Firejail is GPL-2.0).
- **Security:** Patch kernels (CVE-2026-80521); Firejail's SUID history warrants care (general guidance).
- **Limitations:** Linux-only; profile-writing expertise (secondary).
- **Related resources:** gVisor (S-33), Deno (S-36 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-36 — Deno / Wasmtime — runtime-level sandboxes group
- **Canonical identity:** denoland/deno (secure JS runtime); bytecodealliance/wasmtime (WebAssembly runtime)
- **Category:** B10 / Sandbox runtimes (language/VM level)
- **Type:** Open-source runtimes
- **Official URL:** Not verified in this pass
- **Description:** Deno: secure-by-default JS/TS runtime (explicit --allow-* permissions for fs/net/env). Wasmtime: WASM sandbox with capability-based isolation (WASI).
- **Contents inspected:** 2026 sandbox comparisons (secondary).
- **Actual capabilities (evidence):** Can execute untrusted JS/WASM with deny-by-default permissions (secondary consensus; widely established).
- **Usage domain:** Plugin systems; edge compute; agent tool runtimes.
- **Integration method:** Runtime flags; embedding APIs.
- **Compatibility:** JS/TS (Deno); WASM (Wasmtime).
- **Dependencies:** None major.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (Deno); Apache-2.0 (Wasmtime) (widely reported).
- **Security:** Permission flags must actually be set — defaults matter (general guidance).
- **Limitations:** Language-scoped, not full OS isolation (secondary).
- **Related resources:** gVisor (S-33), Bubblewrap group (S-35).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B11. Remote isolated execution (cloud sandboxes / dev environments)

### S-37 — E2B
- **Canonical identity:** E2B — code-execution sandbox cloud ("sandbox for AI agents")
- **Category:** B11 / Remote isolated execution
- **Type:** Commercial SaaS (open-source SDK/runtime)
- **Official URL:** Not verified in this pass
- **Description:** Firecracker-based microVM sandboxes via API/SDK; purpose-built for AI agent code execution; templates, timeouts, network controls.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can execute untrusted agent-generated code in isolated cloud microVMs (vendor claim; secondary).
- **Usage domain:** Agent code execution; AI-generated code eval.
- **Integration method:** SDK (JS/Python); API.
- **Compatibility:** Language SDKs.
- **Dependencies:** E2B account.
- **Availability:** Free tier; paid.
- **Maintenance:** Active (2026 citations).
- **License:** Proprietary SaaS; SDK open (reported).
- **Security:** Code runs on vendor infra — review data-handling; set timeouts/network policy (general caution).
- **Limitations:** Vendor dependency; cost at scale (secondary).
- **Related resources:** Modal (S-38), Firecracker (S-34).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-38 — Modal / Vercel Sandbox / Cloudflare Sandbox SDK / Fly.io Machines / Riza / Val Town — group
- **Canonical identity:** Modal; Vercel Sandbox; Cloudflare Sandbox SDK (Durable Objects); Fly.io Machines; Riza (WASM code exec); Val Town (val.town)
- **Category:** B11 / Remote isolated execution
- **Type:** Commercial platforms (with OSS components)
- **Official URL:** Not verified in this pass
- **Description:** Modal: serverless Python containers for scale-out execution. Vercel Sandbox: isolated execution for AI workloads on Vercel. Cloudflare Sandbox SDK: Durable-Object-backed sandboxes at edge. Fly.io Machines: fast-boot microVMs. Riza: WASM-based polyglot code execution API. Val Town: social JS runtime with persistent vals.
- **Contents inspected:** 2026 comparisons (secondary).
- **Actual capabilities (evidence):** Can run isolated code remotely with varying isolation models (VM, WASM, container) (vendor claims; secondary).
- **Usage domain:** Agent tool execution; scale-out compute; edge sandboxes.
- **Integration method:** SDKs/APIs per platform.
- **Compatibility:** Varies by platform.
- **Dependencies:** Platform accounts.
- **Availability:** Free tiers; paid.
- **Maintenance:** Active per 2026 citations.
- **License:** Proprietary SaaS (SDKs open, reported).
- **Security:** Untrusted code on vendor infra — scope secrets/network (general caution).
- **Limitations:** Platform lock-in; isolation strength varies (secondary).
- **Related resources:** E2B (S-37), GitHub Codespaces (S-39).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

### S-39 — GitHub Codespaces / Ona (ex-Gitpod) / DevPod / CodeSandbox — cloud dev environments group
- **Canonical identity:** GitHub Codespaces; Ona (formerly Gitpod); loft-sh/devpod; CodeSandbox
- **Category:** B11 / Remote isolated execution (dev environments)
- **Type:** Commercial SaaS (Codespaces, Ona, CodeSandbox); open-source client (DevPod)
- **Official URL:** Not verified in this pass
- **Description:** Codespaces: containerized cloud dev environments on GitHub. **Ona: Gitpod rebranded after OpenAI's acquisition of Gitpod (June 2026); Gitpod Classic sunset 2026-10-15** — migration event in progress at verification date. DevPod: open-source client launching devcontainers on any backend. CodeSandbox: browser/cloud JS sandboxes.
- **Contents inspected:** 2026 reporting on Gitpod→Ona transition (secondary).
- **Actual capabilities (evidence):** Can provide isolated, reproducible dev environments in the cloud (secondary consensus).
- **Usage domain:** Remote development; agent dev environments.
- **Integration method:** devcontainer.json; IDE integrations.
- **Compatibility:** Containers/K8s; VS Code/JetBrains.
- **Dependencies:** Accounts/backends.
- **Availability:** Paid (free tiers); DevPod free OSS.
- **Maintenance:** Active; **Gitpod Classic sunsetting 2026-10-15** (transition risk).
- **License:** Proprietary SaaS; DevPod Apache-2.0 (reported).
- **Security:** Dev environments hold repo credentials — scope tokens; review (general caution).
- **Limitations:** Cost; Gitpod migration uncertainty (secondary).
- **Related resources:** devcontainers spec (S-40), E2B (S-37).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## B12. Devcontainers specification

### S-40 — Development Containers spec (devcontainers/cli)
- **Canonical identity:** devcontainers/spec + devcontainers/cli — open containerized dev-environment standard
- **Category:** B12 / Container-based dev environments
- **Type:** Open specification + reference CLI
- **Official URL:** Not verified in this pass
- **Description:** `devcontainer.json` standard: image/Dockerfile, features, lifecycle scripts, port forwarding, mounts; implemented by VS Code, Codespaces, DevPod, Ona; features registry (devcontainers/features).
- **Contents inspected:** 2026 docs and skill references (secondary).
- **Actual capabilities (evidence):** Can define reproducible containerized dev environments declaratively (secondary consensus; widely established).
- **Usage domain:** Reproducible dev/agent environments.
- **Integration method:** devcontainer.json; `devcontainer` CLI.
- **Compatibility:** Docker/Podman; supporting IDEs/hosts.
- **Dependencies:** Container runtime.
- **Availability:** Free, open spec.
- **Maintenance:** Active (2026 citations).
- **License:** MIT (spec/CLI, widely reported).
- **Security:** devcontainer.json can run lifecycle commands and mount the Docker socket — **do not auto-build untrusted devcontainer.json files** (documented risk pattern; general caution).
- **Limitations:** Container-level isolation only (see B10 for stronger); Docker-socket mounts break isolation (secondary).
- **Related resources:** GitHub Codespaces (S-39), DevPod (S-39 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

## B13. Security policy enforcement

### S-41 — OPA / Gatekeeper / Conftest — group
- **Canonical identity:** open-policy-agent/opa (policy engine); Gatekeeper (K8s admission); instrumenta/conftest (policy testing)
- **Category:** B13 / Policy enforcement
- **Type:** Open-source tools (CNCF)
- **Official URL:** Not verified in this pass
- **Description:** OPA: Rego-based policy engine. Gatekeeper: K8s admission control enforcing constraints (e.g. require signed images, block privileged pods). Conftest: tests configs (K8s, Terraform, Dockerfiles) against Rego policies in CI.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can enforce allow/deny policies on K8s admissions and CI config checks (secondary consensus; widely established).
- **Usage domain:** K8s governance; IaC policy gates.
- **Integration method:** Admission webhook (Gatekeeper); CLI/CI (Conftest); Rego bundles.
- **Compatibility:** Kubernetes; Terraform; Dockerfiles; JSON/YAML.
- **Dependencies:** K8s cluster (Gatekeeper).
- **Availability:** Free, open source.
- **Maintenance:** Active (OPA graduated CNCF; 2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Policies are enforceable controls (admission-deny), not guidance — the distinction this catalog requires.
- **Limitations:** Rego learning curve (secondary).
- **Related resources:** Kyverno (S-42), Sigstore policy-controller (S-42 group).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-42 — Kyverno / Sigstore policy-controller / Ratify — group
- **Canonical identity:** kyverno/kyverno (K8s-native policy); sigstore/policy-controller (signature verification); ratify-project/ratify (artifact verification framework)
- **Category:** B13 / Policy enforcement
- **Type:** Open-source tools
- **Official URL:** Not verified in this pass
- **Description:** Kyverno: K8s policies as YAML (validate/mutate/generate). policy-controller: admits only signed images (Sigstore/cosign). Ratify: verification framework for artifact signatures/SBOMs in registries and K8s.
- **Contents inspected:** 2026 skill docs (secondary).
- **Actual capabilities (evidence):** Can enforce signature/provenance admission policies on workloads (secondary consensus).
- **Usage domain:** Supply-chain policy enforcement in clusters/registries.
- **Integration method:** K8s admission; registry webhooks.
- **Compatibility:** Kubernetes; OCI registries.
- **Dependencies:** Sigstore infra (policy-controller); Notary/cosign (Ratify).
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Enforceable admission controls — actual technical enforcement.
- **Limitations:** K8s-scoped (secondary).
- **Related resources:** OPA/Gatekeeper (S-41), Sigstore (S-21), SLSA (S-22).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Low-Medium

## B14. Audit logs, rollback, recovery

### S-43 — restic / kopia — backup tools group
- **Canonical identity:** restic/restic; kopia/kopia
- **Category:** B14 / Backup & recovery
- **Type:** Open-source CLIs
- **Official URL:** Not verified in this pass
- **Description:** restic: fast encrypted deduplicated backups to many backends. kopia: encrypted deduplicated backups with policies, GUI, and repository server.
- **Contents inspected:** 2026 docs mentions (secondary).
- **Actual capabilities (evidence):** Can create encrypted, restorable backups with snapshots (secondary consensus; widely established).
- **Usage domain:** System/data backup; ransomware recovery.
- **Integration method:** CLI; cron/systemd; repository server (kopia).
- **Compatibility:** Linux/macOS/Windows; S3/B2/local backends.
- **Dependencies:** Storage backend.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** BSD-2-Clause (restic); Apache-2.0 (kopia) (widely reported).
- **Security:** Encryption keys must be managed; test restores (general guidance).
- **Limitations:** Backup, not real-time rollback (secondary).
- **Related resources:** Velero (S-44).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

### S-44 — Velero — Kubernetes backup
- **Canonical identity:** vmware-tanzu/velero — K8s backup/disaster recovery
- **Category:** B14 / Audit & recovery
- **Type:** Open-source tool
- **Official URL:** Not verified in this pass
- **Description:** Backs up K8s cluster resources and persistent volumes; scheduled backups, restores, cluster migration.
- **Contents inspected:** 2026 docs mentions (secondary).
- **Actual capabilities (evidence):** Can back up and restore K8s namespaces/clusters (secondary consensus; widely established).
- **Usage domain:** K8s disaster recovery.
- **Integration method:** CLI; schedules; object storage.
- **Compatibility:** Kubernetes.
- **Dependencies:** Object storage; cluster access.
- **Availability:** Free, open source.
- **Maintenance:** Active (2026 citations).
- **License:** Apache-2.0 (widely reported).
- **Security:** Backup storage holds secrets — encrypt and scope access (general caution).
- **Limitations:** K8s-only (secondary).
- **Related resources:** restic/kopia (S-43).
- **Sources:** Secondary 2026 mentions; specific URLs not captured this pass.
- **Verification date:** 2026-10-10
- **Verification:** Partially verified | **Confidence:** Medium

---

# COVERAGE NOTE

## Counts
- **Part 13 (Testing/QA, A1–A20):** 75 records (R-01–R-75), including 6 group records and 4 archive/correction-flagged records.
- **Part 14 (Security/Sandboxing/Safety, B1–B14):** 44 records (S-01–S-44), including 12 group records, 1 verified incident compilation, and 2 historical/archived flags.
- **Total: 119 records** across 34 subcategories.

### Per-subcategory counts
| Subcat | Records | Subcat | Records |
|---|---|---|---|
| A1 unit/integration | 7 (R-01–R-07) | B1 dep auditing | 6 (S-01–S-06) |
| A2 browser/E2E | 8 (R-08–R-15) | B2 container scanning | 3 (S-07–S-09) |
| A3 visual regression | 7 (R-16–R-22) | B3 secret detection | 3 (S-10–S-12) |
| A4 accessibility | 5 (R-23–R-27) | B4 secrets mgmt | 2 (S-13–S-14) |
| A5 device clouds | 3 (R-28–R-30) | B5 pentest/appsec | 4 (S-15–S-18) |
| A6 mobile | 3 (R-31–R-33) | B6 fuzzing | 2 (S-19–S-20) |
| A7 API testing | 6 (R-34–R-39) | B7 supply chain | 5 (S-21–S-25) |
| A8 contract testing | 2 (R-40–R-41) | B8 LLM security | 4 (S-26–S-29) |
| A9 DB/property | 2 (R-42–R-43) | B9 MCP security | 3 (S-30–S-32) |
| A10 load/perf | 6 (R-44–R-49) | B10 sandbox runtimes | 4 (S-33–S-36) |
| A11 type checking | 4 (R-50–R-53) | B11 remote execution | 3 (S-37–S-39) |
| A12 static analysis | 3 (R-54–R-56) | B12 devcontainers | 1 (S-40) |
| A13 coverage | 2 (R-57–R-58) | B13 policy enforcement | 2 (S-41–S-42) |
| A14 AI test gen | 2 (R-59–R-60) | B14 audit/recovery | 2 (S-43–S-44) |
| A15 AI QA agents | 3 (R-61–R-63) | | |
| A16 test mgmt | 2 (R-64–R-65) | | |
| A17 code review | 3 (R-66–R-68) | | |
| A18 synthetic | 2 (R-69–R-70) | | |
| A19 AI-code eval | 3 (R-71–R-73) | | |
| A20 QA skills | 2 (R-74–R-75) | | |

## Limitations
1. **Verification depth is uneven.** ~16 search batches established strong evidence for high-traffic tools (Playwright, axe-core, tsc, SWE-bench, Trivy incident). Long-tail records (R-59–R-70, S-23–S-24, S-38–S-39) rest on secondary comparisons only — labeled Partially verified with Low/Low-Medium confidence.
2. **Primary-source gap:** many official URLs are "Not verified in this pass" because search-result verbatim URLs were prioritized over guessing; a follow-up pass fetching repo READMEs directly would raise confidence.
3. **Dedup boundary:** ~35 already-catalogued items were cross-referenced, not re-researched, per instructions.
4. **Fast-moving 2026 events** (Gitpod→Ona sunset 2026-10-15; CVE-2026-80521; Trivy incident) are recorded as observed 2026-10-10 and will date quickly.
5. **Copyright constraint honored:** paraphrase + citations; no quote exceeds 50 words from any single work.

## Gaps & unresolved items
- **R-60 Cover-Agent:** Unverified — no search hit captured; needs a primary-source pass.
- **Incidents 2–5 in S-25** (axios, LiteLLM, Bitwarden CLI, KICS action): Partially verified from secondary reporting; exact versions/blast radius unconfirmed.
- **License fields** for ~30 records are "widely reported" rather than inspected — a LICENSE-file verification sweep is warranted.
- **Dredd/Optic/git-secrets/BackstopJS/Lost Pixel/Locust Cloud:** correctly flagged Archived/Historical; successors noted where known.
- **Single-source claims:** BackstopJS dormancy date, LambdaTest/TestMu pricing, pa11y LGPL finding (from a skill's LICENSE check — credible but secondhand).

## More work warranted?
Yes, modest: (a) a primary-source sweep fetching the ~40 "URL not verified" repos' READMEs/LICENSE files; (b) confirming S-25 incidents 2–5 against primary advisories; (c) verifying R-60 Cover-Agent; (d) re-checking the Gitpod→Ona migration after 2026-10-15. Estimated as a second research pass, not a full re-do.

*Catalog written 2026-10-10. All sources dated; verification labels per record.*
