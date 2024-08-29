class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

schoolbus = Bus("volvo",12,13)
print(schoolbus.color,schoolbus.name,schoolbus.max_speed,schoolbus.mileage)
car = Car("volvo",12,13)
print(car.color,car.name,car.max_speed,car.mileage)