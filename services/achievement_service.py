from app.services.progress_service import (
    get_progress,
    get_learning_streak
)


def get_achievements(student_id: str):

    progress = get_progress(student_id)
    streak = get_learning_streak(student_id)

    records = progress["records"]
    overall_score = progress["overall_score"]
    strong_topics = progress["strong_topics"]

    achievements = []

    # First Quiz
    if len(records) >= 1:
        achievements.append({
            "name": "First Quiz",
            "icon": "📝",
            "description": "Completed your first quiz!"
        })

    # Quiz Explorer
    if len(records) >= 5:
        achievements.append({
            "name": "Quiz Explorer",
            "icon": "📚",
            "description": "Completed 5 quiz attempts."
        })

    # Perfect Score
    if any(record["score"] == 100 for record in records):
        achievements.append({
            "name": "Perfect Score",
            "icon": "💯",
            "description": "Achieved a perfect score of 100."
        })

    # 3 Day Streak
    if streak >= 3:
        achievements.append({
            "name": "3 Day Streak",
            "icon": "🔥",
            "description": "Learned for 3 consecutive days."
        })

    # 7 Day Streak
    if streak >= 7:
        achievements.append({
            "name": "7 Day Streak",
            "icon": "🔥",
            "description": "Learned for 7 consecutive days."
        })

    # Topic Master
    if strong_topics:
        achievements.append({
            "name": "Topic Master",
            "icon": "🧠",
            "description": "Achieved a strong score in at least one topic."
        })

    return {
        "student_id": student_id,
        "overall_score": overall_score,
        "current_streak": streak,
        "total_achievements": len(achievements),
        "achievements": achievements
    }