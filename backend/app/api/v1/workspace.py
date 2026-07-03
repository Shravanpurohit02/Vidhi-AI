from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.hearing import HearingCreate, HearingResponse
from app.schemas.task import TaskCreate, TaskResponse
from app.services.workspace_service import WorkspaceService

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"],
)


@router.post("/hearings", response_model=HearingResponse)
def create_hearing(
    hearing: HearingCreate,
    db: Session = Depends(get_db),
):
    return WorkspaceService.create_hearing(
        db,
        hearing.model_dump(),
    )


@router.get("/hearings", response_model=list[HearingResponse])
def hearings(
    db: Session = Depends(get_db),
):
    return WorkspaceService.hearings(db)


@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
):
    return WorkspaceService.create_task(
        db,
        task.model_dump(),
    )


@router.get("/tasks", response_model=list[TaskResponse])
def tasks(
    db: Session = Depends(get_db),
):
    return WorkspaceService.tasks(db)
