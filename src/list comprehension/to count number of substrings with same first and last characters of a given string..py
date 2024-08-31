s = "python"
count = 0
lenght = len(s)

for i in range(lenght):
    for j in range(i,lenght):
        if s[i] == s[j]:
            count += 1
print(count)
