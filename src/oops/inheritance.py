# class and object
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f" the {self.make} {self.model} engine is started")

    def stop_engine(self):
        print(f" the {self.make} {self.model} engine is stoped")
#derived class
class car(vehicle):
    def __init__(self,make,model, year,doors):
        super().__init__(make,model,year)
        self.doors = doors

    def open_trunk(self):
        print(f"the trunk of the {self.make} {self.model} is open")


model1 = car("toyata", "camry", "2022",4)
model1.start_engine()
model1.stop_engine()
model1.open_trunk()
