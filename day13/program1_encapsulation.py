class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful:", amount)
        else:
            print("Amount must be positive.")

    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.__balance)


account = BankAccount("Himanshu", 5000)

account.show_balance()
account.deposit(1000)
account.show_balance()