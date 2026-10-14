def calculate_total(a,b,c,d,e):
    return a+b+c+d+e

def calculate_percentage(total):
    return (total/500)*100
def calculate_grade(percentage):
    if percentage>=90:
        return "A"
    elif percentage>=80:
        return "B"
    elif percentage>=70:
        return "C"
    elif percentage>=60:
        return "D"
    else:
        return "F"
num1=int(input("Enter marks for subject 1: "))
num2=int(input("Enter marks for subject 2: "))
num3=int(input("Enter marks for subject 3: "))                 
num4=int(input("Enter marks for subject 4: "))
num5=int(input("Enter marks for subject 5: "))
total=calculate_total(num1,num2,num3,num4,num5)
percentage=calculate_percentage(total)
grade=calculate_grade(percentage)
print("Total marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)       
