class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return "sublacss will be impletements"

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,"bark")

    def speak(self):
        return f"{self.name} says {self.sound}"

class Cat(Animal):
    def _init__(self, name):
        super().__init__(name, "meow")

    def speak(self):
        return f"{self.name} says {self.sound}"


dog1 = Dog(name = "john")
print(dog1.speak())
