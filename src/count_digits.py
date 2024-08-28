str1 = "PYnative29@#8496"

sum =0
cnt = 0
for char in str1:
    if char.isdigit():
        sum += int(char)
        cnt += 1
av = sum/cnt
print(sum,av)
