num = int(input("enter the num"))
orginal_num = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if orginal_num == rev:
    print("palindrome")
else:
    print("not palindrome")
