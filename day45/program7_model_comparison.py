
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define classification models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42
    ),
    "SVM": SVC(kernel="rbf")
}

# Compare models using cross-validation
print("MACHINE LEARNING MODEL COMPARISON")
print("---------------------------------")

results = {}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    mean_score = np.mean(scores)
    results[name] = mean_score

    print(f"{name}: {mean_score * 100:.2f}%")

# Find best model
best_model = max(results, key=results.get)

print("\nBEST PERFORMING MODEL")
print("---------------------")
print(best_model)
print("Accuracy:", round(results[best_model] * 100, 2), "%")
