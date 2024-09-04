t = (2, 34, 45, 6, 7, 2, 4, 5, 78, 34, 2)
count1 = t.count(2)
print(count1)

item = 2
count2 =0


for i in t:
    if i == item:
        count2 += 1
print(count2)