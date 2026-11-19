import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Generate dataset
X, y = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=0.70,
    random_state=42
)

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
model = DBSCAN(
    eps=0.3,
    min_samples=5
)

clusters = model.fit_predict(X_scaled)

# Calculate results
unique_clusters = set(clusters)

total_clusters = len(unique_clusters) - (
    1 if -1 in clusters else 0
)

noise_points = np.sum(clusters == -1)

print("ADVANCED DBSCAN PROJECT")
print("-----------------------")

print("Total Data Points:", len(X))
print("Total Clusters:", total_clusters)
print("Noise Points:", noise_points)

# Calculate silhouette score only when valid
valid_mask = clusters != -1
valid_labels = clusters[valid_mask]

if len(set(valid_labels)) > 1:
    score = silhouette_score(
        X_scaled[valid_mask],
        valid_labels
    )

    print("Silhouette Score:", round(score, 4))
else:
    print("Silhouette Score: Not available")

# Visualize clusters
plt.figure(figsize=(9, 6))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters,
    cmap="viridis",
    s=45
)

plt.title("Advanced DBSCAN Clustering Project")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.grid(True)

plt.show()