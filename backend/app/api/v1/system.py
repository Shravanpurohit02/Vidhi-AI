# backend/app/api/v1/system.py

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from app.audit.audit_log import audit_log
from app.monitoring.metrics import metrics
import logging

# Initialize Logger
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/system",
    tags=["System"],
)

@router.get("/metrics")
def get_metrics():
    """
    Retrieves the current metrics snapshot and increments the metrics request counter.
    
    Returns:
    - A JSON response containing the metrics snapshot.
    """
    try:
        metrics.increment("metrics_requests")
        return metrics.snapshot()
    except Exception as e:
        logger.error(f"Failed to retrieve metrics: {str(e)}")
        return JSONResponse(content={"error": "Failed to retrieve metrics"}, status_code=500)

@router.get("/audit")
def get_audit():
    """
    Writes an audit log entry for viewing the audit log and returns all audit log entries.
    
    Returns:
    - A JSON response containing all audit log entries.
    """
    try:
        audit_log.write("audit_view")
        return audit_log.all()
    except Exception as e:
        logger.error(f"Failed to retrieve audit log: {str(e)}")
        return JSONResponse(content={"error": "Failed to retrieve audit log"}, status_code=500)

@router.get("/healthcheck")
def healthcheck():
    """
    Performs a basic health check of the system.
    
    Returns:
    - A 200 OK response if the system is healthy.
    """
    try:
        # Basic health check: Verify dependencies are accessible
        # For demonstration, this checks if metrics and audit log services are responsive
        metrics.increment("healthcheck_requests")
        audit_log.write("healthcheck")
        return Response(content="OK", status_code=200)
    except Exception as e:
        logger.error(f"Healthcheck failed: {str(e)}")
        return Response(content="Service Unavailable", status_code=503)