string1 = "Heart"
string2 = "eartH"


string_sort = sorted(string1.lower())
string2_sort =sorted(string2.lower())

if string_sort == string2_sort:
    print("annagram")
else:
    print("not anagram")

