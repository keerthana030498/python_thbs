String = "Remove. punctuations @from a% given string?"
result = ""
for char in String:
    if char.isalnum() or char == " ":
        result += char
print(result)

