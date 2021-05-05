"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
"""


def disemvowel(string_):
    vowel = lambda x: True if x not in 'aeiouAEIOU' else False
    return ''.join(filter(vowel, string_))


"""
Other solutions:

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
"""