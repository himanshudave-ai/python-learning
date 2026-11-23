
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
# Columns: Study Hours, Practice Hours
X = np.array([
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 2],
    [5, 3],
    [6, 3]
])

# Student marks
y = np.array([20, 30, 45, 55, 70, 80])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks
new_student = np.array([[7, 4]])
prediction = model.predict(new_student)

# Display results
print("MULTIPLE LINEAR REGRESSION")
print("--------------------------")

print("Study Hours Coefficient:", model.coef_[0])
print("Practice Hours Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)

print("Predicted Marks:", round(prediction[0], 2))
print("R2 Score:", round(model.score(X, y), 4))
