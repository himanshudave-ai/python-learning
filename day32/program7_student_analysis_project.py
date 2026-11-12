
import pandas as pd

# Student dataset
data = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Branch": ["Electrical", "Mechanical", "Civil", "Electrical", "Civil"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

# Overall analysis
total_students = len(df)
average_marks = df["Marks"].mean()

# Find topper
topper = df.loc[df["Marks"].idxmax()]

# Branch-wise average
branch_average = df.groupby("Branch")["Marks"].mean()

# Display report
print("STUDENT PERFORMANCE REPORT")
print("===========================")

print("Total Students:", total_students)
print("Average Marks:", round(average_marks, 2))

print("\nTOPPER DETAILS")
print("--------------")
print("Name:", topper["Name"])
print("Branch:", topper["Branch"])
print("Marks:", topper["Marks"])

print("\nBRANCH-WISE AVERAGE")
print("-------------------")
print(branch_average)

# Save report to CSV
df.to_csv("student_analysis_report.csv", index=False)

print("\nReport saved successfully!")
