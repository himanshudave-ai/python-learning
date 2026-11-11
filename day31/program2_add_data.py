from openpyxl import load_workbook

# Open existing Excel workbook
workbook = load_workbook("student_records.xlsx")

# Select worksheet
sheet = workbook.active

# Add column headings
sheet.append(["Roll No", "Name", "Branch", "Marks"])

# Add student records
sheet.append([101, "Himanshu", "Electrical", 85])
sheet.append([102, "Rahul", "Mechanical", 90])
sheet.append([103, "Amit", "Civil", 78])

# Save workbook
workbook.save("student_records.xlsx")

print("Student records added successfully!")
print("Total student records:", sheet.max_row - 1)