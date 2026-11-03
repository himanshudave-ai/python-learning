import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

while True:

    print("\nSTUDENT DATABASE MANAGEMENT")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        marks = int(input("Enter Marks: "))

        cursor.execute("""
        INSERT INTO students
        (id, name, branch, marks)
        VALUES (?, ?, ?, ?)
        """, (student_id, name, branch, marks))

        connection.commit()

        print("Student added successfully!")

    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        for student in records:
            print(student)

    elif choice == "3":

        student_id = int(input("Enter Student ID: "))
        marks = int(input("Enter New Marks: "))

        cursor.execute("""
        UPDATE students
        SET marks = ?
        WHERE id = ?
        """, (marks, student_id))

        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "4":

        student_id = int(input("Enter Student ID: "))

        cursor.execute("""
        DELETE FROM students
        WHERE id = ?
        """, (student_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":

        print("Exiting Student Database...")
        break

    else:
        print("Invalid choice!")

connection.close()