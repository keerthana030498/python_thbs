def reverse_4(str1):
    lenght_str = len(str1)
    if lenght_str % 4 == 0:
        str1 = str1[::-1]
        return str1
    else:
        return str1


result = (reverse_4("science"))
print(result)