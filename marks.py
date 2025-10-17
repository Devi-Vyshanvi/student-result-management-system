import sqlite3
from student import get_student_id

DB_PATH = "results.db"

def add_mark(roll, subject, marks):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # find the student_id using the roll
    student_id = get_student_id(roll)
    if not student_id:
        print("No student found with that roll number.")
        conn.close()
        return

    # insert mark
    try:
        cur.execute("INSERT INTO marks (student_id, subject, marks) VALUES (?, ?, ?);",
                    (student_id, subject, marks))
        conn.commit()
        print(f"Marks for {subject} added successfully for roll {roll}.")
    except Exception as e:
        print("Error adding marks:", e)
    finally:
        conn.close()

def view_marks(roll):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    student_id = get_student_id(roll)
    if not student_id:
        print("No student found with that roll number.")
        conn.close()
        return

    cur.execute("SELECT subject, marks FROM marks WHERE student_id = ?;", (student_id,))
    rows = cur.fetchall()
    conn.close()

    if rows:
        print(f"\nMarks for roll {roll}:")
        for subject, marks in rows:
            print(f"  {subject}: {marks}")
    else:
        print("No marks found for this student.")

if __name__ == "__main__":
    print("1. Add Marks")
    print("2. View Marks")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        subject = input("Enter subject name: ")
        marks = int(input("Enter marks (0–100): "))
        add_mark(roll, subject, marks)
    elif choice == "2":
        roll = input("Enter roll number: ")
        view_marks(roll)
