lst = [10, 20, 30, 50, 80, 70, 70, 80, 10]
res = []
count = 0
for i in lst:
    if i not in res:
        res.append(i)
        count +=1
print(count)
