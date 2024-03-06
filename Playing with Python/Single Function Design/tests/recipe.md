# Check for #TODO in text recipe

## Describe the Problem

>   As a user
>   So that I can keep track of my tasks
>   I want to check if a text includes the string #TODO.

## Design the Function Signature
"""
Check if the string #TODO is in any given text
"""
def check_for_todo(text):

    Parameters:
    text: a string containing a text.
    
    Returns:
    It will return true if the text contains #TODO (Bool)


## Create Examples as Tests
Running different strings with #TODO and without #TODO including some which have TODO with # and also lower case


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
assert check_for_todo == True






## Implement the Behaviour