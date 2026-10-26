import json
from pathlib import Path

FILE_NAME = Path(__file__).with_name("students.json")


def load_students():
    if not FILE_NAME.exists():
        return []

    try:
        with FILE_NAME.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Invalid student data format.")
        return []

    except (json.JSONDecodeError, OSError) as error:
        print("Could not read student data:", error)
        return []


def save_students(students):
    try:
        with FILE_NAME.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True

    except OSError as error:
        print("Could not save student data:", error)
        return False


def add_student():
    students = load_students()
    roll_no = input("Enter roll number: ").strip()

    if any(student["roll_no"] == roll_no for student in students):
        print("Roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip()

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch
    }

    students.append(student)

    if save_students(students):
        print("Student added successfully.")


def show_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for student in load_students():
        if student["roll_no"] == roll_no:
            print("Student found:", student)
            return

    print("Student not found.")


while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program closed.")
        break
    else:
        print("Invalid choice.")