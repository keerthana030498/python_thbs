def exponent(base,exp):
    result = 1
    for i in range(exp):
        result = base ** exp
    return result

final_result = exponent(2,5)
print (final_result)
