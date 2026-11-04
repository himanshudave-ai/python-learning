class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)


account = BankAccount("Himanshu", 5000)

account.deposit(2000)
account.show_balance()