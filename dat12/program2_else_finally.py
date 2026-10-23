try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")