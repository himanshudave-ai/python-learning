
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Machine Learning model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("TRAIN-TEST SPLIT RESULTS")
print("------------------------")

print("Original Dataset:", X.shape)
print("Training Dataset:", X_train.shape)
print("Testing Dataset:", X_test.shape)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("Model Accuracy:", round(accuracy * 100, 2), "%")
