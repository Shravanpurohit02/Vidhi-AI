from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.api.v1.profile import router as profile_router
from app.api.v1.auth import router as auth_router
from app.api.v1.cases import router as cases_router
from app.api.v1.documents import router as documents_router
from app.core.config import settings
from app.core.logging import get_logger
from app.database.init_db import init_database

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    logger.info("Database initialized.")
    logger.info("Vidhi AI API started.")
    yield
    logger.info("Vidhi AI API stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production-grade Legal AI Platform",
    lifespan=lifespan,
)

app.include_router(users_router)
app.include_router(profile_router)
app.include_router(auth_router)
app.include_router(cases_router)
app.include_router(documents_router)


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Vidhi AI API is running."
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
