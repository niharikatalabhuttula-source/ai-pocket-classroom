from collections import defaultdict

from app.database.database import (
    save_progress,
    get_student_progress,
    get_connection
)
from app.services.adaptive import get_adaptive_difficulty


def record_progress(student_id: str, topic: str, score: int):

    save_progress(student_id,topic,score)
    record_learning_activity(student_id)

    return {
        "message": "Progress recorded successfully",
        "student_id": student_id,
        "topic": topic,
        "score": score
    }


def get_progress(student_id: str):

    records = get_student_progress(student_id)

    if not records:
        return {
            "student_id": student_id,
            "overall_score": 0,
            "strong_topics": [],
            "weak_topics": [],
            "recommended_topic": None,
            "records": []
        }

    topic_scores = defaultdict(list)

    for record in records:
        topic_scores[record["topic"]].append(record["score"])

    averages = {
        topic: sum(scores) / len(scores)
        for topic, scores in topic_scores.items()
    }

    weak_topics = [
        topic for topic, score in averages.items()
        if score < 60
    ]

    strong_topics = [
        topic for topic, score in averages.items()
        if score >= 75
    ]

    recommended_topic = None

    if weak_topics:
        recommended_topic = min(
            weak_topics,
            key=lambda topic: averages[topic]
        )

    overall_score = sum(
        record["score"] for record in records
    ) / len(records)

    return {
        "student_id": student_id,
        "overall_score": round(overall_score),
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "recommended_topic": recommended_topic,
        "records": records
    }
def get_topic_score(student_id: str, topic: str):
    records = get_student_progress(student_id)

    topic_scores = [
        record["score"]
        for record in records
        if record["topic"].lower() == topic.lower()
    ]

    if not topic_scores:
        return None

    return sum(topic_scores) / len(topic_scores)
from datetime import date, timedelta


def record_learning_activity(student_id: str):

    conn = get_connection()

    today = date.today().isoformat()

    conn.execute(
        """
        INSERT OR IGNORE INTO learning_activity
        (student_id, activity_date)
        VALUES (?, ?)
        """,
        (student_id, today)
    )

    conn.commit()
    conn.close()


def get_learning_streak(student_id: str):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT activity_date
        FROM learning_activity
        WHERE student_id = ?
        ORDER BY activity_date DESC
        """,
        (student_id,)
    ).fetchall()

    conn.close()

    if not rows:
        return 0

    activity_dates = {
        date.fromisoformat(row["activity_date"])
        for row in rows
    }

    today = date.today()

    # If the student did not study today or yesterday,
    # the current streak is broken.
    if today not in activity_dates and (today - timedelta(days=1)) not in activity_dates:
        return 0

    # Start from today if they studied today.
    # Otherwise start from yesterday.
    current_date = today if today in activity_dates else today - timedelta(days=1)

    streak = 0

    while current_date in activity_dates:
        streak += 1
        current_date -= timedelta(days=1)

    return streak
