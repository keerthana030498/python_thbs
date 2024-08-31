Strings = "Tutor Joes Computer Education"

Strings = Strings.split()
small = Strings[0]
largest = Strings[0]
for char in Strings:
    if len(char) < len(small):
        small = char
    if len(char) > len(largest):
        largest = char
print(f"smalelst is = {small}")
print(f"largest is = {largest}")