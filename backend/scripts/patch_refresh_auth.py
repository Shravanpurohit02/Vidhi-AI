from pathlib import Path

# ---------- security.py ----------
security = Path("app/auth/security.py")
text = security.read_text()

if "def decode_refresh_token" not in text:
    text += """

def decode_refresh_token(token: str):
    payload = decode_access_token(token)

    if payload is None:
        return None

    if payload.get("type") != "refresh":
        return None

    return payload
"""

security.write_text(text)

# ---------- auth.py ----------
auth = Path("app/api/v1/auth.py")
text = auth.read_text()

text = text.replace(
    "from app.auth.security import create_access_token",
    "from app.auth.security import create_access_token, create_refresh_token, decode_refresh_token",
)

text = text.replace(
    """class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
""",
    """class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str
""",
)

text = text.replace(
    """    token = create_access_token(
        {
            "sub": user.email,
            "uid": user.id,
        }
    )

    return TokenResponse(
        access_token=token,
    )
""",
    """    payload = {
        "sub": user.email,
        "uid": user.id,
    }

    return TokenResponse(
        access_token=create_access_token(payload),
        refresh_token=create_refresh_token(payload),
    )
""",
)

if '@router.post("/refresh"' not in text:
    text += """

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(request: RefreshTokenRequest):
    payload = decode_refresh_token(request.refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    data = {
        "sub": payload["sub"],
        "uid": payload.get("uid"),
    }

    return TokenResponse(
        access_token=create_access_token(data),
        refresh_token=create_refresh_token(data),
    )


@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}
"""

auth.write_text(text)

print("✓ Refresh authentication implemented")
