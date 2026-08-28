from pydantic import BaseModel
from typing import List, Optional


class ExplanationRequest(BaseModel):
    question: str
    level: str = "beginner"


class ExplanationResponse(BaseModel):
    topic: str
    explanation: str
    example: str
    key_points: List[str]


class QuizRequest(BaseModel):
    student_id:str
    topic: str
    number_of_questions: int = 5


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: str


class QuizResponse(BaseModel):
    topic: str
    difficulty: str
    previous_score:Optional[float]=None
    questions: List[QuizQuestion]


class EvaluateRequest(BaseModel):
    question: str
    student_answer: str


class EvaluateResponse(BaseModel):
    score: int
    correct: bool
    feedback: str
    missing_concepts: List[str]


class ProgressRequest(BaseModel):
    student_id: str
    topic: str
    score: int


class ProgressResponse(BaseModel):
    message: str
    student_id: str
    topic: str
    score: int

class StreakResponse(BaseModel):
    student_id:str
    current_streak:int

class LearningPathDay(BaseModel):
    day: int
    topic: str
    activity: str
    difficulty: str


class LearningPathResponse(BaseModel):
    student_id: str
    overall_score: int
    focus_topic: Optional[str]
    learning_path: List[LearningPathDay]

class WeaknessDiagnosisResponse(BaseModel):
    student_id: str
    overall_score: int
    weak_topics: List[str]
    diagnosis: str
    main_learning_gap: Optional[str]
    recommended_action: str

class DoubtRequest(BaseModel):
    question: str
    topic: str = "General"
    level: str = "beginner"


class DoubtResponse(BaseModel):
    topic: str
    answer: str
    example: str
    key_points: List[str]
    follow_up_question: str

class DailyGoalResponse(BaseModel):
    student_id: str
    date: str
    focus_topic: str
    goal: str
    target_questions: int
    target_minutes: int
    difficulty: str

class Achievement(BaseModel):
    name: str
    icon: str
    description: str


class AchievementResponse(BaseModel):
    student_id: str
    overall_score: int
    current_streak: int
    total_achievements: int
    achievements: List[Achievement]