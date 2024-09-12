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


keys = input("enter the input :::")
key_list = keys.split('.')
print(key_list)
value = json_string
for k in key_list:
    if k.isdigit():
        k = int(k)
    value = value[k]
print(value)
