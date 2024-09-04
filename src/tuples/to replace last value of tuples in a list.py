l = [(5, 2, 3), (4, 7, 6), (8, 9, 6)]

for i in range(len(l)):
   l[i] = l[i][:-1] + (10,)
print(l)
