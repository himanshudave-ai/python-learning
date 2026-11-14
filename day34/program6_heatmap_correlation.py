import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study Hours": [1, 2, 3, 4, 5, 6, 7],
    "Attendance": [60, 65, 70, 75, 80, 85, 90],
    "Marks": [45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

correlation = df.corr()

print("CORRELATION MATRIX")
print(correlation)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Student Performance Correlation")
plt.show()