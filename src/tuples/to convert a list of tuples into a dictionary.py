t = [ ("Name", "Ram"), ("Name", "Pooja"), ("Age", 21), ("Gender", "Male"), ("Age", 23), ("Gender", "Female") ]
mydict = {}

for k,v in t:
    if k not in mydict:
        mydict[k] = []
    mydict[k].append(v)
print(mydict)