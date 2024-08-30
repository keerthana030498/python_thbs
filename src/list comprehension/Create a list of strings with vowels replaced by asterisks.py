lst = ['apple', 'banana', 'cherry']
vowels = "aeiouAEIOU"

vowel = [''.join("*" if char in vowels else char for char in words )for words in lst]
print(vowel)