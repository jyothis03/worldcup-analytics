from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "World Cup AI Tactical Predictor"
    gemini_api_key: str
    groq_api_key: str
    tavily_api_key: str    

    class Config:
        env_file = ".env"

settings = Settings()
    