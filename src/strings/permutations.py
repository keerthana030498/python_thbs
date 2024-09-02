#import itertools

#strng = "abc"
#permutation = itertools.permutations(strng)
#for perm in permutation:
    #print(''.join(perm))

#recurise method


def get_permuatiations(String, i=0):
    if i == len(String):
        print("".join(String))
    for j in range(i,len(String)):
        words = [c for c in String]
        words[i],words[j] = words[j],words[i]
        get_permuatiations(words,i+1)
print(get_permuatiations("yup"))

