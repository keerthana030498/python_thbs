s = "mother terresa"
mydict = {}

for char in s:
    if char in mydict:
        mydict[char] += 1
    else:
        mydict[char]= 1
filetred_dict = {}
for char,count in mydict.items():
    if count>1:
        filetred_dict[char] = count
print(filetred_dict)

