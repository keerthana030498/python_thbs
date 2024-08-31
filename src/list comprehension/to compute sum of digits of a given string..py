String = "Hello World 2345"
sum = 0

for x in String:
    if x.isdigit():
        sum += int(x)
print(sum)