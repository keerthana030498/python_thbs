import json

json_string = {
    "name": "keer",
    "age": 26,
    "email": "keerthana.va@gmail.com",
    "address": {
        "street": "nagarbhavi",
        "city": "bangalore"
    },
    "phonenumbers": [
        {
            "type": "home",
            "number": "9399393"
        },
        {
            "type": "work",
            "number": "9393349393"
        }
    ],
    "is_Active": "true"
}

#print(json_string['phonenumbers'][0]["type"])
value = json_string
Key = input("enter the key valye")
value = value.get(Key)
print(value)
