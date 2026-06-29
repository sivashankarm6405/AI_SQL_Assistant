TEST_CASES = [
    {
        "question": "Show all customers",
        "expected_contains": ["SELECT", "FROM customers"],
    },
    {
        "question": "Show top 5 customers by revenue",
        "expected_contains": ["SUM", "GROUP BY", "ORDER BY", "LIMIT 5"],
    },
    {
        "question": "List orders sorted by highest total amount",
        "expected_contains": ["FROM orders", "ORDER BY", "total_amount"],
    },
]  