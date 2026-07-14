from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.auth.password import verify_password
from app.auth.security import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)
from app.auth.token_hash import hash_refresh_token
from app.models.refresh_token import RefreshToken
from app.repositories.refresh_token_repository import RefreshTokenRepository
from app.repositories.user_repository import UserRepository


class AuthenticationService:
    repository = RefreshTokenRepository()

    @classmethod
    def login(cls, db: Session, email: str, password: str) -> dict:
        user = UserRepository.get_by_email(db, email)

        if user is None or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")

        access_token = create_access_token({"sub": user.email, "uid": user.id})
        refresh_token = create_refresh_token({"sub": user.email, "uid": user.id})

        decoded = decode_refresh_token(refresh_token)

        record = RefreshToken(
            user_id=user.id,
            jti=decoded["jti"],
            token_hash=hash_refresh_token(refresh_token),
            issued_at=datetime.fromtimestamp(decoded["iat"], tz=UTC),
            expires_at=datetime.fromtimestamp(decoded["exp"], tz=UTC),
        )

        cls.repository.create(db, record)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",  # nosec B105
        }

    @classmethod
    def refresh(cls, db: Session, refresh_token: str) -> dict:
        from app.auth.security import (
            create_access_token,
            create_refresh_token,
            decode_refresh_token,
        )
        from app.auth.session_validation import validate_session
        from app.auth.session_rotation import rotate_session
        from app.auth.token_hash import (
            hash_refresh_token,
            verify_refresh_token,
        )

        payload = decode_refresh_token(refresh_token)

        if payload is None:
            raise ValueError("Invalid refresh token")

        session = cls.repository.find_by_jti(
            db,
            payload["jti"],
        )

        if session is None:
            raise ValueError("Session not found")

        if not validate_session(session):
            raise ValueError("Session expired or revoked")

        if not verify_refresh_token(
            refresh_token,
            session.token_hash,
        ):
            raise ValueError("Refresh token verification failed")

        rotate_session(
            db,
            session,
            repository=cls.repository,
        )

        access_token = create_access_token(
            {
                "sub": payload["sub"],
                "uid": payload["uid"],
            }
        )

        new_refresh_token = create_refresh_token(
            {
                "sub": payload["sub"],
                "uid": payload["uid"],
            }
        )

        decoded = decode_refresh_token(
            new_refresh_token,
        )

        cls.repository.create(
            db,
            RefreshToken(
                user_id=session.user_id,
                jti=decoded["jti"],
                token_hash=hash_refresh_token(
                    new_refresh_token,
                ),
                issued_at=datetime.fromtimestamp(decoded["iat"], tz=UTC),
                expires_at=datetime.fromtimestamp(decoded["exp"], tz=UTC),
            ),
        )

        return {
            "access_token": access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer",  # nosec B105
        }

    @classmethod
    def logout(cls, db: Session, refresh_token: str) -> None:
        from app.auth.security import decode_refresh_token

        payload = decode_refresh_token(refresh_token)

        if payload is None:
            raise ValueError("Invalid refresh token")

        session = cls.repository.find_by_jti(
            db,
            payload["jti"],
        )

        if session is None:
            return

        cls.repository.revoke(
            db,
            session,
        )

    @classmethod
    def logout_all(cls, db: Session, user_id: int) -> int:
        return cls.repository.revoke_all_for_user(
            db,
            user_id,
        )
