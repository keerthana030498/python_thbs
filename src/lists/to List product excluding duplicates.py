lst = [2, 1, 2, 4, 6, 4, 3, 2, 1]

res=[]
mult = 1
for i in lst:
    if i not in res:
        res.append(i)
        mult *=i
print(mult)

