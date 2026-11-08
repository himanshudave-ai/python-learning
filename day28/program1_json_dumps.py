import json

student = {
    "name": "Himanshu",
    "branch": "Electrical Engineering",
    "college": "VIT VELLORE",
    "learning_day": 28
}

json_data = json.dumps(student, indent=4)

print(json_data)
print("Data converted into JSON successfully!")