import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = 5

cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (student_id,))

connection.commit()

if cursor.rowcount > 0:
    print("Student record deleted successfully!")
else:
    print("Student ID not found.")

connection.close()