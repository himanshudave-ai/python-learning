class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Manager(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name, basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus


class Developer(Employee):
    def __init__(self, name, basic_salary, overtime):
        super().__init__(name, basic_salary)
        self.overtime = overtime

    def calculate_salary(self):
        return self.basic_salary + self.overtime


employees = [
    Employee("Amit", 30000),
    Manager("Neha", 50000, 10000),
    Developer("Raj", 40000, 5000)
]

for employee in employees:
    print(employee.name, "Salary:", employee.calculate_salary())