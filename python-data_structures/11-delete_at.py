#!/usr/bin/python3
def deleteAt(myList=[], idx=0):

    if idx < 0 or idx >= len(myList):
        return myList
    del myList[idx]
    return myList