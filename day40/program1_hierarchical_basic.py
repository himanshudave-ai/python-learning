
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Load Iris dataset
iris = load_iris()
X = iris.data

# Create Hierarchical Clustering model
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Perform clustering
clusters = model.fit_predict(X)

# Display results
print("HIERARCHICAL CLUSTERING RESULTS")
print("--------------------------------")

print("First 20 Cluster Labels:")
print(clusters[:20])

print("\nTotal Clusters:")
print(len(set(clusters)))

print("\nTotal Data Points:")
print(len(X))
