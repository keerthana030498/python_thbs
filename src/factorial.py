def fact(num):
    if num == 0:
        return 1
    else:
        for i in range(num):
            res = num * fact(num - 1)
        return res


num = 4
result = fact(num)
print(f"factorial is {result}")
