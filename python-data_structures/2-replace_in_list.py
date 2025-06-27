#!/usr/bin/python3
def replaceInList(myList, idx, element):
    if idx < 0 or idx >= len(myList):
        return myList
    myList[idx] = element
    return myList