a= 20
b =100

smaller = min(a,b)

for i in range(smaller,0,-1):
    if a%i == 0 and b%i ==0:
        print(i)
