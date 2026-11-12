
import pandas as pd

# Create sample CSV file
data = {
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Branch": ["Electrical", "Mechanical", "Civil", "Electrical", "Civil"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Read CSV file
students = pd.read_csv("students.csv")

print("STUDENT RECORDS FROM CSV")
print("------------------------")
print(students)

print("\nCSV file read successfully!")
