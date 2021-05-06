"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010)
and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter.
When writing on Twitter, he is known for almost always capitalizing every word.
For simplicity, you'll have to capitalize each word, check out how contractions are expected to be
in the example below.
Your task is to convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally
typed them.
Example:
    Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
    Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
    Link to Jaden's former Twitter account @officialjaden via archive.org
"""


def to_jaden_case(string):
    s = string.capitalize()
    i = 0
    x = []
    for i in range(len(s)):
        if s[i] != ' ':
            x.append(s[i])
        elif s[i] == ' ':
            x.append(s[i])
            s1 = s[i + 1]
            s1 = s1.capitalize()
            x.append(s1)
            i += 1
        i += 1
        a = ''
        for k in x:
            a = str(a) + str(k)
    return a
