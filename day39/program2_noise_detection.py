from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import numpy as np

# Generate normal data
X, y = make_blobs(
    n_samples=100,
    centers=3,
    random_state=42
)

# Add artificial outliers
outliers = np.array([
    [10, 10],
    [12, 12],
    [-10, -10],
    [15, -12]
])

X = np.vstack((X, outliers))

# Apply DBSCAN
model = DBSCAN(eps=0.8, min_samples=5)
clusters = model.fit_predict(X)

# Identify noise points
noise_points = X[clusters == -1]

print("NOISE DETECTION RESULTS")
print("-----------------------")

print("Total Data Points:", len(X))
print("Noise Points:", len(noise_points))

print("\nOutlier Coordinates:")

for point in noise_points:
    print(point)