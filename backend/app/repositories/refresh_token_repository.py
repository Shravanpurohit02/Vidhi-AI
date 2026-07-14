from __future__ import annotations

from datetime import datetime
from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken


class RefreshTokenRepository:
    """Repository for persistent refresh-token management."""

    @staticmethod
    def create(db: Session, token: RefreshToken) -> RefreshToken:
        db.add(token)
        db.commit()
        db.refresh(token)
        return token

    @staticmethod
    def find_by_jti(db: Session, jti: str) -> RefreshToken | None:
        return db.query(RefreshToken).filter(RefreshToken.jti == jti).first()

    @staticmethod
    def find_active_for_user(
        db: Session,
        user_id: int,
    ) -> list[RefreshToken]:
        return (
            db.query(RefreshToken)
            .filter(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked_at.is_(None),
            )
            .order_by(RefreshToken.issued_at.desc())
            .all()
        )

    @staticmethod
    def revoke(
        db: Session,
        token: RefreshToken,
        *,
        replaced_by_jti: str | None = None,
    ) -> RefreshToken:
        token.revoked_at = datetime.utcnow()
        token.replaced_by_jti = replaced_by_jti
        db.add(token)
        db.commit()
        db.refresh(token)
        return token

    @staticmethod
    def revoke_all_for_user(db: Session, user_id: int) -> int:
        tokens = (
            db.query(RefreshToken)
            .filter(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked_at.is_(None),
            )
            .all()
        )

        now = datetime.utcnow()
        for token in tokens:
            token.revoked_at = now

        db.commit()
        return len(tokens)

    @staticmethod
    def delete_expired(db: Session, now: datetime) -> int:
        count = (
            db.query(RefreshToken)
            .filter(RefreshToken.expires_at < now)
            .delete(synchronize_session=False)
        )
        db.commit()
        return count
