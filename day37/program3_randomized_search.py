from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create model
model = RandomForestClassifier(random_state=42)

# Define parameter options
param_dist = {
    "n_estimators": [50, 100, 150, 200],
    "max_depth": [2, 3, 4, 5, None],
    "criterion": ["gini", "entropy"]
}

# Apply Randomized Search
random_search = RandomizedSearchCV(
    model,
    param_dist,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42
)

random_search.fit(X, y)

# Display results
print("RANDOMIZED SEARCH RESULTS")
print("-------------------------")

print("Best Parameters:", random_search.best_params_)
print(
    "Best Accuracy:",
    round(random_search.best_score_ * 100, 2),
    "%"
)