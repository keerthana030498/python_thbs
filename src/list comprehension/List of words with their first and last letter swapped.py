lst = ['apple', 'banana', 'cherry', 'date']

rev = [char[-1]+ char[1:-1]+char[0] for char in lst]
print(rev)