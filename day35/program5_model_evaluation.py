from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

X = [[1], [2], [3], [4], [5], [6], [7]]
y = [45, 50, 55, 65, 70, 80, 90]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

r2 = r2_score(y, predictions)
mae = mean_absolute_error(y, predictions)

print("MODEL EVALUATION")
print("----------------")
print("R2 Score:", round(r2, 3))
print("Mean Absolute Error:", round(mae, 2))