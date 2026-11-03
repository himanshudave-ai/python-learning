import sqlite3

# Connect to database
connection = sqlite3.connect("college.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    marks INTEGER
)
""")

# Save changes
connection.commit()

print("Database created successfully!")
print("Students table created successfully!")

# Close connection
connection.close()