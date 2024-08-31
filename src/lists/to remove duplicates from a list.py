lst = [1,2,3,7,2,1,5,6,4,8,5,4]
result = set(lst)
print(result)



res = []
for i in lst:
    if i not in res:
        res.append(i)

print(set(res))