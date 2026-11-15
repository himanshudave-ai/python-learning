import pandas as pd

# Create student dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("STUDENT DATASET")
print("----------------")
print(df)

print("\nDataset Information")
print("Total Students:", len(df))
print("Average Marks:", df["Marks"].mean())