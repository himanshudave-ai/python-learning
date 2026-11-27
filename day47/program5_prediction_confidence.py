
import joblib
from sklearn.datasets import load_iris

# Load saved model
model = joblib.load("iris_model.pkl")

# Load Iris dataset
iris = load_iris()

# Input sample
sample = [[5.1, 3.5, 1.4, 0.2]]

# Predict flower
prediction = model.predict(sample)

# Calculate prediction probabilities
probabilities = model.predict_proba(sample)

# Get predicted flower name
flower_name = iris.target_names[prediction[0]]

# Display results
print("IRIS PREDICTION WITH CONFIDENCE")
print("--------------------------------")

print("Predicted Flower:", flower_name)

print("\nConfidence Scores:")

for name, probability in zip(
    iris.target_names, probabilities[0]
):
    print(name, ":", round(probability * 100, 2), "%")

print("\nFinal Confidence:",
      round(max(probabilities[0]) * 100, 2), "%")
