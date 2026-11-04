class Student:
    def __init__(self, name, branch, marks):
        self.name = name
        self.branch = branch
        self.marks = marks

    def display(self):
        print("Student Details")
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Marks:", self.marks)


student1 = Student("Himanshu", "Electrical", 85)
student2 = Student("Rahul", "Mechanical", 90)

student1.display()
print()
student2.display()