import json

json_data = '''{
    "name": "Carol",
    "age": 40,
    "email": "carol@example.com",
    "address": [
        {
            "city": "Metropolis",
            "zip": "54321"
        },
        {
            "city": "polis",
            "zip": "543210"
        }
    ]
}'''

data = json.loads(json_data)

def key_value(data, key_input):
    value = data
    key_list = key_input.split(".")

    try:
        for k in key_list:
            if k.isdigit():
                k = int(k)
            value = value[k]
        return value
    except KeyError:
        return "key not found"

key_input = input("enter the input:")
result = key_value(data,key_input)
print(result)