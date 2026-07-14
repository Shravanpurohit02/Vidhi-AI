from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.auth_service import AuthenticationService
from app.security.dependencies import rate_limit

router = APIRouter(prefix="/auth", tags=["Authentication"])


class LoginRequest(BaseModel):
    email: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class TokenPairResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@router.post(
    "/login",
    response_model=TokenPairResponse,
    dependencies=[Depends(rate_limit(limit=10, window_seconds=60))],
)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    try:
        return AuthenticationService.login(
            db=db,
            email=credentials.email,
            password=credentials.password,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


@router.post(
    "/refresh",
    response_model=TokenPairResponse,
    dependencies=[Depends(rate_limit(limit=20, window_seconds=60))],
)
def refresh(payload: RefreshRequest, db: Session = Depends(get_db)):
    try:
        return AuthenticationService.refresh(
            db=db,
            refresh_token=payload.refresh_token,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


@router.post("/logout", dependencies=[Depends(rate_limit(limit=30, window_seconds=60))])
def logout(payload: RefreshRequest, db: Session = Depends(get_db)):
    try:
        AuthenticationService.logout(
            db=db,
            refresh_token=payload.refresh_token,
        )
        return {"message": "Logged out successfully"}
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


class LogoutAllRequest(BaseModel):
    user_id: int


@router.post(
    "/logout-all", dependencies=[Depends(rate_limit(limit=10, window_seconds=60))]
)
def logout_all(
    payload: LogoutAllRequest,
    db: Session = Depends(get_db),
):
    return {
        "revoked_sessions": AuthenticationService.logout_all(
            db=db,
            user_id=payload.user_id,
        )
    }
