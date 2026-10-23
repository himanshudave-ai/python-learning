class ATM:
    def __init__(self, balance=5000):
        self.balance = balance

    def check_balance(self):
        print("Available balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawal successful.")


atm = ATM()

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid menu option.")

    except ValueError as error:
        print("Error:", error)