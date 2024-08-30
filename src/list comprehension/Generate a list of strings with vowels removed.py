lst = ['apple', 'banana', 'cherry']
vowels = "aeiouAEIOU"
vowels_Removed = [''.join(char for char in word if char not in vowels) for word in lst ]
print(vowels_Removed)