class student:
    def __init__(self, name, age, branch, CGPA):
        self.name = name
        self.age = age
        self.branch = branch
        self.CGPA = CGPA 
            
student1=student("himanshu", 34, "electrical", 8.5)
student2=student("dinesh", 33, "mechanical", 8.3)

print(student1.name)
print(student1.age)
print(student1.branch)
print(student1.CGPA)
