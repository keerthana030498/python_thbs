string1 = "Baa credit"
string2 = "Debit cara"

s1 = string1.lower().replace(" ", "")
s2 = string2.lower().replace(" ", "")

count1 = {}
count2 = {}
for char in s1:
    if char in count1:
        count1[char] += 1
    else:
        count1[char] = 1

for char in s2:
    if char in count2:
        count2[char] += 1
    else:
        count2[char] = 1
print(f"count1 = {count1}")
print(f"count2 = {count2}")
if count1 == count2:
    print("anagram")
else:
    print("not anagram")
