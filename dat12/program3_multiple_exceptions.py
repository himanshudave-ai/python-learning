numbers = [10, 20, 30]

try:
    index = int(input("Enter index (0-2): "))
    divisor = int(input("Enter divisor: "))

    result = numbers[index] / divisor
    print("Result:", result)

except ValueError:
    print("Please enter integers only.")

except IndexError:
    print("Invalid index.")

except ZeroDivisionError:
    print("Cannot divide by zero.")