import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.llm_service import generate_sql_from_question
from tests.test_cases import TEST_CASES


def main():
    passed = 0

    for idx, test in enumerate(TEST_CASES, start=1):
        sql = generate_sql_from_question(test["question"])
        ok = all(token.lower() in sql.lower() for token in test["expected_contains"])

        status = "PASS" if ok else "FAIL"
        print(f"{idx}. {status} - {test['question']}")
        print(sql)
        print("-" * 50)

        if ok:
            passed += 1

    print(f"Passed {passed}/{len(TEST_CASES)} tests")


if __name__ == "__main__":
    main() 