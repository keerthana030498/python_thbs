numbers = [1, 2, 3, 4, 5]
square_list = []

for num in numbers:
    num = num * 2
    square_list.append(num)
print(square_list)



#list comprehension

square_list_com = [num * 2 for num in numbers]
print(square_list_com)