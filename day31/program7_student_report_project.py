from openpyxl import load_workbook

workbook = load_workbook("student_records.xlsx")
sheet = workbook.active

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")

for row in range(2, sheet.max_row + 1):
    roll_no = sheet.cell(row, 1).value
    name = sheet.cell(row, 2).value
    branch = sheet.cell(row, 3).value
    marks = sheet.cell(row, 4).value

    if not name:
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    else:
        grade = "C"

    print("Roll No:", roll_no)
    print("Name:", name)
    print("Branch:", branch)
    print("Marks:", marks)
    print("Grade:", grade)
    print("--------------------------")