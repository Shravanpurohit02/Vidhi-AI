from app.auth.security import create_access_token, decode_access_token


def test_token_contains_uid():
    token = create_access_token(
        {
            "sub": "shravan@example.com",
            "uid": 1,
        }
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "shravan@example.com"
    assert payload["uid"] == 1


def test_invalid_token_returns_none():
    assert decode_access_token("invalid.token") is None
