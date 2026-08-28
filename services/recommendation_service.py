import json

from app.services.ai_service import ask_ai
from app.services.progress_service import get_progress


def generate_recommendation(student_id: str):

    progress = get_progress(student_id)

    weak_topics = progress.get("weak_topics", [])
    strong_topics = progress.get("strong_topics", [])
    overall_score = progress.get("overall_score", 0)

    if not weak_topics:
        return {
            "student_id": student_id,
            "recommended_topic": "Revision",
            "reason": "You currently don't have any major weak topics.",
            "learning_plan": [
                "Revise your recently learned concepts",
                "Take a practice quiz",
                "Try a slightly harder difficulty level"
            ],
            "difficulty": "medium"
        }

    weak_topic = progress.get("recommendation_topic")

    prompt = f"""
You are an intelligent personal AI tutor.

Student overall score: {overall_score}%
Weak topic: {weak_topic}
Strong topics: {strong_topics}

Create a personalized learning recommendation for this student.

Return ONLY valid JSON:

{{
    "recommended_topic": "{weak_topic}",
    "reason": "Why the student should learn this topic",
    "learning_plan": [
        "Step 1",
        "Step 2",
        "Step 3",
        "Step 4"
    ],
    "difficulty": "easy"
}}

The learning plan should be practical and suitable for a college student.
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    recommendation = json.loads(result)

    recommendation["student_id"] = student_id

    return recommendation