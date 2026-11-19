import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Create customer dataset
data = {
    "Income": [
        15, 18, 20, 22, 25,
        45, 48, 50, 52, 55,
        75, 78, 80, 82, 85
    ],

    "Spending": [
        20, 22, 18, 25, 21,
        45, 48, 50, 52, 47,
        75, 78, 80, 82, 77
    ]
}

df = pd.DataFrame(data)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Apply DBSCAN
model = DBSCAN(
    eps=0.6,
    min_samples=3
)

df["Cluster"] = model.fit_predict(X_scaled)

# Display results
print("CUSTOMER SEGMENTATION RESULTS")
print("------------------------------")

print(df)

print("\nCluster Summary:")
print(df.groupby("Cluster")[["Income", "Spending"]].mean().round(2))

print("\nCustomer Count:")
print(df["Cluster"].value_counts().sort_index())