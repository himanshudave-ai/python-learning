
import pandas as pd

# Student dataset
data = {
    "Name": ["Amit", "Ravi", "Priya", "Neha", "Rahul"],
    "Maths": [85, 72, 95, 88, 65],
    "Science": [78, 80, 92, 85, 70],
    "English": [82, 75, 89, 90, 68]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Science", "English"]

print("SUBJECT-WISE PERFORMANCE ANALYSIS")

for subject in subjects:

    print("\nSubject:", subject)

    print("Average Marks:", df[subject].mean())

    print("Highest Marks:", df[subject].max())

    print("Lowest Marks:", df[subject].min())

    # Find student with highest marks
    topper_index = df[subject].idxmax()

    topper_name = df.loc[topper_index, "Name"]

    topper_marks = df.loc[topper_index, subject]

    print("Subject Topper:", topper_name)

    print("Topper Marks:", topper_marks)

# Overall subject comparison
print("\nOVERALL SUBJECT AVERAGE")

print(df[subjects].mean())
