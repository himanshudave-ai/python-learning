
import pandas as pd

data = {
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Branch": ["Electrical", "Mechanical", "Civil", "Electrical", "Civil"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

# Filter students scoring 85 or above
top_students = df[df["Marks"] >= 85]

print("STUDENTS SCORING 85 OR ABOVE")
print("----------------------------")
print(top_students)
