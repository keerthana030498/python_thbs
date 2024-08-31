lst = ['Words', 'Longer', 'given', 'Words','cat']
minlen = 4
res = []
for word in lst:
    if len(word) > minlen:
        res.append(word)
print(res)