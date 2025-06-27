#!/usr/bin/python3
def printReversedListInt(myList=[]):

    if myList is None:
        return
    for num in reversed(myList):
        print("{:d}".format(num))