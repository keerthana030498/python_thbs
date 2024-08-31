string1 = "Hello"
lenght = len(string1)
upper_count = 0
lower_count = 0
digit_count = 0
if lenght >= 8:
    print("it should contain 8 length")
for char in string1:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
if upper_count >0 and lower_count > 0 and digit_count >0:
    print("its a valid string")
else:
    print("not valid")
