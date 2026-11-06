# Program 1: Write data into a file

file = open("student.txt", "w")

file.write("Student Name: Himanshu\n")
file.write("Branch: Electrical Engineering\n")
file.write("College: VIT VELLORE\n")

file.close()

print("Data written successfully!")