import csv
import json
import os

import pytest
import requests
from jsonschema import validate, ValidationError


def read_path_to_file(file_name):
    current_dir = os.getcwd()
    return current_dir + "\\" + file_name


path_to_test_data_csv_file = read_path_to_file('data_file.csv')
path_json_schema_file = read_path_to_file('schema_first.json')
base_url = 'http://base.url/'


def read_test_data_from_csv(path_to_test_data_csv_file):
    test_data = []
    with open(path_to_test_data_csv_file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)
        for row in data:
            test_data.append(row)
            return test_data


def read_data_from_json_schema_example(path_json_schema_file):
    file = open(path_json_schema_file, 'r')
    return json.loads(file.read())


# очень приблизит
@pytest.mark.parametrize("value_1, value_2", path_to_test_data_csv_file)
def test_using_csv_with_different_fields_negative(value_1, value_2):
    payload = {'id': value_1, 'address': value_2}
    response = requests.post(base_url, params=payload)
    response_body = response.json()
    with pytest.raises(ValidationError) as e:
        validate(instance=response_body, schema=read_data_from_json_schema_example(path_json_schema_file))
    assert 'ValidationError' in str(e.value)


payload_1 = {
    "id": 2,
    "category": {
        "id": 2,
        "name": "string"
    },
    "name": "Jack",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

endpoint = "https://petstore.swagger.io/v2/pet"

json_schema = {
    "id": int,
    "category": {
        "id": int,
        "name": "string"
    },
    "name": "string",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": int,
            "name": "string"
        }
    ],
    "status": "available"
}


# def test_using_csv_with_different_fields():
#     payload = payload_1
#     response = requests.post(endpoint, params=payload)
#     response_body = response.json()
#     # result_1 = validate(instance=response_body, schema=json_schema)
#     # print("Result "+ result_1)
#     print(response_body)
#     assert validate(instance=response_body, schema=json_schema) == None
