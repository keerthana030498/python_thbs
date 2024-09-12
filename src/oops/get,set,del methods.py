class Student:
    name = "ram"
    age = "26"

print(getattr(Student,'name'))
print(getattr(Student,'age'))
print(getattr(Student,'gender','no attribute found'))


#dot notation
print(Student.name)
print(Student.age)

setattr(Student,'name','keer')
print(Student.name)

setattr(Student,'gender','female')
print(Student.gender)

Student.city = "blr"
print(Student.city)

print(Student.__dict__)

delattr(Student,'city')
print(Student.__dict__)