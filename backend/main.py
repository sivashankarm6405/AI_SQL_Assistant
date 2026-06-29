from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.config import ALLOWED_ORIGINS
from backend.llm_service import explain_sql, generate_sql_from_question
from backend.query_service import run_query
from validators.sql_validator import validate_sql

app = FastAPI(title="AI SQL Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS if ALLOWED_ORIGINS != ['*'] else ['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "AI SQL Assistant API is running"}


@app.post("/generate-sql")
def generate_sql(request: QueryRequest):
    sql = generate_sql_from_question(request.question)

    is_valid, message = validate_sql(sql)
    if not is_valid:
        return {"error": f"Unsafe or invalid SQL: {message}", "sql": sql}

    rows = run_query(sql)
    explanation = explain_sql(sql)

    return {
        "question": request.question,
        "sql": sql,
        "explanation": explanation,
        "rows": rows,
    }