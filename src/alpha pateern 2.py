level = int(input("enter the level"))

num = 65

for i in range(0,level):
    for j in range(0,i+1):
        ch = chr(num)
        print(ch,end=" ")
    num = num +1
    print()