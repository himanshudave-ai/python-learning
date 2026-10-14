password="python"
user=input("Enter the password: ")
while user!=password:
    print("Incorrect password! Try again.")
    user=input("Enter the password: ")
print("Correct password!")