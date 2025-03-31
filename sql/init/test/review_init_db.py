import psycopg2
from tabulate import tabulate

def fetch_all(cursor, query, description):
    print(f"\n--- {description} ---")
    cursor.execute(query)
    rows = cursor.fetchall()
    print(tabulate(rows, headers=[desc[0] for desc in cursor.description], tablefmt="psql"))

def main():
    try:
        conn = psycopg2.connect(
            dbname="quantpositions",
            user="postgres",
            password="0000",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        fetch_all(cursor, "SELECT * FROM users;", "Users Table")
        fetch_all(cursor, "SELECT * FROM companies;", "Companies Table")
        fetch_all(cursor, "SELECT * FROM positions;", "Positions Table")
        fetch_all(cursor, "SELECT * FROM applied;", "Applied Table")

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
