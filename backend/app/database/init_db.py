import app.models
from sqlalchemy import text

from app.core.config import settings
from app.database.database import Base, engine


def init_database():
    """
    Initialize the database.

    Development:
        Optionally creates missing tables.

    Production:
        Verifies connectivity only.
        Database schema must be managed with Alembic.
    """

    if settings.APP_ENV.lower() == "production":
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Database connection verified.")
        print("Run 'alembic upgrade head' before starting production.")
        return

    Base.metadata.create_all(bind=engine)
    print("Development database initialized successfully.")


if __name__ == "__main__":
    init_database()
