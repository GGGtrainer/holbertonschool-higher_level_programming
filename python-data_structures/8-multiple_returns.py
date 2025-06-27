#!/usr/bin/python3
def multipleReturns(sentence):

    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])