import matplotlib.pyplot as plt

students = ["Himanshu", "Rahul", "Amit", "Priya", "Neha"]
marks = [95, 90, 78, 88, 82]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("STUDENT PERFORMANCE ANALYSIS")
print("----------------------------")
print("Total Students:", len(students))
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

plt.bar(students, marks)

plt.axhline(
    y=average,
    linestyle="--",
    label="Average Marks"
)

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(axis="y")

plt.show()