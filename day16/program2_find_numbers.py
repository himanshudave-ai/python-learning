import re

text = "I have 2 laptops, 3 phones and 15 books."

numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)

total = sum(int(number) for number in numbers)
print("Sum of numbers:", total)