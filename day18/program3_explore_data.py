import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print("First two rows:")
print(df.head(2))

print("\nData information:")
print(df.info())

print("\nSummary statistics:")
print(df["Marks"].describe())