nth = int(input("enter the number of terms"))
n1,n2 = 0,1

for i in range (nth):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth


