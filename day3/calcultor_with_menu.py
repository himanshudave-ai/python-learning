while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 + num2}")
        
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 - num2}")
        
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 * num2}")
        
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error! Division by zero.")
            
    elif choice == '5':
        print("Exiting the calculator.")
        
    else:
        print("Invalid choice! Please try again.")
        