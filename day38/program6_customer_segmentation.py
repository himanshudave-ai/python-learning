
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer dataset
data = {
    "Income": [15, 16, 17, 18, 20, 25,
               30, 35, 40, 45, 50, 55],

    "Spending": [39, 81, 6, 77, 40, 76,
                 10, 75, 35, 80, 20, 70]
}

df = pd.DataFrame(data)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Apply K-Means
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

# Analyze clusters
print("CUSTOMER SEGMENTATION ANALYSIS")
print("------------------------------")

print("\nCustomer Data:")
print(df)

print("\nCluster Summary:")
summary = df.groupby("Cluster").mean().round(2)

print(summary)

print("\nCustomer Count:")
print(df["Cluster"].value_counts().sort_index())
