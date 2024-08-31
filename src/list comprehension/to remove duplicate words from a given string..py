String = "Python Exercises Practice Solution Exercises"
String = String.split()
result = ""
for word in String:
    if word not in result:
        result += " " + word
print(result)
