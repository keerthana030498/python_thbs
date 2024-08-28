String = "keerthana"
vowels = "aeiouAEIOU"
count = 0
my_dic = dict()

for char in String:
     if char in vowels:
         count +=1
         my_dic[char] = count
print(my_dic)