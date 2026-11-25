
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert labels into binary format
y_binary = label_binarize(y, classes=[0, 1, 2])
n_classes = len(iris.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y_binary,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create and train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train using original class labels
model.fit(X_train, np.argmax(y_train, axis=1))

# Predict probabilities
y_prob = model.predict_proba(X_test)

# Calculate ROC curve and AUC for each class
plt.figure(figsize=(8, 6))

for i in range(n_classes):
    fpr, tpr, thresholds = roc_curve(
        y_test[:, i],
        y_prob[:, i]
    )

    roc_auc = auc(fpr, tpr)

    print(
        f"{iris.target_names[i]} AUC:",
        round(roc_auc, 4)
    )

    plt.plot(
        fpr,
        tpr,
        label=f"{iris.target_names[i]} (AUC = {roc_auc:.2f})"
    )

# Plot random classifier reference line
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

# Graph formatting
plt.title("ROC Curve - Random Forest Classifier")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid()

plt.show()
