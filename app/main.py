# main.py
import os
from dotenv import load_dotenv
from app.schema_loader import load_schema
from app.query_generator import generate_sql
from app.query_runner import run_query

def main():
    load_dotenv()
    conn_str = os.getenv("DB_CONN_STR") or input("Enter your DB connection string: ")
    schema = load_schema(conn_str)
    print("Loaded schema:", schema)
    while True:
        nl_query = input("\nAsk your question (or type 'exit'): ")
        if nl_query.lower() == 'exit':
            break
        # generate_sql only requires the natural language question. The previous
        # implementation passed the database schema as the first argument which
        # caused the question to be interpreted as the model name. This resulted
        # in invalid API calls. We now pass only the question.
        sql = generate_sql(nl_query)
        print("\nGenerated SQL:\n", sql)
        try:
            df = run_query(conn_str, sql)
            print("\nQuery Results:\n", df)
        except Exception as e:
            print("Error running query:", e)

if __name__ == "__main__":
    main()
