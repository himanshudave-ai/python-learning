# Program 4: Read file line by line

file = open("student.txt", "r")

print("STUDENT DETAILS")
print("----------------")

for line in file:
    print(line.strip())

file.close()