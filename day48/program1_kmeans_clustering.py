
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load Iris dataset
iris = load_iris()
X = iris.data

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train model
model.fit(X)

# Get cluster labels
labels = model.labels_

# Display results
print("K-MEANS CLUSTERING")
print("------------------")

print("Total Samples:", len(X))
print("Number of Clusters:", model.n_clusters)

print("\nFirst 10 Cluster Labels:")

for i in range(10):
    print("Sample", i + 1, ":", labels[i])

print("\nCluster Centers:")
print(model.cluster_centers_)

print("\nCluster Distribution:")

for cluster in range(3):
    count = sum(labels == cluster)
    print("Cluster", cluster, ":", count, "samples")
