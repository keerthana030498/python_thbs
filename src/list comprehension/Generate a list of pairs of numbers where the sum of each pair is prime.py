def isprime(number):
    if number <=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

primenum = [(x,y) for x in range(1,11) for y in range(1,11) if isprime(x+y)]
print(primenum)