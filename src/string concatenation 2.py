s1 = "America"
s2 = "Japan"


s1_mi = len(s1)//2
s2_mi = len(s2)//2

s1_f = s1[0]
s2_f = s2[0]

s1_l = s1[-1]
s2_l = s2[-1]
res = s1_f + s2_f+ s1[s1_mi] + s2[s2_mi] + s1_l + s2_l

print(res)
