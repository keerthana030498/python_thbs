class Person:
    count = 0  # class variable

    def __init__(self,name,age):
        self.name = name  # this is instance variable
        self.age = age
        Person.count += 1


person1 = Person("keer",26)
person2 =Person("bhavan",24)
print(Person.count)
