import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
DB_PATH = os.getenv("DB_PATH", "database/app.db")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")