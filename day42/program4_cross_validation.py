
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create model
model = DecisionTreeClassifier(random_state=42)

# Perform 5-fold cross-validation
scores = cross_val_score(
    model, X, y, cv=5, scoring="accuracy"
)

# Display results
print("CROSS VALIDATION RESULTS")
print("------------------------")

for i, score in enumerate(scores, start=1):
    print(f"Fold {i} Accuracy: {score:.2f}")

print("Average Accuracy:", round(scores.mean(), 4))
