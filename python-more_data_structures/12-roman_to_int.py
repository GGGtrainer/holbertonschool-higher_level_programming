#!/usr/bin/python3
def roman_to_int(s):
    if not isinstance(s, str):
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for char in s:
        value = roman_numerals.get(char, 0)
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total