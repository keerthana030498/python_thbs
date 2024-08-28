lst = [20, 340, 50, 10, 30]

largest  = lst[0]
second_largest = 0

for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(f"seconf largest {second_largest}")
