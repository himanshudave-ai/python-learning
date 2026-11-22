
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create K-Fold
kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Evaluate model
scores = cross_val_score(
    model, X, y, cv=kfold, scoring="accuracy"
)

# Display results
print("K-FOLD CROSS VALIDATION")
print("-----------------------")

for i, score in enumerate(scores, start=1):
    print(f"Fold {i}: {score:.2f}")

print("Mean Accuracy:", round(scores.mean(), 4))
print("Standard Deviation:", round(scores.std(), 4))
