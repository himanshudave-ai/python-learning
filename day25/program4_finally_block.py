try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input!")

finally:
    print("Program execution completed.")