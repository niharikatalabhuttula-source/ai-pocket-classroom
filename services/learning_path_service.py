from app.services.ai_service import ask_ai
from app.services.progress_service import get_progress
import json


def generate_learning_path(student_id: str):

    progress = get_progress(student_id)

    weak_topics = progress["weak_topics"]
    strong_topics = progress["strong_topics"]
    overall_score = progress["overall_score"]

    # If the student has no progress yet
    if not weak_topics and not strong_topics:
        return {
            "student_id": student_id,
            "overall_score": overall_score,
            "focus_topic": None,
            "learning_path": [
                {
                    "day": 1,
                    "activity": "Choose a topic and learn the basics"
                },
                {
                    "day": 2,
                    "activity": "Practice basic concepts"
                },
                {
                    "day": 3,
                    "activity": "Take a beginner quiz"
                }
            ]
        }

    # Select the weakest topic as the main focus
    focus_topic = weak_topics[0] if weak_topics else strong_topics[0]

    prompt = f"""
You are an AI learning coach.

Create a personalized 7-day learning path for a student.

Student overall score: {overall_score}
Weak topics: {weak_topics}
Strong topics: {strong_topics}
Main focus topic: {focus_topic}

The goal is to help the student improve their weakest area.

Create exactly 7 days.

Each day must contain:
- day number
- topic
- activity
- difficulty

Difficulty should be one of:
easy, medium, hard

Learning path should gradually increase difficulty.

Return ONLY valid JSON in this format:

{{
    "focus_topic": "{focus_topic}",
    "learning_path": [
        {{
            "day": 1,
            "topic": "Topic name",
            "activity": "What the student should do",
            "difficulty": "easy"
        }}
    ]
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    ai_result = json.loads(result)

    return {
        "student_id": student_id,
        "overall_score": overall_score,
        "focus_topic": ai_result["focus_topic"],
        "learning_path": ai_result["learning_path"]
    }