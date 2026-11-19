from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Generate data
X, y = make_blobs(
    n_samples=150,
    centers=3,
    cluster_std=0.60,
    random_state=42
)

# Apply DBSCAN
model = DBSCAN(eps=0.8, min_samples=5)
clusters = model.fit_predict(X)

# Plot clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=clusters,
    cmap="viridis",
    s=50
)

plt.title("DBSCAN Cluster Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.colorbar(label="Cluster Label")
plt.grid(True)

plt.show()