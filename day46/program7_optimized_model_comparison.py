
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Define models and parameter grids
models = {
    "KNN": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", KNeighborsClassifier())
        ]),
        {
            "model__n_neighbors": [3, 5, 7, 9],
            "model__weights": ["uniform", "distance"]
        }
    ),

    "Decision Tree": (
        DecisionTreeClassifier(random_state=42),
        {
            "max_depth": [None, 3, 5, 7],
            "min_samples_split": [2, 5, 10]
        }
    ),

    "Random Forest": (
        RandomForestClassifier(random_state=42),
        {
            "n_estimators": [50, 100],
            "max_depth": [None, 5, 10]
        }
    ),

    "SVM": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", SVC())
        ]),
        {
            "model__C": [0.1, 1, 10],
            "model__kernel": ["linear", "rbf"]
        }
    )
}

# Tune and evaluate models
results = {}

for name, (model, params) in models.items():
    search = GridSearchCV(
        model,
        params,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    search.fit(X_train, y_train)

    y_pred = search.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    results[name] = test_accuracy

    print("\nModel:", name)
    print("Best Parameters:", search.best_params_)
    print("CV Accuracy:", round(search.best_score_ * 100, 2), "%")
    print("Test Accuracy:", round(test_accuracy * 100, 2), "%")

# Find best model
best_model = max(results, key=results.get)

print("\nFINAL MODEL COMPARISON")
print("----------------------")

for name, score in results.items():
    print(name, ":", round(score * 100, 2), "%")

print("\nBest Performing Model:", best_model)
print("Best Test Accuracy:", round(results[best_model] * 100, 2), "%")
