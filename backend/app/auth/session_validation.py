from __future__ import annotations

from datetime import UTC, datetime

from app.models.refresh_token import RefreshToken


def is_session_expired(session: RefreshToken) -> bool:
    return session.expires_at <= datetime.now(UTC).replace(tzinfo=None)


def is_session_revoked(session: RefreshToken) -> bool:
    return session.revoked_at is not None


def validate_session(session: RefreshToken) -> bool:
    if session is None:
        return False
    if is_session_revoked(session):
        return False
    if is_session_expired(session):
        return False
    return True
