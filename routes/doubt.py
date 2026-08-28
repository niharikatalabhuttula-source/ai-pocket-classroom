from fastapi import APIRouter

from app.models.schemas import (
    DoubtRequest,
    DoubtResponse
)

from app.services.doubt_service import answer_doubt


router = APIRouter(
    prefix="/api/doubt",
    tags=["AI Doubt Tutor"]
)


@router.post("/ask", response_model=DoubtResponse)
def ask_doubt(request: DoubtRequest):

    return answer_doubt(
        request.question,
        request.topic,
        request.level
    )