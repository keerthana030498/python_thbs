string = "ComPuTeR"
upper_Count = 0
for char in string:
    if char.upper() == char:
        upper_Count += 1

if upper_Count > 2 :
    print(string.upper())
else:
    print(string)