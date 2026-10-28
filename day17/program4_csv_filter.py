import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Marks"]) >= 80:
            print(row["Name"], row["Marks"])