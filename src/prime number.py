def isprime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
num = 12
if isprime(num):
    print("its is a primenumber")
else:
    print("its not a primenumber")


