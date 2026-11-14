import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Branch": [
        "Electrical", "Mechanical", "Civil",
        "Electrical", "Civil", "Mechanical",
        "Electrical", "Civil"
    ]
}

df = pd.DataFrame(data)

sns.countplot(data=df, x="Branch")

plt.title("Number of Students in Each Branch")
plt.xlabel("Engineering Branch")
plt.ylabel("Number of Students")
plt.show()