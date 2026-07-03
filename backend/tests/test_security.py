from app.auth.security import (
    create_access_token,
    decode_access_token,
)


def test_create_access_token():
    token = create_access_token(
        {"sub": "shravan@example.com"}
    )

    assert isinstance(token, str)
    assert len(token) > 20


def test_decode_access_token():
    token = create_access_token(
        {"sub": "shravan@example.com"}
    )

    payload = decode_access_token(token)

    assert payload is not None
    assert payload["sub"] == "shravan@example.com"


def test_invalid_token():
    assert decode_access_token("invalid.token") is None
