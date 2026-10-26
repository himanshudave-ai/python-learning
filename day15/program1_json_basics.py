import json

student = {
    "name": "Himanshu",
    "branch": "Electrical",
    "marks": 85
}

# Python dictionary to JSON string
json_data = json.dumps(student, indent=4)
print("JSON Data:")
print(json_data)

# JSON string to Python dictionary
python_data = json.loads(json_data)

print("Student Name:", python_data["name"])
print("Marks:", python_data["marks"])