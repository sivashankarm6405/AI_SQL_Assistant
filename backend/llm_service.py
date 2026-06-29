from openai import OpenAI

from backend.config import MODEL_NAME, OPENAI_API_KEY
from prompts.sql_prompt import build_explanation_prompt, build_sql_prompt

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


def _mock_sql(question: str) -> str:
    q = question.lower()

    if "top 5 customers" in q and "revenue" in q:
        return """
SELECT c.name, SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY revenue DESC
LIMIT 5;
""".strip()

    if "all customers" in q or "show customers" in q:
        return "SELECT id, name, city FROM customers;"

    if "orders" in q and "highest" in q:
        return "SELECT id, customer_id, product_name, total_amount FROM orders ORDER BY total_amount DESC;"

    return "SELECT id, name, city FROM customers LIMIT 5;"


def generate_sql_from_question(question: str) -> str:
    if not client:
        return _mock_sql(question)

    prompt = build_sql_prompt(question)
    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
    )

    sql = response.output_text.strip()
    return sql.replace("```sql", "").replace("```", "").strip()


def explain_sql(sql: str) -> str:
    if not client:
        return "This query reads data from the sample tables and returns rows matching the user's request."

    prompt = build_explanation_prompt(sql)
    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
    )
    return response.output_text.strip()