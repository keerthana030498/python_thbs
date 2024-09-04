t = ("Tutor", 'J', 23 , 56.67 , [23,12] , True)
t[4].append(20)
print(t)




slice = t[:4] + ([23,12,20,50],) + t[5:]
print(slice)