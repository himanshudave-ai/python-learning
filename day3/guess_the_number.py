secret=9
guess=0
while guess!=secret:
    guess=int(input("Enter your guess: "))
    if guess==secret:
        print("You guessed it right!")  
    else:
        print("Try again!")