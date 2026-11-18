
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load dataset
iris = load_iris()
X = iris.data

# Create model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Perform clustering
clusters = model.fit_predict(X)

# Calculate Silhouette Score
score = silhouette_score(X, clusters)

# Display result
print("SILHOUETTE SCORE RESULTS")
print("------------------------")

print("Number of Clusters:", len(set(clusters)))
print("Silhouette Score:", round(score, 4))
