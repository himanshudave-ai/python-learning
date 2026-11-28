
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create Hierarchical Clustering model
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Perform clustering
labels = model.fit_predict(X_scaled)

# Calculate silhouette score
score = silhouette_score(X_scaled, labels)

# Display results
print("HIERARCHICAL CLUSTERING")
print("-----------------------")

print("Total Samples:", len(X_scaled))
print("Number of Clusters:", model.n_clusters)
print("Silhouette Score:", round(score, 4))

print("\nCluster Distribution:")

for cluster in range(3):
    count = sum(labels == cluster)
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

plt.title("Hierarchical Clustering - Iris Dataset")
plt.xlabel("Standardized Sepal Length")
plt.ylabel("Standardized Sepal Width")
plt.grid(True)

plt.show()
