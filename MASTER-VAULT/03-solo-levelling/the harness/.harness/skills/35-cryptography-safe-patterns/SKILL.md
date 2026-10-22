---
name: cryptography-safe-patterns
domain: Security & Hardening
version: 1.0.0
tier: Essential
cap: CAP-26
triggers:
  - "encrypt"
  - "hash password"
  - "sign data"
  - "crypto"
  - "key generation"
---

# Cryptography Safe Patterns Runbook

## Objective
Enforce strict cryptographic safety standards across all application layers. This runbook mandates provably secure, modern cryptographic primitives for symmetric authenticated encryption, password hashing, digital signatures, and cryptographically secure random token generation, while strictly prohibiting deprecated, insecure, or flawed algorithms and modes.

---

## When to Activate
- When implementing data encryption at rest or in transit.
- When handling user credential hashing, authentication, and password verification.
- When generating digital signatures, verifying webhooks, or establishing asymmetric trust.
- When issuing API keys, CSRF tokens, session IDs, or password reset tokens.
- When conducting security audits and static analysis code reviews for cryptographic vulnerabilities.

---

## Step-by-Step Runbook

### Section A — Symmetric Authenticated Encryption (AES-256-GCM)
Always use Authenticated Encryption with Associated Data (AEAD). Use **AES-256-GCM** (Galois/Counter Mode). Never use ECB mode (which preserves plaintext patterns) or unauthenticated CBC mode (which is vulnerable to padding oracle attacks).

**Key Rules**:
- Generate a fresh, unique 12-byte (96-bit) nonce for every single encryption operation.
- Never reuse a nonce with the same key (nonce reuse destroys AES-GCM security).
- Prepend or package the nonce alongside the ciphertext for decryption.

```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class SymmetricCrypto:
    @staticmethod
    def generate_key() -> bytes:
        """Generates a cryptographically secure 256-bit (32-byte) AES key."""
        return AESGCM.generate_key(bit_length=256)

    @staticmethod
    def encrypt(key: bytes, plaintext: bytes, associated_data: bytes = b"") -> bytes:
        """Encrypts plaintext using AES-256-GCM with a fresh 12-byte nonce."""
        nonce = os.urandom(12)  # 96-bit nonce
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
        # Return nonce concatenated with ciphertext (including 16-byte auth tag)
        return nonce + ciphertext

    @staticmethod
    def decrypt(key: bytes, payload: bytes, associated_data: bytes = b"") -> bytes:
        """Decrypts AES-256-GCM payload and verifies authentication tag."""
        if len(payload) < 28:  # 12-byte nonce + 16-byte minimum auth tag
            raise ValueError("Invalid ciphertext payload: insufficient length.")
        
        nonce = payload[:12]
        ciphertext = payload[12:]
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, associated_data)
```

---

### Section B — Password Hashing (Argon2id)
Always use **Argon2id** (the winner of the Password Hashing Competition, combining resistance against GPU cracking and side-channel cache attacks). Never use MD5, SHA-1, plain SHA-256, or legacy algorithms. For new code, prioritize Argon2id over bcrypt.

```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

class PasswordSecurity:
    # Recommended RFC 9106 baseline parameters
    _ph = PasswordHasher(
        time_cost=3,        # 3 iterations
        memory_cost=65536,  # 64 MiB memory hardness
        parallelism=4,      # 4 concurrent threads
        hash_len=32,
        salt_len=16
    )

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Hashes a plaintext password with unique random salt using Argon2id."""
        return cls._ph.hash(password)

    @classmethod
    def verify_password(cls, stored_hash: str, candidate_password: str) -> bool:
        """Verifies password in constant-time against stored Argon2id hash."""
        try:
            return cls._ph.verify(stored_hash, candidate_password)
        except (VerifyMismatchError, InvalidHashError):
            return False

    @classmethod
    def needs_rehash(cls, stored_hash: str) -> bool:
        """Checks if hash parameters need upgrading to meet newer security baselines."""
        return cls._ph.check_needs_rehash(stored_hash)
```

---

### Section C — Asymmetric Digital Signatures (Ed25519)
Use **Ed25519** (Edwards-curve Digital Signature Algorithm). It provides high performance, 128-bit security level, immune to timing attacks, and compact 32-byte public keys and 64-byte signatures. Never use RSA-1024 or ECDSA with SHA-1.

