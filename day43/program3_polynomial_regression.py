
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 25, 50, 85, 130])

# Convert input into polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Create and train model
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
new_values = np.array([[6], [7], [8]])
new_poly = poly.transform(new_values)
predictions = model.predict(new_poly)

# Display results
print("POLYNOMIAL REGRESSION")
print("---------------------")

print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

for value, prediction in zip(new_values, predictions):
    print(f"Input: {value[0]}, Predicted Value: {prediction:.2f}")

print("R2 Score:", round(model.score(X_poly, y), 4))
