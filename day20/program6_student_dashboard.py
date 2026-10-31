
import pandas as pd
import matplotlib.pyplot as plt

# Student dataset
data = {
    "Name": ["Amit", "Ravi", "Priya", "Neha", "Rahul"],
    "Maths": [85, 72, 95, 88, 65],
    "Science": [78, 80, 92, 85, 70],
    "English": [82, 75, 89, 90, 68]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Science", "English"]

# Calculate results
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / 3

# Assign grades
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# Display dashboard
print("=" * 45)
print("       STUDENT PERFORMANCE DASHBOARD")
print("=" * 45)

print("\nComplete Student Results:")
print(df.to_string(index=False))

# Class statistics
print("\nClass Average:", round(df["Percentage"].mean(), 2))
print("Highest Percentage:", round(df["Percentage"].max(), 2))
print("Lowest Percentage:", round(df["Percentage"].min(), 2))

# Overall topper
topper = df.loc[df["Total"].idxmax()]

print("\nCLASS TOPPER:", topper["Name"])
print("Topper Percentage:", round(topper["Percentage"], 2))

# Subject averages
print("\nSubject-wise Average:")
print(df[subjects].mean())

# Dashboard visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Student percentage chart
axes[0].bar(df["Name"], df["Percentage"])
axes[0].set_title("Student Performance")
axes[0].set_xlabel("Students")
axes[0].set_ylabel("Percentage")

# Subject average chart
subject_avg = df[subjects].mean()

axes[1].bar(subject_avg.index, subject_avg.values)
axes[1].set_title("Subject-wise Average")
axes[1].set_xlabel("Subjects")
axes[1].set_ylabel("Average Marks")

plt.tight_layout()
plt.show()
