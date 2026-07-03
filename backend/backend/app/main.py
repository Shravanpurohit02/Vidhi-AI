from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Vidhi AI API started.")
    yield
    logger.info("Vidhi AI API stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production-grade Legal AI Platform",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    logger.info("Root endpoint accessed.")
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Vidhi AI API is running."
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
