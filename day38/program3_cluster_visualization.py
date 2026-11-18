
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()
X = iris.data

# Use first two features
X_2d = X[:, :2]

# Create model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(X_2d)

# Plot clusters
plt.scatter(
    X_2d[:, 0],
    X_2d[:, 1],
    c=clusters,
    cmap="viridis"
)

# Plot cluster centers
centers = model.cluster_centers_

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200,
    color="red",
    label="Centroids"
)

plt.title("K-Means Cluster Visualization")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()

print("Cluster Visualization Completed!")
print("Number of Clusters:", len(set(clusters)))
