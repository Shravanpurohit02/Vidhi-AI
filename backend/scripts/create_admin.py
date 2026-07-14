from getpass import getpass

from app.auth.password import hash_password
from app.database.database import SessionLocal
from app.models.user import User
from app.repositories.user_repository import UserRepository


def main():
    db = SessionLocal()

    try:
        existing = db.query(User).filter(User.role == "admin").first()

        if existing:
            print(f"Admin already exists: {existing.email}")
            return

        print("\\n=== Create First Administrator ===\\n")

        full_name = input("Full name: ").strip()
        email = input("Email: ").strip()
        password = getpass("Password: ")

        UserRepository.create(
            db=db,
            full_name=full_name,
            email=email,
            password=hash_password(password),
            role="admin",
        )

        print("\\nAdministrator created successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
