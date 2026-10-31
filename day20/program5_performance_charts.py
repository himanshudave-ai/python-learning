
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Ravi", "Priya", "Neha", "Rahul"],
    "Maths": [85, 72, 95, 88, 65],
    "Science": [78, 80, 92, 85, 70],
    "English": [82, 75, 89, 90, 68]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Science", "English"]

# Calculate total marks
df["Total"] = df[subjects].sum(axis=1)

# Chart 1: Student Total Marks
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Total"])
plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()

# Chart 2: Subject Average
subject_average = df[subjects].mean()

plt.figure(figsize=(8, 5))
plt.bar(subject_average.index, subject_average.values)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# Chart 3: Student Percentage
df["Percentage"] = df["Total"] / 3

plt.figure(figsize=(8, 5))
plt.pie(
    df["Total"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
plt.title("Student Marks Distribution")
plt.show()
