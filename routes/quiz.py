from fastapi import APIRouter


from app.models.schemas import (
    QuizRequest,
    QuizResponse,
    EvaluateRequest,
    EvaluateResponse
)

from app.services.quiz_service import (
    generate_adaptive_quiz,
    evaluate_answer
)



router = APIRouter(
    prefix="/api/quiz",
    tags=["Quiz"]
)


@router.post("/generate", response_model=QuizResponse)
def create_quiz(request: QuizRequest):
    



    
    result = generate_adaptive_quiz(
        request.student_id,
        request.topic,
        request.number_of_questions
    )

    return result


@router.post("/evaluate", response_model=EvaluateResponse)
def check_answer(request: EvaluateRequest):

    result = evaluate_answer(
        request.question,
        request.student_answer
    )

    return result