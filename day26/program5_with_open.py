# Program 5: Using with open()

with open("student.txt", "r") as file:
    data = file.read()

print("STUDENT INFORMATION")
print("--------------------")
print(data)

print("File closed automatically after reading.")