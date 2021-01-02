import json

schema = {
    "id": "int",
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": "int"
}


def builder_for_json(dict):
    items = sorted(dict.items(), key=lambda item: item[0])
    values = [item[1] for item in items]
    json_dict = json.dumps(values)
    return json_dict


print(builder_for_json(schema))
