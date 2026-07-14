from __future__ import annotations

import time

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

from app.legal.drafting.generators.document_generator import (
    DocumentGenerator,
)
from app.legal.drafting.review.reviewer import DraftReviewer

router = APIRouter(
    prefix="/drafting",
    tags=["AI Drafting"],
)

generator = DocumentGenerator()
reviewer = DraftReviewer()


SUPPORTED_TEMPLATES = {
    "legal_notice",
    "plaint",
    "written_statement",
    "affidavit",
    "petition",
    "agreement",
    "contract",
    "reply",
    "application",
}


class DraftRequest(BaseModel):
    conversation_id: str = "drafting"
    template: str
    facts: str
    relief: str | None = None
    provider: str | None = None


@router.post("/generate")
def generate(
    request: DraftRequest,
):

    if request.template not in SUPPORTED_TEMPLATES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported template: {request.template}",
        )

    start = time.perf_counter()

    draft = generator.generate(
        conversation_id=request.conversation_id,
        template=request.template,
        facts=request.facts
        + (f"\n\nRelief Sought:\n{request.relief}" if request.relief else ""),
        provider=request.provider,
    )

    review = reviewer.review(draft)

    processing_time = round(time.perf_counter() - start, 6)

    return {
        "template": request.template,
        "provider": request.provider or "mock",
        "document": draft,
        "processing_time": processing_time,
        "word_count": len(draft.split()),
        "review": review,
    }


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "module": "drafting",
    }
