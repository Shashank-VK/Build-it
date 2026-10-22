---
name: playwright-e2e-matrix
domain: Testing & QA
version: 1.0.0
tier: Essential
cap: CAP-01/C3
triggers:
  - "e2e test"
  - "browser test"
  - "playwright"
  - "UI automation"
---

# Playwright E2E Matrix Runbook

## Objective
Deliver deterministic, flake-free end-to-end (E2E) browser automation and user journey validation using Playwright. This runbook establishes rigid standards for resilient locator hierarchies, network isolation and external API mocking, hermetic test fixtures, headless local execution, and parallel test sharding in CI pipelines.

---

## When to Activate
- When authoring, refactoring, or maintaining end-to-end browser test suites.
- When validating critical frontend user journeys (e.g., authentication, checkout flows, multi-step forms).
- When debugging flaky browser tests, timing races, or intermittent CI failures.
- When configuring CI/CD test matrices with headless parallel execution and sharded test runners.

---

## Step-by-Step Runbook

### Step 1: Use Auto-Waiting User-Facing Locators
Never use brittle CSS selectors (e.g., `div.container > form > button.btn-primary`), XPath queries, or arbitrary timeouts (`page.waitForTimeout(5000)`). Always prioritize Playwright's built-in accessible, auto-waiting locators that mirror actual user interactions:

1. **`page.getByRole(role, { name })`**: Preferred for all interactive elements (buttons, links, headings, checkboxes).
2. **`page.getByLabel(label)`**: For form inputs associated with `<label>` elements.
3. **`page.getByPlaceholder(placeholder)`**: For inputs lacking explicit labels.
4. **`page.getByText(text)`**: For locating non-interactive text content.
5. **`page.getByTestId(id)`**: Fallback only when semantic roles or accessible text are insufficient (`data-testid="..."`).

Combine locators with **Web-First Assertions** (`expect(locator)...`) which automatically poll and retry until the condition is met or timeout is reached:
```typescript
await expect(page.getByRole('button', { name: 'Submit' })).toBeVisible();
await expect(page.getByRole('button', { name: 'Submit' })).toBeEnabled();
```

### Step 2: Mock External Network Calls (`page.route()`)
Hermetic E2E tests must not depend on live external third-party services (e.g., Stripe, SendGrid, OAuth identity providers, external analytics). Mock all external network boundaries to ensure zero test flakiness and deterministic assertions:

```typescript
// Intercept external auth API
await page.route('**/api/v1/auth/login', async (route) => {
  const request = route.request();
  const postData = request.postDataJSON();

  if (postData.email === 'user@example.com' && postData.password === 'SecurePassword123!') {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      json: {
        token: 'mock-jwt-token-xyz',
        user: { id: 'usr_01', email: 'user@example.com', name: 'Alice Developer' }
      }
    });
  } else {
    await route.fulfill({
      status: 401,
      contentType: 'application/json',
      json: { error: 'Invalid credentials' }
    });
  }
});
```

### Step 3: Use Fixtures for Hermetic Setup and Teardown
Leverage Playwright test fixtures (`test.extend<T>()`) to isolate test state and encapsulate repetitive setup/teardown logic:

```typescript
// fixtures/auth.fixture.ts
import { test as base, Page } from '@playwright/test';

type AuthFixtures = {
  authenticatedPage: Page;
};

export const test = base.extend<AuthFixtures>({
  authenticatedPage: async ({ page }, use) => {
    // Setup: set authentication cookie/token in context
    await page.context().addCookies([
      {
        name: 'session_token',
        value: 'mock_valid_session_token',
        domain: 'localhost',
        path: '/'
      }
    ]);
    await use(page);
    // Teardown: clear cookies/storage
    await page.context().clearCookies();
  }
});

export { expect } from '@playwright/test';
```

### Step 4: Execute Locally in Headless Mode
Validate tests locally using headless execution and list reporting for clear, actionable feedback:

```bash
# Run all E2E tests in headless mode
npx playwright test --reporter=list

# Run a specific test file
npx playwright test tests/e2e/login.spec.ts --reporter=list

# Debug failures interactively with UI mode
npx playwright test --ui
```

### Step 5: Configure CI Sharding and Parallelism
In CI pipelines, scale test execution horizontally by partitioning test suites across multiple parallel matrix jobs using `--shard`:

