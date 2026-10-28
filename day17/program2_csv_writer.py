import csv

students = [
    ["Aman", 85],
    ["Riya", 92],
    ["Rahul", 78]
]

with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerows(students)

print("Student records saved successfully!")