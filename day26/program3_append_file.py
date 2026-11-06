# Program 3: Append data to a file

file = open("student.txt", "a")

file.write("Course: Python Programming\n")
file.write("Learning Day: 26\n")

file.close()

print("New data appended successfully!")