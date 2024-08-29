sentence = "Calculate Square Root"
words = sentence.split()
max_lenght = 0
for char in words:
    if len(char) > max_lenght:
        max_lenght = len(char)
print(max_lenght)