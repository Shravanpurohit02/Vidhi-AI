from __future__ import annotations

import hashlib
import hmac

_DIGEST = "sha256"


def hash_refresh_token(token: str) -> str:
    """Return SHA-256 hex digest of a refresh token."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def verify_refresh_token(token: str, token_hash: str) -> bool:
    """Constant-time verification of a refresh token."""
    expected = hash_refresh_token(token)
    return hmac.compare_digest(expected, token_hash)
