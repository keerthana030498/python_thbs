Text = "Tutor Joes"
vowels = 'aeiouAEIOU'
count = 0
for char in Text:
    if char in vowels:
        print(char,end = " ")
        count += 1
print(count)