def sumfun(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


arr = [1,2,3,4,5]
result = sumfun(arr)
print(result)