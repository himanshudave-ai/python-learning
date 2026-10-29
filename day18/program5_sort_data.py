import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(
    by="Marks",
    ascending=False
)

print("Students sorted by marks:")
print(sorted_df)