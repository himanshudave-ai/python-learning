class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def show_branch(self):
        print("Branch:", self.branch)


student1 = Student("Himanshu", "Electrical")

student1.show_name()
student1.show_branch()