name=input("enter the name of student")
marks1=int(input("enter the marks of subject 1: "))
marks2=int(input("enter the marks of subject 2: "))
marks3=int(input("enter the marks of subject 3: "))
marks4=int(input("enter the marks of subject 4: "))
marks5=int(input("enter the marks of subject 5: "))
total_marks=marks1+marks2+marks3+marks4+marks5
percentage=(total_marks/500)*100
print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
if percentage>=90:
    Grade= "A"
elif percentage>=80:
    Grade= "B"
elif percentage>=70:
    Grade= "C"
elif percentage>=60:
    Grade= "D"
else:
    Grade= "F"

print(f"Grade: {Grade}")
if Grade=="F":
    print("The student has failed.")
else:
    print("The student has passed.")