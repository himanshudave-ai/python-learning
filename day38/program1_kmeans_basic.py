
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()
X = iris.data

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Perform clustering
clusters = model.fit_predict(X)

# Display results
print("K-MEANS CLUSTERING RESULTS")
print("--------------------------")

print("First 20 Cluster Labels:")
print(clusters[:20])

print("\nCluster Centers:")
print(model.cluster_centers_)

print("\nInertia:")
print(round(model.inertia_, 2))

print("\nTotal Clusters:", len(set(clusters)))
