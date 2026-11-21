
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Load dataset
iris = load_iris()
X = iris.data

# Step 2: Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

# Step 4: Apply K-Means
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(X_pca)

# Step 5: Evaluate model
score = silhouette_score(X_pca, clusters)

print("ADVANCED PCA PROJECT")
print("--------------------")

print("Original Features:", X.shape[1])
print("Reduced Features:", X_pca.shape[1])

print("Original Dataset Shape:", X.shape)
print("Reduced Dataset Shape:", X_pca.shape)

print("\nVariance Retained:",
      round(sum(pca.explained_variance_ratio_) * 100, 2), "%")

print("Total Clusters:", len(set(clusters)))
print("Silhouette Score:", round(score, 4))

print("\nCluster Summary:")

for cluster_id in sorted(set(clusters)):
    count = sum(clusters == cluster_id)
    print(f"Cluster {cluster_id}: {count} data points")

# Step 6: Visualize clusters
plt.figure(figsize=(8, 6))

for cluster_id in sorted(set(clusters)):
    plt.scatter(
        X_pca[clusters == cluster_id, 0],
        X_pca[clusters == cluster_id, 1],
        label=f"Cluster {cluster_id}"
    )

plt.title("Advanced PCA with K-Means")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()
