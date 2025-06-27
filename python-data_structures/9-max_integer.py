#!/usr/bin/python3
def max_integer(myList=[]):

    if len(myList) == 0:
        return None
    else:
        maxInt = myList[0]
        for i in myList:
            if i > maxInt:
                maxInt = i
        return maxInt