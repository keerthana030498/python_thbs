class Dog:
    def barking(self):
        print("dog barking")

    def eating(self):
        print("dog eating")

class Car:
    def __init__(self):
        self.dog = Dog()
    def wheels(self):
        print("car has wheels")

    def engine(self):
        print("car has engine")

    def dogbarking(self):
        self.dog.barking()

c1 = Car()
c1.engine()
c1.wheels()
c1.dogbarking()
