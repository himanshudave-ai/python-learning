from sklearn.linear_model import LogisticRegression

# Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

study_hours = [[6]]

prediction = model.predict(study_hours)

print("Study Hours:", study_hours[0][0])

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")