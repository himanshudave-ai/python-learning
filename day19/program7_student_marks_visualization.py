import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Rahul", "Neha", "Karan"]
marks = [85, 92, 78, 88, 95]

average = sum(marks) / len(marks)
highest = max(marks)

plt.bar(students, marks, label="Student Marks")

plt.axhline(
    y=average,
    linestyle="--",
    label=f"Average: {average:.2f}"
)

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid(axis="y")

plt.show()

print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Topper:", students[marks.index(highest)])