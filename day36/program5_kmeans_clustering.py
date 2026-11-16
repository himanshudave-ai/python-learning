
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Train model
clusters = model.fit_predict(X_scaled)

print("K-MEANS CLUSTERING")
print("------------------")
print("Total Data Points:", len(X))
print("Number of Clusters:", 3)

for cluster in range(3):
    count = sum(clusters == cluster)
    print("Cluster", cluster, ":", count, "data points")

# Visualization
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1 (Scaled)")
plt.ylabel("Feature 2 (Scaled)")
plt.show()
