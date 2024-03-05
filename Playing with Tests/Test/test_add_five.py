from lib.add_five import *
def test_if_given_three_returns_eight():
    result = add_five(3)
    assert result == 8

def test_if_given_five_returns_ten():
    result = add_five(5)
    assert result == 10