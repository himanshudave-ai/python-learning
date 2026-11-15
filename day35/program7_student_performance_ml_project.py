
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Step 1: Dataset
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [45, 50, 55, 65, 70,
     80, 90, 95, 100, 105]

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Test predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate model
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("STUDENT PERFORMANCE PREDICTION")
print("--------------------------------")
print("Model Training Completed!")
print("R2 Score:", round(r2, 3))
print("Mean Absolute Error:", round(mae, 2))

# Step 6: Predict marks for a new student
study_hours = [[7]]
predicted_marks = model.predict(study_hours)

print("\nNew Student Study Hours:", study_hours[0][0])
print("Predicted Marks:", round(predicted_marks[0], 2))

# Step 7: Visualize results
plt.scatter(X, y, label="Actual Marks")
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Student Marks")
plt.title("Student Performance Prediction")
plt.legend()
plt.grid(True)
plt.show()
