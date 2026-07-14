from fastapi import APIRouter

from app.ai_observability.services.metrics import ai_metrics
from app.ai_observability.storage.trace_store import trace_store

router = APIRouter(
    prefix="/ai-observability",
    tags=["AI Observability"],
)


@router.get("/metrics")
def metrics():
    return ai_metrics.summary()


@router.get("/traces")
def traces():
    return trace_store.all()


@router.delete("/traces")
def clear_traces():
    trace_store.clear()
    return {"message": "Trace store cleared"}
