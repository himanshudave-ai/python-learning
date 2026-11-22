
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,
    stratify=y
)

# Create ML pipeline
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("ADVANCED MODEL EVALUATION")
print("-------------------------")

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Classification report
print("\nCLASSIFICATION REPORT")
print(classification_report(
    y_test, y_pred, target_names=iris.target_names
))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("CONFUSION MATRIX")
print(cm)

# Cross-validation
cv_scores = cross_val_score(
    model, X, y, cv=5, scoring="accuracy"
)

print("\nCROSS VALIDATION SCORES")
print(cv_scores)

print("Average CV Accuracy:",
      round(cv_scores.mean() * 100, 2), "%")

# Visualize confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot(cmap="Blues")
plt.title("Advanced Model Evaluation")
plt.show()
