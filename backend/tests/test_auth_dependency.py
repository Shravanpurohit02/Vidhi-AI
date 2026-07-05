from app.auth.security import create_access_token, decode_access_token


def test_access_token_contains_subject():
    token = create_access_token({"sub": "shravan@example.com"})

    payload = decode_access_token(token)

    assert payload["sub"] == "shravan@example.com"
