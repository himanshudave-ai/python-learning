import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

passed_students = df[df["Marks"] >= 80]

print("Students scoring 80 or more:")
print(passed_students)