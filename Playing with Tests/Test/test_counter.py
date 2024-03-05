from lib.counter import *

"""
Reports a count of zero
"""
def test_count_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
Adds a number to the counter, shown in final count
"""
def adds_a_number_to_count():
    count.add(23)
    assert counter.report() == "Counted to 23 so far."

"""
Add multiple numbers to counter, sum of numbers is final count
"""
def final_count():
    counter.add(23)
    counter.add(32)
    assert counter.report() == "Counted to 55 so far."
