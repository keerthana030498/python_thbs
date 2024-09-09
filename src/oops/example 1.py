from datetime import datetime
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculateAge(self):
        today = datetime.today()
        age = today.year - self.dob.year
        if today < datetime(today.year,self.dob.month,self.dob.day):
            age -= 1
        return age

person1 = Person("bhavana","india",datetime(1999,11,12))
print(person1.calculateAge())
