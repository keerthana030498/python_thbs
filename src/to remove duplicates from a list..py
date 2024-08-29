def remove_duplicate(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

lst = [10,20,40,20,20, 40]
un_lst = remove_duplicate(lst)
print(un_lst)
