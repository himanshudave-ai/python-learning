
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
iris = load_iris()
X = iris.data

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA with all components
pca = PCA()
pca.fit(X_scaled)

# Display explained variance
print("EXPLAINED VARIANCE ANALYSIS")
print("--------------------------")

for i, variance in enumerate(pca.explained_variance_ratio_):
    print(f"PC{i+1}: {variance * 100:.2f}%")

# Cumulative variance
cumulative = pca.explained_variance_ratio_.cumsum()

print("\nCumulative Explained Variance:")

for i, value in enumerate(cumulative):
    print(f"First {i+1} Components: {value * 100:.2f}%")
