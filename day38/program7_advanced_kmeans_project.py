
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load dataset
iris = load_iris()
X = iris.data

# Scale dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Compare different K values
print("ADVANCED K-MEANS ANALYSIS")
print("------------------------")

results = {}

for k in range(2, 6):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)

    results[k] = score

    print(
        f"K = {k}, "
        f"Silhouette Score = {score:.4f}, "
        f"Inertia = {model.inertia_:.2f}"
    )

# Select best K based on silhouette score
best_k = max(results, key=results.get)

print("\nBEST CLUSTER MODEL")
print("-----------------")
print("Best K:", best_k)
print("Best Silhouette Score:", round(results[best_k], 4))

# Train final model
final_model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

final_labels = final_model.fit_predict(X_scaled)

print("\nFinal Model Completed!")
print("Total Clusters:", len(set(final_labels)))

# Visualize using first two scaled features
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=final_labels,
    cmap="viridis"
)

plt.title("Advanced K-Means Clustering")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.show()
