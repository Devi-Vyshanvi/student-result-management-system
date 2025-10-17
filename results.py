import sqlite3
from student import get_student_id

DB_PATH = "results.db"

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def generate_result(roll):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    student_id = get_student_id(roll)
    if not student_id:
        print("No student found with that roll number.")
        conn.close()
        return

    # get student info
    cur.execute("SELECT name, class FROM students WHERE student_id = ?;", (student_id,))
    student = cur.fetchone()

    # get marks
    cur.execute("SELECT subject, marks FROM marks WHERE student_id = ?;", (student_id,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No marks found for this student.")
        return

    total = sum(m for _, m in rows)
    avg = total / len(rows)
    grade = calculate_grade(avg)

    print("\n===== Student Result =====")
    print(f"Name: {student[0]}")
    print(f"Class: {student[1]}")
    print(f"Roll No: {roll}")
    print("\nSubjects and Marks:")
    for subject, marks in rows:
        print(f"  {subject}: {marks}")
    print("----------------------------")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print("============================\n")

if __name__ == "__main__":
    roll = input("Enter roll number: ")
    generate_result(roll)
