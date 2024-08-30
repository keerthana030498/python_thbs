num = 4

digits = str(num)
digitlen = len(digits)
sum = 0
for i in digits:
    sum += int(i) ** digitlen

if sum == num:
    print("its amstrong num")
else:
    print("not a amstrong num")