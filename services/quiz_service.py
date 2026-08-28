from app.services.ai_service import ask_ai
import json

from app.services.progress_service import get_topic_score
from app.services.adaptive import get_adaptive_difficulty


def generate_quiz(
    topic: str,
    difficulty: str,
    number_of_questions: int
):

    prompt = f"""
You are an AI teacher creating a quiz for a student.

Topic: {topic}
Difficulty: {difficulty}
Number of questions: {number_of_questions}

Create multiple-choice questions.

Rules:
- Give exactly {number_of_questions} questions.
- Each question must have 4 options.
- Only one option should be correct.
- Keep questions suitable for the requested difficulty.

Difficulty guidelines:

EASY:
- Test basic definitions and fundamental concepts.
- Use simple examples.
- Avoid complicated reasoning.

MEDIUM:
- Test understanding and application.
- Include practical examples.
- Require some reasoning.

HARD:
- Test deeper understanding.
- Include challenging problems.
- Require multi-step reasoning or application.

Return ONLY valid JSON in this format:

{{
    "topic": "{topic}",
    "questions": [
        {{
            "question": "Question here",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correct_answer": "Option A"
        }}
    ]
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)


def evaluate_answer(question: str, student_answer: str):

    prompt = f"""
You are an AI tutor evaluating a student's answer.

Question:
{question}

Student answer:
{student_answer}

Evaluate how well the student understands the concept.

Return ONLY valid JSON:

{{
    "score": 0,
    "correct": false,
    "feedback": "Helpful feedback for the student",
    "missing_concepts": []
}}

Rules:
- score must be between 0 and 100.
- correct should be true if the answer is substantially correct.
- Give encouraging and educational feedback.
- Mention concepts the student missed.
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)


def generate_adaptive_quiz(
    student_id: str,
    topic: str,
    number_of_questions: int = 5
):

    # Get the student's previous performance for this topic
    previous_score = get_topic_score(
        student_id,
        topic
    )

    # Decide the next difficulty
    difficulty = get_adaptive_difficulty(
        previous_score
    )

    # Generate quiz using the selected difficulty
    quiz = generate_quiz(
        topic,
        difficulty,
        number_of_questions
    )

    # Include difficulty in the response
    quiz["difficulty"] = difficulty

    # Include previous score so the frontend can display it
    quiz["previous_score"] = previous_score

    return quiz