class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def show_details(self):
        self.show_name()
        print("Branch:", self.branch)


student = Student("Himanshu", "Electrical Engineering")
student.show_details()