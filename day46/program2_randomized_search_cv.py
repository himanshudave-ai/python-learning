
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import randint

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(random_state=42)

# Define parameter distributions
param_dist = {
    "n_estimators": randint(50, 201),
    "max_depth": [None, 3, 5, 7, 10],
    "min_samples_split": randint(2, 11),
    "min_samples_leaf": randint(1, 5)
}

# Apply Randomized Search
random_search = RandomizedSearchCV(
    model,
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)

# Train model
random_search.fit(X_train, y_train)

# Make predictions
y_pred = random_search.predict(X_test)

# Display results
print("RANDOMIZED SEARCH CV")
print("---------------------------")
print("Best Parameters:", random_search.best_params_)
print("Best CV Accuracy:", round(random_search.best_score_ * 100, 2), "%")
print("Test Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
