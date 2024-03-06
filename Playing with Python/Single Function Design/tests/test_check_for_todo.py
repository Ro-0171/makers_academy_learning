from lib.check_for_todo import *

def test_check_for_todo():
    text = "There are things #TODO"
    assert check_for_todo(text) == True

    text = "There are things #todo"
    assert check_for_todo(text) == False

    text = "There are things TODO"
    assert check_for_todo(text) == False

    text = "There are no things #TODO"
    assert check_for_todo(text) == True

    text = "There are no things to do"
    assert check_for_todo(text) == False

    text = "Much #TODO"
    assert check_for_todo(text) == True


    