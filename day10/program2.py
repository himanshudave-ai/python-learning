class Animal():
    def speak(self):
        print("Animal can speak")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog1=Dog()
dog2=Dog()

class Cat(Animal):
    def mow(self):
        print("Cat mows")
cat1=Cat()
cat2=Cat()

dog1.bark()
cat2.mow()
