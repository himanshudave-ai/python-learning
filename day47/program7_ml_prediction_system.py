
import joblib
from sklearn.datasets import load_iris

# Load saved model
model = joblib.load("iris_model.pkl")

# Load Iris dataset
iris = load_iris()

print("IRIS FLOWER PREDICTION SYSTEM")
print("-----------------------------")

# Take input from user
sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

# Prepare input
sample = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

# Predict flower
prediction = model.predict(sample)
probabilities = model.predict_proba(sample)

# Get flower name
flower_name = iris.target_names[prediction[0]]

# Calculate confidence
confidence = max(probabilities[0]) * 100

# Display results
print("\nPREDICTION RESULT")
print("-----------------")
print("Predicted Flower:", flower_name)
print("Confidence Score:", round(confidence, 2), "%")
