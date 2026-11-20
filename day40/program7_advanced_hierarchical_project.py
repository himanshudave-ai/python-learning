
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram

# Create customer dataset
data = {
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

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Create model
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Perform clustering
clusters = model.fit_predict(X_scaled)

df["Cluster"] = clusters

# Calculate silhouette score
score = silhouette_score(
    X_scaled,
    clusters
)

# Display results
print("ADVANCED HIERARCHICAL CLUSTERING")
print("--------------------------------")

print("\nCustomer Data:")
print(df)

print("\nTotal Clusters:", len(set(clusters)))

print("Silhouette Score:", round(score, 4))

print("\nCluster Summary:")
print(df.groupby("Cluster").mean().round(2))

# Generate dendrogram
linked = linkage(X_scaled, method="ward")

plt.figure(figsize=(10, 5))

dendrogram(linked)

plt.title("Customer Hierarchical Dendrogram")
plt.xlabel("Customer Index")
plt.ylabel("Distance")

plt.show()

# Visualize clusters
plt.figure(figsize=(8, 5))

for cluster_id in sorted(set(clusters)):

    cluster_data = df[df["Cluster"] == cluster_id]

    plt.scatter(
        cluster_data["Income"],
        cluster_data["Spending"],
        label=f"Cluster {cluster_id}"
    )

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.grid(True)

plt.show()
