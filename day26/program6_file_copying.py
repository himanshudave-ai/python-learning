import shutil

source = "student.txt"
destination = "student_backup.txt"

shutil.copy(source, destination)

print("File copied successfully!")
print("Backup created:", destination)