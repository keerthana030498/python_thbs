lst = [10,20,400, 500,0,1,5,9]
min_value = lst[0]
max_value = lst[0]

for i in lst:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i
print(f"largest is {max_value}, smallest is {min_value}")


min_Value1 = min(lst)
max_Value1 = max(lst)
print("largest is "+ str(max_Value1) + ", smallest is " + str(min_Value1))
