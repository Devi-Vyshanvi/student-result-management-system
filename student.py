import sqlite3

DB_PATH = "results.db"

def add_student(roll, name, student_class):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO students (roll, name, class) VALUES (?, ?, ?);", 
                    (roll, name, student_class))
        conn.commit()
        print(f"Student '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print("Roll number already exists. Try another one.")
    finally:
        conn.close()

def get_student_id(roll):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT student_id FROM students WHERE roll = ?;", (roll,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

if __name__ == "__main__":
    print("1. Add Student")
    print("2. Get Student ID by Roll")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        student_class = input("Enter class: ")
        add_student(roll, name, student_class)
    elif choice == "2":
        roll = input("Enter roll number: ")
        student_id = get_student_id(roll)
        if student_id:
            print(f"Student ID for roll {roll} is {student_id}")
        else:
            print("No student found with that roll number.")
