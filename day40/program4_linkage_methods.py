
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Load dataset
iris = load_iris()
X = iris.data

linkage_methods = [
    "ward",
    "complete",
    "average",
    "single"
]

print("LINKAGE METHODS COMPARISON")
print("--------------------------")

for method in linkage_methods:

    model = AgglomerativeClustering(
        n_clusters=3,
        linkage=method
    )

    clusters = model.fit_predict(X)

    print("\nLinkage Method:", method)
    print("Total Clusters:", len(set(clusters)))

    for cluster_id in range(3):
        count = sum(clusters == cluster_id)
        print(f"Cluster {cluster_id}: {count} points")
