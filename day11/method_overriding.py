class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

e1 = Employee()
m1 = Manager()

e1.work()
m1.work()