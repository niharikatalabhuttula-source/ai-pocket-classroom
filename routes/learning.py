from fastapi import APIRouter
from app.models.schemas import (
    ExplanationRequest,
    ExplanationResponse
)
from app.services.ai_service import generate_explanation

router = APIRouter(
    prefix="/api/learn",
    tags=["Learning"]
)


@router.post("/explain", response_model=ExplanationResponse)
def explain_topic(request: ExplanationRequest):

    result = generate_explanation(
        request.question,
        request.level
    )

    return result