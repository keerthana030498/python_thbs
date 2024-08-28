lst = [5,3,2,1,6,7]

min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print("smallest is ", min_value)