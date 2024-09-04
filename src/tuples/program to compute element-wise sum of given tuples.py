A = (2, 5, 8)

B = (6, 5, 1)

C = (1, 4, 7)

D = (3, 7, 2)

print(tuple(map(sum,zip(A,B,C,D))))

sums= []
for i in range(len(A)):
    total = A[i]+B[i]+C[i]+D[i]
    sums.append(total)
print(tuple(sums))