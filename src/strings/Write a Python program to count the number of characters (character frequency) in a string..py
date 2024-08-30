s = "tutorjoes"
mydict = {}
for char in s:
    if char in mydict:
        mydict[char] += 1
    else:
        mydict[char] = 1
print(mydict)