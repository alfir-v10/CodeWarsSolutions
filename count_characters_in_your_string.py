"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    res = {}
    for letter in string:
        if letter not in res.keys():
            res[letter] = 1
        else:
            res[letter] += 1
    return res
