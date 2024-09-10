class Dog:


    def __init__(self, name):
        self.name = name


    def barking(self):
        print(f"{self.name} dog is barking")


    def eating(self):
        print(f"{self.name}dog is eating")


class Car:
    def __init__(self, dogname, carname):
        self.dog = Dog(dogname) #creating instannce of dog with a name
        self.carname = carname
    def engine(self):
        print(f"{self.carname} has engine ")

    def wheels(self):
        print(f"{self.carname} has wheels")

    def car_barking(self):
        self.dog.barking()# accessing the barking method from Dog class
dog1 = Dog("ghost")
dog1.barking()
dog1.eating()

car = Car("john","ford")

car.wheels()
car.engine()
car.car_barking()
