#!/usr/bin/python3
def print_reversed_list_integer(myList=[]):

    if myList is None:
        return
    for num in reversed(myList):
        print("{:d}".format(num))