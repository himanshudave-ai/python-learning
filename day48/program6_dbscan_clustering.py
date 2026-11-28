
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import numpy as np

# Load Iris dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create DBSCAN model
model = DBSCAN(
    eps=0.8,
    min_samples=5
)

# Perform clustering
labels = model.fit_predict(X_scaled)

# Identify clusters and noise
unique_labels = set(labels)
n_clusters = len(unique_labels - {-1})
n_noise = list(labels).count(-1)

# Display results
print("DBSCAN CLUSTERING")
print("-----------------")

print("Total Samples:", len(X_scaled))
print("Number of Clusters:", n_clusters)
print("Noise Points:", n_noise)

print("\nCluster Distribution:")

for cluster in sorted(unique_labels):
    count = np.sum(labels == cluster)

    if cluster == -1:
        print("Noise:", count, "samples")
    else:
        print("Cluster", cluster, ":", count, "samples")

# Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels,
    cmap="viridis",
    s=50
)

plt.title("DBSCAN Clustering - Iris Dataset")
plt.xlabel("Standardized Sepal Length")
plt.ylabel("Standardized Sepal Width")
plt.grid(True)

plt.show()
