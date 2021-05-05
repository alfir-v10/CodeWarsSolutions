"""
Basic regex tasks. Write a function that takes in a numeric code of any length.
The function should check if the code begins with 1, 2, or 3 and return true if so.
Return false otherwise.

You can assume the input will always be a number.
"""


def validate_code(code):
    first_digit = str(code)[0]
    return first_digit in '123'


"""
Other solution:

def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

def validate_code(code):
    import re
    return bool(re.match('[123]',str(code)))

validate_code = lambda c: str(c)[0] in "123"
"""