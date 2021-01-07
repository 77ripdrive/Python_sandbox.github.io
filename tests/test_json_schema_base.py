import logging

import pytest
from jsonschema import Draft7Validator

LOGGER = logging.getLogger(__name__)


@pytest.mark.jsonValidation
def test_using_csv_with_different_fields(set_schema, set_base_payload):
    result = Draft7Validator(set_schema).is_valid(set_base_payload)
    assert result == True, LOGGER.info("Schema is valid")
