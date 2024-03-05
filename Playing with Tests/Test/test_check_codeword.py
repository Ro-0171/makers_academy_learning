from lib.check_codeword import *

"""
If the codeword is correct
Returns 'Correct! Come in.'
"""
def test_if_codeword_given_is_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

"""
If the codeword is wrong
Returns 'WRONG!'
"""

def test_with_incorrect_codeword():
    result = check_codeword('water')
    assert result == 'WRONG!'

"""
If the codeword has the right first and last letter
Returns 'Close, but nope.'
"""

def test_with_close_codeword():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

"""
If the codeword has the right first letter and wrong last letter
Returns 'WRONG!'
"""

def test_with_mistakenly_close_codeword():
    result = check_codeword('hat')
    assert result == 'WRONG!'

"""
If the codeword has the wrong first letter and the right last letter
Returns 'WRONG!'
"""
def test_with_mistakenly_close_codeword():
    result = check_codeword('mouse')
    assert result == 'WRONG!'




