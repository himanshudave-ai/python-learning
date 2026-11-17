
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = DecisionTreeClassifier(random_state=42)

# Define parameters
param_grid = {
    "max_depth": [2, 3, 4, 5, None],
    "criterion": ["gini", "entropy"]
}

# Apply Grid Search
grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X, y)

# Display results
print("GRID SEARCH RESULTS")
print("-------------------")

print("Best Parameters:", grid_search.best_params_)
print("Best Accuracy:",
      round(grid_search.best_score_ * 100, 2), "%")
