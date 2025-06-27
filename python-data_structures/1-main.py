#!/usr/bin/python3
elementAt = __import__('1-element_at').elementAt

myList = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, elementAt(myList, idx)))