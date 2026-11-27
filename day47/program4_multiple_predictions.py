
import joblib
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

# Display results
print("MULTIPLE IRIS FLOWER PREDICTIONS")
print("--------------------------------")

for i, prediction in enumerate(predictions):
    flower_name = iris.target_names[prediction]

    print("\nSample", i + 1)
    print("Measurements:", samples[i])
    print("Predicted Class:", prediction)
    print("Predicted Flower:", flower_name)
