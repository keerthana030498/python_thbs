s = "Hell0 W0rld ! 123 * #"
upper_count=0
lower_count=0
digit_count=0
special_count = 0
s = s.replace(" ","")
for char in s:
    if char.isdigit():
        digit_count +=1
    elif char.isupper():
        upper_count +=1
    elif char.islower():
        lower_count +=1
    else:
        special_count += 1
print(f"digit case = {digit_count}")
print(f"upper case = {upper_count}")
print(f"lower case = {lower_count}")
print(f"special case = {special_count}")





#without functions
s1 = "Hell0 W0rld ! 123 * #"
upper_count1=0
lower_count1=0
digit_count1=0
special_count1 = 0
s1 = s1.replace(" ","")
for char in range(len(s1)):
    if s1[char] >='0' and s1[char] <= '9':
        digit_count1 +=1
    elif s1[char]>='A' and s1[char] <= 'Z':
        upper_count1 +=1
    elif s1[char]>='a' and s1[char] <= 'z':
        lower_count1 +=1
    else:
        special_count1 += 1
print(f"digit case = {digit_count1}")
print(f"upper case = {upper_count1}")
print(f"lower case = {lower_count1}")
print(f"special case = {special_count1}")


