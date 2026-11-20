
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram

# Load dataset
iris = load_iris()
X = iris.data

# Calculate linkage matrix
linked = linkage(X, method="ward")

# Plot dendrogram
plt.figure(figsize=(10, 5))

dendrogram(
    linked,
    truncate_mode="lastp",
    p=25
)

plt.title("Dendrogram - Optimal Clusters")
plt.xlabel("Data Points / Clusters")
plt.ylabel("Distance")
plt.show()

# Calculate silhouette scores
print("OPTIMAL CLUSTER ANALYSIS")
print("------------------------")

for k in range(2, 7):

    model = AgglomerativeClustering(
        n_clusters=k,
        linkage="ward"
    )

    labels = model.fit_predict(X)

    score = silhouette_score(X, labels)

    print(
        f"Clusters: {k}, "
        f"Silhouette Score: {score:.4f}"
    )
