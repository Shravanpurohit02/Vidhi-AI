from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import APIRouter, Response

REQUEST_COUNT = Counter(
    "vidhi_requests_total",
    "Total HTTP requests",
)

REQUEST_LATENCY = Histogram(
    "vidhi_request_duration_seconds",
    "HTTP request latency",
)

router = APIRouter(tags=["Monitoring"])

@router.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
