from fileinput import close

st = [10, 22, 44, 23, 4]
clone_res = []

for i in st:
    if i in st:
        clone_res.append(i)
print(clone_res)