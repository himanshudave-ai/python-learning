import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Marks": [
        45, 50, 55, 60, 62, 65, 68, 70,
        72, 75, 78, 80, 82, 85, 88, 90, 95
    ]
}

df = pd.DataFrame(data)

sns.histplot(
    data=df,
    x="Marks",
    bins=6,
    kde=True
)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()