---
name: bos-pytest-fixture-factory
domain: Testing & QA
version: 1.0.0
tier: Essential
cap: CAP-32
triggers:
  - "pytest fixture"
  - "test setup"
  - "database fixture"
  - "parametrize"
---

# Pytest Fixture Factory Runbook

## Objective
Author modular, high-performance, and hermetic Pytest fixture architectures. This runbook establishes patterns for precise fixture scoping, unified `yield`-based setup and teardown, transaction-isolated database testing without table truncation, combinatorial parameter matrix generation, and clean `conftest.py` hierarchical inheritance.

---

## When to Activate
- When architecting or refactoring Python test suites and fixture hierarchies.
- When creating reusable test dependencies (database sessions, HTTP client instances, mock services, authenticated users).
- When resolving test pollution, order-dependent failures, or slow database test suites.
- When designing comprehensive input matrices with `@pytest.mark.parametrize`.

---

## Step-by-Step Runbook

### Step 1: Select the Optimal Fixture Scope
Pytest supports four primary fixture lifecycles. Always choose the broadest scope that does not introduce mutable state pollution:

1. **`scope="session"`**: Initialized once per test run. Reserved strictly for immutable or expensive shared resources (e.g., SQLAlchemy `Engine`, Docker testcontainers, temporary directories).
2. **`scope="module"`**: Initialized once per test file. Ideal for read-only fixtures shared across tests in a single file.
3. **`scope="class"`**: Initialized once per test class. Useful for organizing tests sharing expensive setup.
4. **`scope="function"` (Default)**: Initialized fresh for each individual test function. Mandatory for all mutable state, database transactions, mock patches, and user sessions.

### Step 2: Use `yield` Fixtures for Unified Setup and Teardown
Never separate setup and teardown into disparate hooks. Encapsulate lifecycle management within a single `@pytest.fixture` using Python's `yield` statement:

```python
import pytest

@pytest.fixture
def managed_resource():
    # --- SETUP PHASE ---
    resource = allocate_resource()
    resource.connect()
    
    yield resource  # Injected into the requesting test
    
    # --- TEARDOWN PHASE (Runs even if test fails) ---
    resource.disconnect()
    resource.cleanup()
```

### Step 3: Implement Database Transaction Rollback Isolation
Never truncate or re-create database tables between tests—this causes severe performance degradation. Instead, use nested database transactions (savepoints) and roll back all mutations upon test completion:

1. **Session Scope**: Create the database engine, run schema migrations once, and dispose of the engine on session exit.
2. **Function Scope**: Open a connection, start an outer transaction, bind an ORM session, yield the session to the test, and unconditionally roll back the transaction in the teardown phase.

### Step 4: Construct Combinatorial Parametrized Matrices
Use `@pytest.mark.parametrize` to systematically evaluate boundary values, equivalence partitions, and error states without duplicating test logic:

```python
@pytest.mark.parametrize(
    "input_val, expected_status, expected_error",
    [
        pytest.param("valid_user@test.com", 200, None, id="valid_email"),
        pytest.param("missing-at-domain.com", 422, "Invalid email format", id="missing_at_symbol"),
        pytest.param("", 400, "Email cannot be empty", id="empty_string"),
        pytest.param("a" * 300 + "@test.com", 422, "Email exceeds max length", id="exceeds_max_len"),
    ]
)
def test_user_email_validation(client, input_val, expected_status, expected_error):
    response = client.post("/api/v1/users", json={"email": input_val})
    assert response.status_code == expected_status
    if expected_error:
        assert expected_error in response.json()["detail"]
```

### Step 5: Structure Shared vs Module-Specific `conftest.py`
Maintain a clean fixture discovery hierarchy:
- **Root `tests/conftest.py`**: Global engine configurations, environment variable overrides, HTTP client factories, and general assertions.
- **Subdirectory `tests/api/conftest.py`**: API route clients, OAuth bearer tokens, mock payment providers.
- **Subdirectory `tests/unit/conftest.py`**: Fast in-memory fakes and mock objects.

