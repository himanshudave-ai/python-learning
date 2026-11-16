
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
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
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, predictions)

print("ADVANCED ML PROJECT")
print("-------------------")
print("Project: Iris Flower Classification")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nCLASSIFICATION REPORT")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot()
plt.title("Iris Classification - Confusion Matrix")
plt.show()

# Predict new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("NEW FLOWER PREDICTION")
print("Predicted Species:", iris.target_names[prediction[0]])
