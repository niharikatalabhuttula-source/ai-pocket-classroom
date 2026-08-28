from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.learning import router as learning_router
from app.routes.quiz import router as quiz_router
from app.routes.progress import router as progress_router
from app.database.database import create_tables
from app.routes.doubt import router as doubt_router
from app.routes.daily_goal import router as daily_goal_router
from app.routes.achievements import router as achievements_router


app = FastAPI(
    title="AI Pocket Classroom",
    description="Personalized AI learning platform",
    version="1.0.0"
)

create_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(learning_router)
app.include_router(quiz_router)
app.include_router(progress_router)
app.include_router(doubt_router)
app.include_router(daily_goal_router)
app.include_router(achievements_router)


@app.get("/")
def root():
    return {
        "message": "AI Pocket Classroom Backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }