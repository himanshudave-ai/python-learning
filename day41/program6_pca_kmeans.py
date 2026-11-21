
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reduce dimensions using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply K-Means
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(X_pca)

# Display results
print("PCA WITH K-MEANS RESULTS")
print("-----------------------")

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)

print("\nFirst 20 Cluster Labels:")
print(clusters[:20])

print("\nTotal Clusters:", len(set(clusters)))

print("Silhouette Score:",
      round(silhouette_score(X_pca, clusters), 4))

print("\nCluster Sizes:")

for cluster_id in sorted(set(clusters)):
    count = sum(clusters == cluster_id)
    print(f"Cluster {cluster_id}: {count} data points")
