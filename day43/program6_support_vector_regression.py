
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([15, 25, 35, 45, 55, 65, 75, 85])

# Scale input features
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

# Create SVR model
model = SVR(kernel="rbf", C=100, gamma="scale", epsilon=0.1)

# Train model
model.fit(X_scaled, y)

# Make predictions
experience = np.array([[2.5], [4.5], [6.5]])
experience_scaled = scaler_X.transform(experience)

predictions = model.predict(experience_scaled)

# Display results
print("SUPPORT VECTOR REGRESSION")
print("-------------------------")

for exp, salary in zip(experience, predictions):
    print(
        f"Experience: {exp[0]} years, "
        f"Predicted Salary: {salary:.2f} LPA"
    )

print("Model R2 Score:", round(model.score(X_scaled, y), 4))
