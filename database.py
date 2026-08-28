import sqlite3


DATABASE = "progress.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            topic TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS learning_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            activity_date TEXT NOT NULL,
            UNIQUE(student_id, activity_date)
        )
    """)

    conn.commit()
    conn.close()


def save_progress(student_id: str, topic: str, score: int):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO progress (student_id, topic, score)
        VALUES (?, ?, ?)
        """,
        (student_id, topic, score)
    )

    conn.commit()
    conn.close()


def get_student_progress(student_id: str):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT topic, score
        FROM progress
        WHERE student_id = ?
        """,
        (student_id,)
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]