s = "Hello world ! Hello Tutor Joes"
words = s.split()
result = set()
for word in words:
    if word in result:
        print(word)
    else:
        result.add(word)
