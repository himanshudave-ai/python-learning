import math
import random
from datetime import datetime


while True:
    print("\n--- UTILITY TOOLKIT ---")
    print("1. Square Root")
    print("2. Random Number")
    print("3. Current Date and Time")
    print("4. Factorial")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            num = float(input("Enter a non-negative number: "))

            if num < 0:
                print("Number cannot be negative.")
            else:
                print("Square root:", math.sqrt(num))

        elif choice == "2":
            start = int(input("Enter starting number: "))
            end = int(input("Enter ending number: "))

            if start > end:
                print("Starting number must not exceed ending number.")
            else:
                print("Random number:", random.randint(start, end))

        elif choice == "3":
            print("Current date and time:", datetime.now())

        elif choice == "4":
            num = int(input("Enter a non-negative integer: "))

            if num < 0:
                print("Number cannot be negative.")
            else:
                print("Factorial:", math.factorial(num))

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")