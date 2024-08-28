str1 = "P@#yn26at^&i5ve"
count_alpa = 0
count_digit = 0
count_symbols = 0
for char in str1:
    if char.isalpha():
        count_alpa += 1
    elif char.isdigit():
        count_digit += 1
    else:
        count_symbols +=1
print(f"alpha = {count_alpa},digits = {count_digit}, symbols = {count_symbols}")
