
import pandas as pd

data = {
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

print("STUDENT MARKS ANALYSIS")
print("----------------------")

print("Total Students:", len(df))
print("Total Marks:", df["Marks"].sum())
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
