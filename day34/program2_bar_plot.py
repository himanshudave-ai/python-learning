import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

sns.barplot(data=df, x="Student", y="Marks")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.show()