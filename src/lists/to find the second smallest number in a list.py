
lst = [2, 4, 56, 78, 4, 34, 5, 8, 9]

small = None
secondsmall = None

for i in lst:
    if small is None or i < small:
        secondsmall = small
        small = i
    elif (secondsmall is None or i < secondsmall) and i >small:
        secondsmall = i
print(secondsmall)