"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
 You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
starting with the leftmost digit and skipping any 0s.
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

"""


def solution(roman):
    roman_set = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, ' ': 0}
    count = 0
    roman += ' '
    print(roman)
    if len(roman) == 1:
        return roman_set[roman[0]]
    for i in range(len(roman)):
        if roman_set[roman[i]] > roman_set[roman[i-1]] and i != 0:
            count -= roman_set[roman[i - 1]]
            count += roman_set[roman[i]] - roman_set[roman[i-1]]
        else:
            count += roman_set[roman[i]]
    return count
