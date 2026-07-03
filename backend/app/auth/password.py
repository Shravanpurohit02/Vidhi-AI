import hashlib
import secrets

from passlib.context import CryptContext

try:
    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
    )

    pwd_context.hash("vidhi_ai_test")
    USE_BCRYPT = True

except Exception:
    USE_BCRYPT = False


def hash_password(password: str) -> str:
    if USE_BCRYPT:
        return pwd_context.hash(password)

    salt = secrets.token_hex(16)
    digest = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"sha256${salt}${digest}"


def verify_password(password: str, hashed_password: str) -> bool:
    if hashed_password.startswith("sha256$"):
        _, salt, digest = hashed_password.split("$")
        return hashlib.sha256((salt + password).encode()).hexdigest() == digest

    return pwd_context.verify(password, hashed_password)
