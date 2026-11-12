
import pandas as pd

data = {
    "Name": ["Himanshu", "Rahul", "Amit", "Priya", "Neha"],
    "Marks": [95, 90, 78, 88, 82]
}

df = pd.DataFrame(data)

# Sort marks in descending order
sorted_data = df.sort_values(
    by="Marks",
    ascending=False
)

print("STUDENTS RANKED BY MARKS")
print("------------------------")
print(sorted_data)
