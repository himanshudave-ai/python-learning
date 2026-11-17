from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = {}

print("MACHINE LEARNING MODEL COMPARISON")
print("---------------------------------")

# Evaluate each model
for name, model in models.items():

    # Cross validation
    cv_scores = cross_val_score(
        model, X_train, y_train, cv=5
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    results[name] = accuracy

    print("\nModel:", name)
    print("Cross Validation Accuracy:",
          round(cv_scores.mean() * 100, 2), "%")
    print("Test Accuracy:",
          round(accuracy * 100, 2), "%")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=iris.target_names
        )
    )

# Identify best model
best_model = max(results, key=results.get)

print("\nBEST PERFORMING MODEL")
print("---------------------")
print("Model:", best_model)
print("Accuracy:", round(results[best_model] * 100, 2), "%")