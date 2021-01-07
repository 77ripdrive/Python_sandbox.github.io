import csv
import json
import os

import pytest

path_json_schema_file = os.getcwd() + "/asset/schema_first.json"


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


# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step failed: {step}")
    print(f"Request failed: {request}")


@pytest.fixture(scope="session")
def set_base_payload():
    payload = {"productId": 1, "productName": "A green door", "productPrice": 12.50, "tags": ["home", "green"]}
    return payload


@pytest.fixture(scope="session")
def set_schema():
    schema = get_data_from_json_schema(path_json_schema_file)
    return schema
