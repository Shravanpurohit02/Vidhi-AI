from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.workflows.schemas.dashboard_response import (
    DashboardResponse,
)
from app.workflows.workflow_service import WorkflowService

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"],
)


@router.get(
    "/dashboard",
    response_model=DashboardResponse,
)
def dashboard(
    db: Session = Depends(get_db),
):
    return WorkflowService.dashboard(db)
