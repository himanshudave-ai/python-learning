text=input("enter a text:")
for ch in set(text):
    print(ch,":",text.count(ch))