lst = [-2, 3, -5, 7, -11]

signs = [(x,"postive") if x > 0 else (x,"negative") for x in lst]
print(signs)