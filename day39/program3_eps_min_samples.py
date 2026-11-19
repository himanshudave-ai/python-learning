from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import numpy as np

# Generate dataset
X, y = make_blobs(
    n_samples=100,
    centers=3,
    cluster_std=0.60,
    random_state=42
)

# Different parameter combinations
settings = [
    (0.3, 5),
    (0.5, 5),
    (0.8, 5),
    (1.0, 5),
    (0.8, 10)
]

print("EPS AND MIN SAMPLES COMPARISON")
print("--------------------------------")

for eps, min_samples in settings:

    model = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    labels = model.fit_predict(X)

    total_clusters = len(set(labels)) - (
        1 if -1 in labels else 0
    )

    noise = np.sum(labels == -1)

    print(
        f"EPS: {eps}, "
        f"Min Samples: {min_samples}, "
        f"Clusters: {total_clusters}, "
        f"Noise: {noise}"
    )