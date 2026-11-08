import json

with open("employee.json", "r") as file:
    employee = json.load(file)

employee["salary"] = 50000
employee["department"] = "Power Systems"

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("Employee data updated successfully!")
print("Updated Salary:", employee["salary"])
print("Updated Department:", employee["department"])