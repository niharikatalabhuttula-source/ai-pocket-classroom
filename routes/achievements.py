from fastapi import APIRouter

from app.models.schemas import AchievementResponse
from app.services.achievement_service import get_achievements


router = APIRouter(
    prefix="/api/achievements",
    tags=["Achievements"]
)


@router.get(
    "/{student_id}",
    response_model=AchievementResponse
)
def achievements(student_id: str):

    return get_achievements(student_id)