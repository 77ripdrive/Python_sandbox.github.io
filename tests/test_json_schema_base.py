import csv
import json

import pytest
from jsonschema import Draft7Validator

path_to_test_data_csv_file = "../asset/data_file.csv"
path_json_schema_file = "../asset/schema_first.json"


def read_test_data_from_csv(path):
    test_data = []
    with open(path, newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)
        for row in data:
            test_data.append(row)
            return test_data


def get_data_from_json_schema(path):
    with open(path, "r") as schema_file:
        return json.load(schema_file)


payload = {"productId": 1, "productName": "A green door", "price": 12.50, "tags": ["home", "green"]}


def test_using_csv_with_different_fields():
    with open("../asset/schema_first.json", "r") as schema_file:
        schema = json.load(schema_file)
    result = Draft7Validator(schema).is_valid(payload)
    print(result)
    assert result == True


@pytest.mark.skip
@pytest.mark.parametrize("productId,productName,price,tags", read_test_data_from_csv(path_to_test_data_csv_file))
def test_using_csv_with_different_fields_negative(productId, productName, price, tags):
    schema = get_data_from_json_schema(path_json_schema_file)
    payload.update({"productId": productId})
    payload.update({"productName": productName})
    payload.update({"price": price})
    payload.update({"tags": tags})
    print(payload)
    result = Draft7Validator(schema).is_valid(payload)
    assert result == True
