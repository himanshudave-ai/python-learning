
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Automatically select components
pca = PCA(n_components=0.95)
X_reduced = pca.fit_transform(X_scaled)

# Display results
print("FEATURE REDUCTION RESULTS")
print("-------------------------")

print("Original Features:", X.shape[1])
print("Reduced Features:", X_reduced.shape[1])

print("Reduced Dataset Shape:", X_reduced.shape)

print("Variance Retained:",
      round(sum(pca.explained_variance_ratio_) * 100, 2), "%")
