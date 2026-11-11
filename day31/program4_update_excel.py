
from openpyxl import load_workbook

# Open existing Excel workbook
workbook = load_workbook("student_records.xlsx")

# Select worksheet
sheet = workbook.active

# Update student marks
sheet["D2"] = 95
sheet["D3"] = 90

# Save updated workbook
workbook.save("student_records.xlsx")

print("Student marks updated successfully!")
print("Himanshu's marks:", sheet["D2"].value)
print("Rahul's marks:", sheet["D3"].value)
