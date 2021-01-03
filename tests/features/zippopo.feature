Feature: Zippopo Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API,
  So that my app can get answers anywhere.


  Scenario Outline: Basic ZIP search
    Given the Zippopotam API is queried with "<country_code>" and "<zip_code>"
    Then the response status code is "200"
    Then the response contains results for "<place_name>"

    Examples:
      | country_code | zip_code | place_name                 |
      | us           | 12345    | Schenectady                |
      | nl           | 3825     | Vathorst                   |
