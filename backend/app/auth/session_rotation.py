from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from app.auth.session_validation import validate_session
from app.repositories.refresh_token_repository import RefreshTokenRepository


def rotate_session(
    db,
    session,
    repository: RefreshTokenRepository | None = None,
):
    if not validate_session(session):
        raise ValueError("Session is invalid or expired")

    repo = repository or RefreshTokenRepository()
    new_jti = str(uuid4())

    repo.revoke(
        db,
        session,
        replaced_by_jti=new_jti,
    )

    return new_jti


def cleanup_expired_sessions(
    db,
    repository: RefreshTokenRepository | None = None,
) -> int:
    repo = repository or RefreshTokenRepository()
    return repo.delete_expired(
        db,
        datetime.now(UTC).replace(tzinfo=None),
    )
