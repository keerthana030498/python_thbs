lst = [82, 4, 10, 56, 78, 4, 34, 5, 10, 9]

res = []

for i in lst:
    if i  not in res:
        res.append(i)
print(res)
