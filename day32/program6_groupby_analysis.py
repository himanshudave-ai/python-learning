
import pandas as pd

data = {
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Branch": ["Electrical", "Mechanical", "Civil", "Electrical", "Civil"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

# Group students by branch
branch_analysis = df.groupby("Branch")["Marks"].agg(
    ["count", "mean", "max", "min"]
)

print("BRANCH-WISE PERFORMANCE")
print("-----------------------")
print(branch_analysis)
