s = "String and String Function"
remove_duplicate = ""
for char in s:
    if char not in remove_duplicate:
        remove_duplicate += char
print(remove_duplicate)
