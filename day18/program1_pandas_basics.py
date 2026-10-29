import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha"],
    "Branch": ["EE", "CSE", "Civil", "EE"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df)
print("\nDataFrame created successfully!")