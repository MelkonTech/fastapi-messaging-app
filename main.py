from app.models.stats_message import Base
from app.messages import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configs.database import engine
from app.configs.config import settings


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, tags=["Messages"], prefix="/api")


@app.get("/healthchecker")
async def root() -> dict:
    return {"message": "Welcome to Messages stats"}
