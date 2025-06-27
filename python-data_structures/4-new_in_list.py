#!/usr/bin/python3
def newInList(myList, idx, element):
    if idx < 0 or idx >= len(myList):
        return myList
    newList = myList.copy()
    newList[idx] = element
    return newList