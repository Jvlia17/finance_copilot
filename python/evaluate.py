import json
import time
import psycopg2

from sql_agent import generate_sql


# ==========================
# Database connection
# ==========================

DB_CONFIG = {
    "host": "localhost",
    "database": "finance_copilot",
    "user": "postgres",
    "password": "YOUR_PASSWORD",
    "port": 5432
}


# ==========================
# Load evaluation dataset
# ==========================

with open("../data/evaluation_dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)


# ==========================
# Execute SQL
# ==========================

def execute_sql(query):
    connection = None

    try:
        connection = psycopg2.connect(**DB_CONFIG)

        cursor = connection.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()

        return result, None

    except Exception as e:
        return None, str(e)

    finally:
        if connection:
            connection.close()



# ==========================
# Normalize results
# ==========================

def normalize_result(result):

    if result is None:
        return []

    normalized = []

    for row in result:
        cleaned_row = []

        for value in row:

            if isinstance(value, float):
                value = round(value, 5)

            if isinstance(value, str):
                value = value.strip()

            cleaned_row.append(value)

        normalized.append(tuple(cleaned_row))

    return sorted(normalized)



# ==========================
# Evaluation
# ==========================

passed = 0
failed = 0


results_summary = []


for item in dataset:

    print("\n" + "=" * 70)

    print(f"Test {item['id']}")
    print(f"Difficulty: {item['difficulty']}")
    print(f"Question:")
    print(item["question"])


    # Generate SQL
    try:

        start = time.time()

        generated_sql = generate_sql(
            item["question"]
        )

        generation_time = time.time() - start


    except Exception as e:

        print("\n❌ SQL generation failed")
        print(e)

        failed += 1

        continue



    print("\nGenerated SQL:")
    print(generated_sql)



    # Expected SQL execution

    expected_result, expected_error = execute_sql(
        item["expected_sql"]
    )


    # Generated SQL execution

    generated_result, generated_error = execute_sql(
        generated_sql
    )



    if generated_error:

        print("\n❌ Generated SQL failed")
        print(generated_error)

        failed += 1

        results_summary.append(
            {
                "id": item["id"],
                "status": "FAILED",
                "reason": "SQL error"
            }
        )

        continue



    expected_normalized = normalize_result(
        expected_result
    )

    generated_normalized = normalize_result(
        generated_result
    )



    if expected_normalized == generated_normalized:

        print("\n✅ PASS")

        passed += 1

        status = "PASS"


    else:

        print("\n❌ FAIL")

        print("\nExpected result:")
        print(expected_result[:10])

        print("\nGenerated result:")
        print(generated_result[:10])

        failed += 1

        status = "FAIL"



    print(
        f"\nGeneration time: {generation_time:.2f}s"
    )


    results_summary.append(
        {
            "id": item["id"],
            "status": status,
            "generation_time": round(generation_time, 3)
        }
    )



# ==========================
# Final report
# ==========================

print("\n\n")
print("=" * 70)

print("FINAL RESULTS")

print("=" * 70)

print(
    f"Passed: {passed}/{len(dataset)}"
)

print(
    f"Failed: {failed}/{len(dataset)}"
)


accuracy = passed / len(dataset) * 100

print(
    f"Accuracy: {accuracy:.2f}%"
)


# Save report

with open(
        "../results/evaluation_results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results_summary,
        file,
        indent=4
    )

print("\nReport saved as evaluation_results.json")