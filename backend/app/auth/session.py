from __future__ import annotations

from app.repositories.refresh_token_repository import RefreshTokenRepository


class SessionManager:
    """Session management facade for refresh-token backed sessions."""

    def __init__(self, repository: RefreshTokenRepository | None = None):
        self.repository = repository or RefreshTokenRepository()

    def get_session_by_jti(self, db, jti: str):
        return self.repository.find_by_jti(db, jti)

    def get_active_sessions(self, db, user_id: int):
        return self.repository.find_active_for_user(db, user_id)

    def revoke_session(self, db, token, *, replaced_by_jti: str | None = None):
        return self.repository.revoke(
            db,
            token,
            replaced_by_jti=replaced_by_jti,
        )

    def revoke_all_sessions(self, db, user_id: int):
        return self.repository.revoke_all_for_user(db, user_id)
