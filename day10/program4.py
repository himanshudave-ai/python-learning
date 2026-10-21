class Person:
    def __init__(self,name):
        self.name=name
    
    def show_name(self):
        print("Name:", self.name)

class student(Person):
    def study(self):
        print(self.name,"is studying")

student1=student("himanshu")

student1.show_name()
student1.study()