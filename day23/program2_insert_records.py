import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

students = [
    (1, "Amit", "Electrical", 85),
    (2, "Priya", "Computer", 92),
    (3, "Rahul", "Mechanical", 76),
    (4, "Neha", "Civil", 88),
    (5, "Ravi", "Electrical", 68)
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(id, name, branch, marks)
VALUES (?, ?, ?, ?)
""", students)

connection.commit()

print("Student records inserted successfully!")

connection.close()