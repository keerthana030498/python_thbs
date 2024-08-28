string1= "keerthanahhdjdj"
mydict = dict()
count = 0
for char in string1:
    String_count = string1.count(char)
    if String_count > 1:
        count += 1
        mydict[char] = String_count
print(mydict)