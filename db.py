import sqlite3

DB_PATH = "results.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    # enforce foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    # create students table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        class TEXT
    );
    """)

    # create marks table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        marks INTEGER NOT NULL CHECK(marks >= 0 AND marks <= 100),
        FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()
    print(f"Database '{DB_PATH}' created/checked and tables are ready.")

if __name__ == "__main__":
    create_tables()
