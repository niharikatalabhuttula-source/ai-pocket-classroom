import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai(prompt: str):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def generate_explanation(question: str, level: str):

    prompt = f"""
You are an AI tutor for college students.

Student level: {level}
Question: {question}

Explain this concept in very simple student-friendly language.

Return ONLY valid JSON in this format:

{{
    "topic": "short topic name",
    "explanation": "simple explanation",
    "example": "real world example",
    "key_points": [
        "point 1",
        "point 2",
        "point 3"
    ]
}}
"""

    result = ask_ai(prompt)

    # Remove markdown if Gemini adds ```json
    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)


def generate_quiz(topic: str, difficulty: str, number_of_questions: int):

    prompt = f"""
You are an AI teacher.

Topic: {topic}
Difficulty: {difficulty}
Number of questions: {number_of_questions}

Create multiple-choice questions.

Return ONLY valid JSON:

{{
    "topic": "{topic}",
    "questions": [
        {{
            "question": "question",
            "options": [
                "option 1",
                "option 2",
                "option 3",
                "option 4"
            ],
            "correct_answer": "correct option"
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

Evaluate the answer.

Return ONLY valid JSON:

{{
    "score": 0,
    "correct": false,
    "feedback": "short helpful feedback",
    "missing_concepts": [
        "concept 1"
    ]
}}

Score should be between 0 and 100.
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)