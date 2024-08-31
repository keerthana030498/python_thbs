String = "AAAABBBBCCCC"
org = ""

for char in String:
    if char not in org:
        org += char
print(org)