
lst = [2, 4, 56, 78, 4, 34, 5, 8, 9]

largest = 0
secondlarge = 0

for i in lst:
    if i > largest:
        secondlarge = largest
        largest = i
    elif i > secondlarge and i <largest:
        secondlarge = i
print(secondlarge)