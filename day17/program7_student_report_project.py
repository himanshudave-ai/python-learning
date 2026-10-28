import csv

total = 0
count = 0
topper = ""
highest_marks = -1

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        marks = int(row["Marks"])

        total += marks
        count += 1

        if marks > highest_marks:
            highest_marks = marks
            topper = name

if count > 0:
    print("Total Students:", count)
    print("Total Marks:", total)
    print("Average Marks:", round(total / count, 2))
    print("Topper:", topper)
    print("Highest Marks:", highest_marks)
else:
    print("No student records found.")