class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawn:", amount)

    def show_balance(self):
        print("Account holder:", self.holder)
        print("Balance:", self.balance)


account = BankAccount("Himanshu", 5000)

try:
    account.deposit(1000)
    account.withdraw(2000)
    account.show_balance()

except ValueError as error:
    print("Transaction error:", error)