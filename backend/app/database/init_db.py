from sqlalchemy import text

from app.core.config import settings
from app.core.logging import get_logger
from app.database.database import Base, engine
import app.models  # noqa: F401

logger = get_logger()


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
        logger.info("Database connection verified.")
        logger.info("Run 'alembic upgrade head' before starting production.")
        return

    Base.metadata.create_all(bind=engine)
    logger.info("Development database initialized successfully.")


if __name__ == "__main__":
    init_database()
