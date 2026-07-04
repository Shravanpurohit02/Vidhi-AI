from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from app.court.captcha import captcha_service
from app.court.schemas import (
    ImportCourtCaseRequest,
    SearchByCNRRequest,
)
from app.court.service import CourtService
from app.court.session import session_manager

router = APIRouter(
    prefix="/court",
    tags=["Court Services"],
)

service = CourtService()


@router.get(
    "/captcha",
    responses={
        200: {
            "content": {
                "image/png": {}
            },
            "description": "Official eCourts CAPTCHA image",
        }
    },
)
async def captcha():
    sid = session_manager.create()
    image = captcha_service.fetch(sid)

    return Response(
        content=image,
        media_type="image/png",
        headers={
            "X-Session-ID": sid,
        },
    )


@router.post("/search-by-cnr")
async def search_by_cnr(request: SearchByCNRRequest):
    return await service.search_by_cnr(
        session_id=request.session_id,
        cnr=request.cnr,
        captcha=request.captcha,
    )


@router.post("/import")
async def import_case(request: ImportCourtCaseRequest):
    return await service.search_by_cnr(
        session_id=request.session_id,
        cnr=request.cnr,
        captcha=request.captcha,
    )
