
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()
X = iris.data

# Apply StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train model
model.fit(X_scaled)

# Get cluster labels
labels = model.labels_

# Display results
print("K-MEANS WITH STANDARD SCALER")
print("----------------------------")

print("Total Samples:", len(X_scaled))
print("Number of Clusters:", model.n_clusters)

print("\nFirst 10 Cluster Labels:")

for i in range(10):
    print("Sample", i + 1, ":", labels[i])

print("\nCluster Distribution:")

for cluster in range(3):
    count = sum(labels == cluster)
    print("Cluster", cluster, ":", count, "samples")

print("\nScaled Cluster Centers:")
print(model.cluster_centers_)
