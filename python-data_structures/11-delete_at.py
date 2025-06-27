#!/usr/bin/python3
def delete_at(myList=[], idx=0):

    if idx < 0 or idx >= len(myList):
        return myList
    del myList[idx]
    return myList