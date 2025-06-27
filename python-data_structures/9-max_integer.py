#!/usr/bin/python3
def maxInteger(myList=[]):

    if len(myList) == 0:
        return None
    else:
        maxInt = myList[0]
        for i in myList:
            if i > maxInt:
                maxInt = i
        return maxInt