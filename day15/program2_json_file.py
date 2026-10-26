import json

student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "Computer Science",
    "marks": 90
}

# Save data to JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data saved successfully.")

# Read data from JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("Student Name:", data["name"])
print("Roll Number:", data["roll_no"])
print("Marks:", data["marks"])