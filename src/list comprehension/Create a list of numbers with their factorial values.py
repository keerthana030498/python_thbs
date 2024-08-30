def fact(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num * fact(num-1)

lst = [2, 3, 4, 5]
factorial = [fact(x) for x in lst ]
print(factorial)