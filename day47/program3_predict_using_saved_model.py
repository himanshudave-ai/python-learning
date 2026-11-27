
import joblib
from sklearn.datasets import load_iris

# Load saved model
model = joblib.load("iris_model.pkl")

# Load Iris dataset for class names
iris = load_iris()

# Sample flower measurements
sample = [[5.1, 3.5, 1.4, 0.2]]

# Predict flower class
prediction = model.predict(sample)

# Get predicted flower name
flower_name = iris.target_names[prediction[0]]

# Display results
print("IRIS FLOWER PREDICTION")
print("----------------------")
print("Sepal Length:", sample[0][0], "cm")
print("Sepal Width:", sample[0][1], "cm")
print("Petal Length:", sample[0][2], "cm")
print("Petal Width:", sample[0][3], "cm")

print("\nPredicted Class:", prediction[0])
print("Predicted Flower:", flower_name)
