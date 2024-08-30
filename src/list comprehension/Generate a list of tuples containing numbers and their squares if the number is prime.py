def isprime(number):
    if number <= 1:
         return  False
    for i in range (2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

prime_number_square = [(num, num ** 2) for num in range(1,11) if isprime(num)]
print(prime_number_square)