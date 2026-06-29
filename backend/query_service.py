from database.db import get_connection


def run_query(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)

    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    rows = cursor.fetchall()

    conn.close()
    return [dict(zip(columns, row)) for row in rows]  