from openpyxl import load_workbook

# Open existing Excel workbook
workbook = load_workbook("student_records.xlsx")

# Select worksheet
sheet = workbook.active

print("STUDENT RECORDS")
print("-------------------------------")

# Read and display all rows
for row in sheet.iter_rows(values_only=True):
    print(row)