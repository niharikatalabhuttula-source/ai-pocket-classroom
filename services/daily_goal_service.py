from app.services.ai_service import ask_ai
from app.services.progress_service import get_progress
from app.services.adaptive import get_adaptive_difficulty
import json
from datetime import date


def generate_daily_goal(student_id: str):

    progress = get_progress(student_id)

    overall_score = progress["overall_score"]
    weak_topics = progress["weak_topics"]
    strong_topics = progress["strong_topics"]

    # Choose the main focus topic
    if weak_topics:
        focus_topic = weak_topics[0]
    elif strong_topics:
        focus_topic = strong_topics[0]
    else:
        focus_topic = "General Learning"

    # Determine difficulty from overall performance
    difficulty = get_adaptive_difficulty(overall_score)

    prompt = f"""
You are an AI learning coach for a student.

Create ONE personalized daily learning goal.

Student ID:
{student_id}

Overall score:
{overall_score}

Weak topics:
{weak_topics}

Strong topics:
{strong_topics}

Focus topic:
{focus_topic}

Difficulty:
{difficulty}

Create a realistic goal that the student can complete today.

The goal should include:
- Studying the focus topic
- Practicing quiz questions
- A reasonable amount of time

Return ONLY valid JSON:

{{
    "goal": "A clear daily learning goal",
    "target_questions": 5,
    "target_minutes": 20
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    ai_result = json.loads(result)

    return {
        "student_id": student_id,
        "date": date.today().isoformat(),
        "focus_topic": focus_topic,
        "goal": ai_result["goal"],
        "target_questions": ai_result["target_questions"],
        "target_minutes": ai_result["target_minutes"],
        "difficulty": difficulty
    }