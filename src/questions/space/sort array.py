lst = [20, 340, 50, 10, 30]

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j]>lst[j+1]:
            lst[j+1],lst[j] = lst[j],lst[j+1]
print(lst)