import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Rahul", "Neha"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()