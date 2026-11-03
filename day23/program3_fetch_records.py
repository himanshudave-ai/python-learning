import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("STUDENT RECORDS")
print("-" * 45)

for student in records:
    print("ID:", student[0])
    print("Name:", student[1])
    print("Branch:", student[2])
    print("Marks:", student[3])
    print("-" * 45)

connection.close()