```python
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class SignatureService:
    @staticmethod
    def generate_keypair() -> tuple[Ed25519PrivateKey, Ed25519PublicKey]:
        """Generates an Ed25519 private/public keypair."""
        private_key = Ed25519PrivateKey.generate()
        return private_key, private_key.public_key()

    @staticmethod
    def sign(private_key: Ed25519PrivateKey, message: bytes) -> bytes:
        """Generates a 64-byte deterministic Ed25519 signature."""
        return private_key.sign(message)

    @staticmethod
    def verify(public_key: Ed25519PublicKey, signature: bytes, message: bytes) -> bool:
        """Verifies an Ed25519 digital signature."""
        try:
            public_key.verify(signature, message)
            return True
        except InvalidSignature:
            return False
```

---

### Section D — Cryptographically Secure Random Tokens
Always generate secrets, session identifiers, password reset tokens, and API keys using the operating system's Cryptographically Secure Pseudo-Random Number Generator (CSPRNG via Python `secrets` module). Never use `random.random()`, `random.choice()`, or time-seeded generators.

```python
import secrets

class TokenFactory:
    @staticmethod
    def generate_api_key(prefix: str = "sk_live_") -> str:
        """Generates a 256-bit entropy API key with human-readable prefix."""
        # 32 bytes = 256 bits of CSPRNG entropy -> 64 hex characters
        raw_token = secrets.token_hex(32)
        return f"{prefix}{raw_token}"

    @staticmethod
    def generate_url_safe_token(nbytes: int = 32) -> str:
        """Generates URL-safe base64 token for email verification / password resets."""
        return secrets.token_urlsafe(nbytes)

    @staticmethod
    def constant_time_compare(val_a: str, val_b: str) -> bool:
        """Prevents timing attacks when comparing security tokens."""
        return secrets.compare_digest(val_a, val_b)
```

---

## Banned Cryptographic Algorithms & Modes

| Banned Primitive / Mode | Severe Vulnerability / Risk | Approved Modern Replacement |
| :--- | :--- | :--- |
| **MD5** | Practical collision attacks; completely broken | **SHA-256 / SHA-512 / BLAKE3** |
| **SHA-1** (for security/signatures) | Theoretical and practical collision attacks (SHAttered) | **SHA-256 / SHA-384 / Ed25519** |
| **DES / 3DES (Triple DES)** | 56-bit / 112-bit effective keys; Sweet32 64-bit block collision | **AES-256-GCM** |
| **RSA < 2048-bit** (e.g., RSA-1024) | Factorizable via modern compute; insecure | **Ed25519** or **RSA-4096 (PSS padding)** |
| **AES in ECB Mode** | Does not provide pattern diffusion; leaks structural plaintext data | **AES-256-GCM** (or ChaCha20-Poly1305) |
| **AES in CBC Mode (without HMAC)** | Vulnerable to padding oracle attacks and bit-flipping tampering | **AES-256-GCM** |
| **`random.random()` / `random.choice()`** | Mersenne Twister PRNG is fully predictable after 624 outputs | **`secrets` module** (`os.urandom`) |
| **Plain fast hashes for passwords (SHA256/MD5)** | Crushed by GPU clusters at billions of hashes per second | **Argon2id** |

---

## Completion Gate
Before deploying code involving cryptographic routines:
- [ ] **Zero banned primitives**: Static analysis confirms 0 instances of MD5, SHA-1, DES, ECB, or `random` for security tokens.
- [ ] **Authenticated encryption**: All symmetric encryption uses AES-256-GCM with fresh 12-byte random nonces.
- [ ] **Password security**: Passwords hashed and verified using Argon2id (`PasswordHasher`).
- [ ] **Modern signatures**: Asymmetric signing uses Ed25519.
- [ ] **Constant-time comparison**: Token verification utilizes `secrets.compare_digest()`.

---

## Common Pitfalls

| Anti-Pattern | Bad Implementation | Correct Solution |
| :--- | :--- | :--- |
| **Reusing AES-GCM Nonces** | `nonce = b"012345678901"` hardcoded | Generate fresh nonce per encryption: `os.urandom(12)` |
| **ECB Mode Usage** | `Cipher(AES(key), modes.ECB())` | `AESGCM(key)` |
| **Insecure Randomness** | `token = str(random.randint(100000, 999999))` | `secrets.randbelow(1000000)` or `secrets.token_hex(32)` |
| **Fast Password Hashing** | `hashlib.sha256(password.encode()).hexdigest()` | `PasswordHasher().hash(password)` (Argon2id) |
| **String Comparison of Secrets** | `if candidate_token == actual_token:` | `if secrets.compare_digest(candidate_token, actual_token):` |
