#!/usr/bin/python3
def elementAt(myList, idx):
    if idx < 0 or idx >= len(myList):
        return None
    return myList[idx]