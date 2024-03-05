from lib.report_length import *

def test_report_length():
    result = report_length('Hello')
    assert result == f'This string is {5} charcters long.'

def test_report_another_length():
    result = report_length('Goodbye')
    assert result == f'This string is {7} charcters long.'

def test_long_word_length():
    result = report_length('Incomprehensible')
    assert result == f'This string is {16} charcters long.'

