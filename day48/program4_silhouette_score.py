
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculate silhouette scores
scores = []

for k in range(2, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)
    scores.append(score)

    print("Clusters:", k, "| Silhouette Score:", round(score, 4))

# Find best number of clusters
best_k = range(2, 11)[scores.index(max(scores))]

print("\nBEST NUMBER OF CLUSTERS:", best_k)
print("BEST SILHOUETTE SCORE:", round(max(scores), 4))

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), scores, marker="o")

plt.title("Silhouette Score Analysis")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.xticks(range(2, 11))
plt.grid(True)

plt.show()
