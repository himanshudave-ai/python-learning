class InsufficientBalanceError(Exception):
    pass


balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance."
        )

    balance = balance - amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as error:
    print("Invalid amount:", error)

except InsufficientBalanceError as error:
    print("Transaction failed:", error)