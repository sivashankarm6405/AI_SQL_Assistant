SCHEMA_DESCRIPTION = """
Database schema:

Table: customers
- id
- name
- city

Table: orders
- id
- customer_id
- product_name
- quantity
- total_amount
- order_date

Relationship:
- orders.customer_id references customers.id
"""


def build_sql_prompt(question: str) -> str:
    return f"""
You are a SQL assistant.
Convert the user question into a valid SQLite SQL query.

Rules:
- Only generate a single SELECT query.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, or PRAGMA.
- Use only the tables and columns from the schema below.
- Return only SQL.

{SCHEMA_DESCRIPTION}

User question:
{question}
""".strip()


def build_explanation_prompt(sql: str) -> str:
    return f"""
Explain this SQL query in simple beginner-friendly English.
Keep it short and clear.

SQL:
{sql}
""".strip() 