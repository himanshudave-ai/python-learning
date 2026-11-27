
import joblib
import csv
from sklearn.datasets import load_iris

# Load saved model
model = joblib.load("iris_model.pkl")

# Load Iris dataset
iris = load_iris()

# Multiple flower samples
samples = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.5, 3.0, 5.5, 1.8]
]

# Make predictions
predictions = model.predict(samples)
probabilities = model.predict_proba(samples)

# Save results to CSV
with open("flower_predictions.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Sepal Length",
        "Sepal Width",
        "Petal Length",
        "Petal Width",
        "Predicted Flower",
        "Confidence"
    ])

    for sample, prediction, probability in zip(
        samples, predictions, probabilities
    ):
        flower_name = iris.target_names[prediction]
        confidence = round(max(probability) * 100, 2)

        writer.writerow(
            sample + [flower_name, confidence]
        )

print("Predictions saved successfully!")
print("File created: flower_predictions.csv")
