from dataclasses import dataclass

import pytest
from assertpy import assert_that
from cerberus import Validator


@dataclass
class Person:
    name: str
    age: int


class PersonValidator(Validator):
    def validate_person(self, obj):
        return self.validate(obj.__dict__)


schema = {"name": {"type": "string", "minlength": 2}, "age": {"type": "integer", "min": 18, "max": 65}}


@pytest.mark.json_validation_cerberus
def test_cerberus_validator_base(set_schema, set_base_payload):
    v = PersonValidator(schema)
    person = Person("John Doe", 20)
    result = v.validate_person(person)
    assert_that(result, description=v.errors).is_true()


@pytest.mark.json_validation_cerberus
def test_cerberus_validator_negative(set_schema, set_base_payload):
    v = PersonValidator(schema)
    children = Person("Zoe Doe", 2)
    result = v.validate_person(children)
    assert_that(result, description=v.errors).is_false()
