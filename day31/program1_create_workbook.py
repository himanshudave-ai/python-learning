from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select active worksheet
sheet = workbook.active

# Rename worksheet
sheet.title = "Students"

# Save Excel file
workbook.save("student_records.xlsx")

print("Excel workbook created successfully!")
print("File name: student_records.xlsx")