number=int(input("Enter a number: "))
print(f"square={number**2}")
print(f"cube={number**3}")
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

fact=1
for i in range(1,number+1):
    fact*=i
print(f"Factorial={fact}")

sum=0
for i in range(1,number+1):
    sum+=i
print(f"Sum={sum}")
    