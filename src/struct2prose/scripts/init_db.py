from struct2prose.persistence.db import connect, init_db

def main():
    with connect("struct2prose.db") as conn:
        init_db(conn)
        print("Database initialized.")

if __name__ == "__main__":
    main()