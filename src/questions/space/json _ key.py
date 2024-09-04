import json

json_string = {
    "name": "keer",
    "age": 26,
    "email": "keerthana.va@gmail.com",
    "address": {
        "street": "nagarbhavi",
        "city": "bangalore"
    },
    "country": {
        "street": "mysore",
        "place": "india"
    },
    "phonenumbers": [
        {
            "type": "home",
            "number": "9399393"
        },
        {
            "loc": "work",
            "num": "9393349393"
        }
    ],
    "is_Active": "true"
}

#print(json_string['phonenumbers'][0]["type"])

Key = input("enter the key valye")
#Value = json_string[key]
#print(value)
value = json_string
keys = Key.split('.')
print(f"keys are {keys}")
for key in keys:
    if key.isdigit():
        key = int(key)
    value = value[key]
print(value)
