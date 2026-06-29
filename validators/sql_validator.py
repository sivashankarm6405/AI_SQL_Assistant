import sqlglot
from sqlglot import exp

FORBIDDEN = {"INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE", "CREATE", "PRAGMA"}


def validate_sql(sql: str):
    try:
        statements = sqlglot.parse(sql, read="sqlite")
    except Exception as e:
        return False, f"Parse error: {e}"

    if len(statements) != 1:
        return False, "Only one SQL statement is allowed."

    parsed = statements[0]
    if not isinstance(parsed, exp.Select):
        return False, "Only SELECT queries are allowed."

    upper_sql = sql.upper()
    for keyword in FORBIDDEN:
        if keyword in upper_sql:
            return False, f"{keyword} is not allowed."

    return True, "Valid SQL"