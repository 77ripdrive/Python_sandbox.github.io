import jsonpath
import requests
from pytest_bdd import given
from pytest_bdd import parsers
from pytest_bdd import scenarios
from pytest_bdd import then

from config import BASE_URL_ZIPPOPO

CONVERTERS = {"country_code": str, "zip_code": int, "place_name": str}

scenarios("../features/zippopo.feature", example_converters=CONVERTERS)


@given('the Zippopotam API is queried with "<country_code>" and "<zip_code>"', target_fixture="ddg_response")
def ddg_response(country_code, zip_code):
    response = requests.get(f"{BASE_URL_ZIPPOPO}/{country_code}/{zip_code}")
    return response


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code


@then('the response contains results for "<place_name>"')
def ddg_response_contents(ddg_response, place_name):
    results = jsonpath.jsonpath(ddg_response.json(), "$..places[0].place name")[0]
    assert place_name == results
