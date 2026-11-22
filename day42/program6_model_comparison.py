
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define models
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    ),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42
    ),
    "SVM": make_pipeline(
        StandardScaler(),
        SVC()
    )
}

# Cross-validation setup
cv = StratifiedKFold(
    n_splits=5, shuffle=True, random_state=42
)

# Compare models
print("MACHINE LEARNING MODEL COMPARISON")
print("--------------------------------")

results = {}

for name, model in models.items():
    scores = cross_val_score(
        model, X, y, cv=cv, scoring="accuracy"
    )

    results[name] = scores.mean()

    print(f"{name}: {scores.mean():.4f}")

# Best model
best_model = max(results, key=results.get)

print("\nBest Performing Model:", best_model)
print("Best Accuracy:", round(results[best_model], 4))
