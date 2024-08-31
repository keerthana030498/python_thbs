lst = [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30,100]
res = dict()

for i in lst:
    if i in res:
        res[i] +=1
    else:
        res[i] = 1
print(res)