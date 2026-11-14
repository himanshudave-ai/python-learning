import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Student dataset
data = {
    "Name": [
        "Himanshu", "Rahul", "Amit", "Priya", "Neha",
        "Rohit", "Karan", "Pooja", "Ankit", "Sneha"
    ],
    "Branch": [
        "Electrical", "Mechanical", "Civil", "Electrical", "Civil",
        "Mechanical", "Electrical", "Civil", "Mechanical", "Electrical"
    ],
    "Study Hours": [7, 5, 3, 6, 4, 5, 8, 3, 6, 7],
    "Attendance": [95, 85, 70, 90, 75, 80, 98, 68, 88, 92],
    "Marks": [95, 80, 60, 88, 65, 78, 98, 55, 85, 92]
}

df = pd.DataFrame(data)

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 1. Study Hours vs Marks
sns.scatterplot(
    data=df,
    x="Study Hours",
    y="Marks",
    hue="Branch",
    s=100,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Study Hours vs Marks")

# 2. Average Marks by Branch
sns.barplot(
    data=df,
    x="Branch",
    y="Marks",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Average Marks by Branch")

# 3. Student Count by Branch
sns.countplot(
    data=df,
    x="Branch",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Students by Branch")

# 4. Correlation Heatmap
correlation = df[
    ["Study Hours", "Attendance", "Marks"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Performance Correlation")

plt.tight_layout()
plt.show()

# Display summary
print("STUDENT PERFORMANCE SUMMARY")
print("----------------------------")
print("Total Students:", len(df))
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())