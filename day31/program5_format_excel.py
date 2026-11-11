
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# Get the folder where this Python script is saved
folder = Path(__file__).resolve().parent

# Open Excel file from the same folder
file_path = folder / "student_records.xlsx"
workbook = load_workbook(file_path)

# Select worksheet
sheet = workbook.active

# Clear old formatting from all student rows
for row in sheet.iter_rows(min_row=2):
    for cell in row:
        cell.fill = PatternFill(fill_type=None)
        cell.font = Font(color="000000", bold=False)
        cell.alignment = Alignment(horizontal="left")

# Format only the heading row
for cell in sheet[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(
        start_color="000080",
        end_color="000080",
        fill_type="solid"
    )
    cell.alignment = Alignment(horizontal="center")

# Adjust column widths
sheet.column_dimensions["A"].width = 12
sheet.column_dimensions["B"].width = 18
sheet.column_dimensions["C"].width = 22
sheet.column_dimensions["D"].width = 12

# Save updated workbook
workbook.save(file_path)

print("Excel formatting completed successfully!")
print("Updated file:", file_path)
print("Only heading row formatted.")
print("Student records preserved.")
