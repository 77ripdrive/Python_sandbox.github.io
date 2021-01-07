import json
import logging
import os

import allure
import pytest
from jsonschema import ValidationError
from jsonschema import validate

LOGGER = logging.getLogger(__name__)
path_json_schema_file = os.getcwd() + "/asset/schema_first.json"


def get_data_from_json_schema(path):
    with open(path, "r") as schema_file:
        return json.load(schema_file)


@allure.feature("Jsonschema validation")
@allure.story("Validation with incorrect value")
@pytest.mark.jsonValidation
@pytest.mark.parametrize(
    "productId,productName,price,tags",
    [(2, "apple", "two", ["green", "grey"]), ("one", "banana", 30, []), (4, "one", 20, "green")],
)
def test_using_csv_with_different_fields_negative(productId, productName, price, tags):
    payload = {"productId": None, "productName": None, "productPrice": None, "tags": None}
    with allure.step("insert nit correct value "):
        payload.update({"productId": productId})
        payload.update({"productName": productName})
        payload.update({"productPrice": price})
        payload.update({"tags": tags})
        schema = get_data_from_json_schema(path_json_schema_file)
        with allure.step("Validation with base JsonSchema"):
            with pytest.raises(ValidationError) as e:
                validate(payload, schema=schema)
                assert e.value.__module__.strip("ValidationError") == "jsonschema.exceptions"
                LOGGER.info(e.value)
