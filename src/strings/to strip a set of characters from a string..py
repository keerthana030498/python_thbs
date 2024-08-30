String = "Tutor Joes Computer Education"
vowels = "aeioAEIOU"
result = ""
for i in String:
    if i not in vowels:
        result = result + i
    else:
        result = result + " "
print(result)