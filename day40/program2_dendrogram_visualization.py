
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
iris = load_iris()
X = iris.data

# Create linkage matrix
linked = linkage(X, method="ward")

# Plot dendrogram
plt.figure(figsize=(12, 6))

dendrogram(
    linked,
    truncate_mode="lastp",
    p=30
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points / Clusters")
plt.ylabel("Euclidean Distance")
plt.grid(axis="y")

plt.show()

print("DENDROGRAM RESULTS")
print("------------------")
print("Total Data Points:", len(X))
print("Linkage Method: Ward")
print("Dendrogram generated successfully!")
