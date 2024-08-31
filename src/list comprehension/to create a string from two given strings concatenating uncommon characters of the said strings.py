String1 = "ABCPQXYZ"
String2 = "XYNZABMC"
result = ""

for char in String1:
    if char not in String2:
        result += char
for char in String2:
    if char not in String1:
        result += char

print(result)
