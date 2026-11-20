
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Load dataset
iris = load_iris()
X = iris.data

# Create models with different cluster counts
for k in [2, 3, 4, 5]:

    model = AgglomerativeClustering(
        n_clusters=k,
        linkage="ward"
    )

    clusters = model.fit_predict(X)

    print(f"\nNumber of Clusters: {k}")
    print("Cluster Labels:", set(clusters))
    print("Cluster Sizes:")

    for cluster_id in range(k):
        count = sum(clusters == cluster_id)
        print(f"Cluster {cluster_id}: {count} data points")
