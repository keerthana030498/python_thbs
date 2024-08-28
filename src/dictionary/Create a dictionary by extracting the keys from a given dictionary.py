sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

mydict ={}

for i in keys:
    mydict[i] = sample_dict[i]
print(mydict)