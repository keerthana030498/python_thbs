sentence = input("enter the sentence")
mydict = dict()
count = 0
for char in sentence:
    if char == " " or char == ",":
        count += 1
        mydict[char] = count
print(mydict)
