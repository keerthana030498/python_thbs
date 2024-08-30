String = "keerthana"
vowels = "aeiouAEIOU"

my_dic = dict()

for char in String:
     if char in vowels:
         if char in my_dic:
            my_dic[char] += 1
         else:
             my_dic[char] = 1
print(my_dic)