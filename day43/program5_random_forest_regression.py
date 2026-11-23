
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([15, 25, 35, 45, 55, 65, 75, 85])

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X, y)

# Make predictions
experience = np.array([[2.5], [4.5], [6.5]])
predictions = model.predict(experience)

# Display results
print("RANDOM FOREST REGRESSION")
print("------------------------")

for exp, salary in zip(experience, predictions):
    print(
        f"Experience: {exp[0]} years, "
        f"Predicted Salary: {salary:.2f} LPA"
    )

print("Model R2 Score:", round(model.score(X, y), 4))
