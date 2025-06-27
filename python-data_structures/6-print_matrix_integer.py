#!/usr/bin/python3
def printMatrixInteger(matrix=[[]]):

    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))