
import pandas as pd

# Student dataset
data = {
    "Name": ["Amit", "Ravi", "Priya", "Neha", "Rahul"],
    "Maths": [85, 72, 95, 88, 65],
    "Science": [78, 80, 92, 85, 70],
    "English": [82, 75, 89, 90, 68]
}

df = pd.DataFrame(data)

# Calculate total and percentage
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Percentage"] = df["Total"] / 3

# Overall statistics
print("STUDENT PERFORMANCE STATISTICS")

print("\nAverage Marks:")
print(df[["Maths", "Science", "English"]].mean())

print("\nHighest Marks:")
print(df[["Maths", "Science", "English"]].max())

print("\nLowest Marks:")
print(df[["Maths", "Science", "English"]].min())

print("\nClass Average Percentage:")
print(round(df["Percentage"].mean(), 2))

print("\nHighest Total Marks:")
print(df["Total"].max())

print("\nLowest Total Marks:")
print(df["Total"].min())

print("\nComplete Student Statistics:")
print(df)
