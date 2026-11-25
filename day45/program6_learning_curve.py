
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import learning_curve

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Calculate learning curve
train_sizes, train_scores, validation_scores = learning_curve(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy",
    train_sizes=np.linspace(0.1, 1.0, 5),
    random_state=42
)

# Calculate mean scores
train_mean = np.mean(train_scores, axis=1)
validation_mean = np.mean(validation_scores, axis=1)

# Display results
print("LEARNING CURVE ANALYSIS")
print("-----------------------")

for size, train_score, val_score in zip(
    train_sizes, train_mean, validation_mean
):
    print(
        f"Training Samples: {size}, "
        f"Training Accuracy: {train_score:.3f}, "
        f"Validation Accuracy: {val_score:.3f}"
    )

# Plot learning curves
plt.figure(figsize=(8, 6))

plt.plot(
    train_sizes,
    train_mean,
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    train_sizes,
    validation_mean,
    marker="o",
    label="Validation Accuracy"
)

# Graph formatting
plt.title("Learning Curve - Random Forest Classifier")
plt.xlabel("Number of Training Samples")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()

plt.show()
