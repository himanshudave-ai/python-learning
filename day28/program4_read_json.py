import json

with open("employee.json", "r") as file:
    employee = json.load(file)

print("EMPLOYEE DETAILS")
print("----------------")
print("Name:", employee["name"])
print("Employee ID:", employee["employee_id"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])