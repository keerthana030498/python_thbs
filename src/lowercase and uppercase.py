str1 = "PyNaTive"
lowercase_chars = ""
uppercase_chars = ""
for char in str1:
    if char.islower():
        lowercase_chars += char
    elif char.isupper():
        uppercase_chars += char
print(lowercase_chars + uppercase_chars)

