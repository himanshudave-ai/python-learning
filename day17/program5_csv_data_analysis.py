import csv

marks = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append(int(row["Marks"]))

if marks:
    print("Total Marks:", sum(marks))
    print("Average Marks:", sum(marks) / len(marks))
    print("Highest Marks:", max(marks))