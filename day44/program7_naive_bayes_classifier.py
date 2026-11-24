
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Naive Bayes model
model = GaussianNB()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("NAIVE BAYES CLASSIFICATION")
print("--------------------------")

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nFirst 5 Predictions:")
for actual, predicted in zip(y_test[:5], y_pred[:5]):
    print(
        "Actual:", iris.target_names[actual],
        "| Predicted:", iris.target_names[predicted]
    )

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))
