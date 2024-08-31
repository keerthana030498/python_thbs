lst = [51,7,10,34,2,8]

small = lst[0]

for i in lst:
    if i < small:
        small = i
print(small)