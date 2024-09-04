import json

json_string = '''{
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
}'''

data = json.loads(json_string)


name = data["name"]
street = data["address"]["street"]
homenum = data["phonenumbers"][0]["number"]

print(f"name is {name},steet is {street},homenum is {homenum}")