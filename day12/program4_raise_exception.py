age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError as error:
    print("Error:", error)