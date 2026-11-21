
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load Iris dataset
iris = load_iris()
X = iris.data

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Display results
print("BASIC PCA RESULTS")
print("-----------------")

print("Original Dataset Shape:", X.shape)
print("Reduced Dataset Shape:", X_pca.shape)

print("\nFirst 5 PCA Values:")
print(X_pca[:5])

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Retained:")
print(round(sum(pca.explained_variance_ratio_) * 100, 2), "%")
