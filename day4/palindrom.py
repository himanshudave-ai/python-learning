while True:
 text=input("enter your text:")         
 if text==text[::-1]:        
    print("The text is a palindrome.")
 else:
    print("The text is not a palindrome.")