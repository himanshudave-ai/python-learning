import matplotlib.pyplot as plt

subjects = ["Python", "Electrical", "Maths", "Physics", "English"]
marks = [85, 90, 78, 88, 82]

plt.bar(subjects, marks)

plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()