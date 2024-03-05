import pytest
from lib.present import *

"""
When we wrap an item
We get it back when unwrapping
"""
def test_wrap_then_unwrap():
    present = Present()
    present.wrap(30)
    assert present.unwrap() == 30

"""
If we unwrap before wrapping
Error message
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

"""
If we wrap a present which has already been wrapped
Error message
"""

def test_wrapped_already():
    present = Present()
    present.wrap(45)
    with pytest.raises(Exception) as err:
        present.wrap(60)
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

"""
If we try to wrap an already wrapped present 
First wrapped value is unchanged
"""

def test_wrapping_already_preserves_value():
    present = Present()
    present.wrap(45)
    with pytest.raises(Exception) as err:
        present.wrap(60)
    assert present.unwrap() == 45