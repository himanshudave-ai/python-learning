
import pandas as pd

# Create student data
data = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Branch": ["Electrical", "Mechanical", "Civil", "Electrical", "Civil"],
    "Marks": [95, 90, 78, 88, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display student data
print("STUDENT DATA")
print("-------------")
print(df)

# Display basic information
print("\nTotal Students:", len(df))
print("Average Marks:", df["Marks"].mean())
