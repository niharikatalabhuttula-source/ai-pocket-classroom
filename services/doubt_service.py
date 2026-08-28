from app.services.ai_service import ask_ai
import json


def answer_doubt(
    question: str,
    topic: str = "General",
    level: str = "beginner"
):

    prompt = f"""
You are an AI tutor inside an educational application called AI Pocket Classroom.

A student has asked a doubt.

Topic:
{topic}

Student level:
{level}

Student's question:
{question}

Your job is to teach the student, not just give a short answer.

Rules:
- Explain the concept clearly and simply.
- Use language suitable for the student's level.
- Give a simple example when useful.
- Break difficult concepts into small steps.
- Do not make the explanation unnecessarily complicated.
- Be encouraging.
- End with one short follow-up question to check whether the student understood.

Return ONLY valid JSON in this exact format:

{{
    "topic": "{topic}",
    "answer": "Clear explanation of the doubt",
    "example": "A simple example",
    "key_points": [
        "Important point 1",
        "Important point 2",
        "Important point 3"
    ],
    "follow_up_question": "A short question to check understanding"
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)