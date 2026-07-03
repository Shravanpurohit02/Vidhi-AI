from fastapi import APIRouter

from app.workers.job_queue import queue

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("/status")
def status():
    return {
        "queued_jobs": queue.size(),
    }
