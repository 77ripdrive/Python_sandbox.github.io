Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.


  Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples:
      | initial | some | total |
      | 0       | 3    | 3     |
      | 3       | 4    | 7     |
      | 7       | 5    | 12    |


  Scenario Outline: Remove cucumbers from the basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are removed from the basket
    Then the basket contains "<total>" cucumbers

    Examples:
      | initial | some | total |
      | 8       | 3    | 5     |
      | 5       | 4    | 1     |
      | 1       | 1    | 0     |
