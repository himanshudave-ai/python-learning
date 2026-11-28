
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define clustering algorithms
models = {
    "K-Means": KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    ),

    "Hierarchical": AgglomerativeClustering(
        n_clusters=3,
        linkage="ward"
    ),

    "DBSCAN": DBSCAN(
        eps=0.8,
        min_samples=5
    )
}

# Compare algorithms
print("CLUSTERING ALGORITHM COMPARISON")
print("--------------------------------")

for name, model in models.items():

    labels = model.fit_predict(X_scaled)

    # Exclude noise points for DBSCAN
    valid_mask = labels != -1
    valid_labels = labels[valid_mask]
    valid_data = X_scaled[valid_mask]

    n_clusters = len(set(labels) - {-1})
    n_noise = sum(labels == -1)

    print("\nAlgorithm:", name)
    print("Number of Clusters:", n_clusters)
    print("Noise Points:", n_noise)

    if n_clusters >= 2 and len(set(valid_labels)) >= 2:
        score = silhouette_score(valid_data, valid_labels)
        print("Silhouette Score:", round(score, 4))
    else:
        print("Silhouette Score: Not applicable")
