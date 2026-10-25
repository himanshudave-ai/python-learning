import random

print("Random number:", random.randint(1, 100))
print("Random choice:", random.choice(["Python", "Java", "C++"]))

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)

print("Shuffled list:", numbers)