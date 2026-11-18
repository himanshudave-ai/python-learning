
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer data:
# Annual Income (thousands), Spending Score
X = np.array([
    [15, 39],
    [16, 81],
    [17, 6],
    [18, 77],
    [20, 40],
    [25, 76],
    [30, 10],
    [35, 75],
    [40, 35],
    [45, 80],
    [50, 20],
    [55, 70]
])

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(X_scaled)

# Display results
print("CUSTOMER CLUSTERING RESULTS")
print("---------------------------")

for i, cluster in enumerate(clusters):
    print(
        f"Customer {i + 1}: "
        f"Income = {X[i][0]}, "
        f"Spending = {X[i][1]}, "
        f"Cluster = {cluster}"
    )

print("\nTotal Clusters:", len(set(clusters)))
