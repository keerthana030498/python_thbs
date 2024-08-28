String1 = "keerthana"
mydict = dict()

for char in String1:
    if char in mydict:
        mydict[char] += 1  # Increment the count if the character is already in the dictionary
    else:
        mydict[char] = 1  # Initialize the count if the character is not in the dictionary

print(mydict)