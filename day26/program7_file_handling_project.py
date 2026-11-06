def add_student():
    name = input("Enter student name: ")
    branch = input("Enter branch: ")

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}, Branch: {branch}\n")

    print("Student record added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()

            if data:
                print("\nSTUDENT RECORDS")
                print("----------------")
                print(data)
            else:
                print("No student records found.")

    except FileNotFoundError:
        print("No records found. Add a student first.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting Student Record Manager.")
        break

    else:
        print("Invalid choice! Try again.")