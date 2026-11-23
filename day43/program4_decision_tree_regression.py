
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([10, 20, 30, 40, 50, 60])

# Create model
model = DecisionTreeRegressor(random_state=42)

# Train model
model.fit(X, y)

# Predict values
experience = np.array([[2.5], [4.5], [6.5]])
predictions = model.predict(experience)

# Display results
print("DECISION TREE REGRESSION")
print("------------------------")

for exp, salary in zip(experience, predictions):
    print(f"Experience: {exp[0]} years, Predicted Salary: {salary:.2f} LPA")

print("Model R2 Score:", model.score(X, y))
