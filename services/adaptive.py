def get_adaptive_difficulty(score):

    if score is None:
        return "medium"

    if score < 40:
        return "easy"

    elif score < 70:
        return "medium"

    else:
        return "hard"


def get_difficulty_reason(score: float) -> str:

    if score is None:
        return (
            "You have not attempted this topic yet, "
            "so we are starting with medium-level questions."
        )

    if score < 40:
        return (
            "Your previous score was low, so we are starting "
            "with easier questions to strengthen your basics."
        )

    elif score < 70:
        return (
            "Your performance is improving, so we are keeping "
            "the difficulty at a medium level."
        )

    else:
        return (
            "You performed well, so we are increasing the "
            "difficulty to challenge you further."
        )