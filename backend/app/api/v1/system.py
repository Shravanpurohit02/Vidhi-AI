from fastapi import APIRouter

from app.audit.audit_log import audit_log
from app.monitoring.metrics import metrics

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/metrics")
def get_metrics():
    metrics.increment("metrics_requests")
    return metrics.snapshot()


@router.get("/audit")
def get_audit():
    audit_log.write("audit_view")
    return audit_log.all()
