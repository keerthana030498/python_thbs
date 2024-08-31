l1 = [23,45,67,78,89,34]

l2 = [34,89,55,56,39,67]
#l1 = set(l1)
#l2 = set(l2)

#print(l1.intersection(l2))

res = []
for i in l1:
    if i in l2:
        if i not in res:
            res.append(i)
print(res)



