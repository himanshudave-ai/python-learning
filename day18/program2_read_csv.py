import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print(df)