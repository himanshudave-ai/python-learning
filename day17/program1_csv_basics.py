import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Branch", "Marks"])
    writer.writerow(["Aman", "Electrical", 85])
    writer.writerow(["Riya", "CSE", 92])
    writer.writerow(["Rahul", "Civil", 78])

print("CSV file created successfully!")