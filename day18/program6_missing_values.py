import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, None, 78, 88]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nData after filling missing marks:")
print(df)