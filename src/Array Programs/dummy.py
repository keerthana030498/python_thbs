def vowels_to_upper(String):
    mydict = dict()
    for char in String:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1

max_freq = 0
for char, count in mydict.items():
    if count > max_freq:

vowels_to_upper("Keerthana")
