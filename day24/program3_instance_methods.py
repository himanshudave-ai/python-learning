class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")


calc = Calculator()

calc.add(20, 10)
calc.subtract(20, 10)
calc.multiply(20, 10)
calc.divide(20, 10)