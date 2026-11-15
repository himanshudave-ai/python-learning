from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5], [6], [7]]
y = [45, 50, 55, 65, 70, 80, 90]

model = LinearRegression()
model.fit(X, y)

# Predict marks for 8 study hours
predicted_marks = model.predict([[8]])

print("Study Hours: 8")
print("Predicted Marks:", round(predicted_marks[0], 2))