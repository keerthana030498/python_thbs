myDict = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}

mykeys = list(myDict.keys())
mykeys.sort()
print(f'keys sorted',mykeys)
soreteddict = {i:myDict[i] for i in mykeys}
print(soreteddict)

