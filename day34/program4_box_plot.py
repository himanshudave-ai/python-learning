import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Branch": [
        "Electrical", "Electrical", "Electrical",
        "Mechanical", "Mechanical", "Mechanical",
        "Civil", "Civil", "Civil"
    ],
    "Marks": [75, 85, 95, 60, 70, 80, 65, 75, 90]
}

df = pd.DataFrame(data)

sns.boxplot(data=df, x="Branch", y="Marks")

plt.title("Marks Distribution by Branch")
plt.xlabel("Engineering Branch")
plt.ylabel("Marks")
plt.show()