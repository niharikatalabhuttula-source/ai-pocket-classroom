from fastapi import APIRouter

from app.models.schemas import DailyGoalResponse
from app.services.daily_goal_service import generate_daily_goal


router = APIRouter(
    prefix="/api/goals",
    tags=["Daily Learning Goal"]
)


@router.get(
    "/{student_id}",
    response_model=DailyGoalResponse
)
def get_daily_goal(student_id: str):

    return generate_daily_goal(student_id)