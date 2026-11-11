from openpyxl import load_workbook

workbook = load_workbook("student_records.xlsx")
sheet = workbook.active

total_marks = 0
count = 0

for row in range(2, sheet.max_row + 1):
    marks = sheet.cell(row=row, column=4).value

    if isinstance(marks, (int, float)):
        total_marks += marks
        count += 1

if count > 0:
    average = total_marks / count

    print("STUDENT MARKS ANALYSIS")
    print("----------------------")
    print("Total Students:", count)
    print("Total Marks:", total_marks)
    print("Average Marks:", round(average, 2))
else:
    print("No student marks found.")