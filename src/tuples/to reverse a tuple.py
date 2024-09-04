t = ( 23, 45, 67, 78, 89, 90, 34, 56 )
rev = ()

for i in t:
    rev= (i,)+rev

print(rev)

reverse = t[::-1]
print(reverse)
