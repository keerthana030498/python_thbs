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


model1 = vehicle("toyata", "camry", "2022")
model1.start_engine()
model1.stop_engine()
