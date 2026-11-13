import matplotlib.pyplot as plt

subjects = ["Python", "Electrical", "Maths", "Physics"]
study_hours = [4, 3, 2, 1]

plt.pie(
    study_hours,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Daily Study Time Distribution")

plt.show()