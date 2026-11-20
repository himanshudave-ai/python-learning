
import pandas as pd

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# Create customer dataset
data = {
    "Customer": [
        "A", "B", "C", "D",
        "E", "F", "G", "H",
        "I", "J", "K", "L"
    ],

    "Income": [
        20, 22, 18, 25,
        45, 48, 50, 52,
        70, 75, 78, 80
    ],

    "Spending": [
        80, 75, 77, 76,
        40, 35, 42, 38,
        20, 25, 18, 22
    ]
}

df = pd.DataFrame(data)

# Select features
X = df[["Income", "Spending"]]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create clustering model
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Perform clustering
df["Cluster"] = model.fit_predict(X_scaled)

# Display results
print("CUSTOMER SEGMENTATION RESULTS")
print("-----------------------------")

print(df)

print("\nCUSTOMER CLUSTER SUMMARY")

summary = df.groupby("Cluster")[
    ["Income", "Spending"]
].mean().round(2)

print(summary)

print("\nCUSTOMER COUNT")
print(df["Cluster"].value_counts().sort_index())
