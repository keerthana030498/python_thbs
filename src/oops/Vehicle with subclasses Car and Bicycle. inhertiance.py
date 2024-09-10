class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def drive(self):
        return "sublass will be implementes"

class Car(vehicle):
    def __init__(self,brand,model,fueltype):
        super().__init__(brand,model)
        self.fueltype = fueltype
    def drive(self):
        return f"{self.brand} and {self.model} has {self.fueltype}"

class Bicycle(vehicle):
    def __init__(self,brand,model,gearcount):
        super().__init__(brand,model)
        self.gearcount = gearcount
    def drive(self):
        return f"{self.brand} and {self.model} has {self.gearcount}"


cycle1 = Bicycle("BSA",1998,12)
print(cycle1.drive())