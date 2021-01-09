import allure
import pytest
from jsonschema import Draft7Validator


@allure.feature("Jsonschema validation")
@allure.story("Validation with correct payload value")
@pytest.mark.jsonValidation
def test_using_csv_with_different_fields(set_schema, set_base_payload):
    with allure.step("Validation with correct  JsonSchema"):
        result = Draft7Validator(set_schema).is_valid(set_base_payload)
        assert result == True
