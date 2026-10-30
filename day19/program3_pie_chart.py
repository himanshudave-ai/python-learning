import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "Electrical", "English"]
hours = [4, 3, 2, 1]

plt.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Daily Study Time Distribution")

plt.show()