```bash
# Example for a 4-runner matrix job (Runner 1 of 4)
npx playwright test --shard=1/4 --reporter=github,blob

# Runner 2 of 4
npx playwright test --shard=2/4 --reporter=github,blob

# Merge report blobs after all shards complete
npx playwright merge-reports --reporter=html ./blob-report
```

---

## Complete Example Test: Authentication Login Flow

```typescript
// tests/e2e/login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication: Login Form Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Mock backend authentication endpoint
    await page.route('**/api/v1/auth/login', async (route) => {
      const payload = route.request().postDataJSON();
      if (payload.email === 'admin@example.com' && payload.password === 'CorrectPassword123!') {
        await route.fulfill({
          status: 200,
          contentType: 'application/json',
          json: {
            success: true,
            user: { id: 'usr_admin', name: 'Admin User', role: 'admin' },
            token: 'valid-jwt-token'
          }
        });
      } else {
        await route.fulfill({
          status: 401,
          contentType: 'application/json',
          json: { success: false, message: 'Invalid email or password' }
        });
      }
    });

    // Navigate to login page
    await page.goto('/login');
  });

  test('successfully logs in with valid credentials and redirects to dashboard', async ({ page }) => {
    // Locate elements using auto-waiting semantic locators
    const emailInput = page.getByLabel('Email Address');
    const passwordInput = page.getByLabel('Password');
    const submitButton = page.getByRole('button', { name: 'Sign In' });

    // Assert initial visibility
    await expect(emailInput).toBeVisible();
    await expect(passwordInput).toBeVisible();
    await expect(submitButton).toBeEnabled();

    // Fill form
    await emailInput.fill('admin@example.com');
    await passwordInput.fill('CorrectPassword123!');
    await submitButton.click();

    // Assert successful navigation and dashboard state
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.getByRole('heading', { level: 1, name: 'Dashboard' })).toBeVisible();
    await expect(page.getByText('Welcome back, Admin User')).toBeVisible();
  });

  test('displays validation error banner on invalid credentials', async ({ page }) => {
    const emailInput = page.getByLabel('Email Address');
    const passwordInput = page.getByLabel('Password');
    const submitButton = page.getByRole('button', { name: 'Sign In' });

    await emailInput.fill('admin@example.com');
    await passwordInput.fill('WrongPassword!');
    await submitButton.click();

    // Assert error alert displays with proper text
    const errorAlert = page.getByRole('alert');
    await expect(errorAlert).toBeVisible();
    await expect(errorAlert).toContainText('Invalid email or password');
    await expect(page).toHaveURL(/.*login/);
  });
});
```

---

## Completion Gate
Before declaring Playwright E2E test suites ready:
- [ ] **Zero manual sleeps**: No occurrences of `page.waitForTimeout()` or `setTimeout()` anywhere in the test codebase.
- [ ] **Semantic locators**: All interactions rely on `getByRole`, `getByLabel`, `getByText`, or `getByTestId`.
- [ ] **Network hermeticity**: All third-party external API requests are intercepted and mocked via `page.route()`.
- [ ] **Headless passing**: `npx playwright test --reporter=list` exits with code 0 in headless mode.
- [ ] **CI sharding configuration**: Sharding parameters (`--shard=X/Y`) and report merge steps are documented for CI runners.

---

## Common Pitfalls

| Anti-Pattern | Bad Implementation | Correct Solution |
| :--- | :--- | :--- |
| **Arbitrary Timeouts** | `await page.waitForTimeout(5000);` | Rely on auto-waiting assertions: `await expect(el).toBeVisible();` |
| **Brittle CSS Hierarchy** | `page.locator('div > .card > form button:nth-child(2)')` | `page.getByRole('button', { name: 'Submit' })` |
| **Unmocked Third-Party APIs** | Calling live Stripe/Auth0 endpoints in CI runs | Intercept with `page.route('**/stripe/**', route => route.fulfill(...))` |
| **Shared Mutable Context** | Reusing a single browser page across disparate tests | Use isolated fixtures and browser contexts per test |
| **Missing Headless Check** | Tests only pass in headed mode due to viewport assumptions | Explicitly configure viewport in `playwright.config.ts` and verify headlessly |
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
