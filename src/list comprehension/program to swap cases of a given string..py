String = "Tutor Joes Computer Education"
result = ""
for char in String:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)