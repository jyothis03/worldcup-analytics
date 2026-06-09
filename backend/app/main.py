from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.predict import router as predict_router

app = FastAPI(
    title="World Cup AI Tactical Predictor",
    description="AI-powered tactical predictions for World Cup matches",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router)


@app.get("/")
async def root():
    return {"status": "online", "message": "World Cup Predictor API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
