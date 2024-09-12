class user:
    course ="JAVA"
print(user.__dict__)
print(user.course)

o = user()
print(o.__dict__)
o.course = "c++"
print(o.__dict__)
o2 = user()
print(o2.course)