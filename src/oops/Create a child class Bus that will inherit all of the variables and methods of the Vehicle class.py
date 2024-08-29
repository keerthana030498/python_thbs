class Vehicle:
    def __init__(self,name,max_Speed,mileage):
        self.name = name
        self.max_Speed = max_Speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

schoolbus = Bus("bmw",100,80)
print(schoolbus.name,schoolbus.max_Speed,schoolbus.mileage)
