lst = [1, 2, 2, 3, 4, 4, 4, 5]
frequency ={num : lst.count(num) for num in set(lst)}
print(frequency)