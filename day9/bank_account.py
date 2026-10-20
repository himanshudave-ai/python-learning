class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


# Object
account1 = BankAccount("Himanshu", 1000)

# Calling methods
account1.show_balance()

account1.deposit(500)

account1.withdraw(200)

account1.withdraw(2000)

account1.show_balance()