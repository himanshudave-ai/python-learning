def calculator():
    while True:
        print("\nSAFE CALCULATOR")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)

            elif choice == "2":
                print("Result:", a - b)

            elif choice == "3":
                print("Result:", a * b)

            elif choice == "4":
                if b == 0:
                    raise ZeroDivisionError
                print("Result:", a / b)

        except ValueError:
            print("Please enter valid numbers!")

        except ZeroDivisionError:
            print("Cannot divide by zero!")


calculator()