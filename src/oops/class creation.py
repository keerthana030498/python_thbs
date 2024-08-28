class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print("hello wold name is ",self.name)

    def age_person(self):
        print("my age is",self.age)

person1 = Person("ayan",26)
person1.greet()
person1.age_person()