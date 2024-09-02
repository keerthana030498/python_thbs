data = {
    'apple': 5,
    'banana': 2,
    'cherry': 9,
    'date': 3
}

items = list(data.items())

n = len(items)

for i in range(n):
    for j in range(n-i-1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorteddict = {}

for item in items:
    sorteddict[item[0]] = item[1]

print(sorteddict)