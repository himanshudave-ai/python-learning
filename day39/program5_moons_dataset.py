from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate moons dataset
X, y = make_moons(
    n_samples=200,
    noise=0.08,
    random_state=42
)

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
model = DBSCAN(
    eps=0.3,
    min_samples=5
)

clusters = model.fit_predict(X_scaled)

# Display visualization
plt.figure(figsize=(8, 5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters,
    cmap="plasma",
    s=40
)

plt.title("DBSCAN on Moons Dataset")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.grid(True)

plt.show()

print("Total Clusters:",
      len(set(clusters)) - (1 if -1 in clusters else 0))

print("Noise Points:",
      sum(clusters == -1))