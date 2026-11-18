
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()
X = iris.data

# Store inertia values
inertia_values = []

# Test different K values
for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)
    inertia_values.append(model.inertia_)

# Display inertia values
print("ELBOW METHOD RESULTS")
print("--------------------")

for k, inertia in enumerate(inertia_values, start=1):
    print(f"K = {k}, Inertia = {inertia:.2f}")

# Plot Elbow graph
plt.plot(
    range(1, 11),
    inertia_values,
    marker="o"
)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()
