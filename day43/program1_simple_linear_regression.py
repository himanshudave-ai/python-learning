
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([15, 25, 35, 45, 55])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Make prediction
hours = np.array([[6], [7], [8]])
predictions = model.predict(hours)

# Display results
print("SIMPLE LINEAR REGRESSION")
print("------------------------")

print("Model Slope:", model.coef_[0])
print("Model Intercept:", model.intercept_)

for hour, marks in zip(hours, predictions):
    print(f"Study Hours: {hour[0]}, Predicted Marks: {marks:.2f}")

print("Model R2 Score:", model.score(X, y))
