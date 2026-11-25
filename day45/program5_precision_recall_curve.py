
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize
from sklearn.metrics import precision_recall_curve, average_precision_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

n_classes = len(iris.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Predict class probabilities
y_prob = model.predict_proba(X_test)

# Convert test labels into binary format
y_test_binary = label_binarize(
    y_test,
    classes=np.arange(n_classes)
)

# Plot Precision-Recall curves
plt.figure(figsize=(8, 6))

for i in range(n_classes):
    precision, recall, thresholds = precision_recall_curve(
        y_test_binary[:, i],
        y_prob[:, i]
    )

    ap_score = average_precision_score(
        y_test_binary[:, i],
        y_prob[:, i]
    )

    print(
        f"{iris.target_names[i]} Average Precision:",
        round(ap_score, 4)
    )

    plt.plot(
        recall,
        precision,
        label=f"{iris.target_names[i]} (AP = {ap_score:.2f})"
    )

# Graph formatting
plt.title("Precision-Recall Curve - Random Forest")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.legend()
plt.grid()

plt.show()
