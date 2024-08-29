def coomon(list_a,list_b):
    unique_list = []
    for i in list_a:
        if i in list_b:
            unique_list.append(i)
    return unique_list

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common_elements = coomon(list_a,list_b)
print(common_elements)



list_c = [1, 2, 3, 4, 5]
list_d = [4, 5, 6, 7, 8]

comon_ele = list(set(list_c) & set(list_d))
print(comon_ele)

seta = set(list_c)
setb = set(list_d)
intersection = seta.intersection(setb)
print(list(intersection))


