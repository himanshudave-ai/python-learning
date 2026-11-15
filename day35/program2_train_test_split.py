from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))

print("\nX Training:", X_train)
print("X Testing:", X_test)