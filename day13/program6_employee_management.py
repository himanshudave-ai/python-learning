class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-" * 25)


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter employee ID: ")

        if any(emp.emp_id == emp_id for emp in self.employees):
            print("Employee ID already exists.")
            return

        name = input("Enter employee name: ")
        department = input("Enter department: ")

        try:
            salary = float(input("Enter salary: "))
            if salary < 0:
                print("Salary cannot be negative.")
                return
        except ValueError:
            print("Please enter a valid salary.")
            return

        employee = Employee(emp_id, name, department, salary)
        self.employees.append(employee)
        print("Employee added successfully.")

    def show_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for emp in self.employees:
            emp.display()

    def search_employee(self):
        emp_id = input("Enter employee ID to search: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.display()
                return

        print("Employee not found.")


system = EmployeeManagement()

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_employee()
    elif choice == "2":
        system.show_employees()
    elif choice == "3":
        system.search_employee()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")