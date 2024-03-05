from lib.stringbuilder import *

"""
Start with an empty string
"""
def test_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

"""
When adding a single string, the output is now that string
"""
def test_adding_string_outputs_a_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

"""
When we add a single string, this reflects the size of that string
"""
def test_adding_string_sets_size_to_string_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

"""
When adding multiple strings
The output is those strings concatenated. 
"""

def test_adding_strings_is_concatenated():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world!")
    assert string_builder.output() == "hello world!"

"""
When adding multiple strings
The outcome is the total of the strings added
"""
def test_total_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world!")
    assert string_builder.size() == 12
