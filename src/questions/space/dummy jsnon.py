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


dat = json_string
keys = input("enter the keys required to get its value")
keys_list = keys.split('.')
print(keys_list)

for key in keys_list:
    if key.isdigit():
        key = int(key)
    dat = dat[key]
print(dat)