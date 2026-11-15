from sklearn.linear_model import LinearRegression

# Input: Study hours
X = [[1], [2], [3], [4], [5], [6], [7]]

# Output: Student marks
y = [45, 50, 55, 65, 70, 80, 90]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

print("Model Training Completed!")

print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))