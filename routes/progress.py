from fastapi import APIRouter
from app.services.recommendation_service import generate_recommendation
from app.services.progress_service import get_learning_streak
from app.services.learning_path_service import generate_learning_path
from app.services.weakness_service import generate_weakness_diagnosis

from app.models.schemas import (
    ProgressRequest,
    ProgressResponse,
    StreakResponse,
    LearningPathResponse,
    WeaknessDiagnosisResponse
)

from app.services.progress_service import (
    record_progress,
    get_progress
)


router = APIRouter(
    prefix="/api/progress",
    tags=["Progress"]
)


@router.post("/record", response_model=ProgressResponse)
def save_progress(request: ProgressRequest):

    return record_progress(
        request.student_id,
        request.topic,
        request.score
    )


@router.get("/{student_id}/recommendation")
def recommendation(student_id: str):

    return generate_recommendation(student_id)


@router.get("/streak/{student_id}", response_model=StreakResponse)
def get_streak(student_id: str):

    streak = get_learning_streak(student_id)

    return {
        "student_id": student_id,
        "current_streak": streak
    }


@router.get(
    "/learning-path/{student_id}",
    response_model=LearningPathResponse
)
def learning_path(student_id: str):

    return generate_learning_path(student_id)


@router.get(
    "/weakness-diagnosis/{student_id}",
    response_model=WeaknessDiagnosisResponse
)
def weakness_diagnosis(student_id: str):

    return generate_weakness_diagnosis(student_id)



@router.get("/{student_id}")
def progress(student_id: str):

    return get_progress(student_id)




