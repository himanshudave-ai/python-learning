try:
    with open("student.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found. Please create student.txt.")

except PermissionError:
    print("Permission denied while reading the file.")