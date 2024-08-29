level = int(input("enter the level"))
num =1
for i in range(0,level):
    for j in range(0,i+1):
        print(num ,end = " ")
        num = num + 1
    print()