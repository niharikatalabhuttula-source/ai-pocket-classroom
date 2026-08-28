from app.services.ai_service import ask_ai
from app.services.progress_service import get_progress
import json


def generate_weakness_diagnosis(student_id: str):

    progress = get_progress(student_id)

    weak_topics = progress["weak_topics"]
    strong_topics = progress["strong_topics"]
    overall_score = progress["overall_score"]

    # No learning data yet
    if not weak_topics:
        return {
            "student_id": student_id,
            "overall_score": overall_score,
            "weak_topics": [],
            "diagnosis": "There is not enough performance data to identify a weakness yet.",
            "main_learning_gap": None,
            "recommended_action": "Complete a few quizzes so your learning pattern can be analyzed."
        }

    prompt = f"""
You are an AI learning diagnosis system.

Analyze this student's learning performance.

Overall score: {overall_score}
Weak topics: {weak_topics}
Strong topics: {strong_topics}

The student's weakest topics are:
{weak_topics}

Provide a useful educational diagnosis.

Explain:
1. Which areas need improvement.
2. Why the student may be struggling.
3. The main learning gap.
4. What the student should do next.

Keep the diagnosis encouraging and suitable for a student.

Return ONLY valid JSON:

{{
    "weak_topics": ["topic 1", "topic 2"],
    "diagnosis": "Explanation of the student's weakness",
    "main_learning_gap": "The main concept or skill the student needs to improve",
    "recommended_action": "What the student should do next"
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    ai_result = json.loads(result)

    return {
        "student_id": student_id,
        "overall_score": overall_score,
        "weak_topics": ai_result["weak_topics"],
        "diagnosis": ai_result["diagnosis"],
        "main_learning_gap": ai_result["main_learning_gap"],
        "recommended_action": ai_result["recommended_action"]
    }