---

## Code Examples

### 1. Session-Scoped Database Engine Fixture
```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

TEST_DATABASE_URL = "postgresql://test_user:test_pass@localhost:5432/test_db"
Base = declarative_base()

@pytest.fixture(scope="session")
def db_engine():
    """Initializes the database schema once for the entire test session."""
    engine = create_engine(TEST_DATABASE_URL, pool_pre_ping=True)
    
    # Apply schema / migrations
    Base.metadata.create_all(bind=engine)
    
    yield engine
    
    # Drop all tables on test suite completion
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
```

### 2. Function-Scoped DB Session with Transaction Rollback & User Factory
```python
# tests/conftest.py
import pytest
from sqlalchemy.orm import sessionmaker, Session
from src.models.user import User

@pytest.fixture(scope="function")
def db_session(db_engine) -> Session:
    """Wraps each test in an isolated transaction that is rolled back on teardown."""
    connection = db_engine.connect()
    transaction = connection.begin()
    
    SessionLocal = sessionmaker(bind=connection, autoflush=False, autocommit=False)
    session = SessionLocal()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def user_factory(db_session: Session):
    """Factory fixture for generating test users with automatic rollback."""
    created_users = []
    
    def _create_user(email: str = "test@example.com", role: str = "member") -> User:
        user = User(email=email, role=role, is_active=True)
        db_session.add(user)
        db_session.flush()  # Assigns primary key without committing
        created_users.append(user)
        return user
        
    return _create_user
```

### 3. Parametrized Input Matrix Test
```python
# tests/test_user_service.py
import pytest
from src.services.user_service import calculate_account_tier

@pytest.mark.parametrize(
    "credits_spent, active_months, expected_tier",
    [
        pytest.param(0, 1, "free", id="new_free_user"),
        pytest.param(99, 12, "free", id="sub_threshold_long_tenure"),
        pytest.param(100, 1, "silver", id="silver_minimum_spend"),
        pytest.param(499, 5, "silver", id="silver_upper_bound"),
        pytest.param(500, 6, "gold", id="gold_minimum_spend"),
        pytest.param(10000, 24, "platinum", id="platinum_high_value"),
    ]
)
def test_calculate_account_tier(credits_spent: int, active_months: int, expected_tier: str):
    tier = calculate_account_tier(credits=credits_spent, months=active_months)
    assert tier == expected_tier
```

---

## Completion Gate
Before deploying test suites:
- [ ] **Appropriate scoping**: All expensive connections/engines are session-scoped; all state mutations are function-scoped.
- [ ] **Deterministic rollback**: Zero database mutations survive test execution (verified by checking row counts post-run).
- [ ] **Unified teardown**: All fixture setup/teardown pairs use `yield`.
- [ ] **Parametrization coverage**: Edge cases, boundary conditions, and null states are tested with explicit parameter IDs.
- [ ] **No order dependency**: Tests succeed when executed in random order (`pytest --randomly-seed=42`).

---

## Common Pitfalls

| Anti-Pattern | Bad Implementation | Correct Solution |
| :--- | :--- | :--- |
| **Table Truncation in Teardown** | Executing `TRUNCATE TABLE` or `DELETE FROM` after every test | Use nested database transactions with `rollback()` |
| **Function-Scoped Engines** | Recreating SQLAlchemy `create_engine()` on every test | Scope `db_engine` to `session` |
| **Shared Mutable Fixture Return** | Returning a shared dictionary or list from a `session` fixture | Return immutable objects or use `function` scope |
| **Silent Fixture Failure** | Uncaught exceptions in teardown leaving open connections | Encapsulate teardown in robust `try...finally` blocks |
| **Unindexed Parametrize** | `@pytest.mark.parametrize("x", [1, 2, 3])` without IDs | Provide explicit `pytest.param(..., id="...")` labels |
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
