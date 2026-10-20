class student:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"hello,my name is {self.name}")

student1=student("himanshu")
student2=student("komal")
student3=student("jayansh")
student3.introduce()