
import pandas as pd

data = {
    "Name": ["Amit", "Ravi", "Priya", "Neha", "Rahul"],
    "Maths": [85, 72, 95, 88, 65],
    "Science": [78, 80, 92, 85, 70],
    "English": [82, 75, 89, 90, 68]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Science", "English"]

# Calculate total and percentage
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / len(subjects)

# Sort students by total marks
df = df.sort_values(by="Total", ascending=False)

print("STUDENT TOPPER ANALYSIS")

print("\nStudent Ranking:")
print(df[["Name", "Total", "Percentage"]].to_string(index=False))

# Overall topper
topper = df.iloc[0]

print("\nOVERALL TOPPER")
print("Name:", topper["Name"])
print("Total Marks:", topper["Total"])
print("Percentage:", round(topper["Percentage"], 2))

# Subject-wise toppers
print("\nSUBJECT-WISE TOPPERS")

for subject in subjects:
    index = df[subject].idxmax()
    print(subject, ":", df.loc[index, "Name"],
          "-", df.loc[index, subject])
