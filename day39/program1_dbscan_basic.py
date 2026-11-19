from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import numpy as np

# Generate sample data
X, y = make_blobs(
    n_samples=100,
    centers=3,
    cluster_std=0.60,
    random_state=42
)

# Create DBSCAN model
model = DBSCAN(
    eps=0.8,
    min_samples=5
)

# Perform clustering
clusters = model.fit_predict(X)

# Display results
print("DBSCAN CLUSTERING RESULTS")
print("-------------------------")

print("First 20 Cluster Labels:")
print(clusters[:20])

print("\nTotal Clusters:",
      len(set(clusters)) - (1 if -1 in clusters else 0))

print("Noise Points:",
      np.sum(clusters == -1))

print("Total Data Points:", len(X))