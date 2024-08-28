import itertools

strng = "abc"
permutation = itertools.permutations(strng)
for perm in permutation:
    print(''.join(perm))

