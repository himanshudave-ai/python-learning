import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = 1
new_marks = 95

cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (new_marks, student_id))

connection.commit()

if cursor.rowcount > 0:
    print("Student record updated successfully!")
else:
    print("Student ID not found.")

connection.close()