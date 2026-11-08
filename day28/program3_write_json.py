import json

employee = {
    "name": "Amit",
    "employee_id": 101,
    "department": "Electrical",
    "salary": 45000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("JSON file created successfully!")