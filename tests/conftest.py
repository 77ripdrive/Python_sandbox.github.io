import pytest

from tests.utils.utils import read_data_from_json_file


# bdd hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step failed: {step}")
    print(f"Request failed: {request}")


@pytest.fixture(scope="session")
def set_base_payload():
    payload = {"productId": 1, "productName": "A green door", "productPrice": 12.50, "tags": ["home", "green"]}
    yield payload


@pytest.fixture(scope="session")
def set_schema():
    schema = read_data_from_json_file("schema_first.json")
    yield schema
