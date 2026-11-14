import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create student data
data = {
    "Study Hours": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Create scatter plot
sns.scatterplot(
    data=df,
    x="Study Hours",
    y="Marks",
    s=100
)

plt.title("Study Hours vs Student Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.show()