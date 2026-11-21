
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Create 3D plot
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

for species in range(3):
    ax.scatter(
        X_pca[y == species, 0],
        X_pca[y == species, 1],
        X_pca[y == species, 2],
        label=iris.target_names[species]
    )

ax.set_title("PCA 3D Visualization")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.legend()

plt.show()

print("Explained Variance:", pca.explained_variance_ratio_)
print("Total Variance Retained:",
      round(sum(pca.explained_variance_ratio_) * 100, 2), "%")
