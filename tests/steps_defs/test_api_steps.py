import requests
from pytest_bdd import given
from pytest_bdd import parsers
from pytest_bdd import scenarios
from pytest_bdd import then

# Shared Variables
from config import DUCKDUCKGO_API

# Scenarios


scenarios("../features/api.feature", example_converters=dict(phrase=str))


# Given Steps


@given('the DuckDuckGo API is queried with "<phrase>"', target_fixture="ddg_response")
def ddg_response(phrase):
    params = {"q": phrase, "format": "json"}
    response = requests.get({DUCKDUCKGO_API}, params=params)
    return response


# Then Steps


@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()["Heading"].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code
