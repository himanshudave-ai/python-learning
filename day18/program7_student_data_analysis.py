import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Karan"],
    "Branch": ["EE", "CSE", "Civil", "EE", "CSE"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Student Report")
print(df)

print("\nTotal students:", len(df))
print("Average marks:", round(df["Marks"].mean(), 2))
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())

topper = df.loc[df["Marks"].idxmax()]

print("\nTopper:", topper["Name"])
print("Topper's marks:", topper["Marks"])

print("\nBranch-wise average marks:")
print(df.groupby("Branch")["Marks"].mean())