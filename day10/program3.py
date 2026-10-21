class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is Driving")
car1=Car()
class byke(Vehicle):
    def run(self):
        print("byke runs")
byke1=byke()

car1.start()
car1.drive()
byke1.run()

