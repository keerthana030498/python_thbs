String = "Computer Education"
afteroddindex = String[0:-1:2]
print(afteroddindex)


result = ""
for i in range(len(String)):
    if i %2 == 0:
        result = result + String[i]
print(result)
