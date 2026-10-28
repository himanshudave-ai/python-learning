import csv

updated_rows = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"] == "Aman":
            row["Marks"] = "90"

        updated_rows.append(row)

with open("updated_students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Branch", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(updated_rows)

print("Updated records saved successfully!")