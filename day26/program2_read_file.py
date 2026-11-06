# Program 2: Read data from a file

file = open("student.txt", "r")

data = file.read()

print("STUDENT DETAILS")
print("----------------")
print(data)

file.close()