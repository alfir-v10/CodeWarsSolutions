"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
 For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
 because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""

import string


def is_pangram(s):
    count = 0
    for letter in string.ascii_lowercase:
        if letter in s.lower():
            count += 1
    if count == len(string.ascii_uppercase):
        return True
    return False


"""
Other solutions:

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
    
    
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
"""