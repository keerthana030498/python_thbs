import json

# JSON data as a string
json_string = '''
{
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
'''

# Convert JSON string to Python dictionary
data = json.loads(json_string)


# Function to find all paths with the target value
def find_value_paths(data, target_value, path=""):
    paths = []

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}/{key}" if path else key
            if value == target_value:
                paths.append(current_path)
            else:
                paths.extend(find_value_paths(value, target_value, current_path))

    elif isinstance(data, list):
        for index, item in enumerate(data):
            current_path = f"{path}[{index}]"
            if item == target_value:
                paths.append(current_path)
            else:
                paths.extend(find_value_paths(item, target_value, current_path))

    return paths


# Get the target value from user input
target_value = input("Enter the value: ")

# Find all paths to the target value
result_paths = find_value_paths(data, target_value)

# Print the results
print(f"Paths to the value '{target_value}':")
for path in result_paths:
    print(path)
