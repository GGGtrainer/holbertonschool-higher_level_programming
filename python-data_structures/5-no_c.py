#!/usr/bin/python3
def no_c(myString):
    newString = ""
    for char in myString:
        if char != 'c' and char != 'C':
            newString += char
    return newString