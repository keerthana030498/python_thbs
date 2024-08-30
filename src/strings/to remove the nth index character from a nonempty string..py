s = "Tutor Joes"
s = s.replace("t","")
print(s)



def remove(str1, num):
    s1 = str1[:num]
    s2 = str1[num+1:]
    return s1 + s2

result = remove("keerthana",4)
print(result)
