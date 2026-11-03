import sqlite3

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

connection.commit()

while True:

    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        cursor.execute("""
        INSERT INTO employees
        VALUES (?, ?, ?, ?)
        """, (emp_id, name, department, salary))

        connection.commit()

        print("Employee added successfully!")

    elif choice == "2":

        cursor.execute("SELECT * FROM employees")

        records = cursor.fetchall()

        for employee in records:
            print(employee)

    elif choice == "3":

        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter New Salary: "))

        cursor.execute("""
        UPDATE employees
        SET salary = ?
        WHERE id = ?
        """, (salary, emp_id))

        connection.commit()

        if cursor.rowcount > 0:
            print("Salary updated successfully!")
        else:
            print("Employee not found.")

    elif choice == "4":

        emp_id = int(input("Enter Employee ID: "))

        cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
        """, (emp_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    elif choice == "5":

        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice!")

connection.close()