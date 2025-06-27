#!/usr/bin/python3
def add_tuple(tupleA=(), tupleB=()):

    tupleA = tupleA + (0, 0)
    tupleB = tupleB + (0, 0)

    return (tupleA[0] + tupleB[0], tupleA[1] + tupleB[1])