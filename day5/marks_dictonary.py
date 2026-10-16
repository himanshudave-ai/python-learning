marks = {}

subjects = ["Physics", "Math", "English", "Programming", "Electronics"]

for subject in subjects:
    marks[subject] = int(input(f"Enter marks in {subject}: "))

print("\nMarks")

for subject, mark in marks.items():
    print(subject, ":", mark)

print("Total =", sum(marks.values()))
print("Highest =", max(marks.values()))
print("Lowest =", min(marks.values()))
print("Average =", sum(marks.values()) / len(marks))